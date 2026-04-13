import os
import json
from bs4 import BeautifulSoup

def parse_dom(html_path, out_dir):
    os.makedirs(out_dir, exist_ok=True)

    with open(html_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    elements = []

    for tag in soup.find_all():
        selector = None
        cls = tag.get("class")

        if tag.get("id"):
            selector = f"#{tag.get('id')}"
        elif cls:
            selector = "." + ".".join(cls)

        elements.append({
            "tag": tag.name,
            "id": tag.get("id"),
            "class": cls,
            "selector": selector
        })

    # save json cho đẹp báo cáo
    filename = os.path.basename(html_path).replace(".html", ".json")
    json_path = os.path.join(out_dir, filename)

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(elements, f, indent=2, ensure_ascii=False)

    return elements
