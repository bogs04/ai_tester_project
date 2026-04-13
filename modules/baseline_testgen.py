import os

class BaselineTestGenerator:
    def __init__(self, out_dir="data/testcases/baseline"):
        self.out_dir = out_dir
        os.makedirs(self.out_dir, exist_ok=True)

    def generate(self, dom_elements, url):
        # Giống với mock LLM, nhưng cố định 3 steps
        lines = [
            "from selenium import webdriver",
            "from selenium.webdriver.common.by import By",
            "import time",
            "",
            f'driver = webdriver.Chrome()',
            f'driver.get("{url}")',
            "time.sleep(1)",
            "",
            'print("STEP 1 - Check page title")',
            "try:",
            '    assert "Example Domain" in driver.title',
            '    print("PASS - step 1")',
            "except AssertionError:",
            '    print("FAIL - step 1")',
            "except Exception as e:",
            '    print("ERROR - step 1:", e)',
            "",
            'print("STEP 2 - Check H1")',
            "try:",
            '    h1 = driver.find_element(By.TAG_NAME, "h1")',
            '    if h1 and h1.text.strip():',
            '        print("PASS - step 2")',
            "    else:",
            '        print("FAIL - step 2")',
            "except Exception as e:",
            '    print("ERROR - step 2:", e)',
            "",
            'print("STEP 3 - Check paragraph")',
            "try:",
            '    p = driver.find_element(By.TAG_NAME, "p")',
            '    if p and p.text.strip():',
            '        print("PASS - step 3")',
            "    else:",
            '        print("FAIL - step 3")',
            "except Exception as e:",
            '    print("ERROR - step 3:", e)',
            "",
            "driver.quit()"
        ]
        return "\n".join(lines)
