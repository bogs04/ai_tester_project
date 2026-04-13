# modules_extra/autoscript_cleaner.py

def clean_steps(steps):
    cleaned = []
    seen = set()

    for step in steps:
        action = step.get("action", "").lower()

        target = step.get("target", {})
        by = target.get("by", "")
        value = target.get("value", "")

        signature = f"{action}:{by}:{value}"

        if signature in seen:
            continue
        seen.add(signature)

        # normalize
        step["action"] = action
        if "target" in step:
            if "by" in step["target"]:
                step["target"]["by"] = step["target"]["by"].lower()

        cleaned.append(step)

    return cleaned


def clean_script_file(input_path, output_path):
    import json

    with open(input_path, "r", encoding="utf-8") as f:
        steps = json.load(f)

    cleaned_steps = clean_steps(steps)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(cleaned_steps, f, indent=2)
