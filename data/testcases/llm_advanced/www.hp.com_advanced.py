from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.hp.com")
wait = WebDriverWait(driver, 10)

print("STEP 1 - Check element html#None.['djr-micro-locale', 'hfv5', 'wf-formadjrmicro-n4-active', 'wf-newhpicon-n4-active', 'wf-headericons-n4-active', 'wf-aemhpicons-n4-active', 'wf-active']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['djr-micro-locale', 'hfv5', 'wf-formadjrmicro-n4-active', 'wf-newhpicon-n4-active', 'wf-headericons-n4-active', 'wf-aemhpicons-n4-active', 'wf-active']")))
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

print("STEP 4 - Check element title#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "title")))
    print('PASS - step 4')
except Exception as e:
    print('FAIL - step 4' if isinstance(e, AssertionError) else f'ERROR - step 4: {e}')

print("STEP 5 - Check element script#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "script")))
    print('PASS - step 5')
except Exception as e:
    print('FAIL - step 5' if isinstance(e, AssertionError) else f'ERROR - step 5: {e}')

print("STEP 6 - Check element script#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "script")))
    print('PASS - step 6')
except Exception as e:
    print('FAIL - step 6' if isinstance(e, AssertionError) else f'ERROR - step 6: {e}')

print("STEP 7 - Check element script#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "script")))
    print('PASS - step 7')
except Exception as e:
    print('FAIL - step 7' if isinstance(e, AssertionError) else f'ERROR - step 7: {e}')

print("STEP 8 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 8')
except Exception as e:
    print('FAIL - step 8' if isinstance(e, AssertionError) else f'ERROR - step 8: {e}')

print("STEP 9 - Check element meta#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "meta")))
    print('PASS - step 9')
except Exception as e:
    print('FAIL - step 9' if isinstance(e, AssertionError) else f'ERROR - step 9: {e}')

print("STEP 10 - Check element meta#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "meta")))
    print('PASS - step 10')
except Exception as e:
    print('FAIL - step 10' if isinstance(e, AssertionError) else f'ERROR - step 10: {e}')

print("STEP 11 - Check element meta#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "meta")))
    print('PASS - step 11')
except Exception as e:
    print('FAIL - step 11' if isinstance(e, AssertionError) else f'ERROR - step 11: {e}')

print("STEP 12 - Check element meta#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "meta")))
    print('PASS - step 12')
except Exception as e:
    print('FAIL - step 12' if isinstance(e, AssertionError) else f'ERROR - step 12: {e}')

print("STEP 13 - Check element meta#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "meta")))
    print('PASS - step 13')
except Exception as e:
    print('FAIL - step 13' if isinstance(e, AssertionError) else f'ERROR - step 13: {e}')

print("STEP 14 - Check element meta#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "meta")))
    print('PASS - step 14')
except Exception as e:
    print('FAIL - step 14' if isinstance(e, AssertionError) else f'ERROR - step 14: {e}')

print("STEP 15 - Check element meta#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "meta")))
    print('PASS - step 15')
except Exception as e:
    print('FAIL - step 15' if isinstance(e, AssertionError) else f'ERROR - step 15: {e}')

print("STEP 16 - Check element meta#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "meta")))
    print('PASS - step 16')
except Exception as e:
    print('FAIL - step 16' if isinstance(e, AssertionError) else f'ERROR - step 16: {e}')

print("STEP 17 - Check element meta#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "meta")))
    print('PASS - step 17')
except Exception as e:
    print('FAIL - step 17' if isinstance(e, AssertionError) else f'ERROR - step 17: {e}')

print("STEP 18 - Check element meta#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "meta")))
    print('PASS - step 18')
except Exception as e:
    print('FAIL - step 18' if isinstance(e, AssertionError) else f'ERROR - step 18: {e}')

print("STEP 19 - Check element meta#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "meta")))
    print('PASS - step 19')
except Exception as e:
    print('FAIL - step 19' if isinstance(e, AssertionError) else f'ERROR - step 19: {e}')

print("STEP 20 - Check element meta#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "meta")))
    print('PASS - step 20')
except Exception as e:
    print('FAIL - step 20' if isinstance(e, AssertionError) else f'ERROR - step 20: {e}')

print("STEP 21 - Check element meta#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "meta")))
    print('PASS - step 21')
except Exception as e:
    print('FAIL - step 21' if isinstance(e, AssertionError) else f'ERROR - step 21: {e}')

print("STEP 22 - Check element meta#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "meta")))
    print('PASS - step 22')
except Exception as e:
    print('FAIL - step 22' if isinstance(e, AssertionError) else f'ERROR - step 22: {e}')

print("STEP 23 - Check element meta#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "meta")))
    print('PASS - step 23')
except Exception as e:
    print('FAIL - step 23' if isinstance(e, AssertionError) else f'ERROR - step 23: {e}')

print("STEP 24 - Check element meta#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "meta")))
    print('PASS - step 24')
except Exception as e:
    print('FAIL - step 24' if isinstance(e, AssertionError) else f'ERROR - step 24: {e}')

print("STEP 25 - Check element meta#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "meta")))
    print('PASS - step 25')
except Exception as e:
    print('FAIL - step 25' if isinstance(e, AssertionError) else f'ERROR - step 25: {e}')

print("STEP 26 - Check element meta#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "meta")))
    print('PASS - step 26')
except Exception as e:
    print('FAIL - step 26' if isinstance(e, AssertionError) else f'ERROR - step 26: {e}')

print("STEP 27 - Check element meta#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "meta")))
    print('PASS - step 27')
except Exception as e:
    print('FAIL - step 27' if isinstance(e, AssertionError) else f'ERROR - step 27: {e}')

print("STEP 28 - Check element meta#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "meta")))
    print('PASS - step 28')
except Exception as e:
    print('FAIL - step 28' if isinstance(e, AssertionError) else f'ERROR - step 28: {e}')

print("STEP 29 - Check element meta#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "meta")))
    print('PASS - step 29')
except Exception as e:
    print('FAIL - step 29' if isinstance(e, AssertionError) else f'ERROR - step 29: {e}')

print("STEP 30 - Check element meta#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "meta")))
    print('PASS - step 30')
except Exception as e:
    print('FAIL - step 30' if isinstance(e, AssertionError) else f'ERROR - step 30: {e}')

print("STEP 31 - Check element meta#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "meta")))
    print('PASS - step 31')
except Exception as e:
    print('FAIL - step 31' if isinstance(e, AssertionError) else f'ERROR - step 31: {e}')

print("STEP 32 - Check element meta#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "meta")))
    print('PASS - step 32')
except Exception as e:
    print('FAIL - step 32' if isinstance(e, AssertionError) else f'ERROR - step 32: {e}')

print("STEP 33 - Check element meta#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "meta")))
    print('PASS - step 33')
except Exception as e:
    print('FAIL - step 33' if isinstance(e, AssertionError) else f'ERROR - step 33: {e}')

print("STEP 34 - Check element meta#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "meta")))
    print('PASS - step 34')
except Exception as e:
    print('FAIL - step 34' if isinstance(e, AssertionError) else f'ERROR - step 34: {e}')

print("STEP 35 - Check element meta#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "meta")))
    print('PASS - step 35')
except Exception as e:
    print('FAIL - step 35' if isinstance(e, AssertionError) else f'ERROR - step 35: {e}')

print("STEP 36 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 36')
except Exception as e:
    print('FAIL - step 36' if isinstance(e, AssertionError) else f'ERROR - step 36: {e}')

print("STEP 37 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 37')
except Exception as e:
    print('FAIL - step 37' if isinstance(e, AssertionError) else f'ERROR - step 37: {e}')

print("STEP 38 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 38')
except Exception as e:
    print('FAIL - step 38' if isinstance(e, AssertionError) else f'ERROR - step 38: {e}')

print("STEP 39 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 39')
except Exception as e:
    print('FAIL - step 39' if isinstance(e, AssertionError) else f'ERROR - step 39: {e}')

print("STEP 40 - Check element script#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "script")))
    print('PASS - step 40')
except Exception as e:
    print('FAIL - step 40' if isinstance(e, AssertionError) else f'ERROR - step 40: {e}')

print("STEP 41 - Check element script#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "script")))
    print('PASS - step 41')
except Exception as e:
    print('FAIL - step 41' if isinstance(e, AssertionError) else f'ERROR - step 41: {e}')

print("STEP 42 - Check element script#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "script")))
    print('PASS - step 42')
except Exception as e:
    print('FAIL - step 42' if isinstance(e, AssertionError) else f'ERROR - step 42: {e}')

print("STEP 43 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 43')
except Exception as e:
    print('FAIL - step 43' if isinstance(e, AssertionError) else f'ERROR - step 43: {e}')

print("STEP 44 - Check element script#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "script")))
    print('PASS - step 44')
except Exception as e:
    print('FAIL - step 44' if isinstance(e, AssertionError) else f'ERROR - step 44: {e}')

print("STEP 45 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 45')
except Exception as e:
    print('FAIL - step 45' if isinstance(e, AssertionError) else f'ERROR - step 45: {e}')

print("STEP 46 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 46')
except Exception as e:
    print('FAIL - step 46' if isinstance(e, AssertionError) else f'ERROR - step 46: {e}')

print("STEP 47 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 47')
except Exception as e:
    print('FAIL - step 47' if isinstance(e, AssertionError) else f'ERROR - step 47: {e}')

print("STEP 48 - Check element script#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "script")))
    print('PASS - step 48')
except Exception as e:
    print('FAIL - step 48' if isinstance(e, AssertionError) else f'ERROR - step 48: {e}')

print("STEP 49 - Check element script#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "script")))
    print('PASS - step 49')
except Exception as e:
    print('FAIL - step 49' if isinstance(e, AssertionError) else f'ERROR - step 49: {e}')

print("STEP 50 - Check element script#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "script")))
    print('PASS - step 50')
except Exception as e:
    print('FAIL - step 50' if isinstance(e, AssertionError) else f'ERROR - step 50: {e}')

print("STEP 51 - Check element script#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "script")))
    print('PASS - step 51')
except Exception as e:
    print('FAIL - step 51' if isinstance(e, AssertionError) else f'ERROR - step 51: {e}')

print("STEP 52 - Check element script#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "script")))
    print('PASS - step 52')
except Exception as e:
    print('FAIL - step 52' if isinstance(e, AssertionError) else f'ERROR - step 52: {e}')

print("STEP 53 - Check element style#onetrust-style.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "onetrust-style")))
    print('PASS - step 53')
except Exception as e:
    print('FAIL - step 53' if isinstance(e, AssertionError) else f'ERROR - step 53: {e}')

print("STEP 54 - Check element body#None.['page', 'basicpage', 'default', 'chrome', 'windows', 'hpgn-footer-v2', 'left-to-right']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['page', 'basicpage', 'default', 'chrome', 'windows', 'hpgn-footer-v2', 'left-to-right']")))
    print('PASS - step 54')
except Exception as e:
    print('FAIL - step 54' if isinstance(e, AssertionError) else f'ERROR - step 54: {e}')

print("STEP 55 - Check element noscript#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "noscript")))
    print('PASS - step 55')
except Exception as e:
    print('FAIL - step 55' if isinstance(e, AssertionError) else f'ERROR - step 55: {e}')

print("STEP 56 - Check element iframe#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
    print('PASS - step 56')
except Exception as e:
    print('FAIL - step 56' if isinstance(e, AssertionError) else f'ERROR - step 56: {e}')

print("STEP 57 - Check element script#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "script")))
    print('PASS - step 57')
except Exception as e:
    print('FAIL - step 57' if isinstance(e, AssertionError) else f'ERROR - step 57: {e}')

print("STEP 58 - Check element div#everything.['everything']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "everything")))
    print('PASS - step 58')
except Exception as e:
    print('FAIL - step 58' if isinstance(e, AssertionError) else f'ERROR - step 58: {e}')

print("STEP 59 - Check element div#content.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "content")))
    print('PASS - step 59')
except Exception as e:
    print('FAIL - step 59' if isinstance(e, AssertionError) else f'ERROR - step 59: {e}')

print("STEP 60 - Check element section#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "section")))
    print('PASS - step 60')
except Exception as e:
    print('FAIL - step 60' if isinstance(e, AssertionError) else f'ERROR - step 60: {e}')

print("STEP 61 - Check element meta#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "meta")))
    print('PASS - step 61')
except Exception as e:
    print('FAIL - step 61' if isinstance(e, AssertionError) else f'ERROR - step 61: {e}')

print("STEP 62 - Check element meta#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "meta")))
    print('PASS - step 62')
except Exception as e:
    print('FAIL - step 62' if isinstance(e, AssertionError) else f'ERROR - step 62: {e}')

print("STEP 63 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 63')
except Exception as e:
    print('FAIL - step 63' if isinstance(e, AssertionError) else f'ERROR - step 63: {e}')

print("STEP 64 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 64')
except Exception as e:
    print('FAIL - step 64' if isinstance(e, AssertionError) else f'ERROR - step 64: {e}')

print("STEP 65 - Check element div#header.['header']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "header")))
    print('PASS - step 65')
except Exception as e:
    print('FAIL - step 65' if isinstance(e, AssertionError) else f'ERROR - step 65: {e}')

print("STEP 66 - Check element div#None.['wps-header-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wps-header-wrapper']")))
    print('PASS - step 66')
except Exception as e:
    print('FAIL - step 66' if isinstance(e, AssertionError) else f'ERROR - step 66: {e}')

print("STEP 67 - Check element div#None.['wps-mobile']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wps-mobile']")))
    print('PASS - step 67')
except Exception as e:
    print('FAIL - step 67' if isinstance(e, AssertionError) else f'ERROR - step 67: {e}')

print("STEP 68 - Check element nav#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "nav")))
    print('PASS - step 68')
except Exception as e:
    print('FAIL - step 68' if isinstance(e, AssertionError) else f'ERROR - step 68: {e}')

print("STEP 69 - Check element div#None.['wpr-header-tab']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-header-tab']")))
    print('PASS - step 69')
except Exception as e:
    print('FAIL - step 69' if isinstance(e, AssertionError) else f'ERROR - step 69: {e}')

print("STEP 70 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 70')
except Exception as e:
    print('FAIL - step 70' if isinstance(e, AssertionError) else f'ERROR - step 70: {e}')

print("STEP 71 - Check element span#None.['wpr-skip-links']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-skip-links']")))
    print('PASS - step 71')
except Exception as e:
    print('FAIL - step 71' if isinstance(e, AssertionError) else f'ERROR - step 71: {e}')

print("STEP 72 - Check element a#None.['js-skip-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['js-skip-link']")))
    print('PASS - step 72')
except Exception as e:
    print('FAIL - step 72' if isinstance(e, AssertionError) else f'ERROR - step 72: {e}')

print("STEP 73 - Check element a#None.['js-skip-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['js-skip-link']")))
    print('PASS - step 73')
except Exception as e:
    print('FAIL - step 73' if isinstance(e, AssertionError) else f'ERROR - step 73: {e}')

print("STEP 74 - Check element div#None.['wpr-logo-holder']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-logo-holder']")))
    print('PASS - step 74')
except Exception as e:
    print('FAIL - step 74' if isinstance(e, AssertionError) else f'ERROR - step 74: {e}')

print("STEP 75 - Check element a#None.['wpr-main-logo-svg']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-main-logo-svg']")))
    print('PASS - step 75')
except Exception as e:
    print('FAIL - step 75' if isinstance(e, AssertionError) else f'ERROR - step 75: {e}')

print("STEP 76 - Check element div#None.['wpr-icons-holder']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-icons-holder']")))
    print('PASS - step 76')
except Exception as e:
    print('FAIL - step 76' if isinstance(e, AssertionError) else f'ERROR - step 76: {e}')

print("STEP 77 - Check element div#None.['wpr-search-icon', 'wpr-icon-center']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-search-icon', 'wpr-icon-center']")))
    print('PASS - step 77')
except Exception as e:
    print('FAIL - step 77' if isinstance(e, AssertionError) else f'ERROR - step 77: {e}')

print("STEP 78 - Check element a#None.['wpr-search-icon-logo']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-search-icon-logo']")))
    print('PASS - step 78')
except Exception as e:
    print('FAIL - step 78' if isinstance(e, AssertionError) else f'ERROR - step 78: {e}')

print("STEP 79 - Check element div#None.['arrows_search_mobile']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['arrows_search_mobile']")))
    print('PASS - step 79')
except Exception as e:
    print('FAIL - step 79' if isinstance(e, AssertionError) else f'ERROR - step 79: {e}')

print("STEP 80 - Check element div#None.['top_arrow']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['top_arrow']")))
    print('PASS - step 80')
except Exception as e:
    print('FAIL - step 80' if isinstance(e, AssertionError) else f'ERROR - step 80: {e}')

print("STEP 81 - Check element div#None.['bottom_arrow']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['bottom_arrow']")))
    print('PASS - step 81')
except Exception as e:
    print('FAIL - step 81' if isinstance(e, AssertionError) else f'ERROR - step 81: {e}')

print("STEP 82 - Check element div#wpr-signin.['wpr-icon-center', 'wpr-signin']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "wpr-signin")))
    print('PASS - step 82')
except Exception as e:
    print('FAIL - step 82' if isinstance(e, AssertionError) else f'ERROR - step 82: {e}')

print("STEP 83 - Check element div#None.['signin-loader']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['signin-loader']")))
    print('PASS - step 83')
except Exception as e:
    print('FAIL - step 83' if isinstance(e, AssertionError) else f'ERROR - step 83: {e}')

print("STEP 84 - Check element span#None.['signin-profile-image']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['signin-profile-image']")))
    print('PASS - step 84')
except Exception as e:
    print('FAIL - step 84' if isinstance(e, AssertionError) else f'ERROR - step 84: {e}')

print("STEP 85 - Check element a#None.['signin-button', 'hidden']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['signin-button', 'hidden']")))
    print('PASS - step 85')
except Exception as e:
    print('FAIL - step 85' if isinstance(e, AssertionError) else f'ERROR - step 85: {e}')

print("STEP 86 - Check element span#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "span")))
    print('PASS - step 86')
except Exception as e:
    print('FAIL - step 86' if isinstance(e, AssertionError) else f'ERROR - step 86: {e}')

print("STEP 87 - Check element p#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "p")))
    print('PASS - step 87')
except Exception as e:
    print('FAIL - step 87' if isinstance(e, AssertionError) else f'ERROR - step 87: {e}')

print("STEP 88 - Check element div#None.['wpr-signin-arrows']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-signin-arrows']")))
    print('PASS - step 88')
except Exception as e:
    print('FAIL - step 88' if isinstance(e, AssertionError) else f'ERROR - step 88: {e}')

print("STEP 89 - Check element div#None.['top_arrow']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['top_arrow']")))
    print('PASS - step 89')
except Exception as e:
    print('FAIL - step 89' if isinstance(e, AssertionError) else f'ERROR - step 89: {e}')

print("STEP 90 - Check element div#None.['bottom_arrow']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['bottom_arrow']")))
    print('PASS - step 90')
except Exception as e:
    print('FAIL - step 90' if isinstance(e, AssertionError) else f'ERROR - step 90: {e}')

print("STEP 91 - Check element div#wpr-hamburger.['wpr-menu-icon', 'wpr-icon-center']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "wpr-hamburger")))
    print('PASS - step 91')
except Exception as e:
    print('FAIL - step 91' if isinstance(e, AssertionError) else f'ERROR - step 91: {e}')

print("STEP 92 - Check element a#None.['wpr-menu-icon-logo']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-menu-icon-logo']")))
    print('PASS - step 92')
except Exception as e:
    print('FAIL - step 92' if isinstance(e, AssertionError) else f'ERROR - step 92: {e}')

print("STEP 93 - Check element div#None.['wpr-signin-menu']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-signin-menu']")))
    print('PASS - step 93')
except Exception as e:
    print('FAIL - step 93' if isinstance(e, AssertionError) else f'ERROR - step 93: {e}')

print("STEP 94 - Check element div#None.['wpr-signin-menu-item', 'signed-menu-item', 'user-info']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-signin-menu-item', 'signed-menu-item', 'user-info']")))
    print('PASS - step 94')
except Exception as e:
    print('FAIL - step 94' if isinstance(e, AssertionError) else f'ERROR - step 94: {e}')

print("STEP 95 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 95')
except Exception as e:
    print('FAIL - step 95' if isinstance(e, AssertionError) else f'ERROR - step 95: {e}')

print("STEP 96 - Check element span#signin-profile-image.['signin-profile-image']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "signin-profile-image")))
    print('PASS - step 96')
except Exception as e:
    print('FAIL - step 96' if isinstance(e, AssertionError) else f'ERROR - step 96: {e}')

print("STEP 97 - Check element p#None.['first-letter']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['first-letter']")))
    print('PASS - step 97')
except Exception as e:
    print('FAIL - step 97' if isinstance(e, AssertionError) else f'ERROR - step 97: {e}')

print("STEP 98 - Check element div#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 98')
except Exception as e:
    print('FAIL - step 98' if isinstance(e, AssertionError) else f'ERROR - step 98: {e}')

print("STEP 99 - Check element span#signin-profile-name.['signin-profile-name']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "signin-profile-name")))
    print('PASS - step 99')
except Exception as e:
    print('FAIL - step 99' if isinstance(e, AssertionError) else f'ERROR - step 99: {e}')

print("STEP 100 - Check element span#signin-profile-email.['signin-profile-email']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "signin-profile-email")))
    print('PASS - step 100')
except Exception as e:
    print('FAIL - step 100' if isinstance(e, AssertionError) else f'ERROR - step 100: {e}')

print("STEP 101 - Check element span#signin-profile-settings.['signin-profile-settings']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "signin-profile-settings")))
    print('PASS - step 101')
except Exception as e:
    print('FAIL - step 101' if isinstance(e, AssertionError) else f'ERROR - step 101: {e}')

print("STEP 102 - Check element a#None.['myAccount', 'link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['myAccount', 'link_metrics']")))
    print('PASS - step 102')
except Exception as e:
    print('FAIL - step 102' if isinstance(e, AssertionError) else f'ERROR - step 102: {e}')

print("STEP 103 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 103')
except Exception as e:
    print('FAIL - step 103' if isinstance(e, AssertionError) else f'ERROR - step 103: {e}')

print("STEP 104 - Check element div#None.['wpr-signin-menu-item', 'signed-menu-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-signin-menu-item', 'signed-menu-item']")))
    print('PASS - step 104')
except Exception as e:
    print('FAIL - step 104' if isinstance(e, AssertionError) else f'ERROR - step 104: {e}')

print("STEP 105 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 105')
except Exception as e:
    print('FAIL - step 105' if isinstance(e, AssertionError) else f'ERROR - step 105: {e}')

print("STEP 106 - Check element div#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 106')
except Exception as e:
    print('FAIL - step 106' if isinstance(e, AssertionError) else f'ERROR - step 106: {e}')

print("STEP 107 - Check element span#None.['screenReadingText']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['screenReadingText']")))
    print('PASS - step 107')
except Exception as e:
    print('FAIL - step 107' if isinstance(e, AssertionError) else f'ERROR - step 107: {e}')

print("STEP 108 - Check element a#signoutButton-mobile.['signoutButton', 'link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "signoutButton-mobile")))
    print('PASS - step 108')
except Exception as e:
    print('FAIL - step 108' if isinstance(e, AssertionError) else f'ERROR - step 108: {e}')

print("STEP 109 - Check element div#None.['wpr-signin-menu-item', 'signed-menu-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-signin-menu-item', 'signed-menu-item']")))
    print('PASS - step 109')
except Exception as e:
    print('FAIL - step 109' if isinstance(e, AssertionError) else f'ERROR - step 109: {e}')

print("STEP 110 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 110')
except Exception as e:
    print('FAIL - step 110' if isinstance(e, AssertionError) else f'ERROR - step 110: {e}')

print("STEP 111 - Check element div#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 111')
except Exception as e:
    print('FAIL - step 111' if isinstance(e, AssertionError) else f'ERROR - step 111: {e}')

print("STEP 112 - Check element span#None.['screenReadingText']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['screenReadingText']")))
    print('PASS - step 112')
except Exception as e:
    print('FAIL - step 112' if isinstance(e, AssertionError) else f'ERROR - step 112: {e}')

print("STEP 113 - Check element div#None.['wpr-navbar-container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-navbar-container']")))
    print('PASS - step 113')
except Exception as e:
    print('FAIL - step 113' if isinstance(e, AssertionError) else f'ERROR - step 113: {e}')

print("STEP 114 - Check element div#None.['wpr-side-nav']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-side-nav']")))
    print('PASS - step 114')
except Exception as e:
    print('FAIL - step 114' if isinstance(e, AssertionError) else f'ERROR - step 114: {e}')

print("STEP 115 - Check element div#None.['wpr-side-nav-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-side-nav-row']")))
    print('PASS - step 115')
except Exception as e:
    print('FAIL - step 115' if isinstance(e, AssertionError) else f'ERROR - step 115: {e}')

print("STEP 116 - Check element div#wpr-close-button.['wpr-close-button']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "wpr-close-button")))
    print('PASS - step 116')
except Exception as e:
    print('FAIL - step 116' if isinstance(e, AssertionError) else f'ERROR - step 116: {e}')

print("STEP 117 - Check element a#None.['close_icon_desk']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['close_icon_desk']")))
    print('PASS - step 117')
except Exception as e:
    print('FAIL - step 117' if isinstance(e, AssertionError) else f'ERROR - step 117: {e}')

print("STEP 118 - Check element div#None.['mobile-menu-output']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['mobile-menu-output']")))
    print('PASS - step 118')
except Exception as e:
    print('FAIL - step 118' if isinstance(e, AssertionError) else f'ERROR - step 118: {e}')

print("STEP 119 - Check element div#menuitemOne.['Rectangle-515']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "menuitemOne")))
    print('PASS - step 119')
except Exception as e:
    print('FAIL - step 119' if isinstance(e, AssertionError) else f'ERROR - step 119: {e}')

print("STEP 120 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 120')
except Exception as e:
    print('FAIL - step 120' if isinstance(e, AssertionError) else f'ERROR - step 120: {e}')

print("STEP 121 - Check element div#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 121')
except Exception as e:
    print('FAIL - step 121' if isinstance(e, AssertionError) else f'ERROR - step 121: {e}')

print("STEP 122 - Check element label#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "label")))
    print('PASS - step 122')
except Exception as e:
    print('FAIL - step 122' if isinstance(e, AssertionError) else f'ERROR - step 122: {e}')

print("STEP 123 - Check element span#None.['screenReadingText']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['screenReadingText']")))
    print('PASS - step 123')
except Exception as e:
    print('FAIL - step 123' if isinstance(e, AssertionError) else f'ERROR - step 123: {e}')

print("STEP 124 - Check element a#None.['forward_icon']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['forward_icon']")))
    print('PASS - step 124')
except Exception as e:
    print('FAIL - step 124' if isinstance(e, AssertionError) else f'ERROR - step 124: {e}')

print("STEP 125 - Check element div#None.['Line-208']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Line-208']")))
    print('PASS - step 125')
except Exception as e:
    print('FAIL - step 125' if isinstance(e, AssertionError) else f'ERROR - step 125: {e}')

print("STEP 126 - Check element div#menuitemTwo.['Rectangle-515']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "menuitemTwo")))
    print('PASS - step 126')
except Exception as e:
    print('FAIL - step 126' if isinstance(e, AssertionError) else f'ERROR - step 126: {e}')

print("STEP 127 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 127')
except Exception as e:
    print('FAIL - step 127' if isinstance(e, AssertionError) else f'ERROR - step 127: {e}')

print("STEP 128 - Check element div#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 128')
except Exception as e:
    print('FAIL - step 128' if isinstance(e, AssertionError) else f'ERROR - step 128: {e}')

print("STEP 129 - Check element label#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "label")))
    print('PASS - step 129')
except Exception as e:
    print('FAIL - step 129' if isinstance(e, AssertionError) else f'ERROR - step 129: {e}')

print("STEP 130 - Check element span#None.['screenReadingText']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['screenReadingText']")))
    print('PASS - step 130')
except Exception as e:
    print('FAIL - step 130' if isinstance(e, AssertionError) else f'ERROR - step 130: {e}')

print("STEP 131 - Check element a#None.['forward_icon']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['forward_icon']")))
    print('PASS - step 131')
except Exception as e:
    print('FAIL - step 131' if isinstance(e, AssertionError) else f'ERROR - step 131: {e}')

print("STEP 132 - Check element div#None.['Line-208']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Line-208']")))
    print('PASS - step 132')
except Exception as e:
    print('FAIL - step 132' if isinstance(e, AssertionError) else f'ERROR - step 132: {e}')

print("STEP 133 - Check element div#menuitemThree.['Rectangle-515']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "menuitemThree")))
    print('PASS - step 133')
except Exception as e:
    print('FAIL - step 133' if isinstance(e, AssertionError) else f'ERROR - step 133: {e}')

print("STEP 134 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 134')
except Exception as e:
    print('FAIL - step 134' if isinstance(e, AssertionError) else f'ERROR - step 134: {e}')

print("STEP 135 - Check element div#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 135')
except Exception as e:
    print('FAIL - step 135' if isinstance(e, AssertionError) else f'ERROR - step 135: {e}')

print("STEP 136 - Check element label#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "label")))
    print('PASS - step 136')
except Exception as e:
    print('FAIL - step 136' if isinstance(e, AssertionError) else f'ERROR - step 136: {e}')

print("STEP 137 - Check element span#None.['screenReadingText']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['screenReadingText']")))
    print('PASS - step 137')
except Exception as e:
    print('FAIL - step 137' if isinstance(e, AssertionError) else f'ERROR - step 137: {e}')

print("STEP 138 - Check element a#None.['forward_icon']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['forward_icon']")))
    print('PASS - step 138')
except Exception as e:
    print('FAIL - step 138' if isinstance(e, AssertionError) else f'ERROR - step 138: {e}')

print("STEP 139 - Check element div#None.['Line-208']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Line-208']")))
    print('PASS - step 139')
except Exception as e:
    print('FAIL - step 139' if isinstance(e, AssertionError) else f'ERROR - step 139: {e}')

print("STEP 140 - Check element div#None.['mobile-level-two-menu']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['mobile-level-two-menu']")))
    print('PASS - step 140')
except Exception as e:
    print('FAIL - step 140' if isinstance(e, AssertionError) else f'ERROR - step 140: {e}')

print("STEP 141 - Check element div#menuitemOne_sub.['wpr-side-nav-submenu']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "menuitemOne_sub")))
    print('PASS - step 141')
except Exception as e:
    print('FAIL - step 141' if isinstance(e, AssertionError) else f'ERROR - step 141: {e}')

print("STEP 142 - Check element div#None.['wpr-side-nav-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-side-nav-row']")))
    print('PASS - step 142')
except Exception as e:
    print('FAIL - step 142' if isinstance(e, AssertionError) else f'ERROR - step 142: {e}')

print("STEP 143 - Check element div#None.['header-submenu']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['header-submenu']")))
    print('PASS - step 143')
except Exception as e:
    print('FAIL - step 143' if isinstance(e, AssertionError) else f'ERROR - step 143: {e}')

print("STEP 144 - Check element a#None.['back_icon']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['back_icon']")))
    print('PASS - step 144')
except Exception as e:
    print('FAIL - step 144' if isinstance(e, AssertionError) else f'ERROR - step 144: {e}')

print("STEP 145 - Check element label#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "label")))
    print('PASS - step 145')
except Exception as e:
    print('FAIL - step 145' if isinstance(e, AssertionError) else f'ERROR - step 145: {e}')

print("STEP 146 - Check element div#wpr-close-button.['wpr-close-button-L2']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "wpr-close-button")))
    print('PASS - step 146')
except Exception as e:
    print('FAIL - step 146' if isinstance(e, AssertionError) else f'ERROR - step 146: {e}')

print("STEP 147 - Check element a#None.['close_icon_desk']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['close_icon_desk']")))
    print('PASS - step 147')
except Exception as e:
    print('FAIL - step 147' if isinstance(e, AssertionError) else f'ERROR - step 147: {e}')

print("STEP 148 - Check element div#None.['mobile-submenu-items']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['mobile-submenu-items']")))
    print('PASS - step 148')
except Exception as e:
    print('FAIL - step 148' if isinstance(e, AssertionError) else f'ERROR - step 148: {e}')

print("STEP 149 - Check element ul#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "ul")))
    print('PASS - step 149')
except Exception as e:
    print('FAIL - step 149' if isinstance(e, AssertionError) else f'ERROR - step 149: {e}')

print("STEP 150 - Check element div#None.['wpr-submenu-item-mobile']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-submenu-item-mobile']")))
    print('PASS - step 150')
except Exception as e:
    print('FAIL - step 150' if isinstance(e, AssertionError) else f'ERROR - step 150: {e}')

print("STEP 151 - Check element div#None.['wpr-submenu-heading']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-submenu-heading']")))
    print('PASS - step 151')
except Exception as e:
    print('FAIL - step 151' if isinstance(e, AssertionError) else f'ERROR - step 151: {e}')

print("STEP 152 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 152')
except Exception as e:
    print('FAIL - step 152' if isinstance(e, AssertionError) else f'ERROR - step 152: {e}')

print("STEP 153 - Check element li#None.['headind_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['headind_content']")))
    print('PASS - step 153')
except Exception as e:
    print('FAIL - step 153' if isinstance(e, AssertionError) else f'ERROR - step 153: {e}')

print("STEP 154 - Check element label#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "label")))
    print('PASS - step 154')
except Exception as e:
    print('FAIL - step 154' if isinstance(e, AssertionError) else f'ERROR - step 154: {e}')

print("STEP 155 - Check element div#None.['sub-submenu-data-mobile']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['sub-submenu-data-mobile']")))
    print('PASS - step 155')
except Exception as e:
    print('FAIL - step 155' if isinstance(e, AssertionError) else f'ERROR - step 155: {e}')

print("STEP 156 - Check element ul#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "ul")))
    print('PASS - step 156')
except Exception as e:
    print('FAIL - step 156' if isinstance(e, AssertionError) else f'ERROR - step 156: {e}')

print("STEP 157 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 157')
except Exception as e:
    print('FAIL - step 157' if isinstance(e, AssertionError) else f'ERROR - step 157: {e}')

print("STEP 158 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 158')
except Exception as e:
    print('FAIL - step 158' if isinstance(e, AssertionError) else f'ERROR - step 158: {e}')

print("STEP 159 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 159')
except Exception as e:
    print('FAIL - step 159' if isinstance(e, AssertionError) else f'ERROR - step 159: {e}')

print("STEP 160 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 160')
except Exception as e:
    print('FAIL - step 160' if isinstance(e, AssertionError) else f'ERROR - step 160: {e}')

print("STEP 161 - Check element label#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "label")))
    print('PASS - step 161')
except Exception as e:
    print('FAIL - step 161' if isinstance(e, AssertionError) else f'ERROR - step 161: {e}')

print("STEP 162 - Check element div#None.['Line-208']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Line-208']")))
    print('PASS - step 162')
except Exception as e:
    print('FAIL - step 162' if isinstance(e, AssertionError) else f'ERROR - step 162: {e}')

print("STEP 163 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 163')
except Exception as e:
    print('FAIL - step 163' if isinstance(e, AssertionError) else f'ERROR - step 163: {e}')

print("STEP 164 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 164')
except Exception as e:
    print('FAIL - step 164' if isinstance(e, AssertionError) else f'ERROR - step 164: {e}')

print("STEP 165 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 165')
except Exception as e:
    print('FAIL - step 165' if isinstance(e, AssertionError) else f'ERROR - step 165: {e}')

print("STEP 166 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 166')
except Exception as e:
    print('FAIL - step 166' if isinstance(e, AssertionError) else f'ERROR - step 166: {e}')

print("STEP 167 - Check element label#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "label")))
    print('PASS - step 167')
except Exception as e:
    print('FAIL - step 167' if isinstance(e, AssertionError) else f'ERROR - step 167: {e}')

print("STEP 168 - Check element div#None.['Line-208']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Line-208']")))
    print('PASS - step 168')
except Exception as e:
    print('FAIL - step 168' if isinstance(e, AssertionError) else f'ERROR - step 168: {e}')

print("STEP 169 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 169')
except Exception as e:
    print('FAIL - step 169' if isinstance(e, AssertionError) else f'ERROR - step 169: {e}')

print("STEP 170 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 170')
except Exception as e:
    print('FAIL - step 170' if isinstance(e, AssertionError) else f'ERROR - step 170: {e}')

print("STEP 171 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 171')
except Exception as e:
    print('FAIL - step 171' if isinstance(e, AssertionError) else f'ERROR - step 171: {e}')

print("STEP 172 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 172')
except Exception as e:
    print('FAIL - step 172' if isinstance(e, AssertionError) else f'ERROR - step 172: {e}')

print("STEP 173 - Check element label#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "label")))
    print('PASS - step 173')
except Exception as e:
    print('FAIL - step 173' if isinstance(e, AssertionError) else f'ERROR - step 173: {e}')

print("STEP 174 - Check element div#None.['Line-208']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Line-208']")))
    print('PASS - step 174')
except Exception as e:
    print('FAIL - step 174' if isinstance(e, AssertionError) else f'ERROR - step 174: {e}')

print("STEP 175 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 175')
except Exception as e:
    print('FAIL - step 175' if isinstance(e, AssertionError) else f'ERROR - step 175: {e}')

print("STEP 176 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 176')
except Exception as e:
    print('FAIL - step 176' if isinstance(e, AssertionError) else f'ERROR - step 176: {e}')

print("STEP 177 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 177')
except Exception as e:
    print('FAIL - step 177' if isinstance(e, AssertionError) else f'ERROR - step 177: {e}')

print("STEP 178 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 178')
except Exception as e:
    print('FAIL - step 178' if isinstance(e, AssertionError) else f'ERROR - step 178: {e}')

print("STEP 179 - Check element label#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "label")))
    print('PASS - step 179')
except Exception as e:
    print('FAIL - step 179' if isinstance(e, AssertionError) else f'ERROR - step 179: {e}')

print("STEP 180 - Check element div#None.['Line-208']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Line-208']")))
    print('PASS - step 180')
except Exception as e:
    print('FAIL - step 180' if isinstance(e, AssertionError) else f'ERROR - step 180: {e}')

print("STEP 181 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 181')
except Exception as e:
    print('FAIL - step 181' if isinstance(e, AssertionError) else f'ERROR - step 181: {e}')

print("STEP 182 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 182')
except Exception as e:
    print('FAIL - step 182' if isinstance(e, AssertionError) else f'ERROR - step 182: {e}')

print("STEP 183 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 183')
except Exception as e:
    print('FAIL - step 183' if isinstance(e, AssertionError) else f'ERROR - step 183: {e}')

print("STEP 184 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 184')
except Exception as e:
    print('FAIL - step 184' if isinstance(e, AssertionError) else f'ERROR - step 184: {e}')

print("STEP 185 - Check element label#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "label")))
    print('PASS - step 185')
except Exception as e:
    print('FAIL - step 185' if isinstance(e, AssertionError) else f'ERROR - step 185: {e}')

print("STEP 186 - Check element div#None.['Line-208']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Line-208']")))
    print('PASS - step 186')
except Exception as e:
    print('FAIL - step 186' if isinstance(e, AssertionError) else f'ERROR - step 186: {e}')

print("STEP 187 - Check element div#None.['wpr-submenu-item-mobile']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-submenu-item-mobile']")))
    print('PASS - step 187')
except Exception as e:
    print('FAIL - step 187' if isinstance(e, AssertionError) else f'ERROR - step 187: {e}')

print("STEP 188 - Check element div#None.['wpr-submenu-heading']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-submenu-heading']")))
    print('PASS - step 188')
except Exception as e:
    print('FAIL - step 188' if isinstance(e, AssertionError) else f'ERROR - step 188: {e}')

print("STEP 189 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 189')
except Exception as e:
    print('FAIL - step 189' if isinstance(e, AssertionError) else f'ERROR - step 189: {e}')

print("STEP 190 - Check element li#None.['headind_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['headind_content']")))
    print('PASS - step 190')
except Exception as e:
    print('FAIL - step 190' if isinstance(e, AssertionError) else f'ERROR - step 190: {e}')

print("STEP 191 - Check element label#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "label")))
    print('PASS - step 191')
except Exception as e:
    print('FAIL - step 191' if isinstance(e, AssertionError) else f'ERROR - step 191: {e}')

print("STEP 192 - Check element div#None.['sub-submenu-data-mobile']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['sub-submenu-data-mobile']")))
    print('PASS - step 192')
except Exception as e:
    print('FAIL - step 192' if isinstance(e, AssertionError) else f'ERROR - step 192: {e}')

print("STEP 193 - Check element ul#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "ul")))
    print('PASS - step 193')
except Exception as e:
    print('FAIL - step 193' if isinstance(e, AssertionError) else f'ERROR - step 193: {e}')

print("STEP 194 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 194')
except Exception as e:
    print('FAIL - step 194' if isinstance(e, AssertionError) else f'ERROR - step 194: {e}')

print("STEP 195 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 195')
except Exception as e:
    print('FAIL - step 195' if isinstance(e, AssertionError) else f'ERROR - step 195: {e}')

print("STEP 196 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 196')
except Exception as e:
    print('FAIL - step 196' if isinstance(e, AssertionError) else f'ERROR - step 196: {e}')

print("STEP 197 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 197')
except Exception as e:
    print('FAIL - step 197' if isinstance(e, AssertionError) else f'ERROR - step 197: {e}')

print("STEP 198 - Check element label#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "label")))
    print('PASS - step 198')
except Exception as e:
    print('FAIL - step 198' if isinstance(e, AssertionError) else f'ERROR - step 198: {e}')

print("STEP 199 - Check element div#None.['Line-208']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Line-208']")))
    print('PASS - step 199')
except Exception as e:
    print('FAIL - step 199' if isinstance(e, AssertionError) else f'ERROR - step 199: {e}')

print("STEP 200 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 200')
except Exception as e:
    print('FAIL - step 200' if isinstance(e, AssertionError) else f'ERROR - step 200: {e}')

print("STEP 201 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 201')
except Exception as e:
    print('FAIL - step 201' if isinstance(e, AssertionError) else f'ERROR - step 201: {e}')

print("STEP 202 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 202')
except Exception as e:
    print('FAIL - step 202' if isinstance(e, AssertionError) else f'ERROR - step 202: {e}')

print("STEP 203 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 203')
except Exception as e:
    print('FAIL - step 203' if isinstance(e, AssertionError) else f'ERROR - step 203: {e}')

print("STEP 204 - Check element label#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "label")))
    print('PASS - step 204')
except Exception as e:
    print('FAIL - step 204' if isinstance(e, AssertionError) else f'ERROR - step 204: {e}')

print("STEP 205 - Check element div#None.['Line-208']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Line-208']")))
    print('PASS - step 205')
except Exception as e:
    print('FAIL - step 205' if isinstance(e, AssertionError) else f'ERROR - step 205: {e}')

print("STEP 206 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 206')
except Exception as e:
    print('FAIL - step 206' if isinstance(e, AssertionError) else f'ERROR - step 206: {e}')

print("STEP 207 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 207')
except Exception as e:
    print('FAIL - step 207' if isinstance(e, AssertionError) else f'ERROR - step 207: {e}')

print("STEP 208 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 208')
except Exception as e:
    print('FAIL - step 208' if isinstance(e, AssertionError) else f'ERROR - step 208: {e}')

print("STEP 209 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 209')
except Exception as e:
    print('FAIL - step 209' if isinstance(e, AssertionError) else f'ERROR - step 209: {e}')

print("STEP 210 - Check element label#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "label")))
    print('PASS - step 210')
except Exception as e:
    print('FAIL - step 210' if isinstance(e, AssertionError) else f'ERROR - step 210: {e}')

print("STEP 211 - Check element div#None.['Line-208']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Line-208']")))
    print('PASS - step 211')
except Exception as e:
    print('FAIL - step 211' if isinstance(e, AssertionError) else f'ERROR - step 211: {e}')

print("STEP 212 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 212')
except Exception as e:
    print('FAIL - step 212' if isinstance(e, AssertionError) else f'ERROR - step 212: {e}')

print("STEP 213 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 213')
except Exception as e:
    print('FAIL - step 213' if isinstance(e, AssertionError) else f'ERROR - step 213: {e}')

print("STEP 214 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 214')
except Exception as e:
    print('FAIL - step 214' if isinstance(e, AssertionError) else f'ERROR - step 214: {e}')

print("STEP 215 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 215')
except Exception as e:
    print('FAIL - step 215' if isinstance(e, AssertionError) else f'ERROR - step 215: {e}')

print("STEP 216 - Check element label#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "label")))
    print('PASS - step 216')
except Exception as e:
    print('FAIL - step 216' if isinstance(e, AssertionError) else f'ERROR - step 216: {e}')

print("STEP 217 - Check element div#None.['Line-208']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Line-208']")))
    print('PASS - step 217')
except Exception as e:
    print('FAIL - step 217' if isinstance(e, AssertionError) else f'ERROR - step 217: {e}')

print("STEP 218 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 218')
except Exception as e:
    print('FAIL - step 218' if isinstance(e, AssertionError) else f'ERROR - step 218: {e}')

print("STEP 219 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 219')
except Exception as e:
    print('FAIL - step 219' if isinstance(e, AssertionError) else f'ERROR - step 219: {e}')

print("STEP 220 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 220')
except Exception as e:
    print('FAIL - step 220' if isinstance(e, AssertionError) else f'ERROR - step 220: {e}')

print("STEP 221 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 221')
except Exception as e:
    print('FAIL - step 221' if isinstance(e, AssertionError) else f'ERROR - step 221: {e}')

print("STEP 222 - Check element label#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "label")))
    print('PASS - step 222')
except Exception as e:
    print('FAIL - step 222' if isinstance(e, AssertionError) else f'ERROR - step 222: {e}')

print("STEP 223 - Check element div#None.['Line-208']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Line-208']")))
    print('PASS - step 223')
except Exception as e:
    print('FAIL - step 223' if isinstance(e, AssertionError) else f'ERROR - step 223: {e}')

print("STEP 224 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 224')
except Exception as e:
    print('FAIL - step 224' if isinstance(e, AssertionError) else f'ERROR - step 224: {e}')

print("STEP 225 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 225')
except Exception as e:
    print('FAIL - step 225' if isinstance(e, AssertionError) else f'ERROR - step 225: {e}')

print("STEP 226 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 226')
except Exception as e:
    print('FAIL - step 226' if isinstance(e, AssertionError) else f'ERROR - step 226: {e}')

print("STEP 227 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 227')
except Exception as e:
    print('FAIL - step 227' if isinstance(e, AssertionError) else f'ERROR - step 227: {e}')

print("STEP 228 - Check element label#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "label")))
    print('PASS - step 228')
except Exception as e:
    print('FAIL - step 228' if isinstance(e, AssertionError) else f'ERROR - step 228: {e}')

print("STEP 229 - Check element div#None.['Line-208']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Line-208']")))
    print('PASS - step 229')
except Exception as e:
    print('FAIL - step 229' if isinstance(e, AssertionError) else f'ERROR - step 229: {e}')

print("STEP 230 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 230')
except Exception as e:
    print('FAIL - step 230' if isinstance(e, AssertionError) else f'ERROR - step 230: {e}')

print("STEP 231 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 231')
except Exception as e:
    print('FAIL - step 231' if isinstance(e, AssertionError) else f'ERROR - step 231: {e}')

print("STEP 232 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 232')
except Exception as e:
    print('FAIL - step 232' if isinstance(e, AssertionError) else f'ERROR - step 232: {e}')

print("STEP 233 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 233')
except Exception as e:
    print('FAIL - step 233' if isinstance(e, AssertionError) else f'ERROR - step 233: {e}')

print("STEP 234 - Check element label#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "label")))
    print('PASS - step 234')
except Exception as e:
    print('FAIL - step 234' if isinstance(e, AssertionError) else f'ERROR - step 234: {e}')

print("STEP 235 - Check element div#None.['Line-208']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Line-208']")))
    print('PASS - step 235')
except Exception as e:
    print('FAIL - step 235' if isinstance(e, AssertionError) else f'ERROR - step 235: {e}')

print("STEP 236 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 236')
except Exception as e:
    print('FAIL - step 236' if isinstance(e, AssertionError) else f'ERROR - step 236: {e}')

print("STEP 237 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 237')
except Exception as e:
    print('FAIL - step 237' if isinstance(e, AssertionError) else f'ERROR - step 237: {e}')

print("STEP 238 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 238')
except Exception as e:
    print('FAIL - step 238' if isinstance(e, AssertionError) else f'ERROR - step 238: {e}')

print("STEP 239 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 239')
except Exception as e:
    print('FAIL - step 239' if isinstance(e, AssertionError) else f'ERROR - step 239: {e}')

print("STEP 240 - Check element label#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "label")))
    print('PASS - step 240')
except Exception as e:
    print('FAIL - step 240' if isinstance(e, AssertionError) else f'ERROR - step 240: {e}')

print("STEP 241 - Check element div#None.['Line-208']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Line-208']")))
    print('PASS - step 241')
except Exception as e:
    print('FAIL - step 241' if isinstance(e, AssertionError) else f'ERROR - step 241: {e}')

print("STEP 242 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 242')
except Exception as e:
    print('FAIL - step 242' if isinstance(e, AssertionError) else f'ERROR - step 242: {e}')

print("STEP 243 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 243')
except Exception as e:
    print('FAIL - step 243' if isinstance(e, AssertionError) else f'ERROR - step 243: {e}')

print("STEP 244 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 244')
except Exception as e:
    print('FAIL - step 244' if isinstance(e, AssertionError) else f'ERROR - step 244: {e}')

print("STEP 245 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 245')
except Exception as e:
    print('FAIL - step 245' if isinstance(e, AssertionError) else f'ERROR - step 245: {e}')

print("STEP 246 - Check element label#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "label")))
    print('PASS - step 246')
except Exception as e:
    print('FAIL - step 246' if isinstance(e, AssertionError) else f'ERROR - step 246: {e}')

print("STEP 247 - Check element div#None.['Line-208']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Line-208']")))
    print('PASS - step 247')
except Exception as e:
    print('FAIL - step 247' if isinstance(e, AssertionError) else f'ERROR - step 247: {e}')

print("STEP 248 - Check element div#None.['wpr-submenu-item-mobile']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-submenu-item-mobile']")))
    print('PASS - step 248')
except Exception as e:
    print('FAIL - step 248' if isinstance(e, AssertionError) else f'ERROR - step 248: {e}')

print("STEP 249 - Check element div#None.['wpr-submenu-heading']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-submenu-heading']")))
    print('PASS - step 249')
except Exception as e:
    print('FAIL - step 249' if isinstance(e, AssertionError) else f'ERROR - step 249: {e}')

print("STEP 250 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 250')
except Exception as e:
    print('FAIL - step 250' if isinstance(e, AssertionError) else f'ERROR - step 250: {e}')

print("STEP 251 - Check element li#None.['headind_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['headind_content']")))
    print('PASS - step 251')
except Exception as e:
    print('FAIL - step 251' if isinstance(e, AssertionError) else f'ERROR - step 251: {e}')

print("STEP 252 - Check element label#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "label")))
    print('PASS - step 252')
except Exception as e:
    print('FAIL - step 252' if isinstance(e, AssertionError) else f'ERROR - step 252: {e}')

print("STEP 253 - Check element div#None.['sub-submenu-data-mobile']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['sub-submenu-data-mobile']")))
    print('PASS - step 253')
except Exception as e:
    print('FAIL - step 253' if isinstance(e, AssertionError) else f'ERROR - step 253: {e}')

print("STEP 254 - Check element ul#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "ul")))
    print('PASS - step 254')
except Exception as e:
    print('FAIL - step 254' if isinstance(e, AssertionError) else f'ERROR - step 254: {e}')

print("STEP 255 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 255')
except Exception as e:
    print('FAIL - step 255' if isinstance(e, AssertionError) else f'ERROR - step 255: {e}')

print("STEP 256 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 256')
except Exception as e:
    print('FAIL - step 256' if isinstance(e, AssertionError) else f'ERROR - step 256: {e}')

print("STEP 257 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 257')
except Exception as e:
    print('FAIL - step 257' if isinstance(e, AssertionError) else f'ERROR - step 257: {e}')

print("STEP 258 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 258')
except Exception as e:
    print('FAIL - step 258' if isinstance(e, AssertionError) else f'ERROR - step 258: {e}')

print("STEP 259 - Check element label#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "label")))
    print('PASS - step 259')
except Exception as e:
    print('FAIL - step 259' if isinstance(e, AssertionError) else f'ERROR - step 259: {e}')

print("STEP 260 - Check element div#None.['Line-208']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Line-208']")))
    print('PASS - step 260')
except Exception as e:
    print('FAIL - step 260' if isinstance(e, AssertionError) else f'ERROR - step 260: {e}')

print("STEP 261 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 261')
except Exception as e:
    print('FAIL - step 261' if isinstance(e, AssertionError) else f'ERROR - step 261: {e}')

print("STEP 262 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 262')
except Exception as e:
    print('FAIL - step 262' if isinstance(e, AssertionError) else f'ERROR - step 262: {e}')

print("STEP 263 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 263')
except Exception as e:
    print('FAIL - step 263' if isinstance(e, AssertionError) else f'ERROR - step 263: {e}')

print("STEP 264 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 264')
except Exception as e:
    print('FAIL - step 264' if isinstance(e, AssertionError) else f'ERROR - step 264: {e}')

print("STEP 265 - Check element label#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "label")))
    print('PASS - step 265')
except Exception as e:
    print('FAIL - step 265' if isinstance(e, AssertionError) else f'ERROR - step 265: {e}')

print("STEP 266 - Check element div#None.['Line-208']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Line-208']")))
    print('PASS - step 266')
except Exception as e:
    print('FAIL - step 266' if isinstance(e, AssertionError) else f'ERROR - step 266: {e}')

print("STEP 267 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 267')
except Exception as e:
    print('FAIL - step 267' if isinstance(e, AssertionError) else f'ERROR - step 267: {e}')

print("STEP 268 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 268')
except Exception as e:
    print('FAIL - step 268' if isinstance(e, AssertionError) else f'ERROR - step 268: {e}')

print("STEP 269 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 269')
except Exception as e:
    print('FAIL - step 269' if isinstance(e, AssertionError) else f'ERROR - step 269: {e}')

print("STEP 270 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 270')
except Exception as e:
    print('FAIL - step 270' if isinstance(e, AssertionError) else f'ERROR - step 270: {e}')

print("STEP 271 - Check element label#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "label")))
    print('PASS - step 271')
except Exception as e:
    print('FAIL - step 271' if isinstance(e, AssertionError) else f'ERROR - step 271: {e}')

print("STEP 272 - Check element div#None.['Line-208']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Line-208']")))
    print('PASS - step 272')
except Exception as e:
    print('FAIL - step 272' if isinstance(e, AssertionError) else f'ERROR - step 272: {e}')

print("STEP 273 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 273')
except Exception as e:
    print('FAIL - step 273' if isinstance(e, AssertionError) else f'ERROR - step 273: {e}')

print("STEP 274 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 274')
except Exception as e:
    print('FAIL - step 274' if isinstance(e, AssertionError) else f'ERROR - step 274: {e}')

print("STEP 275 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 275')
except Exception as e:
    print('FAIL - step 275' if isinstance(e, AssertionError) else f'ERROR - step 275: {e}')

print("STEP 276 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 276')
except Exception as e:
    print('FAIL - step 276' if isinstance(e, AssertionError) else f'ERROR - step 276: {e}')

print("STEP 277 - Check element label#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "label")))
    print('PASS - step 277')
except Exception as e:
    print('FAIL - step 277' if isinstance(e, AssertionError) else f'ERROR - step 277: {e}')

print("STEP 278 - Check element div#None.['Line-208']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Line-208']")))
    print('PASS - step 278')
except Exception as e:
    print('FAIL - step 278' if isinstance(e, AssertionError) else f'ERROR - step 278: {e}')

print("STEP 279 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 279')
except Exception as e:
    print('FAIL - step 279' if isinstance(e, AssertionError) else f'ERROR - step 279: {e}')

print("STEP 280 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 280')
except Exception as e:
    print('FAIL - step 280' if isinstance(e, AssertionError) else f'ERROR - step 280: {e}')

print("STEP 281 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 281')
except Exception as e:
    print('FAIL - step 281' if isinstance(e, AssertionError) else f'ERROR - step 281: {e}')

print("STEP 282 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 282')
except Exception as e:
    print('FAIL - step 282' if isinstance(e, AssertionError) else f'ERROR - step 282: {e}')

print("STEP 283 - Check element label#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "label")))
    print('PASS - step 283')
except Exception as e:
    print('FAIL - step 283' if isinstance(e, AssertionError) else f'ERROR - step 283: {e}')

print("STEP 284 - Check element div#None.['Line-208']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Line-208']")))
    print('PASS - step 284')
except Exception as e:
    print('FAIL - step 284' if isinstance(e, AssertionError) else f'ERROR - step 284: {e}')

print("STEP 285 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 285')
except Exception as e:
    print('FAIL - step 285' if isinstance(e, AssertionError) else f'ERROR - step 285: {e}')

print("STEP 286 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 286')
except Exception as e:
    print('FAIL - step 286' if isinstance(e, AssertionError) else f'ERROR - step 286: {e}')

print("STEP 287 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 287')
except Exception as e:
    print('FAIL - step 287' if isinstance(e, AssertionError) else f'ERROR - step 287: {e}')

print("STEP 288 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 288')
except Exception as e:
    print('FAIL - step 288' if isinstance(e, AssertionError) else f'ERROR - step 288: {e}')

print("STEP 289 - Check element label#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "label")))
    print('PASS - step 289')
except Exception as e:
    print('FAIL - step 289' if isinstance(e, AssertionError) else f'ERROR - step 289: {e}')

print("STEP 290 - Check element div#None.['Line-208']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Line-208']")))
    print('PASS - step 290')
except Exception as e:
    print('FAIL - step 290' if isinstance(e, AssertionError) else f'ERROR - step 290: {e}')

print("STEP 291 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 291')
except Exception as e:
    print('FAIL - step 291' if isinstance(e, AssertionError) else f'ERROR - step 291: {e}')

print("STEP 292 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 292')
except Exception as e:
    print('FAIL - step 292' if isinstance(e, AssertionError) else f'ERROR - step 292: {e}')

print("STEP 293 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 293')
except Exception as e:
    print('FAIL - step 293' if isinstance(e, AssertionError) else f'ERROR - step 293: {e}')

print("STEP 294 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 294')
except Exception as e:
    print('FAIL - step 294' if isinstance(e, AssertionError) else f'ERROR - step 294: {e}')

print("STEP 295 - Check element label#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "label")))
    print('PASS - step 295')
except Exception as e:
    print('FAIL - step 295' if isinstance(e, AssertionError) else f'ERROR - step 295: {e}')

print("STEP 296 - Check element div#None.['Line-208']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Line-208']")))
    print('PASS - step 296')
except Exception as e:
    print('FAIL - step 296' if isinstance(e, AssertionError) else f'ERROR - step 296: {e}')

print("STEP 297 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 297')
except Exception as e:
    print('FAIL - step 297' if isinstance(e, AssertionError) else f'ERROR - step 297: {e}')

print("STEP 298 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 298')
except Exception as e:
    print('FAIL - step 298' if isinstance(e, AssertionError) else f'ERROR - step 298: {e}')

print("STEP 299 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 299')
except Exception as e:
    print('FAIL - step 299' if isinstance(e, AssertionError) else f'ERROR - step 299: {e}')

print("STEP 300 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 300')
except Exception as e:
    print('FAIL - step 300' if isinstance(e, AssertionError) else f'ERROR - step 300: {e}')

print("STEP 301 - Check element label#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "label")))
    print('PASS - step 301')
except Exception as e:
    print('FAIL - step 301' if isinstance(e, AssertionError) else f'ERROR - step 301: {e}')

print("STEP 302 - Check element div#None.['Line-208']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Line-208']")))
    print('PASS - step 302')
except Exception as e:
    print('FAIL - step 302' if isinstance(e, AssertionError) else f'ERROR - step 302: {e}')

print("STEP 303 - Check element div#None.['wpr-submenu-item-mobile']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-submenu-item-mobile']")))
    print('PASS - step 303')
except Exception as e:
    print('FAIL - step 303' if isinstance(e, AssertionError) else f'ERROR - step 303: {e}')

print("STEP 304 - Check element div#None.['wpr-submenu-heading']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-submenu-heading']")))
    print('PASS - step 304')
except Exception as e:
    print('FAIL - step 304' if isinstance(e, AssertionError) else f'ERROR - step 304: {e}')

print("STEP 305 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 305')
except Exception as e:
    print('FAIL - step 305' if isinstance(e, AssertionError) else f'ERROR - step 305: {e}')

print("STEP 306 - Check element li#None.['headind_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['headind_content']")))
    print('PASS - step 306')
except Exception as e:
    print('FAIL - step 306' if isinstance(e, AssertionError) else f'ERROR - step 306: {e}')

print("STEP 307 - Check element label#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "label")))
    print('PASS - step 307')
except Exception as e:
    print('FAIL - step 307' if isinstance(e, AssertionError) else f'ERROR - step 307: {e}')

print("STEP 308 - Check element div#None.['sub-submenu-data-mobile']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['sub-submenu-data-mobile']")))
    print('PASS - step 308')
except Exception as e:
    print('FAIL - step 308' if isinstance(e, AssertionError) else f'ERROR - step 308: {e}')

print("STEP 309 - Check element ul#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "ul")))
    print('PASS - step 309')
except Exception as e:
    print('FAIL - step 309' if isinstance(e, AssertionError) else f'ERROR - step 309: {e}')

print("STEP 310 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 310')
except Exception as e:
    print('FAIL - step 310' if isinstance(e, AssertionError) else f'ERROR - step 310: {e}')

print("STEP 311 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 311')
except Exception as e:
    print('FAIL - step 311' if isinstance(e, AssertionError) else f'ERROR - step 311: {e}')

print("STEP 312 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 312')
except Exception as e:
    print('FAIL - step 312' if isinstance(e, AssertionError) else f'ERROR - step 312: {e}')

print("STEP 313 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 313')
except Exception as e:
    print('FAIL - step 313' if isinstance(e, AssertionError) else f'ERROR - step 313: {e}')

print("STEP 314 - Check element label#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "label")))
    print('PASS - step 314')
except Exception as e:
    print('FAIL - step 314' if isinstance(e, AssertionError) else f'ERROR - step 314: {e}')

print("STEP 315 - Check element div#None.['Line-208']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Line-208']")))
    print('PASS - step 315')
except Exception as e:
    print('FAIL - step 315' if isinstance(e, AssertionError) else f'ERROR - step 315: {e}')

print("STEP 316 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 316')
except Exception as e:
    print('FAIL - step 316' if isinstance(e, AssertionError) else f'ERROR - step 316: {e}')

print("STEP 317 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 317')
except Exception as e:
    print('FAIL - step 317' if isinstance(e, AssertionError) else f'ERROR - step 317: {e}')

print("STEP 318 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 318')
except Exception as e:
    print('FAIL - step 318' if isinstance(e, AssertionError) else f'ERROR - step 318: {e}')

print("STEP 319 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 319')
except Exception as e:
    print('FAIL - step 319' if isinstance(e, AssertionError) else f'ERROR - step 319: {e}')

print("STEP 320 - Check element label#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "label")))
    print('PASS - step 320')
except Exception as e:
    print('FAIL - step 320' if isinstance(e, AssertionError) else f'ERROR - step 320: {e}')

print("STEP 321 - Check element div#None.['Line-208']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Line-208']")))
    print('PASS - step 321')
except Exception as e:
    print('FAIL - step 321' if isinstance(e, AssertionError) else f'ERROR - step 321: {e}')

print("STEP 322 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 322')
except Exception as e:
    print('FAIL - step 322' if isinstance(e, AssertionError) else f'ERROR - step 322: {e}')

print("STEP 323 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 323')
except Exception as e:
    print('FAIL - step 323' if isinstance(e, AssertionError) else f'ERROR - step 323: {e}')

print("STEP 324 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 324')
except Exception as e:
    print('FAIL - step 324' if isinstance(e, AssertionError) else f'ERROR - step 324: {e}')

print("STEP 325 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 325')
except Exception as e:
    print('FAIL - step 325' if isinstance(e, AssertionError) else f'ERROR - step 325: {e}')

print("STEP 326 - Check element label#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "label")))
    print('PASS - step 326')
except Exception as e:
    print('FAIL - step 326' if isinstance(e, AssertionError) else f'ERROR - step 326: {e}')

print("STEP 327 - Check element div#None.['Line-208']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Line-208']")))
    print('PASS - step 327')
except Exception as e:
    print('FAIL - step 327' if isinstance(e, AssertionError) else f'ERROR - step 327: {e}')

print("STEP 328 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 328')
except Exception as e:
    print('FAIL - step 328' if isinstance(e, AssertionError) else f'ERROR - step 328: {e}')

print("STEP 329 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 329')
except Exception as e:
    print('FAIL - step 329' if isinstance(e, AssertionError) else f'ERROR - step 329: {e}')

print("STEP 330 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 330')
except Exception as e:
    print('FAIL - step 330' if isinstance(e, AssertionError) else f'ERROR - step 330: {e}')

print("STEP 331 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 331')
except Exception as e:
    print('FAIL - step 331' if isinstance(e, AssertionError) else f'ERROR - step 331: {e}')

print("STEP 332 - Check element label#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "label")))
    print('PASS - step 332')
except Exception as e:
    print('FAIL - step 332' if isinstance(e, AssertionError) else f'ERROR - step 332: {e}')

print("STEP 333 - Check element div#None.['Line-208']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Line-208']")))
    print('PASS - step 333')
except Exception as e:
    print('FAIL - step 333' if isinstance(e, AssertionError) else f'ERROR - step 333: {e}')

print("STEP 334 - Check element div#menuitemTwo_sub.['wpr-side-nav-submenu']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "menuitemTwo_sub")))
    print('PASS - step 334')
except Exception as e:
    print('FAIL - step 334' if isinstance(e, AssertionError) else f'ERROR - step 334: {e}')

print("STEP 335 - Check element div#None.['wpr-side-nav-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-side-nav-row']")))
    print('PASS - step 335')
except Exception as e:
    print('FAIL - step 335' if isinstance(e, AssertionError) else f'ERROR - step 335: {e}')

print("STEP 336 - Check element div#None.['header-submenu']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['header-submenu']")))
    print('PASS - step 336')
except Exception as e:
    print('FAIL - step 336' if isinstance(e, AssertionError) else f'ERROR - step 336: {e}')

print("STEP 337 - Check element a#None.['back_icon']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['back_icon']")))
    print('PASS - step 337')
except Exception as e:
    print('FAIL - step 337' if isinstance(e, AssertionError) else f'ERROR - step 337: {e}')

print("STEP 338 - Check element label#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "label")))
    print('PASS - step 338')
except Exception as e:
    print('FAIL - step 338' if isinstance(e, AssertionError) else f'ERROR - step 338: {e}')

print("STEP 339 - Check element div#wpr-close-button.['wpr-close-button-L2']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "wpr-close-button")))
    print('PASS - step 339')
except Exception as e:
    print('FAIL - step 339' if isinstance(e, AssertionError) else f'ERROR - step 339: {e}')

print("STEP 340 - Check element a#None.['close_icon_desk']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['close_icon_desk']")))
    print('PASS - step 340')
except Exception as e:
    print('FAIL - step 340' if isinstance(e, AssertionError) else f'ERROR - step 340: {e}')

print("STEP 341 - Check element div#None.['mobile-submenu-items']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['mobile-submenu-items']")))
    print('PASS - step 341')
except Exception as e:
    print('FAIL - step 341' if isinstance(e, AssertionError) else f'ERROR - step 341: {e}')

print("STEP 342 - Check element ul#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "ul")))
    print('PASS - step 342')
except Exception as e:
    print('FAIL - step 342' if isinstance(e, AssertionError) else f'ERROR - step 342: {e}')

print("STEP 343 - Check element div#None.['wpr-submenu-item-mobile']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-submenu-item-mobile']")))
    print('PASS - step 343')
except Exception as e:
    print('FAIL - step 343' if isinstance(e, AssertionError) else f'ERROR - step 343: {e}')

print("STEP 344 - Check element div#None.['wpr-submenu-heading']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-submenu-heading']")))
    print('PASS - step 344')
except Exception as e:
    print('FAIL - step 344' if isinstance(e, AssertionError) else f'ERROR - step 344: {e}')

print("STEP 345 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 345')
except Exception as e:
    print('FAIL - step 345' if isinstance(e, AssertionError) else f'ERROR - step 345: {e}')

print("STEP 346 - Check element li#None.['headind_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['headind_content']")))
    print('PASS - step 346')
except Exception as e:
    print('FAIL - step 346' if isinstance(e, AssertionError) else f'ERROR - step 346: {e}')

print("STEP 347 - Check element label#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "label")))
    print('PASS - step 347')
except Exception as e:
    print('FAIL - step 347' if isinstance(e, AssertionError) else f'ERROR - step 347: {e}')

print("STEP 348 - Check element div#None.['sub-submenu-data-mobile']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['sub-submenu-data-mobile']")))
    print('PASS - step 348')
except Exception as e:
    print('FAIL - step 348' if isinstance(e, AssertionError) else f'ERROR - step 348: {e}')

print("STEP 349 - Check element ul#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "ul")))
    print('PASS - step 349')
except Exception as e:
    print('FAIL - step 349' if isinstance(e, AssertionError) else f'ERROR - step 349: {e}')

print("STEP 350 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 350')
except Exception as e:
    print('FAIL - step 350' if isinstance(e, AssertionError) else f'ERROR - step 350: {e}')

print("STEP 351 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 351')
except Exception as e:
    print('FAIL - step 351' if isinstance(e, AssertionError) else f'ERROR - step 351: {e}')

print("STEP 352 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 352')
except Exception as e:
    print('FAIL - step 352' if isinstance(e, AssertionError) else f'ERROR - step 352: {e}')

print("STEP 353 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 353')
except Exception as e:
    print('FAIL - step 353' if isinstance(e, AssertionError) else f'ERROR - step 353: {e}')

print("STEP 354 - Check element label#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "label")))
    print('PASS - step 354')
except Exception as e:
    print('FAIL - step 354' if isinstance(e, AssertionError) else f'ERROR - step 354: {e}')

print("STEP 355 - Check element div#None.['Line-208']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Line-208']")))
    print('PASS - step 355')
except Exception as e:
    print('FAIL - step 355' if isinstance(e, AssertionError) else f'ERROR - step 355: {e}')

print("STEP 356 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 356')
except Exception as e:
    print('FAIL - step 356' if isinstance(e, AssertionError) else f'ERROR - step 356: {e}')

print("STEP 357 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 357')
except Exception as e:
    print('FAIL - step 357' if isinstance(e, AssertionError) else f'ERROR - step 357: {e}')

print("STEP 358 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 358')
except Exception as e:
    print('FAIL - step 358' if isinstance(e, AssertionError) else f'ERROR - step 358: {e}')

print("STEP 359 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 359')
except Exception as e:
    print('FAIL - step 359' if isinstance(e, AssertionError) else f'ERROR - step 359: {e}')

print("STEP 360 - Check element label#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "label")))
    print('PASS - step 360')
except Exception as e:
    print('FAIL - step 360' if isinstance(e, AssertionError) else f'ERROR - step 360: {e}')

print("STEP 361 - Check element div#None.['Line-208']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Line-208']")))
    print('PASS - step 361')
except Exception as e:
    print('FAIL - step 361' if isinstance(e, AssertionError) else f'ERROR - step 361: {e}')

print("STEP 362 - Check element div#menuitemThree_sub.['wpr-side-nav-submenu']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "menuitemThree_sub")))
    print('PASS - step 362')
except Exception as e:
    print('FAIL - step 362' if isinstance(e, AssertionError) else f'ERROR - step 362: {e}')

print("STEP 363 - Check element div#None.['wpr-side-nav-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-side-nav-row']")))
    print('PASS - step 363')
except Exception as e:
    print('FAIL - step 363' if isinstance(e, AssertionError) else f'ERROR - step 363: {e}')

print("STEP 364 - Check element div#None.['header-submenu']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['header-submenu']")))
    print('PASS - step 364')
except Exception as e:
    print('FAIL - step 364' if isinstance(e, AssertionError) else f'ERROR - step 364: {e}')

print("STEP 365 - Check element a#None.['back_icon']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['back_icon']")))
    print('PASS - step 365')
except Exception as e:
    print('FAIL - step 365' if isinstance(e, AssertionError) else f'ERROR - step 365: {e}')

print("STEP 366 - Check element label#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "label")))
    print('PASS - step 366')
except Exception as e:
    print('FAIL - step 366' if isinstance(e, AssertionError) else f'ERROR - step 366: {e}')

print("STEP 367 - Check element div#wpr-close-button.['wpr-close-button-L2']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "wpr-close-button")))
    print('PASS - step 367')
except Exception as e:
    print('FAIL - step 367' if isinstance(e, AssertionError) else f'ERROR - step 367: {e}')

print("STEP 368 - Check element a#None.['close_icon_desk']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['close_icon_desk']")))
    print('PASS - step 368')
except Exception as e:
    print('FAIL - step 368' if isinstance(e, AssertionError) else f'ERROR - step 368: {e}')

print("STEP 369 - Check element div#None.['mobile-submenu-items']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['mobile-submenu-items']")))
    print('PASS - step 369')
except Exception as e:
    print('FAIL - step 369' if isinstance(e, AssertionError) else f'ERROR - step 369: {e}')

print("STEP 370 - Check element ul#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "ul")))
    print('PASS - step 370')
except Exception as e:
    print('FAIL - step 370' if isinstance(e, AssertionError) else f'ERROR - step 370: {e}')

print("STEP 371 - Check element div#None.['wpr-submenu-item-mobile']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-submenu-item-mobile']")))
    print('PASS - step 371')
except Exception as e:
    print('FAIL - step 371' if isinstance(e, AssertionError) else f'ERROR - step 371: {e}')

print("STEP 372 - Check element div#None.['wpr-submenu-heading']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-submenu-heading']")))
    print('PASS - step 372')
except Exception as e:
    print('FAIL - step 372' if isinstance(e, AssertionError) else f'ERROR - step 372: {e}')

print("STEP 373 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 373')
except Exception as e:
    print('FAIL - step 373' if isinstance(e, AssertionError) else f'ERROR - step 373: {e}')

print("STEP 374 - Check element li#None.['headind_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['headind_content']")))
    print('PASS - step 374')
except Exception as e:
    print('FAIL - step 374' if isinstance(e, AssertionError) else f'ERROR - step 374: {e}')

print("STEP 375 - Check element label#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "label")))
    print('PASS - step 375')
except Exception as e:
    print('FAIL - step 375' if isinstance(e, AssertionError) else f'ERROR - step 375: {e}')

print("STEP 376 - Check element div#None.['sub-submenu-data-mobile']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['sub-submenu-data-mobile']")))
    print('PASS - step 376')
except Exception as e:
    print('FAIL - step 376' if isinstance(e, AssertionError) else f'ERROR - step 376: {e}')

print("STEP 377 - Check element ul#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "ul")))
    print('PASS - step 377')
except Exception as e:
    print('FAIL - step 377' if isinstance(e, AssertionError) else f'ERROR - step 377: {e}')

print("STEP 378 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 378')
except Exception as e:
    print('FAIL - step 378' if isinstance(e, AssertionError) else f'ERROR - step 378: {e}')

print("STEP 379 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 379')
except Exception as e:
    print('FAIL - step 379' if isinstance(e, AssertionError) else f'ERROR - step 379: {e}')

print("STEP 380 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 380')
except Exception as e:
    print('FAIL - step 380' if isinstance(e, AssertionError) else f'ERROR - step 380: {e}')

print("STEP 381 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 381')
except Exception as e:
    print('FAIL - step 381' if isinstance(e, AssertionError) else f'ERROR - step 381: {e}')

print("STEP 382 - Check element label#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "label")))
    print('PASS - step 382')
except Exception as e:
    print('FAIL - step 382' if isinstance(e, AssertionError) else f'ERROR - step 382: {e}')

print("STEP 383 - Check element div#None.['Line-208']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Line-208']")))
    print('PASS - step 383')
except Exception as e:
    print('FAIL - step 383' if isinstance(e, AssertionError) else f'ERROR - step 383: {e}')

print("STEP 384 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 384')
except Exception as e:
    print('FAIL - step 384' if isinstance(e, AssertionError) else f'ERROR - step 384: {e}')

print("STEP 385 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 385')
except Exception as e:
    print('FAIL - step 385' if isinstance(e, AssertionError) else f'ERROR - step 385: {e}')

print("STEP 386 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 386')
except Exception as e:
    print('FAIL - step 386' if isinstance(e, AssertionError) else f'ERROR - step 386: {e}')

print("STEP 387 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 387')
except Exception as e:
    print('FAIL - step 387' if isinstance(e, AssertionError) else f'ERROR - step 387: {e}')

print("STEP 388 - Check element label#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "label")))
    print('PASS - step 388')
except Exception as e:
    print('FAIL - step 388' if isinstance(e, AssertionError) else f'ERROR - step 388: {e}')

print("STEP 389 - Check element div#None.['Line-208']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Line-208']")))
    print('PASS - step 389')
except Exception as e:
    print('FAIL - step 389' if isinstance(e, AssertionError) else f'ERROR - step 389: {e}')

print("STEP 390 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 390')
except Exception as e:
    print('FAIL - step 390' if isinstance(e, AssertionError) else f'ERROR - step 390: {e}')

print("STEP 391 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 391')
except Exception as e:
    print('FAIL - step 391' if isinstance(e, AssertionError) else f'ERROR - step 391: {e}')

print("STEP 392 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 392')
except Exception as e:
    print('FAIL - step 392' if isinstance(e, AssertionError) else f'ERROR - step 392: {e}')

print("STEP 393 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 393')
except Exception as e:
    print('FAIL - step 393' if isinstance(e, AssertionError) else f'ERROR - step 393: {e}')

print("STEP 394 - Check element label#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "label")))
    print('PASS - step 394')
except Exception as e:
    print('FAIL - step 394' if isinstance(e, AssertionError) else f'ERROR - step 394: {e}')

print("STEP 395 - Check element div#None.['Line-208']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Line-208']")))
    print('PASS - step 395')
except Exception as e:
    print('FAIL - step 395' if isinstance(e, AssertionError) else f'ERROR - step 395: {e}')

print("STEP 396 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 396')
except Exception as e:
    print('FAIL - step 396' if isinstance(e, AssertionError) else f'ERROR - step 396: {e}')

print("STEP 397 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 397')
except Exception as e:
    print('FAIL - step 397' if isinstance(e, AssertionError) else f'ERROR - step 397: {e}')

print("STEP 398 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 398')
except Exception as e:
    print('FAIL - step 398' if isinstance(e, AssertionError) else f'ERROR - step 398: {e}')

print("STEP 399 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 399')
except Exception as e:
    print('FAIL - step 399' if isinstance(e, AssertionError) else f'ERROR - step 399: {e}')

print("STEP 400 - Check element label#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "label")))
    print('PASS - step 400')
except Exception as e:
    print('FAIL - step 400' if isinstance(e, AssertionError) else f'ERROR - step 400: {e}')

print("STEP 401 - Check element div#None.['Line-208']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Line-208']")))
    print('PASS - step 401')
except Exception as e:
    print('FAIL - step 401' if isinstance(e, AssertionError) else f'ERROR - step 401: {e}')

print("STEP 402 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 402')
except Exception as e:
    print('FAIL - step 402' if isinstance(e, AssertionError) else f'ERROR - step 402: {e}')

print("STEP 403 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 403')
except Exception as e:
    print('FAIL - step 403' if isinstance(e, AssertionError) else f'ERROR - step 403: {e}')

print("STEP 404 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 404')
except Exception as e:
    print('FAIL - step 404' if isinstance(e, AssertionError) else f'ERROR - step 404: {e}')

print("STEP 405 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 405')
except Exception as e:
    print('FAIL - step 405' if isinstance(e, AssertionError) else f'ERROR - step 405: {e}')

print("STEP 406 - Check element label#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "label")))
    print('PASS - step 406')
except Exception as e:
    print('FAIL - step 406' if isinstance(e, AssertionError) else f'ERROR - step 406: {e}')

print("STEP 407 - Check element div#None.['Line-208']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Line-208']")))
    print('PASS - step 407')
except Exception as e:
    print('FAIL - step 407' if isinstance(e, AssertionError) else f'ERROR - step 407: {e}')

print("STEP 408 - Check element div#None.['wpr-submenu-item-mobile']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-submenu-item-mobile']")))
    print('PASS - step 408')
except Exception as e:
    print('FAIL - step 408' if isinstance(e, AssertionError) else f'ERROR - step 408: {e}')

print("STEP 409 - Check element div#None.['wpr-submenu-heading']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-submenu-heading']")))
    print('PASS - step 409')
except Exception as e:
    print('FAIL - step 409' if isinstance(e, AssertionError) else f'ERROR - step 409: {e}')

print("STEP 410 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 410')
except Exception as e:
    print('FAIL - step 410' if isinstance(e, AssertionError) else f'ERROR - step 410: {e}')

print("STEP 411 - Check element li#None.['headind_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['headind_content']")))
    print('PASS - step 411')
except Exception as e:
    print('FAIL - step 411' if isinstance(e, AssertionError) else f'ERROR - step 411: {e}')

print("STEP 412 - Check element label#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "label")))
    print('PASS - step 412')
except Exception as e:
    print('FAIL - step 412' if isinstance(e, AssertionError) else f'ERROR - step 412: {e}')

print("STEP 413 - Check element div#None.['sub-submenu-data-mobile']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['sub-submenu-data-mobile']")))
    print('PASS - step 413')
except Exception as e:
    print('FAIL - step 413' if isinstance(e, AssertionError) else f'ERROR - step 413: {e}')

print("STEP 414 - Check element ul#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "ul")))
    print('PASS - step 414')
except Exception as e:
    print('FAIL - step 414' if isinstance(e, AssertionError) else f'ERROR - step 414: {e}')

print("STEP 415 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 415')
except Exception as e:
    print('FAIL - step 415' if isinstance(e, AssertionError) else f'ERROR - step 415: {e}')

print("STEP 416 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 416')
except Exception as e:
    print('FAIL - step 416' if isinstance(e, AssertionError) else f'ERROR - step 416: {e}')

print("STEP 417 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 417')
except Exception as e:
    print('FAIL - step 417' if isinstance(e, AssertionError) else f'ERROR - step 417: {e}')

print("STEP 418 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 418')
except Exception as e:
    print('FAIL - step 418' if isinstance(e, AssertionError) else f'ERROR - step 418: {e}')

print("STEP 419 - Check element label#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "label")))
    print('PASS - step 419')
except Exception as e:
    print('FAIL - step 419' if isinstance(e, AssertionError) else f'ERROR - step 419: {e}')

print("STEP 420 - Check element div#None.['Line-208']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Line-208']")))
    print('PASS - step 420')
except Exception as e:
    print('FAIL - step 420' if isinstance(e, AssertionError) else f'ERROR - step 420: {e}')

print("STEP 421 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 421')
except Exception as e:
    print('FAIL - step 421' if isinstance(e, AssertionError) else f'ERROR - step 421: {e}')

print("STEP 422 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 422')
except Exception as e:
    print('FAIL - step 422' if isinstance(e, AssertionError) else f'ERROR - step 422: {e}')

print("STEP 423 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 423')
except Exception as e:
    print('FAIL - step 423' if isinstance(e, AssertionError) else f'ERROR - step 423: {e}')

print("STEP 424 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 424')
except Exception as e:
    print('FAIL - step 424' if isinstance(e, AssertionError) else f'ERROR - step 424: {e}')

print("STEP 425 - Check element label#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "label")))
    print('PASS - step 425')
except Exception as e:
    print('FAIL - step 425' if isinstance(e, AssertionError) else f'ERROR - step 425: {e}')

print("STEP 426 - Check element div#None.['Line-208']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Line-208']")))
    print('PASS - step 426')
except Exception as e:
    print('FAIL - step 426' if isinstance(e, AssertionError) else f'ERROR - step 426: {e}')

print("STEP 427 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 427')
except Exception as e:
    print('FAIL - step 427' if isinstance(e, AssertionError) else f'ERROR - step 427: {e}')

print("STEP 428 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 428')
except Exception as e:
    print('FAIL - step 428' if isinstance(e, AssertionError) else f'ERROR - step 428: {e}')

print("STEP 429 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 429')
except Exception as e:
    print('FAIL - step 429' if isinstance(e, AssertionError) else f'ERROR - step 429: {e}')

print("STEP 430 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 430')
except Exception as e:
    print('FAIL - step 430' if isinstance(e, AssertionError) else f'ERROR - step 430: {e}')

print("STEP 431 - Check element label#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "label")))
    print('PASS - step 431')
except Exception as e:
    print('FAIL - step 431' if isinstance(e, AssertionError) else f'ERROR - step 431: {e}')

print("STEP 432 - Check element div#None.['Line-208']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Line-208']")))
    print('PASS - step 432')
except Exception as e:
    print('FAIL - step 432' if isinstance(e, AssertionError) else f'ERROR - step 432: {e}')

print("STEP 433 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 433')
except Exception as e:
    print('FAIL - step 433' if isinstance(e, AssertionError) else f'ERROR - step 433: {e}')

print("STEP 434 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 434')
except Exception as e:
    print('FAIL - step 434' if isinstance(e, AssertionError) else f'ERROR - step 434: {e}')

print("STEP 435 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 435')
except Exception as e:
    print('FAIL - step 435' if isinstance(e, AssertionError) else f'ERROR - step 435: {e}')

print("STEP 436 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 436')
except Exception as e:
    print('FAIL - step 436' if isinstance(e, AssertionError) else f'ERROR - step 436: {e}')

print("STEP 437 - Check element label#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "label")))
    print('PASS - step 437')
except Exception as e:
    print('FAIL - step 437' if isinstance(e, AssertionError) else f'ERROR - step 437: {e}')

print("STEP 438 - Check element div#None.['Line-208']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Line-208']")))
    print('PASS - step 438')
except Exception as e:
    print('FAIL - step 438' if isinstance(e, AssertionError) else f'ERROR - step 438: {e}')

print("STEP 439 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 439')
except Exception as e:
    print('FAIL - step 439' if isinstance(e, AssertionError) else f'ERROR - step 439: {e}')

print("STEP 440 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 440')
except Exception as e:
    print('FAIL - step 440' if isinstance(e, AssertionError) else f'ERROR - step 440: {e}')

print("STEP 441 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 441')
except Exception as e:
    print('FAIL - step 441' if isinstance(e, AssertionError) else f'ERROR - step 441: {e}')

print("STEP 442 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 442')
except Exception as e:
    print('FAIL - step 442' if isinstance(e, AssertionError) else f'ERROR - step 442: {e}')

print("STEP 443 - Check element label#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "label")))
    print('PASS - step 443')
except Exception as e:
    print('FAIL - step 443' if isinstance(e, AssertionError) else f'ERROR - step 443: {e}')

print("STEP 444 - Check element div#None.['Line-208']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Line-208']")))
    print('PASS - step 444')
except Exception as e:
    print('FAIL - step 444' if isinstance(e, AssertionError) else f'ERROR - step 444: {e}')

print("STEP 445 - Check element div#None.['wpr-submenu-item-mobile']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-submenu-item-mobile']")))
    print('PASS - step 445')
except Exception as e:
    print('FAIL - step 445' if isinstance(e, AssertionError) else f'ERROR - step 445: {e}')

print("STEP 446 - Check element div#None.['wpr-submenu-heading']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-submenu-heading']")))
    print('PASS - step 446')
except Exception as e:
    print('FAIL - step 446' if isinstance(e, AssertionError) else f'ERROR - step 446: {e}')

print("STEP 447 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 447')
except Exception as e:
    print('FAIL - step 447' if isinstance(e, AssertionError) else f'ERROR - step 447: {e}')

print("STEP 448 - Check element li#None.['headind_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['headind_content']")))
    print('PASS - step 448')
except Exception as e:
    print('FAIL - step 448' if isinstance(e, AssertionError) else f'ERROR - step 448: {e}')

print("STEP 449 - Check element label#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "label")))
    print('PASS - step 449')
except Exception as e:
    print('FAIL - step 449' if isinstance(e, AssertionError) else f'ERROR - step 449: {e}')

print("STEP 450 - Check element div#None.['sub-submenu-data-mobile']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['sub-submenu-data-mobile']")))
    print('PASS - step 450')
except Exception as e:
    print('FAIL - step 450' if isinstance(e, AssertionError) else f'ERROR - step 450: {e}')

print("STEP 451 - Check element ul#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "ul")))
    print('PASS - step 451')
except Exception as e:
    print('FAIL - step 451' if isinstance(e, AssertionError) else f'ERROR - step 451: {e}')

print("STEP 452 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 452')
except Exception as e:
    print('FAIL - step 452' if isinstance(e, AssertionError) else f'ERROR - step 452: {e}')

print("STEP 453 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 453')
except Exception as e:
    print('FAIL - step 453' if isinstance(e, AssertionError) else f'ERROR - step 453: {e}')

print("STEP 454 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 454')
except Exception as e:
    print('FAIL - step 454' if isinstance(e, AssertionError) else f'ERROR - step 454: {e}')

print("STEP 455 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 455')
except Exception as e:
    print('FAIL - step 455' if isinstance(e, AssertionError) else f'ERROR - step 455: {e}')

print("STEP 456 - Check element label#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "label")))
    print('PASS - step 456')
except Exception as e:
    print('FAIL - step 456' if isinstance(e, AssertionError) else f'ERROR - step 456: {e}')

print("STEP 457 - Check element div#None.['Line-208']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Line-208']")))
    print('PASS - step 457')
except Exception as e:
    print('FAIL - step 457' if isinstance(e, AssertionError) else f'ERROR - step 457: {e}')

print("STEP 458 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 458')
except Exception as e:
    print('FAIL - step 458' if isinstance(e, AssertionError) else f'ERROR - step 458: {e}')

print("STEP 459 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 459')
except Exception as e:
    print('FAIL - step 459' if isinstance(e, AssertionError) else f'ERROR - step 459: {e}')

print("STEP 460 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 460')
except Exception as e:
    print('FAIL - step 460' if isinstance(e, AssertionError) else f'ERROR - step 460: {e}')

print("STEP 461 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 461')
except Exception as e:
    print('FAIL - step 461' if isinstance(e, AssertionError) else f'ERROR - step 461: {e}')

print("STEP 462 - Check element label#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "label")))
    print('PASS - step 462')
except Exception as e:
    print('FAIL - step 462' if isinstance(e, AssertionError) else f'ERROR - step 462: {e}')

print("STEP 463 - Check element div#None.['Line-208']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Line-208']")))
    print('PASS - step 463')
except Exception as e:
    print('FAIL - step 463' if isinstance(e, AssertionError) else f'ERROR - step 463: {e}')

print("STEP 464 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 464')
except Exception as e:
    print('FAIL - step 464' if isinstance(e, AssertionError) else f'ERROR - step 464: {e}')

print("STEP 465 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 465')
except Exception as e:
    print('FAIL - step 465' if isinstance(e, AssertionError) else f'ERROR - step 465: {e}')

print("STEP 466 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 466')
except Exception as e:
    print('FAIL - step 466' if isinstance(e, AssertionError) else f'ERROR - step 466: {e}')

print("STEP 467 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 467')
except Exception as e:
    print('FAIL - step 467' if isinstance(e, AssertionError) else f'ERROR - step 467: {e}')

print("STEP 468 - Check element label#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "label")))
    print('PASS - step 468')
except Exception as e:
    print('FAIL - step 468' if isinstance(e, AssertionError) else f'ERROR - step 468: {e}')

print("STEP 469 - Check element div#None.['Line-208']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Line-208']")))
    print('PASS - step 469')
except Exception as e:
    print('FAIL - step 469' if isinstance(e, AssertionError) else f'ERROR - step 469: {e}')

print("STEP 470 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 470')
except Exception as e:
    print('FAIL - step 470' if isinstance(e, AssertionError) else f'ERROR - step 470: {e}')

print("STEP 471 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 471')
except Exception as e:
    print('FAIL - step 471' if isinstance(e, AssertionError) else f'ERROR - step 471: {e}')

print("STEP 472 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 472')
except Exception as e:
    print('FAIL - step 472' if isinstance(e, AssertionError) else f'ERROR - step 472: {e}')

print("STEP 473 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 473')
except Exception as e:
    print('FAIL - step 473' if isinstance(e, AssertionError) else f'ERROR - step 473: {e}')

print("STEP 474 - Check element label#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "label")))
    print('PASS - step 474')
except Exception as e:
    print('FAIL - step 474' if isinstance(e, AssertionError) else f'ERROR - step 474: {e}')

print("STEP 475 - Check element div#None.['Line-208']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Line-208']")))
    print('PASS - step 475')
except Exception as e:
    print('FAIL - step 475' if isinstance(e, AssertionError) else f'ERROR - step 475: {e}')

print("STEP 476 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 476')
except Exception as e:
    print('FAIL - step 476' if isinstance(e, AssertionError) else f'ERROR - step 476: {e}')

print("STEP 477 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 477')
except Exception as e:
    print('FAIL - step 477' if isinstance(e, AssertionError) else f'ERROR - step 477: {e}')

print("STEP 478 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 478')
except Exception as e:
    print('FAIL - step 478' if isinstance(e, AssertionError) else f'ERROR - step 478: {e}')

print("STEP 479 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 479')
except Exception as e:
    print('FAIL - step 479' if isinstance(e, AssertionError) else f'ERROR - step 479: {e}')

print("STEP 480 - Check element label#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "label")))
    print('PASS - step 480')
except Exception as e:
    print('FAIL - step 480' if isinstance(e, AssertionError) else f'ERROR - step 480: {e}')

print("STEP 481 - Check element div#None.['Line-208']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Line-208']")))
    print('PASS - step 481')
except Exception as e:
    print('FAIL - step 481' if isinstance(e, AssertionError) else f'ERROR - step 481: {e}')

print("STEP 482 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 482')
except Exception as e:
    print('FAIL - step 482' if isinstance(e, AssertionError) else f'ERROR - step 482: {e}')

print("STEP 483 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 483')
except Exception as e:
    print('FAIL - step 483' if isinstance(e, AssertionError) else f'ERROR - step 483: {e}')

print("STEP 484 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 484')
except Exception as e:
    print('FAIL - step 484' if isinstance(e, AssertionError) else f'ERROR - step 484: {e}')

print("STEP 485 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 485')
except Exception as e:
    print('FAIL - step 485' if isinstance(e, AssertionError) else f'ERROR - step 485: {e}')

print("STEP 486 - Check element label#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "label")))
    print('PASS - step 486')
except Exception as e:
    print('FAIL - step 486' if isinstance(e, AssertionError) else f'ERROR - step 486: {e}')

print("STEP 487 - Check element div#None.['Line-208']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Line-208']")))
    print('PASS - step 487')
except Exception as e:
    print('FAIL - step 487' if isinstance(e, AssertionError) else f'ERROR - step 487: {e}')

print("STEP 488 - Check element div#countryCode.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "countryCode")))
    print('PASS - step 488')
except Exception as e:
    print('FAIL - step 488' if isinstance(e, AssertionError) else f'ERROR - step 488: {e}')

print("STEP 489 - Check element div#languageCode.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "languageCode")))
    print('PASS - step 489')
except Exception as e:
    print('FAIL - step 489' if isinstance(e, AssertionError) else f'ERROR - step 489: {e}')

print("STEP 490 - Check element div#languageRTL.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "languageRTL")))
    print('PASS - step 490')
except Exception as e:
    print('FAIL - step 490' if isinstance(e, AssertionError) else f'ERROR - step 490: {e}')

print("STEP 491 - Check element div#privacyURL.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "privacyURL")))
    print('PASS - step 491')
except Exception as e:
    print('FAIL - step 491' if isinstance(e, AssertionError) else f'ERROR - step 491: {e}')

print("STEP 492 - Check element div#hpCaasServer.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "hpCaasServer")))
    print('PASS - step 492')
except Exception as e:
    print('FAIL - step 492' if isinstance(e, AssertionError) else f'ERROR - step 492: {e}')

print("STEP 493 - Check element div#hsEndpointTracking.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "hsEndpointTracking")))
    print('PASS - step 493')
except Exception as e:
    print('FAIL - step 493' if isinstance(e, AssertionError) else f'ERROR - step 493: {e}')

print("STEP 494 - Check element div#None.['wpr-search-container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-search-container']")))
    print('PASS - step 494')
except Exception as e:
    print('FAIL - step 494' if isinstance(e, AssertionError) else f'ERROR - step 494: {e}')

print("STEP 495 - Check element div#None.['wpr-search-bar']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-search-bar']")))
    print('PASS - step 495')
except Exception as e:
    print('FAIL - step 495' if isinstance(e, AssertionError) else f'ERROR - step 495: {e}')

print("STEP 496 - Check element div#None.['Rectangle-426']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-426']")))
    print('PASS - step 496')
except Exception as e:
    print('FAIL - step 496' if isinstance(e, AssertionError) else f'ERROR - step 496: {e}')

print("STEP 497 - Check element input#search_focus_mobile.['search-bar', 'link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "search_focus_mobile")))
    print('PASS - step 497')
except Exception as e:
    print('FAIL - step 497' if isinstance(e, AssertionError) else f'ERROR - step 497: {e}')

print("STEP 498 - Check element span#None.['clear-search']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['clear-search']")))
    print('PASS - step 498')
except Exception as e:
    print('FAIL - step 498' if isinstance(e, AssertionError) else f'ERROR - step 498: {e}')

print("STEP 499 - Check element a#None.['wpr-clear-icon-logo']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-clear-icon-logo']")))
    print('PASS - step 499')
except Exception as e:
    print('FAIL - step 499' if isinstance(e, AssertionError) else f'ERROR - step 499: {e}')

print("STEP 500 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 500')
except Exception as e:
    print('FAIL - step 500' if isinstance(e, AssertionError) else f'ERROR - step 500: {e}')

print("STEP 501 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 501')
except Exception as e:
    print('FAIL - step 501' if isinstance(e, AssertionError) else f'ERROR - step 501: {e}')

print("STEP 502 - Check element span#None.['screenReadingText']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['screenReadingText']")))
    print('PASS - step 502')
except Exception as e:
    print('FAIL - step 502' if isinstance(e, AssertionError) else f'ERROR - step 502: {e}')

print("STEP 503 - Check element a#None.['wpr-search-icon-logo', 'search_trigger', 'link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-search-icon-logo', 'search_trigger', 'link_metrics']")))
    print('PASS - step 503')
except Exception as e:
    print('FAIL - step 503' if isinstance(e, AssertionError) else f'ERROR - step 503: {e}')

print("STEP 504 - Check element a#None.['cancel']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['cancel']")))
    print('PASS - step 504')
except Exception as e:
    print('FAIL - step 504' if isinstance(e, AssertionError) else f'ERROR - step 504: {e}')

print("STEP 505 - Check element div#None.['wps-tablet']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wps-tablet']")))
    print('PASS - step 505')
except Exception as e:
    print('FAIL - step 505' if isinstance(e, AssertionError) else f'ERROR - step 505: {e}')

print("STEP 506 - Check element nav#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "nav")))
    print('PASS - step 506')
except Exception as e:
    print('FAIL - step 506' if isinstance(e, AssertionError) else f'ERROR - step 506: {e}')

print("STEP 507 - Check element div#None.['wpr-header-tab']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-header-tab']")))
    print('PASS - step 507')
except Exception as e:
    print('FAIL - step 507' if isinstance(e, AssertionError) else f'ERROR - step 507: {e}')

print("STEP 508 - Check element div#None.['wpr-row', 'header_container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row', 'header_container']")))
    print('PASS - step 508')
except Exception as e:
    print('FAIL - step 508' if isinstance(e, AssertionError) else f'ERROR - step 508: {e}')

print("STEP 509 - Check element div#None.['wpr-logo-header-holder']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-logo-header-holder']")))
    print('PASS - step 509')
except Exception as e:
    print('FAIL - step 509' if isinstance(e, AssertionError) else f'ERROR - step 509: {e}')

print("STEP 510 - Check element div#None.['wpr-logo-headers', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-logo-headers', 'unselectable']")))
    print('PASS - step 510')
except Exception as e:
    print('FAIL - step 510' if isinstance(e, AssertionError) else f'ERROR - step 510: {e}')

print("STEP 511 - Check element span#None.['wpr-skip-links']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-skip-links']")))
    print('PASS - step 511')
except Exception as e:
    print('FAIL - step 511' if isinstance(e, AssertionError) else f'ERROR - step 511: {e}')

print("STEP 512 - Check element a#None.['js-skip-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['js-skip-link']")))
    print('PASS - step 512')
except Exception as e:
    print('FAIL - step 512' if isinstance(e, AssertionError) else f'ERROR - step 512: {e}')

print("STEP 513 - Check element a#None.['js-skip-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['js-skip-link']")))
    print('PASS - step 513')
except Exception as e:
    print('FAIL - step 513' if isinstance(e, AssertionError) else f'ERROR - step 513: {e}')

print("STEP 514 - Check element a#None.['wpr-main-logo-svg', 'unselectable', 'link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-main-logo-svg', 'unselectable', 'link_metrics']")))
    print('PASS - step 514')
except Exception as e:
    print('FAIL - step 514' if isinstance(e, AssertionError) else f'ERROR - step 514: {e}')

print("STEP 515 - Check element div#None.['wpr-link-container', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-link-container', 'unselectable']")))
    print('PASS - step 515')
except Exception as e:
    print('FAIL - step 515' if isinstance(e, AssertionError) else f'ERROR - step 515: {e}')

print("STEP 516 - Check element div#menuitemOne_tab.['navbar-header-links', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "menuitemOne_tab")))
    print('PASS - step 516')
except Exception as e:
    print('FAIL - step 516' if isinstance(e, AssertionError) else f'ERROR - step 516: {e}')

print("STEP 517 - Check element span#None.['font-style-h5']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['font-style-h5']")))
    print('PASS - step 517')
except Exception as e:
    print('FAIL - step 517' if isinstance(e, AssertionError) else f'ERROR - step 517: {e}')

print("STEP 518 - Check element span#None.['screenReadingText']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['screenReadingText']")))
    print('PASS - step 518')
except Exception as e:
    print('FAIL - step 518' if isinstance(e, AssertionError) else f'ERROR - step 518: {e}')

print("STEP 519 - Check element div#menuitemTwo_tab.['navbar-header-links', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "menuitemTwo_tab")))
    print('PASS - step 519')
except Exception as e:
    print('FAIL - step 519' if isinstance(e, AssertionError) else f'ERROR - step 519: {e}')

print("STEP 520 - Check element span#None.['font-style-h5']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['font-style-h5']")))
    print('PASS - step 520')
except Exception as e:
    print('FAIL - step 520' if isinstance(e, AssertionError) else f'ERROR - step 520: {e}')

print("STEP 521 - Check element span#None.['screenReadingText']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['screenReadingText']")))
    print('PASS - step 521')
except Exception as e:
    print('FAIL - step 521' if isinstance(e, AssertionError) else f'ERROR - step 521: {e}')

print("STEP 522 - Check element div#menuitemThree_tab.['navbar-header-links', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "menuitemThree_tab")))
    print('PASS - step 522')
except Exception as e:
    print('FAIL - step 522' if isinstance(e, AssertionError) else f'ERROR - step 522: {e}')

print("STEP 523 - Check element span#None.['font-style-h5']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['font-style-h5']")))
    print('PASS - step 523')
except Exception as e:
    print('FAIL - step 523' if isinstance(e, AssertionError) else f'ERROR - step 523: {e}')

print("STEP 524 - Check element span#None.['screenReadingText']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['screenReadingText']")))
    print('PASS - step 524')
except Exception as e:
    print('FAIL - step 524' if isinstance(e, AssertionError) else f'ERROR - step 524: {e}')

print("STEP 525 - Check element div#None.['wpr-icons-holder']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-icons-holder']")))
    print('PASS - step 525')
except Exception as e:
    print('FAIL - step 525' if isinstance(e, AssertionError) else f'ERROR - step 525: {e}')

print("STEP 526 - Check element div#None.['Rectangle-426']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-426']")))
    print('PASS - step 526')
except Exception as e:
    print('FAIL - step 526' if isinstance(e, AssertionError) else f'ERROR - step 526: {e}')

print("STEP 527 - Check element input#search_focus_desktop.['search_trigger_onenter', 'search-bar', 'tab-search', 'link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "search_focus_desktop")))
    print('PASS - step 527')
except Exception as e:
    print('FAIL - step 527' if isinstance(e, AssertionError) else f'ERROR - step 527: {e}')

print("STEP 528 - Check element span#None.['clear-search']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['clear-search']")))
    print('PASS - step 528')
except Exception as e:
    print('FAIL - step 528' if isinstance(e, AssertionError) else f'ERROR - step 528: {e}')

print("STEP 529 - Check element a#None.['wpr-backspace-icon']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-backspace-icon']")))
    print('PASS - step 529')
except Exception as e:
    print('FAIL - step 529' if isinstance(e, AssertionError) else f'ERROR - step 529: {e}')

print("STEP 530 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 530')
except Exception as e:
    print('FAIL - step 530' if isinstance(e, AssertionError) else f'ERROR - step 530: {e}')

print("STEP 531 - Check element g#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "g")))
    print('PASS - step 531')
except Exception as e:
    print('FAIL - step 531' if isinstance(e, AssertionError) else f'ERROR - step 531: {e}')

print("STEP 532 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 532')
except Exception as e:
    print('FAIL - step 532' if isinstance(e, AssertionError) else f'ERROR - step 532: {e}')

print("STEP 533 - Check element g#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "g")))
    print('PASS - step 533')
except Exception as e:
    print('FAIL - step 533' if isinstance(e, AssertionError) else f'ERROR - step 533: {e}')

print("STEP 534 - Check element rect#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "rect")))
    print('PASS - step 534')
except Exception as e:
    print('FAIL - step 534' if isinstance(e, AssertionError) else f'ERROR - step 534: {e}')

print("STEP 535 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 535')
except Exception as e:
    print('FAIL - step 535' if isinstance(e, AssertionError) else f'ERROR - step 535: {e}')

print("STEP 536 - Check element span#None.['screenReadingText']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['screenReadingText']")))
    print('PASS - step 536')
except Exception as e:
    print('FAIL - step 536' if isinstance(e, AssertionError) else f'ERROR - step 536: {e}')

print("STEP 537 - Check element a#None.['wpr-search-icon-logo', 'search_trigger', 'link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-search-icon-logo', 'search_trigger', 'link_metrics']")))
    print('PASS - step 537')
except Exception as e:
    print('FAIL - step 537' if isinstance(e, AssertionError) else f'ERROR - step 537: {e}')

print("STEP 538 - Check element a#None.['wpr-close-autocomplete']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-close-autocomplete']")))
    print('PASS - step 538')
except Exception as e:
    print('FAIL - step 538' if isinstance(e, AssertionError) else f'ERROR - step 538: {e}')

print("STEP 539 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 539')
except Exception as e:
    print('FAIL - step 539' if isinstance(e, AssertionError) else f'ERROR - step 539: {e}')

print("STEP 540 - Check element g#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "g")))
    print('PASS - step 540')
except Exception as e:
    print('FAIL - step 540' if isinstance(e, AssertionError) else f'ERROR - step 540: {e}')

print("STEP 541 - Check element circle#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "circle")))
    print('PASS - step 541')
except Exception as e:
    print('FAIL - step 541' if isinstance(e, AssertionError) else f'ERROR - step 541: {e}')

print("STEP 542 - Check element circle#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "circle")))
    print('PASS - step 542')
except Exception as e:
    print('FAIL - step 542' if isinstance(e, AssertionError) else f'ERROR - step 542: {e}')

print("STEP 543 - Check element g#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "g")))
    print('PASS - step 543')
except Exception as e:
    print('FAIL - step 543' if isinstance(e, AssertionError) else f'ERROR - step 543: {e}')

print("STEP 544 - Check element rect#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "rect")))
    print('PASS - step 544')
except Exception as e:
    print('FAIL - step 544' if isinstance(e, AssertionError) else f'ERROR - step 544: {e}')

print("STEP 545 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 545')
except Exception as e:
    print('FAIL - step 545' if isinstance(e, AssertionError) else f'ERROR - step 545: {e}')

print("STEP 546 - Check element div#data-sso.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "data-sso")))
    print('PASS - step 546')
except Exception as e:
    print('FAIL - step 546' if isinstance(e, AssertionError) else f'ERROR - step 546: {e}')

print("STEP 547 - Check element div#wpr-signin-tablet.['wpr-signin']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "wpr-signin-tablet")))
    print('PASS - step 547')
except Exception as e:
    print('FAIL - step 547' if isinstance(e, AssertionError) else f'ERROR - step 547: {e}')

print("STEP 548 - Check element div#None.['signin-loader']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['signin-loader']")))
    print('PASS - step 548')
except Exception as e:
    print('FAIL - step 548' if isinstance(e, AssertionError) else f'ERROR - step 548: {e}')

print("STEP 549 - Check element span#signin-profile-image.['signin-profile-image']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "signin-profile-image")))
    print('PASS - step 549')
except Exception as e:
    print('FAIL - step 549' if isinstance(e, AssertionError) else f'ERROR - step 549: {e}')

print("STEP 550 - Check element a#None.['signin-button', 'hidden']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['signin-button', 'hidden']")))
    print('PASS - step 550')
except Exception as e:
    print('FAIL - step 550' if isinstance(e, AssertionError) else f'ERROR - step 550: {e}')

print("STEP 551 - Check element span#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "span")))
    print('PASS - step 551')
except Exception as e:
    print('FAIL - step 551' if isinstance(e, AssertionError) else f'ERROR - step 551: {e}')

print("STEP 552 - Check element p#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "p")))
    print('PASS - step 552')
except Exception as e:
    print('FAIL - step 552' if isinstance(e, AssertionError) else f'ERROR - step 552: {e}')

print("STEP 553 - Check element div#None.['wpr-signin-arrows']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-signin-arrows']")))
    print('PASS - step 553')
except Exception as e:
    print('FAIL - step 553' if isinstance(e, AssertionError) else f'ERROR - step 553: {e}')

print("STEP 554 - Check element div#None.['top_arrow']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['top_arrow']")))
    print('PASS - step 554')
except Exception as e:
    print('FAIL - step 554' if isinstance(e, AssertionError) else f'ERROR - step 554: {e}')

print("STEP 555 - Check element div#None.['bottom_arrow']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['bottom_arrow']")))
    print('PASS - step 555')
except Exception as e:
    print('FAIL - step 555' if isinstance(e, AssertionError) else f'ERROR - step 555: {e}')

print("STEP 556 - Check element div#None.['wpr-signin-menu']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-signin-menu']")))
    print('PASS - step 556')
except Exception as e:
    print('FAIL - step 556' if isinstance(e, AssertionError) else f'ERROR - step 556: {e}')

print("STEP 557 - Check element div#None.['wpr-signin-menu-item', 'signed-menu-item', 'user-info', 'link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-signin-menu-item', 'signed-menu-item', 'user-info', 'link_metrics']")))
    print('PASS - step 557')
except Exception as e:
    print('FAIL - step 557' if isinstance(e, AssertionError) else f'ERROR - step 557: {e}')

print("STEP 558 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 558')
except Exception as e:
    print('FAIL - step 558' if isinstance(e, AssertionError) else f'ERROR - step 558: {e}')

print("STEP 559 - Check element span#signin-profile-image.['signin-profile-image']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "signin-profile-image")))
    print('PASS - step 559')
except Exception as e:
    print('FAIL - step 559' if isinstance(e, AssertionError) else f'ERROR - step 559: {e}')

print("STEP 560 - Check element p#None.['first-letter']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['first-letter']")))
    print('PASS - step 560')
except Exception as e:
    print('FAIL - step 560' if isinstance(e, AssertionError) else f'ERROR - step 560: {e}')

print("STEP 561 - Check element div#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 561')
except Exception as e:
    print('FAIL - step 561' if isinstance(e, AssertionError) else f'ERROR - step 561: {e}')

print("STEP 562 - Check element span#signin-profile-name.['signin-profile-name']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "signin-profile-name")))
    print('PASS - step 562')
except Exception as e:
    print('FAIL - step 562' if isinstance(e, AssertionError) else f'ERROR - step 562: {e}')

print("STEP 563 - Check element span#signin-profile-email.['signin-profile-email']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "signin-profile-email")))
    print('PASS - step 563')
except Exception as e:
    print('FAIL - step 563' if isinstance(e, AssertionError) else f'ERROR - step 563: {e}')

print("STEP 564 - Check element span#signin-profile-settings.['signin-profile-settings']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "signin-profile-settings")))
    print('PASS - step 564')
except Exception as e:
    print('FAIL - step 564' if isinstance(e, AssertionError) else f'ERROR - step 564: {e}')

print("STEP 565 - Check element a#None.['myAccount', 'link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['myAccount', 'link_metrics']")))
    print('PASS - step 565')
except Exception as e:
    print('FAIL - step 565' if isinstance(e, AssertionError) else f'ERROR - step 565: {e}')

print("STEP 566 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 566')
except Exception as e:
    print('FAIL - step 566' if isinstance(e, AssertionError) else f'ERROR - step 566: {e}')

print("STEP 567 - Check element div#None.['wpr-signin-menu-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-signin-menu-item']")))
    print('PASS - step 567')
except Exception as e:
    print('FAIL - step 567' if isinstance(e, AssertionError) else f'ERROR - step 567: {e}')

print("STEP 568 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 568')
except Exception as e:
    print('FAIL - step 568' if isinstance(e, AssertionError) else f'ERROR - step 568: {e}')

print("STEP 569 - Check element div#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 569')
except Exception as e:
    print('FAIL - step 569' if isinstance(e, AssertionError) else f'ERROR - step 569: {e}')

print("STEP 570 - Check element span#None.['screenReadingText']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['screenReadingText']")))
    print('PASS - step 570')
except Exception as e:
    print('FAIL - step 570' if isinstance(e, AssertionError) else f'ERROR - step 570: {e}')

print("STEP 571 - Check element a#signoutButton.['signoutButton', 'link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "signoutButton")))
    print('PASS - step 571')
except Exception as e:
    print('FAIL - step 571' if isinstance(e, AssertionError) else f'ERROR - step 571: {e}')

print("STEP 572 - Check element div#None.['wpr-signin-menu-item', 'signed-menu-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-signin-menu-item', 'signed-menu-item']")))
    print('PASS - step 572')
except Exception as e:
    print('FAIL - step 572' if isinstance(e, AssertionError) else f'ERROR - step 572: {e}')

print("STEP 573 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 573')
except Exception as e:
    print('FAIL - step 573' if isinstance(e, AssertionError) else f'ERROR - step 573: {e}')

print("STEP 574 - Check element div#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 574')
except Exception as e:
    print('FAIL - step 574' if isinstance(e, AssertionError) else f'ERROR - step 574: {e}')

print("STEP 575 - Check element span#None.['screenReadingText']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['screenReadingText']")))
    print('PASS - step 575')
except Exception as e:
    print('FAIL - step 575' if isinstance(e, AssertionError) else f'ERROR - step 575: {e}')

print("STEP 576 - Check element div#None.['wpr-dropdown-container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-dropdown-container']")))
    print('PASS - step 576')
except Exception as e:
    print('FAIL - step 576' if isinstance(e, AssertionError) else f'ERROR - step 576: {e}')

print("STEP 577 - Check element div#None.['wpr-closing-overlay']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-closing-overlay']")))
    print('PASS - step 577')
except Exception as e:
    print('FAIL - step 577' if isinstance(e, AssertionError) else f'ERROR - step 577: {e}')

print("STEP 578 - Check element div#None.['dropdowns_insert']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['dropdowns_insert']")))
    print('PASS - step 578')
except Exception as e:
    print('FAIL - step 578' if isinstance(e, AssertionError) else f'ERROR - step 578: {e}')

print("STEP 579 - Check element div#menuitemOne_tab_drop.['wpr-dropdown-nav', 'wpr-show']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "menuitemOne_tab_drop")))
    print('PASS - step 579')
except Exception as e:
    print('FAIL - step 579' if isinstance(e, AssertionError) else f'ERROR - step 579: {e}')

print("STEP 580 - Check element div#None.['submenu_data']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['submenu_data']")))
    print('PASS - step 580')
except Exception as e:
    print('FAIL - step 580' if isinstance(e, AssertionError) else f'ERROR - step 580: {e}')

print("STEP 581 - Check element ul#None.['wpr-submenu-container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-submenu-container']")))
    print('PASS - step 581')
except Exception as e:
    print('FAIL - step 581' if isinstance(e, AssertionError) else f'ERROR - step 581: {e}')

print("STEP 582 - Check element div#None.['wpr-submenu-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-submenu-item']")))
    print('PASS - step 582')
except Exception as e:
    print('FAIL - step 582' if isinstance(e, AssertionError) else f'ERROR - step 582: {e}')

print("STEP 583 - Check element div#None.['wpr-submenu-heading']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-submenu-heading']")))
    print('PASS - step 583')
except Exception as e:
    print('FAIL - step 583' if isinstance(e, AssertionError) else f'ERROR - step 583: {e}')

print("STEP 584 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 584')
except Exception as e:
    print('FAIL - step 584' if isinstance(e, AssertionError) else f'ERROR - step 584: {e}')

print("STEP 585 - Check element li#None.['headind_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['headind_content']")))
    print('PASS - step 585')
except Exception as e:
    print('FAIL - step 585' if isinstance(e, AssertionError) else f'ERROR - step 585: {e}')

print("STEP 586 - Check element label#None.['unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unselectable']")))
    print('PASS - step 586')
except Exception as e:
    print('FAIL - step 586' if isinstance(e, AssertionError) else f'ERROR - step 586: {e}')

print("STEP 587 - Check element div#None.['sub-submenu-data']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['sub-submenu-data']")))
    print('PASS - step 587')
except Exception as e:
    print('FAIL - step 587' if isinstance(e, AssertionError) else f'ERROR - step 587: {e}')

print("STEP 588 - Check element ul#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "ul")))
    print('PASS - step 588')
except Exception as e:
    print('FAIL - step 588' if isinstance(e, AssertionError) else f'ERROR - step 588: {e}')

print("STEP 589 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 589')
except Exception as e:
    print('FAIL - step 589' if isinstance(e, AssertionError) else f'ERROR - step 589: {e}')

print("STEP 590 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 590')
except Exception as e:
    print('FAIL - step 590' if isinstance(e, AssertionError) else f'ERROR - step 590: {e}')

print("STEP 591 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 591')
except Exception as e:
    print('FAIL - step 591' if isinstance(e, AssertionError) else f'ERROR - step 591: {e}')

print("STEP 592 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 592')
except Exception as e:
    print('FAIL - step 592' if isinstance(e, AssertionError) else f'ERROR - step 592: {e}')

print("STEP 593 - Check element label#None.['unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unselectable']")))
    print('PASS - step 593')
except Exception as e:
    print('FAIL - step 593' if isinstance(e, AssertionError) else f'ERROR - step 593: {e}')

print("STEP 594 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 594')
except Exception as e:
    print('FAIL - step 594' if isinstance(e, AssertionError) else f'ERROR - step 594: {e}')

print("STEP 595 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 595')
except Exception as e:
    print('FAIL - step 595' if isinstance(e, AssertionError) else f'ERROR - step 595: {e}')

print("STEP 596 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 596')
except Exception as e:
    print('FAIL - step 596' if isinstance(e, AssertionError) else f'ERROR - step 596: {e}')

print("STEP 597 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 597')
except Exception as e:
    print('FAIL - step 597' if isinstance(e, AssertionError) else f'ERROR - step 597: {e}')

print("STEP 598 - Check element label#None.['unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unselectable']")))
    print('PASS - step 598')
except Exception as e:
    print('FAIL - step 598' if isinstance(e, AssertionError) else f'ERROR - step 598: {e}')

print("STEP 599 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 599')
except Exception as e:
    print('FAIL - step 599' if isinstance(e, AssertionError) else f'ERROR - step 599: {e}')

print("STEP 600 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 600')
except Exception as e:
    print('FAIL - step 600' if isinstance(e, AssertionError) else f'ERROR - step 600: {e}')

print("STEP 601 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 601')
except Exception as e:
    print('FAIL - step 601' if isinstance(e, AssertionError) else f'ERROR - step 601: {e}')

print("STEP 602 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 602')
except Exception as e:
    print('FAIL - step 602' if isinstance(e, AssertionError) else f'ERROR - step 602: {e}')

print("STEP 603 - Check element label#None.['unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unselectable']")))
    print('PASS - step 603')
except Exception as e:
    print('FAIL - step 603' if isinstance(e, AssertionError) else f'ERROR - step 603: {e}')

print("STEP 604 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 604')
except Exception as e:
    print('FAIL - step 604' if isinstance(e, AssertionError) else f'ERROR - step 604: {e}')

print("STEP 605 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 605')
except Exception as e:
    print('FAIL - step 605' if isinstance(e, AssertionError) else f'ERROR - step 605: {e}')

print("STEP 606 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 606')
except Exception as e:
    print('FAIL - step 606' if isinstance(e, AssertionError) else f'ERROR - step 606: {e}')

print("STEP 607 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 607')
except Exception as e:
    print('FAIL - step 607' if isinstance(e, AssertionError) else f'ERROR - step 607: {e}')

print("STEP 608 - Check element label#None.['unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unselectable']")))
    print('PASS - step 608')
except Exception as e:
    print('FAIL - step 608' if isinstance(e, AssertionError) else f'ERROR - step 608: {e}')

print("STEP 609 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 609')
except Exception as e:
    print('FAIL - step 609' if isinstance(e, AssertionError) else f'ERROR - step 609: {e}')

print("STEP 610 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 610')
except Exception as e:
    print('FAIL - step 610' if isinstance(e, AssertionError) else f'ERROR - step 610: {e}')

print("STEP 611 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 611')
except Exception as e:
    print('FAIL - step 611' if isinstance(e, AssertionError) else f'ERROR - step 611: {e}')

print("STEP 612 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 612')
except Exception as e:
    print('FAIL - step 612' if isinstance(e, AssertionError) else f'ERROR - step 612: {e}')

print("STEP 613 - Check element label#None.['unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unselectable']")))
    print('PASS - step 613')
except Exception as e:
    print('FAIL - step 613' if isinstance(e, AssertionError) else f'ERROR - step 613: {e}')

print("STEP 614 - Check element div#None.['wpr-submenu-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-submenu-item']")))
    print('PASS - step 614')
except Exception as e:
    print('FAIL - step 614' if isinstance(e, AssertionError) else f'ERROR - step 614: {e}')

print("STEP 615 - Check element div#None.['wpr-submenu-heading']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-submenu-heading']")))
    print('PASS - step 615')
except Exception as e:
    print('FAIL - step 615' if isinstance(e, AssertionError) else f'ERROR - step 615: {e}')

print("STEP 616 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 616')
except Exception as e:
    print('FAIL - step 616' if isinstance(e, AssertionError) else f'ERROR - step 616: {e}')

print("STEP 617 - Check element li#None.['headind_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['headind_content']")))
    print('PASS - step 617')
except Exception as e:
    print('FAIL - step 617' if isinstance(e, AssertionError) else f'ERROR - step 617: {e}')

print("STEP 618 - Check element label#None.['unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unselectable']")))
    print('PASS - step 618')
except Exception as e:
    print('FAIL - step 618' if isinstance(e, AssertionError) else f'ERROR - step 618: {e}')

print("STEP 619 - Check element div#None.['sub-submenu-data']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['sub-submenu-data']")))
    print('PASS - step 619')
except Exception as e:
    print('FAIL - step 619' if isinstance(e, AssertionError) else f'ERROR - step 619: {e}')

print("STEP 620 - Check element ul#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "ul")))
    print('PASS - step 620')
except Exception as e:
    print('FAIL - step 620' if isinstance(e, AssertionError) else f'ERROR - step 620: {e}')

print("STEP 621 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 621')
except Exception as e:
    print('FAIL - step 621' if isinstance(e, AssertionError) else f'ERROR - step 621: {e}')

print("STEP 622 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 622')
except Exception as e:
    print('FAIL - step 622' if isinstance(e, AssertionError) else f'ERROR - step 622: {e}')

print("STEP 623 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 623')
except Exception as e:
    print('FAIL - step 623' if isinstance(e, AssertionError) else f'ERROR - step 623: {e}')

print("STEP 624 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 624')
except Exception as e:
    print('FAIL - step 624' if isinstance(e, AssertionError) else f'ERROR - step 624: {e}')

print("STEP 625 - Check element label#None.['unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unselectable']")))
    print('PASS - step 625')
except Exception as e:
    print('FAIL - step 625' if isinstance(e, AssertionError) else f'ERROR - step 625: {e}')

print("STEP 626 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 626')
except Exception as e:
    print('FAIL - step 626' if isinstance(e, AssertionError) else f'ERROR - step 626: {e}')

print("STEP 627 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 627')
except Exception as e:
    print('FAIL - step 627' if isinstance(e, AssertionError) else f'ERROR - step 627: {e}')

print("STEP 628 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 628')
except Exception as e:
    print('FAIL - step 628' if isinstance(e, AssertionError) else f'ERROR - step 628: {e}')

print("STEP 629 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 629')
except Exception as e:
    print('FAIL - step 629' if isinstance(e, AssertionError) else f'ERROR - step 629: {e}')

print("STEP 630 - Check element label#None.['unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unselectable']")))
    print('PASS - step 630')
except Exception as e:
    print('FAIL - step 630' if isinstance(e, AssertionError) else f'ERROR - step 630: {e}')

print("STEP 631 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 631')
except Exception as e:
    print('FAIL - step 631' if isinstance(e, AssertionError) else f'ERROR - step 631: {e}')

print("STEP 632 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 632')
except Exception as e:
    print('FAIL - step 632' if isinstance(e, AssertionError) else f'ERROR - step 632: {e}')

print("STEP 633 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 633')
except Exception as e:
    print('FAIL - step 633' if isinstance(e, AssertionError) else f'ERROR - step 633: {e}')

print("STEP 634 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 634')
except Exception as e:
    print('FAIL - step 634' if isinstance(e, AssertionError) else f'ERROR - step 634: {e}')

print("STEP 635 - Check element label#None.['unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unselectable']")))
    print('PASS - step 635')
except Exception as e:
    print('FAIL - step 635' if isinstance(e, AssertionError) else f'ERROR - step 635: {e}')

print("STEP 636 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 636')
except Exception as e:
    print('FAIL - step 636' if isinstance(e, AssertionError) else f'ERROR - step 636: {e}')

print("STEP 637 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 637')
except Exception as e:
    print('FAIL - step 637' if isinstance(e, AssertionError) else f'ERROR - step 637: {e}')

print("STEP 638 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 638')
except Exception as e:
    print('FAIL - step 638' if isinstance(e, AssertionError) else f'ERROR - step 638: {e}')

print("STEP 639 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 639')
except Exception as e:
    print('FAIL - step 639' if isinstance(e, AssertionError) else f'ERROR - step 639: {e}')

print("STEP 640 - Check element label#None.['unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unselectable']")))
    print('PASS - step 640')
except Exception as e:
    print('FAIL - step 640' if isinstance(e, AssertionError) else f'ERROR - step 640: {e}')

print("STEP 641 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 641')
except Exception as e:
    print('FAIL - step 641' if isinstance(e, AssertionError) else f'ERROR - step 641: {e}')

print("STEP 642 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 642')
except Exception as e:
    print('FAIL - step 642' if isinstance(e, AssertionError) else f'ERROR - step 642: {e}')

print("STEP 643 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 643')
except Exception as e:
    print('FAIL - step 643' if isinstance(e, AssertionError) else f'ERROR - step 643: {e}')

print("STEP 644 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 644')
except Exception as e:
    print('FAIL - step 644' if isinstance(e, AssertionError) else f'ERROR - step 644: {e}')

print("STEP 645 - Check element label#None.['unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unselectable']")))
    print('PASS - step 645')
except Exception as e:
    print('FAIL - step 645' if isinstance(e, AssertionError) else f'ERROR - step 645: {e}')

print("STEP 646 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 646')
except Exception as e:
    print('FAIL - step 646' if isinstance(e, AssertionError) else f'ERROR - step 646: {e}')

print("STEP 647 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 647')
except Exception as e:
    print('FAIL - step 647' if isinstance(e, AssertionError) else f'ERROR - step 647: {e}')

print("STEP 648 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 648')
except Exception as e:
    print('FAIL - step 648' if isinstance(e, AssertionError) else f'ERROR - step 648: {e}')

print("STEP 649 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 649')
except Exception as e:
    print('FAIL - step 649' if isinstance(e, AssertionError) else f'ERROR - step 649: {e}')

print("STEP 650 - Check element label#None.['unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unselectable']")))
    print('PASS - step 650')
except Exception as e:
    print('FAIL - step 650' if isinstance(e, AssertionError) else f'ERROR - step 650: {e}')

print("STEP 651 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 651')
except Exception as e:
    print('FAIL - step 651' if isinstance(e, AssertionError) else f'ERROR - step 651: {e}')

print("STEP 652 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 652')
except Exception as e:
    print('FAIL - step 652' if isinstance(e, AssertionError) else f'ERROR - step 652: {e}')

print("STEP 653 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 653')
except Exception as e:
    print('FAIL - step 653' if isinstance(e, AssertionError) else f'ERROR - step 653: {e}')

print("STEP 654 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 654')
except Exception as e:
    print('FAIL - step 654' if isinstance(e, AssertionError) else f'ERROR - step 654: {e}')

print("STEP 655 - Check element label#None.['unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unselectable']")))
    print('PASS - step 655')
except Exception as e:
    print('FAIL - step 655' if isinstance(e, AssertionError) else f'ERROR - step 655: {e}')

print("STEP 656 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 656')
except Exception as e:
    print('FAIL - step 656' if isinstance(e, AssertionError) else f'ERROR - step 656: {e}')

print("STEP 657 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 657')
except Exception as e:
    print('FAIL - step 657' if isinstance(e, AssertionError) else f'ERROR - step 657: {e}')

print("STEP 658 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 658')
except Exception as e:
    print('FAIL - step 658' if isinstance(e, AssertionError) else f'ERROR - step 658: {e}')

print("STEP 659 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 659')
except Exception as e:
    print('FAIL - step 659' if isinstance(e, AssertionError) else f'ERROR - step 659: {e}')

print("STEP 660 - Check element label#None.['unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unselectable']")))
    print('PASS - step 660')
except Exception as e:
    print('FAIL - step 660' if isinstance(e, AssertionError) else f'ERROR - step 660: {e}')

print("STEP 661 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 661')
except Exception as e:
    print('FAIL - step 661' if isinstance(e, AssertionError) else f'ERROR - step 661: {e}')

print("STEP 662 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 662')
except Exception as e:
    print('FAIL - step 662' if isinstance(e, AssertionError) else f'ERROR - step 662: {e}')

print("STEP 663 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 663')
except Exception as e:
    print('FAIL - step 663' if isinstance(e, AssertionError) else f'ERROR - step 663: {e}')

print("STEP 664 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 664')
except Exception as e:
    print('FAIL - step 664' if isinstance(e, AssertionError) else f'ERROR - step 664: {e}')

print("STEP 665 - Check element label#None.['unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unselectable']")))
    print('PASS - step 665')
except Exception as e:
    print('FAIL - step 665' if isinstance(e, AssertionError) else f'ERROR - step 665: {e}')

print("STEP 666 - Check element div#None.['wpr-submenu-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-submenu-item']")))
    print('PASS - step 666')
except Exception as e:
    print('FAIL - step 666' if isinstance(e, AssertionError) else f'ERROR - step 666: {e}')

print("STEP 667 - Check element div#None.['wpr-submenu-heading']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-submenu-heading']")))
    print('PASS - step 667')
except Exception as e:
    print('FAIL - step 667' if isinstance(e, AssertionError) else f'ERROR - step 667: {e}')

print("STEP 668 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 668')
except Exception as e:
    print('FAIL - step 668' if isinstance(e, AssertionError) else f'ERROR - step 668: {e}')

print("STEP 669 - Check element li#None.['headind_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['headind_content']")))
    print('PASS - step 669')
except Exception as e:
    print('FAIL - step 669' if isinstance(e, AssertionError) else f'ERROR - step 669: {e}')

print("STEP 670 - Check element label#None.['unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unselectable']")))
    print('PASS - step 670')
except Exception as e:
    print('FAIL - step 670' if isinstance(e, AssertionError) else f'ERROR - step 670: {e}')

print("STEP 671 - Check element div#None.['sub-submenu-data']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['sub-submenu-data']")))
    print('PASS - step 671')
except Exception as e:
    print('FAIL - step 671' if isinstance(e, AssertionError) else f'ERROR - step 671: {e}')

print("STEP 672 - Check element ul#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "ul")))
    print('PASS - step 672')
except Exception as e:
    print('FAIL - step 672' if isinstance(e, AssertionError) else f'ERROR - step 672: {e}')

print("STEP 673 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 673')
except Exception as e:
    print('FAIL - step 673' if isinstance(e, AssertionError) else f'ERROR - step 673: {e}')

print("STEP 674 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 674')
except Exception as e:
    print('FAIL - step 674' if isinstance(e, AssertionError) else f'ERROR - step 674: {e}')

print("STEP 675 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 675')
except Exception as e:
    print('FAIL - step 675' if isinstance(e, AssertionError) else f'ERROR - step 675: {e}')

print("STEP 676 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 676')
except Exception as e:
    print('FAIL - step 676' if isinstance(e, AssertionError) else f'ERROR - step 676: {e}')

print("STEP 677 - Check element label#None.['unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unselectable']")))
    print('PASS - step 677')
except Exception as e:
    print('FAIL - step 677' if isinstance(e, AssertionError) else f'ERROR - step 677: {e}')

print("STEP 678 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 678')
except Exception as e:
    print('FAIL - step 678' if isinstance(e, AssertionError) else f'ERROR - step 678: {e}')

print("STEP 679 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 679')
except Exception as e:
    print('FAIL - step 679' if isinstance(e, AssertionError) else f'ERROR - step 679: {e}')

print("STEP 680 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 680')
except Exception as e:
    print('FAIL - step 680' if isinstance(e, AssertionError) else f'ERROR - step 680: {e}')

print("STEP 681 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 681')
except Exception as e:
    print('FAIL - step 681' if isinstance(e, AssertionError) else f'ERROR - step 681: {e}')

print("STEP 682 - Check element label#None.['unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unselectable']")))
    print('PASS - step 682')
except Exception as e:
    print('FAIL - step 682' if isinstance(e, AssertionError) else f'ERROR - step 682: {e}')

print("STEP 683 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 683')
except Exception as e:
    print('FAIL - step 683' if isinstance(e, AssertionError) else f'ERROR - step 683: {e}')

print("STEP 684 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 684')
except Exception as e:
    print('FAIL - step 684' if isinstance(e, AssertionError) else f'ERROR - step 684: {e}')

print("STEP 685 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 685')
except Exception as e:
    print('FAIL - step 685' if isinstance(e, AssertionError) else f'ERROR - step 685: {e}')

print("STEP 686 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 686')
except Exception as e:
    print('FAIL - step 686' if isinstance(e, AssertionError) else f'ERROR - step 686: {e}')

print("STEP 687 - Check element label#None.['unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unselectable']")))
    print('PASS - step 687')
except Exception as e:
    print('FAIL - step 687' if isinstance(e, AssertionError) else f'ERROR - step 687: {e}')

print("STEP 688 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 688')
except Exception as e:
    print('FAIL - step 688' if isinstance(e, AssertionError) else f'ERROR - step 688: {e}')

print("STEP 689 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 689')
except Exception as e:
    print('FAIL - step 689' if isinstance(e, AssertionError) else f'ERROR - step 689: {e}')

print("STEP 690 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 690')
except Exception as e:
    print('FAIL - step 690' if isinstance(e, AssertionError) else f'ERROR - step 690: {e}')

print("STEP 691 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 691')
except Exception as e:
    print('FAIL - step 691' if isinstance(e, AssertionError) else f'ERROR - step 691: {e}')

print("STEP 692 - Check element label#None.['unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unselectable']")))
    print('PASS - step 692')
except Exception as e:
    print('FAIL - step 692' if isinstance(e, AssertionError) else f'ERROR - step 692: {e}')

print("STEP 693 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 693')
except Exception as e:
    print('FAIL - step 693' if isinstance(e, AssertionError) else f'ERROR - step 693: {e}')

print("STEP 694 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 694')
except Exception as e:
    print('FAIL - step 694' if isinstance(e, AssertionError) else f'ERROR - step 694: {e}')

print("STEP 695 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 695')
except Exception as e:
    print('FAIL - step 695' if isinstance(e, AssertionError) else f'ERROR - step 695: {e}')

print("STEP 696 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 696')
except Exception as e:
    print('FAIL - step 696' if isinstance(e, AssertionError) else f'ERROR - step 696: {e}')

print("STEP 697 - Check element label#None.['unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unselectable']")))
    print('PASS - step 697')
except Exception as e:
    print('FAIL - step 697' if isinstance(e, AssertionError) else f'ERROR - step 697: {e}')

print("STEP 698 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 698')
except Exception as e:
    print('FAIL - step 698' if isinstance(e, AssertionError) else f'ERROR - step 698: {e}')

print("STEP 699 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 699')
except Exception as e:
    print('FAIL - step 699' if isinstance(e, AssertionError) else f'ERROR - step 699: {e}')

print("STEP 700 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 700')
except Exception as e:
    print('FAIL - step 700' if isinstance(e, AssertionError) else f'ERROR - step 700: {e}')

print("STEP 701 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 701')
except Exception as e:
    print('FAIL - step 701' if isinstance(e, AssertionError) else f'ERROR - step 701: {e}')

print("STEP 702 - Check element label#None.['unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unselectable']")))
    print('PASS - step 702')
except Exception as e:
    print('FAIL - step 702' if isinstance(e, AssertionError) else f'ERROR - step 702: {e}')

print("STEP 703 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 703')
except Exception as e:
    print('FAIL - step 703' if isinstance(e, AssertionError) else f'ERROR - step 703: {e}')

print("STEP 704 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 704')
except Exception as e:
    print('FAIL - step 704' if isinstance(e, AssertionError) else f'ERROR - step 704: {e}')

print("STEP 705 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 705')
except Exception as e:
    print('FAIL - step 705' if isinstance(e, AssertionError) else f'ERROR - step 705: {e}')

print("STEP 706 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 706')
except Exception as e:
    print('FAIL - step 706' if isinstance(e, AssertionError) else f'ERROR - step 706: {e}')

print("STEP 707 - Check element label#None.['unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unselectable']")))
    print('PASS - step 707')
except Exception as e:
    print('FAIL - step 707' if isinstance(e, AssertionError) else f'ERROR - step 707: {e}')

print("STEP 708 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 708')
except Exception as e:
    print('FAIL - step 708' if isinstance(e, AssertionError) else f'ERROR - step 708: {e}')

print("STEP 709 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 709')
except Exception as e:
    print('FAIL - step 709' if isinstance(e, AssertionError) else f'ERROR - step 709: {e}')

print("STEP 710 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 710')
except Exception as e:
    print('FAIL - step 710' if isinstance(e, AssertionError) else f'ERROR - step 710: {e}')

print("STEP 711 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 711')
except Exception as e:
    print('FAIL - step 711' if isinstance(e, AssertionError) else f'ERROR - step 711: {e}')

print("STEP 712 - Check element label#None.['unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unselectable']")))
    print('PASS - step 712')
except Exception as e:
    print('FAIL - step 712' if isinstance(e, AssertionError) else f'ERROR - step 712: {e}')

print("STEP 713 - Check element div#None.['wpr-submenu-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-submenu-item']")))
    print('PASS - step 713')
except Exception as e:
    print('FAIL - step 713' if isinstance(e, AssertionError) else f'ERROR - step 713: {e}')

print("STEP 714 - Check element div#None.['wpr-submenu-heading']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-submenu-heading']")))
    print('PASS - step 714')
except Exception as e:
    print('FAIL - step 714' if isinstance(e, AssertionError) else f'ERROR - step 714: {e}')

print("STEP 715 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 715')
except Exception as e:
    print('FAIL - step 715' if isinstance(e, AssertionError) else f'ERROR - step 715: {e}')

print("STEP 716 - Check element li#None.['headind_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['headind_content']")))
    print('PASS - step 716')
except Exception as e:
    print('FAIL - step 716' if isinstance(e, AssertionError) else f'ERROR - step 716: {e}')

print("STEP 717 - Check element label#None.['unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unselectable']")))
    print('PASS - step 717')
except Exception as e:
    print('FAIL - step 717' if isinstance(e, AssertionError) else f'ERROR - step 717: {e}')

print("STEP 718 - Check element div#None.['sub-submenu-data']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['sub-submenu-data']")))
    print('PASS - step 718')
except Exception as e:
    print('FAIL - step 718' if isinstance(e, AssertionError) else f'ERROR - step 718: {e}')

print("STEP 719 - Check element ul#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "ul")))
    print('PASS - step 719')
except Exception as e:
    print('FAIL - step 719' if isinstance(e, AssertionError) else f'ERROR - step 719: {e}')

print("STEP 720 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 720')
except Exception as e:
    print('FAIL - step 720' if isinstance(e, AssertionError) else f'ERROR - step 720: {e}')

print("STEP 721 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 721')
except Exception as e:
    print('FAIL - step 721' if isinstance(e, AssertionError) else f'ERROR - step 721: {e}')

print("STEP 722 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 722')
except Exception as e:
    print('FAIL - step 722' if isinstance(e, AssertionError) else f'ERROR - step 722: {e}')

print("STEP 723 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 723')
except Exception as e:
    print('FAIL - step 723' if isinstance(e, AssertionError) else f'ERROR - step 723: {e}')

print("STEP 724 - Check element label#None.['unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unselectable']")))
    print('PASS - step 724')
except Exception as e:
    print('FAIL - step 724' if isinstance(e, AssertionError) else f'ERROR - step 724: {e}')

print("STEP 725 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 725')
except Exception as e:
    print('FAIL - step 725' if isinstance(e, AssertionError) else f'ERROR - step 725: {e}')

print("STEP 726 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 726')
except Exception as e:
    print('FAIL - step 726' if isinstance(e, AssertionError) else f'ERROR - step 726: {e}')

print("STEP 727 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 727')
except Exception as e:
    print('FAIL - step 727' if isinstance(e, AssertionError) else f'ERROR - step 727: {e}')

print("STEP 728 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 728')
except Exception as e:
    print('FAIL - step 728' if isinstance(e, AssertionError) else f'ERROR - step 728: {e}')

print("STEP 729 - Check element label#None.['unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unselectable']")))
    print('PASS - step 729')
except Exception as e:
    print('FAIL - step 729' if isinstance(e, AssertionError) else f'ERROR - step 729: {e}')

print("STEP 730 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 730')
except Exception as e:
    print('FAIL - step 730' if isinstance(e, AssertionError) else f'ERROR - step 730: {e}')

print("STEP 731 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 731')
except Exception as e:
    print('FAIL - step 731' if isinstance(e, AssertionError) else f'ERROR - step 731: {e}')

print("STEP 732 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 732')
except Exception as e:
    print('FAIL - step 732' if isinstance(e, AssertionError) else f'ERROR - step 732: {e}')

print("STEP 733 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 733')
except Exception as e:
    print('FAIL - step 733' if isinstance(e, AssertionError) else f'ERROR - step 733: {e}')

print("STEP 734 - Check element label#None.['unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unselectable']")))
    print('PASS - step 734')
except Exception as e:
    print('FAIL - step 734' if isinstance(e, AssertionError) else f'ERROR - step 734: {e}')

print("STEP 735 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 735')
except Exception as e:
    print('FAIL - step 735' if isinstance(e, AssertionError) else f'ERROR - step 735: {e}')

print("STEP 736 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 736')
except Exception as e:
    print('FAIL - step 736' if isinstance(e, AssertionError) else f'ERROR - step 736: {e}')

print("STEP 737 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 737')
except Exception as e:
    print('FAIL - step 737' if isinstance(e, AssertionError) else f'ERROR - step 737: {e}')

print("STEP 738 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 738')
except Exception as e:
    print('FAIL - step 738' if isinstance(e, AssertionError) else f'ERROR - step 738: {e}')

print("STEP 739 - Check element label#None.['unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unselectable']")))
    print('PASS - step 739')
except Exception as e:
    print('FAIL - step 739' if isinstance(e, AssertionError) else f'ERROR - step 739: {e}')

print("STEP 740 - Check element div#None.['wpr-close-submenu-desk']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-close-submenu-desk']")))
    print('PASS - step 740')
except Exception as e:
    print('FAIL - step 740' if isinstance(e, AssertionError) else f'ERROR - step 740: {e}')

print("STEP 741 - Check element a#None.['close_icon_desk']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['close_icon_desk']")))
    print('PASS - step 741')
except Exception as e:
    print('FAIL - step 741' if isinstance(e, AssertionError) else f'ERROR - step 741: {e}')

print("STEP 742 - Check element div#menuitemTwo_tab_drop.['wpr-dropdown-nav', 'wpr-show']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "menuitemTwo_tab_drop")))
    print('PASS - step 742')
except Exception as e:
    print('FAIL - step 742' if isinstance(e, AssertionError) else f'ERROR - step 742: {e}')

print("STEP 743 - Check element div#None.['submenu_data']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['submenu_data']")))
    print('PASS - step 743')
except Exception as e:
    print('FAIL - step 743' if isinstance(e, AssertionError) else f'ERROR - step 743: {e}')

print("STEP 744 - Check element ul#None.['wpr-submenu-container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-submenu-container']")))
    print('PASS - step 744')
except Exception as e:
    print('FAIL - step 744' if isinstance(e, AssertionError) else f'ERROR - step 744: {e}')

print("STEP 745 - Check element div#None.['wpr-submenu-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-submenu-item']")))
    print('PASS - step 745')
except Exception as e:
    print('FAIL - step 745' if isinstance(e, AssertionError) else f'ERROR - step 745: {e}')

print("STEP 746 - Check element div#None.['wpr-submenu-heading']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-submenu-heading']")))
    print('PASS - step 746')
except Exception as e:
    print('FAIL - step 746' if isinstance(e, AssertionError) else f'ERROR - step 746: {e}')

print("STEP 747 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 747')
except Exception as e:
    print('FAIL - step 747' if isinstance(e, AssertionError) else f'ERROR - step 747: {e}')

print("STEP 748 - Check element li#None.['headind_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['headind_content']")))
    print('PASS - step 748')
except Exception as e:
    print('FAIL - step 748' if isinstance(e, AssertionError) else f'ERROR - step 748: {e}')

print("STEP 749 - Check element label#None.['unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unselectable']")))
    print('PASS - step 749')
except Exception as e:
    print('FAIL - step 749' if isinstance(e, AssertionError) else f'ERROR - step 749: {e}')

print("STEP 750 - Check element div#None.['sub-submenu-data']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['sub-submenu-data']")))
    print('PASS - step 750')
except Exception as e:
    print('FAIL - step 750' if isinstance(e, AssertionError) else f'ERROR - step 750: {e}')

print("STEP 751 - Check element ul#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "ul")))
    print('PASS - step 751')
except Exception as e:
    print('FAIL - step 751' if isinstance(e, AssertionError) else f'ERROR - step 751: {e}')

print("STEP 752 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 752')
except Exception as e:
    print('FAIL - step 752' if isinstance(e, AssertionError) else f'ERROR - step 752: {e}')

print("STEP 753 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 753')
except Exception as e:
    print('FAIL - step 753' if isinstance(e, AssertionError) else f'ERROR - step 753: {e}')

print("STEP 754 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 754')
except Exception as e:
    print('FAIL - step 754' if isinstance(e, AssertionError) else f'ERROR - step 754: {e}')

print("STEP 755 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 755')
except Exception as e:
    print('FAIL - step 755' if isinstance(e, AssertionError) else f'ERROR - step 755: {e}')

print("STEP 756 - Check element label#None.['unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unselectable']")))
    print('PASS - step 756')
except Exception as e:
    print('FAIL - step 756' if isinstance(e, AssertionError) else f'ERROR - step 756: {e}')

print("STEP 757 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 757')
except Exception as e:
    print('FAIL - step 757' if isinstance(e, AssertionError) else f'ERROR - step 757: {e}')

print("STEP 758 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 758')
except Exception as e:
    print('FAIL - step 758' if isinstance(e, AssertionError) else f'ERROR - step 758: {e}')

print("STEP 759 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 759')
except Exception as e:
    print('FAIL - step 759' if isinstance(e, AssertionError) else f'ERROR - step 759: {e}')

print("STEP 760 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 760')
except Exception as e:
    print('FAIL - step 760' if isinstance(e, AssertionError) else f'ERROR - step 760: {e}')

print("STEP 761 - Check element label#None.['unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unselectable']")))
    print('PASS - step 761')
except Exception as e:
    print('FAIL - step 761' if isinstance(e, AssertionError) else f'ERROR - step 761: {e}')

print("STEP 762 - Check element div#None.['wpr-close-submenu-desk']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-close-submenu-desk']")))
    print('PASS - step 762')
except Exception as e:
    print('FAIL - step 762' if isinstance(e, AssertionError) else f'ERROR - step 762: {e}')

print("STEP 763 - Check element a#None.['close_icon_desk']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['close_icon_desk']")))
    print('PASS - step 763')
except Exception as e:
    print('FAIL - step 763' if isinstance(e, AssertionError) else f'ERROR - step 763: {e}')

print("STEP 764 - Check element div#menuitemThree_tab_drop.['wpr-dropdown-nav', 'wpr-show']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "menuitemThree_tab_drop")))
    print('PASS - step 764')
except Exception as e:
    print('FAIL - step 764' if isinstance(e, AssertionError) else f'ERROR - step 764: {e}')

print("STEP 765 - Check element div#None.['submenu_data']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['submenu_data']")))
    print('PASS - step 765')
except Exception as e:
    print('FAIL - step 765' if isinstance(e, AssertionError) else f'ERROR - step 765: {e}')

print("STEP 766 - Check element ul#None.['wpr-submenu-container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-submenu-container']")))
    print('PASS - step 766')
except Exception as e:
    print('FAIL - step 766' if isinstance(e, AssertionError) else f'ERROR - step 766: {e}')

print("STEP 767 - Check element div#None.['wpr-submenu-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-submenu-item']")))
    print('PASS - step 767')
except Exception as e:
    print('FAIL - step 767' if isinstance(e, AssertionError) else f'ERROR - step 767: {e}')

print("STEP 768 - Check element div#None.['wpr-submenu-heading']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-submenu-heading']")))
    print('PASS - step 768')
except Exception as e:
    print('FAIL - step 768' if isinstance(e, AssertionError) else f'ERROR - step 768: {e}')

print("STEP 769 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 769')
except Exception as e:
    print('FAIL - step 769' if isinstance(e, AssertionError) else f'ERROR - step 769: {e}')

print("STEP 770 - Check element li#None.['headind_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['headind_content']")))
    print('PASS - step 770')
except Exception as e:
    print('FAIL - step 770' if isinstance(e, AssertionError) else f'ERROR - step 770: {e}')

print("STEP 771 - Check element label#None.['unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unselectable']")))
    print('PASS - step 771')
except Exception as e:
    print('FAIL - step 771' if isinstance(e, AssertionError) else f'ERROR - step 771: {e}')

print("STEP 772 - Check element div#None.['sub-submenu-data']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['sub-submenu-data']")))
    print('PASS - step 772')
except Exception as e:
    print('FAIL - step 772' if isinstance(e, AssertionError) else f'ERROR - step 772: {e}')

print("STEP 773 - Check element ul#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "ul")))
    print('PASS - step 773')
except Exception as e:
    print('FAIL - step 773' if isinstance(e, AssertionError) else f'ERROR - step 773: {e}')

print("STEP 774 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 774')
except Exception as e:
    print('FAIL - step 774' if isinstance(e, AssertionError) else f'ERROR - step 774: {e}')

print("STEP 775 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 775')
except Exception as e:
    print('FAIL - step 775' if isinstance(e, AssertionError) else f'ERROR - step 775: {e}')

print("STEP 776 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 776')
except Exception as e:
    print('FAIL - step 776' if isinstance(e, AssertionError) else f'ERROR - step 776: {e}')

print("STEP 777 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 777')
except Exception as e:
    print('FAIL - step 777' if isinstance(e, AssertionError) else f'ERROR - step 777: {e}')

print("STEP 778 - Check element label#None.['unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unselectable']")))
    print('PASS - step 778')
except Exception as e:
    print('FAIL - step 778' if isinstance(e, AssertionError) else f'ERROR - step 778: {e}')

print("STEP 779 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 779')
except Exception as e:
    print('FAIL - step 779' if isinstance(e, AssertionError) else f'ERROR - step 779: {e}')

print("STEP 780 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 780')
except Exception as e:
    print('FAIL - step 780' if isinstance(e, AssertionError) else f'ERROR - step 780: {e}')

print("STEP 781 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 781')
except Exception as e:
    print('FAIL - step 781' if isinstance(e, AssertionError) else f'ERROR - step 781: {e}')

print("STEP 782 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 782')
except Exception as e:
    print('FAIL - step 782' if isinstance(e, AssertionError) else f'ERROR - step 782: {e}')

print("STEP 783 - Check element label#None.['unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unselectable']")))
    print('PASS - step 783')
except Exception as e:
    print('FAIL - step 783' if isinstance(e, AssertionError) else f'ERROR - step 783: {e}')

print("STEP 784 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 784')
except Exception as e:
    print('FAIL - step 784' if isinstance(e, AssertionError) else f'ERROR - step 784: {e}')

print("STEP 785 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 785')
except Exception as e:
    print('FAIL - step 785' if isinstance(e, AssertionError) else f'ERROR - step 785: {e}')

print("STEP 786 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 786')
except Exception as e:
    print('FAIL - step 786' if isinstance(e, AssertionError) else f'ERROR - step 786: {e}')

print("STEP 787 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 787')
except Exception as e:
    print('FAIL - step 787' if isinstance(e, AssertionError) else f'ERROR - step 787: {e}')

print("STEP 788 - Check element label#None.['unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unselectable']")))
    print('PASS - step 788')
except Exception as e:
    print('FAIL - step 788' if isinstance(e, AssertionError) else f'ERROR - step 788: {e}')

print("STEP 789 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 789')
except Exception as e:
    print('FAIL - step 789' if isinstance(e, AssertionError) else f'ERROR - step 789: {e}')

print("STEP 790 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 790')
except Exception as e:
    print('FAIL - step 790' if isinstance(e, AssertionError) else f'ERROR - step 790: {e}')

print("STEP 791 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 791')
except Exception as e:
    print('FAIL - step 791' if isinstance(e, AssertionError) else f'ERROR - step 791: {e}')

print("STEP 792 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 792')
except Exception as e:
    print('FAIL - step 792' if isinstance(e, AssertionError) else f'ERROR - step 792: {e}')

print("STEP 793 - Check element label#None.['unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unselectable']")))
    print('PASS - step 793')
except Exception as e:
    print('FAIL - step 793' if isinstance(e, AssertionError) else f'ERROR - step 793: {e}')

print("STEP 794 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 794')
except Exception as e:
    print('FAIL - step 794' if isinstance(e, AssertionError) else f'ERROR - step 794: {e}')

print("STEP 795 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 795')
except Exception as e:
    print('FAIL - step 795' if isinstance(e, AssertionError) else f'ERROR - step 795: {e}')

print("STEP 796 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 796')
except Exception as e:
    print('FAIL - step 796' if isinstance(e, AssertionError) else f'ERROR - step 796: {e}')

print("STEP 797 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 797')
except Exception as e:
    print('FAIL - step 797' if isinstance(e, AssertionError) else f'ERROR - step 797: {e}')

print("STEP 798 - Check element label#None.['unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unselectable']")))
    print('PASS - step 798')
except Exception as e:
    print('FAIL - step 798' if isinstance(e, AssertionError) else f'ERROR - step 798: {e}')

print("STEP 799 - Check element div#None.['wpr-submenu-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-submenu-item']")))
    print('PASS - step 799')
except Exception as e:
    print('FAIL - step 799' if isinstance(e, AssertionError) else f'ERROR - step 799: {e}')

print("STEP 800 - Check element div#None.['wpr-submenu-heading']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-submenu-heading']")))
    print('PASS - step 800')
except Exception as e:
    print('FAIL - step 800' if isinstance(e, AssertionError) else f'ERROR - step 800: {e}')

print("STEP 801 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 801')
except Exception as e:
    print('FAIL - step 801' if isinstance(e, AssertionError) else f'ERROR - step 801: {e}')

print("STEP 802 - Check element li#None.['headind_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['headind_content']")))
    print('PASS - step 802')
except Exception as e:
    print('FAIL - step 802' if isinstance(e, AssertionError) else f'ERROR - step 802: {e}')

print("STEP 803 - Check element label#None.['unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unselectable']")))
    print('PASS - step 803')
except Exception as e:
    print('FAIL - step 803' if isinstance(e, AssertionError) else f'ERROR - step 803: {e}')

print("STEP 804 - Check element div#None.['sub-submenu-data']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['sub-submenu-data']")))
    print('PASS - step 804')
except Exception as e:
    print('FAIL - step 804' if isinstance(e, AssertionError) else f'ERROR - step 804: {e}')

print("STEP 805 - Check element ul#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "ul")))
    print('PASS - step 805')
except Exception as e:
    print('FAIL - step 805' if isinstance(e, AssertionError) else f'ERROR - step 805: {e}')

print("STEP 806 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 806')
except Exception as e:
    print('FAIL - step 806' if isinstance(e, AssertionError) else f'ERROR - step 806: {e}')

print("STEP 807 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 807')
except Exception as e:
    print('FAIL - step 807' if isinstance(e, AssertionError) else f'ERROR - step 807: {e}')

print("STEP 808 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 808')
except Exception as e:
    print('FAIL - step 808' if isinstance(e, AssertionError) else f'ERROR - step 808: {e}')

print("STEP 809 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 809')
except Exception as e:
    print('FAIL - step 809' if isinstance(e, AssertionError) else f'ERROR - step 809: {e}')

print("STEP 810 - Check element label#None.['unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unselectable']")))
    print('PASS - step 810')
except Exception as e:
    print('FAIL - step 810' if isinstance(e, AssertionError) else f'ERROR - step 810: {e}')

print("STEP 811 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 811')
except Exception as e:
    print('FAIL - step 811' if isinstance(e, AssertionError) else f'ERROR - step 811: {e}')

print("STEP 812 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 812')
except Exception as e:
    print('FAIL - step 812' if isinstance(e, AssertionError) else f'ERROR - step 812: {e}')

print("STEP 813 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 813')
except Exception as e:
    print('FAIL - step 813' if isinstance(e, AssertionError) else f'ERROR - step 813: {e}')

print("STEP 814 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 814')
except Exception as e:
    print('FAIL - step 814' if isinstance(e, AssertionError) else f'ERROR - step 814: {e}')

print("STEP 815 - Check element label#None.['unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unselectable']")))
    print('PASS - step 815')
except Exception as e:
    print('FAIL - step 815' if isinstance(e, AssertionError) else f'ERROR - step 815: {e}')

print("STEP 816 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 816')
except Exception as e:
    print('FAIL - step 816' if isinstance(e, AssertionError) else f'ERROR - step 816: {e}')

print("STEP 817 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 817')
except Exception as e:
    print('FAIL - step 817' if isinstance(e, AssertionError) else f'ERROR - step 817: {e}')

print("STEP 818 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 818')
except Exception as e:
    print('FAIL - step 818' if isinstance(e, AssertionError) else f'ERROR - step 818: {e}')

print("STEP 819 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 819')
except Exception as e:
    print('FAIL - step 819' if isinstance(e, AssertionError) else f'ERROR - step 819: {e}')

print("STEP 820 - Check element label#None.['unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unselectable']")))
    print('PASS - step 820')
except Exception as e:
    print('FAIL - step 820' if isinstance(e, AssertionError) else f'ERROR - step 820: {e}')

print("STEP 821 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 821')
except Exception as e:
    print('FAIL - step 821' if isinstance(e, AssertionError) else f'ERROR - step 821: {e}')

print("STEP 822 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 822')
except Exception as e:
    print('FAIL - step 822' if isinstance(e, AssertionError) else f'ERROR - step 822: {e}')

print("STEP 823 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 823')
except Exception as e:
    print('FAIL - step 823' if isinstance(e, AssertionError) else f'ERROR - step 823: {e}')

print("STEP 824 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 824')
except Exception as e:
    print('FAIL - step 824' if isinstance(e, AssertionError) else f'ERROR - step 824: {e}')

print("STEP 825 - Check element label#None.['unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unselectable']")))
    print('PASS - step 825')
except Exception as e:
    print('FAIL - step 825' if isinstance(e, AssertionError) else f'ERROR - step 825: {e}')

print("STEP 826 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 826')
except Exception as e:
    print('FAIL - step 826' if isinstance(e, AssertionError) else f'ERROR - step 826: {e}')

print("STEP 827 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 827')
except Exception as e:
    print('FAIL - step 827' if isinstance(e, AssertionError) else f'ERROR - step 827: {e}')

print("STEP 828 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 828')
except Exception as e:
    print('FAIL - step 828' if isinstance(e, AssertionError) else f'ERROR - step 828: {e}')

print("STEP 829 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 829')
except Exception as e:
    print('FAIL - step 829' if isinstance(e, AssertionError) else f'ERROR - step 829: {e}')

print("STEP 830 - Check element label#None.['unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unselectable']")))
    print('PASS - step 830')
except Exception as e:
    print('FAIL - step 830' if isinstance(e, AssertionError) else f'ERROR - step 830: {e}')

print("STEP 831 - Check element div#None.['wpr-submenu-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-submenu-item']")))
    print('PASS - step 831')
except Exception as e:
    print('FAIL - step 831' if isinstance(e, AssertionError) else f'ERROR - step 831: {e}')

print("STEP 832 - Check element div#None.['wpr-submenu-heading']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-submenu-heading']")))
    print('PASS - step 832')
except Exception as e:
    print('FAIL - step 832' if isinstance(e, AssertionError) else f'ERROR - step 832: {e}')

print("STEP 833 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 833')
except Exception as e:
    print('FAIL - step 833' if isinstance(e, AssertionError) else f'ERROR - step 833: {e}')

print("STEP 834 - Check element li#None.['headind_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['headind_content']")))
    print('PASS - step 834')
except Exception as e:
    print('FAIL - step 834' if isinstance(e, AssertionError) else f'ERROR - step 834: {e}')

print("STEP 835 - Check element label#None.['unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unselectable']")))
    print('PASS - step 835')
except Exception as e:
    print('FAIL - step 835' if isinstance(e, AssertionError) else f'ERROR - step 835: {e}')

print("STEP 836 - Check element div#None.['sub-submenu-data']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['sub-submenu-data']")))
    print('PASS - step 836')
except Exception as e:
    print('FAIL - step 836' if isinstance(e, AssertionError) else f'ERROR - step 836: {e}')

print("STEP 837 - Check element ul#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "ul")))
    print('PASS - step 837')
except Exception as e:
    print('FAIL - step 837' if isinstance(e, AssertionError) else f'ERROR - step 837: {e}')

print("STEP 838 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 838')
except Exception as e:
    print('FAIL - step 838' if isinstance(e, AssertionError) else f'ERROR - step 838: {e}')

print("STEP 839 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 839')
except Exception as e:
    print('FAIL - step 839' if isinstance(e, AssertionError) else f'ERROR - step 839: {e}')

print("STEP 840 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 840')
except Exception as e:
    print('FAIL - step 840' if isinstance(e, AssertionError) else f'ERROR - step 840: {e}')

print("STEP 841 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 841')
except Exception as e:
    print('FAIL - step 841' if isinstance(e, AssertionError) else f'ERROR - step 841: {e}')

print("STEP 842 - Check element label#None.['unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unselectable']")))
    print('PASS - step 842')
except Exception as e:
    print('FAIL - step 842' if isinstance(e, AssertionError) else f'ERROR - step 842: {e}')

print("STEP 843 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 843')
except Exception as e:
    print('FAIL - step 843' if isinstance(e, AssertionError) else f'ERROR - step 843: {e}')

print("STEP 844 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 844')
except Exception as e:
    print('FAIL - step 844' if isinstance(e, AssertionError) else f'ERROR - step 844: {e}')

print("STEP 845 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 845')
except Exception as e:
    print('FAIL - step 845' if isinstance(e, AssertionError) else f'ERROR - step 845: {e}')

print("STEP 846 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 846')
except Exception as e:
    print('FAIL - step 846' if isinstance(e, AssertionError) else f'ERROR - step 846: {e}')

print("STEP 847 - Check element label#None.['unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unselectable']")))
    print('PASS - step 847')
except Exception as e:
    print('FAIL - step 847' if isinstance(e, AssertionError) else f'ERROR - step 847: {e}')

print("STEP 848 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 848')
except Exception as e:
    print('FAIL - step 848' if isinstance(e, AssertionError) else f'ERROR - step 848: {e}')

print("STEP 849 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 849')
except Exception as e:
    print('FAIL - step 849' if isinstance(e, AssertionError) else f'ERROR - step 849: {e}')

print("STEP 850 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 850')
except Exception as e:
    print('FAIL - step 850' if isinstance(e, AssertionError) else f'ERROR - step 850: {e}')

print("STEP 851 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 851')
except Exception as e:
    print('FAIL - step 851' if isinstance(e, AssertionError) else f'ERROR - step 851: {e}')

print("STEP 852 - Check element label#None.['unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unselectable']")))
    print('PASS - step 852')
except Exception as e:
    print('FAIL - step 852' if isinstance(e, AssertionError) else f'ERROR - step 852: {e}')

print("STEP 853 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 853')
except Exception as e:
    print('FAIL - step 853' if isinstance(e, AssertionError) else f'ERROR - step 853: {e}')

print("STEP 854 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 854')
except Exception as e:
    print('FAIL - step 854' if isinstance(e, AssertionError) else f'ERROR - step 854: {e}')

print("STEP 855 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 855')
except Exception as e:
    print('FAIL - step 855' if isinstance(e, AssertionError) else f'ERROR - step 855: {e}')

print("STEP 856 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 856')
except Exception as e:
    print('FAIL - step 856' if isinstance(e, AssertionError) else f'ERROR - step 856: {e}')

print("STEP 857 - Check element label#None.['unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unselectable']")))
    print('PASS - step 857')
except Exception as e:
    print('FAIL - step 857' if isinstance(e, AssertionError) else f'ERROR - step 857: {e}')

print("STEP 858 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 858')
except Exception as e:
    print('FAIL - step 858' if isinstance(e, AssertionError) else f'ERROR - step 858: {e}')

print("STEP 859 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 859')
except Exception as e:
    print('FAIL - step 859' if isinstance(e, AssertionError) else f'ERROR - step 859: {e}')

print("STEP 860 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 860')
except Exception as e:
    print('FAIL - step 860' if isinstance(e, AssertionError) else f'ERROR - step 860: {e}')

print("STEP 861 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 861')
except Exception as e:
    print('FAIL - step 861' if isinstance(e, AssertionError) else f'ERROR - step 861: {e}')

print("STEP 862 - Check element label#None.['unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unselectable']")))
    print('PASS - step 862')
except Exception as e:
    print('FAIL - step 862' if isinstance(e, AssertionError) else f'ERROR - step 862: {e}')

print("STEP 863 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 863')
except Exception as e:
    print('FAIL - step 863' if isinstance(e, AssertionError) else f'ERROR - step 863: {e}')

print("STEP 864 - Check element div#None.['Rectangle-505']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['Rectangle-505']")))
    print('PASS - step 864')
except Exception as e:
    print('FAIL - step 864' if isinstance(e, AssertionError) else f'ERROR - step 864: {e}')

print("STEP 865 - Check element div#None.['wpr-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-row']")))
    print('PASS - step 865')
except Exception as e:
    print('FAIL - step 865' if isinstance(e, AssertionError) else f'ERROR - step 865: {e}')

print("STEP 866 - Check element li#None.['menu_content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['menu_content']")))
    print('PASS - step 866')
except Exception as e:
    print('FAIL - step 866' if isinstance(e, AssertionError) else f'ERROR - step 866: {e}')

print("STEP 867 - Check element label#None.['unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unselectable']")))
    print('PASS - step 867')
except Exception as e:
    print('FAIL - step 867' if isinstance(e, AssertionError) else f'ERROR - step 867: {e}')

print("STEP 868 - Check element div#None.['wpr-close-submenu-desk']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-close-submenu-desk']")))
    print('PASS - step 868')
except Exception as e:
    print('FAIL - step 868' if isinstance(e, AssertionError) else f'ERROR - step 868: {e}')

print("STEP 869 - Check element a#None.['close_icon_desk']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['close_icon_desk']")))
    print('PASS - step 869')
except Exception as e:
    print('FAIL - step 869' if isinstance(e, AssertionError) else f'ERROR - step 869: {e}')

print("STEP 870 - Check element div#None.['target_block_src_data']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['target_block_src_data']")))
    print('PASS - step 870')
except Exception as e:
    print('FAIL - step 870' if isinstance(e, AssertionError) else f'ERROR - step 870: {e}')

print("STEP 871 - Check element div#None.['autocomplete-wrapper', 'main']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['autocomplete-wrapper', 'main']")))
    print('PASS - step 871')
except Exception as e:
    print('FAIL - step 871' if isinstance(e, AssertionError) else f'ERROR - step 871: {e}')

print("STEP 872 - Check element div#ac-support-section.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "ac-support-section")))
    print('PASS - step 872')
except Exception as e:
    print('FAIL - step 872' if isinstance(e, AssertionError) else f'ERROR - step 872: {e}')

print("STEP 873 - Check element div#None.['title']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['title']")))
    print('PASS - step 873')
except Exception as e:
    print('FAIL - step 873' if isinstance(e, AssertionError) else f'ERROR - step 873: {e}')

print("STEP 874 - Check element a#None.['see-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['see-link']")))
    print('PASS - step 874')
except Exception as e:
    print('FAIL - step 874' if isinstance(e, AssertionError) else f'ERROR - step 874: {e}')

print("STEP 875 - Check element div#None.['autocomplete-header']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['autocomplete-header']")))
    print('PASS - step 875')
except Exception as e:
    print('FAIL - step 875' if isinstance(e, AssertionError) else f'ERROR - step 875: {e}')

print("STEP 876 - Check element nav#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "nav")))
    print('PASS - step 876')
except Exception as e:
    print('FAIL - step 876' if isinstance(e, AssertionError) else f'ERROR - step 876: {e}')

print("STEP 877 - Check element div#None.['autocomplete-header__body']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['autocomplete-header__body']")))
    print('PASS - step 877')
except Exception as e:
    print('FAIL - step 877' if isinstance(e, AssertionError) else f'ERROR - step 877: {e}')

print("STEP 878 - Check element div#None.['autocomplete-header__container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['autocomplete-header__container']")))
    print('PASS - step 878')
except Exception as e:
    print('FAIL - step 878' if isinstance(e, AssertionError) else f'ERROR - step 878: {e}')

print("STEP 879 - Check element div#None.['autocomplete-header__logo-holder']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['autocomplete-header__logo-holder']")))
    print('PASS - step 879')
except Exception as e:
    print('FAIL - step 879' if isinstance(e, AssertionError) else f'ERROR - step 879: {e}')

print("STEP 880 - Check element a#None.['wpr-main-logo-svg', 'unselectable', 'link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-main-logo-svg', 'unselectable', 'link_metrics']")))
    print('PASS - step 880')
except Exception as e:
    print('FAIL - step 880' if isinstance(e, AssertionError) else f'ERROR - step 880: {e}')

print("STEP 881 - Check element span#None.['wpr-skip-links']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-skip-links']")))
    print('PASS - step 881')
except Exception as e:
    print('FAIL - step 881' if isinstance(e, AssertionError) else f'ERROR - step 881: {e}')

print("STEP 882 - Check element a#None.['js-skip-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['js-skip-link']")))
    print('PASS - step 882')
except Exception as e:
    print('FAIL - step 882' if isinstance(e, AssertionError) else f'ERROR - step 882: {e}')

print("STEP 883 - Check element a#None.['js-skip-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['js-skip-link']")))
    print('PASS - step 883')
except Exception as e:
    print('FAIL - step 883' if isinstance(e, AssertionError) else f'ERROR - step 883: {e}')

print("STEP 884 - Check element div#None.['autocomplete-header__input-holder']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['autocomplete-header__input-holder']")))
    print('PASS - step 884')
except Exception as e:
    print('FAIL - step 884' if isinstance(e, AssertionError) else f'ERROR - step 884: {e}')

print("STEP 885 - Check element div#None.['input-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['input-wrapper']")))
    print('PASS - step 885')
except Exception as e:
    print('FAIL - step 885' if isinstance(e, AssertionError) else f'ERROR - step 885: {e}')

print("STEP 886 - Check element input#None.['search_trigger_onenter', 'search-bar', 'tab-search', 'link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['search_trigger_onenter', 'search-bar', 'tab-search', 'link_metrics']")))
    print('PASS - step 886')
except Exception as e:
    print('FAIL - step 886' if isinstance(e, AssertionError) else f'ERROR - step 886: {e}')

print("STEP 887 - Check element a#None.['wpr-backspace-icon', 'ac-input-icon']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-backspace-icon', 'ac-input-icon']")))
    print('PASS - step 887')
except Exception as e:
    print('FAIL - step 887' if isinstance(e, AssertionError) else f'ERROR - step 887: {e}')

print("STEP 888 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 888')
except Exception as e:
    print('FAIL - step 888' if isinstance(e, AssertionError) else f'ERROR - step 888: {e}')

print("STEP 889 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 889')
except Exception as e:
    print('FAIL - step 889' if isinstance(e, AssertionError) else f'ERROR - step 889: {e}')

print("STEP 890 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 890')
except Exception as e:
    print('FAIL - step 890' if isinstance(e, AssertionError) else f'ERROR - step 890: {e}')

print("STEP 891 - Check element a#None.['wpr-search-icon-logo', 'ac-input-icon', 'search_trigger', 'link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-search-icon-logo', 'ac-input-icon', 'search_trigger', 'link_metrics']")))
    print('PASS - step 891')
except Exception as e:
    print('FAIL - step 891' if isinstance(e, AssertionError) else f'ERROR - step 891: {e}')

print("STEP 892 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 892')
except Exception as e:
    print('FAIL - step 892' if isinstance(e, AssertionError) else f'ERROR - step 892: {e}')

print("STEP 893 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 893')
except Exception as e:
    print('FAIL - step 893' if isinstance(e, AssertionError) else f'ERROR - step 893: {e}')

print("STEP 894 - Check element a#None.['wpr-close-autocomplete', 'ac-input-icon']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-close-autocomplete', 'ac-input-icon']")))
    print('PASS - step 894')
except Exception as e:
    print('FAIL - step 894' if isinstance(e, AssertionError) else f'ERROR - step 894: {e}')

print("STEP 895 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 895')
except Exception as e:
    print('FAIL - step 895' if isinstance(e, AssertionError) else f'ERROR - step 895: {e}')

print("STEP 896 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 896')
except Exception as e:
    print('FAIL - step 896' if isinstance(e, AssertionError) else f'ERROR - step 896: {e}')

print("STEP 897 - Check element div#None.['wpr-autocomplete']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-autocomplete']")))
    print('PASS - step 897')
except Exception as e:
    print('FAIL - step 897' if isinstance(e, AssertionError) else f'ERROR - step 897: {e}')

print("STEP 898 - Check element div#None.['result']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['result']")))
    print('PASS - step 898')
except Exception as e:
    print('FAIL - step 898' if isinstance(e, AssertionError) else f'ERROR - step 898: {e}')

print("STEP 899 - Check element div#None.['container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['container']")))
    print('PASS - step 899')
except Exception as e:
    print('FAIL - step 899' if isinstance(e, AssertionError) else f'ERROR - step 899: {e}')

print("STEP 900 - Check element div#None.['result__error', 'message']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['result__error', 'message']")))
    print('PASS - step 900')
except Exception as e:
    print('FAIL - step 900' if isinstance(e, AssertionError) else f'ERROR - step 900: {e}')

print("STEP 901 - Check element div#None.['result__row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['result__row']")))
    print('PASS - step 901')
except Exception as e:
    print('FAIL - step 901' if isinstance(e, AssertionError) else f'ERROR - step 901: {e}')

print("STEP 902 - Check element div#None.['result__left']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['result__left']")))
    print('PASS - step 902')
except Exception as e:
    print('FAIL - step 902' if isinstance(e, AssertionError) else f'ERROR - step 902: {e}')

print("STEP 903 - Check element div#suggestion-section.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "suggestion-section")))
    print('PASS - step 903')
except Exception as e:
    print('FAIL - step 903' if isinstance(e, AssertionError) else f'ERROR - step 903: {e}')

print("STEP 904 - Check element div#see-all-results.['see-all']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "see-all-results")))
    print('PASS - step 904')
except Exception as e:
    print('FAIL - step 904' if isinstance(e, AssertionError) else f'ERROR - step 904: {e}')

print("STEP 905 - Check element div#None.['result__right', 'product']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['result__right', 'product']")))
    print('PASS - step 905')
except Exception as e:
    print('FAIL - step 905' if isinstance(e, AssertionError) else f'ERROR - step 905: {e}')

print("STEP 906 - Check element div#None.['ac-background']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-background']")))
    print('PASS - step 906')
except Exception as e:
    print('FAIL - step 906' if isinstance(e, AssertionError) else f'ERROR - step 906: {e}')

print("STEP 907 - Check element div#skiptobody.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "skiptobody")))
    print('PASS - step 907')
except Exception as e:
    print('FAIL - step 907' if isinstance(e, AssertionError) else f'ERROR - step 907: {e}')

print("STEP 908 - Check element div#None.['privacy-nb']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['privacy-nb']")))
    print('PASS - step 908')
except Exception as e:
    print('FAIL - step 908' if isinstance(e, AssertionError) else f'ERROR - step 908: {e}')

print("STEP 909 - Check element div#None.['privacy-notice-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['privacy-notice-wrapper']")))
    print('PASS - step 909')
except Exception as e:
    print('FAIL - step 909' if isinstance(e, AssertionError) else f'ERROR - step 909: {e}')

print("STEP 910 - Check element div#None.['desktop']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['desktop']")))
    print('PASS - step 910')
except Exception as e:
    print('FAIL - step 910' if isinstance(e, AssertionError) else f'ERROR - step 910: {e}')

print("STEP 911 - Check element p#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "p")))
    print('PASS - step 911')
except Exception as e:
    print('FAIL - step 911' if isinstance(e, AssertionError) else f'ERROR - step 911: {e}')

print("STEP 912 - Check element strong#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "strong")))
    print('PASS - step 912')
except Exception as e:
    print('FAIL - step 912' if isinstance(e, AssertionError) else f'ERROR - step 912: {e}')

print("STEP 913 - Check element a#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "a")))
    print('PASS - step 913')
except Exception as e:
    print('FAIL - step 913' if isinstance(e, AssertionError) else f'ERROR - step 913: {e}')

print("STEP 914 - Check element a#None.['c-button-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-button-link']")))
    print('PASS - step 914')
except Exception as e:
    print('FAIL - step 914' if isinstance(e, AssertionError) else f'ERROR - step 914: {e}')

print("STEP 915 - Check element div#None.['mobile']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['mobile']")))
    print('PASS - step 915')
except Exception as e:
    print('FAIL - step 915' if isinstance(e, AssertionError) else f'ERROR - step 915: {e}')

print("STEP 916 - Check element p#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "p")))
    print('PASS - step 916')
except Exception as e:
    print('FAIL - step 916' if isinstance(e, AssertionError) else f'ERROR - step 916: {e}')

print("STEP 917 - Check element strong#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "strong")))
    print('PASS - step 917')
except Exception as e:
    print('FAIL - step 917' if isinstance(e, AssertionError) else f'ERROR - step 917: {e}')

print("STEP 918 - Check element a#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "a")))
    print('PASS - step 918')
except Exception as e:
    print('FAIL - step 918' if isinstance(e, AssertionError) else f'ERROR - step 918: {e}')

print("STEP 919 - Check element a#None.['c-button-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-button-link']")))
    print('PASS - step 919')
except Exception as e:
    print('FAIL - step 919' if isinstance(e, AssertionError) else f'ERROR - step 919: {e}')

print("STEP 920 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 920')
except Exception as e:
    print('FAIL - step 920' if isinstance(e, AssertionError) else f'ERROR - step 920: {e}')

print("STEP 921 - Check element div#body.['body']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "body")))
    print('PASS - step 921')
except Exception as e:
    print('FAIL - step 921' if isinstance(e, AssertionError) else f'ERROR - step 921: {e}')

print("STEP 922 - Check element link#None.['standalone', 'loaded']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['standalone', 'loaded']")))
    print('PASS - step 922')
except Exception as e:
    print('FAIL - step 922' if isinstance(e, AssertionError) else f'ERROR - step 922: {e}')

print("STEP 923 - Check element link#None.['standalone', 'loaded']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['standalone', 'loaded']")))
    print('PASS - step 923')
except Exception as e:
    print('FAIL - step 923' if isinstance(e, AssertionError) else f'ERROR - step 923: {e}')

print("STEP 924 - Check element link#None.['standalone', 'loaded']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['standalone', 'loaded']")))
    print('PASS - step 924')
except Exception as e:
    print('FAIL - step 924' if isinstance(e, AssertionError) else f'ERROR - step 924: {e}')

print("STEP 925 - Check element link#None.['standalone', 'loaded']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['standalone', 'loaded']")))
    print('PASS - step 925')
except Exception as e:
    print('FAIL - step 925' if isinstance(e, AssertionError) else f'ERROR - step 925: {e}')

print("STEP 926 - Check element link#None.['standalone', 'loaded']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['standalone', 'loaded']")))
    print('PASS - step 926')
except Exception as e:
    print('FAIL - step 926' if isinstance(e, AssertionError) else f'ERROR - step 926: {e}')

print("STEP 927 - Check element link#None.['standalone', 'loaded']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['standalone', 'loaded']")))
    print('PASS - step 927')
except Exception as e:
    print('FAIL - step 927' if isinstance(e, AssertionError) else f'ERROR - step 927: {e}')

print("STEP 928 - Check element link#None.['standalone', 'loaded']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['standalone', 'loaded']")))
    print('PASS - step 928')
except Exception as e:
    print('FAIL - step 928' if isinstance(e, AssertionError) else f'ERROR - step 928: {e}')

print("STEP 929 - Check element link#None.['standalone', 'loaded']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['standalone', 'loaded']")))
    print('PASS - step 929')
except Exception as e:
    print('FAIL - step 929' if isinstance(e, AssertionError) else f'ERROR - step 929: {e}')

print("STEP 930 - Check element link#None.['standalone', 'loaded']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['standalone', 'loaded']")))
    print('PASS - step 930')
except Exception as e:
    print('FAIL - step 930' if isinstance(e, AssertionError) else f'ERROR - step 930: {e}')

print("STEP 931 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 931')
except Exception as e:
    print('FAIL - step 931' if isinstance(e, AssertionError) else f'ERROR - step 931: {e}')

print("STEP 932 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 932')
except Exception as e:
    print('FAIL - step 932' if isinstance(e, AssertionError) else f'ERROR - step 932: {e}')

print("STEP 933 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 933')
except Exception as e:
    print('FAIL - step 933' if isinstance(e, AssertionError) else f'ERROR - step 933: {e}')

print("STEP 934 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 934')
except Exception as e:
    print('FAIL - step 934' if isinstance(e, AssertionError) else f'ERROR - step 934: {e}')

print("STEP 935 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 935')
except Exception as e:
    print('FAIL - step 935' if isinstance(e, AssertionError) else f'ERROR - step 935: {e}')

print("STEP 936 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 936')
except Exception as e:
    print('FAIL - step 936' if isinstance(e, AssertionError) else f'ERROR - step 936: {e}')

print("STEP 937 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 937')
except Exception as e:
    print('FAIL - step 937' if isinstance(e, AssertionError) else f'ERROR - step 937: {e}')

print("STEP 938 - Check element div#None.['root', 'responsivegrid']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['root', 'responsivegrid']")))
    print('PASS - step 938')
except Exception as e:
    print('FAIL - step 938' if isinstance(e, AssertionError) else f'ERROR - step 938: {e}')

print("STEP 939 - Check element div#None.['aem-Grid', 'aem-Grid--12', 'aem-Grid--default--12']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem-Grid', 'aem-Grid--12', 'aem-Grid--default--12']")))
    print('PASS - step 939')
except Exception as e:
    print('FAIL - step 939' if isinstance(e, AssertionError) else f'ERROR - step 939: {e}')

print("STEP 940 - Check element div#None.['ghost', 'aem-GridColumn', 'aem-GridColumn--default--12']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ghost', 'aem-GridColumn', 'aem-GridColumn--default--12']")))
    print('PASS - step 940')
except Exception as e:
    print('FAIL - step 940' if isinstance(e, AssertionError) else f'ERROR - step 940: {e}')

print("STEP 941 - Check element div#None.['ghost', 'aem-GridColumn', 'aem-GridColumn--default--12']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ghost', 'aem-GridColumn', 'aem-GridColumn--default--12']")))
    print('PASS - step 941')
except Exception as e:
    print('FAIL - step 941' if isinstance(e, AssertionError) else f'ERROR - step 941: {e}')

print("STEP 942 - Check element div#None.['viewports', 'aem-GridColumn', 'aem-GridColumn--default--12']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['viewports', 'aem-GridColumn', 'aem-GridColumn--default--12']")))
    print('PASS - step 942')
except Exception as e:
    print('FAIL - step 942' if isinstance(e, AssertionError) else f'ERROR - step 942: {e}')

print("STEP 943 - Check element div#None.['c-viewports']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-viewports']")))
    print('PASS - step 943')
except Exception as e:
    print('FAIL - step 943' if isinstance(e, AssertionError) else f'ERROR - step 943: {e}')

print("STEP 944 - Check element div#None.['c-viewports__desktop-content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-viewports__desktop-content']")))
    print('PASS - step 944')
except Exception as e:
    print('FAIL - step 944' if isinstance(e, AssertionError) else f'ERROR - step 944: {e}')

print("STEP 945 - Check element div#None.['genericcarousel']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['genericcarousel']")))
    print('PASS - step 945')
except Exception as e:
    print('FAIL - step 945' if isinstance(e, AssertionError) else f'ERROR - step 945: {e}')

print("STEP 946 - Check element hp-generic-carousel-slider#id95b0ab47c3e9370b98aed0b1d2416b9e5aa0a43a1531bb64202d02db95f19c5b.['js-hp-component', 'c-generic-carousel-slider', 'no-top-spacing-only', 'js-hp-component-initialized']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id95b0ab47c3e9370b98aed0b1d2416b9e5aa0a43a1531bb64202d02db95f19c5b")))
    print('PASS - step 946')
except Exception as e:
    print('FAIL - step 946' if isinstance(e, AssertionError) else f'ERROR - step 946: {e}')

print("STEP 947 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 947')
except Exception as e:
    print('FAIL - step 947' if isinstance(e, AssertionError) else f'ERROR - step 947: {e}')

print("STEP 948 - Check element div#None.['c-generic-carousel-slider__slides', 'swiper-container', 'js-component-extension', 'arrows-dark', 'swiper-dotted', 'swiper-container-initialized', 'swiper-container-horizontal']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-generic-carousel-slider__slides', 'swiper-container', 'js-component-extension', 'arrows-dark', 'swiper-dotted', 'swiper-container-initialized', 'swiper-container-horizontal']")))
    print('PASS - step 948')
except Exception as e:
    print('FAIL - step 948' if isinstance(e, AssertionError) else f'ERROR - step 948: {e}')

print("STEP 949 - Check element button#None.['swiper-arrow', 'c-icon', 'swiper-button-prev']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['swiper-arrow', 'c-icon', 'swiper-button-prev']")))
    print('PASS - step 949')
except Exception as e:
    print('FAIL - step 949' if isinstance(e, AssertionError) else f'ERROR - step 949: {e}')

print("STEP 950 - Check element span#None.['c-icon-regular-state']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-icon-regular-state']")))
    print('PASS - step 950')
except Exception as e:
    print('FAIL - step 950' if isinstance(e, AssertionError) else f'ERROR - step 950: {e}')

print("STEP 951 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 951')
except Exception as e:
    print('FAIL - step 951' if isinstance(e, AssertionError) else f'ERROR - step 951: {e}')

print("STEP 952 - Check element use#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "use")))
    print('PASS - step 952')
except Exception as e:
    print('FAIL - step 952' if isinstance(e, AssertionError) else f'ERROR - step 952: {e}')

print("STEP 953 - Check element span#None.['c-icon-hover-state']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-icon-hover-state']")))
    print('PASS - step 953')
except Exception as e:
    print('FAIL - step 953' if isinstance(e, AssertionError) else f'ERROR - step 953: {e}')

print("STEP 954 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 954')
except Exception as e:
    print('FAIL - step 954' if isinstance(e, AssertionError) else f'ERROR - step 954: {e}')

print("STEP 955 - Check element use#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "use")))
    print('PASS - step 955')
except Exception as e:
    print('FAIL - step 955' if isinstance(e, AssertionError) else f'ERROR - step 955: {e}')

print("STEP 956 - Check element div#None.['swiper-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['swiper-wrapper']")))
    print('PASS - step 956')
except Exception as e:
    print('FAIL - step 956' if isinstance(e, AssertionError) else f'ERROR - step 956: {e}')

print("STEP 957 - Check element div#None.['c-generic-carousel-slider__slide', 'swiper-slide', 'swiper-slide-duplicate', 'swiper-slide-prev']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-generic-carousel-slider__slide', 'swiper-slide', 'swiper-slide-duplicate', 'swiper-slide-prev']")))
    print('PASS - step 957')
except Exception as e:
    print('FAIL - step 957' if isinstance(e, AssertionError) else f'ERROR - step 957: {e}')

print("STEP 958 - Check element hp-generic-card#None.['c-generic-card']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-generic-card']")))
    print('PASS - step 958')
except Exception as e:
    print('FAIL - step 958' if isinstance(e, AssertionError) else f'ERROR - step 958: {e}')

print("STEP 959 - Check element div#None.['c-generic-card__image', 'c-video-container--container-fit']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-generic-card__image', 'c-video-container--container-fit']")))
    print('PASS - step 959')
except Exception as e:
    print('FAIL - step 959' if isinstance(e, AssertionError) else f'ERROR - step 959: {e}')

print("STEP 960 - Check element div#None.['cib-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['cib-wrapper']")))
    print('PASS - step 960')
except Exception as e:
    print('FAIL - step 960' if isinstance(e, AssertionError) else f'ERROR - step 960: {e}')

print("STEP 961 - Check element div#None.['customInfoBanner']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['customInfoBanner']")))
    print('PASS - step 961')
except Exception as e:
    print('FAIL - step 961' if isinstance(e, AssertionError) else f'ERROR - step 961: {e}')

print("STEP 962 - Check element hp-custom-info-banner-v2#None.['js-hp-component', 'c-custom-info-banner-v2', 'id6b762839ecf3cc8ab4aed7345a432c1376f5a31a2e206e361fe8a6b672c538ca', 'media-position-top', 'title-on-side', 'inside-generic-carousel', 'js-hp-component-initialized']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['js-hp-component', 'c-custom-info-banner-v2', 'id6b762839ecf3cc8ab4aed7345a432c1376f5a31a2e206e361fe8a6b672c538ca', 'media-position-top', 'title-on-side', 'inside-generic-carousel', 'js-hp-component-initialized']")))
    print('PASS - step 962')
except Exception as e:
    print('FAIL - step 962' if isinstance(e, AssertionError) else f'ERROR - step 962: {e}')

print("STEP 963 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 963')
except Exception as e:
    print('FAIL - step 963' if isinstance(e, AssertionError) else f'ERROR - step 963: {e}')

print("STEP 964 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 964')
except Exception as e:
    print('FAIL - step 964' if isinstance(e, AssertionError) else f'ERROR - step 964: {e}')

print("STEP 965 - Check element div#None.['c-custom-info-banner-v2__media', 'c-custom-info-banner-v2__media--cloned']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__media', 'c-custom-info-banner-v2__media--cloned']")))
    print('PASS - step 965')
except Exception as e:
    print('FAIL - step 965' if isinstance(e, AssertionError) else f'ERROR - step 965: {e}')

print("STEP 966 - Check element div#None.['c-image-v2', 'image-v2-9b75dd9a-22']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2', 'image-v2-9b75dd9a-22']")))
    print('PASS - step 966')
except Exception as e:
    print('FAIL - step 966' if isinstance(e, AssertionError) else f'ERROR - step 966: {e}')

print("STEP 967 - Check element div#None.['c-image-v2__container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2__container']")))
    print('PASS - step 967')
except Exception as e:
    print('FAIL - step 967' if isinstance(e, AssertionError) else f'ERROR - step 967: {e}')

print("STEP 968 - Check element picture#None.['c-image-v2__wrp']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2__wrp']")))
    print('PASS - step 968')
except Exception as e:
    print('FAIL - step 968' if isinstance(e, AssertionError) else f'ERROR - step 968: {e}')

print("STEP 969 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 969')
except Exception as e:
    print('FAIL - step 969' if isinstance(e, AssertionError) else f'ERROR - step 969: {e}')

print("STEP 970 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 970')
except Exception as e:
    print('FAIL - step 970' if isinstance(e, AssertionError) else f'ERROR - step 970: {e}')

print("STEP 971 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 971')
except Exception as e:
    print('FAIL - step 971' if isinstance(e, AssertionError) else f'ERROR - step 971: {e}')

print("STEP 972 - Check element img#None.['c-image-v2__img']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2__img']")))
    print('PASS - step 972')
except Exception as e:
    print('FAIL - step 972' if isinstance(e, AssertionError) else f'ERROR - step 972: {e}')

print("STEP 973 - Check element div#None.['c-custom-info-banner-v2__header']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header']")))
    print('PASS - step 973')
except Exception as e:
    print('FAIL - step 973' if isinstance(e, AssertionError) else f'ERROR - step 973: {e}')

print("STEP 974 - Check element div#None.['c-custom-info-banner-v2__header--title-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--title-wrapper']")))
    print('PASS - step 974')
except Exception as e:
    print('FAIL - step 974' if isinstance(e, AssertionError) else f'ERROR - step 974: {e}')

print("STEP 975 - Check element div#None.['container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['container']")))
    print('PASS - step 975')
except Exception as e:
    print('FAIL - step 975' if isinstance(e, AssertionError) else f'ERROR - step 975: {e}')

print("STEP 976 - Check element div#None.['c-custom-info-banner-v2__header--title', 'xxl', 'reset-list', 'no-default-list-spacings', 'extra-indented']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--title', 'xxl', 'reset-list', 'no-default-list-spacings', 'extra-indented']")))
    print('PASS - step 976')
except Exception as e:
    print('FAIL - step 976' if isinstance(e, AssertionError) else f'ERROR - step 976: {e}')

print("STEP 977 - Check element div#None.['c-custom-info-banner-v2__header--subtitle-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--subtitle-wrapper']")))
    print('PASS - step 977')
except Exception as e:
    print('FAIL - step 977' if isinstance(e, AssertionError) else f'ERROR - step 977: {e}')

print("STEP 978 - Check element div#None.['container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['container']")))
    print('PASS - step 978')
except Exception as e:
    print('FAIL - step 978' if isinstance(e, AssertionError) else f'ERROR - step 978: {e}')

print("STEP 979 - Check element div#None.['c-custom-info-banner-v2__header--subtitle', 'h2', 'reset-list', 'no-default-list-spacings', 'extra-indented']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--subtitle', 'h2', 'reset-list', 'no-default-list-spacings', 'extra-indented']")))
    print('PASS - step 979')
except Exception as e:
    print('FAIL - step 979' if isinstance(e, AssertionError) else f'ERROR - step 979: {e}')

print("STEP 980 - Check element div#None.['c-custom-info-banner-v2__container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__container']")))
    print('PASS - step 980')
except Exception as e:
    print('FAIL - step 980' if isinstance(e, AssertionError) else f'ERROR - step 980: {e}')

print("STEP 981 - Check element div#None.['c-custom-info-banner-v2__content', 'container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__content', 'container']")))
    print('PASS - step 981')
except Exception as e:
    print('FAIL - step 981' if isinstance(e, AssertionError) else f'ERROR - step 981: {e}')

print("STEP 982 - Check element div#None.['c-custom-info-banner-v2__content--inner']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__content--inner']")))
    print('PASS - step 982')
except Exception as e:
    print('FAIL - step 982' if isinstance(e, AssertionError) else f'ERROR - step 982: {e}')

print("STEP 983 - Check element div#None.['c-custom-info-banner-v2__header--title-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--title-wrapper']")))
    print('PASS - step 983')
except Exception as e:
    print('FAIL - step 983' if isinstance(e, AssertionError) else f'ERROR - step 983: {e}')

print("STEP 984 - Check element div#None.['c-custom-info-banner-v2__header--title', 'xxl', 'reset-list', 'no-default-list-spacings', 'extra-indented']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--title', 'xxl', 'reset-list', 'no-default-list-spacings', 'extra-indented']")))
    print('PASS - step 984')
except Exception as e:
    print('FAIL - step 984' if isinstance(e, AssertionError) else f'ERROR - step 984: {e}')

print("STEP 985 - Check element div#None.['c-custom-info-banner-v2__header--subtitle-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--subtitle-wrapper']")))
    print('PASS - step 985')
except Exception as e:
    print('FAIL - step 985' if isinstance(e, AssertionError) else f'ERROR - step 985: {e}')

print("STEP 986 - Check element div#None.['c-custom-info-banner-v2__header--subtitle', 'h2', 'reset-list', 'no-default-list-spacings', 'extra-indented']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--subtitle', 'h2', 'reset-list', 'no-default-list-spacings', 'extra-indented']")))
    print('PASS - step 986')
except Exception as e:
    print('FAIL - step 986' if isinstance(e, AssertionError) else f'ERROR - step 986: {e}')

print("STEP 987 - Check element div#None.['c-custom-info-banner-v2__content--components-list']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__content--components-list']")))
    print('PASS - step 987')
except Exception as e:
    print('FAIL - step 987' if isinstance(e, AssertionError) else f'ERROR - step 987: {e}')

print("STEP 988 - Check element div#None.['ctadropdownbutton']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ctadropdownbutton']")))
    print('PASS - step 988')
except Exception as e:
    print('FAIL - step 988' if isinstance(e, AssertionError) else f'ERROR - step 988: {e}')

print("STEP 989 - Check element div#None.['cta-dropdown-button', 'text-left', 'inline-container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['cta-dropdown-button', 'text-left', 'inline-container']")))
    print('PASS - step 989')
except Exception as e:
    print('FAIL - step 989' if isinstance(e, AssertionError) else f'ERROR - step 989: {e}')

print("STEP 990 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 990')
except Exception as e:
    print('FAIL - step 990' if isinstance(e, AssertionError) else f'ERROR - step 990: {e}')

print("STEP 991 - Check element a#id28b4a774767b71f2fcb4fd11c6e156a175cb93cd3713174afe9fd1fcfef7176b.['c-button', 'append-misc-url-params']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id28b4a774767b71f2fcb4fd11c6e156a175cb93cd3713174afe9fd1fcfef7176b")))
    print('PASS - step 991')
except Exception as e:
    print('FAIL - step 991' if isinstance(e, AssertionError) else f'ERROR - step 991: {e}')

print("STEP 992 - Check element span#None.['c-button__text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-button__text']")))
    print('PASS - step 992')
except Exception as e:
    print('FAIL - step 992' if isinstance(e, AssertionError) else f'ERROR - step 992: {e}')

print("STEP 993 - Check element p#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "p")))
    print('PASS - step 993')
except Exception as e:
    print('FAIL - step 993' if isinstance(e, AssertionError) else f'ERROR - step 993: {e}')

print("STEP 994 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 994')
except Exception as e:
    print('FAIL - step 994' if isinstance(e, AssertionError) else f'ERROR - step 994: {e}')

print("STEP 995 - Check element a#id104d9403578a72b173f5e594d27adbc38c38d7d0459edebbfd8808949da2ebfb.['c-button', 'append-misc-url-params']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id104d9403578a72b173f5e594d27adbc38c38d7d0459edebbfd8808949da2ebfb")))
    print('PASS - step 995')
except Exception as e:
    print('FAIL - step 995' if isinstance(e, AssertionError) else f'ERROR - step 995: {e}')

print("STEP 996 - Check element span#None.['c-button__text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-button__text']")))
    print('PASS - step 996')
except Exception as e:
    print('FAIL - step 996' if isinstance(e, AssertionError) else f'ERROR - step 996: {e}')

print("STEP 997 - Check element p#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "p")))
    print('PASS - step 997')
except Exception as e:
    print('FAIL - step 997' if isinstance(e, AssertionError) else f'ERROR - step 997: {e}')

print("STEP 998 - Check element div#None.['c-custom-info-banner-v2__media']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__media']")))
    print('PASS - step 998')
except Exception as e:
    print('FAIL - step 998' if isinstance(e, AssertionError) else f'ERROR - step 998: {e}')

print("STEP 999 - Check element div#None.['c-image-v2', 'image-v2-9ba8a960-24']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2', 'image-v2-9ba8a960-24']")))
    print('PASS - step 999')
except Exception as e:
    print('FAIL - step 999' if isinstance(e, AssertionError) else f'ERROR - step 999: {e}')

print("STEP 1000 - Check element div#None.['c-image-v2__container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2__container']")))
    print('PASS - step 1000')
except Exception as e:
    print('FAIL - step 1000' if isinstance(e, AssertionError) else f'ERROR - step 1000: {e}')

print("STEP 1001 - Check element picture#None.['c-image-v2__wrp']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2__wrp']")))
    print('PASS - step 1001')
except Exception as e:
    print('FAIL - step 1001' if isinstance(e, AssertionError) else f'ERROR - step 1001: {e}')

print("STEP 1002 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1002')
except Exception as e:
    print('FAIL - step 1002' if isinstance(e, AssertionError) else f'ERROR - step 1002: {e}')

print("STEP 1003 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1003')
except Exception as e:
    print('FAIL - step 1003' if isinstance(e, AssertionError) else f'ERROR - step 1003: {e}')

print("STEP 1004 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1004')
except Exception as e:
    print('FAIL - step 1004' if isinstance(e, AssertionError) else f'ERROR - step 1004: {e}')

print("STEP 1005 - Check element img#None.['c-image-v2__img']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2__img']")))
    print('PASS - step 1005')
except Exception as e:
    print('FAIL - step 1005' if isinstance(e, AssertionError) else f'ERROR - step 1005: {e}')

print("STEP 1006 - Check element script#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "script")))
    print('PASS - step 1006')
except Exception as e:
    print('FAIL - step 1006' if isinstance(e, AssertionError) else f'ERROR - step 1006: {e}')

print("STEP 1007 - Check element div#None.['c-generic-carousel-slider__slide', 'swiper-slide', 'active-slide']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-generic-carousel-slider__slide', 'swiper-slide', 'active-slide']")))
    print('PASS - step 1007')
except Exception as e:
    print('FAIL - step 1007' if isinstance(e, AssertionError) else f'ERROR - step 1007: {e}')

print("STEP 1008 - Check element hp-generic-card#None.['c-generic-card']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-generic-card']")))
    print('PASS - step 1008')
except Exception as e:
    print('FAIL - step 1008' if isinstance(e, AssertionError) else f'ERROR - step 1008: {e}')

print("STEP 1009 - Check element div#None.['c-generic-card__image', 'c-video-container--container-fit']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-generic-card__image', 'c-video-container--container-fit']")))
    print('PASS - step 1009')
except Exception as e:
    print('FAIL - step 1009' if isinstance(e, AssertionError) else f'ERROR - step 1009: {e}')

print("STEP 1010 - Check element div#None.['cib-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['cib-wrapper']")))
    print('PASS - step 1010')
except Exception as e:
    print('FAIL - step 1010' if isinstance(e, AssertionError) else f'ERROR - step 1010: {e}')

print("STEP 1011 - Check element div#None.['customInfoBanner']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['customInfoBanner']")))
    print('PASS - step 1011')
except Exception as e:
    print('FAIL - step 1011' if isinstance(e, AssertionError) else f'ERROR - step 1011: {e}')

print("STEP 1012 - Check element hp-custom-info-banner-v3#None.['js-hp-component', 'c-custom-info-banner-v3', 'check-footnotes-visibility', 'id0a4ceb7d60804a83fa38ee0f5df84d6aaeacecfd1280ff0f5b540b05e18def95', 'no-tablet-version', 'no-mobile-version', 'js-hp-component-initialized']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['js-hp-component', 'c-custom-info-banner-v3', 'check-footnotes-visibility', 'id0a4ceb7d60804a83fa38ee0f5df84d6aaeacecfd1280ff0f5b540b05e18def95', 'no-tablet-version', 'no-mobile-version', 'js-hp-component-initialized']")))
    print('PASS - step 1012')
except Exception as e:
    print('FAIL - step 1012' if isinstance(e, AssertionError) else f'ERROR - step 1012: {e}')

print("STEP 1013 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1013')
except Exception as e:
    print('FAIL - step 1013' if isinstance(e, AssertionError) else f'ERROR - step 1013: {e}')

print("STEP 1014 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 1014')
except Exception as e:
    print('FAIL - step 1014' if isinstance(e, AssertionError) else f'ERROR - step 1014: {e}')

print("STEP 1015 - Check element div#None.['general']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['general']")))
    print('PASS - step 1015')
except Exception as e:
    print('FAIL - step 1015' if isinstance(e, AssertionError) else f'ERROR - step 1015: {e}')

print("STEP 1016 - Check element hp-custom-info-banner-v2#None.['js-hp-component', 'c-custom-info-banner-v2', 'id4c4dac59d5aac38c9e0d23fc6e6c78f857a2c17b5e83e8f2a32e6c496a88b2c6', 'media-position-top', 'title-on-side', 'js-hp-component-initialized', 'inside-v3', 'inside-generic-carousel']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['js-hp-component', 'c-custom-info-banner-v2', 'id4c4dac59d5aac38c9e0d23fc6e6c78f857a2c17b5e83e8f2a32e6c496a88b2c6', 'media-position-top', 'title-on-side', 'js-hp-component-initialized', 'inside-v3', 'inside-generic-carousel']")))
    print('PASS - step 1016')
except Exception as e:
    print('FAIL - step 1016' if isinstance(e, AssertionError) else f'ERROR - step 1016: {e}')

print("STEP 1017 - Check element div#None.['c-custom-info-banner-v2__media', 'c-custom-info-banner-v2__media--cloned']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__media', 'c-custom-info-banner-v2__media--cloned']")))
    print('PASS - step 1017')
except Exception as e:
    print('FAIL - step 1017' if isinstance(e, AssertionError) else f'ERROR - step 1017: {e}')

print("STEP 1018 - Check element div#None.['c-image-v2', 'image-v2-898c8e3a-2']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2', 'image-v2-898c8e3a-2']")))
    print('PASS - step 1018')
except Exception as e:
    print('FAIL - step 1018' if isinstance(e, AssertionError) else f'ERROR - step 1018: {e}')

print("STEP 1019 - Check element div#None.['c-image-v2__container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2__container']")))
    print('PASS - step 1019')
except Exception as e:
    print('FAIL - step 1019' if isinstance(e, AssertionError) else f'ERROR - step 1019: {e}')

print("STEP 1020 - Check element picture#None.['c-image-v2__wrp']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2__wrp']")))
    print('PASS - step 1020')
except Exception as e:
    print('FAIL - step 1020' if isinstance(e, AssertionError) else f'ERROR - step 1020: {e}')

print("STEP 1021 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1021')
except Exception as e:
    print('FAIL - step 1021' if isinstance(e, AssertionError) else f'ERROR - step 1021: {e}')

print("STEP 1022 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1022')
except Exception as e:
    print('FAIL - step 1022' if isinstance(e, AssertionError) else f'ERROR - step 1022: {e}')

print("STEP 1023 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1023')
except Exception as e:
    print('FAIL - step 1023' if isinstance(e, AssertionError) else f'ERROR - step 1023: {e}')

print("STEP 1024 - Check element img#None.['c-image-v2__img']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2__img']")))
    print('PASS - step 1024')
except Exception as e:
    print('FAIL - step 1024' if isinstance(e, AssertionError) else f'ERROR - step 1024: {e}')

print("STEP 1025 - Check element div#None.['c-custom-info-banner-v2__header']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header']")))
    print('PASS - step 1025')
except Exception as e:
    print('FAIL - step 1025' if isinstance(e, AssertionError) else f'ERROR - step 1025: {e}')

print("STEP 1026 - Check element div#None.['c-custom-info-banner-v2__header--title-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--title-wrapper']")))
    print('PASS - step 1026')
except Exception as e:
    print('FAIL - step 1026' if isinstance(e, AssertionError) else f'ERROR - step 1026: {e}')

print("STEP 1027 - Check element div#None.['container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['container']")))
    print('PASS - step 1027')
except Exception as e:
    print('FAIL - step 1027' if isinstance(e, AssertionError) else f'ERROR - step 1027: {e}')

print("STEP 1028 - Check element h2#None.['c-custom-info-banner-v2__header--title', 'xl', 'reset-list', 'no-default-list-spacings', 'extra-indented']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--title', 'xl', 'reset-list', 'no-default-list-spacings', 'extra-indented']")))
    print('PASS - step 1028')
except Exception as e:
    print('FAIL - step 1028' if isinstance(e, AssertionError) else f'ERROR - step 1028: {e}')

print("STEP 1029 - Check element br#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "br")))
    print('PASS - step 1029')
except Exception as e:
    print('FAIL - step 1029' if isinstance(e, AssertionError) else f'ERROR - step 1029: {e}')

print("STEP 1030 - Check element div#None.['c-custom-info-banner-v2__header--subtitle-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--subtitle-wrapper']")))
    print('PASS - step 1030')
except Exception as e:
    print('FAIL - step 1030' if isinstance(e, AssertionError) else f'ERROR - step 1030: {e}')

print("STEP 1031 - Check element div#None.['container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['container']")))
    print('PASS - step 1031')
except Exception as e:
    print('FAIL - step 1031' if isinstance(e, AssertionError) else f'ERROR - step 1031: {e}')

print("STEP 1032 - Check element h3#None.['c-custom-info-banner-v2__header--subtitle', 'h2', 'reset-list', 'no-default-list-spacings', 'extra-indented']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--subtitle', 'h2', 'reset-list', 'no-default-list-spacings', 'extra-indented']")))
    print('PASS - step 1032')
except Exception as e:
    print('FAIL - step 1032' if isinstance(e, AssertionError) else f'ERROR - step 1032: {e}')

print("STEP 1033 - Check element div#None.['c-custom-info-banner-v2__container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__container']")))
    print('PASS - step 1033')
except Exception as e:
    print('FAIL - step 1033' if isinstance(e, AssertionError) else f'ERROR - step 1033: {e}')

print("STEP 1034 - Check element div#None.['c-custom-info-banner-v2__content', 'container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__content', 'container']")))
    print('PASS - step 1034')
except Exception as e:
    print('FAIL - step 1034' if isinstance(e, AssertionError) else f'ERROR - step 1034: {e}')

print("STEP 1035 - Check element div#None.['c-custom-info-banner-v2__content--inner']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__content--inner']")))
    print('PASS - step 1035')
except Exception as e:
    print('FAIL - step 1035' if isinstance(e, AssertionError) else f'ERROR - step 1035: {e}')

print("STEP 1036 - Check element div#None.['c-custom-info-banner-v2__header--title-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--title-wrapper']")))
    print('PASS - step 1036')
except Exception as e:
    print('FAIL - step 1036' if isinstance(e, AssertionError) else f'ERROR - step 1036: {e}')

print("STEP 1037 - Check element div#None.['c-custom-info-banner-v2__header--title', 'xl', 'reset-list', 'no-default-list-spacings', 'extra-indented']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--title', 'xl', 'reset-list', 'no-default-list-spacings', 'extra-indented']")))
    print('PASS - step 1037')
except Exception as e:
    print('FAIL - step 1037' if isinstance(e, AssertionError) else f'ERROR - step 1037: {e}')

print("STEP 1038 - Check element br#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "br")))
    print('PASS - step 1038')
except Exception as e:
    print('FAIL - step 1038' if isinstance(e, AssertionError) else f'ERROR - step 1038: {e}')

print("STEP 1039 - Check element div#None.['c-custom-info-banner-v2__header--subtitle-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--subtitle-wrapper']")))
    print('PASS - step 1039')
except Exception as e:
    print('FAIL - step 1039' if isinstance(e, AssertionError) else f'ERROR - step 1039: {e}')

print("STEP 1040 - Check element div#None.['c-custom-info-banner-v2__header--subtitle', 'h2', 'reset-list', 'no-default-list-spacings', 'extra-indented']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--subtitle', 'h2', 'reset-list', 'no-default-list-spacings', 'extra-indented']")))
    print('PASS - step 1040')
except Exception as e:
    print('FAIL - step 1040' if isinstance(e, AssertionError) else f'ERROR - step 1040: {e}')

print("STEP 1041 - Check element div#None.['c-custom-info-banner-v2__content--components-list']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__content--components-list']")))
    print('PASS - step 1041')
except Exception as e:
    print('FAIL - step 1041' if isinstance(e, AssertionError) else f'ERROR - step 1041: {e}')

print("STEP 1042 - Check element div#None.['ctaGroup']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ctaGroup']")))
    print('PASS - step 1042')
except Exception as e:
    print('FAIL - step 1042' if isinstance(e, AssertionError) else f'ERROR - step 1042: {e}')

print("STEP 1043 - Check element div#None.['cta-group', 'inline-container', 'idc84249b717e379e0aea39fd256e190ca024e5a431b62e7932af4a66bffd3d69d']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['cta-group', 'inline-container', 'idc84249b717e379e0aea39fd256e190ca024e5a431b62e7932af4a66bffd3d69d']")))
    print('PASS - step 1043')
except Exception as e:
    print('FAIL - step 1043' if isinstance(e, AssertionError) else f'ERROR - step 1043: {e}')

print("STEP 1044 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1044')
except Exception as e:
    print('FAIL - step 1044' if isinstance(e, AssertionError) else f'ERROR - step 1044: {e}')

print("STEP 1045 - Check element div#None.['ctaButton']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ctaButton']")))
    print('PASS - step 1045')
except Exception as e:
    print('FAIL - step 1045' if isinstance(e, AssertionError) else f'ERROR - step 1045: {e}')

print("STEP 1046 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1046')
except Exception as e:
    print('FAIL - step 1046' if isinstance(e, AssertionError) else f'ERROR - step 1046: {e}')

print("STEP 1047 - Check element a#id4137bd87734b2616b01604876f8cf4e8773254c9d91412adf765561c41acbb9c.['c-button', 'append-misc-url-params']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id4137bd87734b2616b01604876f8cf4e8773254c9d91412adf765561c41acbb9c")))
    print('PASS - step 1047')
except Exception as e:
    print('FAIL - step 1047' if isinstance(e, AssertionError) else f'ERROR - step 1047: {e}')

print("STEP 1048 - Check element span#None.['c-button__text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-button__text']")))
    print('PASS - step 1048')
except Exception as e:
    print('FAIL - step 1048' if isinstance(e, AssertionError) else f'ERROR - step 1048: {e}')

print("STEP 1049 - Check element p#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "p")))
    print('PASS - step 1049')
except Exception as e:
    print('FAIL - step 1049' if isinstance(e, AssertionError) else f'ERROR - step 1049: {e}')

print("STEP 1050 - Check element div#None.['ctaButton']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ctaButton']")))
    print('PASS - step 1050')
except Exception as e:
    print('FAIL - step 1050' if isinstance(e, AssertionError) else f'ERROR - step 1050: {e}')

print("STEP 1051 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1051')
except Exception as e:
    print('FAIL - step 1051' if isinstance(e, AssertionError) else f'ERROR - step 1051: {e}')

print("STEP 1052 - Check element a#idaec6c56faa79d308dbd3ccd6193f7c575139b6894959b1e9fd7d5346f1eb92fd.['c-button-outline', 'append-misc-url-params']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "idaec6c56faa79d308dbd3ccd6193f7c575139b6894959b1e9fd7d5346f1eb92fd")))
    print('PASS - step 1052')
except Exception as e:
    print('FAIL - step 1052' if isinstance(e, AssertionError) else f'ERROR - step 1052: {e}')

print("STEP 1053 - Check element span#None.['c-button__text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-button__text']")))
    print('PASS - step 1053')
except Exception as e:
    print('FAIL - step 1053' if isinstance(e, AssertionError) else f'ERROR - step 1053: {e}')

print("STEP 1054 - Check element p#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "p")))
    print('PASS - step 1054')
except Exception as e:
    print('FAIL - step 1054' if isinstance(e, AssertionError) else f'ERROR - step 1054: {e}')

print("STEP 1055 - Check element div#None.['c-custom-info-banner-v2__media']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__media']")))
    print('PASS - step 1055')
except Exception as e:
    print('FAIL - step 1055' if isinstance(e, AssertionError) else f'ERROR - step 1055: {e}')

print("STEP 1056 - Check element div#None.['c-image-v2', 'image-v2-5bb9b725-4']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2', 'image-v2-5bb9b725-4']")))
    print('PASS - step 1056')
except Exception as e:
    print('FAIL - step 1056' if isinstance(e, AssertionError) else f'ERROR - step 1056: {e}')

print("STEP 1057 - Check element div#None.['c-image-v2__container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2__container']")))
    print('PASS - step 1057')
except Exception as e:
    print('FAIL - step 1057' if isinstance(e, AssertionError) else f'ERROR - step 1057: {e}')

print("STEP 1058 - Check element picture#None.['c-image-v2__wrp']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2__wrp']")))
    print('PASS - step 1058')
except Exception as e:
    print('FAIL - step 1058' if isinstance(e, AssertionError) else f'ERROR - step 1058: {e}')

print("STEP 1059 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1059')
except Exception as e:
    print('FAIL - step 1059' if isinstance(e, AssertionError) else f'ERROR - step 1059: {e}')

print("STEP 1060 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1060')
except Exception as e:
    print('FAIL - step 1060' if isinstance(e, AssertionError) else f'ERROR - step 1060: {e}')

print("STEP 1061 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1061')
except Exception as e:
    print('FAIL - step 1061' if isinstance(e, AssertionError) else f'ERROR - step 1061: {e}')

print("STEP 1062 - Check element img#None.['c-image-v2__img']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2__img']")))
    print('PASS - step 1062')
except Exception as e:
    print('FAIL - step 1062' if isinstance(e, AssertionError) else f'ERROR - step 1062: {e}')

print("STEP 1063 - Check element script#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "script")))
    print('PASS - step 1063')
except Exception as e:
    print('FAIL - step 1063' if isinstance(e, AssertionError) else f'ERROR - step 1063: {e}')

print("STEP 1064 - Check element div#None.['c-generic-carousel-slider__slide', 'swiper-slide', 'swiper-slide-next']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-generic-carousel-slider__slide', 'swiper-slide', 'swiper-slide-next']")))
    print('PASS - step 1064')
except Exception as e:
    print('FAIL - step 1064' if isinstance(e, AssertionError) else f'ERROR - step 1064: {e}')

print("STEP 1065 - Check element hp-generic-card#None.['c-generic-card']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-generic-card']")))
    print('PASS - step 1065')
except Exception as e:
    print('FAIL - step 1065' if isinstance(e, AssertionError) else f'ERROR - step 1065: {e}')

print("STEP 1066 - Check element div#None.['c-generic-card__image', 'c-video-container--container-fit']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-generic-card__image', 'c-video-container--container-fit']")))
    print('PASS - step 1066')
except Exception as e:
    print('FAIL - step 1066' if isinstance(e, AssertionError) else f'ERROR - step 1066: {e}')

print("STEP 1067 - Check element div#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "div")))
    print('PASS - step 1067')
except Exception as e:
    print('FAIL - step 1067' if isinstance(e, AssertionError) else f'ERROR - step 1067: {e}')

print("STEP 1068 - Check element div#None.['customInfoBanner']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['customInfoBanner']")))
    print('PASS - step 1068')
except Exception as e:
    print('FAIL - step 1068' if isinstance(e, AssertionError) else f'ERROR - step 1068: {e}')

print("STEP 1069 - Check element hp-custom-info-banner-v3#None.['js-hp-component', 'c-custom-info-banner-v3', 'check-footnotes-visibility', 'idf2b80a0c34a373d768d005e17e71008d75f3baea28a5de18ffdb6a16c745389d', 'no-tablet-version', 'no-mobile-version', 'js-hp-component-initialized']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['js-hp-component', 'c-custom-info-banner-v3', 'check-footnotes-visibility', 'idf2b80a0c34a373d768d005e17e71008d75f3baea28a5de18ffdb6a16c745389d', 'no-tablet-version', 'no-mobile-version', 'js-hp-component-initialized']")))
    print('PASS - step 1069')
except Exception as e:
    print('FAIL - step 1069' if isinstance(e, AssertionError) else f'ERROR - step 1069: {e}')

print("STEP 1070 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1070')
except Exception as e:
    print('FAIL - step 1070' if isinstance(e, AssertionError) else f'ERROR - step 1070: {e}')

print("STEP 1071 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 1071')
except Exception as e:
    print('FAIL - step 1071' if isinstance(e, AssertionError) else f'ERROR - step 1071: {e}')

print("STEP 1072 - Check element div#None.['general']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['general']")))
    print('PASS - step 1072')
except Exception as e:
    print('FAIL - step 1072' if isinstance(e, AssertionError) else f'ERROR - step 1072: {e}')

print("STEP 1073 - Check element hp-custom-info-banner-v2#None.['js-hp-component', 'c-custom-info-banner-v2', 'id6e4f92009aaf670863c3912c8a7ab4be70f08acfa46b481c057c1532c7e348cb', 'wide-media-layout', 'js-hp-component-initialized']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['js-hp-component', 'c-custom-info-banner-v2', 'id6e4f92009aaf670863c3912c8a7ab4be70f08acfa46b481c057c1532c7e348cb', 'wide-media-layout', 'js-hp-component-initialized']")))
    print('PASS - step 1073')
except Exception as e:
    print('FAIL - step 1073' if isinstance(e, AssertionError) else f'ERROR - step 1073: {e}')

print("STEP 1074 - Check element div#None.['c-custom-info-banner-v2__header', 'header-position-bottom', 'over-content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header', 'header-position-bottom', 'over-content']")))
    print('PASS - step 1074')
except Exception as e:
    print('FAIL - step 1074' if isinstance(e, AssertionError) else f'ERROR - step 1074: {e}')

print("STEP 1075 - Check element div#None.['c-custom-info-banner-v2__header--title-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--title-wrapper']")))
    print('PASS - step 1075')
except Exception as e:
    print('FAIL - step 1075' if isinstance(e, AssertionError) else f'ERROR - step 1075: {e}')

print("STEP 1076 - Check element div#None.['container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['container']")))
    print('PASS - step 1076')
except Exception as e:
    print('FAIL - step 1076' if isinstance(e, AssertionError) else f'ERROR - step 1076: {e}')

print("STEP 1077 - Check element h2#None.['c-custom-info-banner-v2__header--title', 'xxl', 'reset-list', 'no-default-list-spacings', 'extra-indented']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--title', 'xxl', 'reset-list', 'no-default-list-spacings', 'extra-indented']")))
    print('PASS - step 1077')
except Exception as e:
    print('FAIL - step 1077' if isinstance(e, AssertionError) else f'ERROR - step 1077: {e}')

print("STEP 1078 - Check element div#None.['c-custom-info-banner-v2__header--subtitle-wrapper', 'enable-cta']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--subtitle-wrapper', 'enable-cta']")))
    print('PASS - step 1078')
except Exception as e:
    print('FAIL - step 1078' if isinstance(e, AssertionError) else f'ERROR - step 1078: {e}')

print("STEP 1079 - Check element div#None.['container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['container']")))
    print('PASS - step 1079')
except Exception as e:
    print('FAIL - step 1079' if isinstance(e, AssertionError) else f'ERROR - step 1079: {e}')

print("STEP 1080 - Check element h3#None.['c-custom-info-banner-v2__header--subtitle', 'h1', 'reset-list', 'no-default-list-spacings', 'extra-indented']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--subtitle', 'h1', 'reset-list', 'no-default-list-spacings', 'extra-indented']")))
    print('PASS - step 1080')
except Exception as e:
    print('FAIL - step 1080' if isinstance(e, AssertionError) else f'ERROR - step 1080: {e}')

print("STEP 1081 - Check element div#None.['ctaGroup']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ctaGroup']")))
    print('PASS - step 1081')
except Exception as e:
    print('FAIL - step 1081' if isinstance(e, AssertionError) else f'ERROR - step 1081: {e}')

print("STEP 1082 - Check element div#None.['cta-group', 'inline-container', 'idaee5cb42dca99561e51dcfbfba1b620d496c209730014d0e4d33bce39bff1383']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['cta-group', 'inline-container', 'idaee5cb42dca99561e51dcfbfba1b620d496c209730014d0e4d33bce39bff1383']")))
    print('PASS - step 1082')
except Exception as e:
    print('FAIL - step 1082' if isinstance(e, AssertionError) else f'ERROR - step 1082: {e}')

print("STEP 1083 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1083')
except Exception as e:
    print('FAIL - step 1083' if isinstance(e, AssertionError) else f'ERROR - step 1083: {e}')

print("STEP 1084 - Check element div#None.['ctaButton']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ctaButton']")))
    print('PASS - step 1084')
except Exception as e:
    print('FAIL - step 1084' if isinstance(e, AssertionError) else f'ERROR - step 1084: {e}')

print("STEP 1085 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1085')
except Exception as e:
    print('FAIL - step 1085' if isinstance(e, AssertionError) else f'ERROR - step 1085: {e}')

print("STEP 1086 - Check element a#id4f773fad257b3647d03e45dca4969cedad4e79a699d0b05528906c9656465a72.['c-button', 'append-misc-url-params']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id4f773fad257b3647d03e45dca4969cedad4e79a699d0b05528906c9656465a72")))
    print('PASS - step 1086')
except Exception as e:
    print('FAIL - step 1086' if isinstance(e, AssertionError) else f'ERROR - step 1086: {e}')

print("STEP 1087 - Check element span#None.['c-button__text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-button__text']")))
    print('PASS - step 1087')
except Exception as e:
    print('FAIL - step 1087' if isinstance(e, AssertionError) else f'ERROR - step 1087: {e}')

print("STEP 1088 - Check element p#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "p")))
    print('PASS - step 1088')
except Exception as e:
    print('FAIL - step 1088' if isinstance(e, AssertionError) else f'ERROR - step 1088: {e}')

print("STEP 1089 - Check element div#None.['ctaButton']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ctaButton']")))
    print('PASS - step 1089')
except Exception as e:
    print('FAIL - step 1089' if isinstance(e, AssertionError) else f'ERROR - step 1089: {e}')

print("STEP 1090 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1090')
except Exception as e:
    print('FAIL - step 1090' if isinstance(e, AssertionError) else f'ERROR - step 1090: {e}')

print("STEP 1091 - Check element a#id9127d79c9838a2d4c0efb4a36acb30a94e35d90a801a217a0c784b5e1c9e951f.['c-button', 'append-misc-url-params']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id9127d79c9838a2d4c0efb4a36acb30a94e35d90a801a217a0c784b5e1c9e951f")))
    print('PASS - step 1091')
except Exception as e:
    print('FAIL - step 1091' if isinstance(e, AssertionError) else f'ERROR - step 1091: {e}')

print("STEP 1092 - Check element span#None.['c-button__text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-button__text']")))
    print('PASS - step 1092')
except Exception as e:
    print('FAIL - step 1092' if isinstance(e, AssertionError) else f'ERROR - step 1092: {e}')

print("STEP 1093 - Check element p#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "p")))
    print('PASS - step 1093')
except Exception as e:
    print('FAIL - step 1093' if isinstance(e, AssertionError) else f'ERROR - step 1093: {e}')

print("STEP 1094 - Check element div#None.['c-custom-info-banner-v2__container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__container']")))
    print('PASS - step 1094')
except Exception as e:
    print('FAIL - step 1094' if isinstance(e, AssertionError) else f'ERROR - step 1094: {e}')

print("STEP 1095 - Check element div#None.['c-custom-info-banner-v2__content', 'container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__content', 'container']")))
    print('PASS - step 1095')
except Exception as e:
    print('FAIL - step 1095' if isinstance(e, AssertionError) else f'ERROR - step 1095: {e}')

print("STEP 1096 - Check element div#None.['c-custom-info-banner-v2__content--inner', 'badges-position-top']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__content--inner', 'badges-position-top']")))
    print('PASS - step 1096')
except Exception as e:
    print('FAIL - step 1096' if isinstance(e, AssertionError) else f'ERROR - step 1096: {e}')

print("STEP 1097 - Check element div#None.['c-custom-info-banner-v2__media']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__media']")))
    print('PASS - step 1097')
except Exception as e:
    print('FAIL - step 1097' if isinstance(e, AssertionError) else f'ERROR - step 1097: {e}')

print("STEP 1098 - Check element div#None.['c-image-v2', 'image-v2-ee90a9ab-6']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2', 'image-v2-ee90a9ab-6']")))
    print('PASS - step 1098')
except Exception as e:
    print('FAIL - step 1098' if isinstance(e, AssertionError) else f'ERROR - step 1098: {e}')

print("STEP 1099 - Check element div#None.['c-image-v2__container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2__container']")))
    print('PASS - step 1099')
except Exception as e:
    print('FAIL - step 1099' if isinstance(e, AssertionError) else f'ERROR - step 1099: {e}')

print("STEP 1100 - Check element picture#None.['c-image-v2__wrp']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2__wrp']")))
    print('PASS - step 1100')
except Exception as e:
    print('FAIL - step 1100' if isinstance(e, AssertionError) else f'ERROR - step 1100: {e}')

print("STEP 1101 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1101')
except Exception as e:
    print('FAIL - step 1101' if isinstance(e, AssertionError) else f'ERROR - step 1101: {e}')

print("STEP 1102 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1102')
except Exception as e:
    print('FAIL - step 1102' if isinstance(e, AssertionError) else f'ERROR - step 1102: {e}')

print("STEP 1103 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1103')
except Exception as e:
    print('FAIL - step 1103' if isinstance(e, AssertionError) else f'ERROR - step 1103: {e}')

print("STEP 1104 - Check element img#None.['c-image-v2__img']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2__img']")))
    print('PASS - step 1104')
except Exception as e:
    print('FAIL - step 1104' if isinstance(e, AssertionError) else f'ERROR - step 1104: {e}')

print("STEP 1105 - Check element div#None.['c-generic-carousel-slider__slide', 'swiper-slide']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-generic-carousel-slider__slide', 'swiper-slide']")))
    print('PASS - step 1105')
except Exception as e:
    print('FAIL - step 1105' if isinstance(e, AssertionError) else f'ERROR - step 1105: {e}')

print("STEP 1106 - Check element hp-generic-card#None.['c-generic-card']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-generic-card']")))
    print('PASS - step 1106')
except Exception as e:
    print('FAIL - step 1106' if isinstance(e, AssertionError) else f'ERROR - step 1106: {e}')

print("STEP 1107 - Check element div#None.['c-generic-card__image', 'c-video-container--container-fit']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-generic-card__image', 'c-video-container--container-fit']")))
    print('PASS - step 1107')
except Exception as e:
    print('FAIL - step 1107' if isinstance(e, AssertionError) else f'ERROR - step 1107: {e}')

print("STEP 1108 - Check element div#None.['cib-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['cib-wrapper']")))
    print('PASS - step 1108')
except Exception as e:
    print('FAIL - step 1108' if isinstance(e, AssertionError) else f'ERROR - step 1108: {e}')

print("STEP 1109 - Check element div#None.['customInfoBanner']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['customInfoBanner']")))
    print('PASS - step 1109')
except Exception as e:
    print('FAIL - step 1109' if isinstance(e, AssertionError) else f'ERROR - step 1109: {e}')

print("STEP 1110 - Check element hp-custom-info-banner-v2#None.['js-hp-component', 'c-custom-info-banner-v2', 'id2137a0ffbc0f5c6e915527cb709ef9812f4a1946e05c674d45d904ef7e79d7a4', 'media-position-top', 'title-on-side', 'inside-generic-carousel', 'js-hp-component-initialized']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['js-hp-component', 'c-custom-info-banner-v2', 'id2137a0ffbc0f5c6e915527cb709ef9812f4a1946e05c674d45d904ef7e79d7a4', 'media-position-top', 'title-on-side', 'inside-generic-carousel', 'js-hp-component-initialized']")))
    print('PASS - step 1110')
except Exception as e:
    print('FAIL - step 1110' if isinstance(e, AssertionError) else f'ERROR - step 1110: {e}')

print("STEP 1111 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1111')
except Exception as e:
    print('FAIL - step 1111' if isinstance(e, AssertionError) else f'ERROR - step 1111: {e}')

print("STEP 1112 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1112')
except Exception as e:
    print('FAIL - step 1112' if isinstance(e, AssertionError) else f'ERROR - step 1112: {e}')

print("STEP 1113 - Check element div#None.['c-custom-info-banner-v2__media', 'c-custom-info-banner-v2__media--cloned']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__media', 'c-custom-info-banner-v2__media--cloned']")))
    print('PASS - step 1113')
except Exception as e:
    print('FAIL - step 1113' if isinstance(e, AssertionError) else f'ERROR - step 1113: {e}')

print("STEP 1114 - Check element div#None.['c-image-v2', 'image-v2-19fad8ae-8']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2', 'image-v2-19fad8ae-8']")))
    print('PASS - step 1114')
except Exception as e:
    print('FAIL - step 1114' if isinstance(e, AssertionError) else f'ERROR - step 1114: {e}')

print("STEP 1115 - Check element div#None.['c-image-v2__container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2__container']")))
    print('PASS - step 1115')
except Exception as e:
    print('FAIL - step 1115' if isinstance(e, AssertionError) else f'ERROR - step 1115: {e}')

print("STEP 1116 - Check element picture#None.['c-image-v2__wrp']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2__wrp']")))
    print('PASS - step 1116')
except Exception as e:
    print('FAIL - step 1116' if isinstance(e, AssertionError) else f'ERROR - step 1116: {e}')

print("STEP 1117 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1117')
except Exception as e:
    print('FAIL - step 1117' if isinstance(e, AssertionError) else f'ERROR - step 1117: {e}')

print("STEP 1118 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1118')
except Exception as e:
    print('FAIL - step 1118' if isinstance(e, AssertionError) else f'ERROR - step 1118: {e}')

print("STEP 1119 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1119')
except Exception as e:
    print('FAIL - step 1119' if isinstance(e, AssertionError) else f'ERROR - step 1119: {e}')

print("STEP 1120 - Check element img#None.['c-image-v2__img']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2__img']")))
    print('PASS - step 1120')
except Exception as e:
    print('FAIL - step 1120' if isinstance(e, AssertionError) else f'ERROR - step 1120: {e}')

print("STEP 1121 - Check element div#None.['c-custom-info-banner-v2__header']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header']")))
    print('PASS - step 1121')
except Exception as e:
    print('FAIL - step 1121' if isinstance(e, AssertionError) else f'ERROR - step 1121: {e}')

print("STEP 1122 - Check element div#None.['c-custom-info-banner-v2__header--title-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--title-wrapper']")))
    print('PASS - step 1122')
except Exception as e:
    print('FAIL - step 1122' if isinstance(e, AssertionError) else f'ERROR - step 1122: {e}')

print("STEP 1123 - Check element div#None.['container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['container']")))
    print('PASS - step 1123')
except Exception as e:
    print('FAIL - step 1123' if isinstance(e, AssertionError) else f'ERROR - step 1123: {e}')

print("STEP 1124 - Check element h2#None.['c-custom-info-banner-v2__header--title', 'xl', 'reset-list', 'no-default-list-spacings', 'extra-indented']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--title', 'xl', 'reset-list', 'no-default-list-spacings', 'extra-indented']")))
    print('PASS - step 1124')
except Exception as e:
    print('FAIL - step 1124' if isinstance(e, AssertionError) else f'ERROR - step 1124: {e}')

print("STEP 1125 - Check element div#None.['c-custom-info-banner-v2__header--subtitle-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--subtitle-wrapper']")))
    print('PASS - step 1125')
except Exception as e:
    print('FAIL - step 1125' if isinstance(e, AssertionError) else f'ERROR - step 1125: {e}')

print("STEP 1126 - Check element div#None.['container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['container']")))
    print('PASS - step 1126')
except Exception as e:
    print('FAIL - step 1126' if isinstance(e, AssertionError) else f'ERROR - step 1126: {e}')

print("STEP 1127 - Check element h3#None.['c-custom-info-banner-v2__header--subtitle', 'h5', 'reset-list', 'no-default-list-spacings', 'extra-indented']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--subtitle', 'h5', 'reset-list', 'no-default-list-spacings', 'extra-indented']")))
    print('PASS - step 1127')
except Exception as e:
    print('FAIL - step 1127' if isinstance(e, AssertionError) else f'ERROR - step 1127: {e}')

print("STEP 1128 - Check element div#None.['c-custom-info-banner-v2__container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__container']")))
    print('PASS - step 1128')
except Exception as e:
    print('FAIL - step 1128' if isinstance(e, AssertionError) else f'ERROR - step 1128: {e}')

print("STEP 1129 - Check element div#None.['c-custom-info-banner-v2__content', 'container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__content', 'container']")))
    print('PASS - step 1129')
except Exception as e:
    print('FAIL - step 1129' if isinstance(e, AssertionError) else f'ERROR - step 1129: {e}')

print("STEP 1130 - Check element div#None.['c-custom-info-banner-v2__content--inner']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__content--inner']")))
    print('PASS - step 1130')
except Exception as e:
    print('FAIL - step 1130' if isinstance(e, AssertionError) else f'ERROR - step 1130: {e}')

print("STEP 1131 - Check element div#None.['c-custom-info-banner-v2__header--title-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--title-wrapper']")))
    print('PASS - step 1131')
except Exception as e:
    print('FAIL - step 1131' if isinstance(e, AssertionError) else f'ERROR - step 1131: {e}')

print("STEP 1132 - Check element div#None.['c-custom-info-banner-v2__header--title', 'xl', 'reset-list', 'no-default-list-spacings', 'extra-indented']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--title', 'xl', 'reset-list', 'no-default-list-spacings', 'extra-indented']")))
    print('PASS - step 1132')
except Exception as e:
    print('FAIL - step 1132' if isinstance(e, AssertionError) else f'ERROR - step 1132: {e}')

print("STEP 1133 - Check element div#None.['c-custom-info-banner-v2__header--subtitle-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--subtitle-wrapper']")))
    print('PASS - step 1133')
except Exception as e:
    print('FAIL - step 1133' if isinstance(e, AssertionError) else f'ERROR - step 1133: {e}')

print("STEP 1134 - Check element div#None.['c-custom-info-banner-v2__header--subtitle', 'h5', 'reset-list', 'no-default-list-spacings', 'extra-indented']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--subtitle', 'h5', 'reset-list', 'no-default-list-spacings', 'extra-indented']")))
    print('PASS - step 1134')
except Exception as e:
    print('FAIL - step 1134' if isinstance(e, AssertionError) else f'ERROR - step 1134: {e}')

print("STEP 1135 - Check element div#None.['c-custom-info-banner-v2__content--components-list']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__content--components-list']")))
    print('PASS - step 1135')
except Exception as e:
    print('FAIL - step 1135' if isinstance(e, AssertionError) else f'ERROR - step 1135: {e}')

print("STEP 1136 - Check element div#None.['ctaGroup']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ctaGroup']")))
    print('PASS - step 1136')
except Exception as e:
    print('FAIL - step 1136' if isinstance(e, AssertionError) else f'ERROR - step 1136: {e}')

print("STEP 1137 - Check element div#None.['cta-group', 'inline-container', 'idee1e9b133477b0a2204c80bb6faef2c6a1158be0fff6173d3c918d0715458aba']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['cta-group', 'inline-container', 'idee1e9b133477b0a2204c80bb6faef2c6a1158be0fff6173d3c918d0715458aba']")))
    print('PASS - step 1137')
except Exception as e:
    print('FAIL - step 1137' if isinstance(e, AssertionError) else f'ERROR - step 1137: {e}')

print("STEP 1138 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1138')
except Exception as e:
    print('FAIL - step 1138' if isinstance(e, AssertionError) else f'ERROR - step 1138: {e}')

print("STEP 1139 - Check element div#None.['ctaButton']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ctaButton']")))
    print('PASS - step 1139')
except Exception as e:
    print('FAIL - step 1139' if isinstance(e, AssertionError) else f'ERROR - step 1139: {e}')

print("STEP 1140 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1140')
except Exception as e:
    print('FAIL - step 1140' if isinstance(e, AssertionError) else f'ERROR - step 1140: {e}')

print("STEP 1141 - Check element a#ida25413bb4e9b793af733cadb9d6981fb5d8622bd630fc7aed64e3380705762da.['c-button', 'append-misc-url-params', 'full-width']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "ida25413bb4e9b793af733cadb9d6981fb5d8622bd630fc7aed64e3380705762da")))
    print('PASS - step 1141')
except Exception as e:
    print('FAIL - step 1141' if isinstance(e, AssertionError) else f'ERROR - step 1141: {e}')

print("STEP 1142 - Check element span#None.['c-button__text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-button__text']")))
    print('PASS - step 1142')
except Exception as e:
    print('FAIL - step 1142' if isinstance(e, AssertionError) else f'ERROR - step 1142: {e}')

print("STEP 1143 - Check element p#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "p")))
    print('PASS - step 1143')
except Exception as e:
    print('FAIL - step 1143' if isinstance(e, AssertionError) else f'ERROR - step 1143: {e}')

print("STEP 1144 - Check element div#None.['ctaButton']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ctaButton']")))
    print('PASS - step 1144')
except Exception as e:
    print('FAIL - step 1144' if isinstance(e, AssertionError) else f'ERROR - step 1144: {e}')

print("STEP 1145 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1145')
except Exception as e:
    print('FAIL - step 1145' if isinstance(e, AssertionError) else f'ERROR - step 1145: {e}')

print("STEP 1146 - Check element a#id602fb63ccb36c630280f53e9239025e0bb11b805d1088e9ac66cbe0bc2821f6a.['c-button-outline', 'append-misc-url-params', 'full-width']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id602fb63ccb36c630280f53e9239025e0bb11b805d1088e9ac66cbe0bc2821f6a")))
    print('PASS - step 1146')
except Exception as e:
    print('FAIL - step 1146' if isinstance(e, AssertionError) else f'ERROR - step 1146: {e}')

print("STEP 1147 - Check element span#None.['c-button__text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-button__text']")))
    print('PASS - step 1147')
except Exception as e:
    print('FAIL - step 1147' if isinstance(e, AssertionError) else f'ERROR - step 1147: {e}')

print("STEP 1148 - Check element p#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "p")))
    print('PASS - step 1148')
except Exception as e:
    print('FAIL - step 1148' if isinstance(e, AssertionError) else f'ERROR - step 1148: {e}')

print("STEP 1149 - Check element div#None.['c-custom-info-banner-v2__media']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__media']")))
    print('PASS - step 1149')
except Exception as e:
    print('FAIL - step 1149' if isinstance(e, AssertionError) else f'ERROR - step 1149: {e}')

print("STEP 1150 - Check element div#None.['c-image-v2', 'image-v2-4dab9a6a-10']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2', 'image-v2-4dab9a6a-10']")))
    print('PASS - step 1150')
except Exception as e:
    print('FAIL - step 1150' if isinstance(e, AssertionError) else f'ERROR - step 1150: {e}')

print("STEP 1151 - Check element div#None.['c-image-v2__container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2__container']")))
    print('PASS - step 1151')
except Exception as e:
    print('FAIL - step 1151' if isinstance(e, AssertionError) else f'ERROR - step 1151: {e}')

print("STEP 1152 - Check element picture#None.['c-image-v2__wrp']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2__wrp']")))
    print('PASS - step 1152')
except Exception as e:
    print('FAIL - step 1152' if isinstance(e, AssertionError) else f'ERROR - step 1152: {e}')

print("STEP 1153 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1153')
except Exception as e:
    print('FAIL - step 1153' if isinstance(e, AssertionError) else f'ERROR - step 1153: {e}')

print("STEP 1154 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1154')
except Exception as e:
    print('FAIL - step 1154' if isinstance(e, AssertionError) else f'ERROR - step 1154: {e}')

print("STEP 1155 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1155')
except Exception as e:
    print('FAIL - step 1155' if isinstance(e, AssertionError) else f'ERROR - step 1155: {e}')

print("STEP 1156 - Check element img#None.['c-image-v2__img']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2__img']")))
    print('PASS - step 1156')
except Exception as e:
    print('FAIL - step 1156' if isinstance(e, AssertionError) else f'ERROR - step 1156: {e}')

print("STEP 1157 - Check element script#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "script")))
    print('PASS - step 1157')
except Exception as e:
    print('FAIL - step 1157' if isinstance(e, AssertionError) else f'ERROR - step 1157: {e}')

print("STEP 1158 - Check element div#None.['c-generic-carousel-slider__slide', 'swiper-slide']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-generic-carousel-slider__slide', 'swiper-slide']")))
    print('PASS - step 1158')
except Exception as e:
    print('FAIL - step 1158' if isinstance(e, AssertionError) else f'ERROR - step 1158: {e}')

print("STEP 1159 - Check element hp-generic-card#None.['c-generic-card']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-generic-card']")))
    print('PASS - step 1159')
except Exception as e:
    print('FAIL - step 1159' if isinstance(e, AssertionError) else f'ERROR - step 1159: {e}')

print("STEP 1160 - Check element div#None.['c-generic-card__image', 'c-video-container--container-fit']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-generic-card__image', 'c-video-container--container-fit']")))
    print('PASS - step 1160')
except Exception as e:
    print('FAIL - step 1160' if isinstance(e, AssertionError) else f'ERROR - step 1160: {e}')

print("STEP 1161 - Check element div#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "div")))
    print('PASS - step 1161')
except Exception as e:
    print('FAIL - step 1161' if isinstance(e, AssertionError) else f'ERROR - step 1161: {e}')

print("STEP 1162 - Check element div#None.['customInfoBanner']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['customInfoBanner']")))
    print('PASS - step 1162')
except Exception as e:
    print('FAIL - step 1162' if isinstance(e, AssertionError) else f'ERROR - step 1162: {e}')

print("STEP 1163 - Check element hp-custom-info-banner-v3#None.['js-hp-component', 'c-custom-info-banner-v3', 'check-footnotes-visibility', 'id9062972ccc989035eee641d7654fa21ea1bab2f6829b217f063d876bf1b62271', 'no-mobile-version', 'js-hp-component-initialized']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['js-hp-component', 'c-custom-info-banner-v3', 'check-footnotes-visibility', 'id9062972ccc989035eee641d7654fa21ea1bab2f6829b217f063d876bf1b62271', 'no-mobile-version', 'js-hp-component-initialized']")))
    print('PASS - step 1163')
except Exception as e:
    print('FAIL - step 1163' if isinstance(e, AssertionError) else f'ERROR - step 1163: {e}')

print("STEP 1164 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1164')
except Exception as e:
    print('FAIL - step 1164' if isinstance(e, AssertionError) else f'ERROR - step 1164: {e}')

print("STEP 1165 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 1165')
except Exception as e:
    print('FAIL - step 1165' if isinstance(e, AssertionError) else f'ERROR - step 1165: {e}')

print("STEP 1166 - Check element div#None.['general']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['general']")))
    print('PASS - step 1166')
except Exception as e:
    print('FAIL - step 1166' if isinstance(e, AssertionError) else f'ERROR - step 1166: {e}')

print("STEP 1167 - Check element hp-custom-info-banner-v2#None.['js-hp-component', 'c-custom-info-banner-v2', 'idf2d509256a2be76a7f786bea7e7e84518b81d5dc9768a3fd2dc762316d9930cc', 'media-position-top', 'title-on-side', 'js-hp-component-initialized']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['js-hp-component', 'c-custom-info-banner-v2', 'idf2d509256a2be76a7f786bea7e7e84518b81d5dc9768a3fd2dc762316d9930cc', 'media-position-top', 'title-on-side', 'js-hp-component-initialized']")))
    print('PASS - step 1167')
except Exception as e:
    print('FAIL - step 1167' if isinstance(e, AssertionError) else f'ERROR - step 1167: {e}')

print("STEP 1168 - Check element div#None.['c-custom-info-banner-v2__media', 'c-custom-info-banner-v2__media--cloned', 'focal-point--left']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__media', 'c-custom-info-banner-v2__media--cloned', 'focal-point--left']")))
    print('PASS - step 1168')
except Exception as e:
    print('FAIL - step 1168' if isinstance(e, AssertionError) else f'ERROR - step 1168: {e}')

print("STEP 1169 - Check element div#None.['c-image-v2', 'image-v2-999b70c9-12']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2', 'image-v2-999b70c9-12']")))
    print('PASS - step 1169')
except Exception as e:
    print('FAIL - step 1169' if isinstance(e, AssertionError) else f'ERROR - step 1169: {e}')

print("STEP 1170 - Check element div#None.['c-image-v2__container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2__container']")))
    print('PASS - step 1170')
except Exception as e:
    print('FAIL - step 1170' if isinstance(e, AssertionError) else f'ERROR - step 1170: {e}')

print("STEP 1171 - Check element picture#None.['c-image-v2__wrp']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2__wrp']")))
    print('PASS - step 1171')
except Exception as e:
    print('FAIL - step 1171' if isinstance(e, AssertionError) else f'ERROR - step 1171: {e}')

print("STEP 1172 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1172')
except Exception as e:
    print('FAIL - step 1172' if isinstance(e, AssertionError) else f'ERROR - step 1172: {e}')

print("STEP 1173 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1173')
except Exception as e:
    print('FAIL - step 1173' if isinstance(e, AssertionError) else f'ERROR - step 1173: {e}')

print("STEP 1174 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1174')
except Exception as e:
    print('FAIL - step 1174' if isinstance(e, AssertionError) else f'ERROR - step 1174: {e}')

print("STEP 1175 - Check element img#None.['c-image-v2__img']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2__img']")))
    print('PASS - step 1175')
except Exception as e:
    print('FAIL - step 1175' if isinstance(e, AssertionError) else f'ERROR - step 1175: {e}')

print("STEP 1176 - Check element div#None.['c-custom-info-banner-v2__header']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header']")))
    print('PASS - step 1176')
except Exception as e:
    print('FAIL - step 1176' if isinstance(e, AssertionError) else f'ERROR - step 1176: {e}')

print("STEP 1177 - Check element div#None.['c-custom-info-banner-v2__header--title-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--title-wrapper']")))
    print('PASS - step 1177')
except Exception as e:
    print('FAIL - step 1177' if isinstance(e, AssertionError) else f'ERROR - step 1177: {e}')

print("STEP 1178 - Check element div#None.['container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['container']")))
    print('PASS - step 1178')
except Exception as e:
    print('FAIL - step 1178' if isinstance(e, AssertionError) else f'ERROR - step 1178: {e}')

print("STEP 1179 - Check element h2#None.['c-custom-info-banner-v2__header--title', 'h1', 'reset-list', 'no-default-list-spacings', 'extra-indented']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--title', 'h1', 'reset-list', 'no-default-list-spacings', 'extra-indented']")))
    print('PASS - step 1179')
except Exception as e:
    print('FAIL - step 1179' if isinstance(e, AssertionError) else f'ERROR - step 1179: {e}')

print("STEP 1180 - Check element div#None.['c-custom-info-banner-v2__header--subtitle-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--subtitle-wrapper']")))
    print('PASS - step 1180')
except Exception as e:
    print('FAIL - step 1180' if isinstance(e, AssertionError) else f'ERROR - step 1180: {e}')

print("STEP 1181 - Check element div#None.['container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['container']")))
    print('PASS - step 1181')
except Exception as e:
    print('FAIL - step 1181' if isinstance(e, AssertionError) else f'ERROR - step 1181: {e}')

print("STEP 1182 - Check element h3#None.['c-custom-info-banner-v2__header--subtitle', 'h5', 'reset-list', 'no-default-list-spacings', 'extra-indented']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--subtitle', 'h5', 'reset-list', 'no-default-list-spacings', 'extra-indented']")))
    print('PASS - step 1182')
except Exception as e:
    print('FAIL - step 1182' if isinstance(e, AssertionError) else f'ERROR - step 1182: {e}')

print("STEP 1183 - Check element div#None.['c-custom-info-banner-v2__container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__container']")))
    print('PASS - step 1183')
except Exception as e:
    print('FAIL - step 1183' if isinstance(e, AssertionError) else f'ERROR - step 1183: {e}')

print("STEP 1184 - Check element div#None.['c-custom-info-banner-v2__content', 'container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__content', 'container']")))
    print('PASS - step 1184')
except Exception as e:
    print('FAIL - step 1184' if isinstance(e, AssertionError) else f'ERROR - step 1184: {e}')

print("STEP 1185 - Check element div#None.['c-custom-info-banner-v2__content--inner']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__content--inner']")))
    print('PASS - step 1185')
except Exception as e:
    print('FAIL - step 1185' if isinstance(e, AssertionError) else f'ERROR - step 1185: {e}')

print("STEP 1186 - Check element div#None.['c-custom-info-banner-v2__header--title-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--title-wrapper']")))
    print('PASS - step 1186')
except Exception as e:
    print('FAIL - step 1186' if isinstance(e, AssertionError) else f'ERROR - step 1186: {e}')

print("STEP 1187 - Check element div#None.['c-custom-info-banner-v2__header--title', 'h1', 'reset-list', 'no-default-list-spacings', 'extra-indented']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--title', 'h1', 'reset-list', 'no-default-list-spacings', 'extra-indented']")))
    print('PASS - step 1187')
except Exception as e:
    print('FAIL - step 1187' if isinstance(e, AssertionError) else f'ERROR - step 1187: {e}')

print("STEP 1188 - Check element div#None.['c-custom-info-banner-v2__header--subtitle-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--subtitle-wrapper']")))
    print('PASS - step 1188')
except Exception as e:
    print('FAIL - step 1188' if isinstance(e, AssertionError) else f'ERROR - step 1188: {e}')

print("STEP 1189 - Check element div#None.['c-custom-info-banner-v2__header--subtitle', 'h5', 'reset-list', 'no-default-list-spacings', 'extra-indented']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--subtitle', 'h5', 'reset-list', 'no-default-list-spacings', 'extra-indented']")))
    print('PASS - step 1189')
except Exception as e:
    print('FAIL - step 1189' if isinstance(e, AssertionError) else f'ERROR - step 1189: {e}')

print("STEP 1190 - Check element div#None.['c-custom-info-banner-v2__content--components-list']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__content--components-list']")))
    print('PASS - step 1190')
except Exception as e:
    print('FAIL - step 1190' if isinstance(e, AssertionError) else f'ERROR - step 1190: {e}')

print("STEP 1191 - Check element div#None.['ctaGroup']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ctaGroup']")))
    print('PASS - step 1191')
except Exception as e:
    print('FAIL - step 1191' if isinstance(e, AssertionError) else f'ERROR - step 1191: {e}')

print("STEP 1192 - Check element div#None.['cta-group', 'inline-container', 'id83765efa68d703f48b9738e438054f6e8b48f4834a4bd142078dfc62d239f6aa']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['cta-group', 'inline-container', 'id83765efa68d703f48b9738e438054f6e8b48f4834a4bd142078dfc62d239f6aa']")))
    print('PASS - step 1192')
except Exception as e:
    print('FAIL - step 1192' if isinstance(e, AssertionError) else f'ERROR - step 1192: {e}')

print("STEP 1193 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1193')
except Exception as e:
    print('FAIL - step 1193' if isinstance(e, AssertionError) else f'ERROR - step 1193: {e}')

print("STEP 1194 - Check element div#None.['ctaButton']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ctaButton']")))
    print('PASS - step 1194')
except Exception as e:
    print('FAIL - step 1194' if isinstance(e, AssertionError) else f'ERROR - step 1194: {e}')

print("STEP 1195 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1195')
except Exception as e:
    print('FAIL - step 1195' if isinstance(e, AssertionError) else f'ERROR - step 1195: {e}')

print("STEP 1196 - Check element a#id710658277e06c4e917e24a5622f0fcadb3ff5ca04f7af2c2c0bace01015e20d8.['c-button', 'append-misc-url-params']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id710658277e06c4e917e24a5622f0fcadb3ff5ca04f7af2c2c0bace01015e20d8")))
    print('PASS - step 1196')
except Exception as e:
    print('FAIL - step 1196' if isinstance(e, AssertionError) else f'ERROR - step 1196: {e}')

print("STEP 1197 - Check element span#None.['c-button__text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-button__text']")))
    print('PASS - step 1197')
except Exception as e:
    print('FAIL - step 1197' if isinstance(e, AssertionError) else f'ERROR - step 1197: {e}')

print("STEP 1198 - Check element p#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "p")))
    print('PASS - step 1198')
except Exception as e:
    print('FAIL - step 1198' if isinstance(e, AssertionError) else f'ERROR - step 1198: {e}')

print("STEP 1199 - Check element div#None.['c-custom-info-banner-v2__media', 'focal-point--left']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__media', 'focal-point--left']")))
    print('PASS - step 1199')
except Exception as e:
    print('FAIL - step 1199' if isinstance(e, AssertionError) else f'ERROR - step 1199: {e}')

print("STEP 1200 - Check element div#None.['c-image-v2', 'image-v2-9b8b90b8-14']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2', 'image-v2-9b8b90b8-14']")))
    print('PASS - step 1200')
except Exception as e:
    print('FAIL - step 1200' if isinstance(e, AssertionError) else f'ERROR - step 1200: {e}')

print("STEP 1201 - Check element div#None.['c-image-v2__container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2__container']")))
    print('PASS - step 1201')
except Exception as e:
    print('FAIL - step 1201' if isinstance(e, AssertionError) else f'ERROR - step 1201: {e}')

print("STEP 1202 - Check element picture#None.['c-image-v2__wrp']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2__wrp']")))
    print('PASS - step 1202')
except Exception as e:
    print('FAIL - step 1202' if isinstance(e, AssertionError) else f'ERROR - step 1202: {e}')

print("STEP 1203 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1203')
except Exception as e:
    print('FAIL - step 1203' if isinstance(e, AssertionError) else f'ERROR - step 1203: {e}')

print("STEP 1204 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1204')
except Exception as e:
    print('FAIL - step 1204' if isinstance(e, AssertionError) else f'ERROR - step 1204: {e}')

print("STEP 1205 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1205')
except Exception as e:
    print('FAIL - step 1205' if isinstance(e, AssertionError) else f'ERROR - step 1205: {e}')

print("STEP 1206 - Check element img#None.['c-image-v2__img']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2__img']")))
    print('PASS - step 1206')
except Exception as e:
    print('FAIL - step 1206' if isinstance(e, AssertionError) else f'ERROR - step 1206: {e}')

print("STEP 1207 - Check element script#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "script")))
    print('PASS - step 1207')
except Exception as e:
    print('FAIL - step 1207' if isinstance(e, AssertionError) else f'ERROR - step 1207: {e}')

print("STEP 1208 - Check element div#None.['tablet']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['tablet']")))
    print('PASS - step 1208')
except Exception as e:
    print('FAIL - step 1208' if isinstance(e, AssertionError) else f'ERROR - step 1208: {e}')

print("STEP 1209 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1209')
except Exception as e:
    print('FAIL - step 1209' if isinstance(e, AssertionError) else f'ERROR - step 1209: {e}')

print("STEP 1210 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 1210')
except Exception as e:
    print('FAIL - step 1210' if isinstance(e, AssertionError) else f'ERROR - step 1210: {e}')

print("STEP 1211 - Check element hp-custom-info-banner-v2#None.['js-hp-component', 'c-custom-info-banner-v2', 'id8c9d258ce6d465b84f81985f6f2ec2fbf2f4a7efe58014671cf2398583f174b4', 'media-position-top', 'title-on-side', 'js-hp-component-initialized']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['js-hp-component', 'c-custom-info-banner-v2', 'id8c9d258ce6d465b84f81985f6f2ec2fbf2f4a7efe58014671cf2398583f174b4', 'media-position-top', 'title-on-side', 'js-hp-component-initialized']")))
    print('PASS - step 1211')
except Exception as e:
    print('FAIL - step 1211' if isinstance(e, AssertionError) else f'ERROR - step 1211: {e}')

print("STEP 1212 - Check element div#None.['c-custom-info-banner-v2__media', 'c-custom-info-banner-v2__media--cloned']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__media', 'c-custom-info-banner-v2__media--cloned']")))
    print('PASS - step 1212')
except Exception as e:
    print('FAIL - step 1212' if isinstance(e, AssertionError) else f'ERROR - step 1212: {e}')

print("STEP 1213 - Check element div#None.['c-image-v2', 'image-v2-faa838ca-16']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2', 'image-v2-faa838ca-16']")))
    print('PASS - step 1213')
except Exception as e:
    print('FAIL - step 1213' if isinstance(e, AssertionError) else f'ERROR - step 1213: {e}')

print("STEP 1214 - Check element div#None.['c-image-v2__container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2__container']")))
    print('PASS - step 1214')
except Exception as e:
    print('FAIL - step 1214' if isinstance(e, AssertionError) else f'ERROR - step 1214: {e}')

print("STEP 1215 - Check element picture#None.['c-image-v2__wrp']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2__wrp']")))
    print('PASS - step 1215')
except Exception as e:
    print('FAIL - step 1215' if isinstance(e, AssertionError) else f'ERROR - step 1215: {e}')

print("STEP 1216 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1216')
except Exception as e:
    print('FAIL - step 1216' if isinstance(e, AssertionError) else f'ERROR - step 1216: {e}')

print("STEP 1217 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1217')
except Exception as e:
    print('FAIL - step 1217' if isinstance(e, AssertionError) else f'ERROR - step 1217: {e}')

print("STEP 1218 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1218')
except Exception as e:
    print('FAIL - step 1218' if isinstance(e, AssertionError) else f'ERROR - step 1218: {e}')

print("STEP 1219 - Check element img#None.['c-image-v2__img']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2__img']")))
    print('PASS - step 1219')
except Exception as e:
    print('FAIL - step 1219' if isinstance(e, AssertionError) else f'ERROR - step 1219: {e}')

print("STEP 1220 - Check element div#None.['c-custom-info-banner-v2__header']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header']")))
    print('PASS - step 1220')
except Exception as e:
    print('FAIL - step 1220' if isinstance(e, AssertionError) else f'ERROR - step 1220: {e}')

print("STEP 1221 - Check element div#None.['c-custom-info-banner-v2__header--title-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--title-wrapper']")))
    print('PASS - step 1221')
except Exception as e:
    print('FAIL - step 1221' if isinstance(e, AssertionError) else f'ERROR - step 1221: {e}')

print("STEP 1222 - Check element div#None.['container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['container']")))
    print('PASS - step 1222')
except Exception as e:
    print('FAIL - step 1222' if isinstance(e, AssertionError) else f'ERROR - step 1222: {e}')

print("STEP 1223 - Check element h2#None.['c-custom-info-banner-v2__header--title', 'h1', 'reset-list', 'no-default-list-spacings', 'extra-indented']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--title', 'h1', 'reset-list', 'no-default-list-spacings', 'extra-indented']")))
    print('PASS - step 1223')
except Exception as e:
    print('FAIL - step 1223' if isinstance(e, AssertionError) else f'ERROR - step 1223: {e}')

print("STEP 1224 - Check element div#None.['c-custom-info-banner-v2__header--subtitle-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--subtitle-wrapper']")))
    print('PASS - step 1224')
except Exception as e:
    print('FAIL - step 1224' if isinstance(e, AssertionError) else f'ERROR - step 1224: {e}')

print("STEP 1225 - Check element div#None.['container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['container']")))
    print('PASS - step 1225')
except Exception as e:
    print('FAIL - step 1225' if isinstance(e, AssertionError) else f'ERROR - step 1225: {e}')

print("STEP 1226 - Check element h3#None.['c-custom-info-banner-v2__header--subtitle', 'h5', 'reset-list', 'no-default-list-spacings', 'extra-indented']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--subtitle', 'h5', 'reset-list', 'no-default-list-spacings', 'extra-indented']")))
    print('PASS - step 1226')
except Exception as e:
    print('FAIL - step 1226' if isinstance(e, AssertionError) else f'ERROR - step 1226: {e}')

print("STEP 1227 - Check element div#None.['c-custom-info-banner-v2__container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__container']")))
    print('PASS - step 1227')
except Exception as e:
    print('FAIL - step 1227' if isinstance(e, AssertionError) else f'ERROR - step 1227: {e}')

print("STEP 1228 - Check element div#None.['c-custom-info-banner-v2__content', 'container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__content', 'container']")))
    print('PASS - step 1228')
except Exception as e:
    print('FAIL - step 1228' if isinstance(e, AssertionError) else f'ERROR - step 1228: {e}')

print("STEP 1229 - Check element div#None.['c-custom-info-banner-v2__content--inner']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__content--inner']")))
    print('PASS - step 1229')
except Exception as e:
    print('FAIL - step 1229' if isinstance(e, AssertionError) else f'ERROR - step 1229: {e}')

print("STEP 1230 - Check element div#None.['c-custom-info-banner-v2__header--title-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--title-wrapper']")))
    print('PASS - step 1230')
except Exception as e:
    print('FAIL - step 1230' if isinstance(e, AssertionError) else f'ERROR - step 1230: {e}')

print("STEP 1231 - Check element div#None.['c-custom-info-banner-v2__header--title', 'h1', 'reset-list', 'no-default-list-spacings', 'extra-indented']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--title', 'h1', 'reset-list', 'no-default-list-spacings', 'extra-indented']")))
    print('PASS - step 1231')
except Exception as e:
    print('FAIL - step 1231' if isinstance(e, AssertionError) else f'ERROR - step 1231: {e}')

print("STEP 1232 - Check element div#None.['c-custom-info-banner-v2__header--subtitle-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--subtitle-wrapper']")))
    print('PASS - step 1232')
except Exception as e:
    print('FAIL - step 1232' if isinstance(e, AssertionError) else f'ERROR - step 1232: {e}')

print("STEP 1233 - Check element div#None.['c-custom-info-banner-v2__header--subtitle', 'h5', 'reset-list', 'no-default-list-spacings', 'extra-indented']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--subtitle', 'h5', 'reset-list', 'no-default-list-spacings', 'extra-indented']")))
    print('PASS - step 1233')
except Exception as e:
    print('FAIL - step 1233' if isinstance(e, AssertionError) else f'ERROR - step 1233: {e}')

print("STEP 1234 - Check element div#None.['c-custom-info-banner-v2__content--components-list']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__content--components-list']")))
    print('PASS - step 1234')
except Exception as e:
    print('FAIL - step 1234' if isinstance(e, AssertionError) else f'ERROR - step 1234: {e}')

print("STEP 1235 - Check element div#None.['ctaGroup']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ctaGroup']")))
    print('PASS - step 1235')
except Exception as e:
    print('FAIL - step 1235' if isinstance(e, AssertionError) else f'ERROR - step 1235: {e}')

print("STEP 1236 - Check element div#None.['cta-group', 'inline-container', 'id66a674eb08bf97046670d7892dac666ef3d74a4b4b590f31e6a1105ceb4d9f9c']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['cta-group', 'inline-container', 'id66a674eb08bf97046670d7892dac666ef3d74a4b4b590f31e6a1105ceb4d9f9c']")))
    print('PASS - step 1236')
except Exception as e:
    print('FAIL - step 1236' if isinstance(e, AssertionError) else f'ERROR - step 1236: {e}')

print("STEP 1237 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1237')
except Exception as e:
    print('FAIL - step 1237' if isinstance(e, AssertionError) else f'ERROR - step 1237: {e}')

print("STEP 1238 - Check element div#None.['ctaButton']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ctaButton']")))
    print('PASS - step 1238')
except Exception as e:
    print('FAIL - step 1238' if isinstance(e, AssertionError) else f'ERROR - step 1238: {e}')

print("STEP 1239 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1239')
except Exception as e:
    print('FAIL - step 1239' if isinstance(e, AssertionError) else f'ERROR - step 1239: {e}')

print("STEP 1240 - Check element a#idb8444a1bd7f1c0261678978d6a001733b7f985a132c8fa0d544f77a116ff8dff.['c-button', 'append-misc-url-params']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "idb8444a1bd7f1c0261678978d6a001733b7f985a132c8fa0d544f77a116ff8dff")))
    print('PASS - step 1240')
except Exception as e:
    print('FAIL - step 1240' if isinstance(e, AssertionError) else f'ERROR - step 1240: {e}')

print("STEP 1241 - Check element span#None.['c-button__text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-button__text']")))
    print('PASS - step 1241')
except Exception as e:
    print('FAIL - step 1241' if isinstance(e, AssertionError) else f'ERROR - step 1241: {e}')

print("STEP 1242 - Check element p#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "p")))
    print('PASS - step 1242')
except Exception as e:
    print('FAIL - step 1242' if isinstance(e, AssertionError) else f'ERROR - step 1242: {e}')

print("STEP 1243 - Check element div#None.['c-custom-info-banner-v2__media']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__media']")))
    print('PASS - step 1243')
except Exception as e:
    print('FAIL - step 1243' if isinstance(e, AssertionError) else f'ERROR - step 1243: {e}')

print("STEP 1244 - Check element div#None.['c-image-v2', 'image-v2-00cd9a4b-18']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2', 'image-v2-00cd9a4b-18']")))
    print('PASS - step 1244')
except Exception as e:
    print('FAIL - step 1244' if isinstance(e, AssertionError) else f'ERROR - step 1244: {e}')

print("STEP 1245 - Check element div#None.['c-image-v2__container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2__container']")))
    print('PASS - step 1245')
except Exception as e:
    print('FAIL - step 1245' if isinstance(e, AssertionError) else f'ERROR - step 1245: {e}')

print("STEP 1246 - Check element picture#None.['c-image-v2__wrp']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2__wrp']")))
    print('PASS - step 1246')
except Exception as e:
    print('FAIL - step 1246' if isinstance(e, AssertionError) else f'ERROR - step 1246: {e}')

print("STEP 1247 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1247')
except Exception as e:
    print('FAIL - step 1247' if isinstance(e, AssertionError) else f'ERROR - step 1247: {e}')

print("STEP 1248 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1248')
except Exception as e:
    print('FAIL - step 1248' if isinstance(e, AssertionError) else f'ERROR - step 1248: {e}')

print("STEP 1249 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1249')
except Exception as e:
    print('FAIL - step 1249' if isinstance(e, AssertionError) else f'ERROR - step 1249: {e}')

print("STEP 1250 - Check element img#None.['c-image-v2__img']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2__img']")))
    print('PASS - step 1250')
except Exception as e:
    print('FAIL - step 1250' if isinstance(e, AssertionError) else f'ERROR - step 1250: {e}')

print("STEP 1251 - Check element script#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "script")))
    print('PASS - step 1251')
except Exception as e:
    print('FAIL - step 1251' if isinstance(e, AssertionError) else f'ERROR - step 1251: {e}')

print("STEP 1252 - Check element div#None.['c-generic-carousel-slider__slide', 'swiper-slide']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-generic-carousel-slider__slide', 'swiper-slide']")))
    print('PASS - step 1252')
except Exception as e:
    print('FAIL - step 1252' if isinstance(e, AssertionError) else f'ERROR - step 1252: {e}')

print("STEP 1253 - Check element hp-generic-card#None.['c-generic-card']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-generic-card']")))
    print('PASS - step 1253')
except Exception as e:
    print('FAIL - step 1253' if isinstance(e, AssertionError) else f'ERROR - step 1253: {e}')

print("STEP 1254 - Check element div#None.['c-generic-card__image', 'c-video-container--container-fit']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-generic-card__image', 'c-video-container--container-fit']")))
    print('PASS - step 1254')
except Exception as e:
    print('FAIL - step 1254' if isinstance(e, AssertionError) else f'ERROR - step 1254: {e}')

print("STEP 1255 - Check element div#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "div")))
    print('PASS - step 1255')
except Exception as e:
    print('FAIL - step 1255' if isinstance(e, AssertionError) else f'ERROR - step 1255: {e}')

print("STEP 1256 - Check element div#None.['customInfoBanner']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['customInfoBanner']")))
    print('PASS - step 1256')
except Exception as e:
    print('FAIL - step 1256' if isinstance(e, AssertionError) else f'ERROR - step 1256: {e}')

print("STEP 1257 - Check element hp-custom-info-banner-v3#None.['js-hp-component', 'c-custom-info-banner-v3', 'check-footnotes-visibility', 'id40c290b6524f2a4763c17692ca5641025b3edb5b1a602f197703bf4a8debfa2b', 'no-tablet-version', 'no-mobile-version', 'js-hp-component-initialized']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['js-hp-component', 'c-custom-info-banner-v3', 'check-footnotes-visibility', 'id40c290b6524f2a4763c17692ca5641025b3edb5b1a602f197703bf4a8debfa2b', 'no-tablet-version', 'no-mobile-version', 'js-hp-component-initialized']")))
    print('PASS - step 1257')
except Exception as e:
    print('FAIL - step 1257' if isinstance(e, AssertionError) else f'ERROR - step 1257: {e}')

print("STEP 1258 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1258')
except Exception as e:
    print('FAIL - step 1258' if isinstance(e, AssertionError) else f'ERROR - step 1258: {e}')

print("STEP 1259 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 1259')
except Exception as e:
    print('FAIL - step 1259' if isinstance(e, AssertionError) else f'ERROR - step 1259: {e}')

print("STEP 1260 - Check element div#None.['general']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['general']")))
    print('PASS - step 1260')
except Exception as e:
    print('FAIL - step 1260' if isinstance(e, AssertionError) else f'ERROR - step 1260: {e}')

print("STEP 1261 - Check element hp-custom-info-banner-v2#None.['js-hp-component', 'c-custom-info-banner-v2', 'id146fde78698304ced40bd47e242275df947043005b21752d40b29a11d8983455', 'wide-media-layout', 'js-hp-component-initialized']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['js-hp-component', 'c-custom-info-banner-v2', 'id146fde78698304ced40bd47e242275df947043005b21752d40b29a11d8983455', 'wide-media-layout', 'js-hp-component-initialized']")))
    print('PASS - step 1261')
except Exception as e:
    print('FAIL - step 1261' if isinstance(e, AssertionError) else f'ERROR - step 1261: {e}')

print("STEP 1262 - Check element div#None.['c-custom-info-banner-v2__header', 'header-position-bottom', 'over-content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header', 'header-position-bottom', 'over-content']")))
    print('PASS - step 1262')
except Exception as e:
    print('FAIL - step 1262' if isinstance(e, AssertionError) else f'ERROR - step 1262: {e}')

print("STEP 1263 - Check element div#None.['c-custom-info-banner-v2__header--title-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--title-wrapper']")))
    print('PASS - step 1263')
except Exception as e:
    print('FAIL - step 1263' if isinstance(e, AssertionError) else f'ERROR - step 1263: {e}')

print("STEP 1264 - Check element div#None.['container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['container']")))
    print('PASS - step 1264')
except Exception as e:
    print('FAIL - step 1264' if isinstance(e, AssertionError) else f'ERROR - step 1264: {e}')

print("STEP 1265 - Check element h2#None.['c-custom-info-banner-v2__header--title', 'xxl', 'reset-list', 'no-default-list-spacings', 'extra-indented']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--title', 'xxl', 'reset-list', 'no-default-list-spacings', 'extra-indented']")))
    print('PASS - step 1265')
except Exception as e:
    print('FAIL - step 1265' if isinstance(e, AssertionError) else f'ERROR - step 1265: {e}')

print("STEP 1266 - Check element div#None.['c-custom-info-banner-v2__header--subtitle-wrapper', 'enable-cta']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--subtitle-wrapper', 'enable-cta']")))
    print('PASS - step 1266')
except Exception as e:
    print('FAIL - step 1266' if isinstance(e, AssertionError) else f'ERROR - step 1266: {e}')

print("STEP 1267 - Check element div#None.['container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['container']")))
    print('PASS - step 1267')
except Exception as e:
    print('FAIL - step 1267' if isinstance(e, AssertionError) else f'ERROR - step 1267: {e}')

print("STEP 1268 - Check element h3#None.['c-custom-info-banner-v2__header--subtitle', 'h1', 'reset-list', 'no-default-list-spacings', 'extra-indented']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--subtitle', 'h1', 'reset-list', 'no-default-list-spacings', 'extra-indented']")))
    print('PASS - step 1268')
except Exception as e:
    print('FAIL - step 1268' if isinstance(e, AssertionError) else f'ERROR - step 1268: {e}')

print("STEP 1269 - Check element div#None.['ctaGroup']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ctaGroup']")))
    print('PASS - step 1269')
except Exception as e:
    print('FAIL - step 1269' if isinstance(e, AssertionError) else f'ERROR - step 1269: {e}')

print("STEP 1270 - Check element div#None.['cta-group', 'inline-container', 'id21bbe1cb6de23206b923c17f8083a2e69ddc2138a7170a09ceee4b2fd1a5253a']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['cta-group', 'inline-container', 'id21bbe1cb6de23206b923c17f8083a2e69ddc2138a7170a09ceee4b2fd1a5253a']")))
    print('PASS - step 1270')
except Exception as e:
    print('FAIL - step 1270' if isinstance(e, AssertionError) else f'ERROR - step 1270: {e}')

print("STEP 1271 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1271')
except Exception as e:
    print('FAIL - step 1271' if isinstance(e, AssertionError) else f'ERROR - step 1271: {e}')

print("STEP 1272 - Check element div#None.['ctaButton']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ctaButton']")))
    print('PASS - step 1272')
except Exception as e:
    print('FAIL - step 1272' if isinstance(e, AssertionError) else f'ERROR - step 1272: {e}')

print("STEP 1273 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1273')
except Exception as e:
    print('FAIL - step 1273' if isinstance(e, AssertionError) else f'ERROR - step 1273: {e}')

print("STEP 1274 - Check element a#id72ea8846eb1130f6c22b302b3322a2d52d2fdd210f58dd1930ccd336ea8f1c85.['c-button', 'append-misc-url-params', 'full-width']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id72ea8846eb1130f6c22b302b3322a2d52d2fdd210f58dd1930ccd336ea8f1c85")))
    print('PASS - step 1274')
except Exception as e:
    print('FAIL - step 1274' if isinstance(e, AssertionError) else f'ERROR - step 1274: {e}')

print("STEP 1275 - Check element span#None.['c-button__text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-button__text']")))
    print('PASS - step 1275')
except Exception as e:
    print('FAIL - step 1275' if isinstance(e, AssertionError) else f'ERROR - step 1275: {e}')

print("STEP 1276 - Check element p#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "p")))
    print('PASS - step 1276')
except Exception as e:
    print('FAIL - step 1276' if isinstance(e, AssertionError) else f'ERROR - step 1276: {e}')

print("STEP 1277 - Check element div#None.['ctaButton']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ctaButton']")))
    print('PASS - step 1277')
except Exception as e:
    print('FAIL - step 1277' if isinstance(e, AssertionError) else f'ERROR - step 1277: {e}')

print("STEP 1278 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1278')
except Exception as e:
    print('FAIL - step 1278' if isinstance(e, AssertionError) else f'ERROR - step 1278: {e}')

print("STEP 1279 - Check element a#idac4c9bc8cf8f2e367da8eb7e9161e60e792fc96bf4281620f1716f2aec6ee7fa.['c-button', 'append-misc-url-params', 'full-width']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "idac4c9bc8cf8f2e367da8eb7e9161e60e792fc96bf4281620f1716f2aec6ee7fa")))
    print('PASS - step 1279')
except Exception as e:
    print('FAIL - step 1279' if isinstance(e, AssertionError) else f'ERROR - step 1279: {e}')

print("STEP 1280 - Check element span#None.['c-button__text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-button__text']")))
    print('PASS - step 1280')
except Exception as e:
    print('FAIL - step 1280' if isinstance(e, AssertionError) else f'ERROR - step 1280: {e}')

print("STEP 1281 - Check element p#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "p")))
    print('PASS - step 1281')
except Exception as e:
    print('FAIL - step 1281' if isinstance(e, AssertionError) else f'ERROR - step 1281: {e}')

print("STEP 1282 - Check element div#None.['c-custom-info-banner-v2__container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__container']")))
    print('PASS - step 1282')
except Exception as e:
    print('FAIL - step 1282' if isinstance(e, AssertionError) else f'ERROR - step 1282: {e}')

print("STEP 1283 - Check element div#None.['c-custom-info-banner-v2__content', 'container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__content', 'container']")))
    print('PASS - step 1283')
except Exception as e:
    print('FAIL - step 1283' if isinstance(e, AssertionError) else f'ERROR - step 1283: {e}')

print("STEP 1284 - Check element div#None.['c-custom-info-banner-v2__content--inner', 'badges-position-top']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__content--inner', 'badges-position-top']")))
    print('PASS - step 1284')
except Exception as e:
    print('FAIL - step 1284' if isinstance(e, AssertionError) else f'ERROR - step 1284: {e}')

print("STEP 1285 - Check element div#None.['c-custom-info-banner-v2__media']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__media']")))
    print('PASS - step 1285')
except Exception as e:
    print('FAIL - step 1285' if isinstance(e, AssertionError) else f'ERROR - step 1285: {e}')

print("STEP 1286 - Check element div#None.['c-image-v2', 'image-v2-91ab9a39-20']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2', 'image-v2-91ab9a39-20']")))
    print('PASS - step 1286')
except Exception as e:
    print('FAIL - step 1286' if isinstance(e, AssertionError) else f'ERROR - step 1286: {e}')

print("STEP 1287 - Check element div#None.['c-image-v2__container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2__container']")))
    print('PASS - step 1287')
except Exception as e:
    print('FAIL - step 1287' if isinstance(e, AssertionError) else f'ERROR - step 1287: {e}')

print("STEP 1288 - Check element picture#None.['c-image-v2__wrp']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2__wrp']")))
    print('PASS - step 1288')
except Exception as e:
    print('FAIL - step 1288' if isinstance(e, AssertionError) else f'ERROR - step 1288: {e}')

print("STEP 1289 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1289')
except Exception as e:
    print('FAIL - step 1289' if isinstance(e, AssertionError) else f'ERROR - step 1289: {e}')

print("STEP 1290 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1290')
except Exception as e:
    print('FAIL - step 1290' if isinstance(e, AssertionError) else f'ERROR - step 1290: {e}')

print("STEP 1291 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1291')
except Exception as e:
    print('FAIL - step 1291' if isinstance(e, AssertionError) else f'ERROR - step 1291: {e}')

print("STEP 1292 - Check element img#None.['c-image-v2__img']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2__img']")))
    print('PASS - step 1292')
except Exception as e:
    print('FAIL - step 1292' if isinstance(e, AssertionError) else f'ERROR - step 1292: {e}')

print("STEP 1293 - Check element div#None.['c-generic-carousel-slider__slide', 'swiper-slide', 'swiper-slide-duplicate-prev']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-generic-carousel-slider__slide', 'swiper-slide', 'swiper-slide-duplicate-prev']")))
    print('PASS - step 1293')
except Exception as e:
    print('FAIL - step 1293' if isinstance(e, AssertionError) else f'ERROR - step 1293: {e}')

print("STEP 1294 - Check element hp-generic-card#None.['c-generic-card']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-generic-card']")))
    print('PASS - step 1294')
except Exception as e:
    print('FAIL - step 1294' if isinstance(e, AssertionError) else f'ERROR - step 1294: {e}')

print("STEP 1295 - Check element div#None.['c-generic-card__image', 'c-video-container--container-fit']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-generic-card__image', 'c-video-container--container-fit']")))
    print('PASS - step 1295')
except Exception as e:
    print('FAIL - step 1295' if isinstance(e, AssertionError) else f'ERROR - step 1295: {e}')

print("STEP 1296 - Check element div#None.['cib-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['cib-wrapper']")))
    print('PASS - step 1296')
except Exception as e:
    print('FAIL - step 1296' if isinstance(e, AssertionError) else f'ERROR - step 1296: {e}')

print("STEP 1297 - Check element div#None.['customInfoBanner']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['customInfoBanner']")))
    print('PASS - step 1297')
except Exception as e:
    print('FAIL - step 1297' if isinstance(e, AssertionError) else f'ERROR - step 1297: {e}')

print("STEP 1298 - Check element hp-custom-info-banner-v2#None.['js-hp-component', 'c-custom-info-banner-v2', 'id6b762839ecf3cc8ab4aed7345a432c1376f5a31a2e206e361fe8a6b672c538ca', 'media-position-top', 'title-on-side', 'inside-generic-carousel', 'js-hp-component-initialized']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['js-hp-component', 'c-custom-info-banner-v2', 'id6b762839ecf3cc8ab4aed7345a432c1376f5a31a2e206e361fe8a6b672c538ca', 'media-position-top', 'title-on-side', 'inside-generic-carousel', 'js-hp-component-initialized']")))
    print('PASS - step 1298')
except Exception as e:
    print('FAIL - step 1298' if isinstance(e, AssertionError) else f'ERROR - step 1298: {e}')

print("STEP 1299 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1299')
except Exception as e:
    print('FAIL - step 1299' if isinstance(e, AssertionError) else f'ERROR - step 1299: {e}')

print("STEP 1300 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1300')
except Exception as e:
    print('FAIL - step 1300' if isinstance(e, AssertionError) else f'ERROR - step 1300: {e}')

print("STEP 1301 - Check element div#None.['c-custom-info-banner-v2__media', 'c-custom-info-banner-v2__media--cloned']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__media', 'c-custom-info-banner-v2__media--cloned']")))
    print('PASS - step 1301')
except Exception as e:
    print('FAIL - step 1301' if isinstance(e, AssertionError) else f'ERROR - step 1301: {e}')

print("STEP 1302 - Check element div#None.['c-image-v2', 'image-v2-9b75dd9a-22']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2', 'image-v2-9b75dd9a-22']")))
    print('PASS - step 1302')
except Exception as e:
    print('FAIL - step 1302' if isinstance(e, AssertionError) else f'ERROR - step 1302: {e}')

print("STEP 1303 - Check element div#None.['c-image-v2__container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2__container']")))
    print('PASS - step 1303')
except Exception as e:
    print('FAIL - step 1303' if isinstance(e, AssertionError) else f'ERROR - step 1303: {e}')

print("STEP 1304 - Check element picture#None.['c-image-v2__wrp']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2__wrp']")))
    print('PASS - step 1304')
except Exception as e:
    print('FAIL - step 1304' if isinstance(e, AssertionError) else f'ERROR - step 1304: {e}')

print("STEP 1305 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1305')
except Exception as e:
    print('FAIL - step 1305' if isinstance(e, AssertionError) else f'ERROR - step 1305: {e}')

print("STEP 1306 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1306')
except Exception as e:
    print('FAIL - step 1306' if isinstance(e, AssertionError) else f'ERROR - step 1306: {e}')

print("STEP 1307 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1307')
except Exception as e:
    print('FAIL - step 1307' if isinstance(e, AssertionError) else f'ERROR - step 1307: {e}')

print("STEP 1308 - Check element img#None.['c-image-v2__img']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2__img']")))
    print('PASS - step 1308')
except Exception as e:
    print('FAIL - step 1308' if isinstance(e, AssertionError) else f'ERROR - step 1308: {e}')

print("STEP 1309 - Check element div#None.['c-custom-info-banner-v2__header']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header']")))
    print('PASS - step 1309')
except Exception as e:
    print('FAIL - step 1309' if isinstance(e, AssertionError) else f'ERROR - step 1309: {e}')

print("STEP 1310 - Check element div#None.['c-custom-info-banner-v2__header--title-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--title-wrapper']")))
    print('PASS - step 1310')
except Exception as e:
    print('FAIL - step 1310' if isinstance(e, AssertionError) else f'ERROR - step 1310: {e}')

print("STEP 1311 - Check element div#None.['container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['container']")))
    print('PASS - step 1311')
except Exception as e:
    print('FAIL - step 1311' if isinstance(e, AssertionError) else f'ERROR - step 1311: {e}')

print("STEP 1312 - Check element h2#None.['c-custom-info-banner-v2__header--title', 'xxl', 'reset-list', 'no-default-list-spacings', 'extra-indented']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--title', 'xxl', 'reset-list', 'no-default-list-spacings', 'extra-indented']")))
    print('PASS - step 1312')
except Exception as e:
    print('FAIL - step 1312' if isinstance(e, AssertionError) else f'ERROR - step 1312: {e}')

print("STEP 1313 - Check element div#None.['c-custom-info-banner-v2__header--subtitle-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--subtitle-wrapper']")))
    print('PASS - step 1313')
except Exception as e:
    print('FAIL - step 1313' if isinstance(e, AssertionError) else f'ERROR - step 1313: {e}')

print("STEP 1314 - Check element div#None.['container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['container']")))
    print('PASS - step 1314')
except Exception as e:
    print('FAIL - step 1314' if isinstance(e, AssertionError) else f'ERROR - step 1314: {e}')

print("STEP 1315 - Check element h3#None.['c-custom-info-banner-v2__header--subtitle', 'h2', 'reset-list', 'no-default-list-spacings', 'extra-indented']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--subtitle', 'h2', 'reset-list', 'no-default-list-spacings', 'extra-indented']")))
    print('PASS - step 1315')
except Exception as e:
    print('FAIL - step 1315' if isinstance(e, AssertionError) else f'ERROR - step 1315: {e}')

print("STEP 1316 - Check element div#None.['c-custom-info-banner-v2__container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__container']")))
    print('PASS - step 1316')
except Exception as e:
    print('FAIL - step 1316' if isinstance(e, AssertionError) else f'ERROR - step 1316: {e}')

print("STEP 1317 - Check element div#None.['c-custom-info-banner-v2__content', 'container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__content', 'container']")))
    print('PASS - step 1317')
except Exception as e:
    print('FAIL - step 1317' if isinstance(e, AssertionError) else f'ERROR - step 1317: {e}')

print("STEP 1318 - Check element div#None.['c-custom-info-banner-v2__content--inner']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__content--inner']")))
    print('PASS - step 1318')
except Exception as e:
    print('FAIL - step 1318' if isinstance(e, AssertionError) else f'ERROR - step 1318: {e}')

print("STEP 1319 - Check element div#None.['c-custom-info-banner-v2__header--title-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--title-wrapper']")))
    print('PASS - step 1319')
except Exception as e:
    print('FAIL - step 1319' if isinstance(e, AssertionError) else f'ERROR - step 1319: {e}')

print("STEP 1320 - Check element div#None.['c-custom-info-banner-v2__header--title', 'xxl', 'reset-list', 'no-default-list-spacings', 'extra-indented']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--title', 'xxl', 'reset-list', 'no-default-list-spacings', 'extra-indented']")))
    print('PASS - step 1320')
except Exception as e:
    print('FAIL - step 1320' if isinstance(e, AssertionError) else f'ERROR - step 1320: {e}')

print("STEP 1321 - Check element div#None.['c-custom-info-banner-v2__header--subtitle-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--subtitle-wrapper']")))
    print('PASS - step 1321')
except Exception as e:
    print('FAIL - step 1321' if isinstance(e, AssertionError) else f'ERROR - step 1321: {e}')

print("STEP 1322 - Check element div#None.['c-custom-info-banner-v2__header--subtitle', 'h2', 'reset-list', 'no-default-list-spacings', 'extra-indented']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--subtitle', 'h2', 'reset-list', 'no-default-list-spacings', 'extra-indented']")))
    print('PASS - step 1322')
except Exception as e:
    print('FAIL - step 1322' if isinstance(e, AssertionError) else f'ERROR - step 1322: {e}')

print("STEP 1323 - Check element div#None.['c-custom-info-banner-v2__content--components-list']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__content--components-list']")))
    print('PASS - step 1323')
except Exception as e:
    print('FAIL - step 1323' if isinstance(e, AssertionError) else f'ERROR - step 1323: {e}')

print("STEP 1324 - Check element div#None.['ctadropdownbutton']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ctadropdownbutton']")))
    print('PASS - step 1324')
except Exception as e:
    print('FAIL - step 1324' if isinstance(e, AssertionError) else f'ERROR - step 1324: {e}')

print("STEP 1325 - Check element div#None.['cta-dropdown-button', 'text-left', 'inline-container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['cta-dropdown-button', 'text-left', 'inline-container']")))
    print('PASS - step 1325')
except Exception as e:
    print('FAIL - step 1325' if isinstance(e, AssertionError) else f'ERROR - step 1325: {e}')

print("STEP 1326 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1326')
except Exception as e:
    print('FAIL - step 1326' if isinstance(e, AssertionError) else f'ERROR - step 1326: {e}')

print("STEP 1327 - Check element a#id28b4a774767b71f2fcb4fd11c6e156a175cb93cd3713174afe9fd1fcfef7176b.['c-button', 'append-misc-url-params']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id28b4a774767b71f2fcb4fd11c6e156a175cb93cd3713174afe9fd1fcfef7176b")))
    print('PASS - step 1327')
except Exception as e:
    print('FAIL - step 1327' if isinstance(e, AssertionError) else f'ERROR - step 1327: {e}')

print("STEP 1328 - Check element span#None.['c-button__text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-button__text']")))
    print('PASS - step 1328')
except Exception as e:
    print('FAIL - step 1328' if isinstance(e, AssertionError) else f'ERROR - step 1328: {e}')

print("STEP 1329 - Check element p#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "p")))
    print('PASS - step 1329')
except Exception as e:
    print('FAIL - step 1329' if isinstance(e, AssertionError) else f'ERROR - step 1329: {e}')

print("STEP 1330 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1330')
except Exception as e:
    print('FAIL - step 1330' if isinstance(e, AssertionError) else f'ERROR - step 1330: {e}')

print("STEP 1331 - Check element a#id104d9403578a72b173f5e594d27adbc38c38d7d0459edebbfd8808949da2ebfb.['c-button', 'append-misc-url-params']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id104d9403578a72b173f5e594d27adbc38c38d7d0459edebbfd8808949da2ebfb")))
    print('PASS - step 1331')
except Exception as e:
    print('FAIL - step 1331' if isinstance(e, AssertionError) else f'ERROR - step 1331: {e}')

print("STEP 1332 - Check element span#None.['c-button__text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-button__text']")))
    print('PASS - step 1332')
except Exception as e:
    print('FAIL - step 1332' if isinstance(e, AssertionError) else f'ERROR - step 1332: {e}')

print("STEP 1333 - Check element p#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "p")))
    print('PASS - step 1333')
except Exception as e:
    print('FAIL - step 1333' if isinstance(e, AssertionError) else f'ERROR - step 1333: {e}')

print("STEP 1334 - Check element div#None.['c-custom-info-banner-v2__media']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__media']")))
    print('PASS - step 1334')
except Exception as e:
    print('FAIL - step 1334' if isinstance(e, AssertionError) else f'ERROR - step 1334: {e}')

print("STEP 1335 - Check element div#None.['c-image-v2', 'image-v2-9ba8a960-24']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2', 'image-v2-9ba8a960-24']")))
    print('PASS - step 1335')
except Exception as e:
    print('FAIL - step 1335' if isinstance(e, AssertionError) else f'ERROR - step 1335: {e}')

print("STEP 1336 - Check element div#None.['c-image-v2__container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2__container']")))
    print('PASS - step 1336')
except Exception as e:
    print('FAIL - step 1336' if isinstance(e, AssertionError) else f'ERROR - step 1336: {e}')

print("STEP 1337 - Check element picture#None.['c-image-v2__wrp']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2__wrp']")))
    print('PASS - step 1337')
except Exception as e:
    print('FAIL - step 1337' if isinstance(e, AssertionError) else f'ERROR - step 1337: {e}')

print("STEP 1338 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1338')
except Exception as e:
    print('FAIL - step 1338' if isinstance(e, AssertionError) else f'ERROR - step 1338: {e}')

print("STEP 1339 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1339')
except Exception as e:
    print('FAIL - step 1339' if isinstance(e, AssertionError) else f'ERROR - step 1339: {e}')

print("STEP 1340 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1340')
except Exception as e:
    print('FAIL - step 1340' if isinstance(e, AssertionError) else f'ERROR - step 1340: {e}')

print("STEP 1341 - Check element img#None.['c-image-v2__img']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2__img']")))
    print('PASS - step 1341')
except Exception as e:
    print('FAIL - step 1341' if isinstance(e, AssertionError) else f'ERROR - step 1341: {e}')

print("STEP 1342 - Check element script#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "script")))
    print('PASS - step 1342')
except Exception as e:
    print('FAIL - step 1342' if isinstance(e, AssertionError) else f'ERROR - step 1342: {e}')

print("STEP 1343 - Check element div#None.['c-generic-carousel-slider__slide', 'swiper-slide', 'swiper-slide-duplicate', 'swiper-slide-duplicate-active']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-generic-carousel-slider__slide', 'swiper-slide', 'swiper-slide-duplicate', 'swiper-slide-duplicate-active']")))
    print('PASS - step 1343')
except Exception as e:
    print('FAIL - step 1343' if isinstance(e, AssertionError) else f'ERROR - step 1343: {e}')

print("STEP 1344 - Check element hp-generic-card#None.['c-generic-card']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-generic-card']")))
    print('PASS - step 1344')
except Exception as e:
    print('FAIL - step 1344' if isinstance(e, AssertionError) else f'ERROR - step 1344: {e}')

print("STEP 1345 - Check element div#None.['c-generic-card__image', 'c-video-container--container-fit']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-generic-card__image', 'c-video-container--container-fit']")))
    print('PASS - step 1345')
except Exception as e:
    print('FAIL - step 1345' if isinstance(e, AssertionError) else f'ERROR - step 1345: {e}')

print("STEP 1346 - Check element div#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "div")))
    print('PASS - step 1346')
except Exception as e:
    print('FAIL - step 1346' if isinstance(e, AssertionError) else f'ERROR - step 1346: {e}')

print("STEP 1347 - Check element div#None.['customInfoBanner']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['customInfoBanner']")))
    print('PASS - step 1347')
except Exception as e:
    print('FAIL - step 1347' if isinstance(e, AssertionError) else f'ERROR - step 1347: {e}')

print("STEP 1348 - Check element hp-custom-info-banner-v3#None.['js-hp-component', 'c-custom-info-banner-v3', 'check-footnotes-visibility', 'id0a4ceb7d60804a83fa38ee0f5df84d6aaeacecfd1280ff0f5b540b05e18def95', 'no-tablet-version', 'no-mobile-version', 'js-hp-component-initialized']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['js-hp-component', 'c-custom-info-banner-v3', 'check-footnotes-visibility', 'id0a4ceb7d60804a83fa38ee0f5df84d6aaeacecfd1280ff0f5b540b05e18def95', 'no-tablet-version', 'no-mobile-version', 'js-hp-component-initialized']")))
    print('PASS - step 1348')
except Exception as e:
    print('FAIL - step 1348' if isinstance(e, AssertionError) else f'ERROR - step 1348: {e}')

print("STEP 1349 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1349')
except Exception as e:
    print('FAIL - step 1349' if isinstance(e, AssertionError) else f'ERROR - step 1349: {e}')

print("STEP 1350 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 1350')
except Exception as e:
    print('FAIL - step 1350' if isinstance(e, AssertionError) else f'ERROR - step 1350: {e}')

print("STEP 1351 - Check element div#None.['general']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['general']")))
    print('PASS - step 1351')
except Exception as e:
    print('FAIL - step 1351' if isinstance(e, AssertionError) else f'ERROR - step 1351: {e}')

print("STEP 1352 - Check element hp-custom-info-banner-v2#None.['js-hp-component', 'c-custom-info-banner-v2', 'id4c4dac59d5aac38c9e0d23fc6e6c78f857a2c17b5e83e8f2a32e6c496a88b2c6', 'media-position-top', 'title-on-side', 'js-hp-component-initialized']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['js-hp-component', 'c-custom-info-banner-v2', 'id4c4dac59d5aac38c9e0d23fc6e6c78f857a2c17b5e83e8f2a32e6c496a88b2c6', 'media-position-top', 'title-on-side', 'js-hp-component-initialized']")))
    print('PASS - step 1352')
except Exception as e:
    print('FAIL - step 1352' if isinstance(e, AssertionError) else f'ERROR - step 1352: {e}')

print("STEP 1353 - Check element div#None.['c-custom-info-banner-v2__media', 'c-custom-info-banner-v2__media--cloned']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__media', 'c-custom-info-banner-v2__media--cloned']")))
    print('PASS - step 1353')
except Exception as e:
    print('FAIL - step 1353' if isinstance(e, AssertionError) else f'ERROR - step 1353: {e}')

print("STEP 1354 - Check element div#None.['c-image-v2', 'image-v2-898c8e3a-2']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2', 'image-v2-898c8e3a-2']")))
    print('PASS - step 1354')
except Exception as e:
    print('FAIL - step 1354' if isinstance(e, AssertionError) else f'ERROR - step 1354: {e}')

print("STEP 1355 - Check element div#None.['c-image-v2__container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2__container']")))
    print('PASS - step 1355')
except Exception as e:
    print('FAIL - step 1355' if isinstance(e, AssertionError) else f'ERROR - step 1355: {e}')

print("STEP 1356 - Check element picture#None.['c-image-v2__wrp']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2__wrp']")))
    print('PASS - step 1356')
except Exception as e:
    print('FAIL - step 1356' if isinstance(e, AssertionError) else f'ERROR - step 1356: {e}')

print("STEP 1357 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1357')
except Exception as e:
    print('FAIL - step 1357' if isinstance(e, AssertionError) else f'ERROR - step 1357: {e}')

print("STEP 1358 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1358')
except Exception as e:
    print('FAIL - step 1358' if isinstance(e, AssertionError) else f'ERROR - step 1358: {e}')

print("STEP 1359 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1359')
except Exception as e:
    print('FAIL - step 1359' if isinstance(e, AssertionError) else f'ERROR - step 1359: {e}')

print("STEP 1360 - Check element img#None.['c-image-v2__img']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2__img']")))
    print('PASS - step 1360')
except Exception as e:
    print('FAIL - step 1360' if isinstance(e, AssertionError) else f'ERROR - step 1360: {e}')

print("STEP 1361 - Check element div#None.['c-custom-info-banner-v2__header']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header']")))
    print('PASS - step 1361')
except Exception as e:
    print('FAIL - step 1361' if isinstance(e, AssertionError) else f'ERROR - step 1361: {e}')

print("STEP 1362 - Check element div#None.['c-custom-info-banner-v2__header--title-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--title-wrapper']")))
    print('PASS - step 1362')
except Exception as e:
    print('FAIL - step 1362' if isinstance(e, AssertionError) else f'ERROR - step 1362: {e}')

print("STEP 1363 - Check element div#None.['container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['container']")))
    print('PASS - step 1363')
except Exception as e:
    print('FAIL - step 1363' if isinstance(e, AssertionError) else f'ERROR - step 1363: {e}')

print("STEP 1364 - Check element div#None.['c-custom-info-banner-v2__header--title', 'xl', 'reset-list', 'no-default-list-spacings', 'extra-indented']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--title', 'xl', 'reset-list', 'no-default-list-spacings', 'extra-indented']")))
    print('PASS - step 1364')
except Exception as e:
    print('FAIL - step 1364' if isinstance(e, AssertionError) else f'ERROR - step 1364: {e}')

print("STEP 1365 - Check element br#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "br")))
    print('PASS - step 1365')
except Exception as e:
    print('FAIL - step 1365' if isinstance(e, AssertionError) else f'ERROR - step 1365: {e}')

print("STEP 1366 - Check element div#None.['c-custom-info-banner-v2__header--subtitle-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--subtitle-wrapper']")))
    print('PASS - step 1366')
except Exception as e:
    print('FAIL - step 1366' if isinstance(e, AssertionError) else f'ERROR - step 1366: {e}')

print("STEP 1367 - Check element div#None.['container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['container']")))
    print('PASS - step 1367')
except Exception as e:
    print('FAIL - step 1367' if isinstance(e, AssertionError) else f'ERROR - step 1367: {e}')

print("STEP 1368 - Check element div#None.['c-custom-info-banner-v2__header--subtitle', 'h2', 'reset-list', 'no-default-list-spacings', 'extra-indented']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--subtitle', 'h2', 'reset-list', 'no-default-list-spacings', 'extra-indented']")))
    print('PASS - step 1368')
except Exception as e:
    print('FAIL - step 1368' if isinstance(e, AssertionError) else f'ERROR - step 1368: {e}')

print("STEP 1369 - Check element div#None.['c-custom-info-banner-v2__container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__container']")))
    print('PASS - step 1369')
except Exception as e:
    print('FAIL - step 1369' if isinstance(e, AssertionError) else f'ERROR - step 1369: {e}')

print("STEP 1370 - Check element div#None.['c-custom-info-banner-v2__content', 'container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__content', 'container']")))
    print('PASS - step 1370')
except Exception as e:
    print('FAIL - step 1370' if isinstance(e, AssertionError) else f'ERROR - step 1370: {e}')

print("STEP 1371 - Check element div#None.['c-custom-info-banner-v2__content--inner']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__content--inner']")))
    print('PASS - step 1371')
except Exception as e:
    print('FAIL - step 1371' if isinstance(e, AssertionError) else f'ERROR - step 1371: {e}')

print("STEP 1372 - Check element div#None.['c-custom-info-banner-v2__header--title-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--title-wrapper']")))
    print('PASS - step 1372')
except Exception as e:
    print('FAIL - step 1372' if isinstance(e, AssertionError) else f'ERROR - step 1372: {e}')

print("STEP 1373 - Check element div#None.['c-custom-info-banner-v2__header--title', 'xl', 'reset-list', 'no-default-list-spacings', 'extra-indented']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--title', 'xl', 'reset-list', 'no-default-list-spacings', 'extra-indented']")))
    print('PASS - step 1373')
except Exception as e:
    print('FAIL - step 1373' if isinstance(e, AssertionError) else f'ERROR - step 1373: {e}')

print("STEP 1374 - Check element br#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "br")))
    print('PASS - step 1374')
except Exception as e:
    print('FAIL - step 1374' if isinstance(e, AssertionError) else f'ERROR - step 1374: {e}')

print("STEP 1375 - Check element div#None.['c-custom-info-banner-v2__header--subtitle-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--subtitle-wrapper']")))
    print('PASS - step 1375')
except Exception as e:
    print('FAIL - step 1375' if isinstance(e, AssertionError) else f'ERROR - step 1375: {e}')

print("STEP 1376 - Check element div#None.['c-custom-info-banner-v2__header--subtitle', 'h2', 'reset-list', 'no-default-list-spacings', 'extra-indented']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__header--subtitle', 'h2', 'reset-list', 'no-default-list-spacings', 'extra-indented']")))
    print('PASS - step 1376')
except Exception as e:
    print('FAIL - step 1376' if isinstance(e, AssertionError) else f'ERROR - step 1376: {e}')

print("STEP 1377 - Check element div#None.['c-custom-info-banner-v2__content--components-list']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__content--components-list']")))
    print('PASS - step 1377')
except Exception as e:
    print('FAIL - step 1377' if isinstance(e, AssertionError) else f'ERROR - step 1377: {e}')

print("STEP 1378 - Check element div#None.['titleAndText']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['titleAndText']")))
    print('PASS - step 1378')
except Exception as e:
    print('FAIL - step 1378' if isinstance(e, AssertionError) else f'ERROR - step 1378: {e}')

print("STEP 1379 - Check element div#None.['ctaGroup']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ctaGroup']")))
    print('PASS - step 1379')
except Exception as e:
    print('FAIL - step 1379' if isinstance(e, AssertionError) else f'ERROR - step 1379: {e}')

print("STEP 1380 - Check element div#None.['cta-group', 'inline-container', 'idc84249b717e379e0aea39fd256e190ca024e5a431b62e7932af4a66bffd3d69d']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['cta-group', 'inline-container', 'idc84249b717e379e0aea39fd256e190ca024e5a431b62e7932af4a66bffd3d69d']")))
    print('PASS - step 1380')
except Exception as e:
    print('FAIL - step 1380' if isinstance(e, AssertionError) else f'ERROR - step 1380: {e}')

print("STEP 1381 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1381')
except Exception as e:
    print('FAIL - step 1381' if isinstance(e, AssertionError) else f'ERROR - step 1381: {e}')

print("STEP 1382 - Check element div#None.['ctaButton']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ctaButton']")))
    print('PASS - step 1382')
except Exception as e:
    print('FAIL - step 1382' if isinstance(e, AssertionError) else f'ERROR - step 1382: {e}')

print("STEP 1383 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1383')
except Exception as e:
    print('FAIL - step 1383' if isinstance(e, AssertionError) else f'ERROR - step 1383: {e}')

print("STEP 1384 - Check element a#id4137bd87734b2616b01604876f8cf4e8773254c9d91412adf765561c41acbb9c.['c-button', 'append-misc-url-params']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id4137bd87734b2616b01604876f8cf4e8773254c9d91412adf765561c41acbb9c")))
    print('PASS - step 1384')
except Exception as e:
    print('FAIL - step 1384' if isinstance(e, AssertionError) else f'ERROR - step 1384: {e}')

print("STEP 1385 - Check element span#None.['c-button__text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-button__text']")))
    print('PASS - step 1385')
except Exception as e:
    print('FAIL - step 1385' if isinstance(e, AssertionError) else f'ERROR - step 1385: {e}')

print("STEP 1386 - Check element p#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "p")))
    print('PASS - step 1386')
except Exception as e:
    print('FAIL - step 1386' if isinstance(e, AssertionError) else f'ERROR - step 1386: {e}')

print("STEP 1387 - Check element div#None.['ctaButton']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ctaButton']")))
    print('PASS - step 1387')
except Exception as e:
    print('FAIL - step 1387' if isinstance(e, AssertionError) else f'ERROR - step 1387: {e}')

print("STEP 1388 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1388')
except Exception as e:
    print('FAIL - step 1388' if isinstance(e, AssertionError) else f'ERROR - step 1388: {e}')

print("STEP 1389 - Check element a#idaec6c56faa79d308dbd3ccd6193f7c575139b6894959b1e9fd7d5346f1eb92fd.['c-button-outline', 'append-misc-url-params']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "idaec6c56faa79d308dbd3ccd6193f7c575139b6894959b1e9fd7d5346f1eb92fd")))
    print('PASS - step 1389')
except Exception as e:
    print('FAIL - step 1389' if isinstance(e, AssertionError) else f'ERROR - step 1389: {e}')

print("STEP 1390 - Check element span#None.['c-button__text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-button__text']")))
    print('PASS - step 1390')
except Exception as e:
    print('FAIL - step 1390' if isinstance(e, AssertionError) else f'ERROR - step 1390: {e}')

print("STEP 1391 - Check element p#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "p")))
    print('PASS - step 1391')
except Exception as e:
    print('FAIL - step 1391' if isinstance(e, AssertionError) else f'ERROR - step 1391: {e}')

print("STEP 1392 - Check element div#None.['c-custom-info-banner-v2__media']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-custom-info-banner-v2__media']")))
    print('PASS - step 1392')
except Exception as e:
    print('FAIL - step 1392' if isinstance(e, AssertionError) else f'ERROR - step 1392: {e}')

print("STEP 1393 - Check element div#None.['c-image-v2', 'image-v2-5bb9b725-4']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2', 'image-v2-5bb9b725-4']")))
    print('PASS - step 1393')
except Exception as e:
    print('FAIL - step 1393' if isinstance(e, AssertionError) else f'ERROR - step 1393: {e}')

print("STEP 1394 - Check element div#None.['c-image-v2__container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2__container']")))
    print('PASS - step 1394')
except Exception as e:
    print('FAIL - step 1394' if isinstance(e, AssertionError) else f'ERROR - step 1394: {e}')

print("STEP 1395 - Check element picture#None.['c-image-v2__wrp']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2__wrp']")))
    print('PASS - step 1395')
except Exception as e:
    print('FAIL - step 1395' if isinstance(e, AssertionError) else f'ERROR - step 1395: {e}')

print("STEP 1396 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1396')
except Exception as e:
    print('FAIL - step 1396' if isinstance(e, AssertionError) else f'ERROR - step 1396: {e}')

print("STEP 1397 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1397')
except Exception as e:
    print('FAIL - step 1397' if isinstance(e, AssertionError) else f'ERROR - step 1397: {e}')

print("STEP 1398 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1398')
except Exception as e:
    print('FAIL - step 1398' if isinstance(e, AssertionError) else f'ERROR - step 1398: {e}')

print("STEP 1399 - Check element img#None.['c-image-v2__img']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2__img']")))
    print('PASS - step 1399')
except Exception as e:
    print('FAIL - step 1399' if isinstance(e, AssertionError) else f'ERROR - step 1399: {e}')

print("STEP 1400 - Check element script#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "script")))
    print('PASS - step 1400')
except Exception as e:
    print('FAIL - step 1400' if isinstance(e, AssertionError) else f'ERROR - step 1400: {e}')

print("STEP 1401 - Check element button#None.['swiper-arrow', 'c-icon', 'swiper-button-next']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['swiper-arrow', 'c-icon', 'swiper-button-next']")))
    print('PASS - step 1401')
except Exception as e:
    print('FAIL - step 1401' if isinstance(e, AssertionError) else f'ERROR - step 1401: {e}')

print("STEP 1402 - Check element span#None.['c-icon-regular-state']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-icon-regular-state']")))
    print('PASS - step 1402')
except Exception as e:
    print('FAIL - step 1402' if isinstance(e, AssertionError) else f'ERROR - step 1402: {e}')

print("STEP 1403 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 1403')
except Exception as e:
    print('FAIL - step 1403' if isinstance(e, AssertionError) else f'ERROR - step 1403: {e}')

print("STEP 1404 - Check element use#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "use")))
    print('PASS - step 1404')
except Exception as e:
    print('FAIL - step 1404' if isinstance(e, AssertionError) else f'ERROR - step 1404: {e}')

print("STEP 1405 - Check element span#None.['c-icon-hover-state']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-icon-hover-state']")))
    print('PASS - step 1405')
except Exception as e:
    print('FAIL - step 1405' if isinstance(e, AssertionError) else f'ERROR - step 1405: {e}')

print("STEP 1406 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 1406')
except Exception as e:
    print('FAIL - step 1406' if isinstance(e, AssertionError) else f'ERROR - step 1406: {e}')

print("STEP 1407 - Check element use#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "use")))
    print('PASS - step 1407')
except Exception as e:
    print('FAIL - step 1407' if isinstance(e, AssertionError) else f'ERROR - step 1407: {e}')

print("STEP 1408 - Check element div#None.['swiper-pagination', 'default-style', 'swiper-pagination-clickable', 'swiper-pagination-bullets']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['swiper-pagination', 'default-style', 'swiper-pagination-clickable', 'swiper-pagination-bullets']")))
    print('PASS - step 1408')
except Exception as e:
    print('FAIL - step 1408' if isinstance(e, AssertionError) else f'ERROR - step 1408: {e}')

print("STEP 1409 - Check element span#None.['swiper-pagination-bullet', 'swiper-pagination-bullet-active']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['swiper-pagination-bullet', 'swiper-pagination-bullet-active']")))
    print('PASS - step 1409')
except Exception as e:
    print('FAIL - step 1409' if isinstance(e, AssertionError) else f'ERROR - step 1409: {e}')

print("STEP 1410 - Check element span#None.['swiper-pagination-bullet']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['swiper-pagination-bullet']")))
    print('PASS - step 1410')
except Exception as e:
    print('FAIL - step 1410' if isinstance(e, AssertionError) else f'ERROR - step 1410: {e}')

print("STEP 1411 - Check element span#None.['swiper-pagination-bullet']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['swiper-pagination-bullet']")))
    print('PASS - step 1411')
except Exception as e:
    print('FAIL - step 1411' if isinstance(e, AssertionError) else f'ERROR - step 1411: {e}')

print("STEP 1412 - Check element span#None.['swiper-pagination-bullet']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['swiper-pagination-bullet']")))
    print('PASS - step 1412')
except Exception as e:
    print('FAIL - step 1412' if isinstance(e, AssertionError) else f'ERROR - step 1412: {e}')

print("STEP 1413 - Check element span#None.['swiper-pagination-bullet']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['swiper-pagination-bullet']")))
    print('PASS - step 1413')
except Exception as e:
    print('FAIL - step 1413' if isinstance(e, AssertionError) else f'ERROR - step 1413: {e}')

print("STEP 1414 - Check element span#None.['swiper-pagination-bullet']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['swiper-pagination-bullet']")))
    print('PASS - step 1414')
except Exception as e:
    print('FAIL - step 1414' if isinstance(e, AssertionError) else f'ERROR - step 1414: {e}')

print("STEP 1415 - Check element span#None.['swiper-notification']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['swiper-notification']")))
    print('PASS - step 1415')
except Exception as e:
    print('FAIL - step 1415' if isinstance(e, AssertionError) else f'ERROR - step 1415: {e}')

print("STEP 1416 - Check element div#None.['spacing', 'aem-GridColumn', 'aem-GridColumn--default--12']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['spacing', 'aem-GridColumn', 'aem-GridColumn--default--12']")))
    print('PASS - step 1416')
except Exception as e:
    print('FAIL - step 1416' if isinstance(e, AssertionError) else f'ERROR - step 1416: {e}')

print("STEP 1417 - Check element div#None.['visualTabs', 'aem-GridColumn', 'aem-GridColumn--default--12']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['visualTabs', 'aem-GridColumn', 'aem-GridColumn--default--12']")))
    print('PASS - step 1417')
except Exception as e:
    print('FAIL - step 1417' if isinstance(e, AssertionError) else f'ERROR - step 1417: {e}')

print("STEP 1418 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1418')
except Exception as e:
    print('FAIL - step 1418' if isinstance(e, AssertionError) else f'ERROR - step 1418: {e}')

print("STEP 1419 - Check element hp-visual-tabs#None.['js-hp-component', 'c-visual-tabs', 'square', 'id2b7015af78773ef014c202a938657cdb5d1633f6788f29f9352652715812b4e4', 'js-hp-component-initialized']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['js-hp-component', 'c-visual-tabs', 'square', 'id2b7015af78773ef014c202a938657cdb5d1633f6788f29f9352652715812b4e4', 'js-hp-component-initialized']")))
    print('PASS - step 1419')
except Exception as e:
    print('FAIL - step 1419' if isinstance(e, AssertionError) else f'ERROR - step 1419: {e}')

print("STEP 1420 - Check element div#None.['c-visual-tabs__pre']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-visual-tabs__pre']")))
    print('PASS - step 1420')
except Exception as e:
    print('FAIL - step 1420' if isinstance(e, AssertionError) else f'ERROR - step 1420: {e}')

print("STEP 1421 - Check element div#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "div")))
    print('PASS - step 1421')
except Exception as e:
    print('FAIL - step 1421' if isinstance(e, AssertionError) else f'ERROR - step 1421: {e}')

print("STEP 1422 - Check element div#None.['titleAndText']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['titleAndText']")))
    print('PASS - step 1422')
except Exception as e:
    print('FAIL - step 1422' if isinstance(e, AssertionError) else f'ERROR - step 1422: {e}')

print("STEP 1423 - Check element hp-title-and-text#None.['c-title-and-text__wrapper', 'font-']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-title-and-text__wrapper', 'font-']")))
    print('PASS - step 1423')
except Exception as e:
    print('FAIL - step 1423' if isinstance(e, AssertionError) else f'ERROR - step 1423: {e}')

print("STEP 1424 - Check element div#None.['c-title-and-text', 'c-title-and-text--text-left', 'bg-', 'font-black', 'id_text_title_id50088e5c650fd73f2b78f5f63755e1a2065b275fa2dc0d4f4d192606958bbc05']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-title-and-text', 'c-title-and-text--text-left', 'bg-', 'font-black', 'id_text_title_id50088e5c650fd73f2b78f5f63755e1a2065b275fa2dc0d4f4d192606958bbc05']")))
    print('PASS - step 1424')
except Exception as e:
    print('FAIL - step 1424' if isinstance(e, AssertionError) else f'ERROR - step 1424: {e}')

print("STEP 1425 - Check element div#None.['c-title-and-text__title']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-title-and-text__title']")))
    print('PASS - step 1425')
except Exception as e:
    print('FAIL - step 1425' if isinstance(e, AssertionError) else f'ERROR - step 1425: {e}')

print("STEP 1426 - Check element h2#None.['xl']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['xl']")))
    print('PASS - step 1426')
except Exception as e:
    print('FAIL - step 1426' if isinstance(e, AssertionError) else f'ERROR - step 1426: {e}')

print("STEP 1427 - Check element div#None.['divider']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['divider']")))
    print('PASS - step 1427')
except Exception as e:
    print('FAIL - step 1427' if isinstance(e, AssertionError) else f'ERROR - step 1427: {e}')

print("STEP 1428 - Check element div#id85cec3dfc6e3fd0e3baf4527297dfedf8fedca4815ee433864a74601f4943912.['c-divider']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id85cec3dfc6e3fd0e3baf4527297dfedf8fedca4815ee433864a74601f4943912")))
    print('PASS - step 1428')
except Exception as e:
    print('FAIL - step 1428' if isinstance(e, AssertionError) else f'ERROR - step 1428: {e}')

print("STEP 1429 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1429')
except Exception as e:
    print('FAIL - step 1429' if isinstance(e, AssertionError) else f'ERROR - step 1429: {e}')

print("STEP 1430 - Check element div#None.['c-divider-inner']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-divider-inner']")))
    print('PASS - step 1430')
except Exception as e:
    print('FAIL - step 1430' if isinstance(e, AssertionError) else f'ERROR - step 1430: {e}')

print("STEP 1431 - Check element div#None.['titleAndText']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['titleAndText']")))
    print('PASS - step 1431')
except Exception as e:
    print('FAIL - step 1431' if isinstance(e, AssertionError) else f'ERROR - step 1431: {e}')

print("STEP 1432 - Check element hp-title-and-text#None.['c-title-and-text__wrapper', 'font-']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-title-and-text__wrapper', 'font-']")))
    print('PASS - step 1432')
except Exception as e:
    print('FAIL - step 1432' if isinstance(e, AssertionError) else f'ERROR - step 1432: {e}')

print("STEP 1433 - Check element div#None.['c-title-and-text', 'c-title-and-text--text-left', 'bg-', 'font-black', 'id_text_title_id06ae57c44284d5ca8db1e8b8d6a20226a783c59c900de25a5be1507069436aea']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-title-and-text', 'c-title-and-text--text-left', 'bg-', 'font-black', 'id_text_title_id06ae57c44284d5ca8db1e8b8d6a20226a783c59c900de25a5be1507069436aea']")))
    print('PASS - step 1433')
except Exception as e:
    print('FAIL - step 1433' if isinstance(e, AssertionError) else f'ERROR - step 1433: {e}')

print("STEP 1434 - Check element div#None.['c-title-and-text__title']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-title-and-text__title']")))
    print('PASS - step 1434')
except Exception as e:
    print('FAIL - step 1434' if isinstance(e, AssertionError) else f'ERROR - step 1434: {e}')

print("STEP 1435 - Check element h2#None.['h2']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['h2']")))
    print('PASS - step 1435')
except Exception as e:
    print('FAIL - step 1435' if isinstance(e, AssertionError) else f'ERROR - step 1435: {e}')

print("STEP 1436 - Check element div#None.['spacing']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['spacing']")))
    print('PASS - step 1436')
except Exception as e:
    print('FAIL - step 1436' if isinstance(e, AssertionError) else f'ERROR - step 1436: {e}')

print("STEP 1437 - Check element div#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "div")))
    print('PASS - step 1437')
except Exception as e:
    print('FAIL - step 1437' if isinstance(e, AssertionError) else f'ERROR - step 1437: {e}')

print("STEP 1438 - Check element div#None.['spacing-20', 'hide-on-mobile']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['spacing-20', 'hide-on-mobile']")))
    print('PASS - step 1438')
except Exception as e:
    print('FAIL - step 1438' if isinstance(e, AssertionError) else f'ERROR - step 1438: {e}')

print("STEP 1439 - Check element span#None.['hidden']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['hidden']")))
    print('PASS - step 1439')
except Exception as e:
    print('FAIL - step 1439' if isinstance(e, AssertionError) else f'ERROR - step 1439: {e}')

print("STEP 1440 - Check element div#None.['spacing-20', 'show-on-mobile']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['spacing-20', 'show-on-mobile']")))
    print('PASS - step 1440')
except Exception as e:
    print('FAIL - step 1440' if isinstance(e, AssertionError) else f'ERROR - step 1440: {e}')

print("STEP 1441 - Check element span#None.['hidden']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['hidden']")))
    print('PASS - step 1441')
except Exception as e:
    print('FAIL - step 1441' if isinstance(e, AssertionError) else f'ERROR - step 1441: {e}')

print("STEP 1442 - Check element hp-grid#None.['js-hp-component', 'hp-grid', 'js-hp-component-initialized']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['js-hp-component', 'hp-grid', 'js-hp-component-initialized']")))
    print('PASS - step 1442')
except Exception as e:
    print('FAIL - step 1442' if isinstance(e, AssertionError) else f'ERROR - step 1442: {e}')

print("STEP 1443 - Check element div#None.['container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['container']")))
    print('PASS - step 1443')
except Exception as e:
    print('FAIL - step 1443' if isinstance(e, AssertionError) else f'ERROR - step 1443: {e}')

print("STEP 1444 - Check element div#None.['row', 'swiper--ignore-auto-margins', 'c-visual-tabs__row-items']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['row', 'swiper--ignore-auto-margins', 'c-visual-tabs__row-items']")))
    print('PASS - step 1444')
except Exception as e:
    print('FAIL - step 1444' if isinstance(e, AssertionError) else f'ERROR - step 1444: {e}')

print("STEP 1445 - Check element div#None.['c-grid-cell', 'col-md-4', 'c-card-carousel-slide', 'c-visual-tabs__grid-cell']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-grid-cell', 'col-md-4', 'c-card-carousel-slide', 'c-visual-tabs__grid-cell']")))
    print('PASS - step 1445')
except Exception as e:
    print('FAIL - step 1445' if isinstance(e, AssertionError) else f'ERROR - step 1445: {e}')

print("STEP 1446 - Check element div#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "div")))
    print('PASS - step 1446')
except Exception as e:
    print('FAIL - step 1446' if isinstance(e, AssertionError) else f'ERROR - step 1446: {e}')

print("STEP 1447 - Check element hp-visual-tabs-item#None.['c-visual-tabs-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-visual-tabs-item']")))
    print('PASS - step 1447')
except Exception as e:
    print('FAIL - step 1447' if isinstance(e, AssertionError) else f'ERROR - step 1447: {e}')

print("STEP 1448 - Check element div#None.['c-visual-tabs-item__trigger', 'hover-play']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-visual-tabs-item__trigger', 'hover-play']")))
    print('PASS - step 1448')
except Exception as e:
    print('FAIL - step 1448' if isinstance(e, AssertionError) else f'ERROR - step 1448: {e}')

print("STEP 1449 - Check element div#None.['c-visual-tabs-item__img']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-visual-tabs-item__img']")))
    print('PASS - step 1449')
except Exception as e:
    print('FAIL - step 1449' if isinstance(e, AssertionError) else f'ERROR - step 1449: {e}')

print("STEP 1450 - Check element div#id_image_id24de085d5e928256368032ba6868868b45f1ee87400062f9ef3bf7083b892bac.['c-image-v2', 'image-v2-8e78ceb9-26']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id_image_id24de085d5e928256368032ba6868868b45f1ee87400062f9ef3bf7083b892bac")))
    print('PASS - step 1450')
except Exception as e:
    print('FAIL - step 1450' if isinstance(e, AssertionError) else f'ERROR - step 1450: {e}')

print("STEP 1451 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1451')
except Exception as e:
    print('FAIL - step 1451' if isinstance(e, AssertionError) else f'ERROR - step 1451: {e}')

print("STEP 1452 - Check element div#None.['c-image-v2__container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2__container']")))
    print('PASS - step 1452')
except Exception as e:
    print('FAIL - step 1452' if isinstance(e, AssertionError) else f'ERROR - step 1452: {e}')

print("STEP 1453 - Check element picture#None.['c-image-v2__wrp']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2__wrp']")))
    print('PASS - step 1453')
except Exception as e:
    print('FAIL - step 1453' if isinstance(e, AssertionError) else f'ERROR - step 1453: {e}')

print("STEP 1454 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1454')
except Exception as e:
    print('FAIL - step 1454' if isinstance(e, AssertionError) else f'ERROR - step 1454: {e}')

print("STEP 1455 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1455')
except Exception as e:
    print('FAIL - step 1455' if isinstance(e, AssertionError) else f'ERROR - step 1455: {e}')

print("STEP 1456 - Check element img#None.['c-image-v2__img']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2__img']")))
    print('PASS - step 1456')
except Exception as e:
    print('FAIL - step 1456' if isinstance(e, AssertionError) else f'ERROR - step 1456: {e}')

print("STEP 1457 - Check element div#None.['c-visual-tabs-item__desc']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-visual-tabs-item__desc']")))
    print('PASS - step 1457')
except Exception as e:
    print('FAIL - step 1457' if isinstance(e, AssertionError) else f'ERROR - step 1457: {e}')

print("STEP 1458 - Check element h3#None.['h3']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['h3']")))
    print('PASS - step 1458')
except Exception as e:
    print('FAIL - step 1458' if isinstance(e, AssertionError) else f'ERROR - step 1458: {e}')

print("STEP 1459 - Check element div#None.['c-grid-cell', 'col-md-4', 'c-card-carousel-slide', 'c-visual-tabs__grid-cell']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-grid-cell', 'col-md-4', 'c-card-carousel-slide', 'c-visual-tabs__grid-cell']")))
    print('PASS - step 1459')
except Exception as e:
    print('FAIL - step 1459' if isinstance(e, AssertionError) else f'ERROR - step 1459: {e}')

print("STEP 1460 - Check element div#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "div")))
    print('PASS - step 1460')
except Exception as e:
    print('FAIL - step 1460' if isinstance(e, AssertionError) else f'ERROR - step 1460: {e}')

print("STEP 1461 - Check element hp-visual-tabs-item#None.['c-visual-tabs-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-visual-tabs-item']")))
    print('PASS - step 1461')
except Exception as e:
    print('FAIL - step 1461' if isinstance(e, AssertionError) else f'ERROR - step 1461: {e}')

print("STEP 1462 - Check element div#None.['c-visual-tabs-item__trigger', 'hover-play']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-visual-tabs-item__trigger', 'hover-play']")))
    print('PASS - step 1462')
except Exception as e:
    print('FAIL - step 1462' if isinstance(e, AssertionError) else f'ERROR - step 1462: {e}')

print("STEP 1463 - Check element div#None.['c-visual-tabs-item__img']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-visual-tabs-item__img']")))
    print('PASS - step 1463')
except Exception as e:
    print('FAIL - step 1463' if isinstance(e, AssertionError) else f'ERROR - step 1463: {e}')

print("STEP 1464 - Check element div#id_image_id251333c63f0c1e670ed05db5b740e3fd84aac9ccd5feced3b504861293e3606e.['c-image-v2', 'image-v2-199fa9e4-28']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id_image_id251333c63f0c1e670ed05db5b740e3fd84aac9ccd5feced3b504861293e3606e")))
    print('PASS - step 1464')
except Exception as e:
    print('FAIL - step 1464' if isinstance(e, AssertionError) else f'ERROR - step 1464: {e}')

print("STEP 1465 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1465')
except Exception as e:
    print('FAIL - step 1465' if isinstance(e, AssertionError) else f'ERROR - step 1465: {e}')

print("STEP 1466 - Check element div#None.['c-image-v2__container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2__container']")))
    print('PASS - step 1466')
except Exception as e:
    print('FAIL - step 1466' if isinstance(e, AssertionError) else f'ERROR - step 1466: {e}')

print("STEP 1467 - Check element picture#None.['c-image-v2__wrp']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2__wrp']")))
    print('PASS - step 1467')
except Exception as e:
    print('FAIL - step 1467' if isinstance(e, AssertionError) else f'ERROR - step 1467: {e}')

print("STEP 1468 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1468')
except Exception as e:
    print('FAIL - step 1468' if isinstance(e, AssertionError) else f'ERROR - step 1468: {e}')

print("STEP 1469 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1469')
except Exception as e:
    print('FAIL - step 1469' if isinstance(e, AssertionError) else f'ERROR - step 1469: {e}')

print("STEP 1470 - Check element img#None.['c-image-v2__img']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2__img']")))
    print('PASS - step 1470')
except Exception as e:
    print('FAIL - step 1470' if isinstance(e, AssertionError) else f'ERROR - step 1470: {e}')

print("STEP 1471 - Check element div#None.['c-visual-tabs-item__desc']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-visual-tabs-item__desc']")))
    print('PASS - step 1471')
except Exception as e:
    print('FAIL - step 1471' if isinstance(e, AssertionError) else f'ERROR - step 1471: {e}')

print("STEP 1472 - Check element h3#None.['h3']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['h3']")))
    print('PASS - step 1472')
except Exception as e:
    print('FAIL - step 1472' if isinstance(e, AssertionError) else f'ERROR - step 1472: {e}')

print("STEP 1473 - Check element div#None.['c-grid-cell', 'col-md-4', 'c-card-carousel-slide', 'c-visual-tabs__grid-cell']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-grid-cell', 'col-md-4', 'c-card-carousel-slide', 'c-visual-tabs__grid-cell']")))
    print('PASS - step 1473')
except Exception as e:
    print('FAIL - step 1473' if isinstance(e, AssertionError) else f'ERROR - step 1473: {e}')

print("STEP 1474 - Check element div#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "div")))
    print('PASS - step 1474')
except Exception as e:
    print('FAIL - step 1474' if isinstance(e, AssertionError) else f'ERROR - step 1474: {e}')

print("STEP 1475 - Check element hp-visual-tabs-item#None.['c-visual-tabs-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-visual-tabs-item']")))
    print('PASS - step 1475')
except Exception as e:
    print('FAIL - step 1475' if isinstance(e, AssertionError) else f'ERROR - step 1475: {e}')

print("STEP 1476 - Check element div#None.['c-visual-tabs-item__trigger', 'hover-play']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-visual-tabs-item__trigger', 'hover-play']")))
    print('PASS - step 1476')
except Exception as e:
    print('FAIL - step 1476' if isinstance(e, AssertionError) else f'ERROR - step 1476: {e}')

print("STEP 1477 - Check element div#None.['c-visual-tabs-item__img']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-visual-tabs-item__img']")))
    print('PASS - step 1477')
except Exception as e:
    print('FAIL - step 1477' if isinstance(e, AssertionError) else f'ERROR - step 1477: {e}')

print("STEP 1478 - Check element div#id_image_idc858081acc10195d41e9678b78b9a85ba014218dda20e749200495f935c8df66.['c-image-v2', 'image-v2-9b28bb8a-30']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id_image_idc858081acc10195d41e9678b78b9a85ba014218dda20e749200495f935c8df66")))
    print('PASS - step 1478')
except Exception as e:
    print('FAIL - step 1478' if isinstance(e, AssertionError) else f'ERROR - step 1478: {e}')

print("STEP 1479 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1479')
except Exception as e:
    print('FAIL - step 1479' if isinstance(e, AssertionError) else f'ERROR - step 1479: {e}')

print("STEP 1480 - Check element div#None.['c-image-v2__container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2__container']")))
    print('PASS - step 1480')
except Exception as e:
    print('FAIL - step 1480' if isinstance(e, AssertionError) else f'ERROR - step 1480: {e}')

print("STEP 1481 - Check element picture#None.['c-image-v2__wrp']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2__wrp']")))
    print('PASS - step 1481')
except Exception as e:
    print('FAIL - step 1481' if isinstance(e, AssertionError) else f'ERROR - step 1481: {e}')

print("STEP 1482 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1482')
except Exception as e:
    print('FAIL - step 1482' if isinstance(e, AssertionError) else f'ERROR - step 1482: {e}')

print("STEP 1483 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1483')
except Exception as e:
    print('FAIL - step 1483' if isinstance(e, AssertionError) else f'ERROR - step 1483: {e}')

print("STEP 1484 - Check element img#None.['c-image-v2__img']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-image-v2__img']")))
    print('PASS - step 1484')
except Exception as e:
    print('FAIL - step 1484' if isinstance(e, AssertionError) else f'ERROR - step 1484: {e}')

print("STEP 1485 - Check element div#None.['c-visual-tabs-item__desc']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-visual-tabs-item__desc']")))
    print('PASS - step 1485')
except Exception as e:
    print('FAIL - step 1485' if isinstance(e, AssertionError) else f'ERROR - step 1485: {e}')

print("STEP 1486 - Check element h3#None.['h3']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['h3']")))
    print('PASS - step 1486')
except Exception as e:
    print('FAIL - step 1486' if isinstance(e, AssertionError) else f'ERROR - step 1486: {e}')

print("STEP 1487 - Check element div#None.['c-visual-tabs__content', 'container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-visual-tabs__content', 'container']")))
    print('PASS - step 1487')
except Exception as e:
    print('FAIL - step 1487' if isinstance(e, AssertionError) else f'ERROR - step 1487: {e}')

print("STEP 1488 - Check element div#None.['c-visual-tabs-item__content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-visual-tabs-item__content']")))
    print('PASS - step 1488')
except Exception as e:
    print('FAIL - step 1488' if isinstance(e, AssertionError) else f'ERROR - step 1488: {e}')

print("STEP 1489 - Check element div#None.['grid']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['grid']")))
    print('PASS - step 1489')
except Exception as e:
    print('FAIL - step 1489' if isinstance(e, AssertionError) else f'ERROR - step 1489: {e}')

print("STEP 1490 - Check element hp-grid#None.['js-hp-component', 'hp-grid', 'id_gridc94f0bc20b5c4f58b6de73b6d6ad9a0a', 'js-hp-component-initialized']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['js-hp-component', 'hp-grid', 'id_gridc94f0bc20b5c4f58b6de73b6d6ad9a0a', 'js-hp-component-initialized']")))
    print('PASS - step 1490')
except Exception as e:
    print('FAIL - step 1490' if isinstance(e, AssertionError) else f'ERROR - step 1490: {e}')

print("STEP 1491 - Check element div#None.['container', 'id_grid_container0f3c34da795447b4b35843797324e707']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['container', 'id_grid_container0f3c34da795447b4b35843797324e707']")))
    print('PASS - step 1491')
except Exception as e:
    print('FAIL - step 1491' if isinstance(e, AssertionError) else f'ERROR - step 1491: {e}')

print("STEP 1492 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1492')
except Exception as e:
    print('FAIL - step 1492' if isinstance(e, AssertionError) else f'ERROR - step 1492: {e}')

print("STEP 1493 - Check element div#None.['row', 'justify-content-center', 'justify-content-lg-center', 'justify-content-md-center']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['row', 'justify-content-center', 'justify-content-lg-center', 'justify-content-md-center']")))
    print('PASS - step 1493')
except Exception as e:
    print('FAIL - step 1493' if isinstance(e, AssertionError) else f'ERROR - step 1493: {e}')

print("STEP 1494 - Check element div#None.['c-grid-cell', 'col-lg-4', 'col-md-6', 'col-sm-12', 'cell-id_grid_cell5604ff369bedc30c44ab30f37f30ffccb3451bea31397feb2be481f80ac1c5f4']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-grid-cell', 'col-lg-4', 'col-md-6', 'col-sm-12', 'cell-id_grid_cell5604ff369bedc30c44ab30f37f30ffccb3451bea31397feb2be481f80ac1c5f4']")))
    print('PASS - step 1494')
except Exception as e:
    print('FAIL - step 1494' if isinstance(e, AssertionError) else f'ERROR - step 1494: {e}')

print("STEP 1495 - Check element div#None.['image']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['image']")))
    print('PASS - step 1495')
except Exception as e:
    print('FAIL - step 1495' if isinstance(e, AssertionError) else f'ERROR - step 1495: {e}')

print("STEP 1496 - Check element div#id_image_id99b32fc03a971d3cc5fc0bef2ef67e09261216ffa31920a52caeeaf5b0e39cd6.['c-image-container', 'cmp-image', 'c-image-container--align-left']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id_image_id99b32fc03a971d3cc5fc0bef2ef67e09261216ffa31920a52caeeaf5b0e39cd6")))
    print('PASS - step 1496')
except Exception as e:
    print('FAIL - step 1496' if isinstance(e, AssertionError) else f'ERROR - step 1496: {e}')

print("STEP 1497 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1497')
except Exception as e:
    print('FAIL - step 1497' if isinstance(e, AssertionError) else f'ERROR - step 1497: {e}')

print("STEP 1498 - Check element hp-image#None.['no-fade', 'c-image']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['no-fade', 'c-image']")))
    print('PASS - step 1498')
except Exception as e:
    print('FAIL - step 1498' if isinstance(e, AssertionError) else f'ERROR - step 1498: {e}')

print("STEP 1499 - Check element div#None.['titleAndText']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['titleAndText']")))
    print('PASS - step 1499')
except Exception as e:
    print('FAIL - step 1499' if isinstance(e, AssertionError) else f'ERROR - step 1499: {e}')

print("STEP 1500 - Check element hp-title-and-text#None.['c-title-and-text__wrapper', 'font-']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-title-and-text__wrapper', 'font-']")))
    print('PASS - step 1500')
except Exception as e:
    print('FAIL - step 1500' if isinstance(e, AssertionError) else f'ERROR - step 1500: {e}')

print("STEP 1501 - Check element div#None.['c-title-and-text', 'c-title-and-text--text-left', 'bg-', 'font-black', 'id_text_title_idb1eec74a0dc958cc43e829c1a233e0ae932c13b0fc16c1c20b310c0cfe1d09a1']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-title-and-text', 'c-title-and-text--text-left', 'bg-', 'font-black', 'id_text_title_idb1eec74a0dc958cc43e829c1a233e0ae932c13b0fc16c1c20b310c0cfe1d09a1']")))
    print('PASS - step 1501')
except Exception as e:
    print('FAIL - step 1501' if isinstance(e, AssertionError) else f'ERROR - step 1501: {e}')

print("STEP 1502 - Check element div#None.['c-title-and-text__title']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-title-and-text__title']")))
    print('PASS - step 1502')
except Exception as e:
    print('FAIL - step 1502' if isinstance(e, AssertionError) else f'ERROR - step 1502: {e}')

print("STEP 1503 - Check element h4#None.['h4']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['h4']")))
    print('PASS - step 1503')
except Exception as e:
    print('FAIL - step 1503' if isinstance(e, AssertionError) else f'ERROR - step 1503: {e}')

print("STEP 1504 - Check element div#None.['ctadropdownbutton']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ctadropdownbutton']")))
    print('PASS - step 1504')
except Exception as e:
    print('FAIL - step 1504' if isinstance(e, AssertionError) else f'ERROR - step 1504: {e}')

print("STEP 1505 - Check element div#None.['cta-dropdown-button', 'text-left', 'inline-container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['cta-dropdown-button', 'text-left', 'inline-container']")))
    print('PASS - step 1505')
except Exception as e:
    print('FAIL - step 1505' if isinstance(e, AssertionError) else f'ERROR - step 1505: {e}')

print("STEP 1506 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1506')
except Exception as e:
    print('FAIL - step 1506' if isinstance(e, AssertionError) else f'ERROR - step 1506: {e}')

print("STEP 1507 - Check element a#id152c34997515f485bbc64411b501b78ea1080edf1abe1621e12850f0d857a56e.['c-button', 'append-misc-url-params']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id152c34997515f485bbc64411b501b78ea1080edf1abe1621e12850f0d857a56e")))
    print('PASS - step 1507')
except Exception as e:
    print('FAIL - step 1507' if isinstance(e, AssertionError) else f'ERROR - step 1507: {e}')

print("STEP 1508 - Check element span#None.['c-button__text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-button__text']")))
    print('PASS - step 1508')
except Exception as e:
    print('FAIL - step 1508' if isinstance(e, AssertionError) else f'ERROR - step 1508: {e}')

print("STEP 1509 - Check element p#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "p")))
    print('PASS - step 1509')
except Exception as e:
    print('FAIL - step 1509' if isinstance(e, AssertionError) else f'ERROR - step 1509: {e}')

print("STEP 1510 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1510')
except Exception as e:
    print('FAIL - step 1510' if isinstance(e, AssertionError) else f'ERROR - step 1510: {e}')

print("STEP 1511 - Check element a#id4b106037dce91c43182a983f9461cc69472c6b30550fe5b08d10a2e519a97388.['c-button-link-with-arrow', 'append-misc-url-params']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id4b106037dce91c43182a983f9461cc69472c6b30550fe5b08d10a2e519a97388")))
    print('PASS - step 1511')
except Exception as e:
    print('FAIL - step 1511' if isinstance(e, AssertionError) else f'ERROR - step 1511: {e}')

print("STEP 1512 - Check element span#None.['c-button__text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-button__text']")))
    print('PASS - step 1512')
except Exception as e:
    print('FAIL - step 1512' if isinstance(e, AssertionError) else f'ERROR - step 1512: {e}')

print("STEP 1513 - Check element p#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "p")))
    print('PASS - step 1513')
except Exception as e:
    print('FAIL - step 1513' if isinstance(e, AssertionError) else f'ERROR - step 1513: {e}')

print("STEP 1514 - Check element svg#None.['link-arrow-svg']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link-arrow-svg']")))
    print('PASS - step 1514')
except Exception as e:
    print('FAIL - step 1514' if isinstance(e, AssertionError) else f'ERROR - step 1514: {e}')

print("STEP 1515 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 1515')
except Exception as e:
    print('FAIL - step 1515' if isinstance(e, AssertionError) else f'ERROR - step 1515: {e}')

print("STEP 1516 - Check element div#None.['c-grid-cell', 'col-lg-4', 'col-md-6', 'col-sm-12', 'cell-id_grid_celld560baf78f4003eb9a7ae1db78dd8d134f0c5db0ad7c3f89e14ab96dfb8daa5f']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-grid-cell', 'col-lg-4', 'col-md-6', 'col-sm-12', 'cell-id_grid_celld560baf78f4003eb9a7ae1db78dd8d134f0c5db0ad7c3f89e14ab96dfb8daa5f']")))
    print('PASS - step 1516')
except Exception as e:
    print('FAIL - step 1516' if isinstance(e, AssertionError) else f'ERROR - step 1516: {e}')

print("STEP 1517 - Check element div#None.['image']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['image']")))
    print('PASS - step 1517')
except Exception as e:
    print('FAIL - step 1517' if isinstance(e, AssertionError) else f'ERROR - step 1517: {e}')

print("STEP 1518 - Check element div#id_image_idd740dfc19680c5b0c0958b2d8b6a6127a162735c4158eb93f2c1c232a7aa41ca.['c-image-container', 'cmp-image', 'c-image-container--align-left']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id_image_idd740dfc19680c5b0c0958b2d8b6a6127a162735c4158eb93f2c1c232a7aa41ca")))
    print('PASS - step 1518')
except Exception as e:
    print('FAIL - step 1518' if isinstance(e, AssertionError) else f'ERROR - step 1518: {e}')

print("STEP 1519 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1519')
except Exception as e:
    print('FAIL - step 1519' if isinstance(e, AssertionError) else f'ERROR - step 1519: {e}')

print("STEP 1520 - Check element hp-image#None.['no-fade', 'c-image']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['no-fade', 'c-image']")))
    print('PASS - step 1520')
except Exception as e:
    print('FAIL - step 1520' if isinstance(e, AssertionError) else f'ERROR - step 1520: {e}')

print("STEP 1521 - Check element div#None.['titleAndText']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['titleAndText']")))
    print('PASS - step 1521')
except Exception as e:
    print('FAIL - step 1521' if isinstance(e, AssertionError) else f'ERROR - step 1521: {e}')

print("STEP 1522 - Check element hp-title-and-text#None.['c-title-and-text__wrapper', 'font-']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-title-and-text__wrapper', 'font-']")))
    print('PASS - step 1522')
except Exception as e:
    print('FAIL - step 1522' if isinstance(e, AssertionError) else f'ERROR - step 1522: {e}')

print("STEP 1523 - Check element div#None.['c-title-and-text', 'c-title-and-text--text-left', 'bg-', 'font-black', 'id_text_title_id78df304023a1edfb538730f43e83c3678c21ca81540bdffa0a275211dbdcb5ac']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-title-and-text', 'c-title-and-text--text-left', 'bg-', 'font-black', 'id_text_title_id78df304023a1edfb538730f43e83c3678c21ca81540bdffa0a275211dbdcb5ac']")))
    print('PASS - step 1523')
except Exception as e:
    print('FAIL - step 1523' if isinstance(e, AssertionError) else f'ERROR - step 1523: {e}')

print("STEP 1524 - Check element div#None.['c-title-and-text__title']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-title-and-text__title']")))
    print('PASS - step 1524')
except Exception as e:
    print('FAIL - step 1524' if isinstance(e, AssertionError) else f'ERROR - step 1524: {e}')

print("STEP 1525 - Check element h4#None.['h4']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['h4']")))
    print('PASS - step 1525')
except Exception as e:
    print('FAIL - step 1525' if isinstance(e, AssertionError) else f'ERROR - step 1525: {e}')

print("STEP 1526 - Check element div#None.['ctadropdownbutton']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ctadropdownbutton']")))
    print('PASS - step 1526')
except Exception as e:
    print('FAIL - step 1526' if isinstance(e, AssertionError) else f'ERROR - step 1526: {e}')

print("STEP 1527 - Check element div#None.['cta-dropdown-button', 'text-left', 'inline-container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['cta-dropdown-button', 'text-left', 'inline-container']")))
    print('PASS - step 1527')
except Exception as e:
    print('FAIL - step 1527' if isinstance(e, AssertionError) else f'ERROR - step 1527: {e}')

print("STEP 1528 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1528')
except Exception as e:
    print('FAIL - step 1528' if isinstance(e, AssertionError) else f'ERROR - step 1528: {e}')

print("STEP 1529 - Check element a#id09f16902d554de1109baba878f1e2f0d508da2c6e8cd6eccfa9fb5a7cf191498.['c-button', 'append-misc-url-params']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id09f16902d554de1109baba878f1e2f0d508da2c6e8cd6eccfa9fb5a7cf191498")))
    print('PASS - step 1529')
except Exception as e:
    print('FAIL - step 1529' if isinstance(e, AssertionError) else f'ERROR - step 1529: {e}')

print("STEP 1530 - Check element span#None.['c-button__text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-button__text']")))
    print('PASS - step 1530')
except Exception as e:
    print('FAIL - step 1530' if isinstance(e, AssertionError) else f'ERROR - step 1530: {e}')

print("STEP 1531 - Check element p#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "p")))
    print('PASS - step 1531')
except Exception as e:
    print('FAIL - step 1531' if isinstance(e, AssertionError) else f'ERROR - step 1531: {e}')

print("STEP 1532 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1532')
except Exception as e:
    print('FAIL - step 1532' if isinstance(e, AssertionError) else f'ERROR - step 1532: {e}')

print("STEP 1533 - Check element a#id585bbb77f3aa5bbb0a9e789825478953013a214c69790022b3382d09a7a1e0cd.['c-button-link-with-arrow', 'append-misc-url-params']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id585bbb77f3aa5bbb0a9e789825478953013a214c69790022b3382d09a7a1e0cd")))
    print('PASS - step 1533')
except Exception as e:
    print('FAIL - step 1533' if isinstance(e, AssertionError) else f'ERROR - step 1533: {e}')

print("STEP 1534 - Check element span#None.['c-button__text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-button__text']")))
    print('PASS - step 1534')
except Exception as e:
    print('FAIL - step 1534' if isinstance(e, AssertionError) else f'ERROR - step 1534: {e}')

print("STEP 1535 - Check element p#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "p")))
    print('PASS - step 1535')
except Exception as e:
    print('FAIL - step 1535' if isinstance(e, AssertionError) else f'ERROR - step 1535: {e}')

print("STEP 1536 - Check element svg#None.['link-arrow-svg']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link-arrow-svg']")))
    print('PASS - step 1536')
except Exception as e:
    print('FAIL - step 1536' if isinstance(e, AssertionError) else f'ERROR - step 1536: {e}')

print("STEP 1537 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 1537')
except Exception as e:
    print('FAIL - step 1537' if isinstance(e, AssertionError) else f'ERROR - step 1537: {e}')

print("STEP 1538 - Check element div#None.['c-grid-cell', 'col-lg-4', 'col-md-6', 'col-sm-12', 'cell-id_grid_cell57676424fa3730e78ee6b9431a380d43e5c68864cecc6ab2a3f4900f2af5ff88']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-grid-cell', 'col-lg-4', 'col-md-6', 'col-sm-12', 'cell-id_grid_cell57676424fa3730e78ee6b9431a380d43e5c68864cecc6ab2a3f4900f2af5ff88']")))
    print('PASS - step 1538')
except Exception as e:
    print('FAIL - step 1538' if isinstance(e, AssertionError) else f'ERROR - step 1538: {e}')

print("STEP 1539 - Check element div#None.['image']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['image']")))
    print('PASS - step 1539')
except Exception as e:
    print('FAIL - step 1539' if isinstance(e, AssertionError) else f'ERROR - step 1539: {e}')

print("STEP 1540 - Check element div#id_image_id4f283f631043c62fced947a00329be4fca073e8d39fb19c2bb7ad16a765a7421.['c-image-container', 'cmp-image', 'c-image-container--align-left']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id_image_id4f283f631043c62fced947a00329be4fca073e8d39fb19c2bb7ad16a765a7421")))
    print('PASS - step 1540')
except Exception as e:
    print('FAIL - step 1540' if isinstance(e, AssertionError) else f'ERROR - step 1540: {e}')

print("STEP 1541 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1541')
except Exception as e:
    print('FAIL - step 1541' if isinstance(e, AssertionError) else f'ERROR - step 1541: {e}')

print("STEP 1542 - Check element hp-image#None.['no-fade', 'c-image']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['no-fade', 'c-image']")))
    print('PASS - step 1542')
except Exception as e:
    print('FAIL - step 1542' if isinstance(e, AssertionError) else f'ERROR - step 1542: {e}')

print("STEP 1543 - Check element div#None.['titleAndText']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['titleAndText']")))
    print('PASS - step 1543')
except Exception as e:
    print('FAIL - step 1543' if isinstance(e, AssertionError) else f'ERROR - step 1543: {e}')

print("STEP 1544 - Check element hp-title-and-text#None.['c-title-and-text__wrapper', 'font-']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-title-and-text__wrapper', 'font-']")))
    print('PASS - step 1544')
except Exception as e:
    print('FAIL - step 1544' if isinstance(e, AssertionError) else f'ERROR - step 1544: {e}')

print("STEP 1545 - Check element div#None.['c-title-and-text', 'c-title-and-text--text-left', 'bg-', 'font-black', 'id_text_title_id32a4b06298db4a71b68dd65d13cef0cff0fd2fbefeea243ab682c0ceda8b3244']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-title-and-text', 'c-title-and-text--text-left', 'bg-', 'font-black', 'id_text_title_id32a4b06298db4a71b68dd65d13cef0cff0fd2fbefeea243ab682c0ceda8b3244']")))
    print('PASS - step 1545')
except Exception as e:
    print('FAIL - step 1545' if isinstance(e, AssertionError) else f'ERROR - step 1545: {e}')

print("STEP 1546 - Check element div#None.['c-title-and-text__title']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-title-and-text__title']")))
    print('PASS - step 1546')
except Exception as e:
    print('FAIL - step 1546' if isinstance(e, AssertionError) else f'ERROR - step 1546: {e}')

print("STEP 1547 - Check element h4#None.['h4']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['h4']")))
    print('PASS - step 1547')
except Exception as e:
    print('FAIL - step 1547' if isinstance(e, AssertionError) else f'ERROR - step 1547: {e}')

print("STEP 1548 - Check element div#None.['ctadropdownbutton']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ctadropdownbutton']")))
    print('PASS - step 1548')
except Exception as e:
    print('FAIL - step 1548' if isinstance(e, AssertionError) else f'ERROR - step 1548: {e}')

print("STEP 1549 - Check element div#None.['cta-dropdown-button', 'text-left', 'inline-container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['cta-dropdown-button', 'text-left', 'inline-container']")))
    print('PASS - step 1549')
except Exception as e:
    print('FAIL - step 1549' if isinstance(e, AssertionError) else f'ERROR - step 1549: {e}')

print("STEP 1550 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1550')
except Exception as e:
    print('FAIL - step 1550' if isinstance(e, AssertionError) else f'ERROR - step 1550: {e}')

print("STEP 1551 - Check element a#idf3c4371f68b02ed0ccc19714b73c31445f5b6231b8d9ee0765e705f2580ead40.['c-button', 'append-misc-url-params']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "idf3c4371f68b02ed0ccc19714b73c31445f5b6231b8d9ee0765e705f2580ead40")))
    print('PASS - step 1551')
except Exception as e:
    print('FAIL - step 1551' if isinstance(e, AssertionError) else f'ERROR - step 1551: {e}')

print("STEP 1552 - Check element span#None.['c-button__text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-button__text']")))
    print('PASS - step 1552')
except Exception as e:
    print('FAIL - step 1552' if isinstance(e, AssertionError) else f'ERROR - step 1552: {e}')

print("STEP 1553 - Check element p#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "p")))
    print('PASS - step 1553')
except Exception as e:
    print('FAIL - step 1553' if isinstance(e, AssertionError) else f'ERROR - step 1553: {e}')

print("STEP 1554 - Check element div#None.['c-grid-cell', 'col-lg-4', 'col-md-6', 'col-sm-12', 'cell-id_grid_cell06b2d158f13c3d5ca7a6d3b85ed4507c3d0e5f58060c5e4a582e7051dc2600e0']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-grid-cell', 'col-lg-4', 'col-md-6', 'col-sm-12', 'cell-id_grid_cell06b2d158f13c3d5ca7a6d3b85ed4507c3d0e5f58060c5e4a582e7051dc2600e0']")))
    print('PASS - step 1554')
except Exception as e:
    print('FAIL - step 1554' if isinstance(e, AssertionError) else f'ERROR - step 1554: {e}')

print("STEP 1555 - Check element div#None.['image']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['image']")))
    print('PASS - step 1555')
except Exception as e:
    print('FAIL - step 1555' if isinstance(e, AssertionError) else f'ERROR - step 1555: {e}')

print("STEP 1556 - Check element div#id_image_id5a508bc345ca61dba2022b4ec78a6c7978ff1bb5f3af4e571e9b2cd7a01caccb.['c-image-container', 'cmp-image', 'c-image-container--align-left']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id_image_id5a508bc345ca61dba2022b4ec78a6c7978ff1bb5f3af4e571e9b2cd7a01caccb")))
    print('PASS - step 1556')
except Exception as e:
    print('FAIL - step 1556' if isinstance(e, AssertionError) else f'ERROR - step 1556: {e}')

print("STEP 1557 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1557')
except Exception as e:
    print('FAIL - step 1557' if isinstance(e, AssertionError) else f'ERROR - step 1557: {e}')

print("STEP 1558 - Check element hp-image#None.['no-fade', 'c-image']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['no-fade', 'c-image']")))
    print('PASS - step 1558')
except Exception as e:
    print('FAIL - step 1558' if isinstance(e, AssertionError) else f'ERROR - step 1558: {e}')

print("STEP 1559 - Check element div#None.['titleAndText']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['titleAndText']")))
    print('PASS - step 1559')
except Exception as e:
    print('FAIL - step 1559' if isinstance(e, AssertionError) else f'ERROR - step 1559: {e}')

print("STEP 1560 - Check element hp-title-and-text#None.['c-title-and-text__wrapper', 'font-']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-title-and-text__wrapper', 'font-']")))
    print('PASS - step 1560')
except Exception as e:
    print('FAIL - step 1560' if isinstance(e, AssertionError) else f'ERROR - step 1560: {e}')

print("STEP 1561 - Check element div#None.['c-title-and-text', 'c-title-and-text--text-left', 'bg-', 'font-black', 'id_text_title_id961f76582ff20be85f4fd3651d5eaf30a1095f257ca03282c2b66c9ab8135c49']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-title-and-text', 'c-title-and-text--text-left', 'bg-', 'font-black', 'id_text_title_id961f76582ff20be85f4fd3651d5eaf30a1095f257ca03282c2b66c9ab8135c49']")))
    print('PASS - step 1561')
except Exception as e:
    print('FAIL - step 1561' if isinstance(e, AssertionError) else f'ERROR - step 1561: {e}')

print("STEP 1562 - Check element div#None.['c-title-and-text__title']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-title-and-text__title']")))
    print('PASS - step 1562')
except Exception as e:
    print('FAIL - step 1562' if isinstance(e, AssertionError) else f'ERROR - step 1562: {e}')

print("STEP 1563 - Check element h4#None.['h4']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['h4']")))
    print('PASS - step 1563')
except Exception as e:
    print('FAIL - step 1563' if isinstance(e, AssertionError) else f'ERROR - step 1563: {e}')

print("STEP 1564 - Check element div#None.['ctadropdownbutton']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ctadropdownbutton']")))
    print('PASS - step 1564')
except Exception as e:
    print('FAIL - step 1564' if isinstance(e, AssertionError) else f'ERROR - step 1564: {e}')

print("STEP 1565 - Check element div#None.['cta-dropdown-button', 'text-left', 'inline-container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['cta-dropdown-button', 'text-left', 'inline-container']")))
    print('PASS - step 1565')
except Exception as e:
    print('FAIL - step 1565' if isinstance(e, AssertionError) else f'ERROR - step 1565: {e}')

print("STEP 1566 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1566')
except Exception as e:
    print('FAIL - step 1566' if isinstance(e, AssertionError) else f'ERROR - step 1566: {e}')

print("STEP 1567 - Check element a#idc5cb07905260057dd085c359deb99c29ffc48c75e977fb63dadd048149e406ee.['c-button', 'append-misc-url-params']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "idc5cb07905260057dd085c359deb99c29ffc48c75e977fb63dadd048149e406ee")))
    print('PASS - step 1567')
except Exception as e:
    print('FAIL - step 1567' if isinstance(e, AssertionError) else f'ERROR - step 1567: {e}')

print("STEP 1568 - Check element span#None.['c-button__text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-button__text']")))
    print('PASS - step 1568')
except Exception as e:
    print('FAIL - step 1568' if isinstance(e, AssertionError) else f'ERROR - step 1568: {e}')

print("STEP 1569 - Check element p#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "p")))
    print('PASS - step 1569')
except Exception as e:
    print('FAIL - step 1569' if isinstance(e, AssertionError) else f'ERROR - step 1569: {e}')

print("STEP 1570 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1570')
except Exception as e:
    print('FAIL - step 1570' if isinstance(e, AssertionError) else f'ERROR - step 1570: {e}')

print("STEP 1571 - Check element a#id066feb03c3723c5f8c68f5fe9b6c5ee6502f6078a3a76faf1776fe686127d96c.['c-button-link-with-arrow', 'append-misc-url-params']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id066feb03c3723c5f8c68f5fe9b6c5ee6502f6078a3a76faf1776fe686127d96c")))
    print('PASS - step 1571')
except Exception as e:
    print('FAIL - step 1571' if isinstance(e, AssertionError) else f'ERROR - step 1571: {e}')

print("STEP 1572 - Check element span#None.['c-button__text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-button__text']")))
    print('PASS - step 1572')
except Exception as e:
    print('FAIL - step 1572' if isinstance(e, AssertionError) else f'ERROR - step 1572: {e}')

print("STEP 1573 - Check element p#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "p")))
    print('PASS - step 1573')
except Exception as e:
    print('FAIL - step 1573' if isinstance(e, AssertionError) else f'ERROR - step 1573: {e}')

print("STEP 1574 - Check element svg#None.['link-arrow-svg']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link-arrow-svg']")))
    print('PASS - step 1574')
except Exception as e:
    print('FAIL - step 1574' if isinstance(e, AssertionError) else f'ERROR - step 1574: {e}')

print("STEP 1575 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 1575')
except Exception as e:
    print('FAIL - step 1575' if isinstance(e, AssertionError) else f'ERROR - step 1575: {e}')

print("STEP 1576 - Check element div#None.['c-grid-cell', 'col-lg-4', 'col-md-6', 'col-sm-12', 'cell-id_grid_cell9e428a8930a0dfca97b0b0341955cf820dd22f4247ab05ac63690675d0f4fb77']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-grid-cell', 'col-lg-4', 'col-md-6', 'col-sm-12', 'cell-id_grid_cell9e428a8930a0dfca97b0b0341955cf820dd22f4247ab05ac63690675d0f4fb77']")))
    print('PASS - step 1576')
except Exception as e:
    print('FAIL - step 1576' if isinstance(e, AssertionError) else f'ERROR - step 1576: {e}')

print("STEP 1577 - Check element div#None.['image']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['image']")))
    print('PASS - step 1577')
except Exception as e:
    print('FAIL - step 1577' if isinstance(e, AssertionError) else f'ERROR - step 1577: {e}')

print("STEP 1578 - Check element div#id_image_idf36feb7cbfa656ff9a2b94cf4d45e307de8d5e564c222f6136ddd6f408bde76c.['c-image-container', 'cmp-image', 'c-image-container--align-left']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id_image_idf36feb7cbfa656ff9a2b94cf4d45e307de8d5e564c222f6136ddd6f408bde76c")))
    print('PASS - step 1578')
except Exception as e:
    print('FAIL - step 1578' if isinstance(e, AssertionError) else f'ERROR - step 1578: {e}')

print("STEP 1579 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1579')
except Exception as e:
    print('FAIL - step 1579' if isinstance(e, AssertionError) else f'ERROR - step 1579: {e}')

print("STEP 1580 - Check element hp-image#None.['no-fade', 'c-image']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['no-fade', 'c-image']")))
    print('PASS - step 1580')
except Exception as e:
    print('FAIL - step 1580' if isinstance(e, AssertionError) else f'ERROR - step 1580: {e}')

print("STEP 1581 - Check element div#None.['titleAndText']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['titleAndText']")))
    print('PASS - step 1581')
except Exception as e:
    print('FAIL - step 1581' if isinstance(e, AssertionError) else f'ERROR - step 1581: {e}')

print("STEP 1582 - Check element hp-title-and-text#None.['c-title-and-text__wrapper', 'font-']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-title-and-text__wrapper', 'font-']")))
    print('PASS - step 1582')
except Exception as e:
    print('FAIL - step 1582' if isinstance(e, AssertionError) else f'ERROR - step 1582: {e}')

print("STEP 1583 - Check element div#None.['c-title-and-text', 'c-title-and-text--text-left', 'bg-', 'font-black', 'id_text_title_ideb1729060729cd7f742204f000bee76c363fa977683837f47142b5520f3f0154']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-title-and-text', 'c-title-and-text--text-left', 'bg-', 'font-black', 'id_text_title_ideb1729060729cd7f742204f000bee76c363fa977683837f47142b5520f3f0154']")))
    print('PASS - step 1583')
except Exception as e:
    print('FAIL - step 1583' if isinstance(e, AssertionError) else f'ERROR - step 1583: {e}')

print("STEP 1584 - Check element div#None.['c-title-and-text__title']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-title-and-text__title']")))
    print('PASS - step 1584')
except Exception as e:
    print('FAIL - step 1584' if isinstance(e, AssertionError) else f'ERROR - step 1584: {e}')

print("STEP 1585 - Check element h4#None.['h4']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['h4']")))
    print('PASS - step 1585')
except Exception as e:
    print('FAIL - step 1585' if isinstance(e, AssertionError) else f'ERROR - step 1585: {e}')

print("STEP 1586 - Check element div#None.['ctadropdownbutton']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ctadropdownbutton']")))
    print('PASS - step 1586')
except Exception as e:
    print('FAIL - step 1586' if isinstance(e, AssertionError) else f'ERROR - step 1586: {e}')

print("STEP 1587 - Check element div#None.['cta-dropdown-button', 'text-left', 'inline-container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['cta-dropdown-button', 'text-left', 'inline-container']")))
    print('PASS - step 1587')
except Exception as e:
    print('FAIL - step 1587' if isinstance(e, AssertionError) else f'ERROR - step 1587: {e}')

print("STEP 1588 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1588')
except Exception as e:
    print('FAIL - step 1588' if isinstance(e, AssertionError) else f'ERROR - step 1588: {e}')

print("STEP 1589 - Check element a#id980ac73986a3de6a5bef7d14ba94877900b73c8e144670c10fccf695d91fe9f2.['c-button', 'append-misc-url-params']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id980ac73986a3de6a5bef7d14ba94877900b73c8e144670c10fccf695d91fe9f2")))
    print('PASS - step 1589')
except Exception as e:
    print('FAIL - step 1589' if isinstance(e, AssertionError) else f'ERROR - step 1589: {e}')

print("STEP 1590 - Check element span#None.['c-button__text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-button__text']")))
    print('PASS - step 1590')
except Exception as e:
    print('FAIL - step 1590' if isinstance(e, AssertionError) else f'ERROR - step 1590: {e}')

print("STEP 1591 - Check element p#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "p")))
    print('PASS - step 1591')
except Exception as e:
    print('FAIL - step 1591' if isinstance(e, AssertionError) else f'ERROR - step 1591: {e}')

print("STEP 1592 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1592')
except Exception as e:
    print('FAIL - step 1592' if isinstance(e, AssertionError) else f'ERROR - step 1592: {e}')

print("STEP 1593 - Check element a#id564c046020852231a2a13e2f3b26df68e65bddfb972ed82bffe009226060e57e.['c-button-link-with-arrow', 'append-misc-url-params']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id564c046020852231a2a13e2f3b26df68e65bddfb972ed82bffe009226060e57e")))
    print('PASS - step 1593')
except Exception as e:
    print('FAIL - step 1593' if isinstance(e, AssertionError) else f'ERROR - step 1593: {e}')

print("STEP 1594 - Check element span#None.['c-button__text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-button__text']")))
    print('PASS - step 1594')
except Exception as e:
    print('FAIL - step 1594' if isinstance(e, AssertionError) else f'ERROR - step 1594: {e}')

print("STEP 1595 - Check element p#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "p")))
    print('PASS - step 1595')
except Exception as e:
    print('FAIL - step 1595' if isinstance(e, AssertionError) else f'ERROR - step 1595: {e}')

print("STEP 1596 - Check element svg#None.['link-arrow-svg']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link-arrow-svg']")))
    print('PASS - step 1596')
except Exception as e:
    print('FAIL - step 1596' if isinstance(e, AssertionError) else f'ERROR - step 1596: {e}')

print("STEP 1597 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 1597')
except Exception as e:
    print('FAIL - step 1597' if isinstance(e, AssertionError) else f'ERROR - step 1597: {e}')

print("STEP 1598 - Check element div#None.['c-grid-cell', 'col-lg-4', 'col-md-6', 'col-sm-12', 'cell-id_grid_cell67c143f2c12417f676e7bc8c35637bece0174e70292537a4d4a105f54c4839f8']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-grid-cell', 'col-lg-4', 'col-md-6', 'col-sm-12', 'cell-id_grid_cell67c143f2c12417f676e7bc8c35637bece0174e70292537a4d4a105f54c4839f8']")))
    print('PASS - step 1598')
except Exception as e:
    print('FAIL - step 1598' if isinstance(e, AssertionError) else f'ERROR - step 1598: {e}')

print("STEP 1599 - Check element div#None.['image']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['image']")))
    print('PASS - step 1599')
except Exception as e:
    print('FAIL - step 1599' if isinstance(e, AssertionError) else f'ERROR - step 1599: {e}')

print("STEP 1600 - Check element div#id_image_id1bdbe57ba60d64f66eade0b68a49103e5ae94d0ce7eb528b2e114de3a3762462.['c-image-container', 'cmp-image', 'c-image-container--align-left']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id_image_id1bdbe57ba60d64f66eade0b68a49103e5ae94d0ce7eb528b2e114de3a3762462")))
    print('PASS - step 1600')
except Exception as e:
    print('FAIL - step 1600' if isinstance(e, AssertionError) else f'ERROR - step 1600: {e}')

print("STEP 1601 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1601')
except Exception as e:
    print('FAIL - step 1601' if isinstance(e, AssertionError) else f'ERROR - step 1601: {e}')

print("STEP 1602 - Check element hp-image#None.['no-fade', 'c-image']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['no-fade', 'c-image']")))
    print('PASS - step 1602')
except Exception as e:
    print('FAIL - step 1602' if isinstance(e, AssertionError) else f'ERROR - step 1602: {e}')

print("STEP 1603 - Check element div#None.['titleAndText']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['titleAndText']")))
    print('PASS - step 1603')
except Exception as e:
    print('FAIL - step 1603' if isinstance(e, AssertionError) else f'ERROR - step 1603: {e}')

print("STEP 1604 - Check element hp-title-and-text#None.['c-title-and-text__wrapper', 'font-']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-title-and-text__wrapper', 'font-']")))
    print('PASS - step 1604')
except Exception as e:
    print('FAIL - step 1604' if isinstance(e, AssertionError) else f'ERROR - step 1604: {e}')

print("STEP 1605 - Check element div#None.['c-title-and-text', 'c-title-and-text--text-left', 'bg-', 'font-black', 'id_text_title_idff034aba3908eda9e67af9cbda8902072bce5e262d78ab3cc640aa8fe989328e']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-title-and-text', 'c-title-and-text--text-left', 'bg-', 'font-black', 'id_text_title_idff034aba3908eda9e67af9cbda8902072bce5e262d78ab3cc640aa8fe989328e']")))
    print('PASS - step 1605')
except Exception as e:
    print('FAIL - step 1605' if isinstance(e, AssertionError) else f'ERROR - step 1605: {e}')

print("STEP 1606 - Check element div#None.['c-title-and-text__title']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-title-and-text__title']")))
    print('PASS - step 1606')
except Exception as e:
    print('FAIL - step 1606' if isinstance(e, AssertionError) else f'ERROR - step 1606: {e}')

print("STEP 1607 - Check element h4#None.['h4']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['h4']")))
    print('PASS - step 1607')
except Exception as e:
    print('FAIL - step 1607' if isinstance(e, AssertionError) else f'ERROR - step 1607: {e}')

print("STEP 1608 - Check element div#None.['ctadropdownbutton']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ctadropdownbutton']")))
    print('PASS - step 1608')
except Exception as e:
    print('FAIL - step 1608' if isinstance(e, AssertionError) else f'ERROR - step 1608: {e}')

print("STEP 1609 - Check element div#None.['cta-dropdown-button', 'text-left', 'inline-container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['cta-dropdown-button', 'text-left', 'inline-container']")))
    print('PASS - step 1609')
except Exception as e:
    print('FAIL - step 1609' if isinstance(e, AssertionError) else f'ERROR - step 1609: {e}')

print("STEP 1610 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1610')
except Exception as e:
    print('FAIL - step 1610' if isinstance(e, AssertionError) else f'ERROR - step 1610: {e}')

print("STEP 1611 - Check element a#id11609668a198e12c5b442e4c644bb656f3b3a00aa216d0c4400658be7419b333.['c-button', 'append-misc-url-params']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id11609668a198e12c5b442e4c644bb656f3b3a00aa216d0c4400658be7419b333")))
    print('PASS - step 1611')
except Exception as e:
    print('FAIL - step 1611' if isinstance(e, AssertionError) else f'ERROR - step 1611: {e}')

print("STEP 1612 - Check element span#None.['c-button__text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-button__text']")))
    print('PASS - step 1612')
except Exception as e:
    print('FAIL - step 1612' if isinstance(e, AssertionError) else f'ERROR - step 1612: {e}')

print("STEP 1613 - Check element p#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "p")))
    print('PASS - step 1613')
except Exception as e:
    print('FAIL - step 1613' if isinstance(e, AssertionError) else f'ERROR - step 1613: {e}')

print("STEP 1614 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1614')
except Exception as e:
    print('FAIL - step 1614' if isinstance(e, AssertionError) else f'ERROR - step 1614: {e}')

print("STEP 1615 - Check element a#id64a27e03638072cd0768466963d760c7e2899d258347bd1b750dac14a145bbc6.['c-button-link-with-arrow', 'append-misc-url-params']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id64a27e03638072cd0768466963d760c7e2899d258347bd1b750dac14a145bbc6")))
    print('PASS - step 1615')
except Exception as e:
    print('FAIL - step 1615' if isinstance(e, AssertionError) else f'ERROR - step 1615: {e}')

print("STEP 1616 - Check element span#None.['c-button__text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-button__text']")))
    print('PASS - step 1616')
except Exception as e:
    print('FAIL - step 1616' if isinstance(e, AssertionError) else f'ERROR - step 1616: {e}')

print("STEP 1617 - Check element p#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "p")))
    print('PASS - step 1617')
except Exception as e:
    print('FAIL - step 1617' if isinstance(e, AssertionError) else f'ERROR - step 1617: {e}')

print("STEP 1618 - Check element svg#None.['link-arrow-svg']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link-arrow-svg']")))
    print('PASS - step 1618')
except Exception as e:
    print('FAIL - step 1618' if isinstance(e, AssertionError) else f'ERROR - step 1618: {e}')

print("STEP 1619 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 1619')
except Exception as e:
    print('FAIL - step 1619' if isinstance(e, AssertionError) else f'ERROR - step 1619: {e}')

print("STEP 1620 - Check element div#None.['c-visual-tabs-item__content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-visual-tabs-item__content']")))
    print('PASS - step 1620')
except Exception as e:
    print('FAIL - step 1620' if isinstance(e, AssertionError) else f'ERROR - step 1620: {e}')

print("STEP 1621 - Check element div#None.['grid']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['grid']")))
    print('PASS - step 1621')
except Exception as e:
    print('FAIL - step 1621' if isinstance(e, AssertionError) else f'ERROR - step 1621: {e}')

print("STEP 1622 - Check element hp-grid#None.['js-hp-component', 'hp-grid', 'id_gridbc80d40668174694941959eda8b76eb0', 'js-hp-component-initialized']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['js-hp-component', 'hp-grid', 'id_gridbc80d40668174694941959eda8b76eb0', 'js-hp-component-initialized']")))
    print('PASS - step 1622')
except Exception as e:
    print('FAIL - step 1622' if isinstance(e, AssertionError) else f'ERROR - step 1622: {e}')

print("STEP 1623 - Check element div#None.['container', 'id_grid_containeraff1dc247b2748658cab0fb3f3ad08df']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['container', 'id_grid_containeraff1dc247b2748658cab0fb3f3ad08df']")))
    print('PASS - step 1623')
except Exception as e:
    print('FAIL - step 1623' if isinstance(e, AssertionError) else f'ERROR - step 1623: {e}')

print("STEP 1624 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1624')
except Exception as e:
    print('FAIL - step 1624' if isinstance(e, AssertionError) else f'ERROR - step 1624: {e}')

print("STEP 1625 - Check element div#None.['row', 'justify-content-center', 'justify-content-lg-center', 'justify-content-md-center']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['row', 'justify-content-center', 'justify-content-lg-center', 'justify-content-md-center']")))
    print('PASS - step 1625')
except Exception as e:
    print('FAIL - step 1625' if isinstance(e, AssertionError) else f'ERROR - step 1625: {e}')

print("STEP 1626 - Check element div#None.['c-grid-cell', 'col-lg-4', 'col-md-6', 'col-sm-12', 'cell-id_grid_cella56508b57de83c32da8d248da3b956224fc114d6dad7b65f16202a36cae9835e']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-grid-cell', 'col-lg-4', 'col-md-6', 'col-sm-12', 'cell-id_grid_cella56508b57de83c32da8d248da3b956224fc114d6dad7b65f16202a36cae9835e']")))
    print('PASS - step 1626')
except Exception as e:
    print('FAIL - step 1626' if isinstance(e, AssertionError) else f'ERROR - step 1626: {e}')

print("STEP 1627 - Check element div#None.['image']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['image']")))
    print('PASS - step 1627')
except Exception as e:
    print('FAIL - step 1627' if isinstance(e, AssertionError) else f'ERROR - step 1627: {e}')

print("STEP 1628 - Check element div#id_image_id37a0715223e6aa936b7e919d4303626e0075b3cbcf63218bf102523962d4dbcd.['c-image-container', 'cmp-image', 'c-image-container--align-left']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id_image_id37a0715223e6aa936b7e919d4303626e0075b3cbcf63218bf102523962d4dbcd")))
    print('PASS - step 1628')
except Exception as e:
    print('FAIL - step 1628' if isinstance(e, AssertionError) else f'ERROR - step 1628: {e}')

print("STEP 1629 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1629')
except Exception as e:
    print('FAIL - step 1629' if isinstance(e, AssertionError) else f'ERROR - step 1629: {e}')

print("STEP 1630 - Check element hp-image#None.['no-fade', 'c-image']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['no-fade', 'c-image']")))
    print('PASS - step 1630')
except Exception as e:
    print('FAIL - step 1630' if isinstance(e, AssertionError) else f'ERROR - step 1630: {e}')

print("STEP 1631 - Check element div#None.['titleAndText']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['titleAndText']")))
    print('PASS - step 1631')
except Exception as e:
    print('FAIL - step 1631' if isinstance(e, AssertionError) else f'ERROR - step 1631: {e}')

print("STEP 1632 - Check element hp-title-and-text#None.['c-title-and-text__wrapper', 'font-']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-title-and-text__wrapper', 'font-']")))
    print('PASS - step 1632')
except Exception as e:
    print('FAIL - step 1632' if isinstance(e, AssertionError) else f'ERROR - step 1632: {e}')

print("STEP 1633 - Check element div#None.['c-title-and-text', 'c-title-and-text--text-left', 'bg-', 'font-black', 'id_text_title_id1f49d5eee3f7a79a5518d244961a29b402c122fa3b1cdbec51532c11b588115d']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-title-and-text', 'c-title-and-text--text-left', 'bg-', 'font-black', 'id_text_title_id1f49d5eee3f7a79a5518d244961a29b402c122fa3b1cdbec51532c11b588115d']")))
    print('PASS - step 1633')
except Exception as e:
    print('FAIL - step 1633' if isinstance(e, AssertionError) else f'ERROR - step 1633: {e}')

print("STEP 1634 - Check element div#None.['c-title-and-text__title']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-title-and-text__title']")))
    print('PASS - step 1634')
except Exception as e:
    print('FAIL - step 1634' if isinstance(e, AssertionError) else f'ERROR - step 1634: {e}')

print("STEP 1635 - Check element h4#None.['h4']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['h4']")))
    print('PASS - step 1635')
except Exception as e:
    print('FAIL - step 1635' if isinstance(e, AssertionError) else f'ERROR - step 1635: {e}')

print("STEP 1636 - Check element div#None.['ctadropdownbutton']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ctadropdownbutton']")))
    print('PASS - step 1636')
except Exception as e:
    print('FAIL - step 1636' if isinstance(e, AssertionError) else f'ERROR - step 1636: {e}')

print("STEP 1637 - Check element div#None.['cta-dropdown-button', 'text-left', 'inline-container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['cta-dropdown-button', 'text-left', 'inline-container']")))
    print('PASS - step 1637')
except Exception as e:
    print('FAIL - step 1637' if isinstance(e, AssertionError) else f'ERROR - step 1637: {e}')

print("STEP 1638 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1638')
except Exception as e:
    print('FAIL - step 1638' if isinstance(e, AssertionError) else f'ERROR - step 1638: {e}')

print("STEP 1639 - Check element a#id14c62ae18e187c16294e88e9229d08840a74fd961731ba9505a7b65a41b15c25.['c-button', 'append-misc-url-params']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id14c62ae18e187c16294e88e9229d08840a74fd961731ba9505a7b65a41b15c25")))
    print('PASS - step 1639')
except Exception as e:
    print('FAIL - step 1639' if isinstance(e, AssertionError) else f'ERROR - step 1639: {e}')

print("STEP 1640 - Check element span#None.['c-button__text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-button__text']")))
    print('PASS - step 1640')
except Exception as e:
    print('FAIL - step 1640' if isinstance(e, AssertionError) else f'ERROR - step 1640: {e}')

print("STEP 1641 - Check element p#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "p")))
    print('PASS - step 1641')
except Exception as e:
    print('FAIL - step 1641' if isinstance(e, AssertionError) else f'ERROR - step 1641: {e}')

print("STEP 1642 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1642')
except Exception as e:
    print('FAIL - step 1642' if isinstance(e, AssertionError) else f'ERROR - step 1642: {e}')

print("STEP 1643 - Check element a#idea7ee0502c0c2be503f4c556af908d91e7024de931bb1b72b8bac6db72bef69d.['c-button-link-with-arrow', 'append-misc-url-params']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "idea7ee0502c0c2be503f4c556af908d91e7024de931bb1b72b8bac6db72bef69d")))
    print('PASS - step 1643')
except Exception as e:
    print('FAIL - step 1643' if isinstance(e, AssertionError) else f'ERROR - step 1643: {e}')

print("STEP 1644 - Check element span#None.['c-button__text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-button__text']")))
    print('PASS - step 1644')
except Exception as e:
    print('FAIL - step 1644' if isinstance(e, AssertionError) else f'ERROR - step 1644: {e}')

print("STEP 1645 - Check element p#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "p")))
    print('PASS - step 1645')
except Exception as e:
    print('FAIL - step 1645' if isinstance(e, AssertionError) else f'ERROR - step 1645: {e}')

print("STEP 1646 - Check element svg#None.['link-arrow-svg']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link-arrow-svg']")))
    print('PASS - step 1646')
except Exception as e:
    print('FAIL - step 1646' if isinstance(e, AssertionError) else f'ERROR - step 1646: {e}')

print("STEP 1647 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 1647')
except Exception as e:
    print('FAIL - step 1647' if isinstance(e, AssertionError) else f'ERROR - step 1647: {e}')

print("STEP 1648 - Check element div#None.['c-grid-cell', 'col-lg-4', 'col-md-6', 'col-sm-12', 'cell-id_grid_cell1eee82fe06eb239bcd1da6d1749cc90528b6699f7d2239823ebab44a1f0f529f']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-grid-cell', 'col-lg-4', 'col-md-6', 'col-sm-12', 'cell-id_grid_cell1eee82fe06eb239bcd1da6d1749cc90528b6699f7d2239823ebab44a1f0f529f']")))
    print('PASS - step 1648')
except Exception as e:
    print('FAIL - step 1648' if isinstance(e, AssertionError) else f'ERROR - step 1648: {e}')

print("STEP 1649 - Check element div#None.['image']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['image']")))
    print('PASS - step 1649')
except Exception as e:
    print('FAIL - step 1649' if isinstance(e, AssertionError) else f'ERROR - step 1649: {e}')

print("STEP 1650 - Check element div#id_image_idb0a9fb162038f5edef24ee85744368cf7e9995e264a36ca078b37fe5c9aad0f0.['c-image-container', 'cmp-image', 'c-image-container--align-left']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id_image_idb0a9fb162038f5edef24ee85744368cf7e9995e264a36ca078b37fe5c9aad0f0")))
    print('PASS - step 1650')
except Exception as e:
    print('FAIL - step 1650' if isinstance(e, AssertionError) else f'ERROR - step 1650: {e}')

print("STEP 1651 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1651')
except Exception as e:
    print('FAIL - step 1651' if isinstance(e, AssertionError) else f'ERROR - step 1651: {e}')

print("STEP 1652 - Check element hp-image#None.['no-fade', 'c-image']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['no-fade', 'c-image']")))
    print('PASS - step 1652')
except Exception as e:
    print('FAIL - step 1652' if isinstance(e, AssertionError) else f'ERROR - step 1652: {e}')

print("STEP 1653 - Check element div#None.['titleAndText']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['titleAndText']")))
    print('PASS - step 1653')
except Exception as e:
    print('FAIL - step 1653' if isinstance(e, AssertionError) else f'ERROR - step 1653: {e}')

print("STEP 1654 - Check element hp-title-and-text#None.['c-title-and-text__wrapper', 'font-']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-title-and-text__wrapper', 'font-']")))
    print('PASS - step 1654')
except Exception as e:
    print('FAIL - step 1654' if isinstance(e, AssertionError) else f'ERROR - step 1654: {e}')

print("STEP 1655 - Check element div#None.['c-title-and-text', 'c-title-and-text--text-left', 'bg-', 'font-black', 'id_text_title_id75444948ff1d817ee68f85bf8efe36c6c5cbe70bfc9eec37dde69a6124f35a0d']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-title-and-text', 'c-title-and-text--text-left', 'bg-', 'font-black', 'id_text_title_id75444948ff1d817ee68f85bf8efe36c6c5cbe70bfc9eec37dde69a6124f35a0d']")))
    print('PASS - step 1655')
except Exception as e:
    print('FAIL - step 1655' if isinstance(e, AssertionError) else f'ERROR - step 1655: {e}')

print("STEP 1656 - Check element div#None.['c-title-and-text__title']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-title-and-text__title']")))
    print('PASS - step 1656')
except Exception as e:
    print('FAIL - step 1656' if isinstance(e, AssertionError) else f'ERROR - step 1656: {e}')

print("STEP 1657 - Check element h4#None.['h4']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['h4']")))
    print('PASS - step 1657')
except Exception as e:
    print('FAIL - step 1657' if isinstance(e, AssertionError) else f'ERROR - step 1657: {e}')

print("STEP 1658 - Check element div#None.['ctadropdownbutton']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ctadropdownbutton']")))
    print('PASS - step 1658')
except Exception as e:
    print('FAIL - step 1658' if isinstance(e, AssertionError) else f'ERROR - step 1658: {e}')

print("STEP 1659 - Check element div#None.['cta-dropdown-button', 'text-left', 'inline-container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['cta-dropdown-button', 'text-left', 'inline-container']")))
    print('PASS - step 1659')
except Exception as e:
    print('FAIL - step 1659' if isinstance(e, AssertionError) else f'ERROR - step 1659: {e}')

print("STEP 1660 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1660')
except Exception as e:
    print('FAIL - step 1660' if isinstance(e, AssertionError) else f'ERROR - step 1660: {e}')

print("STEP 1661 - Check element a#id40664f90be4a4fb804ffd9bc2e3d8c485b5202a9d23702e57bc0327d3c8e2848.['c-button', 'append-misc-url-params']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id40664f90be4a4fb804ffd9bc2e3d8c485b5202a9d23702e57bc0327d3c8e2848")))
    print('PASS - step 1661')
except Exception as e:
    print('FAIL - step 1661' if isinstance(e, AssertionError) else f'ERROR - step 1661: {e}')

print("STEP 1662 - Check element span#None.['c-button__text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-button__text']")))
    print('PASS - step 1662')
except Exception as e:
    print('FAIL - step 1662' if isinstance(e, AssertionError) else f'ERROR - step 1662: {e}')

print("STEP 1663 - Check element p#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "p")))
    print('PASS - step 1663')
except Exception as e:
    print('FAIL - step 1663' if isinstance(e, AssertionError) else f'ERROR - step 1663: {e}')

print("STEP 1664 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1664')
except Exception as e:
    print('FAIL - step 1664' if isinstance(e, AssertionError) else f'ERROR - step 1664: {e}')

print("STEP 1665 - Check element a#idf770123dc7b96f34c1397d9aefd6fcbae333d9bebdcaa06fbf916d076c6d6fa5.['c-button-link-with-arrow', 'append-misc-url-params']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "idf770123dc7b96f34c1397d9aefd6fcbae333d9bebdcaa06fbf916d076c6d6fa5")))
    print('PASS - step 1665')
except Exception as e:
    print('FAIL - step 1665' if isinstance(e, AssertionError) else f'ERROR - step 1665: {e}')

print("STEP 1666 - Check element span#None.['c-button__text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-button__text']")))
    print('PASS - step 1666')
except Exception as e:
    print('FAIL - step 1666' if isinstance(e, AssertionError) else f'ERROR - step 1666: {e}')

print("STEP 1667 - Check element p#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "p")))
    print('PASS - step 1667')
except Exception as e:
    print('FAIL - step 1667' if isinstance(e, AssertionError) else f'ERROR - step 1667: {e}')

print("STEP 1668 - Check element svg#None.['link-arrow-svg']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link-arrow-svg']")))
    print('PASS - step 1668')
except Exception as e:
    print('FAIL - step 1668' if isinstance(e, AssertionError) else f'ERROR - step 1668: {e}')

print("STEP 1669 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 1669')
except Exception as e:
    print('FAIL - step 1669' if isinstance(e, AssertionError) else f'ERROR - step 1669: {e}')

print("STEP 1670 - Check element div#None.['c-grid-cell', 'col-lg-4', 'col-md-6', 'col-sm-12', 'cell-id_grid_cellea6254ef6957d1f70111c7538cda016e8e385cac686062a5c17ee43fda953310']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-grid-cell', 'col-lg-4', 'col-md-6', 'col-sm-12', 'cell-id_grid_cellea6254ef6957d1f70111c7538cda016e8e385cac686062a5c17ee43fda953310']")))
    print('PASS - step 1670')
except Exception as e:
    print('FAIL - step 1670' if isinstance(e, AssertionError) else f'ERROR - step 1670: {e}')

print("STEP 1671 - Check element div#None.['image']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['image']")))
    print('PASS - step 1671')
except Exception as e:
    print('FAIL - step 1671' if isinstance(e, AssertionError) else f'ERROR - step 1671: {e}')

print("STEP 1672 - Check element div#id_image_idc8db0033ebb8cda485cf77be3af42fc2516b1869822a4cd025581f6cdd3451d3.['c-image-container', 'cmp-image', 'c-image-container--align-left']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id_image_idc8db0033ebb8cda485cf77be3af42fc2516b1869822a4cd025581f6cdd3451d3")))
    print('PASS - step 1672')
except Exception as e:
    print('FAIL - step 1672' if isinstance(e, AssertionError) else f'ERROR - step 1672: {e}')

print("STEP 1673 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1673')
except Exception as e:
    print('FAIL - step 1673' if isinstance(e, AssertionError) else f'ERROR - step 1673: {e}')

print("STEP 1674 - Check element hp-image#None.['no-fade', 'c-image']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['no-fade', 'c-image']")))
    print('PASS - step 1674')
except Exception as e:
    print('FAIL - step 1674' if isinstance(e, AssertionError) else f'ERROR - step 1674: {e}')

print("STEP 1675 - Check element div#None.['titleAndText']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['titleAndText']")))
    print('PASS - step 1675')
except Exception as e:
    print('FAIL - step 1675' if isinstance(e, AssertionError) else f'ERROR - step 1675: {e}')

print("STEP 1676 - Check element hp-title-and-text#None.['c-title-and-text__wrapper', 'font-']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-title-and-text__wrapper', 'font-']")))
    print('PASS - step 1676')
except Exception as e:
    print('FAIL - step 1676' if isinstance(e, AssertionError) else f'ERROR - step 1676: {e}')

print("STEP 1677 - Check element div#None.['c-title-and-text', 'c-title-and-text--text-left', 'bg-', 'font-black', 'id_text_title_id8ddbe94a99a60ee570293f3e72e0eac7a0a98728fb381375d85c88469cbdde54']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-title-and-text', 'c-title-and-text--text-left', 'bg-', 'font-black', 'id_text_title_id8ddbe94a99a60ee570293f3e72e0eac7a0a98728fb381375d85c88469cbdde54']")))
    print('PASS - step 1677')
except Exception as e:
    print('FAIL - step 1677' if isinstance(e, AssertionError) else f'ERROR - step 1677: {e}')

print("STEP 1678 - Check element div#None.['c-title-and-text__title']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-title-and-text__title']")))
    print('PASS - step 1678')
except Exception as e:
    print('FAIL - step 1678' if isinstance(e, AssertionError) else f'ERROR - step 1678: {e}')

print("STEP 1679 - Check element h4#None.['h4']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['h4']")))
    print('PASS - step 1679')
except Exception as e:
    print('FAIL - step 1679' if isinstance(e, AssertionError) else f'ERROR - step 1679: {e}')

print("STEP 1680 - Check element div#None.['ctadropdownbutton']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ctadropdownbutton']")))
    print('PASS - step 1680')
except Exception as e:
    print('FAIL - step 1680' if isinstance(e, AssertionError) else f'ERROR - step 1680: {e}')

print("STEP 1681 - Check element div#None.['cta-dropdown-button', 'text-left', 'inline-container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['cta-dropdown-button', 'text-left', 'inline-container']")))
    print('PASS - step 1681')
except Exception as e:
    print('FAIL - step 1681' if isinstance(e, AssertionError) else f'ERROR - step 1681: {e}')

print("STEP 1682 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1682')
except Exception as e:
    print('FAIL - step 1682' if isinstance(e, AssertionError) else f'ERROR - step 1682: {e}')

print("STEP 1683 - Check element a#id4a1435bdaf870cac0ca10232c5e129249cf19425240013188f2a56896bf8ab82.['c-button', 'append-misc-url-params']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id4a1435bdaf870cac0ca10232c5e129249cf19425240013188f2a56896bf8ab82")))
    print('PASS - step 1683')
except Exception as e:
    print('FAIL - step 1683' if isinstance(e, AssertionError) else f'ERROR - step 1683: {e}')

print("STEP 1684 - Check element span#None.['c-button__text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-button__text']")))
    print('PASS - step 1684')
except Exception as e:
    print('FAIL - step 1684' if isinstance(e, AssertionError) else f'ERROR - step 1684: {e}')

print("STEP 1685 - Check element p#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "p")))
    print('PASS - step 1685')
except Exception as e:
    print('FAIL - step 1685' if isinstance(e, AssertionError) else f'ERROR - step 1685: {e}')

print("STEP 1686 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1686')
except Exception as e:
    print('FAIL - step 1686' if isinstance(e, AssertionError) else f'ERROR - step 1686: {e}')

print("STEP 1687 - Check element a#id681f5071db3c2306be440f5d2c62d3768c9ed8dfeaef98ac7ec400b6dca2799d.['c-button-link-with-arrow', 'append-misc-url-params']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id681f5071db3c2306be440f5d2c62d3768c9ed8dfeaef98ac7ec400b6dca2799d")))
    print('PASS - step 1687')
except Exception as e:
    print('FAIL - step 1687' if isinstance(e, AssertionError) else f'ERROR - step 1687: {e}')

print("STEP 1688 - Check element span#None.['c-button__text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-button__text']")))
    print('PASS - step 1688')
except Exception as e:
    print('FAIL - step 1688' if isinstance(e, AssertionError) else f'ERROR - step 1688: {e}')

print("STEP 1689 - Check element p#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "p")))
    print('PASS - step 1689')
except Exception as e:
    print('FAIL - step 1689' if isinstance(e, AssertionError) else f'ERROR - step 1689: {e}')

print("STEP 1690 - Check element svg#None.['link-arrow-svg']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link-arrow-svg']")))
    print('PASS - step 1690')
except Exception as e:
    print('FAIL - step 1690' if isinstance(e, AssertionError) else f'ERROR - step 1690: {e}')

print("STEP 1691 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 1691')
except Exception as e:
    print('FAIL - step 1691' if isinstance(e, AssertionError) else f'ERROR - step 1691: {e}')

print("STEP 1692 - Check element div#None.['c-grid-cell', 'col-lg-4', 'col-md-6', 'col-sm-12', 'cell-id_grid_cell8fe035dade1bf02a6f7751526165e1d70c49a828bafaf0912827392829c0e272']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-grid-cell', 'col-lg-4', 'col-md-6', 'col-sm-12', 'cell-id_grid_cell8fe035dade1bf02a6f7751526165e1d70c49a828bafaf0912827392829c0e272']")))
    print('PASS - step 1692')
except Exception as e:
    print('FAIL - step 1692' if isinstance(e, AssertionError) else f'ERROR - step 1692: {e}')

print("STEP 1693 - Check element div#None.['image']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['image']")))
    print('PASS - step 1693')
except Exception as e:
    print('FAIL - step 1693' if isinstance(e, AssertionError) else f'ERROR - step 1693: {e}')

print("STEP 1694 - Check element div#id_image_id8e531eba0d91ce9caf49c01de5fa5b828a23b0ab579d67a6ea87e9ee9b561c92.['c-image-container', 'cmp-image', 'c-image-container--align-left']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id_image_id8e531eba0d91ce9caf49c01de5fa5b828a23b0ab579d67a6ea87e9ee9b561c92")))
    print('PASS - step 1694')
except Exception as e:
    print('FAIL - step 1694' if isinstance(e, AssertionError) else f'ERROR - step 1694: {e}')

print("STEP 1695 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1695')
except Exception as e:
    print('FAIL - step 1695' if isinstance(e, AssertionError) else f'ERROR - step 1695: {e}')

print("STEP 1696 - Check element hp-image#None.['no-fade', 'c-image']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['no-fade', 'c-image']")))
    print('PASS - step 1696')
except Exception as e:
    print('FAIL - step 1696' if isinstance(e, AssertionError) else f'ERROR - step 1696: {e}')

print("STEP 1697 - Check element div#None.['titleAndText']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['titleAndText']")))
    print('PASS - step 1697')
except Exception as e:
    print('FAIL - step 1697' if isinstance(e, AssertionError) else f'ERROR - step 1697: {e}')

print("STEP 1698 - Check element hp-title-and-text#None.['c-title-and-text__wrapper', 'font-']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-title-and-text__wrapper', 'font-']")))
    print('PASS - step 1698')
except Exception as e:
    print('FAIL - step 1698' if isinstance(e, AssertionError) else f'ERROR - step 1698: {e}')

print("STEP 1699 - Check element div#None.['c-title-and-text', 'c-title-and-text--text-left', 'bg-', 'font-black', 'id_text_title_id5e0875a8ad563e01f5326f5ae9693d76ac4b627bcf1f05ac288708b3573a7c4e']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-title-and-text', 'c-title-and-text--text-left', 'bg-', 'font-black', 'id_text_title_id5e0875a8ad563e01f5326f5ae9693d76ac4b627bcf1f05ac288708b3573a7c4e']")))
    print('PASS - step 1699')
except Exception as e:
    print('FAIL - step 1699' if isinstance(e, AssertionError) else f'ERROR - step 1699: {e}')

print("STEP 1700 - Check element div#None.['c-title-and-text__title']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-title-and-text__title']")))
    print('PASS - step 1700')
except Exception as e:
    print('FAIL - step 1700' if isinstance(e, AssertionError) else f'ERROR - step 1700: {e}')

print("STEP 1701 - Check element h4#None.['h4']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['h4']")))
    print('PASS - step 1701')
except Exception as e:
    print('FAIL - step 1701' if isinstance(e, AssertionError) else f'ERROR - step 1701: {e}')

print("STEP 1702 - Check element div#None.['ctadropdownbutton']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ctadropdownbutton']")))
    print('PASS - step 1702')
except Exception as e:
    print('FAIL - step 1702' if isinstance(e, AssertionError) else f'ERROR - step 1702: {e}')

print("STEP 1703 - Check element div#None.['cta-dropdown-button', 'text-left', 'inline-container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['cta-dropdown-button', 'text-left', 'inline-container']")))
    print('PASS - step 1703')
except Exception as e:
    print('FAIL - step 1703' if isinstance(e, AssertionError) else f'ERROR - step 1703: {e}')

print("STEP 1704 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1704')
except Exception as e:
    print('FAIL - step 1704' if isinstance(e, AssertionError) else f'ERROR - step 1704: {e}')

print("STEP 1705 - Check element a#id7ddf0c2a19a2251fcb043b185de41a3f035303a380106c29b79ae8f31e6bfd36.['c-button', 'append-misc-url-params']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id7ddf0c2a19a2251fcb043b185de41a3f035303a380106c29b79ae8f31e6bfd36")))
    print('PASS - step 1705')
except Exception as e:
    print('FAIL - step 1705' if isinstance(e, AssertionError) else f'ERROR - step 1705: {e}')

print("STEP 1706 - Check element span#None.['c-button__text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-button__text']")))
    print('PASS - step 1706')
except Exception as e:
    print('FAIL - step 1706' if isinstance(e, AssertionError) else f'ERROR - step 1706: {e}')

print("STEP 1707 - Check element p#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "p")))
    print('PASS - step 1707')
except Exception as e:
    print('FAIL - step 1707' if isinstance(e, AssertionError) else f'ERROR - step 1707: {e}')

print("STEP 1708 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1708')
except Exception as e:
    print('FAIL - step 1708' if isinstance(e, AssertionError) else f'ERROR - step 1708: {e}')

print("STEP 1709 - Check element a#idaf8ba5b838cf851e4a4b31483993c0dd2445a1a4101766c012c1ee6edaec387d.['c-button-link-with-arrow', 'append-misc-url-params']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "idaf8ba5b838cf851e4a4b31483993c0dd2445a1a4101766c012c1ee6edaec387d")))
    print('PASS - step 1709')
except Exception as e:
    print('FAIL - step 1709' if isinstance(e, AssertionError) else f'ERROR - step 1709: {e}')

print("STEP 1710 - Check element span#None.['c-button__text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-button__text']")))
    print('PASS - step 1710')
except Exception as e:
    print('FAIL - step 1710' if isinstance(e, AssertionError) else f'ERROR - step 1710: {e}')

print("STEP 1711 - Check element p#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "p")))
    print('PASS - step 1711')
except Exception as e:
    print('FAIL - step 1711' if isinstance(e, AssertionError) else f'ERROR - step 1711: {e}')

print("STEP 1712 - Check element svg#None.['link-arrow-svg']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link-arrow-svg']")))
    print('PASS - step 1712')
except Exception as e:
    print('FAIL - step 1712' if isinstance(e, AssertionError) else f'ERROR - step 1712: {e}')

print("STEP 1713 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 1713')
except Exception as e:
    print('FAIL - step 1713' if isinstance(e, AssertionError) else f'ERROR - step 1713: {e}')

print("STEP 1714 - Check element div#None.['c-grid-cell', 'col-lg-4', 'col-md-6', 'col-sm-12', 'cell-id_grid_cell704c09369aa97139514715fdad5fe552de04b09ff614397bb9506ab38e2f19cc']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-grid-cell', 'col-lg-4', 'col-md-6', 'col-sm-12', 'cell-id_grid_cell704c09369aa97139514715fdad5fe552de04b09ff614397bb9506ab38e2f19cc']")))
    print('PASS - step 1714')
except Exception as e:
    print('FAIL - step 1714' if isinstance(e, AssertionError) else f'ERROR - step 1714: {e}')

print("STEP 1715 - Check element div#None.['image']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['image']")))
    print('PASS - step 1715')
except Exception as e:
    print('FAIL - step 1715' if isinstance(e, AssertionError) else f'ERROR - step 1715: {e}')

print("STEP 1716 - Check element div#id_image_id2e06a2e24baeb06f07b7514a22896c76e421528e4d61fd104dc7c803574d318c.['c-image-container', 'cmp-image', 'c-image-container--align-left']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id_image_id2e06a2e24baeb06f07b7514a22896c76e421528e4d61fd104dc7c803574d318c")))
    print('PASS - step 1716')
except Exception as e:
    print('FAIL - step 1716' if isinstance(e, AssertionError) else f'ERROR - step 1716: {e}')

print("STEP 1717 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1717')
except Exception as e:
    print('FAIL - step 1717' if isinstance(e, AssertionError) else f'ERROR - step 1717: {e}')

print("STEP 1718 - Check element hp-image#None.['no-fade', 'c-image']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['no-fade', 'c-image']")))
    print('PASS - step 1718')
except Exception as e:
    print('FAIL - step 1718' if isinstance(e, AssertionError) else f'ERROR - step 1718: {e}')

print("STEP 1719 - Check element div#None.['titleAndText']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['titleAndText']")))
    print('PASS - step 1719')
except Exception as e:
    print('FAIL - step 1719' if isinstance(e, AssertionError) else f'ERROR - step 1719: {e}')

print("STEP 1720 - Check element hp-title-and-text#None.['c-title-and-text__wrapper', 'font-']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-title-and-text__wrapper', 'font-']")))
    print('PASS - step 1720')
except Exception as e:
    print('FAIL - step 1720' if isinstance(e, AssertionError) else f'ERROR - step 1720: {e}')

print("STEP 1721 - Check element div#None.['c-title-and-text', 'c-title-and-text--text-left', 'bg-', 'font-black', 'id_text_title_id78e110d3c9610f2f524d1735fc50d724fd6b292de4a4410cb17636a1d8f72533']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-title-and-text', 'c-title-and-text--text-left', 'bg-', 'font-black', 'id_text_title_id78e110d3c9610f2f524d1735fc50d724fd6b292de4a4410cb17636a1d8f72533']")))
    print('PASS - step 1721')
except Exception as e:
    print('FAIL - step 1721' if isinstance(e, AssertionError) else f'ERROR - step 1721: {e}')

print("STEP 1722 - Check element div#None.['c-title-and-text__title']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-title-and-text__title']")))
    print('PASS - step 1722')
except Exception as e:
    print('FAIL - step 1722' if isinstance(e, AssertionError) else f'ERROR - step 1722: {e}')

print("STEP 1723 - Check element h4#None.['h4']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['h4']")))
    print('PASS - step 1723')
except Exception as e:
    print('FAIL - step 1723' if isinstance(e, AssertionError) else f'ERROR - step 1723: {e}')

print("STEP 1724 - Check element div#None.['ctadropdownbutton']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ctadropdownbutton']")))
    print('PASS - step 1724')
except Exception as e:
    print('FAIL - step 1724' if isinstance(e, AssertionError) else f'ERROR - step 1724: {e}')

print("STEP 1725 - Check element div#None.['cta-dropdown-button', 'text-left', 'inline-container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['cta-dropdown-button', 'text-left', 'inline-container']")))
    print('PASS - step 1725')
except Exception as e:
    print('FAIL - step 1725' if isinstance(e, AssertionError) else f'ERROR - step 1725: {e}')

print("STEP 1726 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1726')
except Exception as e:
    print('FAIL - step 1726' if isinstance(e, AssertionError) else f'ERROR - step 1726: {e}')

print("STEP 1727 - Check element a#ide55b111e556306466225a50a0e6acc624f770e43e5afbc226679535d2a835c64.['c-button', 'append-misc-url-params']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "ide55b111e556306466225a50a0e6acc624f770e43e5afbc226679535d2a835c64")))
    print('PASS - step 1727')
except Exception as e:
    print('FAIL - step 1727' if isinstance(e, AssertionError) else f'ERROR - step 1727: {e}')

print("STEP 1728 - Check element span#None.['c-button__text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-button__text']")))
    print('PASS - step 1728')
except Exception as e:
    print('FAIL - step 1728' if isinstance(e, AssertionError) else f'ERROR - step 1728: {e}')

print("STEP 1729 - Check element p#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "p")))
    print('PASS - step 1729')
except Exception as e:
    print('FAIL - step 1729' if isinstance(e, AssertionError) else f'ERROR - step 1729: {e}')

print("STEP 1730 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1730')
except Exception as e:
    print('FAIL - step 1730' if isinstance(e, AssertionError) else f'ERROR - step 1730: {e}')

print("STEP 1731 - Check element a#id20987c0e20406052df42d82e0857408077534d8bfa3d97a0c048f72ab12669f2.['c-button-link-with-arrow', 'append-misc-url-params']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id20987c0e20406052df42d82e0857408077534d8bfa3d97a0c048f72ab12669f2")))
    print('PASS - step 1731')
except Exception as e:
    print('FAIL - step 1731' if isinstance(e, AssertionError) else f'ERROR - step 1731: {e}')

print("STEP 1732 - Check element span#None.['c-button__text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-button__text']")))
    print('PASS - step 1732')
except Exception as e:
    print('FAIL - step 1732' if isinstance(e, AssertionError) else f'ERROR - step 1732: {e}')

print("STEP 1733 - Check element p#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "p")))
    print('PASS - step 1733')
except Exception as e:
    print('FAIL - step 1733' if isinstance(e, AssertionError) else f'ERROR - step 1733: {e}')

print("STEP 1734 - Check element svg#None.['link-arrow-svg']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link-arrow-svg']")))
    print('PASS - step 1734')
except Exception as e:
    print('FAIL - step 1734' if isinstance(e, AssertionError) else f'ERROR - step 1734: {e}')

print("STEP 1735 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 1735')
except Exception as e:
    print('FAIL - step 1735' if isinstance(e, AssertionError) else f'ERROR - step 1735: {e}')

print("STEP 1736 - Check element div#None.['c-grid-cell', 'col-lg-4', 'col-md-6', 'col-sm-12', 'cell-id_grid_cell045c4503be1cf5b4a565ebc89d9747447c980412d64ce2160681f1323857fedd']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-grid-cell', 'col-lg-4', 'col-md-6', 'col-sm-12', 'cell-id_grid_cell045c4503be1cf5b4a565ebc89d9747447c980412d64ce2160681f1323857fedd']")))
    print('PASS - step 1736')
except Exception as e:
    print('FAIL - step 1736' if isinstance(e, AssertionError) else f'ERROR - step 1736: {e}')

print("STEP 1737 - Check element div#None.['image']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['image']")))
    print('PASS - step 1737')
except Exception as e:
    print('FAIL - step 1737' if isinstance(e, AssertionError) else f'ERROR - step 1737: {e}')

print("STEP 1738 - Check element div#id_image_id6d33a071aeaed1e1b089b5a002cea93f56397e83658e60e422f55406ad4dc326.['c-image-container', 'cmp-image', 'c-image-container--align-left']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id_image_id6d33a071aeaed1e1b089b5a002cea93f56397e83658e60e422f55406ad4dc326")))
    print('PASS - step 1738')
except Exception as e:
    print('FAIL - step 1738' if isinstance(e, AssertionError) else f'ERROR - step 1738: {e}')

print("STEP 1739 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1739')
except Exception as e:
    print('FAIL - step 1739' if isinstance(e, AssertionError) else f'ERROR - step 1739: {e}')

print("STEP 1740 - Check element hp-image#None.['no-fade', 'c-image']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['no-fade', 'c-image']")))
    print('PASS - step 1740')
except Exception as e:
    print('FAIL - step 1740' if isinstance(e, AssertionError) else f'ERROR - step 1740: {e}')

print("STEP 1741 - Check element div#None.['titleAndText']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['titleAndText']")))
    print('PASS - step 1741')
except Exception as e:
    print('FAIL - step 1741' if isinstance(e, AssertionError) else f'ERROR - step 1741: {e}')

print("STEP 1742 - Check element hp-title-and-text#None.['c-title-and-text__wrapper', 'font-']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-title-and-text__wrapper', 'font-']")))
    print('PASS - step 1742')
except Exception as e:
    print('FAIL - step 1742' if isinstance(e, AssertionError) else f'ERROR - step 1742: {e}')

print("STEP 1743 - Check element div#None.['c-title-and-text', 'c-title-and-text--text-left', 'bg-', 'font-black', 'id_text_title_id9bac3c347fb3bd2f8c638d0a21283f7da06a3041f8cc2d10f421377a23d9e0bb']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-title-and-text', 'c-title-and-text--text-left', 'bg-', 'font-black', 'id_text_title_id9bac3c347fb3bd2f8c638d0a21283f7da06a3041f8cc2d10f421377a23d9e0bb']")))
    print('PASS - step 1743')
except Exception as e:
    print('FAIL - step 1743' if isinstance(e, AssertionError) else f'ERROR - step 1743: {e}')

print("STEP 1744 - Check element div#None.['c-title-and-text__title']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-title-and-text__title']")))
    print('PASS - step 1744')
except Exception as e:
    print('FAIL - step 1744' if isinstance(e, AssertionError) else f'ERROR - step 1744: {e}')

print("STEP 1745 - Check element h4#None.['h4']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['h4']")))
    print('PASS - step 1745')
except Exception as e:
    print('FAIL - step 1745' if isinstance(e, AssertionError) else f'ERROR - step 1745: {e}')

print("STEP 1746 - Check element div#None.['ctadropdownbutton']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ctadropdownbutton']")))
    print('PASS - step 1746')
except Exception as e:
    print('FAIL - step 1746' if isinstance(e, AssertionError) else f'ERROR - step 1746: {e}')

print("STEP 1747 - Check element div#None.['cta-dropdown-button', 'text-left', 'inline-container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['cta-dropdown-button', 'text-left', 'inline-container']")))
    print('PASS - step 1747')
except Exception as e:
    print('FAIL - step 1747' if isinstance(e, AssertionError) else f'ERROR - step 1747: {e}')

print("STEP 1748 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1748')
except Exception as e:
    print('FAIL - step 1748' if isinstance(e, AssertionError) else f'ERROR - step 1748: {e}')

print("STEP 1749 - Check element a#ida436ee962e1a6e910425f5e468ed6ce93cd66a596e1e6e30f1e04692c859a4c8.['c-button', 'append-misc-url-params']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "ida436ee962e1a6e910425f5e468ed6ce93cd66a596e1e6e30f1e04692c859a4c8")))
    print('PASS - step 1749')
except Exception as e:
    print('FAIL - step 1749' if isinstance(e, AssertionError) else f'ERROR - step 1749: {e}')

print("STEP 1750 - Check element span#None.['c-button__text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-button__text']")))
    print('PASS - step 1750')
except Exception as e:
    print('FAIL - step 1750' if isinstance(e, AssertionError) else f'ERROR - step 1750: {e}')

print("STEP 1751 - Check element p#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "p")))
    print('PASS - step 1751')
except Exception as e:
    print('FAIL - step 1751' if isinstance(e, AssertionError) else f'ERROR - step 1751: {e}')

print("STEP 1752 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1752')
except Exception as e:
    print('FAIL - step 1752' if isinstance(e, AssertionError) else f'ERROR - step 1752: {e}')

print("STEP 1753 - Check element a#ida4eb2ad7bee3f92489f9e4e68588faf7c579fd58014238aa1b0e1ead7a8f3c66.['c-button-link-with-arrow', 'append-misc-url-params']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "ida4eb2ad7bee3f92489f9e4e68588faf7c579fd58014238aa1b0e1ead7a8f3c66")))
    print('PASS - step 1753')
except Exception as e:
    print('FAIL - step 1753' if isinstance(e, AssertionError) else f'ERROR - step 1753: {e}')

print("STEP 1754 - Check element span#None.['c-button__text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-button__text']")))
    print('PASS - step 1754')
except Exception as e:
    print('FAIL - step 1754' if isinstance(e, AssertionError) else f'ERROR - step 1754: {e}')

print("STEP 1755 - Check element p#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "p")))
    print('PASS - step 1755')
except Exception as e:
    print('FAIL - step 1755' if isinstance(e, AssertionError) else f'ERROR - step 1755: {e}')

print("STEP 1756 - Check element svg#None.['link-arrow-svg']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link-arrow-svg']")))
    print('PASS - step 1756')
except Exception as e:
    print('FAIL - step 1756' if isinstance(e, AssertionError) else f'ERROR - step 1756: {e}')

print("STEP 1757 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 1757')
except Exception as e:
    print('FAIL - step 1757' if isinstance(e, AssertionError) else f'ERROR - step 1757: {e}')

print("STEP 1758 - Check element div#None.['ghost']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ghost']")))
    print('PASS - step 1758')
except Exception as e:
    print('FAIL - step 1758' if isinstance(e, AssertionError) else f'ERROR - step 1758: {e}')

print("STEP 1759 - Check element div#None.['c-visual-tabs-item__content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-visual-tabs-item__content']")))
    print('PASS - step 1759')
except Exception as e:
    print('FAIL - step 1759' if isinstance(e, AssertionError) else f'ERROR - step 1759: {e}')

print("STEP 1760 - Check element div#None.['grid']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['grid']")))
    print('PASS - step 1760')
except Exception as e:
    print('FAIL - step 1760' if isinstance(e, AssertionError) else f'ERROR - step 1760: {e}')

print("STEP 1761 - Check element hp-grid#None.['js-hp-component', 'hp-grid', 'id_grid861b4a3e22ae4893a61c5f92549a2163', 'js-hp-component-initialized']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['js-hp-component', 'hp-grid', 'id_grid861b4a3e22ae4893a61c5f92549a2163', 'js-hp-component-initialized']")))
    print('PASS - step 1761')
except Exception as e:
    print('FAIL - step 1761' if isinstance(e, AssertionError) else f'ERROR - step 1761: {e}')

print("STEP 1762 - Check element div#None.['container', 'id_grid_containerfd38ae9aa70447839b46a9a3b7ed5018']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['container', 'id_grid_containerfd38ae9aa70447839b46a9a3b7ed5018']")))
    print('PASS - step 1762')
except Exception as e:
    print('FAIL - step 1762' if isinstance(e, AssertionError) else f'ERROR - step 1762: {e}')

print("STEP 1763 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1763')
except Exception as e:
    print('FAIL - step 1763' if isinstance(e, AssertionError) else f'ERROR - step 1763: {e}')

print("STEP 1764 - Check element div#None.['row', 'justify-content-center', 'justify-content-lg-center', 'justify-content-md-center']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['row', 'justify-content-center', 'justify-content-lg-center', 'justify-content-md-center']")))
    print('PASS - step 1764')
except Exception as e:
    print('FAIL - step 1764' if isinstance(e, AssertionError) else f'ERROR - step 1764: {e}')

print("STEP 1765 - Check element div#None.['c-grid-cell', 'col-lg-4', 'col-md-6', 'col-sm-12', 'cell-id_grid_cell0137c51180dc9dce88f679a3826331b0af5ddf57fa7ea1b533b64d550b972dcc']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-grid-cell', 'col-lg-4', 'col-md-6', 'col-sm-12', 'cell-id_grid_cell0137c51180dc9dce88f679a3826331b0af5ddf57fa7ea1b533b64d550b972dcc']")))
    print('PASS - step 1765')
except Exception as e:
    print('FAIL - step 1765' if isinstance(e, AssertionError) else f'ERROR - step 1765: {e}')

print("STEP 1766 - Check element div#None.['image']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['image']")))
    print('PASS - step 1766')
except Exception as e:
    print('FAIL - step 1766' if isinstance(e, AssertionError) else f'ERROR - step 1766: {e}')

print("STEP 1767 - Check element div#id_image_id53de3691e758fa3719350513d1de392cdd837e0e83bb18a947959308a4b1bc7d.['c-image-container', 'cmp-image', 'c-image-container--align-left']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id_image_id53de3691e758fa3719350513d1de392cdd837e0e83bb18a947959308a4b1bc7d")))
    print('PASS - step 1767')
except Exception as e:
    print('FAIL - step 1767' if isinstance(e, AssertionError) else f'ERROR - step 1767: {e}')

print("STEP 1768 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1768')
except Exception as e:
    print('FAIL - step 1768' if isinstance(e, AssertionError) else f'ERROR - step 1768: {e}')

print("STEP 1769 - Check element hp-image#None.['no-fade', 'c-image']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['no-fade', 'c-image']")))
    print('PASS - step 1769')
except Exception as e:
    print('FAIL - step 1769' if isinstance(e, AssertionError) else f'ERROR - step 1769: {e}')

print("STEP 1770 - Check element div#None.['titleAndText']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['titleAndText']")))
    print('PASS - step 1770')
except Exception as e:
    print('FAIL - step 1770' if isinstance(e, AssertionError) else f'ERROR - step 1770: {e}')

print("STEP 1771 - Check element hp-title-and-text#None.['c-title-and-text__wrapper', 'font-']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-title-and-text__wrapper', 'font-']")))
    print('PASS - step 1771')
except Exception as e:
    print('FAIL - step 1771' if isinstance(e, AssertionError) else f'ERROR - step 1771: {e}')

print("STEP 1772 - Check element div#None.['c-title-and-text', 'c-title-and-text--text-left', 'bg-', 'font-black', 'id_text_title_id3e5baacd5f639bebd5caae5a97407e1c798b168fd9c5e48735edcbe53be20f9b']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-title-and-text', 'c-title-and-text--text-left', 'bg-', 'font-black', 'id_text_title_id3e5baacd5f639bebd5caae5a97407e1c798b168fd9c5e48735edcbe53be20f9b']")))
    print('PASS - step 1772')
except Exception as e:
    print('FAIL - step 1772' if isinstance(e, AssertionError) else f'ERROR - step 1772: {e}')

print("STEP 1773 - Check element div#None.['c-title-and-text__title']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-title-and-text__title']")))
    print('PASS - step 1773')
except Exception as e:
    print('FAIL - step 1773' if isinstance(e, AssertionError) else f'ERROR - step 1773: {e}')

print("STEP 1774 - Check element h4#None.['h4']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['h4']")))
    print('PASS - step 1774')
except Exception as e:
    print('FAIL - step 1774' if isinstance(e, AssertionError) else f'ERROR - step 1774: {e}')

print("STEP 1775 - Check element div#None.['ctadropdownbutton']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ctadropdownbutton']")))
    print('PASS - step 1775')
except Exception as e:
    print('FAIL - step 1775' if isinstance(e, AssertionError) else f'ERROR - step 1775: {e}')

print("STEP 1776 - Check element div#None.['cta-dropdown-button', 'text-left', 'inline-container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['cta-dropdown-button', 'text-left', 'inline-container']")))
    print('PASS - step 1776')
except Exception as e:
    print('FAIL - step 1776' if isinstance(e, AssertionError) else f'ERROR - step 1776: {e}')

print("STEP 1777 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1777')
except Exception as e:
    print('FAIL - step 1777' if isinstance(e, AssertionError) else f'ERROR - step 1777: {e}')

print("STEP 1778 - Check element a#id0549cb68c2f120074ddeeeba0440e6e730de3160d8d120bc9babe723e623baf4.['c-button', 'append-misc-url-params']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id0549cb68c2f120074ddeeeba0440e6e730de3160d8d120bc9babe723e623baf4")))
    print('PASS - step 1778')
except Exception as e:
    print('FAIL - step 1778' if isinstance(e, AssertionError) else f'ERROR - step 1778: {e}')

print("STEP 1779 - Check element span#None.['c-button__text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-button__text']")))
    print('PASS - step 1779')
except Exception as e:
    print('FAIL - step 1779' if isinstance(e, AssertionError) else f'ERROR - step 1779: {e}')

print("STEP 1780 - Check element p#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "p")))
    print('PASS - step 1780')
except Exception as e:
    print('FAIL - step 1780' if isinstance(e, AssertionError) else f'ERROR - step 1780: {e}')

print("STEP 1781 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1781')
except Exception as e:
    print('FAIL - step 1781' if isinstance(e, AssertionError) else f'ERROR - step 1781: {e}')

print("STEP 1782 - Check element a#id6d2449f2368b700ed02e757705912a07a643336eea14e07582d779bcfa97934f.['c-button-link-with-arrow', 'append-misc-url-params']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id6d2449f2368b700ed02e757705912a07a643336eea14e07582d779bcfa97934f")))
    print('PASS - step 1782')
except Exception as e:
    print('FAIL - step 1782' if isinstance(e, AssertionError) else f'ERROR - step 1782: {e}')

print("STEP 1783 - Check element span#None.['c-button__text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-button__text']")))
    print('PASS - step 1783')
except Exception as e:
    print('FAIL - step 1783' if isinstance(e, AssertionError) else f'ERROR - step 1783: {e}')

print("STEP 1784 - Check element p#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "p")))
    print('PASS - step 1784')
except Exception as e:
    print('FAIL - step 1784' if isinstance(e, AssertionError) else f'ERROR - step 1784: {e}')

print("STEP 1785 - Check element svg#None.['link-arrow-svg']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link-arrow-svg']")))
    print('PASS - step 1785')
except Exception as e:
    print('FAIL - step 1785' if isinstance(e, AssertionError) else f'ERROR - step 1785: {e}')

print("STEP 1786 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 1786')
except Exception as e:
    print('FAIL - step 1786' if isinstance(e, AssertionError) else f'ERROR - step 1786: {e}')

print("STEP 1787 - Check element div#None.['c-grid-cell', 'col-lg-4', 'col-md-6', 'col-sm-12', 'cell-id_grid_cellc88bf531b8d5be170579bf9fb47e020122cc6dcae441219220d7860705369ef9']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-grid-cell', 'col-lg-4', 'col-md-6', 'col-sm-12', 'cell-id_grid_cellc88bf531b8d5be170579bf9fb47e020122cc6dcae441219220d7860705369ef9']")))
    print('PASS - step 1787')
except Exception as e:
    print('FAIL - step 1787' if isinstance(e, AssertionError) else f'ERROR - step 1787: {e}')

print("STEP 1788 - Check element div#None.['image']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['image']")))
    print('PASS - step 1788')
except Exception as e:
    print('FAIL - step 1788' if isinstance(e, AssertionError) else f'ERROR - step 1788: {e}')

print("STEP 1789 - Check element div#id_image_id33a7b84c8ccf87532cdb59a1a193bc7f7d365ad10f6e5acb5d45884a0fbb052b.['c-image-container', 'cmp-image', 'c-image-container--align-left']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id_image_id33a7b84c8ccf87532cdb59a1a193bc7f7d365ad10f6e5acb5d45884a0fbb052b")))
    print('PASS - step 1789')
except Exception as e:
    print('FAIL - step 1789' if isinstance(e, AssertionError) else f'ERROR - step 1789: {e}')

print("STEP 1790 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1790')
except Exception as e:
    print('FAIL - step 1790' if isinstance(e, AssertionError) else f'ERROR - step 1790: {e}')

print("STEP 1791 - Check element hp-image#None.['no-fade', 'c-image']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['no-fade', 'c-image']")))
    print('PASS - step 1791')
except Exception as e:
    print('FAIL - step 1791' if isinstance(e, AssertionError) else f'ERROR - step 1791: {e}')

print("STEP 1792 - Check element div#None.['titleAndText']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['titleAndText']")))
    print('PASS - step 1792')
except Exception as e:
    print('FAIL - step 1792' if isinstance(e, AssertionError) else f'ERROR - step 1792: {e}')

print("STEP 1793 - Check element hp-title-and-text#None.['c-title-and-text__wrapper', 'font-']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-title-and-text__wrapper', 'font-']")))
    print('PASS - step 1793')
except Exception as e:
    print('FAIL - step 1793' if isinstance(e, AssertionError) else f'ERROR - step 1793: {e}')

print("STEP 1794 - Check element div#None.['c-title-and-text', 'c-title-and-text--text-left', 'bg-', 'font-black', 'id_text_title_id826b8045cbbb29288cb74c3dd519d975a5911ae35497e4ab970f8f7fa2b69844']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-title-and-text', 'c-title-and-text--text-left', 'bg-', 'font-black', 'id_text_title_id826b8045cbbb29288cb74c3dd519d975a5911ae35497e4ab970f8f7fa2b69844']")))
    print('PASS - step 1794')
except Exception as e:
    print('FAIL - step 1794' if isinstance(e, AssertionError) else f'ERROR - step 1794: {e}')

print("STEP 1795 - Check element div#None.['c-title-and-text__title']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-title-and-text__title']")))
    print('PASS - step 1795')
except Exception as e:
    print('FAIL - step 1795' if isinstance(e, AssertionError) else f'ERROR - step 1795: {e}')

print("STEP 1796 - Check element h4#None.['h4']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['h4']")))
    print('PASS - step 1796')
except Exception as e:
    print('FAIL - step 1796' if isinstance(e, AssertionError) else f'ERROR - step 1796: {e}')

print("STEP 1797 - Check element div#None.['ctadropdownbutton']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ctadropdownbutton']")))
    print('PASS - step 1797')
except Exception as e:
    print('FAIL - step 1797' if isinstance(e, AssertionError) else f'ERROR - step 1797: {e}')

print("STEP 1798 - Check element div#None.['cta-dropdown-button', 'text-left', 'stack-container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['cta-dropdown-button', 'text-left', 'stack-container']")))
    print('PASS - step 1798')
except Exception as e:
    print('FAIL - step 1798' if isinstance(e, AssertionError) else f'ERROR - step 1798: {e}')

print("STEP 1799 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1799')
except Exception as e:
    print('FAIL - step 1799' if isinstance(e, AssertionError) else f'ERROR - step 1799: {e}')

print("STEP 1800 - Check element a#id222086c174bf8895ebf958ff202f67a4b7555315b88d1cfbb74c7fd567d3770b.['c-button', 'stack', 'append-misc-url-params']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id222086c174bf8895ebf958ff202f67a4b7555315b88d1cfbb74c7fd567d3770b")))
    print('PASS - step 1800')
except Exception as e:
    print('FAIL - step 1800' if isinstance(e, AssertionError) else f'ERROR - step 1800: {e}')

print("STEP 1801 - Check element span#None.['c-button__text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-button__text']")))
    print('PASS - step 1801')
except Exception as e:
    print('FAIL - step 1801' if isinstance(e, AssertionError) else f'ERROR - step 1801: {e}')

print("STEP 1802 - Check element p#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "p")))
    print('PASS - step 1802')
except Exception as e:
    print('FAIL - step 1802' if isinstance(e, AssertionError) else f'ERROR - step 1802: {e}')

print("STEP 1803 - Check element div#None.['c-grid-cell', 'col-lg-4', 'col-md-6', 'col-sm-12', 'cell-id_grid_cell5eedad75f4e27f4cce142691a190c8b1a0aceaff501de7a615a9947e86f14254']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-grid-cell', 'col-lg-4', 'col-md-6', 'col-sm-12', 'cell-id_grid_cell5eedad75f4e27f4cce142691a190c8b1a0aceaff501de7a615a9947e86f14254']")))
    print('PASS - step 1803')
except Exception as e:
    print('FAIL - step 1803' if isinstance(e, AssertionError) else f'ERROR - step 1803: {e}')

print("STEP 1804 - Check element div#None.['image']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['image']")))
    print('PASS - step 1804')
except Exception as e:
    print('FAIL - step 1804' if isinstance(e, AssertionError) else f'ERROR - step 1804: {e}')

print("STEP 1805 - Check element div#id_image_idb39ba92d0be3f942f978d77833c3ad856d3962f918b7c397396200983d5254ec.['c-image-container', 'cmp-image', 'c-image-container--align-left']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id_image_idb39ba92d0be3f942f978d77833c3ad856d3962f918b7c397396200983d5254ec")))
    print('PASS - step 1805')
except Exception as e:
    print('FAIL - step 1805' if isinstance(e, AssertionError) else f'ERROR - step 1805: {e}')

print("STEP 1806 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1806')
except Exception as e:
    print('FAIL - step 1806' if isinstance(e, AssertionError) else f'ERROR - step 1806: {e}')

print("STEP 1807 - Check element hp-image#None.['no-fade', 'c-image']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['no-fade', 'c-image']")))
    print('PASS - step 1807')
except Exception as e:
    print('FAIL - step 1807' if isinstance(e, AssertionError) else f'ERROR - step 1807: {e}')

print("STEP 1808 - Check element div#None.['titleAndText']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['titleAndText']")))
    print('PASS - step 1808')
except Exception as e:
    print('FAIL - step 1808' if isinstance(e, AssertionError) else f'ERROR - step 1808: {e}')

print("STEP 1809 - Check element hp-title-and-text#None.['c-title-and-text__wrapper', 'font-']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-title-and-text__wrapper', 'font-']")))
    print('PASS - step 1809')
except Exception as e:
    print('FAIL - step 1809' if isinstance(e, AssertionError) else f'ERROR - step 1809: {e}')

print("STEP 1810 - Check element div#None.['c-title-and-text', 'c-title-and-text--text-left', 'bg-', 'font-black', 'id_text_title_id6f91456702e8000edf256a00672bd4db5923e621b3abf8faa82a40277f01e152']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-title-and-text', 'c-title-and-text--text-left', 'bg-', 'font-black', 'id_text_title_id6f91456702e8000edf256a00672bd4db5923e621b3abf8faa82a40277f01e152']")))
    print('PASS - step 1810')
except Exception as e:
    print('FAIL - step 1810' if isinstance(e, AssertionError) else f'ERROR - step 1810: {e}')

print("STEP 1811 - Check element div#None.['c-title-and-text__title']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-title-and-text__title']")))
    print('PASS - step 1811')
except Exception as e:
    print('FAIL - step 1811' if isinstance(e, AssertionError) else f'ERROR - step 1811: {e}')

print("STEP 1812 - Check element h4#None.['h4']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['h4']")))
    print('PASS - step 1812')
except Exception as e:
    print('FAIL - step 1812' if isinstance(e, AssertionError) else f'ERROR - step 1812: {e}')

print("STEP 1813 - Check element div#None.['ctadropdownbutton']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ctadropdownbutton']")))
    print('PASS - step 1813')
except Exception as e:
    print('FAIL - step 1813' if isinstance(e, AssertionError) else f'ERROR - step 1813: {e}')

print("STEP 1814 - Check element div#None.['cta-dropdown-button', 'text-left', 'inline-container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['cta-dropdown-button', 'text-left', 'inline-container']")))
    print('PASS - step 1814')
except Exception as e:
    print('FAIL - step 1814' if isinstance(e, AssertionError) else f'ERROR - step 1814: {e}')

print("STEP 1815 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1815')
except Exception as e:
    print('FAIL - step 1815' if isinstance(e, AssertionError) else f'ERROR - step 1815: {e}')

print("STEP 1816 - Check element a#id41ea7fb800e6cae756d8504bc5c5f2b2460f228b7a19a1243ade4ad370883270.['c-button', 'append-misc-url-params']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id41ea7fb800e6cae756d8504bc5c5f2b2460f228b7a19a1243ade4ad370883270")))
    print('PASS - step 1816')
except Exception as e:
    print('FAIL - step 1816' if isinstance(e, AssertionError) else f'ERROR - step 1816: {e}')

print("STEP 1817 - Check element span#None.['c-button__text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-button__text']")))
    print('PASS - step 1817')
except Exception as e:
    print('FAIL - step 1817' if isinstance(e, AssertionError) else f'ERROR - step 1817: {e}')

print("STEP 1818 - Check element p#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "p")))
    print('PASS - step 1818')
except Exception as e:
    print('FAIL - step 1818' if isinstance(e, AssertionError) else f'ERROR - step 1818: {e}')

print("STEP 1819 - Check element div#None.['c-grid-cell', 'col-lg-4', 'col-md-6', 'col-sm-12', 'cell-id_grid_cellc6743fbca160abe7840615e28021925cbcb2ff7b01d4f225f3e380b920dccfed']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-grid-cell', 'col-lg-4', 'col-md-6', 'col-sm-12', 'cell-id_grid_cellc6743fbca160abe7840615e28021925cbcb2ff7b01d4f225f3e380b920dccfed']")))
    print('PASS - step 1819')
except Exception as e:
    print('FAIL - step 1819' if isinstance(e, AssertionError) else f'ERROR - step 1819: {e}')

print("STEP 1820 - Check element div#None.['image']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['image']")))
    print('PASS - step 1820')
except Exception as e:
    print('FAIL - step 1820' if isinstance(e, AssertionError) else f'ERROR - step 1820: {e}')

print("STEP 1821 - Check element div#id_image_id7e1be536a78d003a3e29f40c5f5d4b2d021d693c647b181b75d5194358d9a1b6.['c-image-container', 'cmp-image', 'c-image-container--align-left']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id_image_id7e1be536a78d003a3e29f40c5f5d4b2d021d693c647b181b75d5194358d9a1b6")))
    print('PASS - step 1821')
except Exception as e:
    print('FAIL - step 1821' if isinstance(e, AssertionError) else f'ERROR - step 1821: {e}')

print("STEP 1822 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1822')
except Exception as e:
    print('FAIL - step 1822' if isinstance(e, AssertionError) else f'ERROR - step 1822: {e}')

print("STEP 1823 - Check element hp-image#None.['no-fade', 'c-image']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['no-fade', 'c-image']")))
    print('PASS - step 1823')
except Exception as e:
    print('FAIL - step 1823' if isinstance(e, AssertionError) else f'ERROR - step 1823: {e}')

print("STEP 1824 - Check element div#None.['titleAndText']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['titleAndText']")))
    print('PASS - step 1824')
except Exception as e:
    print('FAIL - step 1824' if isinstance(e, AssertionError) else f'ERROR - step 1824: {e}')

print("STEP 1825 - Check element hp-title-and-text#None.['c-title-and-text__wrapper', 'font-']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-title-and-text__wrapper', 'font-']")))
    print('PASS - step 1825')
except Exception as e:
    print('FAIL - step 1825' if isinstance(e, AssertionError) else f'ERROR - step 1825: {e}')

print("STEP 1826 - Check element div#None.['c-title-and-text', 'c-title-and-text--text-left', 'bg-', 'font-black', 'id_text_title_id63974f16378dc38e3ea7ece4496ce999a100db31e17650f3340f4a1750512683']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-title-and-text', 'c-title-and-text--text-left', 'bg-', 'font-black', 'id_text_title_id63974f16378dc38e3ea7ece4496ce999a100db31e17650f3340f4a1750512683']")))
    print('PASS - step 1826')
except Exception as e:
    print('FAIL - step 1826' if isinstance(e, AssertionError) else f'ERROR - step 1826: {e}')

print("STEP 1827 - Check element div#None.['c-title-and-text__title']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-title-and-text__title']")))
    print('PASS - step 1827')
except Exception as e:
    print('FAIL - step 1827' if isinstance(e, AssertionError) else f'ERROR - step 1827: {e}')

print("STEP 1828 - Check element h4#None.['h4']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['h4']")))
    print('PASS - step 1828')
except Exception as e:
    print('FAIL - step 1828' if isinstance(e, AssertionError) else f'ERROR - step 1828: {e}')

print("STEP 1829 - Check element div#None.['ctadropdownbutton']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ctadropdownbutton']")))
    print('PASS - step 1829')
except Exception as e:
    print('FAIL - step 1829' if isinstance(e, AssertionError) else f'ERROR - step 1829: {e}')

print("STEP 1830 - Check element div#None.['cta-dropdown-button', 'text-left', 'inline-container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['cta-dropdown-button', 'text-left', 'inline-container']")))
    print('PASS - step 1830')
except Exception as e:
    print('FAIL - step 1830' if isinstance(e, AssertionError) else f'ERROR - step 1830: {e}')

print("STEP 1831 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1831')
except Exception as e:
    print('FAIL - step 1831' if isinstance(e, AssertionError) else f'ERROR - step 1831: {e}')

print("STEP 1832 - Check element a#id6e7e0a7b0552d59268c1e329f0bad4455a0357d3822d4cf9c796a35bfe7840cf.['c-button', 'append-misc-url-params']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id6e7e0a7b0552d59268c1e329f0bad4455a0357d3822d4cf9c796a35bfe7840cf")))
    print('PASS - step 1832')
except Exception as e:
    print('FAIL - step 1832' if isinstance(e, AssertionError) else f'ERROR - step 1832: {e}')

print("STEP 1833 - Check element span#None.['c-button__text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-button__text']")))
    print('PASS - step 1833')
except Exception as e:
    print('FAIL - step 1833' if isinstance(e, AssertionError) else f'ERROR - step 1833: {e}')

print("STEP 1834 - Check element p#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "p")))
    print('PASS - step 1834')
except Exception as e:
    print('FAIL - step 1834' if isinstance(e, AssertionError) else f'ERROR - step 1834: {e}')

print("STEP 1835 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1835')
except Exception as e:
    print('FAIL - step 1835' if isinstance(e, AssertionError) else f'ERROR - step 1835: {e}')

print("STEP 1836 - Check element a#idbbd61b03077c46f23cae5f8e95f0c1a5ee944ad9b12fedf127d64bb7a34e8441.['c-button-link-with-arrow', 'append-misc-url-params']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "idbbd61b03077c46f23cae5f8e95f0c1a5ee944ad9b12fedf127d64bb7a34e8441")))
    print('PASS - step 1836')
except Exception as e:
    print('FAIL - step 1836' if isinstance(e, AssertionError) else f'ERROR - step 1836: {e}')

print("STEP 1837 - Check element span#None.['c-button__text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-button__text']")))
    print('PASS - step 1837')
except Exception as e:
    print('FAIL - step 1837' if isinstance(e, AssertionError) else f'ERROR - step 1837: {e}')

print("STEP 1838 - Check element p#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "p")))
    print('PASS - step 1838')
except Exception as e:
    print('FAIL - step 1838' if isinstance(e, AssertionError) else f'ERROR - step 1838: {e}')

print("STEP 1839 - Check element svg#None.['link-arrow-svg']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link-arrow-svg']")))
    print('PASS - step 1839')
except Exception as e:
    print('FAIL - step 1839' if isinstance(e, AssertionError) else f'ERROR - step 1839: {e}')

print("STEP 1840 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 1840')
except Exception as e:
    print('FAIL - step 1840' if isinstance(e, AssertionError) else f'ERROR - step 1840: {e}')

print("STEP 1841 - Check element div#None.['c-grid-cell', 'col-lg-4', 'col-md-6', 'col-sm-12', 'cell-id_grid_cell60a963de9707284d62a42b640fbdf6ac7f7810188745ccabc7c6949a67c15486']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-grid-cell', 'col-lg-4', 'col-md-6', 'col-sm-12', 'cell-id_grid_cell60a963de9707284d62a42b640fbdf6ac7f7810188745ccabc7c6949a67c15486']")))
    print('PASS - step 1841')
except Exception as e:
    print('FAIL - step 1841' if isinstance(e, AssertionError) else f'ERROR - step 1841: {e}')

print("STEP 1842 - Check element div#None.['image']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['image']")))
    print('PASS - step 1842')
except Exception as e:
    print('FAIL - step 1842' if isinstance(e, AssertionError) else f'ERROR - step 1842: {e}')

print("STEP 1843 - Check element div#id_image_id2488dba06bbe05952eb3c5640ae1df8297a5791edf2187d6f30acf438c7030f5.['c-image-container', 'cmp-image', 'c-image-container--align-left']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id_image_id2488dba06bbe05952eb3c5640ae1df8297a5791edf2187d6f30acf438c7030f5")))
    print('PASS - step 1843')
except Exception as e:
    print('FAIL - step 1843' if isinstance(e, AssertionError) else f'ERROR - step 1843: {e}')

print("STEP 1844 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1844')
except Exception as e:
    print('FAIL - step 1844' if isinstance(e, AssertionError) else f'ERROR - step 1844: {e}')

print("STEP 1845 - Check element hp-image#None.['no-fade', 'c-image']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['no-fade', 'c-image']")))
    print('PASS - step 1845')
except Exception as e:
    print('FAIL - step 1845' if isinstance(e, AssertionError) else f'ERROR - step 1845: {e}')

print("STEP 1846 - Check element div#None.['titleAndText']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['titleAndText']")))
    print('PASS - step 1846')
except Exception as e:
    print('FAIL - step 1846' if isinstance(e, AssertionError) else f'ERROR - step 1846: {e}')

print("STEP 1847 - Check element hp-title-and-text#None.['c-title-and-text__wrapper', 'font-']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-title-and-text__wrapper', 'font-']")))
    print('PASS - step 1847')
except Exception as e:
    print('FAIL - step 1847' if isinstance(e, AssertionError) else f'ERROR - step 1847: {e}')

print("STEP 1848 - Check element div#None.['c-title-and-text', 'c-title-and-text--text-left', 'bg-', 'font-black', 'id_text_title_idc7d6e3a1632ad1ac44b5d60f3872975e17951f1ceeb9d440e15789e4427ee3f6']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-title-and-text', 'c-title-and-text--text-left', 'bg-', 'font-black', 'id_text_title_idc7d6e3a1632ad1ac44b5d60f3872975e17951f1ceeb9d440e15789e4427ee3f6']")))
    print('PASS - step 1848')
except Exception as e:
    print('FAIL - step 1848' if isinstance(e, AssertionError) else f'ERROR - step 1848: {e}')

print("STEP 1849 - Check element div#None.['c-title-and-text__title']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-title-and-text__title']")))
    print('PASS - step 1849')
except Exception as e:
    print('FAIL - step 1849' if isinstance(e, AssertionError) else f'ERROR - step 1849: {e}')

print("STEP 1850 - Check element h4#None.['h4']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['h4']")))
    print('PASS - step 1850')
except Exception as e:
    print('FAIL - step 1850' if isinstance(e, AssertionError) else f'ERROR - step 1850: {e}')

print("STEP 1851 - Check element div#None.['ctadropdownbutton']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ctadropdownbutton']")))
    print('PASS - step 1851')
except Exception as e:
    print('FAIL - step 1851' if isinstance(e, AssertionError) else f'ERROR - step 1851: {e}')

print("STEP 1852 - Check element div#None.['cta-dropdown-button', 'text-left', 'inline-container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['cta-dropdown-button', 'text-left', 'inline-container']")))
    print('PASS - step 1852')
except Exception as e:
    print('FAIL - step 1852' if isinstance(e, AssertionError) else f'ERROR - step 1852: {e}')

print("STEP 1853 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1853')
except Exception as e:
    print('FAIL - step 1853' if isinstance(e, AssertionError) else f'ERROR - step 1853: {e}')

print("STEP 1854 - Check element a#id191dd90dcf0bf37d3042e68d964d328b53cc3599654ecfa7dd8c420239e37dd1.['c-button', 'append-misc-url-params']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id191dd90dcf0bf37d3042e68d964d328b53cc3599654ecfa7dd8c420239e37dd1")))
    print('PASS - step 1854')
except Exception as e:
    print('FAIL - step 1854' if isinstance(e, AssertionError) else f'ERROR - step 1854: {e}')

print("STEP 1855 - Check element span#None.['c-button__text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-button__text']")))
    print('PASS - step 1855')
except Exception as e:
    print('FAIL - step 1855' if isinstance(e, AssertionError) else f'ERROR - step 1855: {e}')

print("STEP 1856 - Check element p#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "p")))
    print('PASS - step 1856')
except Exception as e:
    print('FAIL - step 1856' if isinstance(e, AssertionError) else f'ERROR - step 1856: {e}')

print("STEP 1857 - Check element div#None.['c-grid-cell', 'col-lg-4', 'col-md-6', 'col-sm-12', 'cell-id_grid_cellacbe910e58e3b4c52967f8bc43979a55ee0bc89a0507364a735d5c0eb1475bf9']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-grid-cell', 'col-lg-4', 'col-md-6', 'col-sm-12', 'cell-id_grid_cellacbe910e58e3b4c52967f8bc43979a55ee0bc89a0507364a735d5c0eb1475bf9']")))
    print('PASS - step 1857')
except Exception as e:
    print('FAIL - step 1857' if isinstance(e, AssertionError) else f'ERROR - step 1857: {e}')

print("STEP 1858 - Check element div#None.['image']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['image']")))
    print('PASS - step 1858')
except Exception as e:
    print('FAIL - step 1858' if isinstance(e, AssertionError) else f'ERROR - step 1858: {e}')

print("STEP 1859 - Check element div#id_image_id099fb8642c9ddb046df7c2b18f6bfb91a10999b5cab93ca14492276846f5dee1.['c-image-container', 'cmp-image', 'c-image-container--align-left']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id_image_id099fb8642c9ddb046df7c2b18f6bfb91a10999b5cab93ca14492276846f5dee1")))
    print('PASS - step 1859')
except Exception as e:
    print('FAIL - step 1859' if isinstance(e, AssertionError) else f'ERROR - step 1859: {e}')

print("STEP 1860 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1860')
except Exception as e:
    print('FAIL - step 1860' if isinstance(e, AssertionError) else f'ERROR - step 1860: {e}')

print("STEP 1861 - Check element hp-image#None.['no-fade', 'c-image']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['no-fade', 'c-image']")))
    print('PASS - step 1861')
except Exception as e:
    print('FAIL - step 1861' if isinstance(e, AssertionError) else f'ERROR - step 1861: {e}')

print("STEP 1862 - Check element div#None.['titleAndText']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['titleAndText']")))
    print('PASS - step 1862')
except Exception as e:
    print('FAIL - step 1862' if isinstance(e, AssertionError) else f'ERROR - step 1862: {e}')

print("STEP 1863 - Check element hp-title-and-text#None.['c-title-and-text__wrapper', 'font-']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-title-and-text__wrapper', 'font-']")))
    print('PASS - step 1863')
except Exception as e:
    print('FAIL - step 1863' if isinstance(e, AssertionError) else f'ERROR - step 1863: {e}')

print("STEP 1864 - Check element div#None.['c-title-and-text', 'c-title-and-text--text-left', 'bg-', 'font-black', 'id_text_title_id0c9d59b86978f599f88d85cb9eb8487380c48cee8ec6101870d17cf568c1620b']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-title-and-text', 'c-title-and-text--text-left', 'bg-', 'font-black', 'id_text_title_id0c9d59b86978f599f88d85cb9eb8487380c48cee8ec6101870d17cf568c1620b']")))
    print('PASS - step 1864')
except Exception as e:
    print('FAIL - step 1864' if isinstance(e, AssertionError) else f'ERROR - step 1864: {e}')

print("STEP 1865 - Check element div#None.['c-title-and-text__title']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-title-and-text__title']")))
    print('PASS - step 1865')
except Exception as e:
    print('FAIL - step 1865' if isinstance(e, AssertionError) else f'ERROR - step 1865: {e}')

print("STEP 1866 - Check element h4#None.['h4']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['h4']")))
    print('PASS - step 1866')
except Exception as e:
    print('FAIL - step 1866' if isinstance(e, AssertionError) else f'ERROR - step 1866: {e}')

print("STEP 1867 - Check element div#None.['ctadropdownbutton']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ctadropdownbutton']")))
    print('PASS - step 1867')
except Exception as e:
    print('FAIL - step 1867' if isinstance(e, AssertionError) else f'ERROR - step 1867: {e}')

print("STEP 1868 - Check element div#None.['cta-dropdown-button', 'text-left', 'inline-container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['cta-dropdown-button', 'text-left', 'inline-container']")))
    print('PASS - step 1868')
except Exception as e:
    print('FAIL - step 1868' if isinstance(e, AssertionError) else f'ERROR - step 1868: {e}')

print("STEP 1869 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1869')
except Exception as e:
    print('FAIL - step 1869' if isinstance(e, AssertionError) else f'ERROR - step 1869: {e}')

print("STEP 1870 - Check element a#id2e890e5b2c25f94747cd8e6e02aeca3fc011150e6502c2010398904f914ef2d1.['c-button', 'append-misc-url-params']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id2e890e5b2c25f94747cd8e6e02aeca3fc011150e6502c2010398904f914ef2d1")))
    print('PASS - step 1870')
except Exception as e:
    print('FAIL - step 1870' if isinstance(e, AssertionError) else f'ERROR - step 1870: {e}')

print("STEP 1871 - Check element span#None.['c-button__text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-button__text']")))
    print('PASS - step 1871')
except Exception as e:
    print('FAIL - step 1871' if isinstance(e, AssertionError) else f'ERROR - step 1871: {e}')

print("STEP 1872 - Check element p#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "p")))
    print('PASS - step 1872')
except Exception as e:
    print('FAIL - step 1872' if isinstance(e, AssertionError) else f'ERROR - step 1872: {e}')

print("STEP 1873 - Check element div#None.['backgroundContainer', 'aem-GridColumn', 'aem-GridColumn--default--12']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['backgroundContainer', 'aem-GridColumn', 'aem-GridColumn--default--12']")))
    print('PASS - step 1873')
except Exception as e:
    print('FAIL - step 1873' if isinstance(e, AssertionError) else f'ERROR - step 1873: {e}')

print("STEP 1874 - Check element section#id_-6171161.['c-bg-container']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id_-6171161")))
    print('PASS - step 1874')
except Exception as e:
    print('FAIL - step 1874' if isinstance(e, AssertionError) else f'ERROR - step 1874: {e}')

print("STEP 1875 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1875')
except Exception as e:
    print('FAIL - step 1875' if isinstance(e, AssertionError) else f'ERROR - step 1875: {e}')

print("STEP 1876 - Check element div#None.['c-bg-container__media-wrapper', 'c-video-container--align-center']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-bg-container__media-wrapper', 'c-video-container--align-center']")))
    print('PASS - step 1876')
except Exception as e:
    print('FAIL - step 1876' if isinstance(e, AssertionError) else f'ERROR - step 1876: {e}')

print("STEP 1877 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 1877')
except Exception as e:
    print('FAIL - step 1877' if isinstance(e, AssertionError) else f'ERROR - step 1877: {e}')

print("STEP 1878 - Check element div#None.['c-bg-container__content', 'full-width']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-bg-container__content', 'full-width']")))
    print('PASS - step 1878')
except Exception as e:
    print('FAIL - step 1878' if isinstance(e, AssertionError) else f'ERROR - step 1878: {e}')

print("STEP 1879 - Check element div#None.['c-bg-container__content-holder']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-bg-container__content-holder']")))
    print('PASS - step 1879')
except Exception as e:
    print('FAIL - step 1879' if isinstance(e, AssertionError) else f'ERROR - step 1879: {e}')

print("STEP 1880 - Check element div#None.['ghost', 'aem-GridColumn', 'aem-GridColumn--default--12']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ghost', 'aem-GridColumn', 'aem-GridColumn--default--12']")))
    print('PASS - step 1880')
except Exception as e:
    print('FAIL - step 1880' if isinstance(e, AssertionError) else f'ERROR - step 1880: {e}')

print("STEP 1881 - Check element section#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "section")))
    print('PASS - step 1881')
except Exception as e:
    print('FAIL - step 1881' if isinstance(e, AssertionError) else f'ERROR - step 1881: {e}')

print("STEP 1882 - Check element div#footer.['footer']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "footer")))
    print('PASS - step 1882')
except Exception as e:
    print('FAIL - step 1882' if isinstance(e, AssertionError) else f'ERROR - step 1882: {e}')

print("STEP 1883 - Check element div#None.['aem_country_selection_wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_country_selection_wrapper']")))
    print('PASS - step 1883')
except Exception as e:
    print('FAIL - step 1883' if isinstance(e, AssertionError) else f'ERROR - step 1883: {e}')

print("STEP 1884 - Check element div#None.['aem_footer_language_selection_container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_footer_language_selection_container']")))
    print('PASS - step 1884')
except Exception as e:
    print('FAIL - step 1884' if isinstance(e, AssertionError) else f'ERROR - step 1884: {e}')

print("STEP 1885 - Check element div#None.['aem_closing_overlay_mobile']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_closing_overlay_mobile']")))
    print('PASS - step 1885')
except Exception as e:
    print('FAIL - step 1885' if isinstance(e, AssertionError) else f'ERROR - step 1885: {e}')

print("STEP 1886 - Check element div#test_sidebar.['aem_test_sidebar']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "test_sidebar")))
    print('PASS - step 1886')
except Exception as e:
    print('FAIL - step 1886' if isinstance(e, AssertionError) else f'ERROR - step 1886: {e}')

print("STEP 1887 - Check element div#None.['aem_mobile_country_header']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_mobile_country_header']")))
    print('PASS - step 1887')
except Exception as e:
    print('FAIL - step 1887' if isinstance(e, AssertionError) else f'ERROR - step 1887: {e}')

print("STEP 1888 - Check element h2#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h2")))
    print('PASS - step 1888')
except Exception as e:
    print('FAIL - step 1888' if isinstance(e, AssertionError) else f'ERROR - step 1888: {e}')

print("STEP 1889 - Check element a#None.['aem_close_btn_mobile_countries']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_close_btn_mobile_countries']")))
    print('PASS - step 1889')
except Exception as e:
    print('FAIL - step 1889' if isinstance(e, AssertionError) else f'ERROR - step 1889: {e}')

print("STEP 1890 - Check element span#None.['aem_screenReadingText']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_screenReadingText']")))
    print('PASS - step 1890')
except Exception as e:
    print('FAIL - step 1890' if isinstance(e, AssertionError) else f'ERROR - step 1890: {e}')

print("STEP 1891 - Check element div#None.['aem_country_options']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_country_options']")))
    print('PASS - step 1891')
except Exception as e:
    print('FAIL - step 1891' if isinstance(e, AssertionError) else f'ERROR - step 1891: {e}')

print("STEP 1892 - Check element div#id_acc_0.['aem_country_sel_cont']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id_acc_0")))
    print('PASS - step 1892')
except Exception as e:
    print('FAIL - step 1892' if isinstance(e, AssertionError) else f'ERROR - step 1892: {e}')

print("STEP 1893 - Check element a#None.['aem_country_sel_cont_header', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_country_sel_cont_header', 'unselectable']")))
    print('PASS - step 1893')
except Exception as e:
    print('FAIL - step 1893' if isinstance(e, AssertionError) else f'ERROR - step 1893: {e}')

print("STEP 1894 - Check element span#None.['aem_accordion-header']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_accordion-header']")))
    print('PASS - step 1894')
except Exception as e:
    print('FAIL - step 1894' if isinstance(e, AssertionError) else f'ERROR - step 1894: {e}')

print("STEP 1895 - Check element span#None.['aem_accordian_arrow_icon_country']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_accordian_arrow_icon_country']")))
    print('PASS - step 1895')
except Exception as e:
    print('FAIL - step 1895' if isinstance(e, AssertionError) else f'ERROR - step 1895: {e}')

print("STEP 1896 - Check element ul#None.['aem_tab_list_country_selec']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_tab_list_country_selec']")))
    print('PASS - step 1896')
except Exception as e:
    print('FAIL - step 1896' if isinstance(e, AssertionError) else f'ERROR - step 1896: {e}')

print("STEP 1897 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 1897')
except Exception as e:
    print('FAIL - step 1897' if isinstance(e, AssertionError) else f'ERROR - step 1897: {e}')

print("STEP 1898 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 1898')
except Exception as e:
    print('FAIL - step 1898' if isinstance(e, AssertionError) else f'ERROR - step 1898: {e}')

print("STEP 1899 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 1899')
except Exception as e:
    print('FAIL - step 1899' if isinstance(e, AssertionError) else f'ERROR - step 1899: {e}')

print("STEP 1900 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 1900')
except Exception as e:
    print('FAIL - step 1900' if isinstance(e, AssertionError) else f'ERROR - step 1900: {e}')

print("STEP 1901 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 1901')
except Exception as e:
    print('FAIL - step 1901' if isinstance(e, AssertionError) else f'ERROR - step 1901: {e}')

print("STEP 1902 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 1902')
except Exception as e:
    print('FAIL - step 1902' if isinstance(e, AssertionError) else f'ERROR - step 1902: {e}')

print("STEP 1903 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 1903')
except Exception as e:
    print('FAIL - step 1903' if isinstance(e, AssertionError) else f'ERROR - step 1903: {e}')

print("STEP 1904 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 1904')
except Exception as e:
    print('FAIL - step 1904' if isinstance(e, AssertionError) else f'ERROR - step 1904: {e}')

print("STEP 1905 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 1905')
except Exception as e:
    print('FAIL - step 1905' if isinstance(e, AssertionError) else f'ERROR - step 1905: {e}')

print("STEP 1906 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 1906')
except Exception as e:
    print('FAIL - step 1906' if isinstance(e, AssertionError) else f'ERROR - step 1906: {e}')

print("STEP 1907 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 1907')
except Exception as e:
    print('FAIL - step 1907' if isinstance(e, AssertionError) else f'ERROR - step 1907: {e}')

print("STEP 1908 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 1908')
except Exception as e:
    print('FAIL - step 1908' if isinstance(e, AssertionError) else f'ERROR - step 1908: {e}')

print("STEP 1909 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 1909')
except Exception as e:
    print('FAIL - step 1909' if isinstance(e, AssertionError) else f'ERROR - step 1909: {e}')

print("STEP 1910 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 1910')
except Exception as e:
    print('FAIL - step 1910' if isinstance(e, AssertionError) else f'ERROR - step 1910: {e}')

print("STEP 1911 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 1911')
except Exception as e:
    print('FAIL - step 1911' if isinstance(e, AssertionError) else f'ERROR - step 1911: {e}')

print("STEP 1912 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 1912')
except Exception as e:
    print('FAIL - step 1912' if isinstance(e, AssertionError) else f'ERROR - step 1912: {e}')

print("STEP 1913 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 1913')
except Exception as e:
    print('FAIL - step 1913' if isinstance(e, AssertionError) else f'ERROR - step 1913: {e}')

print("STEP 1914 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 1914')
except Exception as e:
    print('FAIL - step 1914' if isinstance(e, AssertionError) else f'ERROR - step 1914: {e}')

print("STEP 1915 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 1915')
except Exception as e:
    print('FAIL - step 1915' if isinstance(e, AssertionError) else f'ERROR - step 1915: {e}')

print("STEP 1916 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 1916')
except Exception as e:
    print('FAIL - step 1916' if isinstance(e, AssertionError) else f'ERROR - step 1916: {e}')

print("STEP 1917 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 1917')
except Exception as e:
    print('FAIL - step 1917' if isinstance(e, AssertionError) else f'ERROR - step 1917: {e}')

print("STEP 1918 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 1918')
except Exception as e:
    print('FAIL - step 1918' if isinstance(e, AssertionError) else f'ERROR - step 1918: {e}')

print("STEP 1919 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 1919')
except Exception as e:
    print('FAIL - step 1919' if isinstance(e, AssertionError) else f'ERROR - step 1919: {e}')

print("STEP 1920 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 1920')
except Exception as e:
    print('FAIL - step 1920' if isinstance(e, AssertionError) else f'ERROR - step 1920: {e}')

print("STEP 1921 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 1921')
except Exception as e:
    print('FAIL - step 1921' if isinstance(e, AssertionError) else f'ERROR - step 1921: {e}')

print("STEP 1922 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 1922')
except Exception as e:
    print('FAIL - step 1922' if isinstance(e, AssertionError) else f'ERROR - step 1922: {e}')

print("STEP 1923 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 1923')
except Exception as e:
    print('FAIL - step 1923' if isinstance(e, AssertionError) else f'ERROR - step 1923: {e}')

print("STEP 1924 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 1924')
except Exception as e:
    print('FAIL - step 1924' if isinstance(e, AssertionError) else f'ERROR - step 1924: {e}')

print("STEP 1925 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 1925')
except Exception as e:
    print('FAIL - step 1925' if isinstance(e, AssertionError) else f'ERROR - step 1925: {e}')

print("STEP 1926 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 1926')
except Exception as e:
    print('FAIL - step 1926' if isinstance(e, AssertionError) else f'ERROR - step 1926: {e}')

print("STEP 1927 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 1927')
except Exception as e:
    print('FAIL - step 1927' if isinstance(e, AssertionError) else f'ERROR - step 1927: {e}')

print("STEP 1928 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 1928')
except Exception as e:
    print('FAIL - step 1928' if isinstance(e, AssertionError) else f'ERROR - step 1928: {e}')

print("STEP 1929 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 1929')
except Exception as e:
    print('FAIL - step 1929' if isinstance(e, AssertionError) else f'ERROR - step 1929: {e}')

print("STEP 1930 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 1930')
except Exception as e:
    print('FAIL - step 1930' if isinstance(e, AssertionError) else f'ERROR - step 1930: {e}')

print("STEP 1931 - Check element div#None.['aem_country_options']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_country_options']")))
    print('PASS - step 1931')
except Exception as e:
    print('FAIL - step 1931' if isinstance(e, AssertionError) else f'ERROR - step 1931: {e}')

print("STEP 1932 - Check element div#id_acc_1.['aem_country_sel_cont']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id_acc_1")))
    print('PASS - step 1932')
except Exception as e:
    print('FAIL - step 1932' if isinstance(e, AssertionError) else f'ERROR - step 1932: {e}')

print("STEP 1933 - Check element a#None.['aem_country_sel_cont_header', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_country_sel_cont_header', 'unselectable']")))
    print('PASS - step 1933')
except Exception as e:
    print('FAIL - step 1933' if isinstance(e, AssertionError) else f'ERROR - step 1933: {e}')

print("STEP 1934 - Check element span#None.['aem_accordion-header']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_accordion-header']")))
    print('PASS - step 1934')
except Exception as e:
    print('FAIL - step 1934' if isinstance(e, AssertionError) else f'ERROR - step 1934: {e}')

print("STEP 1935 - Check element span#None.['aem_accordian_arrow_icon_country']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_accordian_arrow_icon_country']")))
    print('PASS - step 1935')
except Exception as e:
    print('FAIL - step 1935' if isinstance(e, AssertionError) else f'ERROR - step 1935: {e}')

print("STEP 1936 - Check element ul#None.['aem_tab_list_country_selec']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_tab_list_country_selec']")))
    print('PASS - step 1936')
except Exception as e:
    print('FAIL - step 1936' if isinstance(e, AssertionError) else f'ERROR - step 1936: {e}')

print("STEP 1937 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 1937')
except Exception as e:
    print('FAIL - step 1937' if isinstance(e, AssertionError) else f'ERROR - step 1937: {e}')

print("STEP 1938 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 1938')
except Exception as e:
    print('FAIL - step 1938' if isinstance(e, AssertionError) else f'ERROR - step 1938: {e}')

print("STEP 1939 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 1939')
except Exception as e:
    print('FAIL - step 1939' if isinstance(e, AssertionError) else f'ERROR - step 1939: {e}')

print("STEP 1940 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 1940')
except Exception as e:
    print('FAIL - step 1940' if isinstance(e, AssertionError) else f'ERROR - step 1940: {e}')

print("STEP 1941 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 1941')
except Exception as e:
    print('FAIL - step 1941' if isinstance(e, AssertionError) else f'ERROR - step 1941: {e}')

print("STEP 1942 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 1942')
except Exception as e:
    print('FAIL - step 1942' if isinstance(e, AssertionError) else f'ERROR - step 1942: {e}')

print("STEP 1943 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 1943')
except Exception as e:
    print('FAIL - step 1943' if isinstance(e, AssertionError) else f'ERROR - step 1943: {e}')

print("STEP 1944 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 1944')
except Exception as e:
    print('FAIL - step 1944' if isinstance(e, AssertionError) else f'ERROR - step 1944: {e}')

print("STEP 1945 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 1945')
except Exception as e:
    print('FAIL - step 1945' if isinstance(e, AssertionError) else f'ERROR - step 1945: {e}')

print("STEP 1946 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 1946')
except Exception as e:
    print('FAIL - step 1946' if isinstance(e, AssertionError) else f'ERROR - step 1946: {e}')

print("STEP 1947 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 1947')
except Exception as e:
    print('FAIL - step 1947' if isinstance(e, AssertionError) else f'ERROR - step 1947: {e}')

print("STEP 1948 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 1948')
except Exception as e:
    print('FAIL - step 1948' if isinstance(e, AssertionError) else f'ERROR - step 1948: {e}')

print("STEP 1949 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 1949')
except Exception as e:
    print('FAIL - step 1949' if isinstance(e, AssertionError) else f'ERROR - step 1949: {e}')

print("STEP 1950 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 1950')
except Exception as e:
    print('FAIL - step 1950' if isinstance(e, AssertionError) else f'ERROR - step 1950: {e}')

print("STEP 1951 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 1951')
except Exception as e:
    print('FAIL - step 1951' if isinstance(e, AssertionError) else f'ERROR - step 1951: {e}')

print("STEP 1952 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 1952')
except Exception as e:
    print('FAIL - step 1952' if isinstance(e, AssertionError) else f'ERROR - step 1952: {e}')

print("STEP 1953 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 1953')
except Exception as e:
    print('FAIL - step 1953' if isinstance(e, AssertionError) else f'ERROR - step 1953: {e}')

print("STEP 1954 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 1954')
except Exception as e:
    print('FAIL - step 1954' if isinstance(e, AssertionError) else f'ERROR - step 1954: {e}')

print("STEP 1955 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 1955')
except Exception as e:
    print('FAIL - step 1955' if isinstance(e, AssertionError) else f'ERROR - step 1955: {e}')

print("STEP 1956 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 1956')
except Exception as e:
    print('FAIL - step 1956' if isinstance(e, AssertionError) else f'ERROR - step 1956: {e}')

print("STEP 1957 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 1957')
except Exception as e:
    print('FAIL - step 1957' if isinstance(e, AssertionError) else f'ERROR - step 1957: {e}')

print("STEP 1958 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 1958')
except Exception as e:
    print('FAIL - step 1958' if isinstance(e, AssertionError) else f'ERROR - step 1958: {e}')

print("STEP 1959 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 1959')
except Exception as e:
    print('FAIL - step 1959' if isinstance(e, AssertionError) else f'ERROR - step 1959: {e}')

print("STEP 1960 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 1960')
except Exception as e:
    print('FAIL - step 1960' if isinstance(e, AssertionError) else f'ERROR - step 1960: {e}')

print("STEP 1961 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 1961')
except Exception as e:
    print('FAIL - step 1961' if isinstance(e, AssertionError) else f'ERROR - step 1961: {e}')

print("STEP 1962 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 1962')
except Exception as e:
    print('FAIL - step 1962' if isinstance(e, AssertionError) else f'ERROR - step 1962: {e}')

print("STEP 1963 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 1963')
except Exception as e:
    print('FAIL - step 1963' if isinstance(e, AssertionError) else f'ERROR - step 1963: {e}')

print("STEP 1964 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 1964')
except Exception as e:
    print('FAIL - step 1964' if isinstance(e, AssertionError) else f'ERROR - step 1964: {e}')

print("STEP 1965 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 1965')
except Exception as e:
    print('FAIL - step 1965' if isinstance(e, AssertionError) else f'ERROR - step 1965: {e}')

print("STEP 1966 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 1966')
except Exception as e:
    print('FAIL - step 1966' if isinstance(e, AssertionError) else f'ERROR - step 1966: {e}')

print("STEP 1967 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 1967')
except Exception as e:
    print('FAIL - step 1967' if isinstance(e, AssertionError) else f'ERROR - step 1967: {e}')

print("STEP 1968 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 1968')
except Exception as e:
    print('FAIL - step 1968' if isinstance(e, AssertionError) else f'ERROR - step 1968: {e}')

print("STEP 1969 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 1969')
except Exception as e:
    print('FAIL - step 1969' if isinstance(e, AssertionError) else f'ERROR - step 1969: {e}')

print("STEP 1970 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 1970')
except Exception as e:
    print('FAIL - step 1970' if isinstance(e, AssertionError) else f'ERROR - step 1970: {e}')

print("STEP 1971 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 1971')
except Exception as e:
    print('FAIL - step 1971' if isinstance(e, AssertionError) else f'ERROR - step 1971: {e}')

print("STEP 1972 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 1972')
except Exception as e:
    print('FAIL - step 1972' if isinstance(e, AssertionError) else f'ERROR - step 1972: {e}')

print("STEP 1973 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 1973')
except Exception as e:
    print('FAIL - step 1973' if isinstance(e, AssertionError) else f'ERROR - step 1973: {e}')

print("STEP 1974 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 1974')
except Exception as e:
    print('FAIL - step 1974' if isinstance(e, AssertionError) else f'ERROR - step 1974: {e}')

print("STEP 1975 - Check element div#None.['aem_country_options']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_country_options']")))
    print('PASS - step 1975')
except Exception as e:
    print('FAIL - step 1975' if isinstance(e, AssertionError) else f'ERROR - step 1975: {e}')

print("STEP 1976 - Check element div#id_acc_2.['aem_country_sel_cont']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id_acc_2")))
    print('PASS - step 1976')
except Exception as e:
    print('FAIL - step 1976' if isinstance(e, AssertionError) else f'ERROR - step 1976: {e}')

print("STEP 1977 - Check element a#None.['aem_country_sel_cont_header', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_country_sel_cont_header', 'unselectable']")))
    print('PASS - step 1977')
except Exception as e:
    print('FAIL - step 1977' if isinstance(e, AssertionError) else f'ERROR - step 1977: {e}')

print("STEP 1978 - Check element span#None.['aem_accordion-header']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_accordion-header']")))
    print('PASS - step 1978')
except Exception as e:
    print('FAIL - step 1978' if isinstance(e, AssertionError) else f'ERROR - step 1978: {e}')

print("STEP 1979 - Check element span#None.['aem_accordian_arrow_icon_country']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_accordian_arrow_icon_country']")))
    print('PASS - step 1979')
except Exception as e:
    print('FAIL - step 1979' if isinstance(e, AssertionError) else f'ERROR - step 1979: {e}')

print("STEP 1980 - Check element ul#None.['aem_tab_list_country_selec']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_tab_list_country_selec']")))
    print('PASS - step 1980')
except Exception as e:
    print('FAIL - step 1980' if isinstance(e, AssertionError) else f'ERROR - step 1980: {e}')

print("STEP 1981 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 1981')
except Exception as e:
    print('FAIL - step 1981' if isinstance(e, AssertionError) else f'ERROR - step 1981: {e}')

print("STEP 1982 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 1982')
except Exception as e:
    print('FAIL - step 1982' if isinstance(e, AssertionError) else f'ERROR - step 1982: {e}')

print("STEP 1983 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 1983')
except Exception as e:
    print('FAIL - step 1983' if isinstance(e, AssertionError) else f'ERROR - step 1983: {e}')

print("STEP 1984 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 1984')
except Exception as e:
    print('FAIL - step 1984' if isinstance(e, AssertionError) else f'ERROR - step 1984: {e}')

print("STEP 1985 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 1985')
except Exception as e:
    print('FAIL - step 1985' if isinstance(e, AssertionError) else f'ERROR - step 1985: {e}')

print("STEP 1986 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 1986')
except Exception as e:
    print('FAIL - step 1986' if isinstance(e, AssertionError) else f'ERROR - step 1986: {e}')

print("STEP 1987 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 1987')
except Exception as e:
    print('FAIL - step 1987' if isinstance(e, AssertionError) else f'ERROR - step 1987: {e}')

print("STEP 1988 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 1988')
except Exception as e:
    print('FAIL - step 1988' if isinstance(e, AssertionError) else f'ERROR - step 1988: {e}')

print("STEP 1989 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 1989')
except Exception as e:
    print('FAIL - step 1989' if isinstance(e, AssertionError) else f'ERROR - step 1989: {e}')

print("STEP 1990 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 1990')
except Exception as e:
    print('FAIL - step 1990' if isinstance(e, AssertionError) else f'ERROR - step 1990: {e}')

print("STEP 1991 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 1991')
except Exception as e:
    print('FAIL - step 1991' if isinstance(e, AssertionError) else f'ERROR - step 1991: {e}')

print("STEP 1992 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 1992')
except Exception as e:
    print('FAIL - step 1992' if isinstance(e, AssertionError) else f'ERROR - step 1992: {e}')

print("STEP 1993 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 1993')
except Exception as e:
    print('FAIL - step 1993' if isinstance(e, AssertionError) else f'ERROR - step 1993: {e}')

print("STEP 1994 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 1994')
except Exception as e:
    print('FAIL - step 1994' if isinstance(e, AssertionError) else f'ERROR - step 1994: {e}')

print("STEP 1995 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 1995')
except Exception as e:
    print('FAIL - step 1995' if isinstance(e, AssertionError) else f'ERROR - step 1995: {e}')

print("STEP 1996 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 1996')
except Exception as e:
    print('FAIL - step 1996' if isinstance(e, AssertionError) else f'ERROR - step 1996: {e}')

print("STEP 1997 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 1997')
except Exception as e:
    print('FAIL - step 1997' if isinstance(e, AssertionError) else f'ERROR - step 1997: {e}')

print("STEP 1998 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 1998')
except Exception as e:
    print('FAIL - step 1998' if isinstance(e, AssertionError) else f'ERROR - step 1998: {e}')

print("STEP 1999 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 1999')
except Exception as e:
    print('FAIL - step 1999' if isinstance(e, AssertionError) else f'ERROR - step 1999: {e}')

print("STEP 2000 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 2000')
except Exception as e:
    print('FAIL - step 2000' if isinstance(e, AssertionError) else f'ERROR - step 2000: {e}')

print("STEP 2001 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2001')
except Exception as e:
    print('FAIL - step 2001' if isinstance(e, AssertionError) else f'ERROR - step 2001: {e}')

print("STEP 2002 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 2002')
except Exception as e:
    print('FAIL - step 2002' if isinstance(e, AssertionError) else f'ERROR - step 2002: {e}')

print("STEP 2003 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2003')
except Exception as e:
    print('FAIL - step 2003' if isinstance(e, AssertionError) else f'ERROR - step 2003: {e}')

print("STEP 2004 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 2004')
except Exception as e:
    print('FAIL - step 2004' if isinstance(e, AssertionError) else f'ERROR - step 2004: {e}')

print("STEP 2005 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2005')
except Exception as e:
    print('FAIL - step 2005' if isinstance(e, AssertionError) else f'ERROR - step 2005: {e}')

print("STEP 2006 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 2006')
except Exception as e:
    print('FAIL - step 2006' if isinstance(e, AssertionError) else f'ERROR - step 2006: {e}')

print("STEP 2007 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2007')
except Exception as e:
    print('FAIL - step 2007' if isinstance(e, AssertionError) else f'ERROR - step 2007: {e}')

print("STEP 2008 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 2008')
except Exception as e:
    print('FAIL - step 2008' if isinstance(e, AssertionError) else f'ERROR - step 2008: {e}')

print("STEP 2009 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2009')
except Exception as e:
    print('FAIL - step 2009' if isinstance(e, AssertionError) else f'ERROR - step 2009: {e}')

print("STEP 2010 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 2010')
except Exception as e:
    print('FAIL - step 2010' if isinstance(e, AssertionError) else f'ERROR - step 2010: {e}')

print("STEP 2011 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2011')
except Exception as e:
    print('FAIL - step 2011' if isinstance(e, AssertionError) else f'ERROR - step 2011: {e}')

print("STEP 2012 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 2012')
except Exception as e:
    print('FAIL - step 2012' if isinstance(e, AssertionError) else f'ERROR - step 2012: {e}')

print("STEP 2013 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2013')
except Exception as e:
    print('FAIL - step 2013' if isinstance(e, AssertionError) else f'ERROR - step 2013: {e}')

print("STEP 2014 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 2014')
except Exception as e:
    print('FAIL - step 2014' if isinstance(e, AssertionError) else f'ERROR - step 2014: {e}')

print("STEP 2015 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2015')
except Exception as e:
    print('FAIL - step 2015' if isinstance(e, AssertionError) else f'ERROR - step 2015: {e}')

print("STEP 2016 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 2016')
except Exception as e:
    print('FAIL - step 2016' if isinstance(e, AssertionError) else f'ERROR - step 2016: {e}')

print("STEP 2017 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2017')
except Exception as e:
    print('FAIL - step 2017' if isinstance(e, AssertionError) else f'ERROR - step 2017: {e}')

print("STEP 2018 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 2018')
except Exception as e:
    print('FAIL - step 2018' if isinstance(e, AssertionError) else f'ERROR - step 2018: {e}')

print("STEP 2019 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2019')
except Exception as e:
    print('FAIL - step 2019' if isinstance(e, AssertionError) else f'ERROR - step 2019: {e}')

print("STEP 2020 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 2020')
except Exception as e:
    print('FAIL - step 2020' if isinstance(e, AssertionError) else f'ERROR - step 2020: {e}')

print("STEP 2021 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2021')
except Exception as e:
    print('FAIL - step 2021' if isinstance(e, AssertionError) else f'ERROR - step 2021: {e}')

print("STEP 2022 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 2022')
except Exception as e:
    print('FAIL - step 2022' if isinstance(e, AssertionError) else f'ERROR - step 2022: {e}')

print("STEP 2023 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2023')
except Exception as e:
    print('FAIL - step 2023' if isinstance(e, AssertionError) else f'ERROR - step 2023: {e}')

print("STEP 2024 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 2024')
except Exception as e:
    print('FAIL - step 2024' if isinstance(e, AssertionError) else f'ERROR - step 2024: {e}')

print("STEP 2025 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2025')
except Exception as e:
    print('FAIL - step 2025' if isinstance(e, AssertionError) else f'ERROR - step 2025: {e}')

print("STEP 2026 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 2026')
except Exception as e:
    print('FAIL - step 2026' if isinstance(e, AssertionError) else f'ERROR - step 2026: {e}')

print("STEP 2027 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2027')
except Exception as e:
    print('FAIL - step 2027' if isinstance(e, AssertionError) else f'ERROR - step 2027: {e}')

print("STEP 2028 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 2028')
except Exception as e:
    print('FAIL - step 2028' if isinstance(e, AssertionError) else f'ERROR - step 2028: {e}')

print("STEP 2029 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2029')
except Exception as e:
    print('FAIL - step 2029' if isinstance(e, AssertionError) else f'ERROR - step 2029: {e}')

print("STEP 2030 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 2030')
except Exception as e:
    print('FAIL - step 2030' if isinstance(e, AssertionError) else f'ERROR - step 2030: {e}')

print("STEP 2031 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2031')
except Exception as e:
    print('FAIL - step 2031' if isinstance(e, AssertionError) else f'ERROR - step 2031: {e}')

print("STEP 2032 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 2032')
except Exception as e:
    print('FAIL - step 2032' if isinstance(e, AssertionError) else f'ERROR - step 2032: {e}')

print("STEP 2033 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2033')
except Exception as e:
    print('FAIL - step 2033' if isinstance(e, AssertionError) else f'ERROR - step 2033: {e}')

print("STEP 2034 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 2034')
except Exception as e:
    print('FAIL - step 2034' if isinstance(e, AssertionError) else f'ERROR - step 2034: {e}')

print("STEP 2035 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2035')
except Exception as e:
    print('FAIL - step 2035' if isinstance(e, AssertionError) else f'ERROR - step 2035: {e}')

print("STEP 2036 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 2036')
except Exception as e:
    print('FAIL - step 2036' if isinstance(e, AssertionError) else f'ERROR - step 2036: {e}')

print("STEP 2037 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2037')
except Exception as e:
    print('FAIL - step 2037' if isinstance(e, AssertionError) else f'ERROR - step 2037: {e}')

print("STEP 2038 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 2038')
except Exception as e:
    print('FAIL - step 2038' if isinstance(e, AssertionError) else f'ERROR - step 2038: {e}')

print("STEP 2039 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2039')
except Exception as e:
    print('FAIL - step 2039' if isinstance(e, AssertionError) else f'ERROR - step 2039: {e}')

print("STEP 2040 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 2040')
except Exception as e:
    print('FAIL - step 2040' if isinstance(e, AssertionError) else f'ERROR - step 2040: {e}')

print("STEP 2041 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2041')
except Exception as e:
    print('FAIL - step 2041' if isinstance(e, AssertionError) else f'ERROR - step 2041: {e}')

print("STEP 2042 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 2042')
except Exception as e:
    print('FAIL - step 2042' if isinstance(e, AssertionError) else f'ERROR - step 2042: {e}')

print("STEP 2043 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2043')
except Exception as e:
    print('FAIL - step 2043' if isinstance(e, AssertionError) else f'ERROR - step 2043: {e}')

print("STEP 2044 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 2044')
except Exception as e:
    print('FAIL - step 2044' if isinstance(e, AssertionError) else f'ERROR - step 2044: {e}')

print("STEP 2045 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2045')
except Exception as e:
    print('FAIL - step 2045' if isinstance(e, AssertionError) else f'ERROR - step 2045: {e}')

print("STEP 2046 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 2046')
except Exception as e:
    print('FAIL - step 2046' if isinstance(e, AssertionError) else f'ERROR - step 2046: {e}')

print("STEP 2047 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2047')
except Exception as e:
    print('FAIL - step 2047' if isinstance(e, AssertionError) else f'ERROR - step 2047: {e}')

print("STEP 2048 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 2048')
except Exception as e:
    print('FAIL - step 2048' if isinstance(e, AssertionError) else f'ERROR - step 2048: {e}')

print("STEP 2049 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2049')
except Exception as e:
    print('FAIL - step 2049' if isinstance(e, AssertionError) else f'ERROR - step 2049: {e}')

print("STEP 2050 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 2050')
except Exception as e:
    print('FAIL - step 2050' if isinstance(e, AssertionError) else f'ERROR - step 2050: {e}')

print("STEP 2051 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2051')
except Exception as e:
    print('FAIL - step 2051' if isinstance(e, AssertionError) else f'ERROR - step 2051: {e}')

print("STEP 2052 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 2052')
except Exception as e:
    print('FAIL - step 2052' if isinstance(e, AssertionError) else f'ERROR - step 2052: {e}')

print("STEP 2053 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2053')
except Exception as e:
    print('FAIL - step 2053' if isinstance(e, AssertionError) else f'ERROR - step 2053: {e}')

print("STEP 2054 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 2054')
except Exception as e:
    print('FAIL - step 2054' if isinstance(e, AssertionError) else f'ERROR - step 2054: {e}')

print("STEP 2055 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2055')
except Exception as e:
    print('FAIL - step 2055' if isinstance(e, AssertionError) else f'ERROR - step 2055: {e}')

print("STEP 2056 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 2056')
except Exception as e:
    print('FAIL - step 2056' if isinstance(e, AssertionError) else f'ERROR - step 2056: {e}')

print("STEP 2057 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2057')
except Exception as e:
    print('FAIL - step 2057' if isinstance(e, AssertionError) else f'ERROR - step 2057: {e}')

print("STEP 2058 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 2058')
except Exception as e:
    print('FAIL - step 2058' if isinstance(e, AssertionError) else f'ERROR - step 2058: {e}')

print("STEP 2059 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2059')
except Exception as e:
    print('FAIL - step 2059' if isinstance(e, AssertionError) else f'ERROR - step 2059: {e}')

print("STEP 2060 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 2060')
except Exception as e:
    print('FAIL - step 2060' if isinstance(e, AssertionError) else f'ERROR - step 2060: {e}')

print("STEP 2061 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2061')
except Exception as e:
    print('FAIL - step 2061' if isinstance(e, AssertionError) else f'ERROR - step 2061: {e}')

print("STEP 2062 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 2062')
except Exception as e:
    print('FAIL - step 2062' if isinstance(e, AssertionError) else f'ERROR - step 2062: {e}')

print("STEP 2063 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2063')
except Exception as e:
    print('FAIL - step 2063' if isinstance(e, AssertionError) else f'ERROR - step 2063: {e}')

print("STEP 2064 - Check element a#None.['aem_link_country_selec', 'no-outline', 'unselectable']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_link_country_selec', 'no-outline', 'unselectable']")))
    print('PASS - step 2064')
except Exception as e:
    print('FAIL - step 2064' if isinstance(e, AssertionError) else f'ERROR - step 2064: {e}')

print("STEP 2065 - Check element a#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "a")))
    print('PASS - step 2065')
except Exception as e:
    print('FAIL - step 2065' if isinstance(e, AssertionError) else f'ERROR - step 2065: {e}')

print("STEP 2066 - Check element span#None.['aem_screenReadingText']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_screenReadingText']")))
    print('PASS - step 2066')
except Exception as e:
    print('FAIL - step 2066' if isinstance(e, AssertionError) else f'ERROR - step 2066: {e}')

print("STEP 2067 - Check element div#None.['aem_footer_language_selection_section', 'aem_hf_clf']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_footer_language_selection_section', 'aem_hf_clf']")))
    print('PASS - step 2067')
except Exception as e:
    print('FAIL - step 2067' if isinstance(e, AssertionError) else f'ERROR - step 2067: {e}')

print("STEP 2068 - Check element div#None.['aem_right_corner']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_right_corner']")))
    print('PASS - step 2068')
except Exception as e:
    print('FAIL - step 2068' if isinstance(e, AssertionError) else f'ERROR - step 2068: {e}')

print("STEP 2069 - Check element div#None.['aem_country_selctor_container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_country_selctor_container']")))
    print('PASS - step 2069')
except Exception as e:
    print('FAIL - step 2069' if isinstance(e, AssertionError) else f'ERROR - step 2069: {e}')

print("STEP 2070 - Check element div#None.['aem_js_cselector', 'aem_country_selector_wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_js_cselector', 'aem_country_selector_wrapper']")))
    print('PASS - step 2070')
except Exception as e:
    print('FAIL - step 2070' if isinstance(e, AssertionError) else f'ERROR - step 2070: {e}')

print("STEP 2071 - Check element a#None.['aem_js_cselector_trigger', 'aem_country_selector', 'aem_country_selected']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_js_cselector_trigger', 'aem_country_selector', 'aem_country_selected']")))
    print('PASS - step 2071')
except Exception as e:
    print('FAIL - step 2071' if isinstance(e, AssertionError) else f'ERROR - step 2071: {e}')

print("STEP 2072 - Check element span#None.['aem_countryRegionLabel']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_countryRegionLabel']")))
    print('PASS - step 2072')
except Exception as e:
    print('FAIL - step 2072' if isinstance(e, AssertionError) else f'ERROR - step 2072: {e}')

print("STEP 2073 - Check element span#None.['aem_screenReadingText', 'aem_js_screen_reading']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_screenReadingText', 'aem_js_screen_reading']")))
    print('PASS - step 2073')
except Exception as e:
    print('FAIL - step 2073' if isinstance(e, AssertionError) else f'ERROR - step 2073: {e}')

print("STEP 2074 - Check element span#None.['aem_flag']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_flag']")))
    print('PASS - step 2074')
except Exception as e:
    print('FAIL - step 2074' if isinstance(e, AssertionError) else f'ERROR - step 2074: {e}')

print("STEP 2075 - Check element span#None.['aem_selCountry']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_selCountry']")))
    print('PASS - step 2075')
except Exception as e:
    print('FAIL - step 2075' if isinstance(e, AssertionError) else f'ERROR - step 2075: {e}')

print("STEP 2076 - Check element span#None.['aem_screenReadingText']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_screenReadingText']")))
    print('PASS - step 2076')
except Exception as e:
    print('FAIL - step 2076' if isinstance(e, AssertionError) else f'ERROR - step 2076: {e}')

print("STEP 2077 - Check element div#None.['aem_worldmap_container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_worldmap_container']")))
    print('PASS - step 2077')
except Exception as e:
    print('FAIL - step 2077' if isinstance(e, AssertionError) else f'ERROR - step 2077: {e}')

print("STEP 2078 - Check element div#None.['aem_world_map', 'aem_js_cselector_target']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_world_map', 'aem_js_cselector_target']")))
    print('PASS - step 2078')
except Exception as e:
    print('FAIL - step 2078' if isinstance(e, AssertionError) else f'ERROR - step 2078: {e}')

print("STEP 2079 - Check element div#None.['aem_shadow_cover_top']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_shadow_cover_top']")))
    print('PASS - step 2079')
except Exception as e:
    print('FAIL - step 2079' if isinstance(e, AssertionError) else f'ERROR - step 2079: {e}')

print("STEP 2080 - Check element h4#None.['aem_screenReadingText']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_screenReadingText']")))
    print('PASS - step 2080')
except Exception as e:
    print('FAIL - step 2080' if isinstance(e, AssertionError) else f'ERROR - step 2080: {e}')

print("STEP 2081 - Check element div#None.['aem_js_worldmap_container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_js_worldmap_container']")))
    print('PASS - step 2081')
except Exception as e:
    print('FAIL - step 2081' if isinstance(e, AssertionError) else f'ERROR - step 2081: {e}')

print("STEP 2082 - Check element div#None.['aem_div_worldmap', 'w-flag']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_div_worldmap', 'w-flag']")))
    print('PASS - step 2082')
except Exception as e:
    print('FAIL - step 2082' if isinstance(e, AssertionError) else f'ERROR - step 2082: {e}')

print("STEP 2083 - Check element div#None.['aem_popup_b_corner']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_popup_b_corner']")))
    print('PASS - step 2083')
except Exception as e:
    print('FAIL - step 2083' if isinstance(e, AssertionError) else f'ERROR - step 2083: {e}')

print("STEP 2084 - Check element span#None.['aem_screenReadingText']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_screenReadingText']")))
    print('PASS - step 2084')
except Exception as e:
    print('FAIL - step 2084' if isinstance(e, AssertionError) else f'ERROR - step 2084: {e}')

print("STEP 2085 - Check element h2#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h2")))
    print('PASS - step 2085')
except Exception as e:
    print('FAIL - step 2085' if isinstance(e, AssertionError) else f'ERROR - step 2085: {e}')

print("STEP 2086 - Check element div#None.['aem_countries_div']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_countries_div']")))
    print('PASS - step 2086')
except Exception as e:
    print('FAIL - step 2086' if isinstance(e, AssertionError) else f'ERROR - step 2086: {e}')

print("STEP 2087 - Check element span#None.['aem_screenReadingText']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_screenReadingText']")))
    print('PASS - step 2087')
except Exception as e:
    print('FAIL - step 2087' if isinstance(e, AssertionError) else f'ERROR - step 2087: {e}')

print("STEP 2088 - Check element ul#countrylist.['aem_countrylist']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "countrylist")))
    print('PASS - step 2088')
except Exception as e:
    print('FAIL - step 2088' if isinstance(e, AssertionError) else f'ERROR - step 2088: {e}')

print("STEP 2089 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2089')
except Exception as e:
    print('FAIL - step 2089' if isinstance(e, AssertionError) else f'ERROR - step 2089: {e}')

print("STEP 2090 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2090')
except Exception as e:
    print('FAIL - step 2090' if isinstance(e, AssertionError) else f'ERROR - step 2090: {e}')

print("STEP 2091 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2091')
except Exception as e:
    print('FAIL - step 2091' if isinstance(e, AssertionError) else f'ERROR - step 2091: {e}')

print("STEP 2092 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2092')
except Exception as e:
    print('FAIL - step 2092' if isinstance(e, AssertionError) else f'ERROR - step 2092: {e}')

print("STEP 2093 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2093')
except Exception as e:
    print('FAIL - step 2093' if isinstance(e, AssertionError) else f'ERROR - step 2093: {e}')

print("STEP 2094 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2094')
except Exception as e:
    print('FAIL - step 2094' if isinstance(e, AssertionError) else f'ERROR - step 2094: {e}')

print("STEP 2095 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2095')
except Exception as e:
    print('FAIL - step 2095' if isinstance(e, AssertionError) else f'ERROR - step 2095: {e}')

print("STEP 2096 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2096')
except Exception as e:
    print('FAIL - step 2096' if isinstance(e, AssertionError) else f'ERROR - step 2096: {e}')

print("STEP 2097 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2097')
except Exception as e:
    print('FAIL - step 2097' if isinstance(e, AssertionError) else f'ERROR - step 2097: {e}')

print("STEP 2098 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2098')
except Exception as e:
    print('FAIL - step 2098' if isinstance(e, AssertionError) else f'ERROR - step 2098: {e}')

print("STEP 2099 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2099')
except Exception as e:
    print('FAIL - step 2099' if isinstance(e, AssertionError) else f'ERROR - step 2099: {e}')

print("STEP 2100 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2100')
except Exception as e:
    print('FAIL - step 2100' if isinstance(e, AssertionError) else f'ERROR - step 2100: {e}')

print("STEP 2101 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2101')
except Exception as e:
    print('FAIL - step 2101' if isinstance(e, AssertionError) else f'ERROR - step 2101: {e}')

print("STEP 2102 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2102')
except Exception as e:
    print('FAIL - step 2102' if isinstance(e, AssertionError) else f'ERROR - step 2102: {e}')

print("STEP 2103 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2103')
except Exception as e:
    print('FAIL - step 2103' if isinstance(e, AssertionError) else f'ERROR - step 2103: {e}')

print("STEP 2104 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2104')
except Exception as e:
    print('FAIL - step 2104' if isinstance(e, AssertionError) else f'ERROR - step 2104: {e}')

print("STEP 2105 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2105')
except Exception as e:
    print('FAIL - step 2105' if isinstance(e, AssertionError) else f'ERROR - step 2105: {e}')

print("STEP 2106 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2106')
except Exception as e:
    print('FAIL - step 2106' if isinstance(e, AssertionError) else f'ERROR - step 2106: {e}')

print("STEP 2107 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2107')
except Exception as e:
    print('FAIL - step 2107' if isinstance(e, AssertionError) else f'ERROR - step 2107: {e}')

print("STEP 2108 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2108')
except Exception as e:
    print('FAIL - step 2108' if isinstance(e, AssertionError) else f'ERROR - step 2108: {e}')

print("STEP 2109 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2109')
except Exception as e:
    print('FAIL - step 2109' if isinstance(e, AssertionError) else f'ERROR - step 2109: {e}')

print("STEP 2110 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2110')
except Exception as e:
    print('FAIL - step 2110' if isinstance(e, AssertionError) else f'ERROR - step 2110: {e}')

print("STEP 2111 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2111')
except Exception as e:
    print('FAIL - step 2111' if isinstance(e, AssertionError) else f'ERROR - step 2111: {e}')

print("STEP 2112 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2112')
except Exception as e:
    print('FAIL - step 2112' if isinstance(e, AssertionError) else f'ERROR - step 2112: {e}')

print("STEP 2113 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2113')
except Exception as e:
    print('FAIL - step 2113' if isinstance(e, AssertionError) else f'ERROR - step 2113: {e}')

print("STEP 2114 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2114')
except Exception as e:
    print('FAIL - step 2114' if isinstance(e, AssertionError) else f'ERROR - step 2114: {e}')

print("STEP 2115 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2115')
except Exception as e:
    print('FAIL - step 2115' if isinstance(e, AssertionError) else f'ERROR - step 2115: {e}')

print("STEP 2116 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2116')
except Exception as e:
    print('FAIL - step 2116' if isinstance(e, AssertionError) else f'ERROR - step 2116: {e}')

print("STEP 2117 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2117')
except Exception as e:
    print('FAIL - step 2117' if isinstance(e, AssertionError) else f'ERROR - step 2117: {e}')

print("STEP 2118 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2118')
except Exception as e:
    print('FAIL - step 2118' if isinstance(e, AssertionError) else f'ERROR - step 2118: {e}')

print("STEP 2119 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2119')
except Exception as e:
    print('FAIL - step 2119' if isinstance(e, AssertionError) else f'ERROR - step 2119: {e}')

print("STEP 2120 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2120')
except Exception as e:
    print('FAIL - step 2120' if isinstance(e, AssertionError) else f'ERROR - step 2120: {e}')

print("STEP 2121 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2121')
except Exception as e:
    print('FAIL - step 2121' if isinstance(e, AssertionError) else f'ERROR - step 2121: {e}')

print("STEP 2122 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2122')
except Exception as e:
    print('FAIL - step 2122' if isinstance(e, AssertionError) else f'ERROR - step 2122: {e}')

print("STEP 2123 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2123')
except Exception as e:
    print('FAIL - step 2123' if isinstance(e, AssertionError) else f'ERROR - step 2123: {e}')

print("STEP 2124 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2124')
except Exception as e:
    print('FAIL - step 2124' if isinstance(e, AssertionError) else f'ERROR - step 2124: {e}')

print("STEP 2125 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2125')
except Exception as e:
    print('FAIL - step 2125' if isinstance(e, AssertionError) else f'ERROR - step 2125: {e}')

print("STEP 2126 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2126')
except Exception as e:
    print('FAIL - step 2126' if isinstance(e, AssertionError) else f'ERROR - step 2126: {e}')

print("STEP 2127 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2127')
except Exception as e:
    print('FAIL - step 2127' if isinstance(e, AssertionError) else f'ERROR - step 2127: {e}')

print("STEP 2128 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2128')
except Exception as e:
    print('FAIL - step 2128' if isinstance(e, AssertionError) else f'ERROR - step 2128: {e}')

print("STEP 2129 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2129')
except Exception as e:
    print('FAIL - step 2129' if isinstance(e, AssertionError) else f'ERROR - step 2129: {e}')

print("STEP 2130 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2130')
except Exception as e:
    print('FAIL - step 2130' if isinstance(e, AssertionError) else f'ERROR - step 2130: {e}')

print("STEP 2131 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2131')
except Exception as e:
    print('FAIL - step 2131' if isinstance(e, AssertionError) else f'ERROR - step 2131: {e}')

print("STEP 2132 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2132')
except Exception as e:
    print('FAIL - step 2132' if isinstance(e, AssertionError) else f'ERROR - step 2132: {e}')

print("STEP 2133 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2133')
except Exception as e:
    print('FAIL - step 2133' if isinstance(e, AssertionError) else f'ERROR - step 2133: {e}')

print("STEP 2134 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2134')
except Exception as e:
    print('FAIL - step 2134' if isinstance(e, AssertionError) else f'ERROR - step 2134: {e}')

print("STEP 2135 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2135')
except Exception as e:
    print('FAIL - step 2135' if isinstance(e, AssertionError) else f'ERROR - step 2135: {e}')

print("STEP 2136 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2136')
except Exception as e:
    print('FAIL - step 2136' if isinstance(e, AssertionError) else f'ERROR - step 2136: {e}')

print("STEP 2137 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2137')
except Exception as e:
    print('FAIL - step 2137' if isinstance(e, AssertionError) else f'ERROR - step 2137: {e}')

print("STEP 2138 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2138')
except Exception as e:
    print('FAIL - step 2138' if isinstance(e, AssertionError) else f'ERROR - step 2138: {e}')

print("STEP 2139 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2139')
except Exception as e:
    print('FAIL - step 2139' if isinstance(e, AssertionError) else f'ERROR - step 2139: {e}')

print("STEP 2140 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2140')
except Exception as e:
    print('FAIL - step 2140' if isinstance(e, AssertionError) else f'ERROR - step 2140: {e}')

print("STEP 2141 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2141')
except Exception as e:
    print('FAIL - step 2141' if isinstance(e, AssertionError) else f'ERROR - step 2141: {e}')

print("STEP 2142 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2142')
except Exception as e:
    print('FAIL - step 2142' if isinstance(e, AssertionError) else f'ERROR - step 2142: {e}')

print("STEP 2143 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2143')
except Exception as e:
    print('FAIL - step 2143' if isinstance(e, AssertionError) else f'ERROR - step 2143: {e}')

print("STEP 2144 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2144')
except Exception as e:
    print('FAIL - step 2144' if isinstance(e, AssertionError) else f'ERROR - step 2144: {e}')

print("STEP 2145 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2145')
except Exception as e:
    print('FAIL - step 2145' if isinstance(e, AssertionError) else f'ERROR - step 2145: {e}')

print("STEP 2146 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2146')
except Exception as e:
    print('FAIL - step 2146' if isinstance(e, AssertionError) else f'ERROR - step 2146: {e}')

print("STEP 2147 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2147')
except Exception as e:
    print('FAIL - step 2147' if isinstance(e, AssertionError) else f'ERROR - step 2147: {e}')

print("STEP 2148 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2148')
except Exception as e:
    print('FAIL - step 2148' if isinstance(e, AssertionError) else f'ERROR - step 2148: {e}')

print("STEP 2149 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2149')
except Exception as e:
    print('FAIL - step 2149' if isinstance(e, AssertionError) else f'ERROR - step 2149: {e}')

print("STEP 2150 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2150')
except Exception as e:
    print('FAIL - step 2150' if isinstance(e, AssertionError) else f'ERROR - step 2150: {e}')

print("STEP 2151 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2151')
except Exception as e:
    print('FAIL - step 2151' if isinstance(e, AssertionError) else f'ERROR - step 2151: {e}')

print("STEP 2152 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2152')
except Exception as e:
    print('FAIL - step 2152' if isinstance(e, AssertionError) else f'ERROR - step 2152: {e}')

print("STEP 2153 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2153')
except Exception as e:
    print('FAIL - step 2153' if isinstance(e, AssertionError) else f'ERROR - step 2153: {e}')

print("STEP 2154 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2154')
except Exception as e:
    print('FAIL - step 2154' if isinstance(e, AssertionError) else f'ERROR - step 2154: {e}')

print("STEP 2155 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2155')
except Exception as e:
    print('FAIL - step 2155' if isinstance(e, AssertionError) else f'ERROR - step 2155: {e}')

print("STEP 2156 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2156')
except Exception as e:
    print('FAIL - step 2156' if isinstance(e, AssertionError) else f'ERROR - step 2156: {e}')

print("STEP 2157 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2157')
except Exception as e:
    print('FAIL - step 2157' if isinstance(e, AssertionError) else f'ERROR - step 2157: {e}')

print("STEP 2158 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2158')
except Exception as e:
    print('FAIL - step 2158' if isinstance(e, AssertionError) else f'ERROR - step 2158: {e}')

print("STEP 2159 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2159')
except Exception as e:
    print('FAIL - step 2159' if isinstance(e, AssertionError) else f'ERROR - step 2159: {e}')

print("STEP 2160 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2160')
except Exception as e:
    print('FAIL - step 2160' if isinstance(e, AssertionError) else f'ERROR - step 2160: {e}')

print("STEP 2161 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2161')
except Exception as e:
    print('FAIL - step 2161' if isinstance(e, AssertionError) else f'ERROR - step 2161: {e}')

print("STEP 2162 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2162')
except Exception as e:
    print('FAIL - step 2162' if isinstance(e, AssertionError) else f'ERROR - step 2162: {e}')

print("STEP 2163 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2163')
except Exception as e:
    print('FAIL - step 2163' if isinstance(e, AssertionError) else f'ERROR - step 2163: {e}')

print("STEP 2164 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2164')
except Exception as e:
    print('FAIL - step 2164' if isinstance(e, AssertionError) else f'ERROR - step 2164: {e}')

print("STEP 2165 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2165')
except Exception as e:
    print('FAIL - step 2165' if isinstance(e, AssertionError) else f'ERROR - step 2165: {e}')

print("STEP 2166 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2166')
except Exception as e:
    print('FAIL - step 2166' if isinstance(e, AssertionError) else f'ERROR - step 2166: {e}')

print("STEP 2167 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2167')
except Exception as e:
    print('FAIL - step 2167' if isinstance(e, AssertionError) else f'ERROR - step 2167: {e}')

print("STEP 2168 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2168')
except Exception as e:
    print('FAIL - step 2168' if isinstance(e, AssertionError) else f'ERROR - step 2168: {e}')

print("STEP 2169 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2169')
except Exception as e:
    print('FAIL - step 2169' if isinstance(e, AssertionError) else f'ERROR - step 2169: {e}')

print("STEP 2170 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2170')
except Exception as e:
    print('FAIL - step 2170' if isinstance(e, AssertionError) else f'ERROR - step 2170: {e}')

print("STEP 2171 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2171')
except Exception as e:
    print('FAIL - step 2171' if isinstance(e, AssertionError) else f'ERROR - step 2171: {e}')

print("STEP 2172 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2172')
except Exception as e:
    print('FAIL - step 2172' if isinstance(e, AssertionError) else f'ERROR - step 2172: {e}')

print("STEP 2173 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2173')
except Exception as e:
    print('FAIL - step 2173' if isinstance(e, AssertionError) else f'ERROR - step 2173: {e}')

print("STEP 2174 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2174')
except Exception as e:
    print('FAIL - step 2174' if isinstance(e, AssertionError) else f'ERROR - step 2174: {e}')

print("STEP 2175 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2175')
except Exception as e:
    print('FAIL - step 2175' if isinstance(e, AssertionError) else f'ERROR - step 2175: {e}')

print("STEP 2176 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2176')
except Exception as e:
    print('FAIL - step 2176' if isinstance(e, AssertionError) else f'ERROR - step 2176: {e}')

print("STEP 2177 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2177')
except Exception as e:
    print('FAIL - step 2177' if isinstance(e, AssertionError) else f'ERROR - step 2177: {e}')

print("STEP 2178 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2178')
except Exception as e:
    print('FAIL - step 2178' if isinstance(e, AssertionError) else f'ERROR - step 2178: {e}')

print("STEP 2179 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2179')
except Exception as e:
    print('FAIL - step 2179' if isinstance(e, AssertionError) else f'ERROR - step 2179: {e}')

print("STEP 2180 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2180')
except Exception as e:
    print('FAIL - step 2180' if isinstance(e, AssertionError) else f'ERROR - step 2180: {e}')

print("STEP 2181 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2181')
except Exception as e:
    print('FAIL - step 2181' if isinstance(e, AssertionError) else f'ERROR - step 2181: {e}')

print("STEP 2182 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2182')
except Exception as e:
    print('FAIL - step 2182' if isinstance(e, AssertionError) else f'ERROR - step 2182: {e}')

print("STEP 2183 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2183')
except Exception as e:
    print('FAIL - step 2183' if isinstance(e, AssertionError) else f'ERROR - step 2183: {e}')

print("STEP 2184 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2184')
except Exception as e:
    print('FAIL - step 2184' if isinstance(e, AssertionError) else f'ERROR - step 2184: {e}')

print("STEP 2185 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2185')
except Exception as e:
    print('FAIL - step 2185' if isinstance(e, AssertionError) else f'ERROR - step 2185: {e}')

print("STEP 2186 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2186')
except Exception as e:
    print('FAIL - step 2186' if isinstance(e, AssertionError) else f'ERROR - step 2186: {e}')

print("STEP 2187 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2187')
except Exception as e:
    print('FAIL - step 2187' if isinstance(e, AssertionError) else f'ERROR - step 2187: {e}')

print("STEP 2188 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2188')
except Exception as e:
    print('FAIL - step 2188' if isinstance(e, AssertionError) else f'ERROR - step 2188: {e}')

print("STEP 2189 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2189')
except Exception as e:
    print('FAIL - step 2189' if isinstance(e, AssertionError) else f'ERROR - step 2189: {e}')

print("STEP 2190 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2190')
except Exception as e:
    print('FAIL - step 2190' if isinstance(e, AssertionError) else f'ERROR - step 2190: {e}')

print("STEP 2191 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2191')
except Exception as e:
    print('FAIL - step 2191' if isinstance(e, AssertionError) else f'ERROR - step 2191: {e}')

print("STEP 2192 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2192')
except Exception as e:
    print('FAIL - step 2192' if isinstance(e, AssertionError) else f'ERROR - step 2192: {e}')

print("STEP 2193 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2193')
except Exception as e:
    print('FAIL - step 2193' if isinstance(e, AssertionError) else f'ERROR - step 2193: {e}')

print("STEP 2194 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2194')
except Exception as e:
    print('FAIL - step 2194' if isinstance(e, AssertionError) else f'ERROR - step 2194: {e}')

print("STEP 2195 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2195')
except Exception as e:
    print('FAIL - step 2195' if isinstance(e, AssertionError) else f'ERROR - step 2195: {e}')

print("STEP 2196 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2196')
except Exception as e:
    print('FAIL - step 2196' if isinstance(e, AssertionError) else f'ERROR - step 2196: {e}')

print("STEP 2197 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2197')
except Exception as e:
    print('FAIL - step 2197' if isinstance(e, AssertionError) else f'ERROR - step 2197: {e}')

print("STEP 2198 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2198')
except Exception as e:
    print('FAIL - step 2198' if isinstance(e, AssertionError) else f'ERROR - step 2198: {e}')

print("STEP 2199 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2199')
except Exception as e:
    print('FAIL - step 2199' if isinstance(e, AssertionError) else f'ERROR - step 2199: {e}')

print("STEP 2200 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2200')
except Exception as e:
    print('FAIL - step 2200' if isinstance(e, AssertionError) else f'ERROR - step 2200: {e}')

print("STEP 2201 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2201')
except Exception as e:
    print('FAIL - step 2201' if isinstance(e, AssertionError) else f'ERROR - step 2201: {e}')

print("STEP 2202 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2202')
except Exception as e:
    print('FAIL - step 2202' if isinstance(e, AssertionError) else f'ERROR - step 2202: {e}')

print("STEP 2203 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2203')
except Exception as e:
    print('FAIL - step 2203' if isinstance(e, AssertionError) else f'ERROR - step 2203: {e}')

print("STEP 2204 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2204')
except Exception as e:
    print('FAIL - step 2204' if isinstance(e, AssertionError) else f'ERROR - step 2204: {e}')

print("STEP 2205 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2205')
except Exception as e:
    print('FAIL - step 2205' if isinstance(e, AssertionError) else f'ERROR - step 2205: {e}')

print("STEP 2206 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2206')
except Exception as e:
    print('FAIL - step 2206' if isinstance(e, AssertionError) else f'ERROR - step 2206: {e}')

print("STEP 2207 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2207')
except Exception as e:
    print('FAIL - step 2207' if isinstance(e, AssertionError) else f'ERROR - step 2207: {e}')

print("STEP 2208 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2208')
except Exception as e:
    print('FAIL - step 2208' if isinstance(e, AssertionError) else f'ERROR - step 2208: {e}')

print("STEP 2209 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2209')
except Exception as e:
    print('FAIL - step 2209' if isinstance(e, AssertionError) else f'ERROR - step 2209: {e}')

print("STEP 2210 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2210')
except Exception as e:
    print('FAIL - step 2210' if isinstance(e, AssertionError) else f'ERROR - step 2210: {e}')

print("STEP 2211 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2211')
except Exception as e:
    print('FAIL - step 2211' if isinstance(e, AssertionError) else f'ERROR - step 2211: {e}')

print("STEP 2212 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2212')
except Exception as e:
    print('FAIL - step 2212' if isinstance(e, AssertionError) else f'ERROR - step 2212: {e}')

print("STEP 2213 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2213')
except Exception as e:
    print('FAIL - step 2213' if isinstance(e, AssertionError) else f'ERROR - step 2213: {e}')

print("STEP 2214 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2214')
except Exception as e:
    print('FAIL - step 2214' if isinstance(e, AssertionError) else f'ERROR - step 2214: {e}')

print("STEP 2215 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2215')
except Exception as e:
    print('FAIL - step 2215' if isinstance(e, AssertionError) else f'ERROR - step 2215: {e}')

print("STEP 2216 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2216')
except Exception as e:
    print('FAIL - step 2216' if isinstance(e, AssertionError) else f'ERROR - step 2216: {e}')

print("STEP 2217 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2217')
except Exception as e:
    print('FAIL - step 2217' if isinstance(e, AssertionError) else f'ERROR - step 2217: {e}')

print("STEP 2218 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2218')
except Exception as e:
    print('FAIL - step 2218' if isinstance(e, AssertionError) else f'ERROR - step 2218: {e}')

print("STEP 2219 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2219')
except Exception as e:
    print('FAIL - step 2219' if isinstance(e, AssertionError) else f'ERROR - step 2219: {e}')

print("STEP 2220 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2220')
except Exception as e:
    print('FAIL - step 2220' if isinstance(e, AssertionError) else f'ERROR - step 2220: {e}')

print("STEP 2221 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2221')
except Exception as e:
    print('FAIL - step 2221' if isinstance(e, AssertionError) else f'ERROR - step 2221: {e}')

print("STEP 2222 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2222')
except Exception as e:
    print('FAIL - step 2222' if isinstance(e, AssertionError) else f'ERROR - step 2222: {e}')

print("STEP 2223 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2223')
except Exception as e:
    print('FAIL - step 2223' if isinstance(e, AssertionError) else f'ERROR - step 2223: {e}')

print("STEP 2224 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2224')
except Exception as e:
    print('FAIL - step 2224' if isinstance(e, AssertionError) else f'ERROR - step 2224: {e}')

print("STEP 2225 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2225')
except Exception as e:
    print('FAIL - step 2225' if isinstance(e, AssertionError) else f'ERROR - step 2225: {e}')

print("STEP 2226 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2226')
except Exception as e:
    print('FAIL - step 2226' if isinstance(e, AssertionError) else f'ERROR - step 2226: {e}')

print("STEP 2227 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2227')
except Exception as e:
    print('FAIL - step 2227' if isinstance(e, AssertionError) else f'ERROR - step 2227: {e}')

print("STEP 2228 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2228')
except Exception as e:
    print('FAIL - step 2228' if isinstance(e, AssertionError) else f'ERROR - step 2228: {e}')

print("STEP 2229 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2229')
except Exception as e:
    print('FAIL - step 2229' if isinstance(e, AssertionError) else f'ERROR - step 2229: {e}')

print("STEP 2230 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2230')
except Exception as e:
    print('FAIL - step 2230' if isinstance(e, AssertionError) else f'ERROR - step 2230: {e}')

print("STEP 2231 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2231')
except Exception as e:
    print('FAIL - step 2231' if isinstance(e, AssertionError) else f'ERROR - step 2231: {e}')

print("STEP 2232 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2232')
except Exception as e:
    print('FAIL - step 2232' if isinstance(e, AssertionError) else f'ERROR - step 2232: {e}')

print("STEP 2233 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2233')
except Exception as e:
    print('FAIL - step 2233' if isinstance(e, AssertionError) else f'ERROR - step 2233: {e}')

print("STEP 2234 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2234')
except Exception as e:
    print('FAIL - step 2234' if isinstance(e, AssertionError) else f'ERROR - step 2234: {e}')

print("STEP 2235 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2235')
except Exception as e:
    print('FAIL - step 2235' if isinstance(e, AssertionError) else f'ERROR - step 2235: {e}')

print("STEP 2236 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2236')
except Exception as e:
    print('FAIL - step 2236' if isinstance(e, AssertionError) else f'ERROR - step 2236: {e}')

print("STEP 2237 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2237')
except Exception as e:
    print('FAIL - step 2237' if isinstance(e, AssertionError) else f'ERROR - step 2237: {e}')

print("STEP 2238 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2238')
except Exception as e:
    print('FAIL - step 2238' if isinstance(e, AssertionError) else f'ERROR - step 2238: {e}')

print("STEP 2239 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2239')
except Exception as e:
    print('FAIL - step 2239' if isinstance(e, AssertionError) else f'ERROR - step 2239: {e}')

print("STEP 2240 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2240')
except Exception as e:
    print('FAIL - step 2240' if isinstance(e, AssertionError) else f'ERROR - step 2240: {e}')

print("STEP 2241 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2241')
except Exception as e:
    print('FAIL - step 2241' if isinstance(e, AssertionError) else f'ERROR - step 2241: {e}')

print("STEP 2242 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2242')
except Exception as e:
    print('FAIL - step 2242' if isinstance(e, AssertionError) else f'ERROR - step 2242: {e}')

print("STEP 2243 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2243')
except Exception as e:
    print('FAIL - step 2243' if isinstance(e, AssertionError) else f'ERROR - step 2243: {e}')

print("STEP 2244 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2244')
except Exception as e:
    print('FAIL - step 2244' if isinstance(e, AssertionError) else f'ERROR - step 2244: {e}')

print("STEP 2245 - Check element span#None.['aem_screenReadingText']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_screenReadingText']")))
    print('PASS - step 2245')
except Exception as e:
    print('FAIL - step 2245' if isinstance(e, AssertionError) else f'ERROR - step 2245: {e}')

print("STEP 2246 - Check element a#None.['aem_cselectorbtn']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_cselectorbtn']")))
    print('PASS - step 2246')
except Exception as e:
    print('FAIL - step 2246' if isinstance(e, AssertionError) else f'ERROR - step 2246: {e}')

print("STEP 2247 - Check element span#None.['aem_screenReadingText']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_screenReadingText']")))
    print('PASS - step 2247')
except Exception as e:
    print('FAIL - step 2247' if isinstance(e, AssertionError) else f'ERROR - step 2247: {e}')

print("STEP 2248 - Check element div#None.['aem_wrapper_right_corner']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_wrapper_right_corner']")))
    print('PASS - step 2248')
except Exception as e:
    print('FAIL - step 2248' if isinstance(e, AssertionError) else f'ERROR - step 2248: {e}')

print("STEP 2249 - Check element div#None.['aem_left_corner']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem_left_corner']")))
    print('PASS - step 2249')
except Exception as e:
    print('FAIL - step 2249' if isinstance(e, AssertionError) else f'ERROR - step 2249: {e}')

print("STEP 2250 - Check element div#None.['footer_links_container_wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['footer_links_container_wrapper']")))
    print('PASS - step 2250')
except Exception as e:
    print('FAIL - step 2250' if isinstance(e, AssertionError) else f'ERROR - step 2250: {e}')

print("STEP 2251 - Check element div#None.['footer_links_container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['footer_links_container']")))
    print('PASS - step 2251')
except Exception as e:
    print('FAIL - step 2251' if isinstance(e, AssertionError) else f'ERROR - step 2251: {e}')

print("STEP 2252 - Check element div#None.['footer_links', 'wpr_column_5']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['footer_links', 'wpr_column_5']")))
    print('PASS - step 2252')
except Exception as e:
    print('FAIL - step 2252' if isinstance(e, AssertionError) else f'ERROR - step 2252: {e}')

print("STEP 2253 - Check element div#id_1.['footer_links_list_container', 'firstchild']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id_1")))
    print('PASS - step 2253')
except Exception as e:
    print('FAIL - step 2253' if isinstance(e, AssertionError) else f'ERROR - step 2253: {e}')

print("STEP 2254 - Check element a#None.['link_metrics', 'ul_site_link_header']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics', 'ul_site_link_header']")))
    print('PASS - step 2254')
except Exception as e:
    print('FAIL - step 2254' if isinstance(e, AssertionError) else f'ERROR - step 2254: {e}')

print("STEP 2255 - Check element span#None.['accordion-header']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['accordion-header']")))
    print('PASS - step 2255')
except Exception as e:
    print('FAIL - step 2255' if isinstance(e, AssertionError) else f'ERROR - step 2255: {e}')

print("STEP 2256 - Check element span#None.['accordian_arrow_icon']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['accordian_arrow_icon']")))
    print('PASS - step 2256')
except Exception as e:
    print('FAIL - step 2256' if isinstance(e, AssertionError) else f'ERROR - step 2256: {e}')

print("STEP 2257 - Check element ul#None.['tab_list']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['tab_list']")))
    print('PASS - step 2257')
except Exception as e:
    print('FAIL - step 2257' if isinstance(e, AssertionError) else f'ERROR - step 2257: {e}')

print("STEP 2258 - Check element li#None.['first_li']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['first_li']")))
    print('PASS - step 2258')
except Exception as e:
    print('FAIL - step 2258' if isinstance(e, AssertionError) else f'ERROR - step 2258: {e}')

print("STEP 2259 - Check element span#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "span")))
    print('PASS - step 2259')
except Exception as e:
    print('FAIL - step 2259' if isinstance(e, AssertionError) else f'ERROR - step 2259: {e}')

print("STEP 2260 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2260')
except Exception as e:
    print('FAIL - step 2260' if isinstance(e, AssertionError) else f'ERROR - step 2260: {e}')

print("STEP 2261 - Check element li#None.['wpr-desktop-hide']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-desktop-hide']")))
    print('PASS - step 2261')
except Exception as e:
    print('FAIL - step 2261' if isinstance(e, AssertionError) else f'ERROR - step 2261: {e}')

print("STEP 2262 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2262')
except Exception as e:
    print('FAIL - step 2262' if isinstance(e, AssertionError) else f'ERROR - step 2262: {e}')

print("STEP 2263 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2263')
except Exception as e:
    print('FAIL - step 2263' if isinstance(e, AssertionError) else f'ERROR - step 2263: {e}')

print("STEP 2264 - Check element a#None.['link_metrics', 'no-outline']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics', 'no-outline']")))
    print('PASS - step 2264')
except Exception as e:
    print('FAIL - step 2264' if isinstance(e, AssertionError) else f'ERROR - step 2264: {e}')

print("STEP 2265 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2265')
except Exception as e:
    print('FAIL - step 2265' if isinstance(e, AssertionError) else f'ERROR - step 2265: {e}')

print("STEP 2266 - Check element a#None.['link_metrics', 'no-outline']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics', 'no-outline']")))
    print('PASS - step 2266')
except Exception as e:
    print('FAIL - step 2266' if isinstance(e, AssertionError) else f'ERROR - step 2266: {e}')

print("STEP 2267 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2267')
except Exception as e:
    print('FAIL - step 2267' if isinstance(e, AssertionError) else f'ERROR - step 2267: {e}')

print("STEP 2268 - Check element a#None.['link_metrics', 'no-outline']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics', 'no-outline']")))
    print('PASS - step 2268')
except Exception as e:
    print('FAIL - step 2268' if isinstance(e, AssertionError) else f'ERROR - step 2268: {e}')

print("STEP 2269 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2269')
except Exception as e:
    print('FAIL - step 2269' if isinstance(e, AssertionError) else f'ERROR - step 2269: {e}')

print("STEP 2270 - Check element a#None.['link_metrics', 'no-outline']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics', 'no-outline']")))
    print('PASS - step 2270')
except Exception as e:
    print('FAIL - step 2270' if isinstance(e, AssertionError) else f'ERROR - step 2270: {e}')

print("STEP 2271 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2271')
except Exception as e:
    print('FAIL - step 2271' if isinstance(e, AssertionError) else f'ERROR - step 2271: {e}')

print("STEP 2272 - Check element a#None.['link_metrics', 'no-outline']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics', 'no-outline']")))
    print('PASS - step 2272')
except Exception as e:
    print('FAIL - step 2272' if isinstance(e, AssertionError) else f'ERROR - step 2272: {e}')

print("STEP 2273 - Check element div#id_2.['footer_links_list_container']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id_2")))
    print('PASS - step 2273')
except Exception as e:
    print('FAIL - step 2273' if isinstance(e, AssertionError) else f'ERROR - step 2273: {e}')

print("STEP 2274 - Check element a#None.['ul_site_link_header', 'link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ul_site_link_header', 'link_metrics']")))
    print('PASS - step 2274')
except Exception as e:
    print('FAIL - step 2274' if isinstance(e, AssertionError) else f'ERROR - step 2274: {e}')

print("STEP 2275 - Check element span#None.['accordion-header']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['accordion-header']")))
    print('PASS - step 2275')
except Exception as e:
    print('FAIL - step 2275' if isinstance(e, AssertionError) else f'ERROR - step 2275: {e}')

print("STEP 2276 - Check element span#None.['accordian_arrow_icon']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['accordian_arrow_icon']")))
    print('PASS - step 2276')
except Exception as e:
    print('FAIL - step 2276' if isinstance(e, AssertionError) else f'ERROR - step 2276: {e}')

print("STEP 2277 - Check element ul#None.['tab_list']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['tab_list']")))
    print('PASS - step 2277')
except Exception as e:
    print('FAIL - step 2277' if isinstance(e, AssertionError) else f'ERROR - step 2277: {e}')

print("STEP 2278 - Check element li#None.['first_li']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['first_li']")))
    print('PASS - step 2278')
except Exception as e:
    print('FAIL - step 2278' if isinstance(e, AssertionError) else f'ERROR - step 2278: {e}')

print("STEP 2279 - Check element span#None.['no-underline']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['no-underline']")))
    print('PASS - step 2279')
except Exception as e:
    print('FAIL - step 2279' if isinstance(e, AssertionError) else f'ERROR - step 2279: {e}')

print("STEP 2280 - Check element a#None.['link_metrics', 'column_no_link', 'link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics', 'column_no_link', 'link_metrics']")))
    print('PASS - step 2280')
except Exception as e:
    print('FAIL - step 2280' if isinstance(e, AssertionError) else f'ERROR - step 2280: {e}')

print("STEP 2281 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2281')
except Exception as e:
    print('FAIL - step 2281' if isinstance(e, AssertionError) else f'ERROR - step 2281: {e}')

print("STEP 2282 - Check element a#None.['link_metrics', 'no-outline', 'link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics', 'no-outline', 'link_metrics']")))
    print('PASS - step 2282')
except Exception as e:
    print('FAIL - step 2282' if isinstance(e, AssertionError) else f'ERROR - step 2282: {e}')

print("STEP 2283 - Check element div#id_3.['footer_links_list_container']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id_3")))
    print('PASS - step 2283')
except Exception as e:
    print('FAIL - step 2283' if isinstance(e, AssertionError) else f'ERROR - step 2283: {e}')

print("STEP 2284 - Check element a#None.['ul_site_link_header', 'link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ul_site_link_header', 'link_metrics']")))
    print('PASS - step 2284')
except Exception as e:
    print('FAIL - step 2284' if isinstance(e, AssertionError) else f'ERROR - step 2284: {e}')

print("STEP 2285 - Check element span#None.['accordion-header']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['accordion-header']")))
    print('PASS - step 2285')
except Exception as e:
    print('FAIL - step 2285' if isinstance(e, AssertionError) else f'ERROR - step 2285: {e}')

print("STEP 2286 - Check element span#None.['accordian_arrow_icon']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['accordian_arrow_icon']")))
    print('PASS - step 2286')
except Exception as e:
    print('FAIL - step 2286' if isinstance(e, AssertionError) else f'ERROR - step 2286: {e}')

print("STEP 2287 - Check element ul#None.['tab_list']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['tab_list']")))
    print('PASS - step 2287')
except Exception as e:
    print('FAIL - step 2287' if isinstance(e, AssertionError) else f'ERROR - step 2287: {e}')

print("STEP 2288 - Check element li#None.['first_li']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['first_li']")))
    print('PASS - step 2288')
except Exception as e:
    print('FAIL - step 2288' if isinstance(e, AssertionError) else f'ERROR - step 2288: {e}')

print("STEP 2289 - Check element span#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "span")))
    print('PASS - step 2289')
except Exception as e:
    print('FAIL - step 2289' if isinstance(e, AssertionError) else f'ERROR - step 2289: {e}')

print("STEP 2290 - Check element a#None.['link_metrics', 'no-outline', 'link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics', 'no-outline', 'link_metrics']")))
    print('PASS - step 2290')
except Exception as e:
    print('FAIL - step 2290' if isinstance(e, AssertionError) else f'ERROR - step 2290: {e}')

print("STEP 2291 - Check element li#None.['wpr-desktop-hide']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['wpr-desktop-hide']")))
    print('PASS - step 2291')
except Exception as e:
    print('FAIL - step 2291' if isinstance(e, AssertionError) else f'ERROR - step 2291: {e}')

print("STEP 2292 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2292')
except Exception as e:
    print('FAIL - step 2292' if isinstance(e, AssertionError) else f'ERROR - step 2292: {e}')

print("STEP 2293 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2293')
except Exception as e:
    print('FAIL - step 2293' if isinstance(e, AssertionError) else f'ERROR - step 2293: {e}')

print("STEP 2294 - Check element a#None.['link_metrics', 'no-outline', 'link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics', 'no-outline', 'link_metrics']")))
    print('PASS - step 2294')
except Exception as e:
    print('FAIL - step 2294' if isinstance(e, AssertionError) else f'ERROR - step 2294: {e}')

print("STEP 2295 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2295')
except Exception as e:
    print('FAIL - step 2295' if isinstance(e, AssertionError) else f'ERROR - step 2295: {e}')

print("STEP 2296 - Check element a#None.['link_metrics', 'no-outline', 'link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics', 'no-outline', 'link_metrics']")))
    print('PASS - step 2296')
except Exception as e:
    print('FAIL - step 2296' if isinstance(e, AssertionError) else f'ERROR - step 2296: {e}')

print("STEP 2297 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2297')
except Exception as e:
    print('FAIL - step 2297' if isinstance(e, AssertionError) else f'ERROR - step 2297: {e}')

print("STEP 2298 - Check element a#None.['link_metrics', 'no-outline', 'link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics', 'no-outline', 'link_metrics']")))
    print('PASS - step 2298')
except Exception as e:
    print('FAIL - step 2298' if isinstance(e, AssertionError) else f'ERROR - step 2298: {e}')

print("STEP 2299 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2299')
except Exception as e:
    print('FAIL - step 2299' if isinstance(e, AssertionError) else f'ERROR - step 2299: {e}')

print("STEP 2300 - Check element a#None.['link_metrics', 'no-outline', 'link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics', 'no-outline', 'link_metrics']")))
    print('PASS - step 2300')
except Exception as e:
    print('FAIL - step 2300' if isinstance(e, AssertionError) else f'ERROR - step 2300: {e}')

print("STEP 2301 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2301')
except Exception as e:
    print('FAIL - step 2301' if isinstance(e, AssertionError) else f'ERROR - step 2301: {e}')

print("STEP 2302 - Check element a#None.['link_metrics', 'no-outline', 'link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics', 'no-outline', 'link_metrics']")))
    print('PASS - step 2302')
except Exception as e:
    print('FAIL - step 2302' if isinstance(e, AssertionError) else f'ERROR - step 2302: {e}')

print("STEP 2303 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2303')
except Exception as e:
    print('FAIL - step 2303' if isinstance(e, AssertionError) else f'ERROR - step 2303: {e}')

print("STEP 2304 - Check element a#None.['link_metrics', 'no-outline', 'link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics', 'no-outline', 'link_metrics']")))
    print('PASS - step 2304')
except Exception as e:
    print('FAIL - step 2304' if isinstance(e, AssertionError) else f'ERROR - step 2304: {e}')

print("STEP 2305 - Check element div#id_4.['footer_links_list_container']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id_4")))
    print('PASS - step 2305')
except Exception as e:
    print('FAIL - step 2305' if isinstance(e, AssertionError) else f'ERROR - step 2305: {e}')

print("STEP 2306 - Check element a#None.['ul_site_link_header', 'link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ul_site_link_header', 'link_metrics']")))
    print('PASS - step 2306')
except Exception as e:
    print('FAIL - step 2306' if isinstance(e, AssertionError) else f'ERROR - step 2306: {e}')

print("STEP 2307 - Check element span#None.['accordion-header']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['accordion-header']")))
    print('PASS - step 2307')
except Exception as e:
    print('FAIL - step 2307' if isinstance(e, AssertionError) else f'ERROR - step 2307: {e}')

print("STEP 2308 - Check element span#None.['accordian_arrow_icon']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['accordian_arrow_icon']")))
    print('PASS - step 2308')
except Exception as e:
    print('FAIL - step 2308' if isinstance(e, AssertionError) else f'ERROR - step 2308: {e}')

print("STEP 2309 - Check element ul#None.['tab_list']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['tab_list']")))
    print('PASS - step 2309')
except Exception as e:
    print('FAIL - step 2309' if isinstance(e, AssertionError) else f'ERROR - step 2309: {e}')

print("STEP 2310 - Check element li#None.['first_li']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['first_li']")))
    print('PASS - step 2310')
except Exception as e:
    print('FAIL - step 2310' if isinstance(e, AssertionError) else f'ERROR - step 2310: {e}')

print("STEP 2311 - Check element span#None.['no-underline']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['no-underline']")))
    print('PASS - step 2311')
except Exception as e:
    print('FAIL - step 2311' if isinstance(e, AssertionError) else f'ERROR - step 2311: {e}')

print("STEP 2312 - Check element a#None.['link_metrics', 'column_no_link', 'no_link', 'link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics', 'column_no_link', 'no_link', 'link_metrics']")))
    print('PASS - step 2312')
except Exception as e:
    print('FAIL - step 2312' if isinstance(e, AssertionError) else f'ERROR - step 2312: {e}')

print("STEP 2313 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2313')
except Exception as e:
    print('FAIL - step 2313' if isinstance(e, AssertionError) else f'ERROR - step 2313: {e}')

print("STEP 2314 - Check element a#None.['link_metrics', 'no-outline', 'link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics', 'no-outline', 'link_metrics']")))
    print('PASS - step 2314')
except Exception as e:
    print('FAIL - step 2314' if isinstance(e, AssertionError) else f'ERROR - step 2314: {e}')

print("STEP 2315 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2315')
except Exception as e:
    print('FAIL - step 2315' if isinstance(e, AssertionError) else f'ERROR - step 2315: {e}')

print("STEP 2316 - Check element a#None.['link_metrics', 'no-outline', 'link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics', 'no-outline', 'link_metrics']")))
    print('PASS - step 2316')
except Exception as e:
    print('FAIL - step 2316' if isinstance(e, AssertionError) else f'ERROR - step 2316: {e}')

print("STEP 2317 - Check element div#None.['WprColumnSingle']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['WprColumnSingle']")))
    print('PASS - step 2317')
except Exception as e:
    print('FAIL - step 2317' if isinstance(e, AssertionError) else f'ERROR - step 2317: {e}')

print("STEP 2318 - Check element div#id_5.['footer_links_list_container']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "id_5")))
    print('PASS - step 2318')
except Exception as e:
    print('FAIL - step 2318' if isinstance(e, AssertionError) else f'ERROR - step 2318: {e}')

print("STEP 2319 - Check element a#None.['ul_site_link_header', 'link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ul_site_link_header', 'link_metrics']")))
    print('PASS - step 2319')
except Exception as e:
    print('FAIL - step 2319' if isinstance(e, AssertionError) else f'ERROR - step 2319: {e}')

print("STEP 2320 - Check element span#None.['accordion-header']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['accordion-header']")))
    print('PASS - step 2320')
except Exception as e:
    print('FAIL - step 2320' if isinstance(e, AssertionError) else f'ERROR - step 2320: {e}')

print("STEP 2321 - Check element span#None.['accordian_arrow_icon']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['accordian_arrow_icon']")))
    print('PASS - step 2321')
except Exception as e:
    print('FAIL - step 2321' if isinstance(e, AssertionError) else f'ERROR - step 2321: {e}')

print("STEP 2322 - Check element ul#None.['tab_list']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['tab_list']")))
    print('PASS - step 2322')
except Exception as e:
    print('FAIL - step 2322' if isinstance(e, AssertionError) else f'ERROR - step 2322: {e}')

print("STEP 2323 - Check element li#None.['first_li']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['first_li']")))
    print('PASS - step 2323')
except Exception as e:
    print('FAIL - step 2323' if isinstance(e, AssertionError) else f'ERROR - step 2323: {e}')

print("STEP 2324 - Check element span#None.['no-underline']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['no-underline']")))
    print('PASS - step 2324')
except Exception as e:
    print('FAIL - step 2324' if isinstance(e, AssertionError) else f'ERROR - step 2324: {e}')

print("STEP 2325 - Check element a#None.['link_metrics', 'column_no_link', 'link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics', 'column_no_link', 'link_metrics']")))
    print('PASS - step 2325')
except Exception as e:
    print('FAIL - step 2325' if isinstance(e, AssertionError) else f'ERROR - step 2325: {e}')

print("STEP 2326 - Check element style#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "style")))
    print('PASS - step 2326')
except Exception as e:
    print('FAIL - step 2326' if isinstance(e, AssertionError) else f'ERROR - step 2326: {e}')

print("STEP 2327 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2327')
except Exception as e:
    print('FAIL - step 2327' if isinstance(e, AssertionError) else f'ERROR - step 2327: {e}')

print("STEP 2328 - Check element ul#None.['ul_media_links']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ul_media_links']")))
    print('PASS - step 2328')
except Exception as e:
    print('FAIL - step 2328' if isinstance(e, AssertionError) else f'ERROR - step 2328: {e}')

print("STEP 2329 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2329')
except Exception as e:
    print('FAIL - step 2329' if isinstance(e, AssertionError) else f'ERROR - step 2329: {e}')

print("STEP 2330 - Check element a#None.['aem-linkedin', 'link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem-linkedin', 'link_metrics']")))
    print('PASS - step 2330')
except Exception as e:
    print('FAIL - step 2330' if isinstance(e, AssertionError) else f'ERROR - step 2330: {e}')

print("STEP 2331 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2331')
except Exception as e:
    print('FAIL - step 2331' if isinstance(e, AssertionError) else f'ERROR - step 2331: {e}')

print("STEP 2332 - Check element a#None.['aem-facebook', 'link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem-facebook', 'link_metrics']")))
    print('PASS - step 2332')
except Exception as e:
    print('FAIL - step 2332' if isinstance(e, AssertionError) else f'ERROR - step 2332: {e}')

print("STEP 2333 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2333')
except Exception as e:
    print('FAIL - step 2333' if isinstance(e, AssertionError) else f'ERROR - step 2333: {e}')

print("STEP 2334 - Check element a#None.['aem-instagram', 'link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem-instagram', 'link_metrics']")))
    print('PASS - step 2334')
except Exception as e:
    print('FAIL - step 2334' if isinstance(e, AssertionError) else f'ERROR - step 2334: {e}')

print("STEP 2335 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2335')
except Exception as e:
    print('FAIL - step 2335' if isinstance(e, AssertionError) else f'ERROR - step 2335: {e}')

print("STEP 2336 - Check element a#None.['aem-youtube', 'link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['aem-youtube', 'link_metrics']")))
    print('PASS - step 2336')
except Exception as e:
    print('FAIL - step 2336' if isinstance(e, AssertionError) else f'ERROR - step 2336: {e}')

print("STEP 2337 - Check element div#None.['footer_privacy_block']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['footer_privacy_block']")))
    print('PASS - step 2337')
except Exception as e:
    print('FAIL - step 2337' if isinstance(e, AssertionError) else f'ERROR - step 2337: {e}')

print("STEP 2338 - Check element ul#None.['footer_privacy_links']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['footer_privacy_links']")))
    print('PASS - step 2338')
except Exception as e:
    print('FAIL - step 2338' if isinstance(e, AssertionError) else f'ERROR - step 2338: {e}')

print("STEP 2339 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2339')
except Exception as e:
    print('FAIL - step 2339' if isinstance(e, AssertionError) else f'ERROR - step 2339: {e}')

print("STEP 2340 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2340')
except Exception as e:
    print('FAIL - step 2340' if isinstance(e, AssertionError) else f'ERROR - step 2340: {e}')

print("STEP 2341 - Check element span#None.['horizontal_sep']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['horizontal_sep']")))
    print('PASS - step 2341')
except Exception as e:
    print('FAIL - step 2341' if isinstance(e, AssertionError) else f'ERROR - step 2341: {e}')

print("STEP 2342 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2342')
except Exception as e:
    print('FAIL - step 2342' if isinstance(e, AssertionError) else f'ERROR - step 2342: {e}')

print("STEP 2343 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2343')
except Exception as e:
    print('FAIL - step 2343' if isinstance(e, AssertionError) else f'ERROR - step 2343: {e}')

print("STEP 2344 - Check element span#None.['horizontal_sep']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['horizontal_sep']")))
    print('PASS - step 2344')
except Exception as e:
    print('FAIL - step 2344' if isinstance(e, AssertionError) else f'ERROR - step 2344: {e}')

print("STEP 2345 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2345')
except Exception as e:
    print('FAIL - step 2345' if isinstance(e, AssertionError) else f'ERROR - step 2345: {e}')

print("STEP 2346 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2346')
except Exception as e:
    print('FAIL - step 2346' if isinstance(e, AssertionError) else f'ERROR - step 2346: {e}')

print("STEP 2347 - Check element span#None.['horizontal_sep']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['horizontal_sep']")))
    print('PASS - step 2347')
except Exception as e:
    print('FAIL - step 2347' if isinstance(e, AssertionError) else f'ERROR - step 2347: {e}')

print("STEP 2348 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2348')
except Exception as e:
    print('FAIL - step 2348' if isinstance(e, AssertionError) else f'ERROR - step 2348: {e}')

print("STEP 2349 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2349')
except Exception as e:
    print('FAIL - step 2349' if isinstance(e, AssertionError) else f'ERROR - step 2349: {e}')

print("STEP 2350 - Check element span#None.['horizontal_sep']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['horizontal_sep']")))
    print('PASS - step 2350')
except Exception as e:
    print('FAIL - step 2350' if isinstance(e, AssertionError) else f'ERROR - step 2350: {e}')

print("STEP 2351 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2351')
except Exception as e:
    print('FAIL - step 2351' if isinstance(e, AssertionError) else f'ERROR - step 2351: {e}')

print("STEP 2352 - Check element a#None.['link_metrics']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics']")))
    print('PASS - step 2352')
except Exception as e:
    print('FAIL - step 2352' if isinstance(e, AssertionError) else f'ERROR - step 2352: {e}')

print("STEP 2353 - Check element span#None.['horizontal_sep']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['horizontal_sep']")))
    print('PASS - step 2353')
except Exception as e:
    print('FAIL - step 2353' if isinstance(e, AssertionError) else f'ERROR - step 2353: {e}')

print("STEP 2354 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 2354')
except Exception as e:
    print('FAIL - step 2354' if isinstance(e, AssertionError) else f'ERROR - step 2354: {e}')

print("STEP 2355 - Check element a#None.['link_metrics', 'ot-sdk-show-settings']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['link_metrics', 'ot-sdk-show-settings']")))
    print('PASS - step 2355')
except Exception as e:
    print('FAIL - step 2355' if isinstance(e, AssertionError) else f'ERROR - step 2355: {e}')

print("STEP 2356 - Check element span#None.['horizontal_sep']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['horizontal_sep']")))
    print('PASS - step 2356')
except Exception as e:
    print('FAIL - step 2356' if isinstance(e, AssertionError) else f'ERROR - step 2356: {e}')

print("STEP 2357 - Check element div#None.['copy-right-section']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['copy-right-section']")))
    print('PASS - step 2357')
except Exception as e:
    print('FAIL - step 2357' if isinstance(e, AssertionError) else f'ERROR - step 2357: {e}')

print("STEP 2358 - Check element p#None.['copyright_mark']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['copyright_mark']")))
    print('PASS - step 2358')
except Exception as e:
    print('FAIL - step 2358' if isinstance(e, AssertionError) else f'ERROR - step 2358: {e}')

print("STEP 2359 - Check element p#None.['mobile_view']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['mobile_view']")))
    print('PASS - step 2359')
except Exception as e:
    print('FAIL - step 2359' if isinstance(e, AssertionError) else f'ERROR - step 2359: {e}')

print("STEP 2360 - Check element meta#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "meta")))
    print('PASS - step 2360')
except Exception as e:
    print('FAIL - step 2360' if isinstance(e, AssertionError) else f'ERROR - step 2360: {e}')

print("STEP 2361 - Check element script#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "script")))
    print('PASS - step 2361')
except Exception as e:
    print('FAIL - step 2361' if isinstance(e, AssertionError) else f'ERROR - step 2361: {e}')

print("STEP 2362 - Check element hp-modal#None.['js-hp-component', 'modal', 'fade', 'iframe-modal', 'js-hp-component-initialized']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['js-hp-component', 'modal', 'fade', 'iframe-modal', 'js-hp-component-initialized']")))
    print('PASS - step 2362')
except Exception as e:
    print('FAIL - step 2362' if isinstance(e, AssertionError) else f'ERROR - step 2362: {e}')

print("STEP 2363 - Check element div#None.['modal-dialog']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['modal-dialog']")))
    print('PASS - step 2363')
except Exception as e:
    print('FAIL - step 2363' if isinstance(e, AssertionError) else f'ERROR - step 2363: {e}')

print("STEP 2364 - Check element div#None.['modal-content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['modal-content']")))
    print('PASS - step 2364')
except Exception as e:
    print('FAIL - step 2364' if isinstance(e, AssertionError) else f'ERROR - step 2364: {e}')

print("STEP 2365 - Check element button#None.['c-icon', 'close']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-icon', 'close']")))
    print('PASS - step 2365')
except Exception as e:
    print('FAIL - step 2365' if isinstance(e, AssertionError) else f'ERROR - step 2365: {e}')

print("STEP 2366 - Check element span#None.['c-icon-regular-state']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-icon-regular-state']")))
    print('PASS - step 2366')
except Exception as e:
    print('FAIL - step 2366' if isinstance(e, AssertionError) else f'ERROR - step 2366: {e}')

print("STEP 2367 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 2367')
except Exception as e:
    print('FAIL - step 2367' if isinstance(e, AssertionError) else f'ERROR - step 2367: {e}')

print("STEP 2368 - Check element use#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "use")))
    print('PASS - step 2368')
except Exception as e:
    print('FAIL - step 2368' if isinstance(e, AssertionError) else f'ERROR - step 2368: {e}')

print("STEP 2369 - Check element span#None.['c-icon-hover-state']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['c-icon-hover-state']")))
    print('PASS - step 2369')
except Exception as e:
    print('FAIL - step 2369' if isinstance(e, AssertionError) else f'ERROR - step 2369: {e}')

print("STEP 2370 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 2370')
except Exception as e:
    print('FAIL - step 2370' if isinstance(e, AssertionError) else f'ERROR - step 2370: {e}')

print("STEP 2371 - Check element use#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "use")))
    print('PASS - step 2371')
except Exception as e:
    print('FAIL - step 2371' if isinstance(e, AssertionError) else f'ERROR - step 2371: {e}')

print("STEP 2372 - Check element div#modal-body.['modal-body']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "modal-body")))
    print('PASS - step 2372')
except Exception as e:
    print('FAIL - step 2372' if isinstance(e, AssertionError) else f'ERROR - step 2372: {e}')

print("STEP 2373 - Check element div#None.['loader', 'loader--blue']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['loader', 'loader--blue']")))
    print('PASS - step 2373')
except Exception as e:
    print('FAIL - step 2373' if isinstance(e, AssertionError) else f'ERROR - step 2373: {e}')

print("STEP 2374 - Check element iframe#iframe-container.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "iframe-container")))
    print('PASS - step 2374')
except Exception as e:
    print('FAIL - step 2374' if isinstance(e, AssertionError) else f'ERROR - step 2374: {e}')

print("STEP 2375 - Check element p#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "p")))
    print('PASS - step 2375')
except Exception as e:
    print('FAIL - step 2375' if isinstance(e, AssertionError) else f'ERROR - step 2375: {e}')

print("STEP 2376 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 2376')
except Exception as e:
    print('FAIL - step 2376' if isinstance(e, AssertionError) else f'ERROR - step 2376: {e}')

print("STEP 2377 - Check element defs#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "defs")))
    print('PASS - step 2377')
except Exception as e:
    print('FAIL - step 2377' if isinstance(e, AssertionError) else f'ERROR - step 2377: {e}')

print("STEP 2378 - Check element g#chevron-bg-1-left.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "chevron-bg-1-left")))
    print('PASS - step 2378')
except Exception as e:
    print('FAIL - step 2378' if isinstance(e, AssertionError) else f'ERROR - step 2378: {e}')

print("STEP 2379 - Check element rect#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "rect")))
    print('PASS - step 2379')
except Exception as e:
    print('FAIL - step 2379' if isinstance(e, AssertionError) else f'ERROR - step 2379: {e}')

print("STEP 2380 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2380')
except Exception as e:
    print('FAIL - step 2380' if isinstance(e, AssertionError) else f'ERROR - step 2380: {e}')

print("STEP 2381 - Check element g#chevron-bg-1-left-hover.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "chevron-bg-1-left-hover")))
    print('PASS - step 2381')
except Exception as e:
    print('FAIL - step 2381' if isinstance(e, AssertionError) else f'ERROR - step 2381: {e}')

print("STEP 2382 - Check element rect#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "rect")))
    print('PASS - step 2382')
except Exception as e:
    print('FAIL - step 2382' if isinstance(e, AssertionError) else f'ERROR - step 2382: {e}')

print("STEP 2383 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2383')
except Exception as e:
    print('FAIL - step 2383' if isinstance(e, AssertionError) else f'ERROR - step 2383: {e}')

print("STEP 2384 - Check element g#chevron-bg-2-left.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "chevron-bg-2-left")))
    print('PASS - step 2384')
except Exception as e:
    print('FAIL - step 2384' if isinstance(e, AssertionError) else f'ERROR - step 2384: {e}')

print("STEP 2385 - Check element rect#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "rect")))
    print('PASS - step 2385')
except Exception as e:
    print('FAIL - step 2385' if isinstance(e, AssertionError) else f'ERROR - step 2385: {e}')

print("STEP 2386 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2386')
except Exception as e:
    print('FAIL - step 2386' if isinstance(e, AssertionError) else f'ERROR - step 2386: {e}')

print("STEP 2387 - Check element g#chevron-bg-2-left-hover.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "chevron-bg-2-left-hover")))
    print('PASS - step 2387')
except Exception as e:
    print('FAIL - step 2387' if isinstance(e, AssertionError) else f'ERROR - step 2387: {e}')

print("STEP 2388 - Check element rect#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "rect")))
    print('PASS - step 2388')
except Exception as e:
    print('FAIL - step 2388' if isinstance(e, AssertionError) else f'ERROR - step 2388: {e}')

print("STEP 2389 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2389')
except Exception as e:
    print('FAIL - step 2389' if isinstance(e, AssertionError) else f'ERROR - step 2389: {e}')

print("STEP 2390 - Check element g#chevron-bg-3-left.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "chevron-bg-3-left")))
    print('PASS - step 2390')
except Exception as e:
    print('FAIL - step 2390' if isinstance(e, AssertionError) else f'ERROR - step 2390: {e}')

print("STEP 2391 - Check element rect#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "rect")))
    print('PASS - step 2391')
except Exception as e:
    print('FAIL - step 2391' if isinstance(e, AssertionError) else f'ERROR - step 2391: {e}')

print("STEP 2392 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2392')
except Exception as e:
    print('FAIL - step 2392' if isinstance(e, AssertionError) else f'ERROR - step 2392: {e}')

print("STEP 2393 - Check element g#chevron-bg-3-left-hover.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "chevron-bg-3-left-hover")))
    print('PASS - step 2393')
except Exception as e:
    print('FAIL - step 2393' if isinstance(e, AssertionError) else f'ERROR - step 2393: {e}')

print("STEP 2394 - Check element rect#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "rect")))
    print('PASS - step 2394')
except Exception as e:
    print('FAIL - step 2394' if isinstance(e, AssertionError) else f'ERROR - step 2394: {e}')

print("STEP 2395 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2395')
except Exception as e:
    print('FAIL - step 2395' if isinstance(e, AssertionError) else f'ERROR - step 2395: {e}')

print("STEP 2396 - Check element g#chevron-bg-4-left.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "chevron-bg-4-left")))
    print('PASS - step 2396')
except Exception as e:
    print('FAIL - step 2396' if isinstance(e, AssertionError) else f'ERROR - step 2396: {e}')

print("STEP 2397 - Check element circle#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "circle")))
    print('PASS - step 2397')
except Exception as e:
    print('FAIL - step 2397' if isinstance(e, AssertionError) else f'ERROR - step 2397: {e}')

print("STEP 2398 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2398')
except Exception as e:
    print('FAIL - step 2398' if isinstance(e, AssertionError) else f'ERROR - step 2398: {e}')

print("STEP 2399 - Check element g#chevron-bg-4-left-hover.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "chevron-bg-4-left-hover")))
    print('PASS - step 2399')
except Exception as e:
    print('FAIL - step 2399' if isinstance(e, AssertionError) else f'ERROR - step 2399: {e}')

print("STEP 2400 - Check element circle#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "circle")))
    print('PASS - step 2400')
except Exception as e:
    print('FAIL - step 2400' if isinstance(e, AssertionError) else f'ERROR - step 2400: {e}')

print("STEP 2401 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2401')
except Exception as e:
    print('FAIL - step 2401' if isinstance(e, AssertionError) else f'ERROR - step 2401: {e}')

print("STEP 2402 - Check element g#chevron-1.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "chevron-1")))
    print('PASS - step 2402')
except Exception as e:
    print('FAIL - step 2402' if isinstance(e, AssertionError) else f'ERROR - step 2402: {e}')

print("STEP 2403 - Check element g#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "g")))
    print('PASS - step 2403')
except Exception as e:
    print('FAIL - step 2403' if isinstance(e, AssertionError) else f'ERROR - step 2403: {e}')

print("STEP 2404 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2404')
except Exception as e:
    print('FAIL - step 2404' if isinstance(e, AssertionError) else f'ERROR - step 2404: {e}')

print("STEP 2405 - Check element g#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "g")))
    print('PASS - step 2405')
except Exception as e:
    print('FAIL - step 2405' if isinstance(e, AssertionError) else f'ERROR - step 2405: {e}')

print("STEP 2406 - Check element rect#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "rect")))
    print('PASS - step 2406')
except Exception as e:
    print('FAIL - step 2406' if isinstance(e, AssertionError) else f'ERROR - step 2406: {e}')

print("STEP 2407 - Check element g#chevron-1-hover.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "chevron-1-hover")))
    print('PASS - step 2407')
except Exception as e:
    print('FAIL - step 2407' if isinstance(e, AssertionError) else f'ERROR - step 2407: {e}')

print("STEP 2408 - Check element g#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "g")))
    print('PASS - step 2408')
except Exception as e:
    print('FAIL - step 2408' if isinstance(e, AssertionError) else f'ERROR - step 2408: {e}')

print("STEP 2409 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2409')
except Exception as e:
    print('FAIL - step 2409' if isinstance(e, AssertionError) else f'ERROR - step 2409: {e}')

print("STEP 2410 - Check element g#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "g")))
    print('PASS - step 2410')
except Exception as e:
    print('FAIL - step 2410' if isinstance(e, AssertionError) else f'ERROR - step 2410: {e}')

print("STEP 2411 - Check element rect#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "rect")))
    print('PASS - step 2411')
except Exception as e:
    print('FAIL - step 2411' if isinstance(e, AssertionError) else f'ERROR - step 2411: {e}')

print("STEP 2412 - Check element g#chevron-2.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "chevron-2")))
    print('PASS - step 2412')
except Exception as e:
    print('FAIL - step 2412' if isinstance(e, AssertionError) else f'ERROR - step 2412: {e}')

print("STEP 2413 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2413')
except Exception as e:
    print('FAIL - step 2413' if isinstance(e, AssertionError) else f'ERROR - step 2413: {e}')

print("STEP 2414 - Check element g#chevron-2-hover.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "chevron-2-hover")))
    print('PASS - step 2414')
except Exception as e:
    print('FAIL - step 2414' if isinstance(e, AssertionError) else f'ERROR - step 2414: {e}')

print("STEP 2415 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2415')
except Exception as e:
    print('FAIL - step 2415' if isinstance(e, AssertionError) else f'ERROR - step 2415: {e}')

print("STEP 2416 - Check element g#chevron-3.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "chevron-3")))
    print('PASS - step 2416')
except Exception as e:
    print('FAIL - step 2416' if isinstance(e, AssertionError) else f'ERROR - step 2416: {e}')

print("STEP 2417 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2417')
except Exception as e:
    print('FAIL - step 2417' if isinstance(e, AssertionError) else f'ERROR - step 2417: {e}')

print("STEP 2418 - Check element g#chevron-3-hover.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "chevron-3-hover")))
    print('PASS - step 2418')
except Exception as e:
    print('FAIL - step 2418' if isinstance(e, AssertionError) else f'ERROR - step 2418: {e}')

print("STEP 2419 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2419')
except Exception as e:
    print('FAIL - step 2419' if isinstance(e, AssertionError) else f'ERROR - step 2419: {e}')

print("STEP 2420 - Check element g#chevron-3-down.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "chevron-3-down")))
    print('PASS - step 2420')
except Exception as e:
    print('FAIL - step 2420' if isinstance(e, AssertionError) else f'ERROR - step 2420: {e}')

print("STEP 2421 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2421')
except Exception as e:
    print('FAIL - step 2421' if isinstance(e, AssertionError) else f'ERROR - step 2421: {e}')

print("STEP 2422 - Check element g#img-arrow-dark-down.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "img-arrow-dark-down")))
    print('PASS - step 2422')
except Exception as e:
    print('FAIL - step 2422' if isinstance(e, AssertionError) else f'ERROR - step 2422: {e}')

print("STEP 2423 - Check element rect#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "rect")))
    print('PASS - step 2423')
except Exception as e:
    print('FAIL - step 2423' if isinstance(e, AssertionError) else f'ERROR - step 2423: {e}')

print("STEP 2424 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2424')
except Exception as e:
    print('FAIL - step 2424' if isinstance(e, AssertionError) else f'ERROR - step 2424: {e}')

print("STEP 2425 - Check element g#img-arrow-dark-down-hover.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "img-arrow-dark-down-hover")))
    print('PASS - step 2425')
except Exception as e:
    print('FAIL - step 2425' if isinstance(e, AssertionError) else f'ERROR - step 2425: {e}')

print("STEP 2426 - Check element rect#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "rect")))
    print('PASS - step 2426')
except Exception as e:
    print('FAIL - step 2426' if isinstance(e, AssertionError) else f'ERROR - step 2426: {e}')

print("STEP 2427 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2427')
except Exception as e:
    print('FAIL - step 2427' if isinstance(e, AssertionError) else f'ERROR - step 2427: {e}')

print("STEP 2428 - Check element g#img-arrow-3-down.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "img-arrow-3-down")))
    print('PASS - step 2428')
except Exception as e:
    print('FAIL - step 2428' if isinstance(e, AssertionError) else f'ERROR - step 2428: {e}')

print("STEP 2429 - Check element rect#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "rect")))
    print('PASS - step 2429')
except Exception as e:
    print('FAIL - step 2429' if isinstance(e, AssertionError) else f'ERROR - step 2429: {e}')

print("STEP 2430 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2430')
except Exception as e:
    print('FAIL - step 2430' if isinstance(e, AssertionError) else f'ERROR - step 2430: {e}')

print("STEP 2431 - Check element g#img-arrow-3-down-hover.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "img-arrow-3-down-hover")))
    print('PASS - step 2431')
except Exception as e:
    print('FAIL - step 2431' if isinstance(e, AssertionError) else f'ERROR - step 2431: {e}')

print("STEP 2432 - Check element rect#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "rect")))
    print('PASS - step 2432')
except Exception as e:
    print('FAIL - step 2432' if isinstance(e, AssertionError) else f'ERROR - step 2432: {e}')

print("STEP 2433 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2433')
except Exception as e:
    print('FAIL - step 2433' if isinstance(e, AssertionError) else f'ERROR - step 2433: {e}')

print("STEP 2434 - Check element g#img-arrow-light-down.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "img-arrow-light-down")))
    print('PASS - step 2434')
except Exception as e:
    print('FAIL - step 2434' if isinstance(e, AssertionError) else f'ERROR - step 2434: {e}')

print("STEP 2435 - Check element rect#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "rect")))
    print('PASS - step 2435')
except Exception as e:
    print('FAIL - step 2435' if isinstance(e, AssertionError) else f'ERROR - step 2435: {e}')

print("STEP 2436 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2436')
except Exception as e:
    print('FAIL - step 2436' if isinstance(e, AssertionError) else f'ERROR - step 2436: {e}')

print("STEP 2437 - Check element g#img-arrow-light-down-hover.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "img-arrow-light-down-hover")))
    print('PASS - step 2437')
except Exception as e:
    print('FAIL - step 2437' if isinstance(e, AssertionError) else f'ERROR - step 2437: {e}')

print("STEP 2438 - Check element rect#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "rect")))
    print('PASS - step 2438')
except Exception as e:
    print('FAIL - step 2438' if isinstance(e, AssertionError) else f'ERROR - step 2438: {e}')

print("STEP 2439 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2439')
except Exception as e:
    print('FAIL - step 2439' if isinstance(e, AssertionError) else f'ERROR - step 2439: {e}')

print("STEP 2440 - Check element g#arrow-right.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "arrow-right")))
    print('PASS - step 2440')
except Exception as e:
    print('FAIL - step 2440' if isinstance(e, AssertionError) else f'ERROR - step 2440: {e}')

print("STEP 2441 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2441')
except Exception as e:
    print('FAIL - step 2441' if isinstance(e, AssertionError) else f'ERROR - step 2441: {e}')

print("STEP 2442 - Check element g#indicator-dark.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "indicator-dark")))
    print('PASS - step 2442')
except Exception as e:
    print('FAIL - step 2442' if isinstance(e, AssertionError) else f'ERROR - step 2442: {e}')

print("STEP 2443 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2443')
except Exception as e:
    print('FAIL - step 2443' if isinstance(e, AssertionError) else f'ERROR - step 2443: {e}')

print("STEP 2444 - Check element g#indicator-light.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "indicator-light")))
    print('PASS - step 2444')
except Exception as e:
    print('FAIL - step 2444' if isinstance(e, AssertionError) else f'ERROR - step 2444: {e}')

print("STEP 2445 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2445')
except Exception as e:
    print('FAIL - step 2445' if isinstance(e, AssertionError) else f'ERROR - step 2445: {e}')

print("STEP 2446 - Check element g#img-close-icon-dark.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "img-close-icon-dark")))
    print('PASS - step 2446')
except Exception as e:
    print('FAIL - step 2446' if isinstance(e, AssertionError) else f'ERROR - step 2446: {e}')

print("STEP 2447 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2447')
except Exception as e:
    print('FAIL - step 2447' if isinstance(e, AssertionError) else f'ERROR - step 2447: {e}')

print("STEP 2448 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2448')
except Exception as e:
    print('FAIL - step 2448' if isinstance(e, AssertionError) else f'ERROR - step 2448: {e}')

print("STEP 2449 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2449')
except Exception as e:
    print('FAIL - step 2449' if isinstance(e, AssertionError) else f'ERROR - step 2449: {e}')

print("STEP 2450 - Check element g#img-close-icon-dark-hover.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "img-close-icon-dark-hover")))
    print('PASS - step 2450')
except Exception as e:
    print('FAIL - step 2450' if isinstance(e, AssertionError) else f'ERROR - step 2450: {e}')

print("STEP 2451 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2451')
except Exception as e:
    print('FAIL - step 2451' if isinstance(e, AssertionError) else f'ERROR - step 2451: {e}')

print("STEP 2452 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2452')
except Exception as e:
    print('FAIL - step 2452' if isinstance(e, AssertionError) else f'ERROR - step 2452: {e}')

print("STEP 2453 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2453')
except Exception as e:
    print('FAIL - step 2453' if isinstance(e, AssertionError) else f'ERROR - step 2453: {e}')

print("STEP 2454 - Check element g#img-close-icon-light.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "img-close-icon-light")))
    print('PASS - step 2454')
except Exception as e:
    print('FAIL - step 2454' if isinstance(e, AssertionError) else f'ERROR - step 2454: {e}')

print("STEP 2455 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2455')
except Exception as e:
    print('FAIL - step 2455' if isinstance(e, AssertionError) else f'ERROR - step 2455: {e}')

print("STEP 2456 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2456')
except Exception as e:
    print('FAIL - step 2456' if isinstance(e, AssertionError) else f'ERROR - step 2456: {e}')

print("STEP 2457 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2457')
except Exception as e:
    print('FAIL - step 2457' if isinstance(e, AssertionError) else f'ERROR - step 2457: {e}')

print("STEP 2458 - Check element g#img-close-icon-light-hover.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "img-close-icon-light-hover")))
    print('PASS - step 2458')
except Exception as e:
    print('FAIL - step 2458' if isinstance(e, AssertionError) else f'ERROR - step 2458: {e}')

print("STEP 2459 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2459')
except Exception as e:
    print('FAIL - step 2459' if isinstance(e, AssertionError) else f'ERROR - step 2459: {e}')

print("STEP 2460 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2460')
except Exception as e:
    print('FAIL - step 2460' if isinstance(e, AssertionError) else f'ERROR - step 2460: {e}')

print("STEP 2461 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2461')
except Exception as e:
    print('FAIL - step 2461' if isinstance(e, AssertionError) else f'ERROR - step 2461: {e}')

print("STEP 2462 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2462')
except Exception as e:
    print('FAIL - step 2462' if isinstance(e, AssertionError) else f'ERROR - step 2462: {e}')

print("STEP 2463 - Check element g#plus-icon.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "plus-icon")))
    print('PASS - step 2463')
except Exception as e:
    print('FAIL - step 2463' if isinstance(e, AssertionError) else f'ERROR - step 2463: {e}')

print("STEP 2464 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2464')
except Exception as e:
    print('FAIL - step 2464' if isinstance(e, AssertionError) else f'ERROR - step 2464: {e}')

print("STEP 2465 - Check element g#minus-icon.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "minus-icon")))
    print('PASS - step 2465')
except Exception as e:
    print('FAIL - step 2465' if isinstance(e, AssertionError) else f'ERROR - step 2465: {e}')

print("STEP 2466 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2466')
except Exception as e:
    print('FAIL - step 2466' if isinstance(e, AssertionError) else f'ERROR - step 2466: {e}')

print("STEP 2467 - Check element g#img-play-btn-large-light.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "img-play-btn-large-light")))
    print('PASS - step 2467')
except Exception as e:
    print('FAIL - step 2467' if isinstance(e, AssertionError) else f'ERROR - step 2467: {e}')

print("STEP 2468 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2468')
except Exception as e:
    print('FAIL - step 2468' if isinstance(e, AssertionError) else f'ERROR - step 2468: {e}')

print("STEP 2469 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2469')
except Exception as e:
    print('FAIL - step 2469' if isinstance(e, AssertionError) else f'ERROR - step 2469: {e}')

print("STEP 2470 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2470')
except Exception as e:
    print('FAIL - step 2470' if isinstance(e, AssertionError) else f'ERROR - step 2470: {e}')

print("STEP 2471 - Check element g#img-play-btn-large-light-hover.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "img-play-btn-large-light-hover")))
    print('PASS - step 2471')
except Exception as e:
    print('FAIL - step 2471' if isinstance(e, AssertionError) else f'ERROR - step 2471: {e}')

print("STEP 2472 - Check element rect#fill.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "fill")))
    print('PASS - step 2472')
except Exception as e:
    print('FAIL - step 2472' if isinstance(e, AssertionError) else f'ERROR - step 2472: {e}')

print("STEP 2473 - Check element path#border.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "border")))
    print('PASS - step 2473')
except Exception as e:
    print('FAIL - step 2473' if isinstance(e, AssertionError) else f'ERROR - step 2473: {e}')

print("STEP 2474 - Check element path#play-large.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "play-large")))
    print('PASS - step 2474')
except Exception as e:
    print('FAIL - step 2474' if isinstance(e, AssertionError) else f'ERROR - step 2474: {e}')

print("STEP 2475 - Check element g#img-collapsible-downarrow.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "img-collapsible-downarrow")))
    print('PASS - step 2475')
except Exception as e:
    print('FAIL - step 2475' if isinstance(e, AssertionError) else f'ERROR - step 2475: {e}')

print("STEP 2476 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2476')
except Exception as e:
    print('FAIL - step 2476' if isinstance(e, AssertionError) else f'ERROR - step 2476: {e}')

print("STEP 2477 - Check element g#img-warning-icon.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "img-warning-icon")))
    print('PASS - step 2477')
except Exception as e:
    print('FAIL - step 2477' if isinstance(e, AssertionError) else f'ERROR - step 2477: {e}')

print("STEP 2478 - Check element defs#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "defs")))
    print('PASS - step 2478')
except Exception as e:
    print('FAIL - step 2478' if isinstance(e, AssertionError) else f'ERROR - step 2478: {e}')

print("STEP 2479 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2479')
except Exception as e:
    print('FAIL - step 2479' if isinstance(e, AssertionError) else f'ERROR - step 2479: {e}')

print("STEP 2480 - Check element g#slider-arrow-dark.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "slider-arrow-dark")))
    print('PASS - step 2480')
except Exception as e:
    print('FAIL - step 2480' if isinstance(e, AssertionError) else f'ERROR - step 2480: {e}')

print("STEP 2481 - Check element path#Path_1.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "Path_1")))
    print('PASS - step 2481')
except Exception as e:
    print('FAIL - step 2481' if isinstance(e, AssertionError) else f'ERROR - step 2481: {e}')

print("STEP 2482 - Check element path#Path_2.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "Path_2")))
    print('PASS - step 2482')
except Exception as e:
    print('FAIL - step 2482' if isinstance(e, AssertionError) else f'ERROR - step 2482: {e}')

print("STEP 2483 - Check element g#slider-arrow-white.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "slider-arrow-white")))
    print('PASS - step 2483')
except Exception as e:
    print('FAIL - step 2483' if isinstance(e, AssertionError) else f'ERROR - step 2483: {e}')

print("STEP 2484 - Check element g#Group.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "Group")))
    print('PASS - step 2484')
except Exception as e:
    print('FAIL - step 2484' if isinstance(e, AssertionError) else f'ERROR - step 2484: {e}')

print("STEP 2485 - Check element path#Fill-1.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "Fill-1")))
    print('PASS - step 2485')
except Exception as e:
    print('FAIL - step 2485' if isinstance(e, AssertionError) else f'ERROR - step 2485: {e}')

print("STEP 2486 - Check element path#Fill-3.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "Fill-3")))
    print('PASS - step 2486')
except Exception as e:
    print('FAIL - step 2486' if isinstance(e, AssertionError) else f'ERROR - step 2486: {e}')

print("STEP 2487 - Check element g#arrow-right-blue.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "arrow-right-blue")))
    print('PASS - step 2487')
except Exception as e:
    print('FAIL - step 2487' if isinstance(e, AssertionError) else f'ERROR - step 2487: {e}')

print("STEP 2488 - Check element path#Chevron-1-2.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "Chevron-1-2")))
    print('PASS - step 2488')
except Exception as e:
    print('FAIL - step 2488' if isinstance(e, AssertionError) else f'ERROR - step 2488: {e}')

print("STEP 2489 - Check element g#arrow-right-white.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "arrow-right-white")))
    print('PASS - step 2489')
except Exception as e:
    print('FAIL - step 2489' if isinstance(e, AssertionError) else f'ERROR - step 2489: {e}')

print("STEP 2490 - Check element path#Chevron-1-2.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "Chevron-1-2")))
    print('PASS - step 2490')
except Exception as e:
    print('FAIL - step 2490' if isinstance(e, AssertionError) else f'ERROR - step 2490: {e}')

print("STEP 2491 - Check element g#square-chevron-bg-1-left.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "square-chevron-bg-1-left")))
    print('PASS - step 2491')
except Exception as e:
    print('FAIL - step 2491' if isinstance(e, AssertionError) else f'ERROR - step 2491: {e}')

print("STEP 2492 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2492')
except Exception as e:
    print('FAIL - step 2492' if isinstance(e, AssertionError) else f'ERROR - step 2492: {e}')

print("STEP 2493 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2493')
except Exception as e:
    print('FAIL - step 2493' if isinstance(e, AssertionError) else f'ERROR - step 2493: {e}')

print("STEP 2494 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2494')
except Exception as e:
    print('FAIL - step 2494' if isinstance(e, AssertionError) else f'ERROR - step 2494: {e}')

print("STEP 2495 - Check element g#square-chevron-bg-1-left-hover.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "square-chevron-bg-1-left-hover")))
    print('PASS - step 2495')
except Exception as e:
    print('FAIL - step 2495' if isinstance(e, AssertionError) else f'ERROR - step 2495: {e}')

print("STEP 2496 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2496')
except Exception as e:
    print('FAIL - step 2496' if isinstance(e, AssertionError) else f'ERROR - step 2496: {e}')

print("STEP 2497 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2497')
except Exception as e:
    print('FAIL - step 2497' if isinstance(e, AssertionError) else f'ERROR - step 2497: {e}')

print("STEP 2498 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2498')
except Exception as e:
    print('FAIL - step 2498' if isinstance(e, AssertionError) else f'ERROR - step 2498: {e}')

print("STEP 2499 - Check element g#square-chevron-bg-2-left.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "square-chevron-bg-2-left")))
    print('PASS - step 2499')
except Exception as e:
    print('FAIL - step 2499' if isinstance(e, AssertionError) else f'ERROR - step 2499: {e}')

print("STEP 2500 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2500')
except Exception as e:
    print('FAIL - step 2500' if isinstance(e, AssertionError) else f'ERROR - step 2500: {e}')

print("STEP 2501 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2501')
except Exception as e:
    print('FAIL - step 2501' if isinstance(e, AssertionError) else f'ERROR - step 2501: {e}')

print("STEP 2502 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2502')
except Exception as e:
    print('FAIL - step 2502' if isinstance(e, AssertionError) else f'ERROR - step 2502: {e}')

print("STEP 2503 - Check element g#square-chevron-bg-2-left-hover.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "square-chevron-bg-2-left-hover")))
    print('PASS - step 2503')
except Exception as e:
    print('FAIL - step 2503' if isinstance(e, AssertionError) else f'ERROR - step 2503: {e}')

print("STEP 2504 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2504')
except Exception as e:
    print('FAIL - step 2504' if isinstance(e, AssertionError) else f'ERROR - step 2504: {e}')

print("STEP 2505 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2505')
except Exception as e:
    print('FAIL - step 2505' if isinstance(e, AssertionError) else f'ERROR - step 2505: {e}')

print("STEP 2506 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2506')
except Exception as e:
    print('FAIL - step 2506' if isinstance(e, AssertionError) else f'ERROR - step 2506: {e}')

print("STEP 2507 - Check element g#square-chevron-bg-3-left.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "square-chevron-bg-3-left")))
    print('PASS - step 2507')
except Exception as e:
    print('FAIL - step 2507' if isinstance(e, AssertionError) else f'ERROR - step 2507: {e}')

print("STEP 2508 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2508')
except Exception as e:
    print('FAIL - step 2508' if isinstance(e, AssertionError) else f'ERROR - step 2508: {e}')

print("STEP 2509 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2509')
except Exception as e:
    print('FAIL - step 2509' if isinstance(e, AssertionError) else f'ERROR - step 2509: {e}')

print("STEP 2510 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2510')
except Exception as e:
    print('FAIL - step 2510' if isinstance(e, AssertionError) else f'ERROR - step 2510: {e}')

print("STEP 2511 - Check element g#square-chevron-bg-3-left-hover.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "square-chevron-bg-3-left-hover")))
    print('PASS - step 2511')
except Exception as e:
    print('FAIL - step 2511' if isinstance(e, AssertionError) else f'ERROR - step 2511: {e}')

print("STEP 2512 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2512')
except Exception as e:
    print('FAIL - step 2512' if isinstance(e, AssertionError) else f'ERROR - step 2512: {e}')

print("STEP 2513 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2513')
except Exception as e:
    print('FAIL - step 2513' if isinstance(e, AssertionError) else f'ERROR - step 2513: {e}')

print("STEP 2514 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2514')
except Exception as e:
    print('FAIL - step 2514' if isinstance(e, AssertionError) else f'ERROR - step 2514: {e}')

print("STEP 2515 - Check element g#square-horizontal-arrow-1-left.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "square-horizontal-arrow-1-left")))
    print('PASS - step 2515')
except Exception as e:
    print('FAIL - step 2515' if isinstance(e, AssertionError) else f'ERROR - step 2515: {e}')

print("STEP 2516 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2516')
except Exception as e:
    print('FAIL - step 2516' if isinstance(e, AssertionError) else f'ERROR - step 2516: {e}')

print("STEP 2517 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2517')
except Exception as e:
    print('FAIL - step 2517' if isinstance(e, AssertionError) else f'ERROR - step 2517: {e}')

print("STEP 2518 - Check element g#square-horizontal-arrow-1-left-hover.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "square-horizontal-arrow-1-left-hover")))
    print('PASS - step 2518')
except Exception as e:
    print('FAIL - step 2518' if isinstance(e, AssertionError) else f'ERROR - step 2518: {e}')

print("STEP 2519 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2519')
except Exception as e:
    print('FAIL - step 2519' if isinstance(e, AssertionError) else f'ERROR - step 2519: {e}')

print("STEP 2520 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2520')
except Exception as e:
    print('FAIL - step 2520' if isinstance(e, AssertionError) else f'ERROR - step 2520: {e}')

print("STEP 2521 - Check element g#square-horizontal-arrow-2-left.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "square-horizontal-arrow-2-left")))
    print('PASS - step 2521')
except Exception as e:
    print('FAIL - step 2521' if isinstance(e, AssertionError) else f'ERROR - step 2521: {e}')

print("STEP 2522 - Check element g#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "g")))
    print('PASS - step 2522')
except Exception as e:
    print('FAIL - step 2522' if isinstance(e, AssertionError) else f'ERROR - step 2522: {e}')

print("STEP 2523 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2523')
except Exception as e:
    print('FAIL - step 2523' if isinstance(e, AssertionError) else f'ERROR - step 2523: {e}')

print("STEP 2524 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2524')
except Exception as e:
    print('FAIL - step 2524' if isinstance(e, AssertionError) else f'ERROR - step 2524: {e}')

print("STEP 2525 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2525')
except Exception as e:
    print('FAIL - step 2525' if isinstance(e, AssertionError) else f'ERROR - step 2525: {e}')

print("STEP 2526 - Check element g#square-horizontal-arrow-2-left-hover.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "square-horizontal-arrow-2-left-hover")))
    print('PASS - step 2526')
except Exception as e:
    print('FAIL - step 2526' if isinstance(e, AssertionError) else f'ERROR - step 2526: {e}')

print("STEP 2527 - Check element g#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "g")))
    print('PASS - step 2527')
except Exception as e:
    print('FAIL - step 2527' if isinstance(e, AssertionError) else f'ERROR - step 2527: {e}')

print("STEP 2528 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2528')
except Exception as e:
    print('FAIL - step 2528' if isinstance(e, AssertionError) else f'ERROR - step 2528: {e}')

print("STEP 2529 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2529')
except Exception as e:
    print('FAIL - step 2529' if isinstance(e, AssertionError) else f'ERROR - step 2529: {e}')

print("STEP 2530 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2530')
except Exception as e:
    print('FAIL - step 2530' if isinstance(e, AssertionError) else f'ERROR - step 2530: {e}')

print("STEP 2531 - Check element g#play-button-small.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "play-button-small")))
    print('PASS - step 2531')
except Exception as e:
    print('FAIL - step 2531' if isinstance(e, AssertionError) else f'ERROR - step 2531: {e}')

print("STEP 2532 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2532')
except Exception as e:
    print('FAIL - step 2532' if isinstance(e, AssertionError) else f'ERROR - step 2532: {e}')

print("STEP 2533 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2533')
except Exception as e:
    print('FAIL - step 2533' if isinstance(e, AssertionError) else f'ERROR - step 2533: {e}')

print("STEP 2534 - Check element g#play-button-small-hover.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "play-button-small-hover")))
    print('PASS - step 2534')
except Exception as e:
    print('FAIL - step 2534' if isinstance(e, AssertionError) else f'ERROR - step 2534: {e}')

print("STEP 2535 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2535')
except Exception as e:
    print('FAIL - step 2535' if isinstance(e, AssertionError) else f'ERROR - step 2535: {e}')

print("STEP 2536 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2536')
except Exception as e:
    print('FAIL - step 2536' if isinstance(e, AssertionError) else f'ERROR - step 2536: {e}')

print("STEP 2537 - Check element g#pause-button-small.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "pause-button-small")))
    print('PASS - step 2537')
except Exception as e:
    print('FAIL - step 2537' if isinstance(e, AssertionError) else f'ERROR - step 2537: {e}')

print("STEP 2538 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2538')
except Exception as e:
    print('FAIL - step 2538' if isinstance(e, AssertionError) else f'ERROR - step 2538: {e}')

print("STEP 2539 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2539')
except Exception as e:
    print('FAIL - step 2539' if isinstance(e, AssertionError) else f'ERROR - step 2539: {e}')

print("STEP 2540 - Check element g#pause-button-small-hover.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "pause-button-small-hover")))
    print('PASS - step 2540')
except Exception as e:
    print('FAIL - step 2540' if isinstance(e, AssertionError) else f'ERROR - step 2540: {e}')

print("STEP 2541 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2541')
except Exception as e:
    print('FAIL - step 2541' if isinstance(e, AssertionError) else f'ERROR - step 2541: {e}')

print("STEP 2542 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2542')
except Exception as e:
    print('FAIL - step 2542' if isinstance(e, AssertionError) else f'ERROR - step 2542: {e}')

print("STEP 2543 - Check element g#stop-button-small.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "stop-button-small")))
    print('PASS - step 2543')
except Exception as e:
    print('FAIL - step 2543' if isinstance(e, AssertionError) else f'ERROR - step 2543: {e}')

print("STEP 2544 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2544')
except Exception as e:
    print('FAIL - step 2544' if isinstance(e, AssertionError) else f'ERROR - step 2544: {e}')

print("STEP 2545 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2545')
except Exception as e:
    print('FAIL - step 2545' if isinstance(e, AssertionError) else f'ERROR - step 2545: {e}')

print("STEP 2546 - Check element g#stop-button-small-hover.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "stop-button-small-hover")))
    print('PASS - step 2546')
except Exception as e:
    print('FAIL - step 2546' if isinstance(e, AssertionError) else f'ERROR - step 2546: {e}')

print("STEP 2547 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2547')
except Exception as e:
    print('FAIL - step 2547' if isinstance(e, AssertionError) else f'ERROR - step 2547: {e}')

print("STEP 2548 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2548')
except Exception as e:
    print('FAIL - step 2548' if isinstance(e, AssertionError) else f'ERROR - step 2548: {e}')

print("STEP 2549 - Check element g#play-button-padding.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "play-button-padding")))
    print('PASS - step 2549')
except Exception as e:
    print('FAIL - step 2549' if isinstance(e, AssertionError) else f'ERROR - step 2549: {e}')

print("STEP 2550 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2550')
except Exception as e:
    print('FAIL - step 2550' if isinstance(e, AssertionError) else f'ERROR - step 2550: {e}')

print("STEP 2551 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2551')
except Exception as e:
    print('FAIL - step 2551' if isinstance(e, AssertionError) else f'ERROR - step 2551: {e}')

print("STEP 2552 - Check element g#play-button-padding-hover.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "play-button-padding-hover")))
    print('PASS - step 2552')
except Exception as e:
    print('FAIL - step 2552' if isinstance(e, AssertionError) else f'ERROR - step 2552: {e}')

print("STEP 2553 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2553')
except Exception as e:
    print('FAIL - step 2553' if isinstance(e, AssertionError) else f'ERROR - step 2553: {e}')

print("STEP 2554 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2554')
except Exception as e:
    print('FAIL - step 2554' if isinstance(e, AssertionError) else f'ERROR - step 2554: {e}')

print("STEP 2555 - Check element g#pause-button-padding.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "pause-button-padding")))
    print('PASS - step 2555')
except Exception as e:
    print('FAIL - step 2555' if isinstance(e, AssertionError) else f'ERROR - step 2555: {e}')

print("STEP 2556 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2556')
except Exception as e:
    print('FAIL - step 2556' if isinstance(e, AssertionError) else f'ERROR - step 2556: {e}')

print("STEP 2557 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2557')
except Exception as e:
    print('FAIL - step 2557' if isinstance(e, AssertionError) else f'ERROR - step 2557: {e}')

print("STEP 2558 - Check element g#pause-button-padding-hover.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "pause-button-padding-hover")))
    print('PASS - step 2558')
except Exception as e:
    print('FAIL - step 2558' if isinstance(e, AssertionError) else f'ERROR - step 2558: {e}')

print("STEP 2559 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2559')
except Exception as e:
    print('FAIL - step 2559' if isinstance(e, AssertionError) else f'ERROR - step 2559: {e}')

print("STEP 2560 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2560')
except Exception as e:
    print('FAIL - step 2560' if isinstance(e, AssertionError) else f'ERROR - step 2560: {e}')

print("STEP 2561 - Check element g#close-button-padding.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "close-button-padding")))
    print('PASS - step 2561')
except Exception as e:
    print('FAIL - step 2561' if isinstance(e, AssertionError) else f'ERROR - step 2561: {e}')

print("STEP 2562 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2562')
except Exception as e:
    print('FAIL - step 2562' if isinstance(e, AssertionError) else f'ERROR - step 2562: {e}')

print("STEP 2563 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2563')
except Exception as e:
    print('FAIL - step 2563' if isinstance(e, AssertionError) else f'ERROR - step 2563: {e}')

print("STEP 2564 - Check element g#close-button-padding-hover.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "close-button-padding-hover")))
    print('PASS - step 2564')
except Exception as e:
    print('FAIL - step 2564' if isinstance(e, AssertionError) else f'ERROR - step 2564: {e}')

print("STEP 2565 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2565')
except Exception as e:
    print('FAIL - step 2565' if isinstance(e, AssertionError) else f'ERROR - step 2565: {e}')

print("STEP 2566 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2566')
except Exception as e:
    print('FAIL - step 2566' if isinstance(e, AssertionError) else f'ERROR - step 2566: {e}')

print("STEP 2567 - Check element g#play-btn-mobile.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "play-btn-mobile")))
    print('PASS - step 2567')
except Exception as e:
    print('FAIL - step 2567' if isinstance(e, AssertionError) else f'ERROR - step 2567: {e}')

print("STEP 2568 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2568')
except Exception as e:
    print('FAIL - step 2568' if isinstance(e, AssertionError) else f'ERROR - step 2568: {e}')

print("STEP 2569 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2569')
except Exception as e:
    print('FAIL - step 2569' if isinstance(e, AssertionError) else f'ERROR - step 2569: {e}')

print("STEP 2570 - Check element g#play-btn-mobile-hover.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "play-btn-mobile-hover")))
    print('PASS - step 2570')
except Exception as e:
    print('FAIL - step 2570' if isinstance(e, AssertionError) else f'ERROR - step 2570: {e}')

print("STEP 2571 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2571')
except Exception as e:
    print('FAIL - step 2571' if isinstance(e, AssertionError) else f'ERROR - step 2571: {e}')

print("STEP 2572 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2572')
except Exception as e:
    print('FAIL - step 2572' if isinstance(e, AssertionError) else f'ERROR - step 2572: {e}')

print("STEP 2573 - Check element g#pause-btn-mobile.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "pause-btn-mobile")))
    print('PASS - step 2573')
except Exception as e:
    print('FAIL - step 2573' if isinstance(e, AssertionError) else f'ERROR - step 2573: {e}')

print("STEP 2574 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2574')
except Exception as e:
    print('FAIL - step 2574' if isinstance(e, AssertionError) else f'ERROR - step 2574: {e}')

print("STEP 2575 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2575')
except Exception as e:
    print('FAIL - step 2575' if isinstance(e, AssertionError) else f'ERROR - step 2575: {e}')

print("STEP 2576 - Check element g#pause-btn-mobile-hover.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "pause-btn-mobile-hover")))
    print('PASS - step 2576')
except Exception as e:
    print('FAIL - step 2576' if isinstance(e, AssertionError) else f'ERROR - step 2576: {e}')

print("STEP 2577 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2577')
except Exception as e:
    print('FAIL - step 2577' if isinstance(e, AssertionError) else f'ERROR - step 2577: {e}')

print("STEP 2578 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2578')
except Exception as e:
    print('FAIL - step 2578' if isinstance(e, AssertionError) else f'ERROR - step 2578: {e}')

print("STEP 2579 - Check element g#close-btn-mobile.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "close-btn-mobile")))
    print('PASS - step 2579')
except Exception as e:
    print('FAIL - step 2579' if isinstance(e, AssertionError) else f'ERROR - step 2579: {e}')

print("STEP 2580 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2580')
except Exception as e:
    print('FAIL - step 2580' if isinstance(e, AssertionError) else f'ERROR - step 2580: {e}')

print("STEP 2581 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2581')
except Exception as e:
    print('FAIL - step 2581' if isinstance(e, AssertionError) else f'ERROR - step 2581: {e}')

print("STEP 2582 - Check element g#close-btn-mobile-hover.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "close-btn-mobile-hover")))
    print('PASS - step 2582')
except Exception as e:
    print('FAIL - step 2582' if isinstance(e, AssertionError) else f'ERROR - step 2582: {e}')

print("STEP 2583 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2583')
except Exception as e:
    print('FAIL - step 2583' if isinstance(e, AssertionError) else f'ERROR - step 2583: {e}')

print("STEP 2584 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2584')
except Exception as e:
    print('FAIL - step 2584' if isinstance(e, AssertionError) else f'ERROR - step 2584: {e}')

print("STEP 2585 - Check element g#z-logo.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "z-logo")))
    print('PASS - step 2585')
except Exception as e:
    print('FAIL - step 2585' if isinstance(e, AssertionError) else f'ERROR - step 2585: {e}')

print("STEP 2586 - Check element g#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "g")))
    print('PASS - step 2586')
except Exception as e:
    print('FAIL - step 2586' if isinstance(e, AssertionError) else f'ERROR - step 2586: {e}')

print("STEP 2587 - Check element g#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "g")))
    print('PASS - step 2587')
except Exception as e:
    print('FAIL - step 2587' if isinstance(e, AssertionError) else f'ERROR - step 2587: {e}')

print("STEP 2588 - Check element g#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "g")))
    print('PASS - step 2588')
except Exception as e:
    print('FAIL - step 2588' if isinstance(e, AssertionError) else f'ERROR - step 2588: {e}')

print("STEP 2589 - Check element g#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "g")))
    print('PASS - step 2589')
except Exception as e:
    print('FAIL - step 2589' if isinstance(e, AssertionError) else f'ERROR - step 2589: {e}')

print("STEP 2590 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2590')
except Exception as e:
    print('FAIL - step 2590' if isinstance(e, AssertionError) else f'ERROR - step 2590: {e}')

print("STEP 2591 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2591')
except Exception as e:
    print('FAIL - step 2591' if isinstance(e, AssertionError) else f'ERROR - step 2591: {e}')

print("STEP 2592 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2592')
except Exception as e:
    print('FAIL - step 2592' if isinstance(e, AssertionError) else f'ERROR - step 2592: {e}')

print("STEP 2593 - Check element g#z-play.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "z-play")))
    print('PASS - step 2593')
except Exception as e:
    print('FAIL - step 2593' if isinstance(e, AssertionError) else f'ERROR - step 2593: {e}')

print("STEP 2594 - Check element g#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "g")))
    print('PASS - step 2594')
except Exception as e:
    print('FAIL - step 2594' if isinstance(e, AssertionError) else f'ERROR - step 2594: {e}')

print("STEP 2595 - Check element g#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "g")))
    print('PASS - step 2595')
except Exception as e:
    print('FAIL - step 2595' if isinstance(e, AssertionError) else f'ERROR - step 2595: {e}')

print("STEP 2596 - Check element g#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "g")))
    print('PASS - step 2596')
except Exception as e:
    print('FAIL - step 2596' if isinstance(e, AssertionError) else f'ERROR - step 2596: {e}')

print("STEP 2597 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2597')
except Exception as e:
    print('FAIL - step 2597' if isinstance(e, AssertionError) else f'ERROR - step 2597: {e}')

print("STEP 2598 - Check element g#z-plus.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "z-plus")))
    print('PASS - step 2598')
except Exception as e:
    print('FAIL - step 2598' if isinstance(e, AssertionError) else f'ERROR - step 2598: {e}')

print("STEP 2599 - Check element g#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "g")))
    print('PASS - step 2599')
except Exception as e:
    print('FAIL - step 2599' if isinstance(e, AssertionError) else f'ERROR - step 2599: {e}')

print("STEP 2600 - Check element g#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "g")))
    print('PASS - step 2600')
except Exception as e:
    print('FAIL - step 2600' if isinstance(e, AssertionError) else f'ERROR - step 2600: {e}')

print("STEP 2601 - Check element g#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "g")))
    print('PASS - step 2601')
except Exception as e:
    print('FAIL - step 2601' if isinstance(e, AssertionError) else f'ERROR - step 2601: {e}')

print("STEP 2602 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2602')
except Exception as e:
    print('FAIL - step 2602' if isinstance(e, AssertionError) else f'ERROR - step 2602: {e}')

print("STEP 2603 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2603')
except Exception as e:
    print('FAIL - step 2603' if isinstance(e, AssertionError) else f'ERROR - step 2603: {e}')

print("STEP 2604 - Check element g#z-minus.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "z-minus")))
    print('PASS - step 2604')
except Exception as e:
    print('FAIL - step 2604' if isinstance(e, AssertionError) else f'ERROR - step 2604: {e}')

print("STEP 2605 - Check element g#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "g")))
    print('PASS - step 2605')
except Exception as e:
    print('FAIL - step 2605' if isinstance(e, AssertionError) else f'ERROR - step 2605: {e}')

print("STEP 2606 - Check element g#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "g")))
    print('PASS - step 2606')
except Exception as e:
    print('FAIL - step 2606' if isinstance(e, AssertionError) else f'ERROR - step 2606: {e}')

print("STEP 2607 - Check element g#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "g")))
    print('PASS - step 2607')
except Exception as e:
    print('FAIL - step 2607' if isinstance(e, AssertionError) else f'ERROR - step 2607: {e}')

print("STEP 2608 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2608')
except Exception as e:
    print('FAIL - step 2608' if isinstance(e, AssertionError) else f'ERROR - step 2608: {e}')

print("STEP 2609 - Check element g#z-chevron.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "z-chevron")))
    print('PASS - step 2609')
except Exception as e:
    print('FAIL - step 2609' if isinstance(e, AssertionError) else f'ERROR - step 2609: {e}')

print("STEP 2610 - Check element g#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "g")))
    print('PASS - step 2610')
except Exception as e:
    print('FAIL - step 2610' if isinstance(e, AssertionError) else f'ERROR - step 2610: {e}')

print("STEP 2611 - Check element g#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "g")))
    print('PASS - step 2611')
except Exception as e:
    print('FAIL - step 2611' if isinstance(e, AssertionError) else f'ERROR - step 2611: {e}')

print("STEP 2612 - Check element g#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "g")))
    print('PASS - step 2612')
except Exception as e:
    print('FAIL - step 2612' if isinstance(e, AssertionError) else f'ERROR - step 2612: {e}')

print("STEP 2613 - Check element g#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "g")))
    print('PASS - step 2613')
except Exception as e:
    print('FAIL - step 2613' if isinstance(e, AssertionError) else f'ERROR - step 2613: {e}')

print("STEP 2614 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2614')
except Exception as e:
    print('FAIL - step 2614' if isinstance(e, AssertionError) else f'ERROR - step 2614: {e}')

print("STEP 2615 - Check element g#z-arrow-16.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "z-arrow-16")))
    print('PASS - step 2615')
except Exception as e:
    print('FAIL - step 2615' if isinstance(e, AssertionError) else f'ERROR - step 2615: {e}')

print("STEP 2616 - Check element g#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "g")))
    print('PASS - step 2616')
except Exception as e:
    print('FAIL - step 2616' if isinstance(e, AssertionError) else f'ERROR - step 2616: {e}')

print("STEP 2617 - Check element g#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "g")))
    print('PASS - step 2617')
except Exception as e:
    print('FAIL - step 2617' if isinstance(e, AssertionError) else f'ERROR - step 2617: {e}')

print("STEP 2618 - Check element g#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "g")))
    print('PASS - step 2618')
except Exception as e:
    print('FAIL - step 2618' if isinstance(e, AssertionError) else f'ERROR - step 2618: {e}')

print("STEP 2619 - Check element g#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "g")))
    print('PASS - step 2619')
except Exception as e:
    print('FAIL - step 2619' if isinstance(e, AssertionError) else f'ERROR - step 2619: {e}')

print("STEP 2620 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2620')
except Exception as e:
    print('FAIL - step 2620' if isinstance(e, AssertionError) else f'ERROR - step 2620: {e}')

print("STEP 2621 - Check element g#z-arrow.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "z-arrow")))
    print('PASS - step 2621')
except Exception as e:
    print('FAIL - step 2621' if isinstance(e, AssertionError) else f'ERROR - step 2621: {e}')

print("STEP 2622 - Check element defs#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "defs")))
    print('PASS - step 2622')
except Exception as e:
    print('FAIL - step 2622' if isinstance(e, AssertionError) else f'ERROR - step 2622: {e}')

print("STEP 2623 - Check element filter#l0iz88j6za.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "l0iz88j6za")))
    print('PASS - step 2623')
except Exception as e:
    print('FAIL - step 2623' if isinstance(e, AssertionError) else f'ERROR - step 2623: {e}')

print("STEP 2624 - Check element fecolormatrix#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "fecolormatrix")))
    print('PASS - step 2624')
except Exception as e:
    print('FAIL - step 2624' if isinstance(e, AssertionError) else f'ERROR - step 2624: {e}')

print("STEP 2625 - Check element g#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "g")))
    print('PASS - step 2625')
except Exception as e:
    print('FAIL - step 2625' if isinstance(e, AssertionError) else f'ERROR - step 2625: {e}')

print("STEP 2626 - Check element g#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "g")))
    print('PASS - step 2626')
except Exception as e:
    print('FAIL - step 2626' if isinstance(e, AssertionError) else f'ERROR - step 2626: {e}')

print("STEP 2627 - Check element g#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "g")))
    print('PASS - step 2627')
except Exception as e:
    print('FAIL - step 2627' if isinstance(e, AssertionError) else f'ERROR - step 2627: {e}')

print("STEP 2628 - Check element g#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "g")))
    print('PASS - step 2628')
except Exception as e:
    print('FAIL - step 2628' if isinstance(e, AssertionError) else f'ERROR - step 2628: {e}')

print("STEP 2629 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2629')
except Exception as e:
    print('FAIL - step 2629' if isinstance(e, AssertionError) else f'ERROR - step 2629: {e}')

print("STEP 2630 - Check element div#hp-translations-map.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "hp-translations-map")))
    print('PASS - step 2630')
except Exception as e:
    print('FAIL - step 2630' if isinstance(e, AssertionError) else f'ERROR - step 2630: {e}')

print("STEP 2631 - Check element span#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "span")))
    print('PASS - step 2631')
except Exception as e:
    print('FAIL - step 2631' if isinstance(e, AssertionError) else f'ERROR - step 2631: {e}')

print("STEP 2632 - Check element span#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "span")))
    print('PASS - step 2632')
except Exception as e:
    print('FAIL - step 2632' if isinstance(e, AssertionError) else f'ERROR - step 2632: {e}')

print("STEP 2633 - Check element span#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "span")))
    print('PASS - step 2633')
except Exception as e:
    print('FAIL - step 2633' if isinstance(e, AssertionError) else f'ERROR - step 2633: {e}')

print("STEP 2634 - Check element span#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "span")))
    print('PASS - step 2634')
except Exception as e:
    print('FAIL - step 2634' if isinstance(e, AssertionError) else f'ERROR - step 2634: {e}')

print("STEP 2635 - Check element span#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "span")))
    print('PASS - step 2635')
except Exception as e:
    print('FAIL - step 2635' if isinstance(e, AssertionError) else f'ERROR - step 2635: {e}')

print("STEP 2636 - Check element span#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "span")))
    print('PASS - step 2636')
except Exception as e:
    print('FAIL - step 2636' if isinstance(e, AssertionError) else f'ERROR - step 2636: {e}')

print("STEP 2637 - Check element script#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "script")))
    print('PASS - step 2637')
except Exception as e:
    print('FAIL - step 2637' if isinstance(e, AssertionError) else f'ERROR - step 2637: {e}')

print("STEP 2638 - Check element script#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "script")))
    print('PASS - step 2638')
except Exception as e:
    print('FAIL - step 2638' if isinstance(e, AssertionError) else f'ERROR - step 2638: {e}')

print("STEP 2639 - Check element noscript#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "noscript")))
    print('PASS - step 2639')
except Exception as e:
    print('FAIL - step 2639' if isinstance(e, AssertionError) else f'ERROR - step 2639: {e}')

print("STEP 2640 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 2640')
except Exception as e:
    print('FAIL - step 2640' if isinstance(e, AssertionError) else f'ERROR - step 2640: {e}')

print("STEP 2641 - Check element script#.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "script")))
    print('PASS - step 2641')
except Exception as e:
    print('FAIL - step 2641' if isinstance(e, AssertionError) else f'ERROR - step 2641: {e}')

print("STEP 2642 - Check element script#.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "script")))
    print('PASS - step 2642')
except Exception as e:
    print('FAIL - step 2642' if isinstance(e, AssertionError) else f'ERROR - step 2642: {e}')

print("STEP 2643 - Check element script#.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "script")))
    print('PASS - step 2643')
except Exception as e:
    print('FAIL - step 2643' if isinstance(e, AssertionError) else f'ERROR - step 2643: {e}')

print("STEP 2644 - Check element script#.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "script")))
    print('PASS - step 2644')
except Exception as e:
    print('FAIL - step 2644' if isinstance(e, AssertionError) else f'ERROR - step 2644: {e}')

print("STEP 2645 - Check element script#.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "script")))
    print('PASS - step 2645')
except Exception as e:
    print('FAIL - step 2645' if isinstance(e, AssertionError) else f'ERROR - step 2645: {e}')

print("STEP 2646 - Check element script#.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "script")))
    print('PASS - step 2646')
except Exception as e:
    print('FAIL - step 2646' if isinstance(e, AssertionError) else f'ERROR - step 2646: {e}')

print("STEP 2647 - Check element script#.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "script")))
    print('PASS - step 2647')
except Exception as e:
    print('FAIL - step 2647' if isinstance(e, AssertionError) else f'ERROR - step 2647: {e}')

print("STEP 2648 - Check element script#.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "script")))
    print('PASS - step 2648')
except Exception as e:
    print('FAIL - step 2648' if isinstance(e, AssertionError) else f'ERROR - step 2648: {e}')

print("STEP 2649 - Check element script#.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "script")))
    print('PASS - step 2649')
except Exception as e:
    print('FAIL - step 2649' if isinstance(e, AssertionError) else f'ERROR - step 2649: {e}')

print("STEP 2650 - Check element script#.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "script")))
    print('PASS - step 2650')
except Exception as e:
    print('FAIL - step 2650' if isinstance(e, AssertionError) else f'ERROR - step 2650: {e}')

print("STEP 2651 - Check element script#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "script")))
    print('PASS - step 2651')
except Exception as e:
    print('FAIL - step 2651' if isinstance(e, AssertionError) else f'ERROR - step 2651: {e}')

print("STEP 2652 - Check element div#onetrust-consent-sdk.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "onetrust-consent-sdk")))
    print('PASS - step 2652')
except Exception as e:
    print('FAIL - step 2652' if isinstance(e, AssertionError) else f'ERROR - step 2652: {e}')

print("STEP 2653 - Check element div#None.['onetrust-pc-dark-filter', 'ot-hide', 'ot-fade-in']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['onetrust-pc-dark-filter', 'ot-hide', 'ot-fade-in']")))
    print('PASS - step 2653')
except Exception as e:
    print('FAIL - step 2653' if isinstance(e, AssertionError) else f'ERROR - step 2653: {e}')

print("STEP 2654 - Check element div#onetrust-banner-sdk.['otCenterRounded', 'default', 'ot-wo-title', 'vertical-align-content']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "onetrust-banner-sdk")))
    print('PASS - step 2654')
except Exception as e:
    print('FAIL - step 2654' if isinstance(e, AssertionError) else f'ERROR - step 2654: {e}')

print("STEP 2655 - Check element div#None.['ot-sdk-container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-sdk-container']")))
    print('PASS - step 2655')
except Exception as e:
    print('FAIL - step 2655' if isinstance(e, AssertionError) else f'ERROR - step 2655: {e}')

print("STEP 2656 - Check element div#None.['ot-sdk-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-sdk-row']")))
    print('PASS - step 2656')
except Exception as e:
    print('FAIL - step 2656' if isinstance(e, AssertionError) else f'ERROR - step 2656: {e}')

print("STEP 2657 - Check element div#onetrust-group-container.['ot-sdk-twelve', 'ot-sdk-columns']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "onetrust-group-container")))
    print('PASS - step 2657')
except Exception as e:
    print('FAIL - step 2657' if isinstance(e, AssertionError) else f'ERROR - step 2657: {e}')

print("STEP 2658 - Check element div#onetrust-policy.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "onetrust-policy")))
    print('PASS - step 2658')
except Exception as e:
    print('FAIL - step 2658' if isinstance(e, AssertionError) else f'ERROR - step 2658: {e}')

print("STEP 2659 - Check element div#None.['banner-header']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['banner-header']")))
    print('PASS - step 2659')
except Exception as e:
    print('FAIL - step 2659' if isinstance(e, AssertionError) else f'ERROR - step 2659: {e}')

print("STEP 2660 - Check element div#None.['banner_logo']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['banner_logo']")))
    print('PASS - step 2660')
except Exception as e:
    print('FAIL - step 2660' if isinstance(e, AssertionError) else f'ERROR - step 2660: {e}')

print("STEP 2661 - Check element div#onetrust-policy-text.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "onetrust-policy-text")))
    print('PASS - step 2661')
except Exception as e:
    print('FAIL - step 2661' if isinstance(e, AssertionError) else f'ERROR - step 2661: {e}')

print("STEP 2662 - Check element div#onetrust-button-group-parent.['ot-sdk-twelve', 'ot-sdk-columns']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "onetrust-button-group-parent")))
    print('PASS - step 2662')
except Exception as e:
    print('FAIL - step 2662' if isinstance(e, AssertionError) else f'ERROR - step 2662: {e}')

print("STEP 2663 - Check element div#onetrust-button-group.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "onetrust-button-group")))
    print('PASS - step 2663')
except Exception as e:
    print('FAIL - step 2663' if isinstance(e, AssertionError) else f'ERROR - step 2663: {e}')

print("STEP 2664 - Check element button#onetrust-pc-btn-handler.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "onetrust-pc-btn-handler")))
    print('PASS - step 2664')
except Exception as e:
    print('FAIL - step 2664' if isinstance(e, AssertionError) else f'ERROR - step 2664: {e}')

print("STEP 2665 - Check element div#None.['banner-actions-container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['banner-actions-container']")))
    print('PASS - step 2665')
except Exception as e:
    print('FAIL - step 2665' if isinstance(e, AssertionError) else f'ERROR - step 2665: {e}')

print("STEP 2666 - Check element button#onetrust-accept-btn-handler.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "onetrust-accept-btn-handler")))
    print('PASS - step 2666')
except Exception as e:
    print('FAIL - step 2666' if isinstance(e, AssertionError) else f'ERROR - step 2666: {e}')

print("STEP 2667 - Check element div#onetrust-close-btn-container.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "onetrust-close-btn-container")))
    print('PASS - step 2667')
except Exception as e:
    print('FAIL - step 2667' if isinstance(e, AssertionError) else f'ERROR - step 2667: {e}')

print("STEP 2668 - Check element button#None.['onetrust-close-btn-handler', 'onetrust-close-btn-ui', 'banner-close-button', 'ot-close-icon']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['onetrust-close-btn-handler', 'onetrust-close-btn-ui', 'banner-close-button', 'ot-close-icon']")))
    print('PASS - step 2668')
except Exception as e:
    print('FAIL - step 2668' if isinstance(e, AssertionError) else f'ERROR - step 2668: {e}')

print("STEP 2669 - Check element div#onetrust-pc-sdk.['otPcTab', 'ot-hide', 'ot-fade-in']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "onetrust-pc-sdk")))
    print('PASS - step 2669')
except Exception as e:
    print('FAIL - step 2669' if isinstance(e, AssertionError) else f'ERROR - step 2669: {e}')

print("STEP 2670 - Check element div#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "div")))
    print('PASS - step 2670')
except Exception as e:
    print('FAIL - step 2670' if isinstance(e, AssertionError) else f'ERROR - step 2670: {e}')

print("STEP 2671 - Check element div#None.['ot-pc-header']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-pc-header']")))
    print('PASS - step 2671')
except Exception as e:
    print('FAIL - step 2671' if isinstance(e, AssertionError) else f'ERROR - step 2671: {e}')

print("STEP 2672 - Check element div#None.['ot-pc-logo']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-pc-logo']")))
    print('PASS - step 2672')
except Exception as e:
    print('FAIL - step 2672' if isinstance(e, AssertionError) else f'ERROR - step 2672: {e}')

print("STEP 2673 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 2673')
except Exception as e:
    print('FAIL - step 2673' if isinstance(e, AssertionError) else f'ERROR - step 2673: {e}')

print("STEP 2674 - Check element div#None.['ot-title-cntr']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-title-cntr']")))
    print('PASS - step 2674')
except Exception as e:
    print('FAIL - step 2674' if isinstance(e, AssertionError) else f'ERROR - step 2674: {e}')

print("STEP 2675 - Check element h2#ot-pc-title.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "ot-pc-title")))
    print('PASS - step 2675')
except Exception as e:
    print('FAIL - step 2675' if isinstance(e, AssertionError) else f'ERROR - step 2675: {e}')

print("STEP 2676 - Check element div#None.['ot-close-cntr']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-close-cntr']")))
    print('PASS - step 2676')
except Exception as e:
    print('FAIL - step 2676' if isinstance(e, AssertionError) else f'ERROR - step 2676: {e}')

print("STEP 2677 - Check element button#close-pc-btn-handler.['ot-close-icon']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "close-pc-btn-handler")))
    print('PASS - step 2677')
except Exception as e:
    print('FAIL - step 2677' if isinstance(e, AssertionError) else f'ERROR - step 2677: {e}')

print("STEP 2678 - Check element div#ot-pc-content.['ot-pc-scrollbar', 'ot-sdk-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "ot-pc-content")))
    print('PASS - step 2678')
except Exception as e:
    print('FAIL - step 2678' if isinstance(e, AssertionError) else f'ERROR - step 2678: {e}')

print("STEP 2679 - Check element div#None.['ot-optout-signal', 'ot-hide']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-optout-signal', 'ot-hide']")))
    print('PASS - step 2679')
except Exception as e:
    print('FAIL - step 2679' if isinstance(e, AssertionError) else f'ERROR - step 2679: {e}')

print("STEP 2680 - Check element div#None.['ot-optout-icon']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-optout-icon']")))
    print('PASS - step 2680')
except Exception as e:
    print('FAIL - step 2680' if isinstance(e, AssertionError) else f'ERROR - step 2680: {e}')

print("STEP 2681 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 2681')
except Exception as e:
    print('FAIL - step 2681' if isinstance(e, AssertionError) else f'ERROR - step 2681: {e}')

print("STEP 2682 - Check element path#None.['ot-floating-button__svg-fill']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-floating-button__svg-fill']")))
    print('PASS - step 2682')
except Exception as e:
    print('FAIL - step 2682' if isinstance(e, AssertionError) else f'ERROR - step 2682: {e}')

print("STEP 2683 - Check element span#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "span")))
    print('PASS - step 2683')
except Exception as e:
    print('FAIL - step 2683' if isinstance(e, AssertionError) else f'ERROR - step 2683: {e}')

print("STEP 2684 - Check element div#None.['ot-sdk-container', 'ot-grps-cntr', 'ot-sdk-column']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-sdk-container', 'ot-grps-cntr', 'ot-sdk-column']")))
    print('PASS - step 2684')
except Exception as e:
    print('FAIL - step 2684' if isinstance(e, AssertionError) else f'ERROR - step 2684: {e}')

print("STEP 2685 - Check element div#None.['ot-sdk-four', 'ot-sdk-columns', 'ot-tab-list']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-sdk-four', 'ot-sdk-columns', 'ot-tab-list']")))
    print('PASS - step 2685')
except Exception as e:
    print('FAIL - step 2685' if isinstance(e, AssertionError) else f'ERROR - step 2685: {e}')

print("STEP 2686 - Check element h2#ot-pc-title-mobile.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "ot-pc-title-mobile")))
    print('PASS - step 2686')
except Exception as e:
    print('FAIL - step 2686' if isinstance(e, AssertionError) else f'ERROR - step 2686: {e}')

print("STEP 2687 - Check element ul#None.['ot-cat-grp']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-cat-grp']")))
    print('PASS - step 2687')
except Exception as e:
    print('FAIL - step 2687' if isinstance(e, AssertionError) else f'ERROR - step 2687: {e}')

print("STEP 2688 - Check element li#None.['ot-abt-tab']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-abt-tab']")))
    print('PASS - step 2688')
except Exception as e:
    print('FAIL - step 2688' if isinstance(e, AssertionError) else f'ERROR - step 2688: {e}')

print("STEP 2689 - Check element div#None.['ot-active-menu', 'category-menu-switch-handler']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-active-menu', 'category-menu-switch-handler']")))
    print('PASS - step 2689')
except Exception as e:
    print('FAIL - step 2689' if isinstance(e, AssertionError) else f'ERROR - step 2689: {e}')

print("STEP 2690 - Check element h3#ot-pvcy-txt.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "ot-pvcy-txt")))
    print('PASS - step 2690')
except Exception as e:
    print('FAIL - step 2690' if isinstance(e, AssertionError) else f'ERROR - step 2690: {e}')

print("STEP 2691 - Check element li#None.['ot-cat-item', 'ot-always-active-group', 'ot-vs-config']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-cat-item', 'ot-always-active-group', 'ot-vs-config']")))
    print('PASS - step 2691')
except Exception as e:
    print('FAIL - step 2691' if isinstance(e, AssertionError) else f'ERROR - step 2691: {e}')

print("STEP 2692 - Check element div#None.['category-menu-switch-handler']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['category-menu-switch-handler']")))
    print('PASS - step 2692')
except Exception as e:
    print('FAIL - step 2692' if isinstance(e, AssertionError) else f'ERROR - step 2692: {e}')

print("STEP 2693 - Check element h3#ot-header-id-1.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "ot-header-id-1")))
    print('PASS - step 2693')
except Exception as e:
    print('FAIL - step 2693' if isinstance(e, AssertionError) else f'ERROR - step 2693: {e}')

print("STEP 2694 - Check element li#None.['ot-cat-item', 'ot-vs-config']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-cat-item', 'ot-vs-config']")))
    print('PASS - step 2694')
except Exception as e:
    print('FAIL - step 2694' if isinstance(e, AssertionError) else f'ERROR - step 2694: {e}')

print("STEP 2695 - Check element div#None.['category-menu-switch-handler']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['category-menu-switch-handler']")))
    print('PASS - step 2695')
except Exception as e:
    print('FAIL - step 2695' if isinstance(e, AssertionError) else f'ERROR - step 2695: {e}')

print("STEP 2696 - Check element h3#ot-header-id-2.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "ot-header-id-2")))
    print('PASS - step 2696')
except Exception as e:
    print('FAIL - step 2696' if isinstance(e, AssertionError) else f'ERROR - step 2696: {e}')

print("STEP 2697 - Check element li#None.['ot-cat-item', 'ot-vs-config']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-cat-item', 'ot-vs-config']")))
    print('PASS - step 2697')
except Exception as e:
    print('FAIL - step 2697' if isinstance(e, AssertionError) else f'ERROR - step 2697: {e}')

print("STEP 2698 - Check element div#None.['category-menu-switch-handler']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['category-menu-switch-handler']")))
    print('PASS - step 2698')
except Exception as e:
    print('FAIL - step 2698' if isinstance(e, AssertionError) else f'ERROR - step 2698: {e}')

print("STEP 2699 - Check element h3#ot-header-id-3.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "ot-header-id-3")))
    print('PASS - step 2699')
except Exception as e:
    print('FAIL - step 2699' if isinstance(e, AssertionError) else f'ERROR - step 2699: {e}')

print("STEP 2700 - Check element li#None.['ot-cat-item', 'ot-vs-config']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-cat-item', 'ot-vs-config']")))
    print('PASS - step 2700')
except Exception as e:
    print('FAIL - step 2700' if isinstance(e, AssertionError) else f'ERROR - step 2700: {e}')

print("STEP 2701 - Check element div#None.['category-menu-switch-handler']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['category-menu-switch-handler']")))
    print('PASS - step 2701')
except Exception as e:
    print('FAIL - step 2701' if isinstance(e, AssertionError) else f'ERROR - step 2701: {e}')

print("STEP 2702 - Check element h3#ot-header-id-4.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "ot-header-id-4")))
    print('PASS - step 2702')
except Exception as e:
    print('FAIL - step 2702' if isinstance(e, AssertionError) else f'ERROR - step 2702: {e}')

print("STEP 2703 - Check element div#None.['ot-tab-desc', 'ot-sdk-eight', 'ot-sdk-columns']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-tab-desc', 'ot-sdk-eight', 'ot-sdk-columns']")))
    print('PASS - step 2703')
except Exception as e:
    print('FAIL - step 2703' if isinstance(e, AssertionError) else f'ERROR - step 2703: {e}')

print("STEP 2704 - Check element div#ot-tab-desc.['ot-desc-cntr']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "ot-tab-desc")))
    print('PASS - step 2704')
except Exception as e:
    print('FAIL - step 2704' if isinstance(e, AssertionError) else f'ERROR - step 2704: {e}')

print("STEP 2705 - Check element h4#ot-pvcy-hdr.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "ot-pvcy-hdr")))
    print('PASS - step 2705')
except Exception as e:
    print('FAIL - step 2705' if isinstance(e, AssertionError) else f'ERROR - step 2705: {e}')

print("STEP 2706 - Check element p#ot-pc-desc.['ot-grp-desc']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "ot-pc-desc")))
    print('PASS - step 2706')
except Exception as e:
    print('FAIL - step 2706' if isinstance(e, AssertionError) else f'ERROR - step 2706: {e}')

print("STEP 2707 - Check element br#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "br")))
    print('PASS - step 2707')
except Exception as e:
    print('FAIL - step 2707' if isinstance(e, AssertionError) else f'ERROR - step 2707: {e}')

print("STEP 2708 - Check element a#None.['privacy-notice-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['privacy-notice-link']")))
    print('PASS - step 2708')
except Exception as e:
    print('FAIL - step 2708' if isinstance(e, AssertionError) else f'ERROR - step 2708: {e}')

print("STEP 2709 - Check element div#ot-desc-id-1.['ot-desc-cntr', 'ot-hide', 'ot-always-active-group']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "ot-desc-id-1")))
    print('PASS - step 2709')
except Exception as e:
    print('FAIL - step 2709' if isinstance(e, AssertionError) else f'ERROR - step 2709: {e}')

print("STEP 2710 - Check element div#None.['ot-grp-hdr1']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-grp-hdr1']")))
    print('PASS - step 2710')
except Exception as e:
    print('FAIL - step 2710' if isinstance(e, AssertionError) else f'ERROR - step 2710: {e}')

print("STEP 2711 - Check element h4#None.['ot-cat-header']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-cat-header']")))
    print('PASS - step 2711')
except Exception as e:
    print('FAIL - step 2711' if isinstance(e, AssertionError) else f'ERROR - step 2711: {e}')

print("STEP 2712 - Check element div#None.['ot-tgl-cntr']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-tgl-cntr']")))
    print('PASS - step 2712')
except Exception as e:
    print('FAIL - step 2712' if isinstance(e, AssertionError) else f'ERROR - step 2712: {e}')

print("STEP 2713 - Check element div#None.['ot-always-active']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-always-active']")))
    print('PASS - step 2713')
except Exception as e:
    print('FAIL - step 2713' if isinstance(e, AssertionError) else f'ERROR - step 2713: {e}')

print("STEP 2714 - Check element p#None.['ot-grp-desc', 'ot-category-desc']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-grp-desc', 'ot-category-desc']")))
    print('PASS - step 2714')
except Exception as e:
    print('FAIL - step 2714' if isinstance(e, AssertionError) else f'ERROR - step 2714: {e}')

print("STEP 2715 - Check element div#ot-desc-id-2.['ot-desc-cntr', 'ot-hide']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "ot-desc-id-2")))
    print('PASS - step 2715')
except Exception as e:
    print('FAIL - step 2715' if isinstance(e, AssertionError) else f'ERROR - step 2715: {e}')

print("STEP 2716 - Check element div#None.['ot-grp-hdr1']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-grp-hdr1']")))
    print('PASS - step 2716')
except Exception as e:
    print('FAIL - step 2716' if isinstance(e, AssertionError) else f'ERROR - step 2716: {e}')

print("STEP 2717 - Check element h4#None.['ot-cat-header']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-cat-header']")))
    print('PASS - step 2717')
except Exception as e:
    print('FAIL - step 2717' if isinstance(e, AssertionError) else f'ERROR - step 2717: {e}')

print("STEP 2718 - Check element div#None.['ot-tgl']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-tgl']")))
    print('PASS - step 2718')
except Exception as e:
    print('FAIL - step 2718' if isinstance(e, AssertionError) else f'ERROR - step 2718: {e}')

print("STEP 2719 - Check element input#ot-group-id-2.['category-switch-handler']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "ot-group-id-2")))
    print('PASS - step 2719')
except Exception as e:
    print('FAIL - step 2719' if isinstance(e, AssertionError) else f'ERROR - step 2719: {e}')

print("STEP 2720 - Check element label#None.['ot-switch']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-switch']")))
    print('PASS - step 2720')
except Exception as e:
    print('FAIL - step 2720' if isinstance(e, AssertionError) else f'ERROR - step 2720: {e}')

print("STEP 2721 - Check element span#None.['ot-switch-nob']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-switch-nob']")))
    print('PASS - step 2721')
except Exception as e:
    print('FAIL - step 2721' if isinstance(e, AssertionError) else f'ERROR - step 2721: {e}')

print("STEP 2722 - Check element span#None.['ot-label-txt']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-label-txt']")))
    print('PASS - step 2722')
except Exception as e:
    print('FAIL - step 2722' if isinstance(e, AssertionError) else f'ERROR - step 2722: {e}')

print("STEP 2723 - Check element div#None.['ot-tgl-cntr']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-tgl-cntr']")))
    print('PASS - step 2723')
except Exception as e:
    print('FAIL - step 2723' if isinstance(e, AssertionError) else f'ERROR - step 2723: {e}')

print("STEP 2724 - Check element p#None.['ot-grp-desc', 'ot-category-desc']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-grp-desc', 'ot-category-desc']")))
    print('PASS - step 2724')
except Exception as e:
    print('FAIL - step 2724' if isinstance(e, AssertionError) else f'ERROR - step 2724: {e}')

print("STEP 2725 - Check element div#ot-desc-id-3.['ot-desc-cntr', 'ot-hide']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "ot-desc-id-3")))
    print('PASS - step 2725')
except Exception as e:
    print('FAIL - step 2725' if isinstance(e, AssertionError) else f'ERROR - step 2725: {e}')

print("STEP 2726 - Check element div#None.['ot-grp-hdr1']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-grp-hdr1']")))
    print('PASS - step 2726')
except Exception as e:
    print('FAIL - step 2726' if isinstance(e, AssertionError) else f'ERROR - step 2726: {e}')

print("STEP 2727 - Check element h4#None.['ot-cat-header']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-cat-header']")))
    print('PASS - step 2727')
except Exception as e:
    print('FAIL - step 2727' if isinstance(e, AssertionError) else f'ERROR - step 2727: {e}')

print("STEP 2728 - Check element div#None.['ot-tgl']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-tgl']")))
    print('PASS - step 2728')
except Exception as e:
    print('FAIL - step 2728' if isinstance(e, AssertionError) else f'ERROR - step 2728: {e}')

print("STEP 2729 - Check element input#ot-group-id-3.['category-switch-handler']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "ot-group-id-3")))
    print('PASS - step 2729')
except Exception as e:
    print('FAIL - step 2729' if isinstance(e, AssertionError) else f'ERROR - step 2729: {e}')

print("STEP 2730 - Check element label#None.['ot-switch']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-switch']")))
    print('PASS - step 2730')
except Exception as e:
    print('FAIL - step 2730' if isinstance(e, AssertionError) else f'ERROR - step 2730: {e}')

print("STEP 2731 - Check element span#None.['ot-switch-nob']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-switch-nob']")))
    print('PASS - step 2731')
except Exception as e:
    print('FAIL - step 2731' if isinstance(e, AssertionError) else f'ERROR - step 2731: {e}')

print("STEP 2732 - Check element span#None.['ot-label-txt']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-label-txt']")))
    print('PASS - step 2732')
except Exception as e:
    print('FAIL - step 2732' if isinstance(e, AssertionError) else f'ERROR - step 2732: {e}')

print("STEP 2733 - Check element div#None.['ot-tgl-cntr']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-tgl-cntr']")))
    print('PASS - step 2733')
except Exception as e:
    print('FAIL - step 2733' if isinstance(e, AssertionError) else f'ERROR - step 2733: {e}')

print("STEP 2734 - Check element p#None.['ot-grp-desc', 'ot-category-desc']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-grp-desc', 'ot-category-desc']")))
    print('PASS - step 2734')
except Exception as e:
    print('FAIL - step 2734' if isinstance(e, AssertionError) else f'ERROR - step 2734: {e}')

print("STEP 2735 - Check element div#ot-desc-id-4.['ot-desc-cntr', 'ot-hide']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "ot-desc-id-4")))
    print('PASS - step 2735')
except Exception as e:
    print('FAIL - step 2735' if isinstance(e, AssertionError) else f'ERROR - step 2735: {e}')

print("STEP 2736 - Check element div#None.['ot-grp-hdr1']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-grp-hdr1']")))
    print('PASS - step 2736')
except Exception as e:
    print('FAIL - step 2736' if isinstance(e, AssertionError) else f'ERROR - step 2736: {e}')

print("STEP 2737 - Check element h4#None.['ot-cat-header']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-cat-header']")))
    print('PASS - step 2737')
except Exception as e:
    print('FAIL - step 2737' if isinstance(e, AssertionError) else f'ERROR - step 2737: {e}')

print("STEP 2738 - Check element div#None.['ot-tgl']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-tgl']")))
    print('PASS - step 2738')
except Exception as e:
    print('FAIL - step 2738' if isinstance(e, AssertionError) else f'ERROR - step 2738: {e}')

print("STEP 2739 - Check element input#ot-group-id-4.['category-switch-handler']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "ot-group-id-4")))
    print('PASS - step 2739')
except Exception as e:
    print('FAIL - step 2739' if isinstance(e, AssertionError) else f'ERROR - step 2739: {e}')

print("STEP 2740 - Check element label#None.['ot-switch']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-switch']")))
    print('PASS - step 2740')
except Exception as e:
    print('FAIL - step 2740' if isinstance(e, AssertionError) else f'ERROR - step 2740: {e}')

print("STEP 2741 - Check element span#None.['ot-switch-nob']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-switch-nob']")))
    print('PASS - step 2741')
except Exception as e:
    print('FAIL - step 2741' if isinstance(e, AssertionError) else f'ERROR - step 2741: {e}')

print("STEP 2742 - Check element span#None.['ot-label-txt']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-label-txt']")))
    print('PASS - step 2742')
except Exception as e:
    print('FAIL - step 2742' if isinstance(e, AssertionError) else f'ERROR - step 2742: {e}')

print("STEP 2743 - Check element div#None.['ot-tgl-cntr']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-tgl-cntr']")))
    print('PASS - step 2743')
except Exception as e:
    print('FAIL - step 2743' if isinstance(e, AssertionError) else f'ERROR - step 2743: {e}')

print("STEP 2744 - Check element p#None.['ot-grp-desc', 'ot-category-desc']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-grp-desc', 'ot-category-desc']")))
    print('PASS - step 2744')
except Exception as e:
    print('FAIL - step 2744' if isinstance(e, AssertionError) else f'ERROR - step 2744: {e}')

print("STEP 2745 - Check element section#ot-pc-lst.['ot-hide', 'ot-pc-scrollbar', 'ot-enbl-chr']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "ot-pc-lst")))
    print('PASS - step 2745')
except Exception as e:
    print('FAIL - step 2745' if isinstance(e, AssertionError) else f'ERROR - step 2745: {e}')

print("STEP 2746 - Check element div#None.['ot-lst-cntr', 'ot-pc-scrollbar']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-lst-cntr', 'ot-pc-scrollbar']")))
    print('PASS - step 2746')
except Exception as e:
    print('FAIL - step 2746' if isinstance(e, AssertionError) else f'ERROR - step 2746: {e}')

print("STEP 2747 - Check element div#ot-pc-hdr.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "ot-pc-hdr")))
    print('PASS - step 2747')
except Exception as e:
    print('FAIL - step 2747' if isinstance(e, AssertionError) else f'ERROR - step 2747: {e}')

print("STEP 2748 - Check element div#ot-lst-title.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "ot-lst-title")))
    print('PASS - step 2748')
except Exception as e:
    print('FAIL - step 2748' if isinstance(e, AssertionError) else f'ERROR - step 2748: {e}')

print("STEP 2749 - Check element button#None.['ot-link-btn', 'back-btn-handler']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-link-btn', 'back-btn-handler']")))
    print('PASS - step 2749')
except Exception as e:
    print('FAIL - step 2749' if isinstance(e, AssertionError) else f'ERROR - step 2749: {e}')

print("STEP 2750 - Check element svg#ot-back-arw.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "ot-back-arw")))
    print('PASS - step 2750')
except Exception as e:
    print('FAIL - step 2750' if isinstance(e, AssertionError) else f'ERROR - step 2750: {e}')

print("STEP 2751 - Check element title#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "title")))
    print('PASS - step 2751')
except Exception as e:
    print('FAIL - step 2751' if isinstance(e, AssertionError) else f'ERROR - step 2751: {e}')

print("STEP 2752 - Check element g#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "g")))
    print('PASS - step 2752')
except Exception as e:
    print('FAIL - step 2752' if isinstance(e, AssertionError) else f'ERROR - step 2752: {e}')

print("STEP 2753 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2753')
except Exception as e:
    print('FAIL - step 2753' if isinstance(e, AssertionError) else f'ERROR - step 2753: {e}')

print("STEP 2754 - Check element h3#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h3")))
    print('PASS - step 2754')
except Exception as e:
    print('FAIL - step 2754' if isinstance(e, AssertionError) else f'ERROR - step 2754: {e}')

print("STEP 2755 - Check element div#None.['ot-lst-subhdr']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-lst-subhdr']")))
    print('PASS - step 2755')
except Exception as e:
    print('FAIL - step 2755' if isinstance(e, AssertionError) else f'ERROR - step 2755: {e}')

print("STEP 2756 - Check element div#ot-search-cntr.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "ot-search-cntr")))
    print('PASS - step 2756')
except Exception as e:
    print('FAIL - step 2756' if isinstance(e, AssertionError) else f'ERROR - step 2756: {e}')

print("STEP 2757 - Check element p#None.['ot-scrn-rdr']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-scrn-rdr']")))
    print('PASS - step 2757')
except Exception as e:
    print('FAIL - step 2757' if isinstance(e, AssertionError) else f'ERROR - step 2757: {e}')

print("STEP 2758 - Check element input#vendor-search-handler.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "vendor-search-handler")))
    print('PASS - step 2758')
except Exception as e:
    print('FAIL - step 2758' if isinstance(e, AssertionError) else f'ERROR - step 2758: {e}')

print("STEP 2759 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 2759')
except Exception as e:
    print('FAIL - step 2759' if isinstance(e, AssertionError) else f'ERROR - step 2759: {e}')

print("STEP 2760 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2760')
except Exception as e:
    print('FAIL - step 2760' if isinstance(e, AssertionError) else f'ERROR - step 2760: {e}')

print("STEP 2761 - Check element div#ot-fltr-cntr.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "ot-fltr-cntr")))
    print('PASS - step 2761')
except Exception as e:
    print('FAIL - step 2761' if isinstance(e, AssertionError) else f'ERROR - step 2761: {e}')

print("STEP 2762 - Check element button#filter-btn-handler.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "filter-btn-handler")))
    print('PASS - step 2762')
except Exception as e:
    print('FAIL - step 2762' if isinstance(e, AssertionError) else f'ERROR - step 2762: {e}')

print("STEP 2763 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 2763')
except Exception as e:
    print('FAIL - step 2763' if isinstance(e, AssertionError) else f'ERROR - step 2763: {e}')

print("STEP 2764 - Check element title#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "title")))
    print('PASS - step 2764')
except Exception as e:
    print('FAIL - step 2764' if isinstance(e, AssertionError) else f'ERROR - step 2764: {e}')

print("STEP 2765 - Check element g#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "g")))
    print('PASS - step 2765')
except Exception as e:
    print('FAIL - step 2765' if isinstance(e, AssertionError) else f'ERROR - step 2765: {e}')

print("STEP 2766 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 2766')
except Exception as e:
    print('FAIL - step 2766' if isinstance(e, AssertionError) else f'ERROR - step 2766: {e}')

print("STEP 2767 - Check element section#ot-lst-cnt.['ot-pc-scrollbar']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "ot-lst-cnt")))
    print('PASS - step 2767')
except Exception as e:
    print('FAIL - step 2767' if isinstance(e, AssertionError) else f'ERROR - step 2767: {e}')

print("STEP 2768 - Check element div#None.['ot-sdk-row']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-sdk-row']")))
    print('PASS - step 2768')
except Exception as e:
    print('FAIL - step 2768' if isinstance(e, AssertionError) else f'ERROR - step 2768: {e}')

print("STEP 2769 - Check element div#None.['ot-sdk-column']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-sdk-column']")))
    print('PASS - step 2769')
except Exception as e:
    print('FAIL - step 2769' if isinstance(e, AssertionError) else f'ERROR - step 2769: {e}')

print("STEP 2770 - Check element div#ot-sel-blk.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "ot-sel-blk")))
    print('PASS - step 2770')
except Exception as e:
    print('FAIL - step 2770' if isinstance(e, AssertionError) else f'ERROR - step 2770: {e}')

print("STEP 2771 - Check element div#None.['ot-sel-all']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-sel-all']")))
    print('PASS - step 2771')
except Exception as e:
    print('FAIL - step 2771' if isinstance(e, AssertionError) else f'ERROR - step 2771: {e}')

print("STEP 2772 - Check element div#None.['ot-sel-all-hdr']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-sel-all-hdr']")))
    print('PASS - step 2772')
except Exception as e:
    print('FAIL - step 2772' if isinstance(e, AssertionError) else f'ERROR - step 2772: {e}')

print("STEP 2773 - Check element span#None.['ot-consent-hdr']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-consent-hdr']")))
    print('PASS - step 2773')
except Exception as e:
    print('FAIL - step 2773' if isinstance(e, AssertionError) else f'ERROR - step 2773: {e}')

print("STEP 2774 - Check element span#None.['ot-li-hdr']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-li-hdr']")))
    print('PASS - step 2774')
except Exception as e:
    print('FAIL - step 2774' if isinstance(e, AssertionError) else f'ERROR - step 2774: {e}')

print("STEP 2775 - Check element div#None.['ot-sel-all-chkbox']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-sel-all-chkbox']")))
    print('PASS - step 2775')
except Exception as e:
    print('FAIL - step 2775' if isinstance(e, AssertionError) else f'ERROR - step 2775: {e}')

print("STEP 2776 - Check element div#ot-selall-hostcntr.['ot-chkbox']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "ot-selall-hostcntr")))
    print('PASS - step 2776')
except Exception as e:
    print('FAIL - step 2776' if isinstance(e, AssertionError) else f'ERROR - step 2776: {e}')

print("STEP 2777 - Check element input#select-all-hosts-groups-handler.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "select-all-hosts-groups-handler")))
    print('PASS - step 2777')
except Exception as e:
    print('FAIL - step 2777' if isinstance(e, AssertionError) else f'ERROR - step 2777: {e}')

print("STEP 2778 - Check element label#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "label")))
    print('PASS - step 2778')
except Exception as e:
    print('FAIL - step 2778' if isinstance(e, AssertionError) else f'ERROR - step 2778: {e}')

print("STEP 2779 - Check element span#None.['ot-label-txt']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-label-txt']")))
    print('PASS - step 2779')
except Exception as e:
    print('FAIL - step 2779' if isinstance(e, AssertionError) else f'ERROR - step 2779: {e}')

print("STEP 2780 - Check element span#None.['ot-label-status']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-label-status']")))
    print('PASS - step 2780')
except Exception as e:
    print('FAIL - step 2780' if isinstance(e, AssertionError) else f'ERROR - step 2780: {e}')

print("STEP 2781 - Check element div#ot-selall-vencntr.['ot-chkbox']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "ot-selall-vencntr")))
    print('PASS - step 2781')
except Exception as e:
    print('FAIL - step 2781' if isinstance(e, AssertionError) else f'ERROR - step 2781: {e}')

print("STEP 2782 - Check element input#select-all-vendor-groups-handler.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "select-all-vendor-groups-handler")))
    print('PASS - step 2782')
except Exception as e:
    print('FAIL - step 2782' if isinstance(e, AssertionError) else f'ERROR - step 2782: {e}')

print("STEP 2783 - Check element label#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "label")))
    print('PASS - step 2783')
except Exception as e:
    print('FAIL - step 2783' if isinstance(e, AssertionError) else f'ERROR - step 2783: {e}')

print("STEP 2784 - Check element span#None.['ot-label-txt']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-label-txt']")))
    print('PASS - step 2784')
except Exception as e:
    print('FAIL - step 2784' if isinstance(e, AssertionError) else f'ERROR - step 2784: {e}')

print("STEP 2785 - Check element span#None.['ot-label-status']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-label-status']")))
    print('PASS - step 2785')
except Exception as e:
    print('FAIL - step 2785' if isinstance(e, AssertionError) else f'ERROR - step 2785: {e}')

print("STEP 2786 - Check element div#ot-selall-licntr.['ot-chkbox']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "ot-selall-licntr")))
    print('PASS - step 2786')
except Exception as e:
    print('FAIL - step 2786' if isinstance(e, AssertionError) else f'ERROR - step 2786: {e}')

print("STEP 2787 - Check element input#select-all-vendor-leg-handler.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "select-all-vendor-leg-handler")))
    print('PASS - step 2787')
except Exception as e:
    print('FAIL - step 2787' if isinstance(e, AssertionError) else f'ERROR - step 2787: {e}')

print("STEP 2788 - Check element label#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "label")))
    print('PASS - step 2788')
except Exception as e:
    print('FAIL - step 2788' if isinstance(e, AssertionError) else f'ERROR - step 2788: {e}')

print("STEP 2789 - Check element span#None.['ot-label-txt']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-label-txt']")))
    print('PASS - step 2789')
except Exception as e:
    print('FAIL - step 2789' if isinstance(e, AssertionError) else f'ERROR - step 2789: {e}')

print("STEP 2790 - Check element span#None.['ot-label-status']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-label-status']")))
    print('PASS - step 2790')
except Exception as e:
    print('FAIL - step 2790' if isinstance(e, AssertionError) else f'ERROR - step 2790: {e}')

print("STEP 2791 - Check element div#ot-anchor.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "ot-anchor")))
    print('PASS - step 2791')
except Exception as e:
    print('FAIL - step 2791' if isinstance(e, AssertionError) else f'ERROR - step 2791: {e}')

print("STEP 2792 - Check element section#ot-fltr-modal.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "ot-fltr-modal")))
    print('PASS - step 2792')
except Exception as e:
    print('FAIL - step 2792' if isinstance(e, AssertionError) else f'ERROR - step 2792: {e}')

print("STEP 2793 - Check element div#ot-fltr-cnt.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "ot-fltr-cnt")))
    print('PASS - step 2793')
except Exception as e:
    print('FAIL - step 2793' if isinstance(e, AssertionError) else f'ERROR - step 2793: {e}')

print("STEP 2794 - Check element div#ot-filter-list-header.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "ot-filter-list-header")))
    print('PASS - step 2794')
except Exception as e:
    print('FAIL - step 2794' if isinstance(e, AssertionError) else f'ERROR - step 2794: {e}')

print("STEP 2795 - Check element button#clear-filters-handler.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "clear-filters-handler")))
    print('PASS - step 2795')
except Exception as e:
    print('FAIL - step 2795' if isinstance(e, AssertionError) else f'ERROR - step 2795: {e}')

print("STEP 2796 - Check element div#None.['ot-fltr-scrlcnt', 'ot-pc-scrollbar']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-fltr-scrlcnt', 'ot-pc-scrollbar']")))
    print('PASS - step 2796')
except Exception as e:
    print('FAIL - step 2796' if isinstance(e, AssertionError) else f'ERROR - step 2796: {e}')

print("STEP 2797 - Check element div#None.['ot-fltr-opts']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-fltr-opts']")))
    print('PASS - step 2797')
except Exception as e:
    print('FAIL - step 2797' if isinstance(e, AssertionError) else f'ERROR - step 2797: {e}')

print("STEP 2798 - Check element div#None.['ot-fltr-opt']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-fltr-opt']")))
    print('PASS - step 2798')
except Exception as e:
    print('FAIL - step 2798' if isinstance(e, AssertionError) else f'ERROR - step 2798: {e}')

print("STEP 2799 - Check element div#None.['ot-chkbox']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-chkbox']")))
    print('PASS - step 2799')
except Exception as e:
    print('FAIL - step 2799' if isinstance(e, AssertionError) else f'ERROR - step 2799: {e}')

print("STEP 2800 - Check element input#chkbox-id.['category-filter-handler']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "chkbox-id")))
    print('PASS - step 2800')
except Exception as e:
    print('FAIL - step 2800' if isinstance(e, AssertionError) else f'ERROR - step 2800: {e}')

print("STEP 2801 - Check element label#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "label")))
    print('PASS - step 2801')
except Exception as e:
    print('FAIL - step 2801' if isinstance(e, AssertionError) else f'ERROR - step 2801: {e}')

print("STEP 2802 - Check element span#None.['ot-label-txt']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-label-txt']")))
    print('PASS - step 2802')
except Exception as e:
    print('FAIL - step 2802' if isinstance(e, AssertionError) else f'ERROR - step 2802: {e}')

print("STEP 2803 - Check element span#None.['ot-label-status']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-label-status']")))
    print('PASS - step 2803')
except Exception as e:
    print('FAIL - step 2803' if isinstance(e, AssertionError) else f'ERROR - step 2803: {e}')

print("STEP 2804 - Check element div#None.['ot-fltr-btns']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-fltr-btns']")))
    print('PASS - step 2804')
except Exception as e:
    print('FAIL - step 2804' if isinstance(e, AssertionError) else f'ERROR - step 2804: {e}')

print("STEP 2805 - Check element button#filter-apply-handler.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "filter-apply-handler")))
    print('PASS - step 2805')
except Exception as e:
    print('FAIL - step 2805' if isinstance(e, AssertionError) else f'ERROR - step 2805: {e}')

print("STEP 2806 - Check element button#filter-cancel-handler.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "filter-cancel-handler")))
    print('PASS - step 2806')
except Exception as e:
    print('FAIL - step 2806' if isinstance(e, AssertionError) else f'ERROR - step 2806: {e}')

print("STEP 2807 - Check element div#None.['ot-pc-footer', 'ot-pc-scrollbar']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-pc-footer', 'ot-pc-scrollbar']")))
    print('PASS - step 2807')
except Exception as e:
    print('FAIL - step 2807' if isinstance(e, AssertionError) else f'ERROR - step 2807: {e}')

print("STEP 2808 - Check element div#None.['ot-btn-container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-btn-container']")))
    print('PASS - step 2808')
except Exception as e:
    print('FAIL - step 2808' if isinstance(e, AssertionError) else f'ERROR - step 2808: {e}')

print("STEP 2809 - Check element button#None.['save-preference-btn-handler', 'onetrust-close-btn-handler']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['save-preference-btn-handler', 'onetrust-close-btn-handler']")))
    print('PASS - step 2809')
except Exception as e:
    print('FAIL - step 2809' if isinstance(e, AssertionError) else f'ERROR - step 2809: {e}')

print("STEP 2810 - Check element div#None.['ot-btn-subcntr']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-btn-subcntr']")))
    print('PASS - step 2810')
except Exception as e:
    print('FAIL - step 2810' if isinstance(e, AssertionError) else f'ERROR - step 2810: {e}')

print("STEP 2811 - Check element button#None.['ot-pc-refuse-all-handler']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-pc-refuse-all-handler']")))
    print('PASS - step 2811')
except Exception as e:
    print('FAIL - step 2811' if isinstance(e, AssertionError) else f'ERROR - step 2811: {e}')

print("STEP 2812 - Check element button#accept-recommended-btn-handler.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "accept-recommended-btn-handler")))
    print('PASS - step 2812')
except Exception as e:
    print('FAIL - step 2812' if isinstance(e, AssertionError) else f'ERROR - step 2812: {e}')

print("STEP 2813 - Check element div#None.['ot-pc-footer-logo']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-pc-footer-logo']")))
    print('PASS - step 2813')
except Exception as e:
    print('FAIL - step 2813' if isinstance(e, AssertionError) else f'ERROR - step 2813: {e}')

print("STEP 2814 - Check element a#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "a")))
    print('PASS - step 2814')
except Exception as e:
    print('FAIL - step 2814' if isinstance(e, AssertionError) else f'ERROR - step 2814: {e}')

print("STEP 2815 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 2815')
except Exception as e:
    print('FAIL - step 2815' if isinstance(e, AssertionError) else f'ERROR - step 2815: {e}')

print("STEP 2816 - Check element span#None.['ot-scrn-rdr']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-scrn-rdr']")))
    print('PASS - step 2816')
except Exception as e:
    print('FAIL - step 2816' if isinstance(e, AssertionError) else f'ERROR - step 2816: {e}')

print("STEP 2817 - Check element iframe#None.['ot-text-resize']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ot-text-resize']")))
    print('PASS - step 2817')
except Exception as e:
    print('FAIL - step 2817' if isinstance(e, AssertionError) else f'ERROR - step 2817: {e}')

driver.quit()