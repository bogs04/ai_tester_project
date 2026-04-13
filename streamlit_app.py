import time
import requests
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

from modules_llm.openai_testgen import generate_gpt_tests
from modules_llm.claude_testgen import generate_claude_tests
from modules_exec.executor import run_actions, execution_metrics


# =========================
# DOM EXTRACTION (STATIC)
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
# RULE-BASED BASELINE
# =========================
def generate_rule_tests(dom):
    return [{"action": "verify", "selector": el["selector"]} for el in dom]


# =========================
# METRICS (NEUTRAL & SAFE)
# =========================
def evaluate(actions, dom):
    """
    Coverage = interaction validity
    NOT full DOM coverage
    """
    dom_selectors = {el["selector"] for el in dom}

    used = []
    hallucinated = 0

    for act in actions:
        sel = act.get("selector")
        if not sel:
            hallucinated += 1
            continue
        used.append(sel)
        if sel not in dom_selectors:
            hallucinated += 1

    steps = len(actions)
    valid = len(set(used) & dom_selectors)

    coverage = valid / steps if steps > 0 else 0
    hallucination = hallucinated / steps if steps > 0 else 0

    return steps, coverage, hallucination


# =========================
# PLOT (UNCHANGED)
# =========================
def plot_bar(df, col, title, ylabel):
    fig, ax = plt.subplots(figsize=(4, 3))
    ax.bar(df["Model"], df[col])
    ax.set_title(title)
    ax.set_ylabel(ylabel)
    ax.grid(axis="y", linestyle=":", alpha=0.5)
    return fig


# =========================
# STREAMLIT UI
# =========================
st.set_page_config(
    page_title="LLM Testcase Generator",
    layout="wide"
)

st.title("🧪 Realtime Testcase Generation & Comparison")
st.write("Compare **Rule**, **GPT**, and **Claude** on a live website.")

url = st.text_input(
    "🔗 Enter URL",
    "https://httpbin.org"
)

models = st.multiselect(
    "🤖 Select generation methods",
    ["rule", "GPT", "Claude"],
    default=["GPT", "Claude"]
)

run_execution = st.checkbox(
    "🧪 Execute testcases (interaction-level)",
    value=True
)

run = st.button("🚀 Generate & Analyze")


# =========================
# RUN PIPELINE
# =========================
if run:
    if not models:
        st.warning("Please select at least one model.")
        st.stop()

    with st.spinner("Fetching DOM & generating testcases..."):
        dom = extract_dom(url)
        dom_count = len(dom)

        rows = []
        all_actions = {}
        all_exec_results = {}

        for model in models:
            start = time.time()

            if model == "rule":
                actions = generate_rule_tests(dom)
            elif model == "GPT":
                actions = generate_gpt_tests(dom)
            else:
                actions = generate_claude_tests(dom)

            latency = (time.time() - start) * 1000
            steps, coverage, halluc = evaluate(actions, dom)

            rows.append({
                "Model": model,
                "Steps": steps,
                "Coverage": round(coverage, 3),
                "Hallucination": round(halluc, 3),
                "Latency (ms)": int(latency),
            })

            all_actions[model] = actions

    # =========================
    # SUMMARY
    # =========================
    st.success("✅ Generation completed")

    st.metric("🔢 DOM Elements Detected", dom_count)

    if dom_count < 50:
        st.info(
            "ℹ️ Low DOM count detected. "
            "This website may rely on dynamic rendering (SPA / lazy-loading)."
        )

    df = pd.DataFrame(rows)

    # =========================
    # INTERPRETATION NOTE
    # =========================
    st.markdown(
        """
### 🔍 Interpretation Note
The reported metrics reflect **interaction behavior**, not absolute model quality.

Different models may prioritize:
- broader exploratory actions,
- conservative valid interactions,
- or faster response latency.

These behaviors are **complementary rather than competitive**.
"""
    )

    # =========================
    # TABLE
    # =========================
    st.subheader("📊 Model Comparison")
    st.dataframe(df, use_container_width=True)

    # =========================
    # CHARTS
    # =========================
    st.subheader("📈 Realtime Comparison Charts")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.pyplot(plot_bar(df, "Coverage", "Interaction Validity", "Ratio"))

    with col2:
        st.pyplot(plot_bar(df, "Latency (ms)", "Latency", "ms"))

    with col3:
        st.pyplot(plot_bar(df, "Hallucination", "Hallucination Rate", "Ratio"))

    # =========================
    # TESTCASES
    # =========================
    st.subheader("📋 Generated Testcases")

    for model, actions in all_actions.items():
        with st.expander(f"{model} Testcases ({len(actions)} steps)"):
            st.json(actions)

    # =========================
    # EXECUTION (PASS / FAIL)
    # =========================
    if run_execution:
        st.subheader("🧪 Execution Result (Interaction-level)")

        for model, actions in all_actions.items():
            with st.expander(f"{model} Execution"):
                results = run_actions(url, actions)
                metrics = execution_metrics(results)

                col1, col2, col3, col4 = st.columns(4)
                col1.metric("Executed", metrics["Executed Steps"])
                col2.metric("Passed", metrics["Passed"])
                col3.metric("Failed", metrics["Failed"])
                col4.metric("Success Rate", metrics["Success Rate"])

                st.json(results)
