from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.ibm.com")
time.sleep(1)

print("STEP 1 - Check page title")
try:
    assert "Example Domain" in driver.title
    print("PASS - step 1")
except AssertionError:
    print("FAIL - step 1")
except Exception as e:
    print("ERROR - step 1:", e)

print("STEP 2 - Check H1")
try:
    h1 = driver.find_element(By.TAG_NAME, "h1")
    if h1 and h1.text.strip():
        print("PASS - step 2")
    else:
        print("FAIL - step 2")
except Exception as e:
    print("ERROR - step 2:", e)

print("STEP 3 - Check paragraph")
try:
    p = driver.find_element(By.TAG_NAME, "p")
    if p and p.text.strip():
        print("PASS - step 3")
    else:
        print("FAIL - step 3")
except Exception as e:
    print("ERROR - step 3:", e)

driver.quit()