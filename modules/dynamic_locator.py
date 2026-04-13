# modules/dynamic_locator.py

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def find_element_safe(driver, locator_type, locator_value, alternatives=None):
    """
    Thử tìm element với locator chính và danh sách alternatives
    Trả về WebElement nếu tìm thấy, None nếu không tìm thấy
    """
    if alternatives is None:
        alternatives = []

    # Chuẩn hóa locator
    by_type = {
        "id": By.ID,
        "name": By.NAME,
        "class": By.CLASS_NAME,
        "xpath": By.XPATH,
        "css": By.CSS_SELECTOR,
        "tag": By.TAG_NAME,
        "link_text": By.LINK_TEXT,
        "partial_link_text": By.PARTIAL_LINK_TEXT
    }.get(locator_type.lower(), By.ID)

    # Thử locator chính
    try:
        return driver.find_element(by_type, locator_value)
    except NoSuchElementException:
        pass

    # Thử các alternatives
    for alt in alternatives:
        alt_type = alt.get("locator_type", locator_type)
        alt_value = alt.get("locator_value")
        alt_by = {
            "id": By.ID,
            "name": By.NAME,
            "class": By.CLASS_NAME,
            "xpath": By.XPATH,
            "css": By.CSS_SELECTOR,
            "tag": By.TAG_NAME,
            "link_text": By.LINK_TEXT,
            "partial_link_text": By.PARTIAL_LINK_TEXT
        }.get(alt_type.lower(), By.ID)

        try:
            return driver.find_element(alt_by, alt_value)
        except NoSuchElementException:
            continue

    # Nếu vẫn không tìm thấy, trả về None
    return None

def generate_alternatives(locator_type, locator_value):
    """
    Sinh các alternatives locator tự động dựa trên locator chính
    Ví dụ: nếu locator là id, có thể thử class, name, xpath gần đúng, text...
    """
    alternatives = []

    # Thử biến đổi từ ID -> class, name
    if locator_type == "id":
        alternatives.append({"locator_type": "name", "locator_value": locator_value})
        alternatives.append({"locator_type": "class", "locator_value": locator_value})

    # Nếu là class -> id, name
    if locator_type == "class":
        alternatives.append({"locator_type": "id", "locator_value": locator_value})
        alternatives.append({"locator_type": "name", "locator_value": locator_value})

    # XPath gần đúng
    alternatives.append({"locator_type": "xpath", "locator_value": f"//*[contains(@id,'{locator_value}')]"})
    alternatives.append({"locator_type": "xpath", "locator_value": f"//*[contains(@class,'{locator_value}')]"})
    alternatives.append({"locator_type": "xpath", "locator_value": f"//*[contains(text(),'{locator_value}')]"} )

    return alternatives
