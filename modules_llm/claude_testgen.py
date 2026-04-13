import json
from anthropic import Anthropic

client = Anthropic()

SYSTEM_PROMPT = """
You are an automated web UI testing agent.

You are given a list of DOM elements extracted from a real webpage.

Your task is to generate a DIVERSE and NON-REDUNDANT set of UI test steps.

Rules:
- Return ONLY a valid JSON array (no explanation, no markdown)
- Generate AT LEAST 10 and AT MOST 20 actions
- EACH action MUST reference a selector from the DOM
- DO NOT repeat the same selector unless absolutely necessary
- DO NOT repeat the same action type on the same selector
- Every action must be meaningfully different
- Prefer covering DIFFERENT page regions and element types
- Use diverse action types: click, input, verify, hover, navigate
- Do NOT hallucinate selectors

Each action must be an object with:
- "action": string
- "selector": string
"""

def generate_claude_tests(dom_elements):
    user_prompt = f"""
DOM Elements:
{json.dumps(dom_elements, indent=2)}

Generate UI test actions following the rules.
"""

    response = client.messages.create(
        model="claude-3-haiku-20240307",  # 💸 RẺ + ỔN
        system=SYSTEM_PROMPT,
        messages=[
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.2,
        max_tokens=1200,
    )

    raw = response.content[0].text.strip()

    try:
        actions = json.loads(raw)
    except Exception as e:
        raise RuntimeError(f"Failed to parse Claude output: {e}\nRaw:\n{raw}")

    if not isinstance(actions, list) or len(actions) < 10:
        raise RuntimeError(f"Too few actions ({len(actions)}). Expect >=10.")

    return actions
