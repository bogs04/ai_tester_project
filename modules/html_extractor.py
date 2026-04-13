# modules/html_extractor.py
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
import time

def fetch_html(url, out_dir):
    """
    Dùng Selenium mở URL, lưu HTML vào out_dir.
    Trả về path file HTML hoặc None nếu lỗi.
    """
    os.makedirs(out_dir, exist_ok=True)
    filename = url.replace("https://", "").replace("http://", "").replace("/", "_") + ".html"
    path = os.path.join(out_dir, filename)

    options = Options()
    options.headless = True  # không mở cửa sổ trình duyệt
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    try:
        # Khởi tạo Chrome driver
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        time.sleep(2)  # chờ load trang

        html_content = driver.page_source

        with open(path, "w", encoding="utf-8") as f:
            f.write(html_content)

        driver.quit()
        return path

    except WebDriverException as e:
        print(f"Error fetching HTML from {url}: {e}")
        return None
