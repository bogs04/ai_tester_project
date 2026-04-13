# modules/llm_template_testgen.py
import os

class MockLLMGenerator:
    """
    LLM Template Test Generator:
    - Sinh test case đơn giản từ DOM elements.
    - Kiểm tra presence của tag + text cơ bản.
    """
    def __init__(self, out_dir="data/testcases/llm_template"):
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
            "import time",
            "",
            f'driver = webdriver.Chrome()',
            f'driver.get("{url}")',
            "time.sleep(1)  # simple wait",
            "",
        ]

        for i, elem in enumerate(dom_elements, start=1):
            tag = elem.get("tag", "")
            text = elem.get("text", "").strip()
            desc = f"{tag}_{i}"
            lines.append(f'print("STEP {i} - Check element {desc}")')
            lines.append("try:")
            
            # chỉ kiểm tra presence của tag
            lines.append(f'    element = driver.find_element(By.TAG_NAME, "{tag}")')
            if text:
                lines.append(f'    assert "{text}" in element.text')
            lines.append(f"    print('PASS - step {i}')")
            lines.append("except Exception as e:")
            lines.append(f"    print('FAIL - step {i}' if isinstance(e, AssertionError) else f'ERROR - step {i}: {{e}}')")
            lines.append("")

        lines.append("driver.quit()")
        return "\n".join(lines)
