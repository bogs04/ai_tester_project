# evaluation.py
import os
import json
import pandas as pd

# --- CONFIG ---
DATA_LOGS = "data/logs"
REPORT_DIR = "reports"
os.makedirs(REPORT_DIR, exist_ok=True)

MODELS = ["baseline", "llm_template", "llm_advanced"]

def load_results():
    all_results = []

    for model in MODELS:
        log_dir = os.path.join(DATA_LOGS, model)
        if not os.path.exists(log_dir):
            continue

        for fname in os.listdir(log_dir):
            if fname.endswith("_results.json"):
                path = os.path.join(log_dir, fname)
                with open(path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                url_name = fname.replace(f"_{model}_results.json", "")
                all_results.append({
                    "url": url_name,
                    "model": model,
                    "total_steps": data.get("total_steps", 0),
                    "passed": data.get("passed", 0),
                    "failed": data.get("failed", 0),
                    "errors": data.get("errors", 0),
                    "score": data.get("score", 0)
                })
    return all_results

def generate_summary(df):
    summary = df.groupby("model").agg({
        "total_steps": ["mean", "min", "max"],
        "passed": ["mean", "min", "max"],
        "failed": ["mean", "min", "max"],
        "errors": ["mean", "min", "max"],
        "score": ["mean", "min", "max"]
    })
    summary.columns = ["_".join(col) for col in summary.columns]
    return summary

def main():
    results = load_results()
    if not results:
        print("No results found in logs.")
        return

    df = pd.DataFrame(results)
    df.sort_values(["url", "model"], inplace=True)

    # Export per-URL results
    per_url_path = os.path.join(REPORT_DIR, "per_url_results.csv")
    df.to_csv(per_url_path, index=False)
    print(f"Per-URL results saved → {per_url_path}")

    # Export summary stats
    summary_df = generate_summary(df)
    summary_path = os.path.join(REPORT_DIR, "summary_results.csv")
    summary_df.to_csv(summary_path)
    print(f"Summary results saved → {summary_path}")

    # Optional: print top stats
    print("\n=== SUMMARY ===")
    print(summary_df)

if __name__ == "__main__":
    main()
