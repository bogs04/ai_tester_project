# modules_extra/structured_testgen.py
# RULE-BASED TEST GENERATOR (Baseline)

def generate_rule_tests(dom_elements, max_steps=10):
    """
    Sinh test case theo rule-based
    - Mỗi DOM element -> 1 step click đơn giản
    """
    steps = []

    for el in dom_elements[:max_steps]:
        step = {
            "action": "click",
            "locator_type": "id" if el.get("id") else "tag",
            "locator_value": el.get("id") or el.get("tag", "div"),
            "alternatives": []
        }
        steps.append(step)

    return steps
