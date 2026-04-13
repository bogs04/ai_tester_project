# 🤖 AI Tester Project

## 📌 Overview

This project implements an **AI-powered automated testing system** that can generate and execute test cases for web applications.

The system combines:

* Large Language Models (LLMs)
* Web automation tools
* Dynamic execution strategies

👉 Goal: Reduce manual testing effort and improve test coverage automatically.

---

## 🚀 Features

* 🔍 **Automatic Test Case Generation**

  * Generate test cases from HTML/DOM using AI (LLM-based)

* 🌐 **Web Page Analysis**

  * Extract and parse HTML structure
  * Convert DOM into structured data

* ⚙️ **Automated Test Execution**

  * Execute generated test cases dynamically

* 🧠 **Multiple Testing Strategies**

  * Baseline testing
  * Template-based LLM testing
  * Advanced LLM-based testing

* 📊 **Evaluation & Comparison**

  * Compare performance across methods
  * Metrics: coverage, pass rate, latency, hallucination

---

## 🏗️ System Architecture

```text
Input URL
   ↓
HTML Extractor
   ↓
DOM Parser
   ↓
Test Case Generator (Baseline / LLM / Advanced)
   ↓
Test Executor
   ↓
Result Evaluation
```

---

## 🛠️ Tech Stack

* **Language:** Python
* **Automation:** Selenium / Playwright
* **Testing:** Pytest
* **AI Models:** OpenAI / Claude
* **Data Processing:** JSON, HTML parsing

---

## 📂 Project Structure

```text
.
├── main.py                  # Main pipeline
├── main_extra.py            # Extended pipeline
├── modules/                 # Core modules
├── modules_exec/            # Execution engine
├── modules_extra/           # Advanced features
├── modules_llm/             # LLM-based generation
├── utils/                   # Helper functions
├── evaluation/              # Metrics & evaluation
├── data/                    # Sample dataset
├── results/                 # Output results
├── requirements.txt
└── streamlit_app.py         # Demo UI (optional)
```

---

## ▶️ How to Run

### 1. Clone repository

```bash
git clone https://github.com/bogs04/ai_tester_project.git
cd ai_tester_project
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run main pipeline

```bash
python main.py
```

### 4. (Optional) Run extended pipeline

```bash
python main_extra.py
```

---

## 📊 Example Workflow

1. Input: Website URL
2. Extract HTML content
3. Parse DOM structure
4. Generate test cases using AI
5. Execute tests automatically
6. Collect and evaluate results

---

## 📷 Sample Output

* Generated test cases (Python scripts)
* Execution logs
* Performance comparison charts

---

## 📂 Dataset

Due to large size, only a **sample dataset** is included in this repository.

Full dataset contains:

* HTML pages
* DOM structures
* Generated test cases
* Execution logs

---

## 🎯 Evaluation Metrics

* ✔ Test coverage
* ✔ Pass rate
* ✔ Execution time
* ✔ Hallucination rate (LLM accuracy)

---

## 🔮 Future Improvements

* Improve LLM prompting strategies
* Enhance self-healing test execution
* Integrate CI/CD pipeline
* Expand dataset and real-world scenarios

---

## 👨‍💻 Author

* Name: (Your Name)
* Project: AI-based Automated Testing System

---

## 📜 License

This project is for academic and research purposes.
