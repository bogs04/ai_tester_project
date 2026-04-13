# modules/test_executor.py

import json
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from modules.dynamic_locator import find_element_safe

def run_test_script(script_path, log_path):
    """
    Chạy script test selenium từ file .py
    Ghi log chi tiết từng step
    """
    log = []
    # Đọc script (giả lập dạng list of steps)
    with open(script_path, "r", encoding="utf-8") as f:
        steps = json.load(f)  # script JSON: [{"action": "click", "locator_type": "id", "locator_value": "btn1", "alternatives": [...]}, ...]

    driver = webdriver.Chrome()
    driver.implicitly_wait(3)

    for i, step in enumerate(steps, 1):
        action = step.get("action")
        locator_type = step.get("locator_type")
        locator_value = step.get("locator_value")
        alternatives = step.get("alternatives", [])

        try:
            element = find_element_safe(driver, locator_type, locator_value, alternatives)
            if not element:
                log.append(f"Step {i} FAIL: element not found")
                continue

            if action == "click":
                element.click()
            elif action == "send_keys":
                element.send_keys(step.get("value", ""))
            else:
                log.append(f"Step {i} WARN: unknown action '{action}'")
                continue

            log.append(f"Step {i} PASS")
            time.sleep(0.1)  # small delay

        except Exception as e:
            log.append(f"Step {i} ERROR: {str(e)}")

    driver.quit()

    # Save log
    with open(log_path, "w", encoding="utf-8") as f:
        for line in log:
            f.write(line + "\n")
    
    return log


def evaluate_log(log_path, result_path):
    """
    Đọc log, tính tổng số bước, pass, fail, error
    Ghi kết quả ra JSON
    """
    with open(log_path, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    total_steps = len(lines)
    passed = sum(1 for l in lines if "PASS" in l)
    failed = sum(1 for l in lines if "FAIL" in l)
    errors = sum(1 for l in lines if "ERROR" in l)

    score = round(passed / total_steps * 100, 2) if total_steps else 0.0

    results = {
        "total_steps": total_steps,
        "passed": passed,
        "failed": failed,
        "errors": errors,
        "score": score
    }

    if result_path:
        with open(result_path, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2)

    return results

def mock_executor(locator_type, locator_value):
    """
    Giả lập Selenium:
    - locator chứa 'invalid' → fail
    - còn lại → pass
    """
    if "invalid" in locator_value:
        return False
    return True