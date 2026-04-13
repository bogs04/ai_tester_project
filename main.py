import os
from modules.html_extractor import fetch_html
from modules.dom_parser import parse_dom
from modules.baseline_testgen import BaselineTestGenerator
from modules.llm_template_testgen import MockLLMGenerator
from modules.llm_advanced_testgen import PromptedLLMGenerator
from modules.test_executor import run_test_script, evaluate_log

# --- CONFIG ---
DATA_HTML = "data/html"
DATA_DOM = "data/dom"
DATA_TEST = "data/testcases"
DATA_LOGS = "data/logs"
URL_FILE = "dataset/urls.txt"

os.makedirs(DATA_HTML, exist_ok=True)
os.makedirs(DATA_DOM, exist_ok=True)
os.makedirs(DATA_TEST, exist_ok=True)
os.makedirs(DATA_LOGS, exist_ok=True)

# --- Load URL list ---
with open(URL_FILE, "r", encoding="utf-8") as f:
    urls = [line.strip() for line in f if line.strip()]

# --- Pipeline per URL ---
for url in urls:
    print(f"[Processing] {url}")
    
    # Stage 1: Fetch HTML
    html_path = fetch_html(url, DATA_HTML)
    if not html_path:
        print(f"{url} FAIL fetching HTML")
        continue

    # Stage 2: Parse DOM
    dom_elements = parse_dom(html_path, DATA_DOM)
    print(f"{url} DOM parsed → {len(dom_elements)} elements")

    # --- Stage 3: Generate test scripts ---
    # 3A - Baseline
    baseline_dir = os.path.join(DATA_TEST, "baseline")
    os.makedirs(baseline_dir, exist_ok=True)
    baseline = BaselineTestGenerator(out_dir=baseline_dir)
    baseline_script = baseline.generate(dom_elements, url)
    baseline_path = os.path.join(baseline_dir, os.path.basename(html_path).replace(".html", "_baseline.py"))
    with open(baseline_path, "w", encoding="utf-8") as f:
        f.write(baseline_script)

    # 3B - LLM Template
    llm_template_dir = os.path.join(DATA_TEST, "llm_template")
    os.makedirs(llm_template_dir, exist_ok=True)
    llm_template = MockLLMGenerator(out_dir=llm_template_dir)
    template_script = llm_template.generate(dom_elements, url)
    template_path = os.path.join(llm_template_dir, os.path.basename(html_path).replace(".html", "_template.py"))
    with open(template_path, "w", encoding="utf-8") as f:
        f.write(template_script)

    # 3C - LLM Advanced
    llm_advanced_dir = os.path.join(DATA_TEST, "llm_advanced")
    os.makedirs(llm_advanced_dir, exist_ok=True)
    llm_advanced = PromptedLLMGenerator(out_dir=llm_advanced_dir)
    advanced_script = llm_advanced.generate(dom_elements, url)
    advanced_path = os.path.join(llm_advanced_dir, os.path.basename(html_path).replace(".html", "_advanced.py"))
    with open(advanced_path, "w", encoding="utf-8") as f:
        f.write(advanced_script)

    # --- Stage 4: Execute & Evaluate ---
    for script_path, log_subdir in [
        (baseline_path, "baseline"),
        (template_path, "llm_template"),
        (advanced_path, "llm_advanced"),
    ]:
        log_dir = os.path.join(DATA_LOGS, log_subdir)
        os.makedirs(log_dir, exist_ok=True)
        log_path = os.path.join(log_dir, os.path.basename(script_path).replace(".py", ".txt"))
        result_path = os.path.join(log_dir, os.path.basename(script_path).replace(".py", "_results.json"))

        # Run Selenium script with proper waits
        run_test_script(script_path, log_path)

        # Evaluate
        results = evaluate_log(log_path, result_path)
        print(f"--- {os.path.basename(script_path)} RESULT ---")
        print(f"Total Steps: {results['total_steps']}")
        print(f"Passed: {results['passed']}")
        print(f"Failed: {results['failed']}")
        print(f"Errors: {results['errors']}")
        print(f"Score: {results['score']}%")
        print("-----------------------")

print("===== PIPELINE COMPLETE =====")
