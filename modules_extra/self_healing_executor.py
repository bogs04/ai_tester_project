# modules_extra/self_healing_executor.py
import random

def mock_execute(step):
    """
    Fake executor:
    - 80% pass
    - 20% fail
    """
    return random.random() < 0.8


def run_step_with_healing(step):
    if mock_execute(step):
        return "PASS"

    # try alternatives
    for alt in step.get("alternatives", []):
        if mock_execute(alt):
            return "PASS_HEALED"

    return "ERROR"
