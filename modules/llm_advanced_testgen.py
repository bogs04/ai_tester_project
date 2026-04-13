# modules/llm_advanced_testgen.py
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

class PromptedLLMGenerator:
    """
    LLM Advanced Test Generator:
    - Sinh test case từ DOM elements.
    - Mỗi DOM element → 1 step.
    - Sử dụng Selenium + WebDriverWait để đảm bảo robust.
    """
    def __init__(self, out_dir="data/testcases/llm_advanced"):
        self.out_dir = out_dir
        os.makedirs(self.out_dir, exist_ok=True)

    def generate(self, dom_elements, url):
        """
        dom_elements: list of dict, mỗi dict chứa tag, id, class, text
        url: URL page
        return: Python test script string
        """
        lines = [
            "from selenium import webdriver",
            "from selenium.webdriver.common.by import By",
            "from selenium.webdriver.support.ui import WebDriverWait",
            "from selenium.webdriver.support import expected_conditions as EC",
            "import time",
            "",
            f'driver = webdriver.Chrome()',
            f'driver.get("{url}")',
            "wait = WebDriverWait(driver, 10)",
            "",
        ]

        for i, elem in enumerate(dom_elements, start=1):
            tag = elem.get("tag", "")
            elem_id = elem.get("id", "")
            elem_class = elem.get("class", "")
            desc = f'{tag}#{elem_id}.{elem_class}'.strip("#.").replace("..", ".")
            if not desc:
                desc = f"{tag}_{i}"

            lines.append(f'print("STEP {i} - Check element {desc}")')
            lines.append("try:")
            
            # Build selector priority: id > class > tag
            selector_line = "element = "
            if elem_id:
                selector_line += f'wait.until(EC.presence_of_element_located((By.ID, "{elem_id}")))' 
            elif elem_class:
                selector_line += f'wait.until(EC.presence_of_element_located((By.CLASS_NAME, "{elem_class}")))' 
            else:
                selector_line += f'wait.until(EC.presence_of_element_located((By.TAG_NAME, "{tag}")))'
            lines.append(f"    {selector_line}")
            lines.append(f"    print('PASS - step {i}')")
            lines.append("except Exception as e:")
            lines.append(f"    print('FAIL - step {i}' if isinstance(e, AssertionError) else f'ERROR - step {i}: {{e}}')")
            lines.append("")

        lines.append("driver.quit()")
        return "\n".join(lines)
