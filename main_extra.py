import os
import time
import csv
import requests
import pandas as pd
import matplotlib.pyplot as plt
import sys
from bs4 import BeautifulSoup

from modules_llm.openai_testgen import generate_gpt_tests
from modules_llm.claude_testgen import generate_claude_tests


# =========================
# CONFIG
# =========================
URLS = [
    "https://httpbin.org",
    "https://books.toscrape.com",
    "https://quotes.toscrape.com",
    "https://www.python.org",
    "https://vnexpress.net"
]

RESULT_DIR = "results"
os.makedirs(RESULT_DIR, exist_ok=True)


# =========================
# DOM EXTRACTION
# =========================
def extract_dom(url):
    html = requests.get(url, timeout=10).text
    soup = BeautifulSoup(html, "html.parser")

    dom = []
    for tag in soup.find_all(["a", "button", "input"]):
        selector = tag.name
        if tag.get("id"):
            selector += f"#{tag['id']}"
        elif tag.get("class"):
            selector += "." + ".".join(tag.get("class"))
        dom.append({"selector": selector})

    return dom


# =========================
# RULE-BASED GENERATOR
# =========================
def generate_rule_tests(dom):
    return [
        {"action": "verify", "selector": el["selector"]}
        for el in dom
    ]


# =========================
# METRICS (FIXED)
# =========================
def evaluate(actions, dom):
    dom_selectors = {el["selector"] for el in dom}

    valid_steps = []
    hallucinated = 0

    for act in actions:
        sel = act.get("selector")

        if not sel:
            hallucinated += 1
            continue

        if sel in dom_selectors:
            valid_steps.append(sel)
        else:
            hallucinated += 1

    steps = len(valid_steps)

    coverage = (
        len(set(valid_steps)) / len(dom_selectors)
        if dom_selectors else 0
    )

    hallucination_rate = (
        hallucinated / len(actions)
        if actions else 0
    )

    return steps, coverage, hallucination_rate


# =========================
# RUN MODEL
# =========================
def run_model(name, fn, dom):
    start = time.time()

    try:
        actions = fn(dom)
        parse_success = True
    except Exception as e:
        print(f"❌ {name} failed: {e}")
        actions = []
        parse_success = False

    latency_ms = (time.time() - start) * 1000
    steps, coverage, halluc = evaluate(actions, dom)

    return {
        "model": name,
        "steps": steps,
        "coverage": coverage,
        "hallucination_rate": halluc,
        "latency_ms": latency_ms,
        "parse_success": parse_success,
    }


# =========================
# CLEAN PLOT
# =========================
def plot_metric_clean(df, metric, ylabel, filename):
    plt.figure(figsize=(5, 3.5))

    data = (
        df.groupby("model")[metric]
        .mean()
        .reindex(["rule", "GPT", "Claude"])
    )

    bars = plt.bar(data.index, data.values, width=0.6)
    plt.ylabel(ylabel)
    plt.title(metric.replace("_", " ").title())
    plt.grid(axis="y", linestyle=":", alpha=0.5)

    for bar in bars:
        y = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            y,
            f"{y:.2f}",
            ha="center",
            va="bottom",
            fontsize=9,
        )

    plt.tight_layout()
    plt.savefig(os.path.join(RESULT_DIR, filename), dpi=200)
    plt.close()


# =========================
# MAIN
# =========================
def main():
    rows = []

    for url in URLS:
        print(f"\nProcessing {url}")
        dom = extract_dom(url)

        for name, fn in [
            ("rule", generate_rule_tests),
            ("GPT", generate_gpt_tests),
            ("Claude", generate_claude_tests),
        ]:
            result = run_model(name, fn, dom)
            result["url"] = url
            rows.append(result)

    # =========================
    # SAVE CSV
    # =========================
    csv_path = os.path.join(RESULT_DIR, "comparison_results.csv")
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "url",
                "model",
                "steps",
                "coverage",
                "hallucination_rate",
                "latency_ms",
                "parse_success",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)

    # =========================
    # SAVE TXT
    # =========================
    df = pd.DataFrame(rows)
    with open(os.path.join(RESULT_DIR, "comparison_results.txt"), "w", encoding="utf-8") as f:
        f.write(df.to_string(index=False))

    # =========================
    # PLOTS
    # =========================
    plot_metric_clean(df, "latency_ms", "Latency (ms)", "latency_comparison.png")
    plot_metric_clean(df, "coverage", "Static DOM Coverage", "coverage_comparison.png")
    plot_metric_clean(df, "hallucination_rate", "Hallucination Rate", "hallucination_comparison.png")
    plot_metric_clean(df, "steps", "Valid Steps", "cost_efficiency.png")

    print(f"\n✅ Results & plots saved in /{RESULT_DIR}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        URLS = [sys.argv[1]]
    main()
