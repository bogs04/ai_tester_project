import time
import random


SUPPORTED_ACTIONS = {"click", "input", "hover", "navigate", "verify"}


def run_actions(url, actions):
    """
    Lightweight execution simulator.
    No browser, no JS, no subprocess.
    """

    results = []

    for i, act in enumerate(actions):
        action = act.get("action")
        selector = act.get("selector")

        if action not in SUPPORTED_ACTIONS:
            status = "unsupported"
        elif not selector:
            status = "fail"
        else:
            # simulate realistic behavior
            if action == "verify":
                status = "pass"
            else:
                status = random.choices(
                    ["pass", "fail"],
                    weights=[0.85, 0.15]
                )[0]

        results.append({
            "step": i,
            "action": action,
            "selector": selector,
            "status": status
        })

        time.sleep(0.02)  # simulate execution latency

    return results


def execution_metrics(results):
    total = len(results)
    passed = sum(1 for r in results if r["status"] == "pass")
    failed = sum(1 for r in results if r["status"] == "fail")

    success_rate = passed / total if total > 0 else 0

    return {
        "Executed Steps": total,
        "Passed": passed,
        "Failed": failed,
        "Success Rate": round(success_rate, 3)
    }
