# modules_extra/dynamic_executor.py
# Thực thi step với mô phỏng self-healing (không cần browser thật)

import random


def run_steps(steps):
    """
    steps: list[dict]
    mỗi step ví dụ:
    {
        "action": "click",
        "locator_type": "id",
        "locator_value": "submit",
        "alternatives": [
            {"locator_type": "name", "locator_value": "submit"},
            {"locator_type": "xpath", "locator_value": "//button"}
        ]
    }

    Return:
        passed_steps, error_steps
    """

    passed = 0
    errors = 0

    for step in steps:
        # --- mô phỏng xác suất fail ban đầu ---
        # giả lập DOM change / locator gãy
        success = random.random() > 0.25  # 75% pass trực tiếp

        if success:
            passed += 1
            continue

        # --- self-healing: thử alternatives ---
        healed = False
        for alt in step.get("alternatives", []):
            # giả lập thử locator khác
            if random.random() > 0.4:  
                healed = True
                break

        if healed:
            passed += 1
        else:
            errors += 1

    return passed, errors
