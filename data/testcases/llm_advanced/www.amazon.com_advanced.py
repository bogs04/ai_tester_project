from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.amazon.com")
wait = WebDriverWait(driver, 10)

print("STEP 1 - Check element html#None.['a-no-js']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['a-no-js']")))
    print('PASS - step 1')
except Exception as e:
    print('FAIL - step 1' if isinstance(e, AssertionError) else f'ERROR - step 1: {e}')

print("STEP 2 - Check element head#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "head")))
    print('PASS - step 2')
except Exception as e:
    print('FAIL - step 2' if isinstance(e, AssertionError) else f'ERROR - step 2: {e}')

print("STEP 3 - Check element meta#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "meta")))
    print('PASS - step 3')
except Exception as e:
    print('FAIL - step 3' if isinstance(e, AssertionError) else f'ERROR - step 3: {e}')

print("STEP 4 - Check element meta#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "meta")))
    print('PASS - step 4')
except Exception as e:
    print('FAIL - step 4' if isinstance(e, AssertionError) else f'ERROR - step 4: {e}')

print("STEP 5 - Check element meta#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "meta")))
    print('PASS - step 5')
except Exception as e:
    print('FAIL - step 5' if isinstance(e, AssertionError) else f'ERROR - step 5: {e}')

print("STEP 6 - Check element title#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "title")))
    print('PASS - step 6')
except Exception as e:
    print('FAIL - step 6' if isinstance(e, AssertionError) else f'ERROR - step 6: {e}')

print("STEP 7 - Check element meta#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "meta")))
    print('PASS - step 7')
except Exception as e:
    print('FAIL - step 7' if isinstance(e, AssertionError) else f'ERROR - step 7: {e}')

print("STEP 8 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 8')
except Exception as e:
    print('FAIL - step 8' if isinstance(e, AssertionError) else f'ERROR - step 8: {e}')

print("STEP 9 - Check element script#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "script")))
    print('PASS - step 9')
except Exception as e:
    print('FAIL - step 9' if isinstance(e, AssertionError) else f'ERROR - step 9: {e}')

print("STEP 10 - Check element script#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "script")))
    print('PASS - step 10')
except Exception as e:
    print('FAIL - step 10' if isinstance(e, AssertionError) else f'ERROR - step 10: {e}')

print("STEP 11 - Check element script#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "script")))
    print('PASS - step 11')
except Exception as e:
    print('FAIL - step 11' if isinstance(e, AssertionError) else f'ERROR - step 11: {e}')

print("STEP 12 - Check element script#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "script")))
    print('PASS - step 12')
except Exception as e:
    print('FAIL - step 12' if isinstance(e, AssertionError) else f'ERROR - step 12: {e}')

print("STEP 13 - Check element script#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "script")))
    print('PASS - step 13')
except Exception as e:
    print('FAIL - step 13' if isinstance(e, AssertionError) else f'ERROR - step 13: {e}')

print("STEP 14 - Check element body#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    print('PASS - step 14')
except Exception as e:
    print('FAIL - step 14' if isinstance(e, AssertionError) else f'ERROR - step 14: {e}')

print("STEP 15 - Check element div#None.['a-container', 'a-padding-double-large']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['a-container', 'a-padding-double-large']")))
    print('PASS - step 15')
except Exception as e:
    print('FAIL - step 15' if isinstance(e, AssertionError) else f'ERROR - step 15: {e}')

print("STEP 16 - Check element div#None.['a-row', 'a-spacing-double-large']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['a-row', 'a-spacing-double-large']")))
    print('PASS - step 16')
except Exception as e:
    print('FAIL - step 16' if isinstance(e, AssertionError) else f'ERROR - step 16: {e}')

print("STEP 17 - Check element div#None.['a-row', 'a-spacing-medium', 'a-text-center']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['a-row', 'a-spacing-medium', 'a-text-center']")))
    print('PASS - step 17')
except Exception as e:
    print('FAIL - step 17' if isinstance(e, AssertionError) else f'ERROR - step 17: {e}')

print("STEP 18 - Check element i#None.['a-icon', 'a-logo']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['a-icon', 'a-logo']")))
    print('PASS - step 18')
except Exception as e:
    print('FAIL - step 18' if isinstance(e, AssertionError) else f'ERROR - step 18: {e}')

print("STEP 19 - Check element div#None.['a-box', 'a-alert', 'a-alert-info', 'a-spacing-base']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['a-box', 'a-alert', 'a-alert-info', 'a-spacing-base']")))
    print('PASS - step 19')
except Exception as e:
    print('FAIL - step 19' if isinstance(e, AssertionError) else f'ERROR - step 19: {e}')

print("STEP 20 - Check element div#None.['a-box-inner']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['a-box-inner']")))
    print('PASS - step 20')
except Exception as e:
    print('FAIL - step 20' if isinstance(e, AssertionError) else f'ERROR - step 20: {e}')

print("STEP 21 - Check element i#None.['a-icon', 'a-icon-alert']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['a-icon', 'a-icon-alert']")))
    print('PASS - step 21')
except Exception as e:
    print('FAIL - step 21' if isinstance(e, AssertionError) else f'ERROR - step 21: {e}')

print("STEP 22 - Check element h4#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h4")))
    print('PASS - step 22')
except Exception as e:
    print('FAIL - step 22' if isinstance(e, AssertionError) else f'ERROR - step 22: {e}')

print("STEP 23 - Check element div#None.['a-section']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['a-section']")))
    print('PASS - step 23')
except Exception as e:
    print('FAIL - step 23' if isinstance(e, AssertionError) else f'ERROR - step 23: {e}')

print("STEP 24 - Check element div#None.['a-box', 'a-color-offset-background']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['a-box', 'a-color-offset-background']")))
    print('PASS - step 24')
except Exception as e:
    print('FAIL - step 24' if isinstance(e, AssertionError) else f'ERROR - step 24: {e}')

print("STEP 25 - Check element div#None.['a-box-inner', 'a-padding-extra-large']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['a-box-inner', 'a-padding-extra-large']")))
    print('PASS - step 25')
except Exception as e:
    print('FAIL - step 25' if isinstance(e, AssertionError) else f'ERROR - step 25: {e}')

print("STEP 26 - Check element form#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "form")))
    print('PASS - step 26')
except Exception as e:
    print('FAIL - step 26' if isinstance(e, AssertionError) else f'ERROR - step 26: {e}')

print("STEP 27 - Check element input#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "input")))
    print('PASS - step 27')
except Exception as e:
    print('FAIL - step 27' if isinstance(e, AssertionError) else f'ERROR - step 27: {e}')

print("STEP 28 - Check element input#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "input")))
    print('PASS - step 28')
except Exception as e:
    print('FAIL - step 28' if isinstance(e, AssertionError) else f'ERROR - step 28: {e}')

print("STEP 29 - Check element input#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "input")))
    print('PASS - step 29')
except Exception as e:
    print('FAIL - step 29' if isinstance(e, AssertionError) else f'ERROR - step 29: {e}')

print("STEP 30 - Check element div#None.['a-section', 'a-spacing-extra-large']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['a-section', 'a-spacing-extra-large']")))
    print('PASS - step 30')
except Exception as e:
    print('FAIL - step 30' if isinstance(e, AssertionError) else f'ERROR - step 30: {e}')

print("STEP 31 - Check element div#None.['a-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['a-row']")))
    print('PASS - step 31')
except Exception as e:
    print('FAIL - step 31' if isinstance(e, AssertionError) else f'ERROR - step 31: {e}')

print("STEP 32 - Check element span#None.['a-button', 'a-button-primary', 'a-span12']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['a-button', 'a-button-primary', 'a-span12']")))
    print('PASS - step 32')
except Exception as e:
    print('FAIL - step 32' if isinstance(e, AssertionError) else f'ERROR - step 32: {e}')

print("STEP 33 - Check element span#None.['a-button-inner']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['a-button-inner']")))
    print('PASS - step 33')
except Exception as e:
    print('FAIL - step 33' if isinstance(e, AssertionError) else f'ERROR - step 33: {e}')

print("STEP 34 - Check element button#None.['a-button-text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['a-button-text']")))
    print('PASS - step 34')
except Exception as e:
    print('FAIL - step 34' if isinstance(e, AssertionError) else f'ERROR - step 34: {e}')

print("STEP 35 - Check element div#None.['a-divider', 'a-divider-section']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['a-divider', 'a-divider-section']")))
    print('PASS - step 35')
except Exception as e:
    print('FAIL - step 35' if isinstance(e, AssertionError) else f'ERROR - step 35: {e}')

print("STEP 36 - Check element div#None.['a-divider-inner']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['a-divider-inner']")))
    print('PASS - step 36')
except Exception as e:
    print('FAIL - step 36' if isinstance(e, AssertionError) else f'ERROR - step 36: {e}')

print("STEP 37 - Check element div#None.['a-text-center', 'a-spacing-small', 'a-size-mini']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['a-text-center', 'a-spacing-small', 'a-size-mini']")))
    print('PASS - step 37')
except Exception as e:
    print('FAIL - step 37' if isinstance(e, AssertionError) else f'ERROR - step 37: {e}')

print("STEP 38 - Check element a#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "a")))
    print('PASS - step 38')
except Exception as e:
    print('FAIL - step 38' if isinstance(e, AssertionError) else f'ERROR - step 38: {e}')

print("STEP 39 - Check element span#None.['a-letter-space']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['a-letter-space']")))
    print('PASS - step 39')
except Exception as e:
    print('FAIL - step 39' if isinstance(e, AssertionError) else f'ERROR - step 39: {e}')

print("STEP 40 - Check element span#None.['a-letter-space']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['a-letter-space']")))
    print('PASS - step 40')
except Exception as e:
    print('FAIL - step 40' if isinstance(e, AssertionError) else f'ERROR - step 40: {e}')

print("STEP 41 - Check element span#None.['a-letter-space']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['a-letter-space']")))
    print('PASS - step 41')
except Exception as e:
    print('FAIL - step 41' if isinstance(e, AssertionError) else f'ERROR - step 41: {e}')

print("STEP 42 - Check element span#None.['a-letter-space']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['a-letter-space']")))
    print('PASS - step 42')
except Exception as e:
    print('FAIL - step 42' if isinstance(e, AssertionError) else f'ERROR - step 42: {e}')

print("STEP 43 - Check element a#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "a")))
    print('PASS - step 43')
except Exception as e:
    print('FAIL - step 43' if isinstance(e, AssertionError) else f'ERROR - step 43: {e}')

print("STEP 44 - Check element div#None.['a-text-center', 'a-size-mini', 'a-color-base']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['a-text-center', 'a-size-mini', 'a-color-base']")))
    print('PASS - step 44')
except Exception as e:
    print('FAIL - step 44' if isinstance(e, AssertionError) else f'ERROR - step 44: {e}')

print("STEP 45 - Check element script#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "script")))
    print('PASS - step 45')
except Exception as e:
    print('FAIL - step 45' if isinstance(e, AssertionError) else f'ERROR - step 45: {e}')

print("STEP 46 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 46')
except Exception as e:
    print('FAIL - step 46' if isinstance(e, AssertionError) else f'ERROR - step 46: {e}')

print("STEP 47 - Check element noscript#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "noscript")))
    print('PASS - step 47')
except Exception as e:
    print('FAIL - step 47' if isinstance(e, AssertionError) else f'ERROR - step 47: {e}')

print("STEP 48 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 48')
except Exception as e:
    print('FAIL - step 48' if isinstance(e, AssertionError) else f'ERROR - step 48: {e}')

print("STEP 49 - Check element script#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "script")))
    print('PASS - step 49')
except Exception as e:
    print('FAIL - step 49' if isinstance(e, AssertionError) else f'ERROR - step 49: {e}')

driver.quit()