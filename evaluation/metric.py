def validity(steps, dom):
    selectors = {e["selector"] for e in dom}
    valid = [
        s for s in steps
        if s.get("action") in {"click","input","submit"}
        and s.get("selector") in selectors
    ]
    return len(valid) / max(1, len(steps))


def coverage(steps, dom):
    used = {s["selector"] for s in steps if "selector" in s}
    return len(used) / max(1, len(dom))


def redundancy(steps):
    sels = [s["selector"] for s in steps if "selector" in s]
    return 1 - (len(sels) - len(set(sels))) / max(1, len(sels))
