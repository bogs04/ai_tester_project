import json

def safe_json_parse(text):
    """
    Absolute-safe JSON extractor for LLM output.
    NEVER throws.
    Returns list.
    """

    if not text or not isinstance(text, str):
        return []

    text = text.strip()

    # tìm vị trí bắt đầu của JSON array
    start = text.find("[")
    if start == -1:
        return []

    # cắt từ [ đến hết
    candidate = text[start:]

    # đếm ngoặc để cắt đúng ]
    bracket = 0
    end = -1

    for i, ch in enumerate(candidate):
        if ch == "[":
            bracket += 1
        elif ch == "]":
            bracket -= 1
            if bracket == 0:
                end = i + 1
                break

    if end == -1:
        return []

    candidate = candidate[:end]

    try:
        parsed = json.loads(candidate)
        if isinstance(parsed, list):
            return parsed
        return []
    except Exception:
        print("\n❌ JSON STILL INVALID:")
        print(candidate)
        return []
