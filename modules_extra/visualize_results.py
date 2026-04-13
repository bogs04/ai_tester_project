import json
import os
import matplotlib.pyplot as plt
from collections import defaultdict


def visualize_from_summary(summary_path, out_dir):
    """
    summary_path: data_extra/results/summary.json
    out_dir: thư mục lưu hình
    """
    os.makedirs(out_dir, exist_ok=True)

    with open(summary_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # ---- Gộp theo model ----
    agg = defaultdict(lambda: {"total": 0, "passed": 0, "errors": 0})

    for item in data:
        for model, res in item["models"].items():
            agg[model]["total"] += res["total"]
            agg[model]["passed"] += res["passed"]
            agg[model]["errors"] += res["errors"]

    models = list(agg.keys())
    pass_rates = []

    for m in models:
        total = agg[m]["total"]
        passed = agg[m]["passed"]
        rate = (passed / total) * 100 if total else 0
        pass_rates.append(rate)

    # ---- BAR CHART ----
    plt.figure()
    plt.bar(models, pass_rates)
    plt.ylabel("Pass rate (%)")
    plt.title("EXTRA PIPELINE – Pass rate comparison")
    plt.ylim(0, 100)

    out_img = os.path.join(out_dir, "pass_rate_comparison.png")
    plt.savefig(out_img)
    plt.close()

    # ---- PRINT TABLE ----
    print("\n=== EXTRA PIPELINE SUMMARY ===")
    for m in models:
        print(f"{m:10s} | total={agg[m]['total']:5d} | passed={agg[m]['passed']:5d} | errors={agg[m]['errors']:5d} | score={(agg[m]['passed']/agg[m]['total']*100 if agg[m]['total'] else 0):.2f}%")

    print(f"\nSaved chart to: {out_img}")
