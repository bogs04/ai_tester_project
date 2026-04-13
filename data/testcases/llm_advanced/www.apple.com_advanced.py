from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.apple.com")
wait = WebDriverWait(driver, 10)

print("STEP 1 - Check element html#None.['js', 'no-touch', 'progressive-image', 'no-reduced-motion', 'no-edge', 'no-ie', 'css-mask', 'enhanced-xp', 'desktop', 'no-tablet', 'windows', 'no-android', 'no-retina', 'no-safari', 'no-macos', 'no-old-safari', 'chrome', 'no-firefox', 'no-iphone', 'no-ipad', 'no-old-macos', 'ac-ls-visible', 'ac-ls-fixed']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['js', 'no-touch', 'progressive-image', 'no-reduced-motion', 'no-edge', 'no-ie', 'css-mask', 'enhanced-xp', 'desktop', 'no-tablet', 'windows', 'no-android', 'no-retina', 'no-safari', 'no-macos', 'no-old-safari', 'chrome', 'no-firefox', 'no-iphone', 'no-ipad', 'no-old-macos', 'ac-ls-visible', 'ac-ls-fixed']")))
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

print("STEP 4 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 4')
except Exception as e:
    print('FAIL - step 4' if isinstance(e, AssertionError) else f'ERROR - step 4: {e}')

print("STEP 5 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 5')
except Exception as e:
    print('FAIL - step 5' if isinstance(e, AssertionError) else f'ERROR - step 5: {e}')

print("STEP 6 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 6')
except Exception as e:
    print('FAIL - step 6' if isinstance(e, AssertionError) else f'ERROR - step 6: {e}')

print("STEP 7 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 7')
except Exception as e:
    print('FAIL - step 7' if isinstance(e, AssertionError) else f'ERROR - step 7: {e}')

print("STEP 8 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 8')
except Exception as e:
    print('FAIL - step 8' if isinstance(e, AssertionError) else f'ERROR - step 8: {e}')

print("STEP 9 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 9')
except Exception as e:
    print('FAIL - step 9' if isinstance(e, AssertionError) else f'ERROR - step 9: {e}')

print("STEP 10 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 10')
except Exception as e:
    print('FAIL - step 10' if isinstance(e, AssertionError) else f'ERROR - step 10: {e}')

print("STEP 11 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 11')
except Exception as e:
    print('FAIL - step 11' if isinstance(e, AssertionError) else f'ERROR - step 11: {e}')

print("STEP 12 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 12')
except Exception as e:
    print('FAIL - step 12' if isinstance(e, AssertionError) else f'ERROR - step 12: {e}')

print("STEP 13 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 13')
except Exception as e:
    print('FAIL - step 13' if isinstance(e, AssertionError) else f'ERROR - step 13: {e}')

print("STEP 14 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 14')
except Exception as e:
    print('FAIL - step 14' if isinstance(e, AssertionError) else f'ERROR - step 14: {e}')

print("STEP 15 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 15')
except Exception as e:
    print('FAIL - step 15' if isinstance(e, AssertionError) else f'ERROR - step 15: {e}')

print("STEP 16 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 16')
except Exception as e:
    print('FAIL - step 16' if isinstance(e, AssertionError) else f'ERROR - step 16: {e}')

print("STEP 17 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 17')
except Exception as e:
    print('FAIL - step 17' if isinstance(e, AssertionError) else f'ERROR - step 17: {e}')

print("STEP 18 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 18')
except Exception as e:
    print('FAIL - step 18' if isinstance(e, AssertionError) else f'ERROR - step 18: {e}')

print("STEP 19 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 19')
except Exception as e:
    print('FAIL - step 19' if isinstance(e, AssertionError) else f'ERROR - step 19: {e}')

print("STEP 20 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 20')
except Exception as e:
    print('FAIL - step 20' if isinstance(e, AssertionError) else f'ERROR - step 20: {e}')

print("STEP 21 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 21')
except Exception as e:
    print('FAIL - step 21' if isinstance(e, AssertionError) else f'ERROR - step 21: {e}')

print("STEP 22 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 22')
except Exception as e:
    print('FAIL - step 22' if isinstance(e, AssertionError) else f'ERROR - step 22: {e}')

print("STEP 23 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 23')
except Exception as e:
    print('FAIL - step 23' if isinstance(e, AssertionError) else f'ERROR - step 23: {e}')

print("STEP 24 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 24')
except Exception as e:
    print('FAIL - step 24' if isinstance(e, AssertionError) else f'ERROR - step 24: {e}')

print("STEP 25 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 25')
except Exception as e:
    print('FAIL - step 25' if isinstance(e, AssertionError) else f'ERROR - step 25: {e}')

print("STEP 26 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 26')
except Exception as e:
    print('FAIL - step 26' if isinstance(e, AssertionError) else f'ERROR - step 26: {e}')

print("STEP 27 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 27')
except Exception as e:
    print('FAIL - step 27' if isinstance(e, AssertionError) else f'ERROR - step 27: {e}')

print("STEP 28 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 28')
except Exception as e:
    print('FAIL - step 28' if isinstance(e, AssertionError) else f'ERROR - step 28: {e}')

print("STEP 29 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 29')
except Exception as e:
    print('FAIL - step 29' if isinstance(e, AssertionError) else f'ERROR - step 29: {e}')

print("STEP 30 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 30')
except Exception as e:
    print('FAIL - step 30' if isinstance(e, AssertionError) else f'ERROR - step 30: {e}')

print("STEP 31 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 31')
except Exception as e:
    print('FAIL - step 31' if isinstance(e, AssertionError) else f'ERROR - step 31: {e}')

print("STEP 32 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 32')
except Exception as e:
    print('FAIL - step 32' if isinstance(e, AssertionError) else f'ERROR - step 32: {e}')

print("STEP 33 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 33')
except Exception as e:
    print('FAIL - step 33' if isinstance(e, AssertionError) else f'ERROR - step 33: {e}')

print("STEP 34 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 34')
except Exception as e:
    print('FAIL - step 34' if isinstance(e, AssertionError) else f'ERROR - step 34: {e}')

print("STEP 35 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
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

print("STEP 40 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 40')
except Exception as e:
    print('FAIL - step 40' if isinstance(e, AssertionError) else f'ERROR - step 40: {e}')

print("STEP 41 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 41')
except Exception as e:
    print('FAIL - step 41' if isinstance(e, AssertionError) else f'ERROR - step 41: {e}')

print("STEP 42 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 42')
except Exception as e:
    print('FAIL - step 42' if isinstance(e, AssertionError) else f'ERROR - step 42: {e}')

print("STEP 43 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 43')
except Exception as e:
    print('FAIL - step 43' if isinstance(e, AssertionError) else f'ERROR - step 43: {e}')

print("STEP 44 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
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

print("STEP 48 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 48')
except Exception as e:
    print('FAIL - step 48' if isinstance(e, AssertionError) else f'ERROR - step 48: {e}')

print("STEP 49 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 49')
except Exception as e:
    print('FAIL - step 49' if isinstance(e, AssertionError) else f'ERROR - step 49: {e}')

print("STEP 50 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 50')
except Exception as e:
    print('FAIL - step 50' if isinstance(e, AssertionError) else f'ERROR - step 50: {e}')

print("STEP 51 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 51')
except Exception as e:
    print('FAIL - step 51' if isinstance(e, AssertionError) else f'ERROR - step 51: {e}')

print("STEP 52 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 52')
except Exception as e:
    print('FAIL - step 52' if isinstance(e, AssertionError) else f'ERROR - step 52: {e}')

print("STEP 53 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 53')
except Exception as e:
    print('FAIL - step 53' if isinstance(e, AssertionError) else f'ERROR - step 53: {e}')

print("STEP 54 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 54')
except Exception as e:
    print('FAIL - step 54' if isinstance(e, AssertionError) else f'ERROR - step 54: {e}')

print("STEP 55 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 55')
except Exception as e:
    print('FAIL - step 55' if isinstance(e, AssertionError) else f'ERROR - step 55: {e}')

print("STEP 56 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 56')
except Exception as e:
    print('FAIL - step 56' if isinstance(e, AssertionError) else f'ERROR - step 56: {e}')

print("STEP 57 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 57')
except Exception as e:
    print('FAIL - step 57' if isinstance(e, AssertionError) else f'ERROR - step 57: {e}')

print("STEP 58 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 58')
except Exception as e:
    print('FAIL - step 58' if isinstance(e, AssertionError) else f'ERROR - step 58: {e}')

print("STEP 59 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 59')
except Exception as e:
    print('FAIL - step 59' if isinstance(e, AssertionError) else f'ERROR - step 59: {e}')

print("STEP 60 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 60')
except Exception as e:
    print('FAIL - step 60' if isinstance(e, AssertionError) else f'ERROR - step 60: {e}')

print("STEP 61 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 61')
except Exception as e:
    print('FAIL - step 61' if isinstance(e, AssertionError) else f'ERROR - step 61: {e}')

print("STEP 62 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
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

print("STEP 65 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 65')
except Exception as e:
    print('FAIL - step 65' if isinstance(e, AssertionError) else f'ERROR - step 65: {e}')

print("STEP 66 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 66')
except Exception as e:
    print('FAIL - step 66' if isinstance(e, AssertionError) else f'ERROR - step 66: {e}')

print("STEP 67 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 67')
except Exception as e:
    print('FAIL - step 67' if isinstance(e, AssertionError) else f'ERROR - step 67: {e}')

print("STEP 68 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 68')
except Exception as e:
    print('FAIL - step 68' if isinstance(e, AssertionError) else f'ERROR - step 68: {e}')

print("STEP 69 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 69')
except Exception as e:
    print('FAIL - step 69' if isinstance(e, AssertionError) else f'ERROR - step 69: {e}')

print("STEP 70 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 70')
except Exception as e:
    print('FAIL - step 70' if isinstance(e, AssertionError) else f'ERROR - step 70: {e}')

print("STEP 71 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 71')
except Exception as e:
    print('FAIL - step 71' if isinstance(e, AssertionError) else f'ERROR - step 71: {e}')

print("STEP 72 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 72')
except Exception as e:
    print('FAIL - step 72' if isinstance(e, AssertionError) else f'ERROR - step 72: {e}')

print("STEP 73 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 73')
except Exception as e:
    print('FAIL - step 73' if isinstance(e, AssertionError) else f'ERROR - step 73: {e}')

print("STEP 74 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 74')
except Exception as e:
    print('FAIL - step 74' if isinstance(e, AssertionError) else f'ERROR - step 74: {e}')

print("STEP 75 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 75')
except Exception as e:
    print('FAIL - step 75' if isinstance(e, AssertionError) else f'ERROR - step 75: {e}')

print("STEP 76 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 76')
except Exception as e:
    print('FAIL - step 76' if isinstance(e, AssertionError) else f'ERROR - step 76: {e}')

print("STEP 77 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 77')
except Exception as e:
    print('FAIL - step 77' if isinstance(e, AssertionError) else f'ERROR - step 77: {e}')

print("STEP 78 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 78')
except Exception as e:
    print('FAIL - step 78' if isinstance(e, AssertionError) else f'ERROR - step 78: {e}')

print("STEP 79 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 79')
except Exception as e:
    print('FAIL - step 79' if isinstance(e, AssertionError) else f'ERROR - step 79: {e}')

print("STEP 80 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 80')
except Exception as e:
    print('FAIL - step 80' if isinstance(e, AssertionError) else f'ERROR - step 80: {e}')

print("STEP 81 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 81')
except Exception as e:
    print('FAIL - step 81' if isinstance(e, AssertionError) else f'ERROR - step 81: {e}')

print("STEP 82 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 82')
except Exception as e:
    print('FAIL - step 82' if isinstance(e, AssertionError) else f'ERROR - step 82: {e}')

print("STEP 83 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 83')
except Exception as e:
    print('FAIL - step 83' if isinstance(e, AssertionError) else f'ERROR - step 83: {e}')

print("STEP 84 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 84')
except Exception as e:
    print('FAIL - step 84' if isinstance(e, AssertionError) else f'ERROR - step 84: {e}')

print("STEP 85 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 85')
except Exception as e:
    print('FAIL - step 85' if isinstance(e, AssertionError) else f'ERROR - step 85: {e}')

print("STEP 86 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 86')
except Exception as e:
    print('FAIL - step 86' if isinstance(e, AssertionError) else f'ERROR - step 86: {e}')

print("STEP 87 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 87')
except Exception as e:
    print('FAIL - step 87' if isinstance(e, AssertionError) else f'ERROR - step 87: {e}')

print("STEP 88 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 88')
except Exception as e:
    print('FAIL - step 88' if isinstance(e, AssertionError) else f'ERROR - step 88: {e}')

print("STEP 89 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 89')
except Exception as e:
    print('FAIL - step 89' if isinstance(e, AssertionError) else f'ERROR - step 89: {e}')

print("STEP 90 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 90')
except Exception as e:
    print('FAIL - step 90' if isinstance(e, AssertionError) else f'ERROR - step 90: {e}')

print("STEP 91 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 91')
except Exception as e:
    print('FAIL - step 91' if isinstance(e, AssertionError) else f'ERROR - step 91: {e}')

print("STEP 92 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 92')
except Exception as e:
    print('FAIL - step 92' if isinstance(e, AssertionError) else f'ERROR - step 92: {e}')

print("STEP 93 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 93')
except Exception as e:
    print('FAIL - step 93' if isinstance(e, AssertionError) else f'ERROR - step 93: {e}')

print("STEP 94 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 94')
except Exception as e:
    print('FAIL - step 94' if isinstance(e, AssertionError) else f'ERROR - step 94: {e}')

print("STEP 95 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 95')
except Exception as e:
    print('FAIL - step 95' if isinstance(e, AssertionError) else f'ERROR - step 95: {e}')

print("STEP 96 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 96')
except Exception as e:
    print('FAIL - step 96' if isinstance(e, AssertionError) else f'ERROR - step 96: {e}')

print("STEP 97 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 97')
except Exception as e:
    print('FAIL - step 97' if isinstance(e, AssertionError) else f'ERROR - step 97: {e}')

print("STEP 98 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 98')
except Exception as e:
    print('FAIL - step 98' if isinstance(e, AssertionError) else f'ERROR - step 98: {e}')

print("STEP 99 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 99')
except Exception as e:
    print('FAIL - step 99' if isinstance(e, AssertionError) else f'ERROR - step 99: {e}')

print("STEP 100 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 100')
except Exception as e:
    print('FAIL - step 100' if isinstance(e, AssertionError) else f'ERROR - step 100: {e}')

print("STEP 101 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 101')
except Exception as e:
    print('FAIL - step 101' if isinstance(e, AssertionError) else f'ERROR - step 101: {e}')

print("STEP 102 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 102')
except Exception as e:
    print('FAIL - step 102' if isinstance(e, AssertionError) else f'ERROR - step 102: {e}')

print("STEP 103 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 103')
except Exception as e:
    print('FAIL - step 103' if isinstance(e, AssertionError) else f'ERROR - step 103: {e}')

print("STEP 104 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 104')
except Exception as e:
    print('FAIL - step 104' if isinstance(e, AssertionError) else f'ERROR - step 104: {e}')

print("STEP 105 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 105')
except Exception as e:
    print('FAIL - step 105' if isinstance(e, AssertionError) else f'ERROR - step 105: {e}')

print("STEP 106 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 106')
except Exception as e:
    print('FAIL - step 106' if isinstance(e, AssertionError) else f'ERROR - step 106: {e}')

print("STEP 107 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 107')
except Exception as e:
    print('FAIL - step 107' if isinstance(e, AssertionError) else f'ERROR - step 107: {e}')

print("STEP 108 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 108')
except Exception as e:
    print('FAIL - step 108' if isinstance(e, AssertionError) else f'ERROR - step 108: {e}')

print("STEP 109 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 109')
except Exception as e:
    print('FAIL - step 109' if isinstance(e, AssertionError) else f'ERROR - step 109: {e}')

print("STEP 110 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 110')
except Exception as e:
    print('FAIL - step 110' if isinstance(e, AssertionError) else f'ERROR - step 110: {e}')

print("STEP 111 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 111')
except Exception as e:
    print('FAIL - step 111' if isinstance(e, AssertionError) else f'ERROR - step 111: {e}')

print("STEP 112 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 112')
except Exception as e:
    print('FAIL - step 112' if isinstance(e, AssertionError) else f'ERROR - step 112: {e}')

print("STEP 113 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 113')
except Exception as e:
    print('FAIL - step 113' if isinstance(e, AssertionError) else f'ERROR - step 113: {e}')

print("STEP 114 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 114')
except Exception as e:
    print('FAIL - step 114' if isinstance(e, AssertionError) else f'ERROR - step 114: {e}')

print("STEP 115 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 115')
except Exception as e:
    print('FAIL - step 115' if isinstance(e, AssertionError) else f'ERROR - step 115: {e}')

print("STEP 116 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 116')
except Exception as e:
    print('FAIL - step 116' if isinstance(e, AssertionError) else f'ERROR - step 116: {e}')

print("STEP 117 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 117')
except Exception as e:
    print('FAIL - step 117' if isinstance(e, AssertionError) else f'ERROR - step 117: {e}')

print("STEP 118 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 118')
except Exception as e:
    print('FAIL - step 118' if isinstance(e, AssertionError) else f'ERROR - step 118: {e}')

print("STEP 119 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 119')
except Exception as e:
    print('FAIL - step 119' if isinstance(e, AssertionError) else f'ERROR - step 119: {e}')

print("STEP 120 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 120')
except Exception as e:
    print('FAIL - step 120' if isinstance(e, AssertionError) else f'ERROR - step 120: {e}')

print("STEP 121 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 121')
except Exception as e:
    print('FAIL - step 121' if isinstance(e, AssertionError) else f'ERROR - step 121: {e}')

print("STEP 122 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 122')
except Exception as e:
    print('FAIL - step 122' if isinstance(e, AssertionError) else f'ERROR - step 122: {e}')

print("STEP 123 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 123')
except Exception as e:
    print('FAIL - step 123' if isinstance(e, AssertionError) else f'ERROR - step 123: {e}')

print("STEP 124 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 124')
except Exception as e:
    print('FAIL - step 124' if isinstance(e, AssertionError) else f'ERROR - step 124: {e}')

print("STEP 125 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 125')
except Exception as e:
    print('FAIL - step 125' if isinstance(e, AssertionError) else f'ERROR - step 125: {e}')

print("STEP 126 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 126')
except Exception as e:
    print('FAIL - step 126' if isinstance(e, AssertionError) else f'ERROR - step 126: {e}')

print("STEP 127 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 127')
except Exception as e:
    print('FAIL - step 127' if isinstance(e, AssertionError) else f'ERROR - step 127: {e}')

print("STEP 128 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 128')
except Exception as e:
    print('FAIL - step 128' if isinstance(e, AssertionError) else f'ERROR - step 128: {e}')

print("STEP 129 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 129')
except Exception as e:
    print('FAIL - step 129' if isinstance(e, AssertionError) else f'ERROR - step 129: {e}')

print("STEP 130 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 130')
except Exception as e:
    print('FAIL - step 130' if isinstance(e, AssertionError) else f'ERROR - step 130: {e}')

print("STEP 131 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 131')
except Exception as e:
    print('FAIL - step 131' if isinstance(e, AssertionError) else f'ERROR - step 131: {e}')

print("STEP 132 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 132')
except Exception as e:
    print('FAIL - step 132' if isinstance(e, AssertionError) else f'ERROR - step 132: {e}')

print("STEP 133 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 133')
except Exception as e:
    print('FAIL - step 133' if isinstance(e, AssertionError) else f'ERROR - step 133: {e}')

print("STEP 134 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 134')
except Exception as e:
    print('FAIL - step 134' if isinstance(e, AssertionError) else f'ERROR - step 134: {e}')

print("STEP 135 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 135')
except Exception as e:
    print('FAIL - step 135' if isinstance(e, AssertionError) else f'ERROR - step 135: {e}')

print("STEP 136 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 136')
except Exception as e:
    print('FAIL - step 136' if isinstance(e, AssertionError) else f'ERROR - step 136: {e}')

print("STEP 137 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 137')
except Exception as e:
    print('FAIL - step 137' if isinstance(e, AssertionError) else f'ERROR - step 137: {e}')

print("STEP 138 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 138')
except Exception as e:
    print('FAIL - step 138' if isinstance(e, AssertionError) else f'ERROR - step 138: {e}')

print("STEP 139 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 139')
except Exception as e:
    print('FAIL - step 139' if isinstance(e, AssertionError) else f'ERROR - step 139: {e}')

print("STEP 140 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 140')
except Exception as e:
    print('FAIL - step 140' if isinstance(e, AssertionError) else f'ERROR - step 140: {e}')

print("STEP 141 - Check element meta#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "meta")))
    print('PASS - step 141')
except Exception as e:
    print('FAIL - step 141' if isinstance(e, AssertionError) else f'ERROR - step 141: {e}')

print("STEP 142 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 142')
except Exception as e:
    print('FAIL - step 142' if isinstance(e, AssertionError) else f'ERROR - step 142: {e}')

print("STEP 143 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 143')
except Exception as e:
    print('FAIL - step 143' if isinstance(e, AssertionError) else f'ERROR - step 143: {e}')

print("STEP 144 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 144')
except Exception as e:
    print('FAIL - step 144' if isinstance(e, AssertionError) else f'ERROR - step 144: {e}')

print("STEP 145 - Check element title#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "title")))
    print('PASS - step 145')
except Exception as e:
    print('FAIL - step 145' if isinstance(e, AssertionError) else f'ERROR - step 145: {e}')

print("STEP 146 - Check element meta#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "meta")))
    print('PASS - step 146')
except Exception as e:
    print('FAIL - step 146' if isinstance(e, AssertionError) else f'ERROR - step 146: {e}')

print("STEP 147 - Check element meta#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "meta")))
    print('PASS - step 147')
except Exception as e:
    print('FAIL - step 147' if isinstance(e, AssertionError) else f'ERROR - step 147: {e}')

print("STEP 148 - Check element meta#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "meta")))
    print('PASS - step 148')
except Exception as e:
    print('FAIL - step 148' if isinstance(e, AssertionError) else f'ERROR - step 148: {e}')

print("STEP 149 - Check element meta#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "meta")))
    print('PASS - step 149')
except Exception as e:
    print('FAIL - step 149' if isinstance(e, AssertionError) else f'ERROR - step 149: {e}')

print("STEP 150 - Check element meta#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "meta")))
    print('PASS - step 150')
except Exception as e:
    print('FAIL - step 150' if isinstance(e, AssertionError) else f'ERROR - step 150: {e}')

print("STEP 151 - Check element meta#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "meta")))
    print('PASS - step 151')
except Exception as e:
    print('FAIL - step 151' if isinstance(e, AssertionError) else f'ERROR - step 151: {e}')

print("STEP 152 - Check element meta#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "meta")))
    print('PASS - step 152')
except Exception as e:
    print('FAIL - step 152' if isinstance(e, AssertionError) else f'ERROR - step 152: {e}')

print("STEP 153 - Check element meta#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "meta")))
    print('PASS - step 153')
except Exception as e:
    print('FAIL - step 153' if isinstance(e, AssertionError) else f'ERROR - step 153: {e}')

print("STEP 154 - Check element meta#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "meta")))
    print('PASS - step 154')
except Exception as e:
    print('FAIL - step 154' if isinstance(e, AssertionError) else f'ERROR - step 154: {e}')

print("STEP 155 - Check element meta#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "meta")))
    print('PASS - step 155')
except Exception as e:
    print('FAIL - step 155' if isinstance(e, AssertionError) else f'ERROR - step 155: {e}')

print("STEP 156 - Check element meta#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "meta")))
    print('PASS - step 156')
except Exception as e:
    print('FAIL - step 156' if isinstance(e, AssertionError) else f'ERROR - step 156: {e}')

print("STEP 157 - Check element meta#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "meta")))
    print('PASS - step 157')
except Exception as e:
    print('FAIL - step 157' if isinstance(e, AssertionError) else f'ERROR - step 157: {e}')

print("STEP 158 - Check element meta#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "meta")))
    print('PASS - step 158')
except Exception as e:
    print('FAIL - step 158' if isinstance(e, AssertionError) else f'ERROR - step 158: {e}')

print("STEP 159 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 159')
except Exception as e:
    print('FAIL - step 159' if isinstance(e, AssertionError) else f'ERROR - step 159: {e}')

print("STEP 160 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 160')
except Exception as e:
    print('FAIL - step 160' if isinstance(e, AssertionError) else f'ERROR - step 160: {e}')

print("STEP 161 - Check element script#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "script")))
    print('PASS - step 161')
except Exception as e:
    print('FAIL - step 161' if isinstance(e, AssertionError) else f'ERROR - step 161: {e}')

print("STEP 162 - Check element meta#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "meta")))
    print('PASS - step 162')
except Exception as e:
    print('FAIL - step 162' if isinstance(e, AssertionError) else f'ERROR - step 162: {e}')

print("STEP 163 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 163')
except Exception as e:
    print('FAIL - step 163' if isinstance(e, AssertionError) else f'ERROR - step 163: {e}')

print("STEP 164 - Check element body#None.['page-home', 'ac-nav-overlap', 'globalnav-scrim', 'globalheader-light', 'ribbon']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['page-home', 'ac-nav-overlap', 'globalnav-scrim', 'globalheader-light', 'ribbon']")))
    print('PASS - step 164')
except Exception as e:
    print('FAIL - step 164' if isinstance(e, AssertionError) else f'ERROR - step 164: {e}')

print("STEP 165 - Check element aside#ac-localeswitcher.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "ac-localeswitcher")))
    print('PASS - step 165')
except Exception as e:
    print('FAIL - step 165' if isinstance(e, AssertionError) else f'ERROR - step 165: {e}')

print("STEP 166 - Check element div#None.['ac-ls-content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-ls-content']")))
    print('PASS - step 166')
except Exception as e:
    print('FAIL - step 166' if isinstance(e, AssertionError) else f'ERROR - step 166: {e}')

print("STEP 167 - Check element div#None.['ac-ls-copy']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-ls-copy']")))
    print('PASS - step 167')
except Exception as e:
    print('FAIL - step 167' if isinstance(e, AssertionError) else f'ERROR - step 167: {e}')

print("STEP 168 - Check element div#None.['ac-ls-actions']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-ls-actions']")))
    print('PASS - step 168')
except Exception as e:
    print('FAIL - step 168' if isinstance(e, AssertionError) else f'ERROR - step 168: {e}')

print("STEP 169 - Check element div#ac-ls-dropdown.['ac-ls-dropdown', 'ac-ls-actions-item', 'select-collapsed']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "ac-ls-dropdown")))
    print('PASS - step 169')
except Exception as e:
    print('FAIL - step 169' if isinstance(e, AssertionError) else f'ERROR - step 169: {e}')

print("STEP 170 - Check element div#ac-ls-dropdown-select.['ac-ls-dropdown-select']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "ac-ls-dropdown-select")))
    print('PASS - step 170')
except Exception as e:
    print('FAIL - step 170' if isinstance(e, AssertionError) else f'ERROR - step 170: {e}')

print("STEP 171 - Check element span#ac-ls-dropdown-title.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "ac-ls-dropdown-title")))
    print('PASS - step 171')
except Exception as e:
    print('FAIL - step 171' if isinstance(e, AssertionError) else f'ERROR - step 171: {e}')

print("STEP 172 - Check element span#None.['ac-ls-dropdown-check']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-ls-dropdown-check']")))
    print('PASS - step 172')
except Exception as e:
    print('FAIL - step 172' if isinstance(e, AssertionError) else f'ERROR - step 172: {e}')

print("STEP 173 - Check element span#None.['ac-ls-dropdown-copy']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-ls-dropdown-copy']")))
    print('PASS - step 173')
except Exception as e:
    print('FAIL - step 173' if isinstance(e, AssertionError) else f'ERROR - step 173: {e}')

print("STEP 174 - Check element div#None.['ac-ls-dropdown-scrim']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-ls-dropdown-scrim']")))
    print('PASS - step 174')
except Exception as e:
    print('FAIL - step 174' if isinstance(e, AssertionError) else f'ERROR - step 174: {e}')

print("STEP 175 - Check element div#ac-ls-dropdown-options.['ac-ls-dropdown-options']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "ac-ls-dropdown-options")))
    print('PASS - step 175')
except Exception as e:
    print('FAIL - step 175' if isinstance(e, AssertionError) else f'ERROR - step 175: {e}')

print("STEP 176 - Check element ul#ac-ls-dropdown-options-list.['ac-ls-dropdown-options-list']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "ac-ls-dropdown-options-list")))
    print('PASS - step 176')
except Exception as e:
    print('FAIL - step 176' if isinstance(e, AssertionError) else f'ERROR - step 176: {e}')

print("STEP 177 - Check element li#ac-ls-dropdown-option-1.['ac-ls-dropdown-option']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "ac-ls-dropdown-option-1")))
    print('PASS - step 177')
except Exception as e:
    print('FAIL - step 177' if isinstance(e, AssertionError) else f'ERROR - step 177: {e}')

print("STEP 178 - Check element span#None.['ac-ls-dropdown-check']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-ls-dropdown-check']")))
    print('PASS - step 178')
except Exception as e:
    print('FAIL - step 178' if isinstance(e, AssertionError) else f'ERROR - step 178: {e}')

print("STEP 179 - Check element span#None.['ac-ls-dropdown-copy']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-ls-dropdown-copy']")))
    print('PASS - step 179')
except Exception as e:
    print('FAIL - step 179' if isinstance(e, AssertionError) else f'ERROR - step 179: {e}')

print("STEP 180 - Check element li#ac-ls-dropdown-option-country-region.['ac-ls-dropdown-option']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "ac-ls-dropdown-option-country-region")))
    print('PASS - step 180')
except Exception as e:
    print('FAIL - step 180' if isinstance(e, AssertionError) else f'ERROR - step 180: {e}')

print("STEP 181 - Check element span#None.['ac-ls-dropdown-check']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-ls-dropdown-check']")))
    print('PASS - step 181')
except Exception as e:
    print('FAIL - step 181' if isinstance(e, AssertionError) else f'ERROR - step 181: {e}')

print("STEP 182 - Check element span#None.['ac-ls-dropdown-copy']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-ls-dropdown-copy']")))
    print('PASS - step 182')
except Exception as e:
    print('FAIL - step 182' if isinstance(e, AssertionError) else f'ERROR - step 182: {e}')

print("STEP 183 - Check element a#ac-ls-continue.['ac-ls-button', 'ac-ls-actions-item', 'ac-ls-continue']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "ac-ls-continue")))
    print('PASS - step 183')
except Exception as e:
    print('FAIL - step 183' if isinstance(e, AssertionError) else f'ERROR - step 183: {e}')

print("STEP 184 - Check element button#ac-ls-close.['ac-ls-close', 'ac-ls-actions-item', 'ac-ls-icon']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "ac-ls-close")))
    print('PASS - step 184')
except Exception as e:
    print('FAIL - step 184' if isinstance(e, AssertionError) else f'ERROR - step 184: {e}')

print("STEP 185 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 185')
except Exception as e:
    print('FAIL - step 185' if isinstance(e, AssertionError) else f'ERROR - step 185: {e}')

print("STEP 186 - Check element polyline#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "polyline")))
    print('PASS - step 186')
except Exception as e:
    print('FAIL - step 186' if isinstance(e, AssertionError) else f'ERROR - step 186: {e}')

print("STEP 187 - Check element polyline#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "polyline")))
    print('PASS - step 187')
except Exception as e:
    print('FAIL - step 187' if isinstance(e, AssertionError) else f'ERROR - step 187: {e}')

print("STEP 188 - Check element h1#None.['visuallyhidden']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['visuallyhidden']")))
    print('PASS - step 188')
except Exception as e:
    print('FAIL - step 188' if isinstance(e, AssertionError) else f'ERROR - step 188: {e}')

print("STEP 189 - Check element meta#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "meta")))
    print('PASS - step 189')
except Exception as e:
    print('FAIL - step 189' if isinstance(e, AssertionError) else f'ERROR - step 189: {e}')

print("STEP 190 - Check element div#globalheader.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "globalheader")))
    print('PASS - step 190')
except Exception as e:
    print('FAIL - step 190' if isinstance(e, AssertionError) else f'ERROR - step 190: {e}')

print("STEP 191 - Check element aside#globalmessage-segment.['globalmessage-segment']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "globalmessage-segment")))
    print('PASS - step 191')
except Exception as e:
    print('FAIL - step 191' if isinstance(e, AssertionError) else f'ERROR - step 191: {e}')

print("STEP 192 - Check element ul#None.['globalmessage-segment-content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalmessage-segment-content']")))
    print('PASS - step 192')
except Exception as e:
    print('FAIL - step 192' if isinstance(e, AssertionError) else f'ERROR - step 192: {e}')

print("STEP 193 - Check element nav#globalnav.['globalnav', 'js']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "globalnav")))
    print('PASS - step 193')
except Exception as e:
    print('FAIL - step 193' if isinstance(e, AssertionError) else f'ERROR - step 193: {e}')

print("STEP 194 - Check element div#None.['globalnav-content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-content']")))
    print('PASS - step 194')
except Exception as e:
    print('FAIL - step 194' if isinstance(e, AssertionError) else f'ERROR - step 194: {e}')

print("STEP 195 - Check element div#None.['globalnav-item', 'globalnav-menuback']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-item', 'globalnav-menuback']")))
    print('PASS - step 195')
except Exception as e:
    print('FAIL - step 195' if isinstance(e, AssertionError) else f'ERROR - step 195: {e}')

print("STEP 196 - Check element button#None.['globalnav-menuback-button']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-menuback-button']")))
    print('PASS - step 196')
except Exception as e:
    print('FAIL - step 196' if isinstance(e, AssertionError) else f'ERROR - step 196: {e}')

print("STEP 197 - Check element span#None.['globalnav-chevron-icon']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-chevron-icon']")))
    print('PASS - step 197')
except Exception as e:
    print('FAIL - step 197' if isinstance(e, AssertionError) else f'ERROR - step 197: {e}')

print("STEP 198 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 198')
except Exception as e:
    print('FAIL - step 198' if isinstance(e, AssertionError) else f'ERROR - step 198: {e}')

print("STEP 199 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 199')
except Exception as e:
    print('FAIL - step 199' if isinstance(e, AssertionError) else f'ERROR - step 199: {e}')

print("STEP 200 - Check element ul#globalnav-list.['globalnav-list']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "globalnav-list")))
    print('PASS - step 200')
except Exception as e:
    print('FAIL - step 200' if isinstance(e, AssertionError) else f'ERROR - step 200: {e}')

print("STEP 201 - Check element li#None.['globalnav-item', 'globalnav-item-apple']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-item', 'globalnav-item-apple']")))
    print('PASS - step 201')
except Exception as e:
    print('FAIL - step 201' if isinstance(e, AssertionError) else f'ERROR - step 201: {e}')

print("STEP 202 - Check element a#None.['globalnav-link', 'globalnav-link-apple']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-link', 'globalnav-link-apple']")))
    print('PASS - step 202')
except Exception as e:
    print('FAIL - step 202' if isinstance(e, AssertionError) else f'ERROR - step 202: {e}')

print("STEP 203 - Check element span#None.['globalnav-image-regular', 'globalnav-link-image']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-image-regular', 'globalnav-link-image']")))
    print('PASS - step 203')
except Exception as e:
    print('FAIL - step 203' if isinstance(e, AssertionError) else f'ERROR - step 203: {e}')

print("STEP 204 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 204')
except Exception as e:
    print('FAIL - step 204' if isinstance(e, AssertionError) else f'ERROR - step 204: {e}')

print("STEP 205 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 205')
except Exception as e:
    print('FAIL - step 205' if isinstance(e, AssertionError) else f'ERROR - step 205: {e}')

print("STEP 206 - Check element span#None.['globalnav-image-compact', 'globalnav-link-image']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-image-compact', 'globalnav-link-image']")))
    print('PASS - step 206')
except Exception as e:
    print('FAIL - step 206' if isinstance(e, AssertionError) else f'ERROR - step 206: {e}')

print("STEP 207 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 207')
except Exception as e:
    print('FAIL - step 207' if isinstance(e, AssertionError) else f'ERROR - step 207: {e}')

print("STEP 208 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 208')
except Exception as e:
    print('FAIL - step 208' if isinstance(e, AssertionError) else f'ERROR - step 208: {e}')

print("STEP 209 - Check element span#None.['globalnav-link-text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-link-text']")))
    print('PASS - step 209')
except Exception as e:
    print('FAIL - step 209' if isinstance(e, AssertionError) else f'ERROR - step 209: {e}')

print("STEP 210 - Check element li#None.['globalnav-item', 'globalnav-menu']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-item', 'globalnav-menu']")))
    print('PASS - step 210')
except Exception as e:
    print('FAIL - step 210' if isinstance(e, AssertionError) else f'ERROR - step 210: {e}')

print("STEP 211 - Check element div#None.['globalnav-flyout']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-flyout']")))
    print('PASS - step 211')
except Exception as e:
    print('FAIL - step 211' if isinstance(e, AssertionError) else f'ERROR - step 211: {e}')

print("STEP 212 - Check element div#None.['globalnav-menu-list']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-menu-list']")))
    print('PASS - step 212')
except Exception as e:
    print('FAIL - step 212' if isinstance(e, AssertionError) else f'ERROR - step 212: {e}')

print("STEP 213 - Check element div#None.['globalnav-item', 'globalnav-item-store', 'globalnav-item-menu', 'globalnav-item-submenu']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-item', 'globalnav-item-store', 'globalnav-item-menu', 'globalnav-item-submenu']")))
    print('PASS - step 213')
except Exception as e:
    print('FAIL - step 213' if isinstance(e, AssertionError) else f'ERROR - step 213: {e}')

print("STEP 214 - Check element ul#None.['globalnav-submenu-trigger-group']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-trigger-group']")))
    print('PASS - step 214')
except Exception as e:
    print('FAIL - step 214' if isinstance(e, AssertionError) else f'ERROR - step 214: {e}')

print("STEP 215 - Check element li#None.['globalnav-submenu-trigger-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-trigger-item']")))
    print('PASS - step 215')
except Exception as e:
    print('FAIL - step 215' if isinstance(e, AssertionError) else f'ERROR - step 215: {e}')

print("STEP 216 - Check element a#None.['globalnav-link', 'globalnav-submenu-trigger-link', 'globalnav-link-store']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-link', 'globalnav-submenu-trigger-link', 'globalnav-link-store']")))
    print('PASS - step 216')
except Exception as e:
    print('FAIL - step 216' if isinstance(e, AssertionError) else f'ERROR - step 216: {e}')

print("STEP 217 - Check element span#None.['globalnav-link-text-container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-link-text-container']")))
    print('PASS - step 217')
except Exception as e:
    print('FAIL - step 217' if isinstance(e, AssertionError) else f'ERROR - step 217: {e}')

print("STEP 218 - Check element span#None.['globalnav-image-regular', 'globalnav-link-image']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-image-regular', 'globalnav-link-image']")))
    print('PASS - step 218')
except Exception as e:
    print('FAIL - step 218' if isinstance(e, AssertionError) else f'ERROR - step 218: {e}')

print("STEP 219 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 219')
except Exception as e:
    print('FAIL - step 219' if isinstance(e, AssertionError) else f'ERROR - step 219: {e}')

print("STEP 220 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 220')
except Exception as e:
    print('FAIL - step 220' if isinstance(e, AssertionError) else f'ERROR - step 220: {e}')

print("STEP 221 - Check element span#None.['globalnav-link-text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-link-text']")))
    print('PASS - step 221')
except Exception as e:
    print('FAIL - step 221' if isinstance(e, AssertionError) else f'ERROR - step 221: {e}')

print("STEP 222 - Check element span#None.['globalnav-link-chevron']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-link-chevron']")))
    print('PASS - step 222')
except Exception as e:
    print('FAIL - step 222' if isinstance(e, AssertionError) else f'ERROR - step 222: {e}')

print("STEP 223 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 223')
except Exception as e:
    print('FAIL - step 223' if isinstance(e, AssertionError) else f'ERROR - step 223: {e}')

print("STEP 224 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 224')
except Exception as e:
    print('FAIL - step 224' if isinstance(e, AssertionError) else f'ERROR - step 224: {e}')

print("STEP 225 - Check element li#None.['globalnav-submenu-trigger-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-trigger-item']")))
    print('PASS - step 225')
except Exception as e:
    print('FAIL - step 225' if isinstance(e, AssertionError) else f'ERROR - step 225: {e}')

print("STEP 226 - Check element button#globalnav-menubutton-link-store.['globalnav-submenu-trigger-button']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "globalnav-menubutton-link-store")))
    print('PASS - step 226')
except Exception as e:
    print('FAIL - step 226' if isinstance(e, AssertionError) else f'ERROR - step 226: {e}')

print("STEP 227 - Check element span#None.['globalnav-image-regular', 'globalnav-submenu-button-icon']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-image-regular', 'globalnav-submenu-button-icon']")))
    print('PASS - step 227')
except Exception as e:
    print('FAIL - step 227' if isinstance(e, AssertionError) else f'ERROR - step 227: {e}')

print("STEP 228 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 228')
except Exception as e:
    print('FAIL - step 228' if isinstance(e, AssertionError) else f'ERROR - step 228: {e}')

print("STEP 229 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 229')
except Exception as e:
    print('FAIL - step 229' if isinstance(e, AssertionError) else f'ERROR - step 229: {e}')

print("STEP 230 - Check element span#None.['globalnav-image-compact', 'globalnav-submenu-button-icon']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-image-compact', 'globalnav-submenu-button-icon']")))
    print('PASS - step 230')
except Exception as e:
    print('FAIL - step 230' if isinstance(e, AssertionError) else f'ERROR - step 230: {e}')

print("STEP 231 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 231')
except Exception as e:
    print('FAIL - step 231' if isinstance(e, AssertionError) else f'ERROR - step 231: {e}')

print("STEP 232 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 232')
except Exception as e:
    print('FAIL - step 232' if isinstance(e, AssertionError) else f'ERROR - step 232: {e}')

print("STEP 233 - Check element div#globalnav-submenu-link-store.['globalnav-flyout', 'globalnav-submenu']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "globalnav-submenu-link-store")))
    print('PASS - step 233')
except Exception as e:
    print('FAIL - step 233' if isinstance(e, AssertionError) else f'ERROR - step 233: {e}')

print("STEP 234 - Check element div#None.['globalnav-flyout-scroll-container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-flyout-scroll-container']")))
    print('PASS - step 234')
except Exception as e:
    print('FAIL - step 234' if isinstance(e, AssertionError) else f'ERROR - step 234: {e}')

print("STEP 235 - Check element div#None.['globalnav-flyout-content', 'globalnav-submenu-content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-flyout-content', 'globalnav-submenu-content']")))
    print('PASS - step 235')
except Exception as e:
    print('FAIL - step 235' if isinstance(e, AssertionError) else f'ERROR - step 235: {e}')

print("STEP 236 - Check element div#None.['globalnav-submenu-group', 'globalnav-submenu-group-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-group', 'globalnav-submenu-group-elevated']")))
    print('PASS - step 236')
except Exception as e:
    print('FAIL - step 236' if isinstance(e, AssertionError) else f'ERROR - step 236: {e}')

print("STEP 237 - Check element h2#c64e0a00.['globalnav-submenu-header']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "c64e0a00")))
    print('PASS - step 237')
except Exception as e:
    print('FAIL - step 237' if isinstance(e, AssertionError) else f'ERROR - step 237: {e}')

print("STEP 238 - Check element ul#None.['globalnav-submenu-list']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list']")))
    print('PASS - step 238')
except Exception as e:
    print('FAIL - step 238' if isinstance(e, AssertionError) else f'ERROR - step 238: {e}')

print("STEP 239 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 239')
except Exception as e:
    print('FAIL - step 239' if isinstance(e, AssertionError) else f'ERROR - step 239: {e}')

print("STEP 240 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 240')
except Exception as e:
    print('FAIL - step 240' if isinstance(e, AssertionError) else f'ERROR - step 240: {e}')

print("STEP 241 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 241')
except Exception as e:
    print('FAIL - step 241' if isinstance(e, AssertionError) else f'ERROR - step 241: {e}')

print("STEP 242 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 242')
except Exception as e:
    print('FAIL - step 242' if isinstance(e, AssertionError) else f'ERROR - step 242: {e}')

print("STEP 243 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 243')
except Exception as e:
    print('FAIL - step 243' if isinstance(e, AssertionError) else f'ERROR - step 243: {e}')

print("STEP 244 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 244')
except Exception as e:
    print('FAIL - step 244' if isinstance(e, AssertionError) else f'ERROR - step 244: {e}')

print("STEP 245 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 245')
except Exception as e:
    print('FAIL - step 245' if isinstance(e, AssertionError) else f'ERROR - step 245: {e}')

print("STEP 246 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 246')
except Exception as e:
    print('FAIL - step 246' if isinstance(e, AssertionError) else f'ERROR - step 246: {e}')

print("STEP 247 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 247')
except Exception as e:
    print('FAIL - step 247' if isinstance(e, AssertionError) else f'ERROR - step 247: {e}')

print("STEP 248 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 248')
except Exception as e:
    print('FAIL - step 248' if isinstance(e, AssertionError) else f'ERROR - step 248: {e}')

print("STEP 249 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 249')
except Exception as e:
    print('FAIL - step 249' if isinstance(e, AssertionError) else f'ERROR - step 249: {e}')

print("STEP 250 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 250')
except Exception as e:
    print('FAIL - step 250' if isinstance(e, AssertionError) else f'ERROR - step 250: {e}')

print("STEP 251 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 251')
except Exception as e:
    print('FAIL - step 251' if isinstance(e, AssertionError) else f'ERROR - step 251: {e}')

print("STEP 252 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 252')
except Exception as e:
    print('FAIL - step 252' if isinstance(e, AssertionError) else f'ERROR - step 252: {e}')

print("STEP 253 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 253')
except Exception as e:
    print('FAIL - step 253' if isinstance(e, AssertionError) else f'ERROR - step 253: {e}')

print("STEP 254 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 254')
except Exception as e:
    print('FAIL - step 254' if isinstance(e, AssertionError) else f'ERROR - step 254: {e}')

print("STEP 255 - Check element div#None.['globalnav-submenu-group']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-group']")))
    print('PASS - step 255')
except Exception as e:
    print('FAIL - step 255' if isinstance(e, AssertionError) else f'ERROR - step 255: {e}')

print("STEP 256 - Check element h2#b80e39ed.['globalnav-submenu-header']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "b80e39ed")))
    print('PASS - step 256')
except Exception as e:
    print('FAIL - step 256' if isinstance(e, AssertionError) else f'ERROR - step 256: {e}')

print("STEP 257 - Check element ul#None.['globalnav-submenu-list']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list']")))
    print('PASS - step 257')
except Exception as e:
    print('FAIL - step 257' if isinstance(e, AssertionError) else f'ERROR - step 257: {e}')

print("STEP 258 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 258')
except Exception as e:
    print('FAIL - step 258' if isinstance(e, AssertionError) else f'ERROR - step 258: {e}')

print("STEP 259 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 259')
except Exception as e:
    print('FAIL - step 259' if isinstance(e, AssertionError) else f'ERROR - step 259: {e}')

print("STEP 260 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 260')
except Exception as e:
    print('FAIL - step 260' if isinstance(e, AssertionError) else f'ERROR - step 260: {e}')

print("STEP 261 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 261')
except Exception as e:
    print('FAIL - step 261' if isinstance(e, AssertionError) else f'ERROR - step 261: {e}')

print("STEP 262 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 262')
except Exception as e:
    print('FAIL - step 262' if isinstance(e, AssertionError) else f'ERROR - step 262: {e}')

print("STEP 263 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 263')
except Exception as e:
    print('FAIL - step 263' if isinstance(e, AssertionError) else f'ERROR - step 263: {e}')

print("STEP 264 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 264')
except Exception as e:
    print('FAIL - step 264' if isinstance(e, AssertionError) else f'ERROR - step 264: {e}')

print("STEP 265 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 265')
except Exception as e:
    print('FAIL - step 265' if isinstance(e, AssertionError) else f'ERROR - step 265: {e}')

print("STEP 266 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 266')
except Exception as e:
    print('FAIL - step 266' if isinstance(e, AssertionError) else f'ERROR - step 266: {e}')

print("STEP 267 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 267')
except Exception as e:
    print('FAIL - step 267' if isinstance(e, AssertionError) else f'ERROR - step 267: {e}')

print("STEP 268 - Check element div#None.['globalnav-submenu-group']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-group']")))
    print('PASS - step 268')
except Exception as e:
    print('FAIL - step 268' if isinstance(e, AssertionError) else f'ERROR - step 268: {e}')

print("STEP 269 - Check element h2#68805228.['globalnav-submenu-header']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "68805228")))
    print('PASS - step 269')
except Exception as e:
    print('FAIL - step 269' if isinstance(e, AssertionError) else f'ERROR - step 269: {e}')

print("STEP 270 - Check element ul#None.['globalnav-submenu-list']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list']")))
    print('PASS - step 270')
except Exception as e:
    print('FAIL - step 270' if isinstance(e, AssertionError) else f'ERROR - step 270: {e}')

print("STEP 271 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 271')
except Exception as e:
    print('FAIL - step 271' if isinstance(e, AssertionError) else f'ERROR - step 271: {e}')

print("STEP 272 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 272')
except Exception as e:
    print('FAIL - step 272' if isinstance(e, AssertionError) else f'ERROR - step 272: {e}')

print("STEP 273 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 273')
except Exception as e:
    print('FAIL - step 273' if isinstance(e, AssertionError) else f'ERROR - step 273: {e}')

print("STEP 274 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 274')
except Exception as e:
    print('FAIL - step 274' if isinstance(e, AssertionError) else f'ERROR - step 274: {e}')

print("STEP 275 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 275')
except Exception as e:
    print('FAIL - step 275' if isinstance(e, AssertionError) else f'ERROR - step 275: {e}')

print("STEP 276 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 276')
except Exception as e:
    print('FAIL - step 276' if isinstance(e, AssertionError) else f'ERROR - step 276: {e}')

print("STEP 277 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 277')
except Exception as e:
    print('FAIL - step 277' if isinstance(e, AssertionError) else f'ERROR - step 277: {e}')

print("STEP 278 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 278')
except Exception as e:
    print('FAIL - step 278' if isinstance(e, AssertionError) else f'ERROR - step 278: {e}')

print("STEP 279 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 279')
except Exception as e:
    print('FAIL - step 279' if isinstance(e, AssertionError) else f'ERROR - step 279: {e}')

print("STEP 280 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 280')
except Exception as e:
    print('FAIL - step 280' if isinstance(e, AssertionError) else f'ERROR - step 280: {e}')

print("STEP 281 - Check element div#None.['globalnav-item', 'globalnav-item-mac', 'globalnav-item-menu', 'globalnav-item-submenu']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-item', 'globalnav-item-mac', 'globalnav-item-menu', 'globalnav-item-submenu']")))
    print('PASS - step 281')
except Exception as e:
    print('FAIL - step 281' if isinstance(e, AssertionError) else f'ERROR - step 281: {e}')

print("STEP 282 - Check element ul#None.['globalnav-submenu-trigger-group']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-trigger-group']")))
    print('PASS - step 282')
except Exception as e:
    print('FAIL - step 282' if isinstance(e, AssertionError) else f'ERROR - step 282: {e}')

print("STEP 283 - Check element li#None.['globalnav-submenu-trigger-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-trigger-item']")))
    print('PASS - step 283')
except Exception as e:
    print('FAIL - step 283' if isinstance(e, AssertionError) else f'ERROR - step 283: {e}')

print("STEP 284 - Check element a#None.['globalnav-link', 'globalnav-submenu-trigger-link', 'globalnav-link-mac']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-link', 'globalnav-submenu-trigger-link', 'globalnav-link-mac']")))
    print('PASS - step 284')
except Exception as e:
    print('FAIL - step 284' if isinstance(e, AssertionError) else f'ERROR - step 284: {e}')

print("STEP 285 - Check element span#None.['globalnav-link-text-container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-link-text-container']")))
    print('PASS - step 285')
except Exception as e:
    print('FAIL - step 285' if isinstance(e, AssertionError) else f'ERROR - step 285: {e}')

print("STEP 286 - Check element span#None.['globalnav-image-regular', 'globalnav-link-image']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-image-regular', 'globalnav-link-image']")))
    print('PASS - step 286')
except Exception as e:
    print('FAIL - step 286' if isinstance(e, AssertionError) else f'ERROR - step 286: {e}')

print("STEP 287 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 287')
except Exception as e:
    print('FAIL - step 287' if isinstance(e, AssertionError) else f'ERROR - step 287: {e}')

print("STEP 288 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 288')
except Exception as e:
    print('FAIL - step 288' if isinstance(e, AssertionError) else f'ERROR - step 288: {e}')

print("STEP 289 - Check element span#None.['globalnav-link-text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-link-text']")))
    print('PASS - step 289')
except Exception as e:
    print('FAIL - step 289' if isinstance(e, AssertionError) else f'ERROR - step 289: {e}')

print("STEP 290 - Check element span#None.['globalnav-link-chevron']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-link-chevron']")))
    print('PASS - step 290')
except Exception as e:
    print('FAIL - step 290' if isinstance(e, AssertionError) else f'ERROR - step 290: {e}')

print("STEP 291 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 291')
except Exception as e:
    print('FAIL - step 291' if isinstance(e, AssertionError) else f'ERROR - step 291: {e}')

print("STEP 292 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 292')
except Exception as e:
    print('FAIL - step 292' if isinstance(e, AssertionError) else f'ERROR - step 292: {e}')

print("STEP 293 - Check element li#None.['globalnav-submenu-trigger-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-trigger-item']")))
    print('PASS - step 293')
except Exception as e:
    print('FAIL - step 293' if isinstance(e, AssertionError) else f'ERROR - step 293: {e}')

print("STEP 294 - Check element button#globalnav-menubutton-link-mac.['globalnav-submenu-trigger-button']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "globalnav-menubutton-link-mac")))
    print('PASS - step 294')
except Exception as e:
    print('FAIL - step 294' if isinstance(e, AssertionError) else f'ERROR - step 294: {e}')

print("STEP 295 - Check element span#None.['globalnav-image-regular', 'globalnav-submenu-button-icon']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-image-regular', 'globalnav-submenu-button-icon']")))
    print('PASS - step 295')
except Exception as e:
    print('FAIL - step 295' if isinstance(e, AssertionError) else f'ERROR - step 295: {e}')

print("STEP 296 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 296')
except Exception as e:
    print('FAIL - step 296' if isinstance(e, AssertionError) else f'ERROR - step 296: {e}')

print("STEP 297 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 297')
except Exception as e:
    print('FAIL - step 297' if isinstance(e, AssertionError) else f'ERROR - step 297: {e}')

print("STEP 298 - Check element span#None.['globalnav-image-compact', 'globalnav-submenu-button-icon']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-image-compact', 'globalnav-submenu-button-icon']")))
    print('PASS - step 298')
except Exception as e:
    print('FAIL - step 298' if isinstance(e, AssertionError) else f'ERROR - step 298: {e}')

print("STEP 299 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 299')
except Exception as e:
    print('FAIL - step 299' if isinstance(e, AssertionError) else f'ERROR - step 299: {e}')

print("STEP 300 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 300')
except Exception as e:
    print('FAIL - step 300' if isinstance(e, AssertionError) else f'ERROR - step 300: {e}')

print("STEP 301 - Check element div#globalnav-submenu-link-mac.['globalnav-flyout', 'globalnav-submenu']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "globalnav-submenu-link-mac")))
    print('PASS - step 301')
except Exception as e:
    print('FAIL - step 301' if isinstance(e, AssertionError) else f'ERROR - step 301: {e}')

print("STEP 302 - Check element div#None.['globalnav-flyout-scroll-container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-flyout-scroll-container']")))
    print('PASS - step 302')
except Exception as e:
    print('FAIL - step 302' if isinstance(e, AssertionError) else f'ERROR - step 302: {e}')

print("STEP 303 - Check element div#None.['globalnav-flyout-content', 'globalnav-submenu-content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-flyout-content', 'globalnav-submenu-content']")))
    print('PASS - step 303')
except Exception as e:
    print('FAIL - step 303' if isinstance(e, AssertionError) else f'ERROR - step 303: {e}')

print("STEP 304 - Check element div#None.['globalnav-submenu-group', 'globalnav-submenu-group-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-group', 'globalnav-submenu-group-elevated']")))
    print('PASS - step 304')
except Exception as e:
    print('FAIL - step 304' if isinstance(e, AssertionError) else f'ERROR - step 304: {e}')

print("STEP 305 - Check element h2#3ded287d.['globalnav-submenu-header']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "3ded287d")))
    print('PASS - step 305')
except Exception as e:
    print('FAIL - step 305' if isinstance(e, AssertionError) else f'ERROR - step 305: {e}')

print("STEP 306 - Check element ul#None.['globalnav-submenu-list']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list']")))
    print('PASS - step 306')
except Exception as e:
    print('FAIL - step 306' if isinstance(e, AssertionError) else f'ERROR - step 306: {e}')

print("STEP 307 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 307')
except Exception as e:
    print('FAIL - step 307' if isinstance(e, AssertionError) else f'ERROR - step 307: {e}')

print("STEP 308 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 308')
except Exception as e:
    print('FAIL - step 308' if isinstance(e, AssertionError) else f'ERROR - step 308: {e}')

print("STEP 309 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 309')
except Exception as e:
    print('FAIL - step 309' if isinstance(e, AssertionError) else f'ERROR - step 309: {e}')

print("STEP 310 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 310')
except Exception as e:
    print('FAIL - step 310' if isinstance(e, AssertionError) else f'ERROR - step 310: {e}')

print("STEP 311 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 311')
except Exception as e:
    print('FAIL - step 311' if isinstance(e, AssertionError) else f'ERROR - step 311: {e}')

print("STEP 312 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 312')
except Exception as e:
    print('FAIL - step 312' if isinstance(e, AssertionError) else f'ERROR - step 312: {e}')

print("STEP 313 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 313')
except Exception as e:
    print('FAIL - step 313' if isinstance(e, AssertionError) else f'ERROR - step 313: {e}')

print("STEP 314 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 314')
except Exception as e:
    print('FAIL - step 314' if isinstance(e, AssertionError) else f'ERROR - step 314: {e}')

print("STEP 315 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 315')
except Exception as e:
    print('FAIL - step 315' if isinstance(e, AssertionError) else f'ERROR - step 315: {e}')

print("STEP 316 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 316')
except Exception as e:
    print('FAIL - step 316' if isinstance(e, AssertionError) else f'ERROR - step 316: {e}')

print("STEP 317 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 317')
except Exception as e:
    print('FAIL - step 317' if isinstance(e, AssertionError) else f'ERROR - step 317: {e}')

print("STEP 318 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 318')
except Exception as e:
    print('FAIL - step 318' if isinstance(e, AssertionError) else f'ERROR - step 318: {e}')

print("STEP 319 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 319')
except Exception as e:
    print('FAIL - step 319' if isinstance(e, AssertionError) else f'ERROR - step 319: {e}')

print("STEP 320 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 320')
except Exception as e:
    print('FAIL - step 320' if isinstance(e, AssertionError) else f'ERROR - step 320: {e}')

print("STEP 321 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 321')
except Exception as e:
    print('FAIL - step 321' if isinstance(e, AssertionError) else f'ERROR - step 321: {e}')

print("STEP 322 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 322')
except Exception as e:
    print('FAIL - step 322' if isinstance(e, AssertionError) else f'ERROR - step 322: {e}')

print("STEP 323 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 323')
except Exception as e:
    print('FAIL - step 323' if isinstance(e, AssertionError) else f'ERROR - step 323: {e}')

print("STEP 324 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 324')
except Exception as e:
    print('FAIL - step 324' if isinstance(e, AssertionError) else f'ERROR - step 324: {e}')

print("STEP 325 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 325')
except Exception as e:
    print('FAIL - step 325' if isinstance(e, AssertionError) else f'ERROR - step 325: {e}')

print("STEP 326 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 326')
except Exception as e:
    print('FAIL - step 326' if isinstance(e, AssertionError) else f'ERROR - step 326: {e}')

print("STEP 327 - Check element div#None.['globalnav-submenu-group']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-group']")))
    print('PASS - step 327')
except Exception as e:
    print('FAIL - step 327' if isinstance(e, AssertionError) else f'ERROR - step 327: {e}')

print("STEP 328 - Check element h2#cd6bb5ab.['globalnav-submenu-header']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "cd6bb5ab")))
    print('PASS - step 328')
except Exception as e:
    print('FAIL - step 328' if isinstance(e, AssertionError) else f'ERROR - step 328: {e}')

print("STEP 329 - Check element ul#None.['globalnav-submenu-list']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list']")))
    print('PASS - step 329')
except Exception as e:
    print('FAIL - step 329' if isinstance(e, AssertionError) else f'ERROR - step 329: {e}')

print("STEP 330 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 330')
except Exception as e:
    print('FAIL - step 330' if isinstance(e, AssertionError) else f'ERROR - step 330: {e}')

print("STEP 331 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 331')
except Exception as e:
    print('FAIL - step 331' if isinstance(e, AssertionError) else f'ERROR - step 331: {e}')

print("STEP 332 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 332')
except Exception as e:
    print('FAIL - step 332' if isinstance(e, AssertionError) else f'ERROR - step 332: {e}')

print("STEP 333 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 333')
except Exception as e:
    print('FAIL - step 333' if isinstance(e, AssertionError) else f'ERROR - step 333: {e}')

print("STEP 334 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 334')
except Exception as e:
    print('FAIL - step 334' if isinstance(e, AssertionError) else f'ERROR - step 334: {e}')

print("STEP 335 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 335')
except Exception as e:
    print('FAIL - step 335' if isinstance(e, AssertionError) else f'ERROR - step 335: {e}')

print("STEP 336 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 336')
except Exception as e:
    print('FAIL - step 336' if isinstance(e, AssertionError) else f'ERROR - step 336: {e}')

print("STEP 337 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 337')
except Exception as e:
    print('FAIL - step 337' if isinstance(e, AssertionError) else f'ERROR - step 337: {e}')

print("STEP 338 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 338')
except Exception as e:
    print('FAIL - step 338' if isinstance(e, AssertionError) else f'ERROR - step 338: {e}')

print("STEP 339 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 339')
except Exception as e:
    print('FAIL - step 339' if isinstance(e, AssertionError) else f'ERROR - step 339: {e}')

print("STEP 340 - Check element div#None.['globalnav-submenu-group']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-group']")))
    print('PASS - step 340')
except Exception as e:
    print('FAIL - step 340' if isinstance(e, AssertionError) else f'ERROR - step 340: {e}')

print("STEP 341 - Check element h2#4632b2ae.['globalnav-submenu-header']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "4632b2ae")))
    print('PASS - step 341')
except Exception as e:
    print('FAIL - step 341' if isinstance(e, AssertionError) else f'ERROR - step 341: {e}')

print("STEP 342 - Check element ul#None.['globalnav-submenu-list']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list']")))
    print('PASS - step 342')
except Exception as e:
    print('FAIL - step 342' if isinstance(e, AssertionError) else f'ERROR - step 342: {e}')

print("STEP 343 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 343')
except Exception as e:
    print('FAIL - step 343' if isinstance(e, AssertionError) else f'ERROR - step 343: {e}')

print("STEP 344 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 344')
except Exception as e:
    print('FAIL - step 344' if isinstance(e, AssertionError) else f'ERROR - step 344: {e}')

print("STEP 345 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 345')
except Exception as e:
    print('FAIL - step 345' if isinstance(e, AssertionError) else f'ERROR - step 345: {e}')

print("STEP 346 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 346')
except Exception as e:
    print('FAIL - step 346' if isinstance(e, AssertionError) else f'ERROR - step 346: {e}')

print("STEP 347 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 347')
except Exception as e:
    print('FAIL - step 347' if isinstance(e, AssertionError) else f'ERROR - step 347: {e}')

print("STEP 348 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 348')
except Exception as e:
    print('FAIL - step 348' if isinstance(e, AssertionError) else f'ERROR - step 348: {e}')

print("STEP 349 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 349')
except Exception as e:
    print('FAIL - step 349' if isinstance(e, AssertionError) else f'ERROR - step 349: {e}')

print("STEP 350 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 350')
except Exception as e:
    print('FAIL - step 350' if isinstance(e, AssertionError) else f'ERROR - step 350: {e}')

print("STEP 351 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 351')
except Exception as e:
    print('FAIL - step 351' if isinstance(e, AssertionError) else f'ERROR - step 351: {e}')

print("STEP 352 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 352')
except Exception as e:
    print('FAIL - step 352' if isinstance(e, AssertionError) else f'ERROR - step 352: {e}')

print("STEP 353 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 353')
except Exception as e:
    print('FAIL - step 353' if isinstance(e, AssertionError) else f'ERROR - step 353: {e}')

print("STEP 354 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 354')
except Exception as e:
    print('FAIL - step 354' if isinstance(e, AssertionError) else f'ERROR - step 354: {e}')

print("STEP 355 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 355')
except Exception as e:
    print('FAIL - step 355' if isinstance(e, AssertionError) else f'ERROR - step 355: {e}')

print("STEP 356 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 356')
except Exception as e:
    print('FAIL - step 356' if isinstance(e, AssertionError) else f'ERROR - step 356: {e}')

print("STEP 357 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 357')
except Exception as e:
    print('FAIL - step 357' if isinstance(e, AssertionError) else f'ERROR - step 357: {e}')

print("STEP 358 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 358')
except Exception as e:
    print('FAIL - step 358' if isinstance(e, AssertionError) else f'ERROR - step 358: {e}')

print("STEP 359 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 359')
except Exception as e:
    print('FAIL - step 359' if isinstance(e, AssertionError) else f'ERROR - step 359: {e}')

print("STEP 360 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 360')
except Exception as e:
    print('FAIL - step 360' if isinstance(e, AssertionError) else f'ERROR - step 360: {e}')

print("STEP 361 - Check element div#None.['globalnav-item', 'globalnav-item-ipad', 'globalnav-item-menu', 'globalnav-item-submenu']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-item', 'globalnav-item-ipad', 'globalnav-item-menu', 'globalnav-item-submenu']")))
    print('PASS - step 361')
except Exception as e:
    print('FAIL - step 361' if isinstance(e, AssertionError) else f'ERROR - step 361: {e}')

print("STEP 362 - Check element ul#None.['globalnav-submenu-trigger-group']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-trigger-group']")))
    print('PASS - step 362')
except Exception as e:
    print('FAIL - step 362' if isinstance(e, AssertionError) else f'ERROR - step 362: {e}')

print("STEP 363 - Check element li#None.['globalnav-submenu-trigger-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-trigger-item']")))
    print('PASS - step 363')
except Exception as e:
    print('FAIL - step 363' if isinstance(e, AssertionError) else f'ERROR - step 363: {e}')

print("STEP 364 - Check element a#None.['globalnav-link', 'globalnav-submenu-trigger-link', 'globalnav-link-ipad']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-link', 'globalnav-submenu-trigger-link', 'globalnav-link-ipad']")))
    print('PASS - step 364')
except Exception as e:
    print('FAIL - step 364' if isinstance(e, AssertionError) else f'ERROR - step 364: {e}')

print("STEP 365 - Check element span#None.['globalnav-link-text-container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-link-text-container']")))
    print('PASS - step 365')
except Exception as e:
    print('FAIL - step 365' if isinstance(e, AssertionError) else f'ERROR - step 365: {e}')

print("STEP 366 - Check element span#None.['globalnav-image-regular', 'globalnav-link-image']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-image-regular', 'globalnav-link-image']")))
    print('PASS - step 366')
except Exception as e:
    print('FAIL - step 366' if isinstance(e, AssertionError) else f'ERROR - step 366: {e}')

print("STEP 367 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 367')
except Exception as e:
    print('FAIL - step 367' if isinstance(e, AssertionError) else f'ERROR - step 367: {e}')

print("STEP 368 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 368')
except Exception as e:
    print('FAIL - step 368' if isinstance(e, AssertionError) else f'ERROR - step 368: {e}')

print("STEP 369 - Check element span#None.['globalnav-link-text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-link-text']")))
    print('PASS - step 369')
except Exception as e:
    print('FAIL - step 369' if isinstance(e, AssertionError) else f'ERROR - step 369: {e}')

print("STEP 370 - Check element span#None.['globalnav-link-chevron']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-link-chevron']")))
    print('PASS - step 370')
except Exception as e:
    print('FAIL - step 370' if isinstance(e, AssertionError) else f'ERROR - step 370: {e}')

print("STEP 371 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 371')
except Exception as e:
    print('FAIL - step 371' if isinstance(e, AssertionError) else f'ERROR - step 371: {e}')

print("STEP 372 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 372')
except Exception as e:
    print('FAIL - step 372' if isinstance(e, AssertionError) else f'ERROR - step 372: {e}')

print("STEP 373 - Check element li#None.['globalnav-submenu-trigger-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-trigger-item']")))
    print('PASS - step 373')
except Exception as e:
    print('FAIL - step 373' if isinstance(e, AssertionError) else f'ERROR - step 373: {e}')

print("STEP 374 - Check element button#globalnav-menubutton-link-ipad.['globalnav-submenu-trigger-button']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "globalnav-menubutton-link-ipad")))
    print('PASS - step 374')
except Exception as e:
    print('FAIL - step 374' if isinstance(e, AssertionError) else f'ERROR - step 374: {e}')

print("STEP 375 - Check element span#None.['globalnav-image-regular', 'globalnav-submenu-button-icon']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-image-regular', 'globalnav-submenu-button-icon']")))
    print('PASS - step 375')
except Exception as e:
    print('FAIL - step 375' if isinstance(e, AssertionError) else f'ERROR - step 375: {e}')

print("STEP 376 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 376')
except Exception as e:
    print('FAIL - step 376' if isinstance(e, AssertionError) else f'ERROR - step 376: {e}')

print("STEP 377 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 377')
except Exception as e:
    print('FAIL - step 377' if isinstance(e, AssertionError) else f'ERROR - step 377: {e}')

print("STEP 378 - Check element span#None.['globalnav-image-compact', 'globalnav-submenu-button-icon']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-image-compact', 'globalnav-submenu-button-icon']")))
    print('PASS - step 378')
except Exception as e:
    print('FAIL - step 378' if isinstance(e, AssertionError) else f'ERROR - step 378: {e}')

print("STEP 379 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 379')
except Exception as e:
    print('FAIL - step 379' if isinstance(e, AssertionError) else f'ERROR - step 379: {e}')

print("STEP 380 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 380')
except Exception as e:
    print('FAIL - step 380' if isinstance(e, AssertionError) else f'ERROR - step 380: {e}')

print("STEP 381 - Check element div#globalnav-submenu-link-ipad.['globalnav-flyout', 'globalnav-submenu']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "globalnav-submenu-link-ipad")))
    print('PASS - step 381')
except Exception as e:
    print('FAIL - step 381' if isinstance(e, AssertionError) else f'ERROR - step 381: {e}')

print("STEP 382 - Check element div#None.['globalnav-flyout-scroll-container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-flyout-scroll-container']")))
    print('PASS - step 382')
except Exception as e:
    print('FAIL - step 382' if isinstance(e, AssertionError) else f'ERROR - step 382: {e}')

print("STEP 383 - Check element div#None.['globalnav-flyout-content', 'globalnav-submenu-content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-flyout-content', 'globalnav-submenu-content']")))
    print('PASS - step 383')
except Exception as e:
    print('FAIL - step 383' if isinstance(e, AssertionError) else f'ERROR - step 383: {e}')

print("STEP 384 - Check element div#None.['globalnav-submenu-group', 'globalnav-submenu-group-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-group', 'globalnav-submenu-group-elevated']")))
    print('PASS - step 384')
except Exception as e:
    print('FAIL - step 384' if isinstance(e, AssertionError) else f'ERROR - step 384: {e}')

print("STEP 385 - Check element h2#3aedc891.['globalnav-submenu-header']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "3aedc891")))
    print('PASS - step 385')
except Exception as e:
    print('FAIL - step 385' if isinstance(e, AssertionError) else f'ERROR - step 385: {e}')

print("STEP 386 - Check element ul#None.['globalnav-submenu-list']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list']")))
    print('PASS - step 386')
except Exception as e:
    print('FAIL - step 386' if isinstance(e, AssertionError) else f'ERROR - step 386: {e}')

print("STEP 387 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 387')
except Exception as e:
    print('FAIL - step 387' if isinstance(e, AssertionError) else f'ERROR - step 387: {e}')

print("STEP 388 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 388')
except Exception as e:
    print('FAIL - step 388' if isinstance(e, AssertionError) else f'ERROR - step 388: {e}')

print("STEP 389 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 389')
except Exception as e:
    print('FAIL - step 389' if isinstance(e, AssertionError) else f'ERROR - step 389: {e}')

print("STEP 390 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 390')
except Exception as e:
    print('FAIL - step 390' if isinstance(e, AssertionError) else f'ERROR - step 390: {e}')

print("STEP 391 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 391')
except Exception as e:
    print('FAIL - step 391' if isinstance(e, AssertionError) else f'ERROR - step 391: {e}')

print("STEP 392 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 392')
except Exception as e:
    print('FAIL - step 392' if isinstance(e, AssertionError) else f'ERROR - step 392: {e}')

print("STEP 393 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 393')
except Exception as e:
    print('FAIL - step 393' if isinstance(e, AssertionError) else f'ERROR - step 393: {e}')

print("STEP 394 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 394')
except Exception as e:
    print('FAIL - step 394' if isinstance(e, AssertionError) else f'ERROR - step 394: {e}')

print("STEP 395 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 395')
except Exception as e:
    print('FAIL - step 395' if isinstance(e, AssertionError) else f'ERROR - step 395: {e}')

print("STEP 396 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 396')
except Exception as e:
    print('FAIL - step 396' if isinstance(e, AssertionError) else f'ERROR - step 396: {e}')

print("STEP 397 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 397')
except Exception as e:
    print('FAIL - step 397' if isinstance(e, AssertionError) else f'ERROR - step 397: {e}')

print("STEP 398 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 398')
except Exception as e:
    print('FAIL - step 398' if isinstance(e, AssertionError) else f'ERROR - step 398: {e}')

print("STEP 399 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 399')
except Exception as e:
    print('FAIL - step 399' if isinstance(e, AssertionError) else f'ERROR - step 399: {e}')

print("STEP 400 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 400')
except Exception as e:
    print('FAIL - step 400' if isinstance(e, AssertionError) else f'ERROR - step 400: {e}')

print("STEP 401 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 401')
except Exception as e:
    print('FAIL - step 401' if isinstance(e, AssertionError) else f'ERROR - step 401: {e}')

print("STEP 402 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 402')
except Exception as e:
    print('FAIL - step 402' if isinstance(e, AssertionError) else f'ERROR - step 402: {e}')

print("STEP 403 - Check element div#None.['globalnav-submenu-group']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-group']")))
    print('PASS - step 403')
except Exception as e:
    print('FAIL - step 403' if isinstance(e, AssertionError) else f'ERROR - step 403: {e}')

print("STEP 404 - Check element h2#62fe7d95.['globalnav-submenu-header']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "62fe7d95")))
    print('PASS - step 404')
except Exception as e:
    print('FAIL - step 404' if isinstance(e, AssertionError) else f'ERROR - step 404: {e}')

print("STEP 405 - Check element ul#None.['globalnav-submenu-list']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list']")))
    print('PASS - step 405')
except Exception as e:
    print('FAIL - step 405' if isinstance(e, AssertionError) else f'ERROR - step 405: {e}')

print("STEP 406 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 406')
except Exception as e:
    print('FAIL - step 406' if isinstance(e, AssertionError) else f'ERROR - step 406: {e}')

print("STEP 407 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 407')
except Exception as e:
    print('FAIL - step 407' if isinstance(e, AssertionError) else f'ERROR - step 407: {e}')

print("STEP 408 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 408')
except Exception as e:
    print('FAIL - step 408' if isinstance(e, AssertionError) else f'ERROR - step 408: {e}')

print("STEP 409 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 409')
except Exception as e:
    print('FAIL - step 409' if isinstance(e, AssertionError) else f'ERROR - step 409: {e}')

print("STEP 410 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 410')
except Exception as e:
    print('FAIL - step 410' if isinstance(e, AssertionError) else f'ERROR - step 410: {e}')

print("STEP 411 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 411')
except Exception as e:
    print('FAIL - step 411' if isinstance(e, AssertionError) else f'ERROR - step 411: {e}')

print("STEP 412 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 412')
except Exception as e:
    print('FAIL - step 412' if isinstance(e, AssertionError) else f'ERROR - step 412: {e}')

print("STEP 413 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 413')
except Exception as e:
    print('FAIL - step 413' if isinstance(e, AssertionError) else f'ERROR - step 413: {e}')

print("STEP 414 - Check element div#None.['globalnav-submenu-group']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-group']")))
    print('PASS - step 414')
except Exception as e:
    print('FAIL - step 414' if isinstance(e, AssertionError) else f'ERROR - step 414: {e}')

print("STEP 415 - Check element h2#be565b03.['globalnav-submenu-header']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "be565b03")))
    print('PASS - step 415')
except Exception as e:
    print('FAIL - step 415' if isinstance(e, AssertionError) else f'ERROR - step 415: {e}')

print("STEP 416 - Check element ul#None.['globalnav-submenu-list']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list']")))
    print('PASS - step 416')
except Exception as e:
    print('FAIL - step 416' if isinstance(e, AssertionError) else f'ERROR - step 416: {e}')

print("STEP 417 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 417')
except Exception as e:
    print('FAIL - step 417' if isinstance(e, AssertionError) else f'ERROR - step 417: {e}')

print("STEP 418 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 418')
except Exception as e:
    print('FAIL - step 418' if isinstance(e, AssertionError) else f'ERROR - step 418: {e}')

print("STEP 419 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 419')
except Exception as e:
    print('FAIL - step 419' if isinstance(e, AssertionError) else f'ERROR - step 419: {e}')

print("STEP 420 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 420')
except Exception as e:
    print('FAIL - step 420' if isinstance(e, AssertionError) else f'ERROR - step 420: {e}')

print("STEP 421 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 421')
except Exception as e:
    print('FAIL - step 421' if isinstance(e, AssertionError) else f'ERROR - step 421: {e}')

print("STEP 422 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 422')
except Exception as e:
    print('FAIL - step 422' if isinstance(e, AssertionError) else f'ERROR - step 422: {e}')

print("STEP 423 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 423')
except Exception as e:
    print('FAIL - step 423' if isinstance(e, AssertionError) else f'ERROR - step 423: {e}')

print("STEP 424 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 424')
except Exception as e:
    print('FAIL - step 424' if isinstance(e, AssertionError) else f'ERROR - step 424: {e}')

print("STEP 425 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 425')
except Exception as e:
    print('FAIL - step 425' if isinstance(e, AssertionError) else f'ERROR - step 425: {e}')

print("STEP 426 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 426')
except Exception as e:
    print('FAIL - step 426' if isinstance(e, AssertionError) else f'ERROR - step 426: {e}')

print("STEP 427 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 427')
except Exception as e:
    print('FAIL - step 427' if isinstance(e, AssertionError) else f'ERROR - step 427: {e}')

print("STEP 428 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 428')
except Exception as e:
    print('FAIL - step 428' if isinstance(e, AssertionError) else f'ERROR - step 428: {e}')

print("STEP 429 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 429')
except Exception as e:
    print('FAIL - step 429' if isinstance(e, AssertionError) else f'ERROR - step 429: {e}')

print("STEP 430 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 430')
except Exception as e:
    print('FAIL - step 430' if isinstance(e, AssertionError) else f'ERROR - step 430: {e}')

print("STEP 431 - Check element div#None.['globalnav-item', 'globalnav-item-iphone', 'globalnav-item-menu', 'globalnav-item-submenu']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-item', 'globalnav-item-iphone', 'globalnav-item-menu', 'globalnav-item-submenu']")))
    print('PASS - step 431')
except Exception as e:
    print('FAIL - step 431' if isinstance(e, AssertionError) else f'ERROR - step 431: {e}')

print("STEP 432 - Check element ul#None.['globalnav-submenu-trigger-group']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-trigger-group']")))
    print('PASS - step 432')
except Exception as e:
    print('FAIL - step 432' if isinstance(e, AssertionError) else f'ERROR - step 432: {e}')

print("STEP 433 - Check element li#None.['globalnav-submenu-trigger-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-trigger-item']")))
    print('PASS - step 433')
except Exception as e:
    print('FAIL - step 433' if isinstance(e, AssertionError) else f'ERROR - step 433: {e}')

print("STEP 434 - Check element a#None.['globalnav-link', 'globalnav-submenu-trigger-link', 'globalnav-link-iphone']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-link', 'globalnav-submenu-trigger-link', 'globalnav-link-iphone']")))
    print('PASS - step 434')
except Exception as e:
    print('FAIL - step 434' if isinstance(e, AssertionError) else f'ERROR - step 434: {e}')

print("STEP 435 - Check element span#None.['globalnav-link-text-container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-link-text-container']")))
    print('PASS - step 435')
except Exception as e:
    print('FAIL - step 435' if isinstance(e, AssertionError) else f'ERROR - step 435: {e}')

print("STEP 436 - Check element span#None.['globalnav-image-regular', 'globalnav-link-image']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-image-regular', 'globalnav-link-image']")))
    print('PASS - step 436')
except Exception as e:
    print('FAIL - step 436' if isinstance(e, AssertionError) else f'ERROR - step 436: {e}')

print("STEP 437 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 437')
except Exception as e:
    print('FAIL - step 437' if isinstance(e, AssertionError) else f'ERROR - step 437: {e}')

print("STEP 438 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 438')
except Exception as e:
    print('FAIL - step 438' if isinstance(e, AssertionError) else f'ERROR - step 438: {e}')

print("STEP 439 - Check element span#None.['globalnav-link-text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-link-text']")))
    print('PASS - step 439')
except Exception as e:
    print('FAIL - step 439' if isinstance(e, AssertionError) else f'ERROR - step 439: {e}')

print("STEP 440 - Check element span#None.['globalnav-link-chevron']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-link-chevron']")))
    print('PASS - step 440')
except Exception as e:
    print('FAIL - step 440' if isinstance(e, AssertionError) else f'ERROR - step 440: {e}')

print("STEP 441 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 441')
except Exception as e:
    print('FAIL - step 441' if isinstance(e, AssertionError) else f'ERROR - step 441: {e}')

print("STEP 442 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 442')
except Exception as e:
    print('FAIL - step 442' if isinstance(e, AssertionError) else f'ERROR - step 442: {e}')

print("STEP 443 - Check element li#None.['globalnav-submenu-trigger-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-trigger-item']")))
    print('PASS - step 443')
except Exception as e:
    print('FAIL - step 443' if isinstance(e, AssertionError) else f'ERROR - step 443: {e}')

print("STEP 444 - Check element button#globalnav-menubutton-link-iphone.['globalnav-submenu-trigger-button']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "globalnav-menubutton-link-iphone")))
    print('PASS - step 444')
except Exception as e:
    print('FAIL - step 444' if isinstance(e, AssertionError) else f'ERROR - step 444: {e}')

print("STEP 445 - Check element span#None.['globalnav-image-regular', 'globalnav-submenu-button-icon']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-image-regular', 'globalnav-submenu-button-icon']")))
    print('PASS - step 445')
except Exception as e:
    print('FAIL - step 445' if isinstance(e, AssertionError) else f'ERROR - step 445: {e}')

print("STEP 446 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 446')
except Exception as e:
    print('FAIL - step 446' if isinstance(e, AssertionError) else f'ERROR - step 446: {e}')

print("STEP 447 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 447')
except Exception as e:
    print('FAIL - step 447' if isinstance(e, AssertionError) else f'ERROR - step 447: {e}')

print("STEP 448 - Check element span#None.['globalnav-image-compact', 'globalnav-submenu-button-icon']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-image-compact', 'globalnav-submenu-button-icon']")))
    print('PASS - step 448')
except Exception as e:
    print('FAIL - step 448' if isinstance(e, AssertionError) else f'ERROR - step 448: {e}')

print("STEP 449 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 449')
except Exception as e:
    print('FAIL - step 449' if isinstance(e, AssertionError) else f'ERROR - step 449: {e}')

print("STEP 450 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 450')
except Exception as e:
    print('FAIL - step 450' if isinstance(e, AssertionError) else f'ERROR - step 450: {e}')

print("STEP 451 - Check element div#globalnav-submenu-link-iphone.['globalnav-flyout', 'globalnav-submenu']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "globalnav-submenu-link-iphone")))
    print('PASS - step 451')
except Exception as e:
    print('FAIL - step 451' if isinstance(e, AssertionError) else f'ERROR - step 451: {e}')

print("STEP 452 - Check element div#None.['globalnav-flyout-scroll-container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-flyout-scroll-container']")))
    print('PASS - step 452')
except Exception as e:
    print('FAIL - step 452' if isinstance(e, AssertionError) else f'ERROR - step 452: {e}')

print("STEP 453 - Check element div#None.['globalnav-flyout-content', 'globalnav-submenu-content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-flyout-content', 'globalnav-submenu-content']")))
    print('PASS - step 453')
except Exception as e:
    print('FAIL - step 453' if isinstance(e, AssertionError) else f'ERROR - step 453: {e}')

print("STEP 454 - Check element div#None.['globalnav-submenu-group', 'globalnav-submenu-group-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-group', 'globalnav-submenu-group-elevated']")))
    print('PASS - step 454')
except Exception as e:
    print('FAIL - step 454' if isinstance(e, AssertionError) else f'ERROR - step 454: {e}')

print("STEP 455 - Check element h2#d836f05a.['globalnav-submenu-header']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "d836f05a")))
    print('PASS - step 455')
except Exception as e:
    print('FAIL - step 455' if isinstance(e, AssertionError) else f'ERROR - step 455: {e}')

print("STEP 456 - Check element ul#None.['globalnav-submenu-list']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list']")))
    print('PASS - step 456')
except Exception as e:
    print('FAIL - step 456' if isinstance(e, AssertionError) else f'ERROR - step 456: {e}')

print("STEP 457 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 457')
except Exception as e:
    print('FAIL - step 457' if isinstance(e, AssertionError) else f'ERROR - step 457: {e}')

print("STEP 458 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 458')
except Exception as e:
    print('FAIL - step 458' if isinstance(e, AssertionError) else f'ERROR - step 458: {e}')

print("STEP 459 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 459')
except Exception as e:
    print('FAIL - step 459' if isinstance(e, AssertionError) else f'ERROR - step 459: {e}')

print("STEP 460 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 460')
except Exception as e:
    print('FAIL - step 460' if isinstance(e, AssertionError) else f'ERROR - step 460: {e}')

print("STEP 461 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 461')
except Exception as e:
    print('FAIL - step 461' if isinstance(e, AssertionError) else f'ERROR - step 461: {e}')

print("STEP 462 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 462')
except Exception as e:
    print('FAIL - step 462' if isinstance(e, AssertionError) else f'ERROR - step 462: {e}')

print("STEP 463 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 463')
except Exception as e:
    print('FAIL - step 463' if isinstance(e, AssertionError) else f'ERROR - step 463: {e}')

print("STEP 464 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 464')
except Exception as e:
    print('FAIL - step 464' if isinstance(e, AssertionError) else f'ERROR - step 464: {e}')

print("STEP 465 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 465')
except Exception as e:
    print('FAIL - step 465' if isinstance(e, AssertionError) else f'ERROR - step 465: {e}')

print("STEP 466 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 466')
except Exception as e:
    print('FAIL - step 466' if isinstance(e, AssertionError) else f'ERROR - step 466: {e}')

print("STEP 467 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 467')
except Exception as e:
    print('FAIL - step 467' if isinstance(e, AssertionError) else f'ERROR - step 467: {e}')

print("STEP 468 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 468')
except Exception as e:
    print('FAIL - step 468' if isinstance(e, AssertionError) else f'ERROR - step 468: {e}')

print("STEP 469 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 469')
except Exception as e:
    print('FAIL - step 469' if isinstance(e, AssertionError) else f'ERROR - step 469: {e}')

print("STEP 470 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 470')
except Exception as e:
    print('FAIL - step 470' if isinstance(e, AssertionError) else f'ERROR - step 470: {e}')

print("STEP 471 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 471')
except Exception as e:
    print('FAIL - step 471' if isinstance(e, AssertionError) else f'ERROR - step 471: {e}')

print("STEP 472 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 472')
except Exception as e:
    print('FAIL - step 472' if isinstance(e, AssertionError) else f'ERROR - step 472: {e}')

print("STEP 473 - Check element div#None.['globalnav-submenu-group']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-group']")))
    print('PASS - step 473')
except Exception as e:
    print('FAIL - step 473' if isinstance(e, AssertionError) else f'ERROR - step 473: {e}')

print("STEP 474 - Check element h2#506e204c.['globalnav-submenu-header']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "506e204c")))
    print('PASS - step 474')
except Exception as e:
    print('FAIL - step 474' if isinstance(e, AssertionError) else f'ERROR - step 474: {e}')

print("STEP 475 - Check element ul#None.['globalnav-submenu-list']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list']")))
    print('PASS - step 475')
except Exception as e:
    print('FAIL - step 475' if isinstance(e, AssertionError) else f'ERROR - step 475: {e}')

print("STEP 476 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 476')
except Exception as e:
    print('FAIL - step 476' if isinstance(e, AssertionError) else f'ERROR - step 476: {e}')

print("STEP 477 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 477')
except Exception as e:
    print('FAIL - step 477' if isinstance(e, AssertionError) else f'ERROR - step 477: {e}')

print("STEP 478 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 478')
except Exception as e:
    print('FAIL - step 478' if isinstance(e, AssertionError) else f'ERROR - step 478: {e}')

print("STEP 479 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 479')
except Exception as e:
    print('FAIL - step 479' if isinstance(e, AssertionError) else f'ERROR - step 479: {e}')

print("STEP 480 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 480')
except Exception as e:
    print('FAIL - step 480' if isinstance(e, AssertionError) else f'ERROR - step 480: {e}')

print("STEP 481 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 481')
except Exception as e:
    print('FAIL - step 481' if isinstance(e, AssertionError) else f'ERROR - step 481: {e}')

print("STEP 482 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 482')
except Exception as e:
    print('FAIL - step 482' if isinstance(e, AssertionError) else f'ERROR - step 482: {e}')

print("STEP 483 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 483')
except Exception as e:
    print('FAIL - step 483' if isinstance(e, AssertionError) else f'ERROR - step 483: {e}')

print("STEP 484 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 484')
except Exception as e:
    print('FAIL - step 484' if isinstance(e, AssertionError) else f'ERROR - step 484: {e}')

print("STEP 485 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 485')
except Exception as e:
    print('FAIL - step 485' if isinstance(e, AssertionError) else f'ERROR - step 485: {e}')

print("STEP 486 - Check element div#None.['globalnav-submenu-group']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-group']")))
    print('PASS - step 486')
except Exception as e:
    print('FAIL - step 486' if isinstance(e, AssertionError) else f'ERROR - step 486: {e}')

print("STEP 487 - Check element h2#579bf70d.['globalnav-submenu-header']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "579bf70d")))
    print('PASS - step 487')
except Exception as e:
    print('FAIL - step 487' if isinstance(e, AssertionError) else f'ERROR - step 487: {e}')

print("STEP 488 - Check element ul#None.['globalnav-submenu-list']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list']")))
    print('PASS - step 488')
except Exception as e:
    print('FAIL - step 488' if isinstance(e, AssertionError) else f'ERROR - step 488: {e}')

print("STEP 489 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 489')
except Exception as e:
    print('FAIL - step 489' if isinstance(e, AssertionError) else f'ERROR - step 489: {e}')

print("STEP 490 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 490')
except Exception as e:
    print('FAIL - step 490' if isinstance(e, AssertionError) else f'ERROR - step 490: {e}')

print("STEP 491 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 491')
except Exception as e:
    print('FAIL - step 491' if isinstance(e, AssertionError) else f'ERROR - step 491: {e}')

print("STEP 492 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 492')
except Exception as e:
    print('FAIL - step 492' if isinstance(e, AssertionError) else f'ERROR - step 492: {e}')

print("STEP 493 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 493')
except Exception as e:
    print('FAIL - step 493' if isinstance(e, AssertionError) else f'ERROR - step 493: {e}')

print("STEP 494 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 494')
except Exception as e:
    print('FAIL - step 494' if isinstance(e, AssertionError) else f'ERROR - step 494: {e}')

print("STEP 495 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 495')
except Exception as e:
    print('FAIL - step 495' if isinstance(e, AssertionError) else f'ERROR - step 495: {e}')

print("STEP 496 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 496')
except Exception as e:
    print('FAIL - step 496' if isinstance(e, AssertionError) else f'ERROR - step 496: {e}')

print("STEP 497 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 497')
except Exception as e:
    print('FAIL - step 497' if isinstance(e, AssertionError) else f'ERROR - step 497: {e}')

print("STEP 498 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 498')
except Exception as e:
    print('FAIL - step 498' if isinstance(e, AssertionError) else f'ERROR - step 498: {e}')

print("STEP 499 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 499')
except Exception as e:
    print('FAIL - step 499' if isinstance(e, AssertionError) else f'ERROR - step 499: {e}')

print("STEP 500 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 500')
except Exception as e:
    print('FAIL - step 500' if isinstance(e, AssertionError) else f'ERROR - step 500: {e}')

print("STEP 501 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 501')
except Exception as e:
    print('FAIL - step 501' if isinstance(e, AssertionError) else f'ERROR - step 501: {e}')

print("STEP 502 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 502')
except Exception as e:
    print('FAIL - step 502' if isinstance(e, AssertionError) else f'ERROR - step 502: {e}')

print("STEP 503 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 503')
except Exception as e:
    print('FAIL - step 503' if isinstance(e, AssertionError) else f'ERROR - step 503: {e}')

print("STEP 504 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 504')
except Exception as e:
    print('FAIL - step 504' if isinstance(e, AssertionError) else f'ERROR - step 504: {e}')

print("STEP 505 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 505')
except Exception as e:
    print('FAIL - step 505' if isinstance(e, AssertionError) else f'ERROR - step 505: {e}')

print("STEP 506 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 506')
except Exception as e:
    print('FAIL - step 506' if isinstance(e, AssertionError) else f'ERROR - step 506: {e}')

print("STEP 507 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 507')
except Exception as e:
    print('FAIL - step 507' if isinstance(e, AssertionError) else f'ERROR - step 507: {e}')

print("STEP 508 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 508')
except Exception as e:
    print('FAIL - step 508' if isinstance(e, AssertionError) else f'ERROR - step 508: {e}')

print("STEP 509 - Check element div#None.['globalnav-item', 'globalnav-item-watch', 'globalnav-item-menu', 'globalnav-item-submenu']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-item', 'globalnav-item-watch', 'globalnav-item-menu', 'globalnav-item-submenu']")))
    print('PASS - step 509')
except Exception as e:
    print('FAIL - step 509' if isinstance(e, AssertionError) else f'ERROR - step 509: {e}')

print("STEP 510 - Check element ul#None.['globalnav-submenu-trigger-group']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-trigger-group']")))
    print('PASS - step 510')
except Exception as e:
    print('FAIL - step 510' if isinstance(e, AssertionError) else f'ERROR - step 510: {e}')

print("STEP 511 - Check element li#None.['globalnav-submenu-trigger-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-trigger-item']")))
    print('PASS - step 511')
except Exception as e:
    print('FAIL - step 511' if isinstance(e, AssertionError) else f'ERROR - step 511: {e}')

print("STEP 512 - Check element a#None.['globalnav-link', 'globalnav-submenu-trigger-link', 'globalnav-link-watch']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-link', 'globalnav-submenu-trigger-link', 'globalnav-link-watch']")))
    print('PASS - step 512')
except Exception as e:
    print('FAIL - step 512' if isinstance(e, AssertionError) else f'ERROR - step 512: {e}')

print("STEP 513 - Check element span#None.['globalnav-link-text-container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-link-text-container']")))
    print('PASS - step 513')
except Exception as e:
    print('FAIL - step 513' if isinstance(e, AssertionError) else f'ERROR - step 513: {e}')

print("STEP 514 - Check element span#None.['globalnav-image-regular', 'globalnav-link-image']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-image-regular', 'globalnav-link-image']")))
    print('PASS - step 514')
except Exception as e:
    print('FAIL - step 514' if isinstance(e, AssertionError) else f'ERROR - step 514: {e}')

print("STEP 515 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 515')
except Exception as e:
    print('FAIL - step 515' if isinstance(e, AssertionError) else f'ERROR - step 515: {e}')

print("STEP 516 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 516')
except Exception as e:
    print('FAIL - step 516' if isinstance(e, AssertionError) else f'ERROR - step 516: {e}')

print("STEP 517 - Check element span#None.['globalnav-link-text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-link-text']")))
    print('PASS - step 517')
except Exception as e:
    print('FAIL - step 517' if isinstance(e, AssertionError) else f'ERROR - step 517: {e}')

print("STEP 518 - Check element span#None.['globalnav-link-chevron']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-link-chevron']")))
    print('PASS - step 518')
except Exception as e:
    print('FAIL - step 518' if isinstance(e, AssertionError) else f'ERROR - step 518: {e}')

print("STEP 519 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 519')
except Exception as e:
    print('FAIL - step 519' if isinstance(e, AssertionError) else f'ERROR - step 519: {e}')

print("STEP 520 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 520')
except Exception as e:
    print('FAIL - step 520' if isinstance(e, AssertionError) else f'ERROR - step 520: {e}')

print("STEP 521 - Check element li#None.['globalnav-submenu-trigger-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-trigger-item']")))
    print('PASS - step 521')
except Exception as e:
    print('FAIL - step 521' if isinstance(e, AssertionError) else f'ERROR - step 521: {e}')

print("STEP 522 - Check element button#globalnav-menubutton-link-watch.['globalnav-submenu-trigger-button']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "globalnav-menubutton-link-watch")))
    print('PASS - step 522')
except Exception as e:
    print('FAIL - step 522' if isinstance(e, AssertionError) else f'ERROR - step 522: {e}')

print("STEP 523 - Check element span#None.['globalnav-image-regular', 'globalnav-submenu-button-icon']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-image-regular', 'globalnav-submenu-button-icon']")))
    print('PASS - step 523')
except Exception as e:
    print('FAIL - step 523' if isinstance(e, AssertionError) else f'ERROR - step 523: {e}')

print("STEP 524 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 524')
except Exception as e:
    print('FAIL - step 524' if isinstance(e, AssertionError) else f'ERROR - step 524: {e}')

print("STEP 525 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 525')
except Exception as e:
    print('FAIL - step 525' if isinstance(e, AssertionError) else f'ERROR - step 525: {e}')

print("STEP 526 - Check element span#None.['globalnav-image-compact', 'globalnav-submenu-button-icon']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-image-compact', 'globalnav-submenu-button-icon']")))
    print('PASS - step 526')
except Exception as e:
    print('FAIL - step 526' if isinstance(e, AssertionError) else f'ERROR - step 526: {e}')

print("STEP 527 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 527')
except Exception as e:
    print('FAIL - step 527' if isinstance(e, AssertionError) else f'ERROR - step 527: {e}')

print("STEP 528 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 528')
except Exception as e:
    print('FAIL - step 528' if isinstance(e, AssertionError) else f'ERROR - step 528: {e}')

print("STEP 529 - Check element div#globalnav-submenu-link-watch.['globalnav-flyout', 'globalnav-submenu']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "globalnav-submenu-link-watch")))
    print('PASS - step 529')
except Exception as e:
    print('FAIL - step 529' if isinstance(e, AssertionError) else f'ERROR - step 529: {e}')

print("STEP 530 - Check element div#None.['globalnav-flyout-scroll-container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-flyout-scroll-container']")))
    print('PASS - step 530')
except Exception as e:
    print('FAIL - step 530' if isinstance(e, AssertionError) else f'ERROR - step 530: {e}')

print("STEP 531 - Check element div#None.['globalnav-flyout-content', 'globalnav-submenu-content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-flyout-content', 'globalnav-submenu-content']")))
    print('PASS - step 531')
except Exception as e:
    print('FAIL - step 531' if isinstance(e, AssertionError) else f'ERROR - step 531: {e}')

print("STEP 532 - Check element div#None.['globalnav-submenu-group', 'globalnav-submenu-group-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-group', 'globalnav-submenu-group-elevated']")))
    print('PASS - step 532')
except Exception as e:
    print('FAIL - step 532' if isinstance(e, AssertionError) else f'ERROR - step 532: {e}')

print("STEP 533 - Check element h2#666abc94.['globalnav-submenu-header']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "666abc94")))
    print('PASS - step 533')
except Exception as e:
    print('FAIL - step 533' if isinstance(e, AssertionError) else f'ERROR - step 533: {e}')

print("STEP 534 - Check element ul#None.['globalnav-submenu-list']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list']")))
    print('PASS - step 534')
except Exception as e:
    print('FAIL - step 534' if isinstance(e, AssertionError) else f'ERROR - step 534: {e}')

print("STEP 535 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 535')
except Exception as e:
    print('FAIL - step 535' if isinstance(e, AssertionError) else f'ERROR - step 535: {e}')

print("STEP 536 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 536')
except Exception as e:
    print('FAIL - step 536' if isinstance(e, AssertionError) else f'ERROR - step 536: {e}')

print("STEP 537 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 537')
except Exception as e:
    print('FAIL - step 537' if isinstance(e, AssertionError) else f'ERROR - step 537: {e}')

print("STEP 538 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 538')
except Exception as e:
    print('FAIL - step 538' if isinstance(e, AssertionError) else f'ERROR - step 538: {e}')

print("STEP 539 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 539')
except Exception as e:
    print('FAIL - step 539' if isinstance(e, AssertionError) else f'ERROR - step 539: {e}')

print("STEP 540 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 540')
except Exception as e:
    print('FAIL - step 540' if isinstance(e, AssertionError) else f'ERROR - step 540: {e}')

print("STEP 541 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 541')
except Exception as e:
    print('FAIL - step 541' if isinstance(e, AssertionError) else f'ERROR - step 541: {e}')

print("STEP 542 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 542')
except Exception as e:
    print('FAIL - step 542' if isinstance(e, AssertionError) else f'ERROR - step 542: {e}')

print("STEP 543 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 543')
except Exception as e:
    print('FAIL - step 543' if isinstance(e, AssertionError) else f'ERROR - step 543: {e}')

print("STEP 544 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 544')
except Exception as e:
    print('FAIL - step 544' if isinstance(e, AssertionError) else f'ERROR - step 544: {e}')

print("STEP 545 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 545')
except Exception as e:
    print('FAIL - step 545' if isinstance(e, AssertionError) else f'ERROR - step 545: {e}')

print("STEP 546 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 546')
except Exception as e:
    print('FAIL - step 546' if isinstance(e, AssertionError) else f'ERROR - step 546: {e}')

print("STEP 547 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 547')
except Exception as e:
    print('FAIL - step 547' if isinstance(e, AssertionError) else f'ERROR - step 547: {e}')

print("STEP 548 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 548')
except Exception as e:
    print('FAIL - step 548' if isinstance(e, AssertionError) else f'ERROR - step 548: {e}')

print("STEP 549 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 549')
except Exception as e:
    print('FAIL - step 549' if isinstance(e, AssertionError) else f'ERROR - step 549: {e}')

print("STEP 550 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 550')
except Exception as e:
    print('FAIL - step 550' if isinstance(e, AssertionError) else f'ERROR - step 550: {e}')

print("STEP 551 - Check element div#None.['globalnav-submenu-group']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-group']")))
    print('PASS - step 551')
except Exception as e:
    print('FAIL - step 551' if isinstance(e, AssertionError) else f'ERROR - step 551: {e}')

print("STEP 552 - Check element h2#1eec1530.['globalnav-submenu-header']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "1eec1530")))
    print('PASS - step 552')
except Exception as e:
    print('FAIL - step 552' if isinstance(e, AssertionError) else f'ERROR - step 552: {e}')

print("STEP 553 - Check element ul#None.['globalnav-submenu-list']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list']")))
    print('PASS - step 553')
except Exception as e:
    print('FAIL - step 553' if isinstance(e, AssertionError) else f'ERROR - step 553: {e}')

print("STEP 554 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 554')
except Exception as e:
    print('FAIL - step 554' if isinstance(e, AssertionError) else f'ERROR - step 554: {e}')

print("STEP 555 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 555')
except Exception as e:
    print('FAIL - step 555' if isinstance(e, AssertionError) else f'ERROR - step 555: {e}')

print("STEP 556 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 556')
except Exception as e:
    print('FAIL - step 556' if isinstance(e, AssertionError) else f'ERROR - step 556: {e}')

print("STEP 557 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 557')
except Exception as e:
    print('FAIL - step 557' if isinstance(e, AssertionError) else f'ERROR - step 557: {e}')

print("STEP 558 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 558')
except Exception as e:
    print('FAIL - step 558' if isinstance(e, AssertionError) else f'ERROR - step 558: {e}')

print("STEP 559 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 559')
except Exception as e:
    print('FAIL - step 559' if isinstance(e, AssertionError) else f'ERROR - step 559: {e}')

print("STEP 560 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 560')
except Exception as e:
    print('FAIL - step 560' if isinstance(e, AssertionError) else f'ERROR - step 560: {e}')

print("STEP 561 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 561')
except Exception as e:
    print('FAIL - step 561' if isinstance(e, AssertionError) else f'ERROR - step 561: {e}')

print("STEP 562 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 562')
except Exception as e:
    print('FAIL - step 562' if isinstance(e, AssertionError) else f'ERROR - step 562: {e}')

print("STEP 563 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 563')
except Exception as e:
    print('FAIL - step 563' if isinstance(e, AssertionError) else f'ERROR - step 563: {e}')

print("STEP 564 - Check element div#None.['globalnav-submenu-group']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-group']")))
    print('PASS - step 564')
except Exception as e:
    print('FAIL - step 564' if isinstance(e, AssertionError) else f'ERROR - step 564: {e}')

print("STEP 565 - Check element h2#1f4cd485.['globalnav-submenu-header']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "1f4cd485")))
    print('PASS - step 565')
except Exception as e:
    print('FAIL - step 565' if isinstance(e, AssertionError) else f'ERROR - step 565: {e}')

print("STEP 566 - Check element ul#None.['globalnav-submenu-list']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list']")))
    print('PASS - step 566')
except Exception as e:
    print('FAIL - step 566' if isinstance(e, AssertionError) else f'ERROR - step 566: {e}')

print("STEP 567 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 567')
except Exception as e:
    print('FAIL - step 567' if isinstance(e, AssertionError) else f'ERROR - step 567: {e}')

print("STEP 568 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 568')
except Exception as e:
    print('FAIL - step 568' if isinstance(e, AssertionError) else f'ERROR - step 568: {e}')

print("STEP 569 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 569')
except Exception as e:
    print('FAIL - step 569' if isinstance(e, AssertionError) else f'ERROR - step 569: {e}')

print("STEP 570 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 570')
except Exception as e:
    print('FAIL - step 570' if isinstance(e, AssertionError) else f'ERROR - step 570: {e}')

print("STEP 571 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 571')
except Exception as e:
    print('FAIL - step 571' if isinstance(e, AssertionError) else f'ERROR - step 571: {e}')

print("STEP 572 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 572')
except Exception as e:
    print('FAIL - step 572' if isinstance(e, AssertionError) else f'ERROR - step 572: {e}')

print("STEP 573 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 573')
except Exception as e:
    print('FAIL - step 573' if isinstance(e, AssertionError) else f'ERROR - step 573: {e}')

print("STEP 574 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 574')
except Exception as e:
    print('FAIL - step 574' if isinstance(e, AssertionError) else f'ERROR - step 574: {e}')

print("STEP 575 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 575')
except Exception as e:
    print('FAIL - step 575' if isinstance(e, AssertionError) else f'ERROR - step 575: {e}')

print("STEP 576 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 576')
except Exception as e:
    print('FAIL - step 576' if isinstance(e, AssertionError) else f'ERROR - step 576: {e}')

print("STEP 577 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 577')
except Exception as e:
    print('FAIL - step 577' if isinstance(e, AssertionError) else f'ERROR - step 577: {e}')

print("STEP 578 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 578')
except Exception as e:
    print('FAIL - step 578' if isinstance(e, AssertionError) else f'ERROR - step 578: {e}')

print("STEP 579 - Check element div#None.['globalnav-item', 'globalnav-item-vision', 'globalnav-item-menu', 'globalnav-item-submenu']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-item', 'globalnav-item-vision', 'globalnav-item-menu', 'globalnav-item-submenu']")))
    print('PASS - step 579')
except Exception as e:
    print('FAIL - step 579' if isinstance(e, AssertionError) else f'ERROR - step 579: {e}')

print("STEP 580 - Check element ul#None.['globalnav-submenu-trigger-group']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-trigger-group']")))
    print('PASS - step 580')
except Exception as e:
    print('FAIL - step 580' if isinstance(e, AssertionError) else f'ERROR - step 580: {e}')

print("STEP 581 - Check element li#None.['globalnav-submenu-trigger-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-trigger-item']")))
    print('PASS - step 581')
except Exception as e:
    print('FAIL - step 581' if isinstance(e, AssertionError) else f'ERROR - step 581: {e}')

print("STEP 582 - Check element a#None.['globalnav-link', 'globalnav-submenu-trigger-link', 'globalnav-link-vision']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-link', 'globalnav-submenu-trigger-link', 'globalnav-link-vision']")))
    print('PASS - step 582')
except Exception as e:
    print('FAIL - step 582' if isinstance(e, AssertionError) else f'ERROR - step 582: {e}')

print("STEP 583 - Check element span#None.['globalnav-link-text-container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-link-text-container']")))
    print('PASS - step 583')
except Exception as e:
    print('FAIL - step 583' if isinstance(e, AssertionError) else f'ERROR - step 583: {e}')

print("STEP 584 - Check element span#None.['globalnav-image-regular', 'globalnav-link-image']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-image-regular', 'globalnav-link-image']")))
    print('PASS - step 584')
except Exception as e:
    print('FAIL - step 584' if isinstance(e, AssertionError) else f'ERROR - step 584: {e}')

print("STEP 585 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 585')
except Exception as e:
    print('FAIL - step 585' if isinstance(e, AssertionError) else f'ERROR - step 585: {e}')

print("STEP 586 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 586')
except Exception as e:
    print('FAIL - step 586' if isinstance(e, AssertionError) else f'ERROR - step 586: {e}')

print("STEP 587 - Check element span#None.['globalnav-link-text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-link-text']")))
    print('PASS - step 587')
except Exception as e:
    print('FAIL - step 587' if isinstance(e, AssertionError) else f'ERROR - step 587: {e}')

print("STEP 588 - Check element span#None.['globalnav-link-chevron']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-link-chevron']")))
    print('PASS - step 588')
except Exception as e:
    print('FAIL - step 588' if isinstance(e, AssertionError) else f'ERROR - step 588: {e}')

print("STEP 589 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 589')
except Exception as e:
    print('FAIL - step 589' if isinstance(e, AssertionError) else f'ERROR - step 589: {e}')

print("STEP 590 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 590')
except Exception as e:
    print('FAIL - step 590' if isinstance(e, AssertionError) else f'ERROR - step 590: {e}')

print("STEP 591 - Check element li#None.['globalnav-submenu-trigger-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-trigger-item']")))
    print('PASS - step 591')
except Exception as e:
    print('FAIL - step 591' if isinstance(e, AssertionError) else f'ERROR - step 591: {e}')

print("STEP 592 - Check element button#globalnav-menubutton-link-vision.['globalnav-submenu-trigger-button']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "globalnav-menubutton-link-vision")))
    print('PASS - step 592')
except Exception as e:
    print('FAIL - step 592' if isinstance(e, AssertionError) else f'ERROR - step 592: {e}')

print("STEP 593 - Check element span#None.['globalnav-image-regular', 'globalnav-submenu-button-icon']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-image-regular', 'globalnav-submenu-button-icon']")))
    print('PASS - step 593')
except Exception as e:
    print('FAIL - step 593' if isinstance(e, AssertionError) else f'ERROR - step 593: {e}')

print("STEP 594 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 594')
except Exception as e:
    print('FAIL - step 594' if isinstance(e, AssertionError) else f'ERROR - step 594: {e}')

print("STEP 595 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 595')
except Exception as e:
    print('FAIL - step 595' if isinstance(e, AssertionError) else f'ERROR - step 595: {e}')

print("STEP 596 - Check element span#None.['globalnav-image-compact', 'globalnav-submenu-button-icon']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-image-compact', 'globalnav-submenu-button-icon']")))
    print('PASS - step 596')
except Exception as e:
    print('FAIL - step 596' if isinstance(e, AssertionError) else f'ERROR - step 596: {e}')

print("STEP 597 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 597')
except Exception as e:
    print('FAIL - step 597' if isinstance(e, AssertionError) else f'ERROR - step 597: {e}')

print("STEP 598 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 598')
except Exception as e:
    print('FAIL - step 598' if isinstance(e, AssertionError) else f'ERROR - step 598: {e}')

print("STEP 599 - Check element div#globalnav-submenu-link-vision.['globalnav-flyout', 'globalnav-submenu']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "globalnav-submenu-link-vision")))
    print('PASS - step 599')
except Exception as e:
    print('FAIL - step 599' if isinstance(e, AssertionError) else f'ERROR - step 599: {e}')

print("STEP 600 - Check element div#None.['globalnav-flyout-scroll-container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-flyout-scroll-container']")))
    print('PASS - step 600')
except Exception as e:
    print('FAIL - step 600' if isinstance(e, AssertionError) else f'ERROR - step 600: {e}')

print("STEP 601 - Check element div#None.['globalnav-flyout-content', 'globalnav-submenu-content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-flyout-content', 'globalnav-submenu-content']")))
    print('PASS - step 601')
except Exception as e:
    print('FAIL - step 601' if isinstance(e, AssertionError) else f'ERROR - step 601: {e}')

print("STEP 602 - Check element div#None.['globalnav-submenu-group', 'globalnav-submenu-group-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-group', 'globalnav-submenu-group-elevated']")))
    print('PASS - step 602')
except Exception as e:
    print('FAIL - step 602' if isinstance(e, AssertionError) else f'ERROR - step 602: {e}')

print("STEP 603 - Check element h2#43b5f4f2.['globalnav-submenu-header']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "43b5f4f2")))
    print('PASS - step 603')
except Exception as e:
    print('FAIL - step 603' if isinstance(e, AssertionError) else f'ERROR - step 603: {e}')

print("STEP 604 - Check element ul#None.['globalnav-submenu-list']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list']")))
    print('PASS - step 604')
except Exception as e:
    print('FAIL - step 604' if isinstance(e, AssertionError) else f'ERROR - step 604: {e}')

print("STEP 605 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 605')
except Exception as e:
    print('FAIL - step 605' if isinstance(e, AssertionError) else f'ERROR - step 605: {e}')

print("STEP 606 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 606')
except Exception as e:
    print('FAIL - step 606' if isinstance(e, AssertionError) else f'ERROR - step 606: {e}')

print("STEP 607 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 607')
except Exception as e:
    print('FAIL - step 607' if isinstance(e, AssertionError) else f'ERROR - step 607: {e}')

print("STEP 608 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 608')
except Exception as e:
    print('FAIL - step 608' if isinstance(e, AssertionError) else f'ERROR - step 608: {e}')

print("STEP 609 - Check element div#None.['globalnav-submenu-group']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-group']")))
    print('PASS - step 609')
except Exception as e:
    print('FAIL - step 609' if isinstance(e, AssertionError) else f'ERROR - step 609: {e}')

print("STEP 610 - Check element h2#19eb6286.['globalnav-submenu-header']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "19eb6286")))
    print('PASS - step 610')
except Exception as e:
    print('FAIL - step 610' if isinstance(e, AssertionError) else f'ERROR - step 610: {e}')

print("STEP 611 - Check element ul#None.['globalnav-submenu-list']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list']")))
    print('PASS - step 611')
except Exception as e:
    print('FAIL - step 611' if isinstance(e, AssertionError) else f'ERROR - step 611: {e}')

print("STEP 612 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 612')
except Exception as e:
    print('FAIL - step 612' if isinstance(e, AssertionError) else f'ERROR - step 612: {e}')

print("STEP 613 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 613')
except Exception as e:
    print('FAIL - step 613' if isinstance(e, AssertionError) else f'ERROR - step 613: {e}')

print("STEP 614 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 614')
except Exception as e:
    print('FAIL - step 614' if isinstance(e, AssertionError) else f'ERROR - step 614: {e}')

print("STEP 615 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 615')
except Exception as e:
    print('FAIL - step 615' if isinstance(e, AssertionError) else f'ERROR - step 615: {e}')

print("STEP 616 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 616')
except Exception as e:
    print('FAIL - step 616' if isinstance(e, AssertionError) else f'ERROR - step 616: {e}')

print("STEP 617 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 617')
except Exception as e:
    print('FAIL - step 617' if isinstance(e, AssertionError) else f'ERROR - step 617: {e}')

print("STEP 618 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 618')
except Exception as e:
    print('FAIL - step 618' if isinstance(e, AssertionError) else f'ERROR - step 618: {e}')

print("STEP 619 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 619')
except Exception as e:
    print('FAIL - step 619' if isinstance(e, AssertionError) else f'ERROR - step 619: {e}')

print("STEP 620 - Check element div#None.['globalnav-submenu-group']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-group']")))
    print('PASS - step 620')
except Exception as e:
    print('FAIL - step 620' if isinstance(e, AssertionError) else f'ERROR - step 620: {e}')

print("STEP 621 - Check element h2#93ef82be.['globalnav-submenu-header']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "93ef82be")))
    print('PASS - step 621')
except Exception as e:
    print('FAIL - step 621' if isinstance(e, AssertionError) else f'ERROR - step 621: {e}')

print("STEP 622 - Check element ul#None.['globalnav-submenu-list']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list']")))
    print('PASS - step 622')
except Exception as e:
    print('FAIL - step 622' if isinstance(e, AssertionError) else f'ERROR - step 622: {e}')

print("STEP 623 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 623')
except Exception as e:
    print('FAIL - step 623' if isinstance(e, AssertionError) else f'ERROR - step 623: {e}')

print("STEP 624 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 624')
except Exception as e:
    print('FAIL - step 624' if isinstance(e, AssertionError) else f'ERROR - step 624: {e}')

print("STEP 625 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 625')
except Exception as e:
    print('FAIL - step 625' if isinstance(e, AssertionError) else f'ERROR - step 625: {e}')

print("STEP 626 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 626')
except Exception as e:
    print('FAIL - step 626' if isinstance(e, AssertionError) else f'ERROR - step 626: {e}')

print("STEP 627 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 627')
except Exception as e:
    print('FAIL - step 627' if isinstance(e, AssertionError) else f'ERROR - step 627: {e}')

print("STEP 628 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 628')
except Exception as e:
    print('FAIL - step 628' if isinstance(e, AssertionError) else f'ERROR - step 628: {e}')

print("STEP 629 - Check element div#None.['globalnav-item', 'globalnav-item-airpods', 'globalnav-item-menu', 'globalnav-item-submenu']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-item', 'globalnav-item-airpods', 'globalnav-item-menu', 'globalnav-item-submenu']")))
    print('PASS - step 629')
except Exception as e:
    print('FAIL - step 629' if isinstance(e, AssertionError) else f'ERROR - step 629: {e}')

print("STEP 630 - Check element ul#None.['globalnav-submenu-trigger-group']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-trigger-group']")))
    print('PASS - step 630')
except Exception as e:
    print('FAIL - step 630' if isinstance(e, AssertionError) else f'ERROR - step 630: {e}')

print("STEP 631 - Check element li#None.['globalnav-submenu-trigger-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-trigger-item']")))
    print('PASS - step 631')
except Exception as e:
    print('FAIL - step 631' if isinstance(e, AssertionError) else f'ERROR - step 631: {e}')

print("STEP 632 - Check element a#None.['globalnav-link', 'globalnav-submenu-trigger-link', 'globalnav-link-airpods']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-link', 'globalnav-submenu-trigger-link', 'globalnav-link-airpods']")))
    print('PASS - step 632')
except Exception as e:
    print('FAIL - step 632' if isinstance(e, AssertionError) else f'ERROR - step 632: {e}')

print("STEP 633 - Check element span#None.['globalnav-link-text-container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-link-text-container']")))
    print('PASS - step 633')
except Exception as e:
    print('FAIL - step 633' if isinstance(e, AssertionError) else f'ERROR - step 633: {e}')

print("STEP 634 - Check element span#None.['globalnav-image-regular', 'globalnav-link-image']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-image-regular', 'globalnav-link-image']")))
    print('PASS - step 634')
except Exception as e:
    print('FAIL - step 634' if isinstance(e, AssertionError) else f'ERROR - step 634: {e}')

print("STEP 635 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 635')
except Exception as e:
    print('FAIL - step 635' if isinstance(e, AssertionError) else f'ERROR - step 635: {e}')

print("STEP 636 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 636')
except Exception as e:
    print('FAIL - step 636' if isinstance(e, AssertionError) else f'ERROR - step 636: {e}')

print("STEP 637 - Check element span#None.['globalnav-link-text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-link-text']")))
    print('PASS - step 637')
except Exception as e:
    print('FAIL - step 637' if isinstance(e, AssertionError) else f'ERROR - step 637: {e}')

print("STEP 638 - Check element span#None.['globalnav-link-chevron']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-link-chevron']")))
    print('PASS - step 638')
except Exception as e:
    print('FAIL - step 638' if isinstance(e, AssertionError) else f'ERROR - step 638: {e}')

print("STEP 639 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 639')
except Exception as e:
    print('FAIL - step 639' if isinstance(e, AssertionError) else f'ERROR - step 639: {e}')

print("STEP 640 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 640')
except Exception as e:
    print('FAIL - step 640' if isinstance(e, AssertionError) else f'ERROR - step 640: {e}')

print("STEP 641 - Check element li#None.['globalnav-submenu-trigger-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-trigger-item']")))
    print('PASS - step 641')
except Exception as e:
    print('FAIL - step 641' if isinstance(e, AssertionError) else f'ERROR - step 641: {e}')

print("STEP 642 - Check element button#globalnav-menubutton-link-airpods.['globalnav-submenu-trigger-button']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "globalnav-menubutton-link-airpods")))
    print('PASS - step 642')
except Exception as e:
    print('FAIL - step 642' if isinstance(e, AssertionError) else f'ERROR - step 642: {e}')

print("STEP 643 - Check element span#None.['globalnav-image-regular', 'globalnav-submenu-button-icon']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-image-regular', 'globalnav-submenu-button-icon']")))
    print('PASS - step 643')
except Exception as e:
    print('FAIL - step 643' if isinstance(e, AssertionError) else f'ERROR - step 643: {e}')

print("STEP 644 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 644')
except Exception as e:
    print('FAIL - step 644' if isinstance(e, AssertionError) else f'ERROR - step 644: {e}')

print("STEP 645 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 645')
except Exception as e:
    print('FAIL - step 645' if isinstance(e, AssertionError) else f'ERROR - step 645: {e}')

print("STEP 646 - Check element span#None.['globalnav-image-compact', 'globalnav-submenu-button-icon']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-image-compact', 'globalnav-submenu-button-icon']")))
    print('PASS - step 646')
except Exception as e:
    print('FAIL - step 646' if isinstance(e, AssertionError) else f'ERROR - step 646: {e}')

print("STEP 647 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 647')
except Exception as e:
    print('FAIL - step 647' if isinstance(e, AssertionError) else f'ERROR - step 647: {e}')

print("STEP 648 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 648')
except Exception as e:
    print('FAIL - step 648' if isinstance(e, AssertionError) else f'ERROR - step 648: {e}')

print("STEP 649 - Check element div#globalnav-submenu-link-airpods.['globalnav-flyout', 'globalnav-submenu']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "globalnav-submenu-link-airpods")))
    print('PASS - step 649')
except Exception as e:
    print('FAIL - step 649' if isinstance(e, AssertionError) else f'ERROR - step 649: {e}')

print("STEP 650 - Check element div#None.['globalnav-flyout-scroll-container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-flyout-scroll-container']")))
    print('PASS - step 650')
except Exception as e:
    print('FAIL - step 650' if isinstance(e, AssertionError) else f'ERROR - step 650: {e}')

print("STEP 651 - Check element div#None.['globalnav-flyout-content', 'globalnav-submenu-content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-flyout-content', 'globalnav-submenu-content']")))
    print('PASS - step 651')
except Exception as e:
    print('FAIL - step 651' if isinstance(e, AssertionError) else f'ERROR - step 651: {e}')

print("STEP 652 - Check element div#None.['globalnav-submenu-group', 'globalnav-submenu-group-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-group', 'globalnav-submenu-group-elevated']")))
    print('PASS - step 652')
except Exception as e:
    print('FAIL - step 652' if isinstance(e, AssertionError) else f'ERROR - step 652: {e}')

print("STEP 653 - Check element h2#9f37924e.['globalnav-submenu-header']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "9f37924e")))
    print('PASS - step 653')
except Exception as e:
    print('FAIL - step 653' if isinstance(e, AssertionError) else f'ERROR - step 653: {e}')

print("STEP 654 - Check element ul#None.['globalnav-submenu-list']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list']")))
    print('PASS - step 654')
except Exception as e:
    print('FAIL - step 654' if isinstance(e, AssertionError) else f'ERROR - step 654: {e}')

print("STEP 655 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 655')
except Exception as e:
    print('FAIL - step 655' if isinstance(e, AssertionError) else f'ERROR - step 655: {e}')

print("STEP 656 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 656')
except Exception as e:
    print('FAIL - step 656' if isinstance(e, AssertionError) else f'ERROR - step 656: {e}')

print("STEP 657 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 657')
except Exception as e:
    print('FAIL - step 657' if isinstance(e, AssertionError) else f'ERROR - step 657: {e}')

print("STEP 658 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 658')
except Exception as e:
    print('FAIL - step 658' if isinstance(e, AssertionError) else f'ERROR - step 658: {e}')

print("STEP 659 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 659')
except Exception as e:
    print('FAIL - step 659' if isinstance(e, AssertionError) else f'ERROR - step 659: {e}')

print("STEP 660 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 660')
except Exception as e:
    print('FAIL - step 660' if isinstance(e, AssertionError) else f'ERROR - step 660: {e}')

print("STEP 661 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 661')
except Exception as e:
    print('FAIL - step 661' if isinstance(e, AssertionError) else f'ERROR - step 661: {e}')

print("STEP 662 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 662')
except Exception as e:
    print('FAIL - step 662' if isinstance(e, AssertionError) else f'ERROR - step 662: {e}')

print("STEP 663 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 663')
except Exception as e:
    print('FAIL - step 663' if isinstance(e, AssertionError) else f'ERROR - step 663: {e}')

print("STEP 664 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 664')
except Exception as e:
    print('FAIL - step 664' if isinstance(e, AssertionError) else f'ERROR - step 664: {e}')

print("STEP 665 - Check element div#None.['globalnav-submenu-group']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-group']")))
    print('PASS - step 665')
except Exception as e:
    print('FAIL - step 665' if isinstance(e, AssertionError) else f'ERROR - step 665: {e}')

print("STEP 666 - Check element h2#afb7a2a1.['globalnav-submenu-header']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "afb7a2a1")))
    print('PASS - step 666')
except Exception as e:
    print('FAIL - step 666' if isinstance(e, AssertionError) else f'ERROR - step 666: {e}')

print("STEP 667 - Check element ul#None.['globalnav-submenu-list']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list']")))
    print('PASS - step 667')
except Exception as e:
    print('FAIL - step 667' if isinstance(e, AssertionError) else f'ERROR - step 667: {e}')

print("STEP 668 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 668')
except Exception as e:
    print('FAIL - step 668' if isinstance(e, AssertionError) else f'ERROR - step 668: {e}')

print("STEP 669 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 669')
except Exception as e:
    print('FAIL - step 669' if isinstance(e, AssertionError) else f'ERROR - step 669: {e}')

print("STEP 670 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 670')
except Exception as e:
    print('FAIL - step 670' if isinstance(e, AssertionError) else f'ERROR - step 670: {e}')

print("STEP 671 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 671')
except Exception as e:
    print('FAIL - step 671' if isinstance(e, AssertionError) else f'ERROR - step 671: {e}')

print("STEP 672 - Check element div#None.['globalnav-submenu-group']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-group']")))
    print('PASS - step 672')
except Exception as e:
    print('FAIL - step 672' if isinstance(e, AssertionError) else f'ERROR - step 672: {e}')

print("STEP 673 - Check element h2#e8053cac.['globalnav-submenu-header']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "e8053cac")))
    print('PASS - step 673')
except Exception as e:
    print('FAIL - step 673' if isinstance(e, AssertionError) else f'ERROR - step 673: {e}')

print("STEP 674 - Check element ul#None.['globalnav-submenu-list']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list']")))
    print('PASS - step 674')
except Exception as e:
    print('FAIL - step 674' if isinstance(e, AssertionError) else f'ERROR - step 674: {e}')

print("STEP 675 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 675')
except Exception as e:
    print('FAIL - step 675' if isinstance(e, AssertionError) else f'ERROR - step 675: {e}')

print("STEP 676 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 676')
except Exception as e:
    print('FAIL - step 676' if isinstance(e, AssertionError) else f'ERROR - step 676: {e}')

print("STEP 677 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 677')
except Exception as e:
    print('FAIL - step 677' if isinstance(e, AssertionError) else f'ERROR - step 677: {e}')

print("STEP 678 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 678')
except Exception as e:
    print('FAIL - step 678' if isinstance(e, AssertionError) else f'ERROR - step 678: {e}')

print("STEP 679 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 679')
except Exception as e:
    print('FAIL - step 679' if isinstance(e, AssertionError) else f'ERROR - step 679: {e}')

print("STEP 680 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 680')
except Exception as e:
    print('FAIL - step 680' if isinstance(e, AssertionError) else f'ERROR - step 680: {e}')

print("STEP 681 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 681')
except Exception as e:
    print('FAIL - step 681' if isinstance(e, AssertionError) else f'ERROR - step 681: {e}')

print("STEP 682 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 682')
except Exception as e:
    print('FAIL - step 682' if isinstance(e, AssertionError) else f'ERROR - step 682: {e}')

print("STEP 683 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 683')
except Exception as e:
    print('FAIL - step 683' if isinstance(e, AssertionError) else f'ERROR - step 683: {e}')

print("STEP 684 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 684')
except Exception as e:
    print('FAIL - step 684' if isinstance(e, AssertionError) else f'ERROR - step 684: {e}')

print("STEP 685 - Check element div#None.['globalnav-item', 'globalnav-item-tv-home', 'globalnav-item-menu', 'globalnav-item-submenu']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-item', 'globalnav-item-tv-home', 'globalnav-item-menu', 'globalnav-item-submenu']")))
    print('PASS - step 685')
except Exception as e:
    print('FAIL - step 685' if isinstance(e, AssertionError) else f'ERROR - step 685: {e}')

print("STEP 686 - Check element ul#None.['globalnav-submenu-trigger-group']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-trigger-group']")))
    print('PASS - step 686')
except Exception as e:
    print('FAIL - step 686' if isinstance(e, AssertionError) else f'ERROR - step 686: {e}')

print("STEP 687 - Check element li#None.['globalnav-submenu-trigger-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-trigger-item']")))
    print('PASS - step 687')
except Exception as e:
    print('FAIL - step 687' if isinstance(e, AssertionError) else f'ERROR - step 687: {e}')

print("STEP 688 - Check element a#None.['globalnav-link', 'globalnav-submenu-trigger-link', 'globalnav-link-tv-home']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-link', 'globalnav-submenu-trigger-link', 'globalnav-link-tv-home']")))
    print('PASS - step 688')
except Exception as e:
    print('FAIL - step 688' if isinstance(e, AssertionError) else f'ERROR - step 688: {e}')

print("STEP 689 - Check element span#None.['globalnav-link-text-container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-link-text-container']")))
    print('PASS - step 689')
except Exception as e:
    print('FAIL - step 689' if isinstance(e, AssertionError) else f'ERROR - step 689: {e}')

print("STEP 690 - Check element span#None.['globalnav-image-regular', 'globalnav-link-image']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-image-regular', 'globalnav-link-image']")))
    print('PASS - step 690')
except Exception as e:
    print('FAIL - step 690' if isinstance(e, AssertionError) else f'ERROR - step 690: {e}')

print("STEP 691 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 691')
except Exception as e:
    print('FAIL - step 691' if isinstance(e, AssertionError) else f'ERROR - step 691: {e}')

print("STEP 692 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 692')
except Exception as e:
    print('FAIL - step 692' if isinstance(e, AssertionError) else f'ERROR - step 692: {e}')

print("STEP 693 - Check element span#None.['globalnav-link-text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-link-text']")))
    print('PASS - step 693')
except Exception as e:
    print('FAIL - step 693' if isinstance(e, AssertionError) else f'ERROR - step 693: {e}')

print("STEP 694 - Check element span#None.['globalnav-link-chevron']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-link-chevron']")))
    print('PASS - step 694')
except Exception as e:
    print('FAIL - step 694' if isinstance(e, AssertionError) else f'ERROR - step 694: {e}')

print("STEP 695 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 695')
except Exception as e:
    print('FAIL - step 695' if isinstance(e, AssertionError) else f'ERROR - step 695: {e}')

print("STEP 696 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 696')
except Exception as e:
    print('FAIL - step 696' if isinstance(e, AssertionError) else f'ERROR - step 696: {e}')

print("STEP 697 - Check element li#None.['globalnav-submenu-trigger-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-trigger-item']")))
    print('PASS - step 697')
except Exception as e:
    print('FAIL - step 697' if isinstance(e, AssertionError) else f'ERROR - step 697: {e}')

print("STEP 698 - Check element button#globalnav-menubutton-link-tv-home.['globalnav-submenu-trigger-button']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "globalnav-menubutton-link-tv-home")))
    print('PASS - step 698')
except Exception as e:
    print('FAIL - step 698' if isinstance(e, AssertionError) else f'ERROR - step 698: {e}')

print("STEP 699 - Check element span#None.['globalnav-image-regular', 'globalnav-submenu-button-icon']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-image-regular', 'globalnav-submenu-button-icon']")))
    print('PASS - step 699')
except Exception as e:
    print('FAIL - step 699' if isinstance(e, AssertionError) else f'ERROR - step 699: {e}')

print("STEP 700 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 700')
except Exception as e:
    print('FAIL - step 700' if isinstance(e, AssertionError) else f'ERROR - step 700: {e}')

print("STEP 701 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 701')
except Exception as e:
    print('FAIL - step 701' if isinstance(e, AssertionError) else f'ERROR - step 701: {e}')

print("STEP 702 - Check element span#None.['globalnav-image-compact', 'globalnav-submenu-button-icon']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-image-compact', 'globalnav-submenu-button-icon']")))
    print('PASS - step 702')
except Exception as e:
    print('FAIL - step 702' if isinstance(e, AssertionError) else f'ERROR - step 702: {e}')

print("STEP 703 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 703')
except Exception as e:
    print('FAIL - step 703' if isinstance(e, AssertionError) else f'ERROR - step 703: {e}')

print("STEP 704 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 704')
except Exception as e:
    print('FAIL - step 704' if isinstance(e, AssertionError) else f'ERROR - step 704: {e}')

print("STEP 705 - Check element div#globalnav-submenu-link-tv-home.['globalnav-flyout', 'globalnav-submenu']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "globalnav-submenu-link-tv-home")))
    print('PASS - step 705')
except Exception as e:
    print('FAIL - step 705' if isinstance(e, AssertionError) else f'ERROR - step 705: {e}')

print("STEP 706 - Check element div#None.['globalnav-flyout-scroll-container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-flyout-scroll-container']")))
    print('PASS - step 706')
except Exception as e:
    print('FAIL - step 706' if isinstance(e, AssertionError) else f'ERROR - step 706: {e}')

print("STEP 707 - Check element div#None.['globalnav-flyout-content', 'globalnav-submenu-content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-flyout-content', 'globalnav-submenu-content']")))
    print('PASS - step 707')
except Exception as e:
    print('FAIL - step 707' if isinstance(e, AssertionError) else f'ERROR - step 707: {e}')

print("STEP 708 - Check element div#None.['globalnav-submenu-group', 'globalnav-submenu-group-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-group', 'globalnav-submenu-group-elevated']")))
    print('PASS - step 708')
except Exception as e:
    print('FAIL - step 708' if isinstance(e, AssertionError) else f'ERROR - step 708: {e}')

print("STEP 709 - Check element h2#97277bad.['globalnav-submenu-header']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "97277bad")))
    print('PASS - step 709')
except Exception as e:
    print('FAIL - step 709' if isinstance(e, AssertionError) else f'ERROR - step 709: {e}')

print("STEP 710 - Check element ul#None.['globalnav-submenu-list']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list']")))
    print('PASS - step 710')
except Exception as e:
    print('FAIL - step 710' if isinstance(e, AssertionError) else f'ERROR - step 710: {e}')

print("STEP 711 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 711')
except Exception as e:
    print('FAIL - step 711' if isinstance(e, AssertionError) else f'ERROR - step 711: {e}')

print("STEP 712 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 712')
except Exception as e:
    print('FAIL - step 712' if isinstance(e, AssertionError) else f'ERROR - step 712: {e}')

print("STEP 713 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 713')
except Exception as e:
    print('FAIL - step 713' if isinstance(e, AssertionError) else f'ERROR - step 713: {e}')

print("STEP 714 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 714')
except Exception as e:
    print('FAIL - step 714' if isinstance(e, AssertionError) else f'ERROR - step 714: {e}')

print("STEP 715 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 715')
except Exception as e:
    print('FAIL - step 715' if isinstance(e, AssertionError) else f'ERROR - step 715: {e}')

print("STEP 716 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 716')
except Exception as e:
    print('FAIL - step 716' if isinstance(e, AssertionError) else f'ERROR - step 716: {e}')

print("STEP 717 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 717')
except Exception as e:
    print('FAIL - step 717' if isinstance(e, AssertionError) else f'ERROR - step 717: {e}')

print("STEP 718 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 718')
except Exception as e:
    print('FAIL - step 718' if isinstance(e, AssertionError) else f'ERROR - step 718: {e}')

print("STEP 719 - Check element div#None.['globalnav-submenu-group']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-group']")))
    print('PASS - step 719')
except Exception as e:
    print('FAIL - step 719' if isinstance(e, AssertionError) else f'ERROR - step 719: {e}')

print("STEP 720 - Check element h2#5b6ea146.['globalnav-submenu-header']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "5b6ea146")))
    print('PASS - step 720')
except Exception as e:
    print('FAIL - step 720' if isinstance(e, AssertionError) else f'ERROR - step 720: {e}')

print("STEP 721 - Check element ul#None.['globalnav-submenu-list']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list']")))
    print('PASS - step 721')
except Exception as e:
    print('FAIL - step 721' if isinstance(e, AssertionError) else f'ERROR - step 721: {e}')

print("STEP 722 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 722')
except Exception as e:
    print('FAIL - step 722' if isinstance(e, AssertionError) else f'ERROR - step 722: {e}')

print("STEP 723 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 723')
except Exception as e:
    print('FAIL - step 723' if isinstance(e, AssertionError) else f'ERROR - step 723: {e}')

print("STEP 724 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 724')
except Exception as e:
    print('FAIL - step 724' if isinstance(e, AssertionError) else f'ERROR - step 724: {e}')

print("STEP 725 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 725')
except Exception as e:
    print('FAIL - step 725' if isinstance(e, AssertionError) else f'ERROR - step 725: {e}')

print("STEP 726 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 726')
except Exception as e:
    print('FAIL - step 726' if isinstance(e, AssertionError) else f'ERROR - step 726: {e}')

print("STEP 727 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 727')
except Exception as e:
    print('FAIL - step 727' if isinstance(e, AssertionError) else f'ERROR - step 727: {e}')

print("STEP 728 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 728')
except Exception as e:
    print('FAIL - step 728' if isinstance(e, AssertionError) else f'ERROR - step 728: {e}')

print("STEP 729 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 729')
except Exception as e:
    print('FAIL - step 729' if isinstance(e, AssertionError) else f'ERROR - step 729: {e}')

print("STEP 730 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 730')
except Exception as e:
    print('FAIL - step 730' if isinstance(e, AssertionError) else f'ERROR - step 730: {e}')

print("STEP 731 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 731')
except Exception as e:
    print('FAIL - step 731' if isinstance(e, AssertionError) else f'ERROR - step 731: {e}')

print("STEP 732 - Check element div#None.['globalnav-submenu-group']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-group']")))
    print('PASS - step 732')
except Exception as e:
    print('FAIL - step 732' if isinstance(e, AssertionError) else f'ERROR - step 732: {e}')

print("STEP 733 - Check element h2#bc65e244.['globalnav-submenu-header']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "bc65e244")))
    print('PASS - step 733')
except Exception as e:
    print('FAIL - step 733' if isinstance(e, AssertionError) else f'ERROR - step 733: {e}')

print("STEP 734 - Check element ul#None.['globalnav-submenu-list']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list']")))
    print('PASS - step 734')
except Exception as e:
    print('FAIL - step 734' if isinstance(e, AssertionError) else f'ERROR - step 734: {e}')

print("STEP 735 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 735')
except Exception as e:
    print('FAIL - step 735' if isinstance(e, AssertionError) else f'ERROR - step 735: {e}')

print("STEP 736 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 736')
except Exception as e:
    print('FAIL - step 736' if isinstance(e, AssertionError) else f'ERROR - step 736: {e}')

print("STEP 737 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 737')
except Exception as e:
    print('FAIL - step 737' if isinstance(e, AssertionError) else f'ERROR - step 737: {e}')

print("STEP 738 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 738')
except Exception as e:
    print('FAIL - step 738' if isinstance(e, AssertionError) else f'ERROR - step 738: {e}')

print("STEP 739 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 739')
except Exception as e:
    print('FAIL - step 739' if isinstance(e, AssertionError) else f'ERROR - step 739: {e}')

print("STEP 740 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 740')
except Exception as e:
    print('FAIL - step 740' if isinstance(e, AssertionError) else f'ERROR - step 740: {e}')

print("STEP 741 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 741')
except Exception as e:
    print('FAIL - step 741' if isinstance(e, AssertionError) else f'ERROR - step 741: {e}')

print("STEP 742 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 742')
except Exception as e:
    print('FAIL - step 742' if isinstance(e, AssertionError) else f'ERROR - step 742: {e}')

print("STEP 743 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 743')
except Exception as e:
    print('FAIL - step 743' if isinstance(e, AssertionError) else f'ERROR - step 743: {e}')

print("STEP 744 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 744')
except Exception as e:
    print('FAIL - step 744' if isinstance(e, AssertionError) else f'ERROR - step 744: {e}')

print("STEP 745 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 745')
except Exception as e:
    print('FAIL - step 745' if isinstance(e, AssertionError) else f'ERROR - step 745: {e}')

print("STEP 746 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 746')
except Exception as e:
    print('FAIL - step 746' if isinstance(e, AssertionError) else f'ERROR - step 746: {e}')

print("STEP 747 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 747')
except Exception as e:
    print('FAIL - step 747' if isinstance(e, AssertionError) else f'ERROR - step 747: {e}')

print("STEP 748 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 748')
except Exception as e:
    print('FAIL - step 748' if isinstance(e, AssertionError) else f'ERROR - step 748: {e}')

print("STEP 749 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 749')
except Exception as e:
    print('FAIL - step 749' if isinstance(e, AssertionError) else f'ERROR - step 749: {e}')

print("STEP 750 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 750')
except Exception as e:
    print('FAIL - step 750' if isinstance(e, AssertionError) else f'ERROR - step 750: {e}')

print("STEP 751 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 751')
except Exception as e:
    print('FAIL - step 751' if isinstance(e, AssertionError) else f'ERROR - step 751: {e}')

print("STEP 752 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 752')
except Exception as e:
    print('FAIL - step 752' if isinstance(e, AssertionError) else f'ERROR - step 752: {e}')

print("STEP 753 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 753')
except Exception as e:
    print('FAIL - step 753' if isinstance(e, AssertionError) else f'ERROR - step 753: {e}')

print("STEP 754 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 754')
except Exception as e:
    print('FAIL - step 754' if isinstance(e, AssertionError) else f'ERROR - step 754: {e}')

print("STEP 755 - Check element div#None.['globalnav-item', 'globalnav-item-entertainment', 'globalnav-item-menu', 'globalnav-item-submenu']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-item', 'globalnav-item-entertainment', 'globalnav-item-menu', 'globalnav-item-submenu']")))
    print('PASS - step 755')
except Exception as e:
    print('FAIL - step 755' if isinstance(e, AssertionError) else f'ERROR - step 755: {e}')

print("STEP 756 - Check element ul#None.['globalnav-submenu-trigger-group']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-trigger-group']")))
    print('PASS - step 756')
except Exception as e:
    print('FAIL - step 756' if isinstance(e, AssertionError) else f'ERROR - step 756: {e}')

print("STEP 757 - Check element li#None.['globalnav-submenu-trigger-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-trigger-item']")))
    print('PASS - step 757')
except Exception as e:
    print('FAIL - step 757' if isinstance(e, AssertionError) else f'ERROR - step 757: {e}')

print("STEP 758 - Check element a#None.['globalnav-link', 'globalnav-submenu-trigger-link', 'globalnav-link-entertainment']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-link', 'globalnav-submenu-trigger-link', 'globalnav-link-entertainment']")))
    print('PASS - step 758')
except Exception as e:
    print('FAIL - step 758' if isinstance(e, AssertionError) else f'ERROR - step 758: {e}')

print("STEP 759 - Check element span#None.['globalnav-link-text-container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-link-text-container']")))
    print('PASS - step 759')
except Exception as e:
    print('FAIL - step 759' if isinstance(e, AssertionError) else f'ERROR - step 759: {e}')

print("STEP 760 - Check element span#None.['globalnav-image-regular', 'globalnav-link-image']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-image-regular', 'globalnav-link-image']")))
    print('PASS - step 760')
except Exception as e:
    print('FAIL - step 760' if isinstance(e, AssertionError) else f'ERROR - step 760: {e}')

print("STEP 761 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 761')
except Exception as e:
    print('FAIL - step 761' if isinstance(e, AssertionError) else f'ERROR - step 761: {e}')

print("STEP 762 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 762')
except Exception as e:
    print('FAIL - step 762' if isinstance(e, AssertionError) else f'ERROR - step 762: {e}')

print("STEP 763 - Check element span#None.['globalnav-link-text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-link-text']")))
    print('PASS - step 763')
except Exception as e:
    print('FAIL - step 763' if isinstance(e, AssertionError) else f'ERROR - step 763: {e}')

print("STEP 764 - Check element span#None.['globalnav-link-chevron']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-link-chevron']")))
    print('PASS - step 764')
except Exception as e:
    print('FAIL - step 764' if isinstance(e, AssertionError) else f'ERROR - step 764: {e}')

print("STEP 765 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 765')
except Exception as e:
    print('FAIL - step 765' if isinstance(e, AssertionError) else f'ERROR - step 765: {e}')

print("STEP 766 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 766')
except Exception as e:
    print('FAIL - step 766' if isinstance(e, AssertionError) else f'ERROR - step 766: {e}')

print("STEP 767 - Check element li#None.['globalnav-submenu-trigger-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-trigger-item']")))
    print('PASS - step 767')
except Exception as e:
    print('FAIL - step 767' if isinstance(e, AssertionError) else f'ERROR - step 767: {e}')

print("STEP 768 - Check element button#globalnav-menubutton-link-entertainment.['globalnav-submenu-trigger-button']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "globalnav-menubutton-link-entertainment")))
    print('PASS - step 768')
except Exception as e:
    print('FAIL - step 768' if isinstance(e, AssertionError) else f'ERROR - step 768: {e}')

print("STEP 769 - Check element span#None.['globalnav-image-regular', 'globalnav-submenu-button-icon']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-image-regular', 'globalnav-submenu-button-icon']")))
    print('PASS - step 769')
except Exception as e:
    print('FAIL - step 769' if isinstance(e, AssertionError) else f'ERROR - step 769: {e}')

print("STEP 770 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 770')
except Exception as e:
    print('FAIL - step 770' if isinstance(e, AssertionError) else f'ERROR - step 770: {e}')

print("STEP 771 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 771')
except Exception as e:
    print('FAIL - step 771' if isinstance(e, AssertionError) else f'ERROR - step 771: {e}')

print("STEP 772 - Check element span#None.['globalnav-image-compact', 'globalnav-submenu-button-icon']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-image-compact', 'globalnav-submenu-button-icon']")))
    print('PASS - step 772')
except Exception as e:
    print('FAIL - step 772' if isinstance(e, AssertionError) else f'ERROR - step 772: {e}')

print("STEP 773 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 773')
except Exception as e:
    print('FAIL - step 773' if isinstance(e, AssertionError) else f'ERROR - step 773: {e}')

print("STEP 774 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 774')
except Exception as e:
    print('FAIL - step 774' if isinstance(e, AssertionError) else f'ERROR - step 774: {e}')

print("STEP 775 - Check element div#globalnav-submenu-link-entertainment.['globalnav-flyout', 'globalnav-submenu']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "globalnav-submenu-link-entertainment")))
    print('PASS - step 775')
except Exception as e:
    print('FAIL - step 775' if isinstance(e, AssertionError) else f'ERROR - step 775: {e}')

print("STEP 776 - Check element div#None.['globalnav-flyout-scroll-container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-flyout-scroll-container']")))
    print('PASS - step 776')
except Exception as e:
    print('FAIL - step 776' if isinstance(e, AssertionError) else f'ERROR - step 776: {e}')

print("STEP 777 - Check element div#None.['globalnav-flyout-content', 'globalnav-submenu-content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-flyout-content', 'globalnav-submenu-content']")))
    print('PASS - step 777')
except Exception as e:
    print('FAIL - step 777' if isinstance(e, AssertionError) else f'ERROR - step 777: {e}')

print("STEP 778 - Check element div#None.['globalnav-submenu-group', 'globalnav-submenu-group-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-group', 'globalnav-submenu-group-elevated']")))
    print('PASS - step 778')
except Exception as e:
    print('FAIL - step 778' if isinstance(e, AssertionError) else f'ERROR - step 778: {e}')

print("STEP 779 - Check element h2#186ff7b2.['globalnav-submenu-header']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "186ff7b2")))
    print('PASS - step 779')
except Exception as e:
    print('FAIL - step 779' if isinstance(e, AssertionError) else f'ERROR - step 779: {e}')

print("STEP 780 - Check element ul#None.['globalnav-submenu-list']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list']")))
    print('PASS - step 780')
except Exception as e:
    print('FAIL - step 780' if isinstance(e, AssertionError) else f'ERROR - step 780: {e}')

print("STEP 781 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 781')
except Exception as e:
    print('FAIL - step 781' if isinstance(e, AssertionError) else f'ERROR - step 781: {e}')

print("STEP 782 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 782')
except Exception as e:
    print('FAIL - step 782' if isinstance(e, AssertionError) else f'ERROR - step 782: {e}')

print("STEP 783 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 783')
except Exception as e:
    print('FAIL - step 783' if isinstance(e, AssertionError) else f'ERROR - step 783: {e}')

print("STEP 784 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 784')
except Exception as e:
    print('FAIL - step 784' if isinstance(e, AssertionError) else f'ERROR - step 784: {e}')

print("STEP 785 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 785')
except Exception as e:
    print('FAIL - step 785' if isinstance(e, AssertionError) else f'ERROR - step 785: {e}')

print("STEP 786 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 786')
except Exception as e:
    print('FAIL - step 786' if isinstance(e, AssertionError) else f'ERROR - step 786: {e}')

print("STEP 787 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 787')
except Exception as e:
    print('FAIL - step 787' if isinstance(e, AssertionError) else f'ERROR - step 787: {e}')

print("STEP 788 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 788')
except Exception as e:
    print('FAIL - step 788' if isinstance(e, AssertionError) else f'ERROR - step 788: {e}')

print("STEP 789 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 789')
except Exception as e:
    print('FAIL - step 789' if isinstance(e, AssertionError) else f'ERROR - step 789: {e}')

print("STEP 790 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 790')
except Exception as e:
    print('FAIL - step 790' if isinstance(e, AssertionError) else f'ERROR - step 790: {e}')

print("STEP 791 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 791')
except Exception as e:
    print('FAIL - step 791' if isinstance(e, AssertionError) else f'ERROR - step 791: {e}')

print("STEP 792 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 792')
except Exception as e:
    print('FAIL - step 792' if isinstance(e, AssertionError) else f'ERROR - step 792: {e}')

print("STEP 793 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 793')
except Exception as e:
    print('FAIL - step 793' if isinstance(e, AssertionError) else f'ERROR - step 793: {e}')

print("STEP 794 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 794')
except Exception as e:
    print('FAIL - step 794' if isinstance(e, AssertionError) else f'ERROR - step 794: {e}')

print("STEP 795 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 795')
except Exception as e:
    print('FAIL - step 795' if isinstance(e, AssertionError) else f'ERROR - step 795: {e}')

print("STEP 796 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 796')
except Exception as e:
    print('FAIL - step 796' if isinstance(e, AssertionError) else f'ERROR - step 796: {e}')

print("STEP 797 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 797')
except Exception as e:
    print('FAIL - step 797' if isinstance(e, AssertionError) else f'ERROR - step 797: {e}')

print("STEP 798 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 798')
except Exception as e:
    print('FAIL - step 798' if isinstance(e, AssertionError) else f'ERROR - step 798: {e}')

print("STEP 799 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 799')
except Exception as e:
    print('FAIL - step 799' if isinstance(e, AssertionError) else f'ERROR - step 799: {e}')

print("STEP 800 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 800')
except Exception as e:
    print('FAIL - step 800' if isinstance(e, AssertionError) else f'ERROR - step 800: {e}')

print("STEP 801 - Check element div#None.['globalnav-submenu-group']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-group']")))
    print('PASS - step 801')
except Exception as e:
    print('FAIL - step 801' if isinstance(e, AssertionError) else f'ERROR - step 801: {e}')

print("STEP 802 - Check element h2#8b3746a6.['globalnav-submenu-header']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "8b3746a6")))
    print('PASS - step 802')
except Exception as e:
    print('FAIL - step 802' if isinstance(e, AssertionError) else f'ERROR - step 802: {e}')

print("STEP 803 - Check element ul#None.['globalnav-submenu-list']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list']")))
    print('PASS - step 803')
except Exception as e:
    print('FAIL - step 803' if isinstance(e, AssertionError) else f'ERROR - step 803: {e}')

print("STEP 804 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 804')
except Exception as e:
    print('FAIL - step 804' if isinstance(e, AssertionError) else f'ERROR - step 804: {e}')

print("STEP 805 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 805')
except Exception as e:
    print('FAIL - step 805' if isinstance(e, AssertionError) else f'ERROR - step 805: {e}')

print("STEP 806 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 806')
except Exception as e:
    print('FAIL - step 806' if isinstance(e, AssertionError) else f'ERROR - step 806: {e}')

print("STEP 807 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 807')
except Exception as e:
    print('FAIL - step 807' if isinstance(e, AssertionError) else f'ERROR - step 807: {e}')

print("STEP 808 - Check element div#None.['globalnav-item', 'globalnav-item-accessories', 'globalnav-item-menu', 'globalnav-item-submenu']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-item', 'globalnav-item-accessories', 'globalnav-item-menu', 'globalnav-item-submenu']")))
    print('PASS - step 808')
except Exception as e:
    print('FAIL - step 808' if isinstance(e, AssertionError) else f'ERROR - step 808: {e}')

print("STEP 809 - Check element ul#None.['globalnav-submenu-trigger-group']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-trigger-group']")))
    print('PASS - step 809')
except Exception as e:
    print('FAIL - step 809' if isinstance(e, AssertionError) else f'ERROR - step 809: {e}')

print("STEP 810 - Check element li#None.['globalnav-submenu-trigger-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-trigger-item']")))
    print('PASS - step 810')
except Exception as e:
    print('FAIL - step 810' if isinstance(e, AssertionError) else f'ERROR - step 810: {e}')

print("STEP 811 - Check element a#None.['globalnav-link', 'globalnav-submenu-trigger-link', 'globalnav-link-accessories']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-link', 'globalnav-submenu-trigger-link', 'globalnav-link-accessories']")))
    print('PASS - step 811')
except Exception as e:
    print('FAIL - step 811' if isinstance(e, AssertionError) else f'ERROR - step 811: {e}')

print("STEP 812 - Check element span#None.['globalnav-link-text-container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-link-text-container']")))
    print('PASS - step 812')
except Exception as e:
    print('FAIL - step 812' if isinstance(e, AssertionError) else f'ERROR - step 812: {e}')

print("STEP 813 - Check element span#None.['globalnav-image-regular', 'globalnav-link-image']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-image-regular', 'globalnav-link-image']")))
    print('PASS - step 813')
except Exception as e:
    print('FAIL - step 813' if isinstance(e, AssertionError) else f'ERROR - step 813: {e}')

print("STEP 814 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 814')
except Exception as e:
    print('FAIL - step 814' if isinstance(e, AssertionError) else f'ERROR - step 814: {e}')

print("STEP 815 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 815')
except Exception as e:
    print('FAIL - step 815' if isinstance(e, AssertionError) else f'ERROR - step 815: {e}')

print("STEP 816 - Check element span#None.['globalnav-link-text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-link-text']")))
    print('PASS - step 816')
except Exception as e:
    print('FAIL - step 816' if isinstance(e, AssertionError) else f'ERROR - step 816: {e}')

print("STEP 817 - Check element span#None.['globalnav-link-chevron']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-link-chevron']")))
    print('PASS - step 817')
except Exception as e:
    print('FAIL - step 817' if isinstance(e, AssertionError) else f'ERROR - step 817: {e}')

print("STEP 818 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 818')
except Exception as e:
    print('FAIL - step 818' if isinstance(e, AssertionError) else f'ERROR - step 818: {e}')

print("STEP 819 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 819')
except Exception as e:
    print('FAIL - step 819' if isinstance(e, AssertionError) else f'ERROR - step 819: {e}')

print("STEP 820 - Check element li#None.['globalnav-submenu-trigger-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-trigger-item']")))
    print('PASS - step 820')
except Exception as e:
    print('FAIL - step 820' if isinstance(e, AssertionError) else f'ERROR - step 820: {e}')

print("STEP 821 - Check element button#globalnav-menubutton-link-accessories.['globalnav-submenu-trigger-button']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "globalnav-menubutton-link-accessories")))
    print('PASS - step 821')
except Exception as e:
    print('FAIL - step 821' if isinstance(e, AssertionError) else f'ERROR - step 821: {e}')

print("STEP 822 - Check element span#None.['globalnav-image-regular', 'globalnav-submenu-button-icon']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-image-regular', 'globalnav-submenu-button-icon']")))
    print('PASS - step 822')
except Exception as e:
    print('FAIL - step 822' if isinstance(e, AssertionError) else f'ERROR - step 822: {e}')

print("STEP 823 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 823')
except Exception as e:
    print('FAIL - step 823' if isinstance(e, AssertionError) else f'ERROR - step 823: {e}')

print("STEP 824 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 824')
except Exception as e:
    print('FAIL - step 824' if isinstance(e, AssertionError) else f'ERROR - step 824: {e}')

print("STEP 825 - Check element span#None.['globalnav-image-compact', 'globalnav-submenu-button-icon']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-image-compact', 'globalnav-submenu-button-icon']")))
    print('PASS - step 825')
except Exception as e:
    print('FAIL - step 825' if isinstance(e, AssertionError) else f'ERROR - step 825: {e}')

print("STEP 826 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 826')
except Exception as e:
    print('FAIL - step 826' if isinstance(e, AssertionError) else f'ERROR - step 826: {e}')

print("STEP 827 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 827')
except Exception as e:
    print('FAIL - step 827' if isinstance(e, AssertionError) else f'ERROR - step 827: {e}')

print("STEP 828 - Check element div#globalnav-submenu-link-accessories.['globalnav-flyout', 'globalnav-submenu']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "globalnav-submenu-link-accessories")))
    print('PASS - step 828')
except Exception as e:
    print('FAIL - step 828' if isinstance(e, AssertionError) else f'ERROR - step 828: {e}')

print("STEP 829 - Check element div#None.['globalnav-flyout-scroll-container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-flyout-scroll-container']")))
    print('PASS - step 829')
except Exception as e:
    print('FAIL - step 829' if isinstance(e, AssertionError) else f'ERROR - step 829: {e}')

print("STEP 830 - Check element div#None.['globalnav-flyout-content', 'globalnav-submenu-content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-flyout-content', 'globalnav-submenu-content']")))
    print('PASS - step 830')
except Exception as e:
    print('FAIL - step 830' if isinstance(e, AssertionError) else f'ERROR - step 830: {e}')

print("STEP 831 - Check element div#None.['globalnav-submenu-group', 'globalnav-submenu-group-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-group', 'globalnav-submenu-group-elevated']")))
    print('PASS - step 831')
except Exception as e:
    print('FAIL - step 831' if isinstance(e, AssertionError) else f'ERROR - step 831: {e}')

print("STEP 832 - Check element h2#3de481ed.['globalnav-submenu-header']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "3de481ed")))
    print('PASS - step 832')
except Exception as e:
    print('FAIL - step 832' if isinstance(e, AssertionError) else f'ERROR - step 832: {e}')

print("STEP 833 - Check element ul#None.['globalnav-submenu-list']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list']")))
    print('PASS - step 833')
except Exception as e:
    print('FAIL - step 833' if isinstance(e, AssertionError) else f'ERROR - step 833: {e}')

print("STEP 834 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 834')
except Exception as e:
    print('FAIL - step 834' if isinstance(e, AssertionError) else f'ERROR - step 834: {e}')

print("STEP 835 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 835')
except Exception as e:
    print('FAIL - step 835' if isinstance(e, AssertionError) else f'ERROR - step 835: {e}')

print("STEP 836 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 836')
except Exception as e:
    print('FAIL - step 836' if isinstance(e, AssertionError) else f'ERROR - step 836: {e}')

print("STEP 837 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 837')
except Exception as e:
    print('FAIL - step 837' if isinstance(e, AssertionError) else f'ERROR - step 837: {e}')

print("STEP 838 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 838')
except Exception as e:
    print('FAIL - step 838' if isinstance(e, AssertionError) else f'ERROR - step 838: {e}')

print("STEP 839 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 839')
except Exception as e:
    print('FAIL - step 839' if isinstance(e, AssertionError) else f'ERROR - step 839: {e}')

print("STEP 840 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 840')
except Exception as e:
    print('FAIL - step 840' if isinstance(e, AssertionError) else f'ERROR - step 840: {e}')

print("STEP 841 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 841')
except Exception as e:
    print('FAIL - step 841' if isinstance(e, AssertionError) else f'ERROR - step 841: {e}')

print("STEP 842 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 842')
except Exception as e:
    print('FAIL - step 842' if isinstance(e, AssertionError) else f'ERROR - step 842: {e}')

print("STEP 843 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 843')
except Exception as e:
    print('FAIL - step 843' if isinstance(e, AssertionError) else f'ERROR - step 843: {e}')

print("STEP 844 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 844')
except Exception as e:
    print('FAIL - step 844' if isinstance(e, AssertionError) else f'ERROR - step 844: {e}')

print("STEP 845 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 845')
except Exception as e:
    print('FAIL - step 845' if isinstance(e, AssertionError) else f'ERROR - step 845: {e}')

print("STEP 846 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 846')
except Exception as e:
    print('FAIL - step 846' if isinstance(e, AssertionError) else f'ERROR - step 846: {e}')

print("STEP 847 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 847')
except Exception as e:
    print('FAIL - step 847' if isinstance(e, AssertionError) else f'ERROR - step 847: {e}')

print("STEP 848 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 848')
except Exception as e:
    print('FAIL - step 848' if isinstance(e, AssertionError) else f'ERROR - step 848: {e}')

print("STEP 849 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 849')
except Exception as e:
    print('FAIL - step 849' if isinstance(e, AssertionError) else f'ERROR - step 849: {e}')

print("STEP 850 - Check element div#None.['globalnav-submenu-group']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-group']")))
    print('PASS - step 850')
except Exception as e:
    print('FAIL - step 850' if isinstance(e, AssertionError) else f'ERROR - step 850: {e}')

print("STEP 851 - Check element h2#5d08097b.['globalnav-submenu-header']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "5d08097b")))
    print('PASS - step 851')
except Exception as e:
    print('FAIL - step 851' if isinstance(e, AssertionError) else f'ERROR - step 851: {e}')

print("STEP 852 - Check element ul#None.['globalnav-submenu-list']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list']")))
    print('PASS - step 852')
except Exception as e:
    print('FAIL - step 852' if isinstance(e, AssertionError) else f'ERROR - step 852: {e}')

print("STEP 853 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 853')
except Exception as e:
    print('FAIL - step 853' if isinstance(e, AssertionError) else f'ERROR - step 853: {e}')

print("STEP 854 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 854')
except Exception as e:
    print('FAIL - step 854' if isinstance(e, AssertionError) else f'ERROR - step 854: {e}')

print("STEP 855 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 855')
except Exception as e:
    print('FAIL - step 855' if isinstance(e, AssertionError) else f'ERROR - step 855: {e}')

print("STEP 856 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 856')
except Exception as e:
    print('FAIL - step 856' if isinstance(e, AssertionError) else f'ERROR - step 856: {e}')

print("STEP 857 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 857')
except Exception as e:
    print('FAIL - step 857' if isinstance(e, AssertionError) else f'ERROR - step 857: {e}')

print("STEP 858 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 858')
except Exception as e:
    print('FAIL - step 858' if isinstance(e, AssertionError) else f'ERROR - step 858: {e}')

print("STEP 859 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 859')
except Exception as e:
    print('FAIL - step 859' if isinstance(e, AssertionError) else f'ERROR - step 859: {e}')

print("STEP 860 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 860')
except Exception as e:
    print('FAIL - step 860' if isinstance(e, AssertionError) else f'ERROR - step 860: {e}')

print("STEP 861 - Check element div#None.['globalnav-item', 'globalnav-item-support', 'globalnav-item-menu', 'globalnav-item-submenu']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-item', 'globalnav-item-support', 'globalnav-item-menu', 'globalnav-item-submenu']")))
    print('PASS - step 861')
except Exception as e:
    print('FAIL - step 861' if isinstance(e, AssertionError) else f'ERROR - step 861: {e}')

print("STEP 862 - Check element ul#None.['globalnav-submenu-trigger-group']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-trigger-group']")))
    print('PASS - step 862')
except Exception as e:
    print('FAIL - step 862' if isinstance(e, AssertionError) else f'ERROR - step 862: {e}')

print("STEP 863 - Check element li#None.['globalnav-submenu-trigger-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-trigger-item']")))
    print('PASS - step 863')
except Exception as e:
    print('FAIL - step 863' if isinstance(e, AssertionError) else f'ERROR - step 863: {e}')

print("STEP 864 - Check element a#None.['globalnav-link', 'globalnav-submenu-trigger-link', 'globalnav-link-support']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-link', 'globalnav-submenu-trigger-link', 'globalnav-link-support']")))
    print('PASS - step 864')
except Exception as e:
    print('FAIL - step 864' if isinstance(e, AssertionError) else f'ERROR - step 864: {e}')

print("STEP 865 - Check element span#None.['globalnav-link-text-container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-link-text-container']")))
    print('PASS - step 865')
except Exception as e:
    print('FAIL - step 865' if isinstance(e, AssertionError) else f'ERROR - step 865: {e}')

print("STEP 866 - Check element span#None.['globalnav-image-regular', 'globalnav-link-image']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-image-regular', 'globalnav-link-image']")))
    print('PASS - step 866')
except Exception as e:
    print('FAIL - step 866' if isinstance(e, AssertionError) else f'ERROR - step 866: {e}')

print("STEP 867 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 867')
except Exception as e:
    print('FAIL - step 867' if isinstance(e, AssertionError) else f'ERROR - step 867: {e}')

print("STEP 868 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 868')
except Exception as e:
    print('FAIL - step 868' if isinstance(e, AssertionError) else f'ERROR - step 868: {e}')

print("STEP 869 - Check element span#None.['globalnav-link-text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-link-text']")))
    print('PASS - step 869')
except Exception as e:
    print('FAIL - step 869' if isinstance(e, AssertionError) else f'ERROR - step 869: {e}')

print("STEP 870 - Check element span#None.['globalnav-link-chevron']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-link-chevron']")))
    print('PASS - step 870')
except Exception as e:
    print('FAIL - step 870' if isinstance(e, AssertionError) else f'ERROR - step 870: {e}')

print("STEP 871 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 871')
except Exception as e:
    print('FAIL - step 871' if isinstance(e, AssertionError) else f'ERROR - step 871: {e}')

print("STEP 872 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 872')
except Exception as e:
    print('FAIL - step 872' if isinstance(e, AssertionError) else f'ERROR - step 872: {e}')

print("STEP 873 - Check element li#None.['globalnav-submenu-trigger-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-trigger-item']")))
    print('PASS - step 873')
except Exception as e:
    print('FAIL - step 873' if isinstance(e, AssertionError) else f'ERROR - step 873: {e}')

print("STEP 874 - Check element button#globalnav-menubutton-link-support.['globalnav-submenu-trigger-button']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "globalnav-menubutton-link-support")))
    print('PASS - step 874')
except Exception as e:
    print('FAIL - step 874' if isinstance(e, AssertionError) else f'ERROR - step 874: {e}')

print("STEP 875 - Check element span#None.['globalnav-image-regular', 'globalnav-submenu-button-icon']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-image-regular', 'globalnav-submenu-button-icon']")))
    print('PASS - step 875')
except Exception as e:
    print('FAIL - step 875' if isinstance(e, AssertionError) else f'ERROR - step 875: {e}')

print("STEP 876 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 876')
except Exception as e:
    print('FAIL - step 876' if isinstance(e, AssertionError) else f'ERROR - step 876: {e}')

print("STEP 877 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 877')
except Exception as e:
    print('FAIL - step 877' if isinstance(e, AssertionError) else f'ERROR - step 877: {e}')

print("STEP 878 - Check element span#None.['globalnav-image-compact', 'globalnav-submenu-button-icon']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-image-compact', 'globalnav-submenu-button-icon']")))
    print('PASS - step 878')
except Exception as e:
    print('FAIL - step 878' if isinstance(e, AssertionError) else f'ERROR - step 878: {e}')

print("STEP 879 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 879')
except Exception as e:
    print('FAIL - step 879' if isinstance(e, AssertionError) else f'ERROR - step 879: {e}')

print("STEP 880 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 880')
except Exception as e:
    print('FAIL - step 880' if isinstance(e, AssertionError) else f'ERROR - step 880: {e}')

print("STEP 881 - Check element div#globalnav-submenu-link-support.['globalnav-flyout', 'globalnav-submenu']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "globalnav-submenu-link-support")))
    print('PASS - step 881')
except Exception as e:
    print('FAIL - step 881' if isinstance(e, AssertionError) else f'ERROR - step 881: {e}')

print("STEP 882 - Check element div#None.['globalnav-flyout-scroll-container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-flyout-scroll-container']")))
    print('PASS - step 882')
except Exception as e:
    print('FAIL - step 882' if isinstance(e, AssertionError) else f'ERROR - step 882: {e}')

print("STEP 883 - Check element div#None.['globalnav-flyout-content', 'globalnav-submenu-content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-flyout-content', 'globalnav-submenu-content']")))
    print('PASS - step 883')
except Exception as e:
    print('FAIL - step 883' if isinstance(e, AssertionError) else f'ERROR - step 883: {e}')

print("STEP 884 - Check element div#None.['globalnav-submenu-group', 'globalnav-submenu-group-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-group', 'globalnav-submenu-group-elevated']")))
    print('PASS - step 884')
except Exception as e:
    print('FAIL - step 884' if isinstance(e, AssertionError) else f'ERROR - step 884: {e}')

print("STEP 885 - Check element h2#a048495e.['globalnav-submenu-header']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "a048495e")))
    print('PASS - step 885')
except Exception as e:
    print('FAIL - step 885' if isinstance(e, AssertionError) else f'ERROR - step 885: {e}')

print("STEP 886 - Check element ul#None.['globalnav-submenu-list']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list']")))
    print('PASS - step 886')
except Exception as e:
    print('FAIL - step 886' if isinstance(e, AssertionError) else f'ERROR - step 886: {e}')

print("STEP 887 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 887')
except Exception as e:
    print('FAIL - step 887' if isinstance(e, AssertionError) else f'ERROR - step 887: {e}')

print("STEP 888 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 888')
except Exception as e:
    print('FAIL - step 888' if isinstance(e, AssertionError) else f'ERROR - step 888: {e}')

print("STEP 889 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 889')
except Exception as e:
    print('FAIL - step 889' if isinstance(e, AssertionError) else f'ERROR - step 889: {e}')

print("STEP 890 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 890')
except Exception as e:
    print('FAIL - step 890' if isinstance(e, AssertionError) else f'ERROR - step 890: {e}')

print("STEP 891 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 891')
except Exception as e:
    print('FAIL - step 891' if isinstance(e, AssertionError) else f'ERROR - step 891: {e}')

print("STEP 892 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 892')
except Exception as e:
    print('FAIL - step 892' if isinstance(e, AssertionError) else f'ERROR - step 892: {e}')

print("STEP 893 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 893')
except Exception as e:
    print('FAIL - step 893' if isinstance(e, AssertionError) else f'ERROR - step 893: {e}')

print("STEP 894 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 894')
except Exception as e:
    print('FAIL - step 894' if isinstance(e, AssertionError) else f'ERROR - step 894: {e}')

print("STEP 895 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 895')
except Exception as e:
    print('FAIL - step 895' if isinstance(e, AssertionError) else f'ERROR - step 895: {e}')

print("STEP 896 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 896')
except Exception as e:
    print('FAIL - step 896' if isinstance(e, AssertionError) else f'ERROR - step 896: {e}')

print("STEP 897 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 897')
except Exception as e:
    print('FAIL - step 897' if isinstance(e, AssertionError) else f'ERROR - step 897: {e}')

print("STEP 898 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 898')
except Exception as e:
    print('FAIL - step 898' if isinstance(e, AssertionError) else f'ERROR - step 898: {e}')

print("STEP 899 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 899')
except Exception as e:
    print('FAIL - step 899' if isinstance(e, AssertionError) else f'ERROR - step 899: {e}')

print("STEP 900 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 900')
except Exception as e:
    print('FAIL - step 900' if isinstance(e, AssertionError) else f'ERROR - step 900: {e}')

print("STEP 901 - Check element li#None.['globalnav-submenu-list-item-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item-elevated']")))
    print('PASS - step 901')
except Exception as e:
    print('FAIL - step 901' if isinstance(e, AssertionError) else f'ERROR - step 901: {e}')

print("STEP 902 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 902')
except Exception as e:
    print('FAIL - step 902' if isinstance(e, AssertionError) else f'ERROR - step 902: {e}')

print("STEP 903 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 903')
except Exception as e:
    print('FAIL - step 903' if isinstance(e, AssertionError) else f'ERROR - step 903: {e}')

print("STEP 904 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 904')
except Exception as e:
    print('FAIL - step 904' if isinstance(e, AssertionError) else f'ERROR - step 904: {e}')

print("STEP 905 - Check element div#None.['globalnav-submenu-group']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-group']")))
    print('PASS - step 905')
except Exception as e:
    print('FAIL - step 905' if isinstance(e, AssertionError) else f'ERROR - step 905: {e}')

print("STEP 906 - Check element h2#eb3ee958.['globalnav-submenu-header']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "eb3ee958")))
    print('PASS - step 906')
except Exception as e:
    print('FAIL - step 906' if isinstance(e, AssertionError) else f'ERROR - step 906: {e}')

print("STEP 907 - Check element ul#None.['globalnav-submenu-list']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list']")))
    print('PASS - step 907')
except Exception as e:
    print('FAIL - step 907' if isinstance(e, AssertionError) else f'ERROR - step 907: {e}')

print("STEP 908 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 908')
except Exception as e:
    print('FAIL - step 908' if isinstance(e, AssertionError) else f'ERROR - step 908: {e}')

print("STEP 909 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 909')
except Exception as e:
    print('FAIL - step 909' if isinstance(e, AssertionError) else f'ERROR - step 909: {e}')

print("STEP 910 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 910')
except Exception as e:
    print('FAIL - step 910' if isinstance(e, AssertionError) else f'ERROR - step 910: {e}')

print("STEP 911 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 911')
except Exception as e:
    print('FAIL - step 911' if isinstance(e, AssertionError) else f'ERROR - step 911: {e}')

print("STEP 912 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 912')
except Exception as e:
    print('FAIL - step 912' if isinstance(e, AssertionError) else f'ERROR - step 912: {e}')

print("STEP 913 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 913')
except Exception as e:
    print('FAIL - step 913' if isinstance(e, AssertionError) else f'ERROR - step 913: {e}')

print("STEP 914 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 914')
except Exception as e:
    print('FAIL - step 914' if isinstance(e, AssertionError) else f'ERROR - step 914: {e}')

print("STEP 915 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 915')
except Exception as e:
    print('FAIL - step 915' if isinstance(e, AssertionError) else f'ERROR - step 915: {e}')

print("STEP 916 - Check element div#None.['globalnav-submenu-group']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-group']")))
    print('PASS - step 916')
except Exception as e:
    print('FAIL - step 916' if isinstance(e, AssertionError) else f'ERROR - step 916: {e}')

print("STEP 917 - Check element h2#ac73ce76.['globalnav-submenu-header']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "ac73ce76")))
    print('PASS - step 917')
except Exception as e:
    print('FAIL - step 917' if isinstance(e, AssertionError) else f'ERROR - step 917: {e}')

print("STEP 918 - Check element ul#None.['globalnav-submenu-list']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list']")))
    print('PASS - step 918')
except Exception as e:
    print('FAIL - step 918' if isinstance(e, AssertionError) else f'ERROR - step 918: {e}')

print("STEP 919 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 919')
except Exception as e:
    print('FAIL - step 919' if isinstance(e, AssertionError) else f'ERROR - step 919: {e}')

print("STEP 920 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 920')
except Exception as e:
    print('FAIL - step 920' if isinstance(e, AssertionError) else f'ERROR - step 920: {e}')

print("STEP 921 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 921')
except Exception as e:
    print('FAIL - step 921' if isinstance(e, AssertionError) else f'ERROR - step 921: {e}')

print("STEP 922 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 922')
except Exception as e:
    print('FAIL - step 922' if isinstance(e, AssertionError) else f'ERROR - step 922: {e}')

print("STEP 923 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 923')
except Exception as e:
    print('FAIL - step 923' if isinstance(e, AssertionError) else f'ERROR - step 923: {e}')

print("STEP 924 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 924')
except Exception as e:
    print('FAIL - step 924' if isinstance(e, AssertionError) else f'ERROR - step 924: {e}')

print("STEP 925 - Check element li#None.['globalnav-submenu-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-list-item']")))
    print('PASS - step 925')
except Exception as e:
    print('FAIL - step 925' if isinstance(e, AssertionError) else f'ERROR - step 925: {e}')

print("STEP 926 - Check element a#None.['globalnav-submenu-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-submenu-link']")))
    print('PASS - step 926')
except Exception as e:
    print('FAIL - step 926' if isinstance(e, AssertionError) else f'ERROR - step 926: {e}')

print("STEP 927 - Check element li#None.['globalnav-item', 'globalnav-search', 'shift-0-1']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-item', 'globalnav-search', 'shift-0-1']")))
    print('PASS - step 927')
except Exception as e:
    print('FAIL - step 927' if isinstance(e, AssertionError) else f'ERROR - step 927: {e}')

print("STEP 928 - Check element a#globalnav-menubutton-link-search.['globalnav-link', 'globalnav-link-search']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "globalnav-menubutton-link-search")))
    print('PASS - step 928')
except Exception as e:
    print('FAIL - step 928' if isinstance(e, AssertionError) else f'ERROR - step 928: {e}')

print("STEP 929 - Check element span#None.['globalnav-image-regular']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-image-regular']")))
    print('PASS - step 929')
except Exception as e:
    print('FAIL - step 929' if isinstance(e, AssertionError) else f'ERROR - step 929: {e}')

print("STEP 930 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 930')
except Exception as e:
    print('FAIL - step 930' if isinstance(e, AssertionError) else f'ERROR - step 930: {e}')

print("STEP 931 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 931')
except Exception as e:
    print('FAIL - step 931' if isinstance(e, AssertionError) else f'ERROR - step 931: {e}')

print("STEP 932 - Check element span#None.['globalnav-image-compact']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-image-compact']")))
    print('PASS - step 932')
except Exception as e:
    print('FAIL - step 932' if isinstance(e, AssertionError) else f'ERROR - step 932: {e}')

print("STEP 933 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 933')
except Exception as e:
    print('FAIL - step 933' if isinstance(e, AssertionError) else f'ERROR - step 933: {e}')

print("STEP 934 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 934')
except Exception as e:
    print('FAIL - step 934' if isinstance(e, AssertionError) else f'ERROR - step 934: {e}')

print("STEP 935 - Check element div#globalnav-submenu-search.['globalnav-flyout', 'globalnav-submenu']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "globalnav-submenu-search")))
    print('PASS - step 935')
except Exception as e:
    print('FAIL - step 935' if isinstance(e, AssertionError) else f'ERROR - step 935: {e}')

print("STEP 936 - Check element div#None.['globalnav-flyout-scroll-container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-flyout-scroll-container']")))
    print('PASS - step 936')
except Exception as e:
    print('FAIL - step 936' if isinstance(e, AssertionError) else f'ERROR - step 936: {e}')

print("STEP 937 - Check element div#None.['globalnav-flyout-content', 'globalnav-submenu-content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-flyout-content', 'globalnav-submenu-content']")))
    print('PASS - step 937')
except Exception as e:
    print('FAIL - step 937' if isinstance(e, AssertionError) else f'ERROR - step 937: {e}')

print("STEP 938 - Check element form#None.['globalnav-searchfield']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-searchfield']")))
    print('PASS - step 938')
except Exception as e:
    print('FAIL - step 938' if isinstance(e, AssertionError) else f'ERROR - step 938: {e}')

print("STEP 939 - Check element div#None.['globalnav-searchfield-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-searchfield-wrapper']")))
    print('PASS - step 939')
except Exception as e:
    print('FAIL - step 939' if isinstance(e, AssertionError) else f'ERROR - step 939: {e}')

print("STEP 940 - Check element input#None.['globalnav-searchfield-input']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-searchfield-input']")))
    print('PASS - step 940')
except Exception as e:
    print('FAIL - step 940' if isinstance(e, AssertionError) else f'ERROR - step 940: {e}')

print("STEP 941 - Check element input#globalnav-searchfield-src.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "globalnav-searchfield-src")))
    print('PASS - step 941')
except Exception as e:
    print('FAIL - step 941' if isinstance(e, AssertionError) else f'ERROR - step 941: {e}')

print("STEP 942 - Check element button#None.['globalnav-searchfield-reset']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-searchfield-reset']")))
    print('PASS - step 942')
except Exception as e:
    print('FAIL - step 942' if isinstance(e, AssertionError) else f'ERROR - step 942: {e}')

print("STEP 943 - Check element span#None.['globalnav-image-regular']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-image-regular']")))
    print('PASS - step 943')
except Exception as e:
    print('FAIL - step 943' if isinstance(e, AssertionError) else f'ERROR - step 943: {e}')

print("STEP 944 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 944')
except Exception as e:
    print('FAIL - step 944' if isinstance(e, AssertionError) else f'ERROR - step 944: {e}')

print("STEP 945 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 945')
except Exception as e:
    print('FAIL - step 945' if isinstance(e, AssertionError) else f'ERROR - step 945: {e}')

print("STEP 946 - Check element span#None.['globalnav-image-compact']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-image-compact']")))
    print('PASS - step 946')
except Exception as e:
    print('FAIL - step 946' if isinstance(e, AssertionError) else f'ERROR - step 946: {e}')

print("STEP 947 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 947')
except Exception as e:
    print('FAIL - step 947' if isinstance(e, AssertionError) else f'ERROR - step 947: {e}')

print("STEP 948 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 948')
except Exception as e:
    print('FAIL - step 948' if isinstance(e, AssertionError) else f'ERROR - step 948: {e}')

print("STEP 949 - Check element button#None.['globalnav-searchfield-submit']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-searchfield-submit']")))
    print('PASS - step 949')
except Exception as e:
    print('FAIL - step 949' if isinstance(e, AssertionError) else f'ERROR - step 949: {e}')

print("STEP 950 - Check element span#None.['globalnav-image-regular']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-image-regular']")))
    print('PASS - step 950')
except Exception as e:
    print('FAIL - step 950' if isinstance(e, AssertionError) else f'ERROR - step 950: {e}')

print("STEP 951 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 951')
except Exception as e:
    print('FAIL - step 951' if isinstance(e, AssertionError) else f'ERROR - step 951: {e}')

print("STEP 952 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 952')
except Exception as e:
    print('FAIL - step 952' if isinstance(e, AssertionError) else f'ERROR - step 952: {e}')

print("STEP 953 - Check element span#None.['globalnav-image-compact']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-image-compact']")))
    print('PASS - step 953')
except Exception as e:
    print('FAIL - step 953' if isinstance(e, AssertionError) else f'ERROR - step 953: {e}')

print("STEP 954 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 954')
except Exception as e:
    print('FAIL - step 954' if isinstance(e, AssertionError) else f'ERROR - step 954: {e}')

print("STEP 955 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 955')
except Exception as e:
    print('FAIL - step 955' if isinstance(e, AssertionError) else f'ERROR - step 955: {e}')

print("STEP 956 - Check element div#None.['globalnav-searchresults-count']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-searchresults-count']")))
    print('PASS - step 956')
except Exception as e:
    print('FAIL - step 956' if isinstance(e, AssertionError) else f'ERROR - step 956: {e}')

print("STEP 957 - Check element div#None.['globalnav-searchresults']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-searchresults']")))
    print('PASS - step 957')
except Exception as e:
    print('FAIL - step 957' if isinstance(e, AssertionError) else f'ERROR - step 957: {e}')

print("STEP 958 - Check element div#None.['globalnav-searchresults-current']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-searchresults-current']")))
    print('PASS - step 958')
except Exception as e:
    print('FAIL - step 958' if isinstance(e, AssertionError) else f'ERROR - step 958: {e}')

print("STEP 959 - Check element div#None.['globalnav-searchresults-container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-searchresults-container']")))
    print('PASS - step 959')
except Exception as e:
    print('FAIL - step 959' if isinstance(e, AssertionError) else f'ERROR - step 959: {e}')

print("STEP 960 - Check element h2#None.['globalnav-searchresults-header']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-searchresults-header']")))
    print('PASS - step 960')
except Exception as e:
    print('FAIL - step 960' if isinstance(e, AssertionError) else f'ERROR - step 960: {e}')

print("STEP 961 - Check element ul#None.['globalnav-searchresults-list']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-searchresults-list']")))
    print('PASS - step 961')
except Exception as e:
    print('FAIL - step 961' if isinstance(e, AssertionError) else f'ERROR - step 961: {e}')

print("STEP 962 - Check element li#None.['globalnav-searchresults-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-searchresults-list-item']")))
    print('PASS - step 962')
except Exception as e:
    print('FAIL - step 962' if isinstance(e, AssertionError) else f'ERROR - step 962: {e}')

print("STEP 963 - Check element a#None.['globalnav-searchresults-list-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-searchresults-list-link']")))
    print('PASS - step 963')
except Exception as e:
    print('FAIL - step 963' if isinstance(e, AssertionError) else f'ERROR - step 963: {e}')

print("STEP 964 - Check element span#None.['globalnav-searchresults-list-icon']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-searchresults-list-icon']")))
    print('PASS - step 964')
except Exception as e:
    print('FAIL - step 964' if isinstance(e, AssertionError) else f'ERROR - step 964: {e}')

print("STEP 965 - Check element span#None.['globalnav-image-regular', 'globalnav-link-image']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-image-regular', 'globalnav-link-image']")))
    print('PASS - step 965')
except Exception as e:
    print('FAIL - step 965' if isinstance(e, AssertionError) else f'ERROR - step 965: {e}')

print("STEP 966 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 966')
except Exception as e:
    print('FAIL - step 966' if isinstance(e, AssertionError) else f'ERROR - step 966: {e}')

print("STEP 967 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 967')
except Exception as e:
    print('FAIL - step 967' if isinstance(e, AssertionError) else f'ERROR - step 967: {e}')

print("STEP 968 - Check element span#None.['globalnav-image-compact', 'globalnav-link-image']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-image-compact', 'globalnav-link-image']")))
    print('PASS - step 968')
except Exception as e:
    print('FAIL - step 968' if isinstance(e, AssertionError) else f'ERROR - step 968: {e}')

print("STEP 969 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 969')
except Exception as e:
    print('FAIL - step 969' if isinstance(e, AssertionError) else f'ERROR - step 969: {e}')

print("STEP 970 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 970')
except Exception as e:
    print('FAIL - step 970' if isinstance(e, AssertionError) else f'ERROR - step 970: {e}')

print("STEP 971 - Check element span#None.['globalnav-searchresults-list-text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-searchresults-list-text']")))
    print('PASS - step 971')
except Exception as e:
    print('FAIL - step 971' if isinstance(e, AssertionError) else f'ERROR - step 971: {e}')

print("STEP 972 - Check element li#None.['globalnav-searchresults-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-searchresults-list-item']")))
    print('PASS - step 972')
except Exception as e:
    print('FAIL - step 972' if isinstance(e, AssertionError) else f'ERROR - step 972: {e}')

print("STEP 973 - Check element a#None.['globalnav-searchresults-list-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-searchresults-list-link']")))
    print('PASS - step 973')
except Exception as e:
    print('FAIL - step 973' if isinstance(e, AssertionError) else f'ERROR - step 973: {e}')

print("STEP 974 - Check element span#None.['globalnav-searchresults-list-icon']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-searchresults-list-icon']")))
    print('PASS - step 974')
except Exception as e:
    print('FAIL - step 974' if isinstance(e, AssertionError) else f'ERROR - step 974: {e}')

print("STEP 975 - Check element span#None.['globalnav-image-regular', 'globalnav-link-image']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-image-regular', 'globalnav-link-image']")))
    print('PASS - step 975')
except Exception as e:
    print('FAIL - step 975' if isinstance(e, AssertionError) else f'ERROR - step 975: {e}')

print("STEP 976 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 976')
except Exception as e:
    print('FAIL - step 976' if isinstance(e, AssertionError) else f'ERROR - step 976: {e}')

print("STEP 977 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 977')
except Exception as e:
    print('FAIL - step 977' if isinstance(e, AssertionError) else f'ERROR - step 977: {e}')

print("STEP 978 - Check element span#None.['globalnav-image-compact', 'globalnav-link-image']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-image-compact', 'globalnav-link-image']")))
    print('PASS - step 978')
except Exception as e:
    print('FAIL - step 978' if isinstance(e, AssertionError) else f'ERROR - step 978: {e}')

print("STEP 979 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 979')
except Exception as e:
    print('FAIL - step 979' if isinstance(e, AssertionError) else f'ERROR - step 979: {e}')

print("STEP 980 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 980')
except Exception as e:
    print('FAIL - step 980' if isinstance(e, AssertionError) else f'ERROR - step 980: {e}')

print("STEP 981 - Check element span#None.['globalnav-searchresults-list-text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-searchresults-list-text']")))
    print('PASS - step 981')
except Exception as e:
    print('FAIL - step 981' if isinstance(e, AssertionError) else f'ERROR - step 981: {e}')

print("STEP 982 - Check element li#None.['globalnav-searchresults-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-searchresults-list-item']")))
    print('PASS - step 982')
except Exception as e:
    print('FAIL - step 982' if isinstance(e, AssertionError) else f'ERROR - step 982: {e}')

print("STEP 983 - Check element a#None.['globalnav-searchresults-list-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-searchresults-list-link']")))
    print('PASS - step 983')
except Exception as e:
    print('FAIL - step 983' if isinstance(e, AssertionError) else f'ERROR - step 983: {e}')

print("STEP 984 - Check element span#None.['globalnav-searchresults-list-icon']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-searchresults-list-icon']")))
    print('PASS - step 984')
except Exception as e:
    print('FAIL - step 984' if isinstance(e, AssertionError) else f'ERROR - step 984: {e}')

print("STEP 985 - Check element span#None.['globalnav-image-regular', 'globalnav-link-image']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-image-regular', 'globalnav-link-image']")))
    print('PASS - step 985')
except Exception as e:
    print('FAIL - step 985' if isinstance(e, AssertionError) else f'ERROR - step 985: {e}')

print("STEP 986 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 986')
except Exception as e:
    print('FAIL - step 986' if isinstance(e, AssertionError) else f'ERROR - step 986: {e}')

print("STEP 987 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 987')
except Exception as e:
    print('FAIL - step 987' if isinstance(e, AssertionError) else f'ERROR - step 987: {e}')

print("STEP 988 - Check element span#None.['globalnav-image-compact', 'globalnav-link-image']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-image-compact', 'globalnav-link-image']")))
    print('PASS - step 988')
except Exception as e:
    print('FAIL - step 988' if isinstance(e, AssertionError) else f'ERROR - step 988: {e}')

print("STEP 989 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 989')
except Exception as e:
    print('FAIL - step 989' if isinstance(e, AssertionError) else f'ERROR - step 989: {e}')

print("STEP 990 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 990')
except Exception as e:
    print('FAIL - step 990' if isinstance(e, AssertionError) else f'ERROR - step 990: {e}')

print("STEP 991 - Check element span#None.['globalnav-searchresults-list-text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-searchresults-list-text']")))
    print('PASS - step 991')
except Exception as e:
    print('FAIL - step 991' if isinstance(e, AssertionError) else f'ERROR - step 991: {e}')

print("STEP 992 - Check element li#None.['globalnav-searchresults-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-searchresults-list-item']")))
    print('PASS - step 992')
except Exception as e:
    print('FAIL - step 992' if isinstance(e, AssertionError) else f'ERROR - step 992: {e}')

print("STEP 993 - Check element a#None.['globalnav-searchresults-list-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-searchresults-list-link']")))
    print('PASS - step 993')
except Exception as e:
    print('FAIL - step 993' if isinstance(e, AssertionError) else f'ERROR - step 993: {e}')

print("STEP 994 - Check element span#None.['globalnav-searchresults-list-icon']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-searchresults-list-icon']")))
    print('PASS - step 994')
except Exception as e:
    print('FAIL - step 994' if isinstance(e, AssertionError) else f'ERROR - step 994: {e}')

print("STEP 995 - Check element span#None.['globalnav-image-regular', 'globalnav-link-image']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-image-regular', 'globalnav-link-image']")))
    print('PASS - step 995')
except Exception as e:
    print('FAIL - step 995' if isinstance(e, AssertionError) else f'ERROR - step 995: {e}')

print("STEP 996 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 996')
except Exception as e:
    print('FAIL - step 996' if isinstance(e, AssertionError) else f'ERROR - step 996: {e}')

print("STEP 997 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 997')
except Exception as e:
    print('FAIL - step 997' if isinstance(e, AssertionError) else f'ERROR - step 997: {e}')

print("STEP 998 - Check element span#None.['globalnav-image-compact', 'globalnav-link-image']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-image-compact', 'globalnav-link-image']")))
    print('PASS - step 998')
except Exception as e:
    print('FAIL - step 998' if isinstance(e, AssertionError) else f'ERROR - step 998: {e}')

print("STEP 999 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 999')
except Exception as e:
    print('FAIL - step 999' if isinstance(e, AssertionError) else f'ERROR - step 999: {e}')

print("STEP 1000 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 1000')
except Exception as e:
    print('FAIL - step 1000' if isinstance(e, AssertionError) else f'ERROR - step 1000: {e}')

print("STEP 1001 - Check element span#None.['globalnav-searchresults-list-text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-searchresults-list-text']")))
    print('PASS - step 1001')
except Exception as e:
    print('FAIL - step 1001' if isinstance(e, AssertionError) else f'ERROR - step 1001: {e}')

print("STEP 1002 - Check element li#None.['globalnav-searchresults-list-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-searchresults-list-item']")))
    print('PASS - step 1002')
except Exception as e:
    print('FAIL - step 1002' if isinstance(e, AssertionError) else f'ERROR - step 1002: {e}')

print("STEP 1003 - Check element a#None.['globalnav-searchresults-list-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-searchresults-list-link']")))
    print('PASS - step 1003')
except Exception as e:
    print('FAIL - step 1003' if isinstance(e, AssertionError) else f'ERROR - step 1003: {e}')

print("STEP 1004 - Check element span#None.['globalnav-searchresults-list-icon']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-searchresults-list-icon']")))
    print('PASS - step 1004')
except Exception as e:
    print('FAIL - step 1004' if isinstance(e, AssertionError) else f'ERROR - step 1004: {e}')

print("STEP 1005 - Check element span#None.['globalnav-image-regular', 'globalnav-link-image']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-image-regular', 'globalnav-link-image']")))
    print('PASS - step 1005')
except Exception as e:
    print('FAIL - step 1005' if isinstance(e, AssertionError) else f'ERROR - step 1005: {e}')

print("STEP 1006 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 1006')
except Exception as e:
    print('FAIL - step 1006' if isinstance(e, AssertionError) else f'ERROR - step 1006: {e}')

print("STEP 1007 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 1007')
except Exception as e:
    print('FAIL - step 1007' if isinstance(e, AssertionError) else f'ERROR - step 1007: {e}')

print("STEP 1008 - Check element span#None.['globalnav-image-compact', 'globalnav-link-image']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-image-compact', 'globalnav-link-image']")))
    print('PASS - step 1008')
except Exception as e:
    print('FAIL - step 1008' if isinstance(e, AssertionError) else f'ERROR - step 1008: {e}')

print("STEP 1009 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 1009')
except Exception as e:
    print('FAIL - step 1009' if isinstance(e, AssertionError) else f'ERROR - step 1009: {e}')

print("STEP 1010 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 1010')
except Exception as e:
    print('FAIL - step 1010' if isinstance(e, AssertionError) else f'ERROR - step 1010: {e}')

print("STEP 1011 - Check element span#None.['globalnav-searchresults-list-text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-searchresults-list-text']")))
    print('PASS - step 1011')
except Exception as e:
    print('FAIL - step 1011' if isinstance(e, AssertionError) else f'ERROR - step 1011: {e}')

print("STEP 1012 - Check element li#globalnav-bag.['globalnav-item', 'globalnav-bag']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "globalnav-bag")))
    print('PASS - step 1012')
except Exception as e:
    print('FAIL - step 1012' if isinstance(e, AssertionError) else f'ERROR - step 1012: {e}')

print("STEP 1013 - Check element div#None.['globalnav-bag-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-bag-wrapper']")))
    print('PASS - step 1013')
except Exception as e:
    print('FAIL - step 1013' if isinstance(e, AssertionError) else f'ERROR - step 1013: {e}')

print("STEP 1014 - Check element a#globalnav-menubutton-link-bag.['globalnav-link', 'globalnav-link-bag']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "globalnav-menubutton-link-bag")))
    print('PASS - step 1014')
except Exception as e:
    print('FAIL - step 1014' if isinstance(e, AssertionError) else f'ERROR - step 1014: {e}')

print("STEP 1015 - Check element span#None.['globalnav-image-regular']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-image-regular']")))
    print('PASS - step 1015')
except Exception as e:
    print('FAIL - step 1015' if isinstance(e, AssertionError) else f'ERROR - step 1015: {e}')

print("STEP 1016 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 1016')
except Exception as e:
    print('FAIL - step 1016' if isinstance(e, AssertionError) else f'ERROR - step 1016: {e}')

print("STEP 1017 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 1017')
except Exception as e:
    print('FAIL - step 1017' if isinstance(e, AssertionError) else f'ERROR - step 1017: {e}')

print("STEP 1018 - Check element span#None.['globalnav-image-compact']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-image-compact']")))
    print('PASS - step 1018')
except Exception as e:
    print('FAIL - step 1018' if isinstance(e, AssertionError) else f'ERROR - step 1018: {e}')

print("STEP 1019 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 1019')
except Exception as e:
    print('FAIL - step 1019' if isinstance(e, AssertionError) else f'ERROR - step 1019: {e}')

print("STEP 1020 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 1020')
except Exception as e:
    print('FAIL - step 1020' if isinstance(e, AssertionError) else f'ERROR - step 1020: {e}')

print("STEP 1021 - Check element span#None.['globalnav-bag-badge']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-bag-badge']")))
    print('PASS - step 1021')
except Exception as e:
    print('FAIL - step 1021' if isinstance(e, AssertionError) else f'ERROR - step 1021: {e}')

print("STEP 1022 - Check element span#None.['globalnav-bag-badge-separator']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-bag-badge-separator']")))
    print('PASS - step 1022')
except Exception as e:
    print('FAIL - step 1022' if isinstance(e, AssertionError) else f'ERROR - step 1022: {e}')

print("STEP 1023 - Check element span#None.['globalnav-bag-badge-number']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-bag-badge-number']")))
    print('PASS - step 1023')
except Exception as e:
    print('FAIL - step 1023' if isinstance(e, AssertionError) else f'ERROR - step 1023: {e}')

print("STEP 1024 - Check element span#None.['globalnav-bag-badge-unit']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-bag-badge-unit']")))
    print('PASS - step 1024')
except Exception as e:
    print('FAIL - step 1024' if isinstance(e, AssertionError) else f'ERROR - step 1024: {e}')

print("STEP 1025 - Check element div#globalnav-submenu-bag.['globalnav-flyout', 'globalnav-submenu']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "globalnav-submenu-bag")))
    print('PASS - step 1025')
except Exception as e:
    print('FAIL - step 1025' if isinstance(e, AssertionError) else f'ERROR - step 1025: {e}')

print("STEP 1026 - Check element div#None.['globalnav-flyout-scroll-container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-flyout-scroll-container']")))
    print('PASS - step 1026')
except Exception as e:
    print('FAIL - step 1026' if isinstance(e, AssertionError) else f'ERROR - step 1026: {e}')

print("STEP 1027 - Check element div#None.['globalnav-flyout-content', 'globalnav-submenu-content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-flyout-content', 'globalnav-submenu-content']")))
    print('PASS - step 1027')
except Exception as e:
    print('FAIL - step 1027' if isinstance(e, AssertionError) else f'ERROR - step 1027: {e}')

print("STEP 1028 - Check element div#None.['globalnav-menutrigger']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['globalnav-menutrigger']")))
    print('PASS - step 1028')
except Exception as e:
    print('FAIL - step 1028' if isinstance(e, AssertionError) else f'ERROR - step 1028: {e}')

print("STEP 1029 - Check element button#globalnav-menutrigger-button.['globalnav-menutrigger-button']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "globalnav-menutrigger-button")))
    print('PASS - step 1029')
except Exception as e:
    print('FAIL - step 1029' if isinstance(e, AssertionError) else f'ERROR - step 1029: {e}')

print("STEP 1030 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 1030')
except Exception as e:
    print('FAIL - step 1030' if isinstance(e, AssertionError) else f'ERROR - step 1030: {e}')

print("STEP 1031 - Check element polyline#globalnav-menutrigger-bread-bottom.['globalnav-menutrigger-bread', 'globalnav-menutrigger-bread-bottom']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "globalnav-menutrigger-bread-bottom")))
    print('PASS - step 1031')
except Exception as e:
    print('FAIL - step 1031' if isinstance(e, AssertionError) else f'ERROR - step 1031: {e}')

print("STEP 1032 - Check element animate#globalnav-anim-menutrigger-bread-bottom-open.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "globalnav-anim-menutrigger-bread-bottom-open")))
    print('PASS - step 1032')
except Exception as e:
    print('FAIL - step 1032' if isinstance(e, AssertionError) else f'ERROR - step 1032: {e}')

print("STEP 1033 - Check element animate#globalnav-anim-menutrigger-bread-bottom-close.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "globalnav-anim-menutrigger-bread-bottom-close")))
    print('PASS - step 1033')
except Exception as e:
    print('FAIL - step 1033' if isinstance(e, AssertionError) else f'ERROR - step 1033: {e}')

print("STEP 1034 - Check element polyline#globalnav-menutrigger-bread-top.['globalnav-menutrigger-bread', 'globalnav-menutrigger-bread-top']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "globalnav-menutrigger-bread-top")))
    print('PASS - step 1034')
except Exception as e:
    print('FAIL - step 1034' if isinstance(e, AssertionError) else f'ERROR - step 1034: {e}')

print("STEP 1035 - Check element animate#globalnav-anim-menutrigger-bread-top-open.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "globalnav-anim-menutrigger-bread-top-open")))
    print('PASS - step 1035')
except Exception as e:
    print('FAIL - step 1035' if isinstance(e, AssertionError) else f'ERROR - step 1035: {e}')

print("STEP 1036 - Check element animate#globalnav-anim-menutrigger-bread-top-close.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "globalnav-anim-menutrigger-bread-top-close")))
    print('PASS - step 1036')
except Exception as e:
    print('FAIL - step 1036' if isinstance(e, AssertionError) else f'ERROR - step 1036: {e}')

print("STEP 1037 - Check element span#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "span")))
    print('PASS - step 1037')
except Exception as e:
    print('FAIL - step 1037' if isinstance(e, AssertionError) else f'ERROR - step 1037: {e}')

print("STEP 1038 - Check element div#globalnav-curtain.['globalnav-curtain']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "globalnav-curtain")))
    print('PASS - step 1038')
except Exception as e:
    print('FAIL - step 1038' if isinstance(e, AssertionError) else f'ERROR - step 1038: {e}')

print("STEP 1039 - Check element div#globalnav-placeholder.['globalnav-placeholder']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "globalnav-placeholder")))
    print('PASS - step 1039')
except Exception as e:
    print('FAIL - step 1039' if isinstance(e, AssertionError) else f'ERROR - step 1039: {e}')

print("STEP 1040 - Check element script#__ACGH_DATA__.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "__ACGH_DATA__")))
    print('PASS - step 1040')
except Exception as e:
    print('FAIL - step 1040' if isinstance(e, AssertionError) else f'ERROR - step 1040: {e}')

print("STEP 1041 - Check element script#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "script")))
    print('PASS - step 1041')
except Exception as e:
    print('FAIL - step 1041' if isinstance(e, AssertionError) else f'ERROR - step 1041: {e}')

print("STEP 1042 - Check element script#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "script")))
    print('PASS - step 1042')
except Exception as e:
    print('FAIL - step 1042' if isinstance(e, AssertionError) else f'ERROR - step 1042: {e}')

print("STEP 1043 - Check element main#None.['main']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['main']")))
    print('PASS - step 1043')
except Exception as e:
    print('FAIL - step 1043' if isinstance(e, AssertionError) else f'ERROR - step 1043: {e}')

print("STEP 1044 - Check element section#None.['homepage-section', 'collection-module']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['homepage-section', 'collection-module']")))
    print('PASS - step 1044')
except Exception as e:
    print('FAIL - step 1044' if isinstance(e, AssertionError) else f'ERROR - step 1044: {e}')

print("STEP 1045 - Check element div#None.['background-white']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['background-white']")))
    print('PASS - step 1045')
except Exception as e:
    print('FAIL - step 1045' if isinstance(e, AssertionError) else f'ERROR - step 1045: {e}')

print("STEP 1046 - Check element div#None.['module-content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['module-content']")))
    print('PASS - step 1046')
except Exception as e:
    print('FAIL - step 1046' if isinstance(e, AssertionError) else f'ERROR - step 1046: {e}')

print("STEP 1047 - Check element div#None.['ribbon-obdb']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ribbon-obdb']")))
    print('PASS - step 1047')
except Exception as e:
    print('FAIL - step 1047' if isinstance(e, AssertionError) else f'ERROR - step 1047: {e}')

print("STEP 1048 - Check element div#None.['section-content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['section-content']")))
    print('PASS - step 1048')
except Exception as e:
    print('FAIL - step 1048' if isinstance(e, AssertionError) else f'ERROR - step 1048: {e}')

print("STEP 1049 - Check element span#None.['obdb-ribbon-copy']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['obdb-ribbon-copy']")))
    print('PASS - step 1049')
except Exception as e:
    print('FAIL - step 1049' if isinstance(e, AssertionError) else f'ERROR - step 1049: {e}')

print("STEP 1050 - Check element a#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "a")))
    print('PASS - step 1050')
except Exception as e:
    print('FAIL - step 1050' if isinstance(e, AssertionError) else f'ERROR - step 1050: {e}')

print("STEP 1051 - Check element span#None.['icon-copy']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['icon-copy']")))
    print('PASS - step 1051')
except Exception as e:
    print('FAIL - step 1051' if isinstance(e, AssertionError) else f'ERROR - step 1051: {e}')

print("STEP 1052 - Check element span#None.['icon', 'icon-after', 'icon-chevronright']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['icon', 'icon-after', 'icon-chevronright']")))
    print('PASS - step 1052')
except Exception as e:
    print('FAIL - step 1052' if isinstance(e, AssertionError) else f'ERROR - step 1052: {e}')

print("STEP 1053 - Check element section#None.['homepage-section', 'collection-module']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['homepage-section', 'collection-module']")))
    print('PASS - step 1053')
except Exception as e:
    print('FAIL - step 1053' if isinstance(e, AssertionError) else f'ERROR - step 1053: {e}')

print("STEP 1054 - Check element div#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "div")))
    print('PASS - step 1054')
except Exception as e:
    print('FAIL - step 1054' if isinstance(e, AssertionError) else f'ERROR - step 1054: {e}')

print("STEP 1055 - Check element div#None.['module-content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['module-content']")))
    print('PASS - step 1055')
except Exception as e:
    print('FAIL - step 1055' if isinstance(e, AssertionError) else f'ERROR - step 1055: {e}')

print("STEP 1056 - Check element div#None.['unit-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unit-wrapper']")))
    print('PASS - step 1056')
except Exception as e:
    print('FAIL - step 1056' if isinstance(e, AssertionError) else f'ERROR - step 1056: {e}')

print("STEP 1057 - Check element a#None.['unit-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unit-link']")))
    print('PASS - step 1057')
except Exception as e:
    print('FAIL - step 1057' if isinstance(e, AssertionError) else f'ERROR - step 1057: {e}')

print("STEP 1058 - Check element div#None.['unit-copy-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unit-copy-wrapper']")))
    print('PASS - step 1058')
except Exception as e:
    print('FAIL - step 1058' if isinstance(e, AssertionError) else f'ERROR - step 1058: {e}')

print("STEP 1059 - Check element h2#None.['headline']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['headline']")))
    print('PASS - step 1059')
except Exception as e:
    print('FAIL - step 1059' if isinstance(e, AssertionError) else f'ERROR - step 1059: {e}')

print("STEP 1060 - Check element p#None.['subhead']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['subhead']")))
    print('PASS - step 1060')
except Exception as e:
    print('FAIL - step 1060' if isinstance(e, AssertionError) else f'ERROR - step 1060: {e}')

print("STEP 1061 - Check element div#None.['cta-links']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['cta-links']")))
    print('PASS - step 1061')
except Exception as e:
    print('FAIL - step 1061' if isinstance(e, AssertionError) else f'ERROR - step 1061: {e}')

print("STEP 1062 - Check element a#None.['button', 'button-elevated', 'button-primary']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['button', 'button-elevated', 'button-primary']")))
    print('PASS - step 1062')
except Exception as e:
    print('FAIL - step 1062' if isinstance(e, AssertionError) else f'ERROR - step 1062: {e}')

print("STEP 1063 - Check element a#None.['button', 'button-elevated', 'button-tertiary']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['button', 'button-elevated', 'button-tertiary']")))
    print('PASS - step 1063')
except Exception as e:
    print('FAIL - step 1063' if isinstance(e, AssertionError) else f'ERROR - step 1063: {e}')

print("STEP 1064 - Check element div#None.['unit-image-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unit-image-wrapper']")))
    print('PASS - step 1064')
except Exception as e:
    print('FAIL - step 1064' if isinstance(e, AssertionError) else f'ERROR - step 1064: {e}')

print("STEP 1065 - Check element figure#None.['unit-image', 'unit-image-iphone-family-hero-iphone-family']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unit-image', 'unit-image-iphone-family-hero-iphone-family']")))
    print('PASS - step 1065')
except Exception as e:
    print('FAIL - step 1065' if isinstance(e, AssertionError) else f'ERROR - step 1065: {e}')

print("STEP 1066 - Check element div#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "div")))
    print('PASS - step 1066')
except Exception as e:
    print('FAIL - step 1066' if isinstance(e, AssertionError) else f'ERROR - step 1066: {e}')

print("STEP 1067 - Check element div#None.['module-content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['module-content']")))
    print('PASS - step 1067')
except Exception as e:
    print('FAIL - step 1067' if isinstance(e, AssertionError) else f'ERROR - step 1067: {e}')

print("STEP 1068 - Check element div#None.['unit-wrapper', 'bottom-copy-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unit-wrapper', 'bottom-copy-wrapper']")))
    print('PASS - step 1068')
except Exception as e:
    print('FAIL - step 1068' if isinstance(e, AssertionError) else f'ERROR - step 1068: {e}')

print("STEP 1069 - Check element a#None.['unit-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unit-link']")))
    print('PASS - step 1069')
except Exception as e:
    print('FAIL - step 1069' if isinstance(e, AssertionError) else f'ERROR - step 1069: {e}')

print("STEP 1070 - Check element div#None.['unit-copy-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unit-copy-wrapper']")))
    print('PASS - step 1070')
except Exception as e:
    print('FAIL - step 1070' if isinstance(e, AssertionError) else f'ERROR - step 1070: {e}')

print("STEP 1071 - Check element h2#None.['headline']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['headline']")))
    print('PASS - step 1071')
except Exception as e:
    print('FAIL - step 1071' if isinstance(e, AssertionError) else f'ERROR - step 1071: {e}')

print("STEP 1072 - Check element p#None.['subhead']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['subhead']")))
    print('PASS - step 1072')
except Exception as e:
    print('FAIL - step 1072' if isinstance(e, AssertionError) else f'ERROR - step 1072: {e}')

print("STEP 1073 - Check element div#None.['cta-links']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['cta-links']")))
    print('PASS - step 1073')
except Exception as e:
    print('FAIL - step 1073' if isinstance(e, AssertionError) else f'ERROR - step 1073: {e}')

print("STEP 1074 - Check element a#None.['button', 'button-elevated', 'button-primary']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['button', 'button-elevated', 'button-primary']")))
    print('PASS - step 1074')
except Exception as e:
    print('FAIL - step 1074' if isinstance(e, AssertionError) else f'ERROR - step 1074: {e}')

print("STEP 1075 - Check element div#None.['unit-image-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unit-image-wrapper']")))
    print('PASS - step 1075')
except Exception as e:
    print('FAIL - step 1075' if isinstance(e, AssertionError) else f'ERROR - step 1075: {e}')

print("STEP 1076 - Check element div#None.['animation-wrapper', 'paused', 'loading']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['animation-wrapper', 'paused', 'loading']")))
    print('PASS - step 1076')
except Exception as e:
    print('FAIL - step 1076' if isinstance(e, AssertionError) else f'ERROR - step 1076: {e}')

print("STEP 1077 - Check element figure#None.['unit-image', 'unit-image-holiday-2025-hero-holiday-2025-startframe', 'start-frame']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unit-image', 'unit-image-holiday-2025-hero-holiday-2025-startframe', 'start-frame']")))
    print('PASS - step 1077')
except Exception as e:
    print('FAIL - step 1077' if isinstance(e, AssertionError) else f'ERROR - step 1077: {e}')

print("STEP 1078 - Check element video#holiday-2025-video.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "holiday-2025-video")))
    print('PASS - step 1078')
except Exception as e:
    print('FAIL - step 1078' if isinstance(e, AssertionError) else f'ERROR - step 1078: {e}')

print("STEP 1079 - Check element figure#None.['unit-image', 'unit-image-holiday-2025-hero-holiday-2025', 'static-frame']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unit-image', 'unit-image-holiday-2025-hero-holiday-2025', 'static-frame']")))
    print('PASS - step 1079')
except Exception as e:
    print('FAIL - step 1079' if isinstance(e, AssertionError) else f'ERROR - step 1079: {e}')

print("STEP 1080 - Check element div#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "div")))
    print('PASS - step 1080')
except Exception as e:
    print('FAIL - step 1080' if isinstance(e, AssertionError) else f'ERROR - step 1080: {e}')

print("STEP 1081 - Check element div#None.['module-content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['module-content']")))
    print('PASS - step 1081')
except Exception as e:
    print('FAIL - step 1081' if isinstance(e, AssertionError) else f'ERROR - step 1081: {e}')

print("STEP 1082 - Check element div#None.['unit-wrapper', 'split-copy-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unit-wrapper', 'split-copy-wrapper']")))
    print('PASS - step 1082')
except Exception as e:
    print('FAIL - step 1082' if isinstance(e, AssertionError) else f'ERROR - step 1082: {e}')

print("STEP 1083 - Check element a#None.['unit-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unit-link']")))
    print('PASS - step 1083')
except Exception as e:
    print('FAIL - step 1083' if isinstance(e, AssertionError) else f'ERROR - step 1083: {e}')

print("STEP 1084 - Check element div#None.['unit-copy-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unit-copy-wrapper']")))
    print('PASS - step 1084')
except Exception as e:
    print('FAIL - step 1084' if isinstance(e, AssertionError) else f'ERROR - step 1084: {e}')

print("STEP 1085 - Check element div#None.['split-wrapper-top']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['split-wrapper-top']")))
    print('PASS - step 1085')
except Exception as e:
    print('FAIL - step 1085' if isinstance(e, AssertionError) else f'ERROR - step 1085: {e}')

print("STEP 1086 - Check element h2#None.['logo-image', 'logo-image-ipad-air-hero-logo-ipad-air', 'headline']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['logo-image', 'logo-image-ipad-air-hero-logo-ipad-air', 'headline']")))
    print('PASS - step 1086')
except Exception as e:
    print('FAIL - step 1086' if isinstance(e, AssertionError) else f'ERROR - step 1086: {e}')

print("STEP 1087 - Check element span#None.['visuallyhidden']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['visuallyhidden']")))
    print('PASS - step 1087')
except Exception as e:
    print('FAIL - step 1087' if isinstance(e, AssertionError) else f'ERROR - step 1087: {e}')

print("STEP 1088 - Check element p#None.['subhead']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['subhead']")))
    print('PASS - step 1088')
except Exception as e:
    print('FAIL - step 1088' if isinstance(e, AssertionError) else f'ERROR - step 1088: {e}')

print("STEP 1089 - Check element div#None.['cta-links']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['cta-links']")))
    print('PASS - step 1089')
except Exception as e:
    print('FAIL - step 1089' if isinstance(e, AssertionError) else f'ERROR - step 1089: {e}')

print("STEP 1090 - Check element a#None.['button', 'button-elevated']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['button', 'button-elevated']")))
    print('PASS - step 1090')
except Exception as e:
    print('FAIL - step 1090' if isinstance(e, AssertionError) else f'ERROR - step 1090: {e}')

print("STEP 1091 - Check element a#None.['button', 'button-elevated', 'button-tertiary']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['button', 'button-elevated', 'button-tertiary']")))
    print('PASS - step 1091')
except Exception as e:
    print('FAIL - step 1091' if isinstance(e, AssertionError) else f'ERROR - step 1091: {e}')

print("STEP 1092 - Check element div#None.['split-wrapper-bottom']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['split-wrapper-bottom']")))
    print('PASS - step 1092')
except Exception as e:
    print('FAIL - step 1092' if isinstance(e, AssertionError) else f'ERROR - step 1092: {e}')

print("STEP 1093 - Check element div#None.['unit-image-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unit-image-wrapper']")))
    print('PASS - step 1093')
except Exception as e:
    print('FAIL - step 1093' if isinstance(e, AssertionError) else f'ERROR - step 1093: {e}')

print("STEP 1094 - Check element figure#None.['unit-image', 'unit-image-ipad-air-hero-ipad-air-avail']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unit-image', 'unit-image-ipad-air-hero-ipad-air-avail']")))
    print('PASS - step 1094')
except Exception as e:
    print('FAIL - step 1094' if isinstance(e, AssertionError) else f'ERROR - step 1094: {e}')

print("STEP 1095 - Check element section#None.['homepage-section', 'collection-module']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['homepage-section', 'collection-module']")))
    print('PASS - step 1095')
except Exception as e:
    print('FAIL - step 1095' if isinstance(e, AssertionError) else f'ERROR - step 1095: {e}')

print("STEP 1096 - Check element div#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "div")))
    print('PASS - step 1096')
except Exception as e:
    print('FAIL - step 1096' if isinstance(e, AssertionError) else f'ERROR - step 1096: {e}')

print("STEP 1097 - Check element div#None.['module-content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['module-content']")))
    print('PASS - step 1097')
except Exception as e:
    print('FAIL - step 1097' if isinstance(e, AssertionError) else f'ERROR - step 1097: {e}')

print("STEP 1098 - Check element div#None.['unit-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unit-wrapper']")))
    print('PASS - step 1098')
except Exception as e:
    print('FAIL - step 1098' if isinstance(e, AssertionError) else f'ERROR - step 1098: {e}')

print("STEP 1099 - Check element a#None.['unit-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unit-link']")))
    print('PASS - step 1099')
except Exception as e:
    print('FAIL - step 1099' if isinstance(e, AssertionError) else f'ERROR - step 1099: {e}')

print("STEP 1100 - Check element div#None.['unit-copy-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unit-copy-wrapper']")))
    print('PASS - step 1100')
except Exception as e:
    print('FAIL - step 1100' if isinstance(e, AssertionError) else f'ERROR - step 1100: {e}')

print("STEP 1101 - Check element h3#None.['headline']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['headline']")))
    print('PASS - step 1101')
except Exception as e:
    print('FAIL - step 1101' if isinstance(e, AssertionError) else f'ERROR - step 1101: {e}')

print("STEP 1102 - Check element p#None.['subhead']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['subhead']")))
    print('PASS - step 1102')
except Exception as e:
    print('FAIL - step 1102' if isinstance(e, AssertionError) else f'ERROR - step 1102: {e}')

print("STEP 1103 - Check element div#None.['cta-links']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['cta-links']")))
    print('PASS - step 1103')
except Exception as e:
    print('FAIL - step 1103' if isinstance(e, AssertionError) else f'ERROR - step 1103: {e}')

print("STEP 1104 - Check element a#None.['button', 'button-primary']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['button', 'button-primary']")))
    print('PASS - step 1104')
except Exception as e:
    print('FAIL - step 1104' if isinstance(e, AssertionError) else f'ERROR - step 1104: {e}')

print("STEP 1105 - Check element a#None.['button', 'button-tertiary']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['button', 'button-tertiary']")))
    print('PASS - step 1105')
except Exception as e:
    print('FAIL - step 1105' if isinstance(e, AssertionError) else f'ERROR - step 1105: {e}')

print("STEP 1106 - Check element div#None.['unit-image-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unit-image-wrapper']")))
    print('PASS - step 1106')
except Exception as e:
    print('FAIL - step 1106' if isinstance(e, AssertionError) else f'ERROR - step 1106: {e}')

print("STEP 1107 - Check element figure#None.['unit-image', 'unit-image-airpods-pro-3-promo-airpodspro-3']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unit-image', 'unit-image-airpods-pro-3-promo-airpodspro-3']")))
    print('PASS - step 1107')
except Exception as e:
    print('FAIL - step 1107' if isinstance(e, AssertionError) else f'ERROR - step 1107: {e}')

print("STEP 1108 - Check element div#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "div")))
    print('PASS - step 1108')
except Exception as e:
    print('FAIL - step 1108' if isinstance(e, AssertionError) else f'ERROR - step 1108: {e}')

print("STEP 1109 - Check element div#None.['module-content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['module-content']")))
    print('PASS - step 1109')
except Exception as e:
    print('FAIL - step 1109' if isinstance(e, AssertionError) else f'ERROR - step 1109: {e}')

print("STEP 1110 - Check element div#None.['unit-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unit-wrapper']")))
    print('PASS - step 1110')
except Exception as e:
    print('FAIL - step 1110' if isinstance(e, AssertionError) else f'ERROR - step 1110: {e}')

print("STEP 1111 - Check element a#None.['unit-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unit-link']")))
    print('PASS - step 1111')
except Exception as e:
    print('FAIL - step 1111' if isinstance(e, AssertionError) else f'ERROR - step 1111: {e}')

print("STEP 1112 - Check element div#None.['unit-copy-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unit-copy-wrapper']")))
    print('PASS - step 1112')
except Exception as e:
    print('FAIL - step 1112' if isinstance(e, AssertionError) else f'ERROR - step 1112: {e}')

print("STEP 1113 - Check element h3#None.['logo-image', 'logo-image-apple-watch-series-11-promo-logo-apple-watch-series-11', 'headline']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['logo-image', 'logo-image-apple-watch-series-11-promo-logo-apple-watch-series-11', 'headline']")))
    print('PASS - step 1113')
except Exception as e:
    print('FAIL - step 1113' if isinstance(e, AssertionError) else f'ERROR - step 1113: {e}')

print("STEP 1114 - Check element span#None.['visuallyhidden']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['visuallyhidden']")))
    print('PASS - step 1114')
except Exception as e:
    print('FAIL - step 1114' if isinstance(e, AssertionError) else f'ERROR - step 1114: {e}')

print("STEP 1115 - Check element p#None.['subhead']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['subhead']")))
    print('PASS - step 1115')
except Exception as e:
    print('FAIL - step 1115' if isinstance(e, AssertionError) else f'ERROR - step 1115: {e}')

print("STEP 1116 - Check element div#None.['cta-links']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['cta-links']")))
    print('PASS - step 1116')
except Exception as e:
    print('FAIL - step 1116' if isinstance(e, AssertionError) else f'ERROR - step 1116: {e}')

print("STEP 1117 - Check element a#None.['button', 'button-primary']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['button', 'button-primary']")))
    print('PASS - step 1117')
except Exception as e:
    print('FAIL - step 1117' if isinstance(e, AssertionError) else f'ERROR - step 1117: {e}')

print("STEP 1118 - Check element a#None.['button', 'button-tertiary']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['button', 'button-tertiary']")))
    print('PASS - step 1118')
except Exception as e:
    print('FAIL - step 1118' if isinstance(e, AssertionError) else f'ERROR - step 1118: {e}')

print("STEP 1119 - Check element div#None.['unit-image-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unit-image-wrapper']")))
    print('PASS - step 1119')
except Exception as e:
    print('FAIL - step 1119' if isinstance(e, AssertionError) else f'ERROR - step 1119: {e}')

print("STEP 1120 - Check element figure#None.['unit-image', 'unit-image-apple-watch-series-11-promo-apple-watch-series-11']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unit-image', 'unit-image-apple-watch-series-11-promo-apple-watch-series-11']")))
    print('PASS - step 1120')
except Exception as e:
    print('FAIL - step 1120' if isinstance(e, AssertionError) else f'ERROR - step 1120: {e}')

print("STEP 1121 - Check element div#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "div")))
    print('PASS - step 1121')
except Exception as e:
    print('FAIL - step 1121' if isinstance(e, AssertionError) else f'ERROR - step 1121: {e}')

print("STEP 1122 - Check element div#None.['module-content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['module-content']")))
    print('PASS - step 1122')
except Exception as e:
    print('FAIL - step 1122' if isinstance(e, AssertionError) else f'ERROR - step 1122: {e}')

print("STEP 1123 - Check element div#None.['unit-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unit-wrapper']")))
    print('PASS - step 1123')
except Exception as e:
    print('FAIL - step 1123' if isinstance(e, AssertionError) else f'ERROR - step 1123: {e}')

print("STEP 1124 - Check element a#None.['unit-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unit-link']")))
    print('PASS - step 1124')
except Exception as e:
    print('FAIL - step 1124' if isinstance(e, AssertionError) else f'ERROR - step 1124: {e}')

print("STEP 1125 - Check element div#None.['unit-copy-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unit-copy-wrapper']")))
    print('PASS - step 1125')
except Exception as e:
    print('FAIL - step 1125' if isinstance(e, AssertionError) else f'ERROR - step 1125: {e}')

print("STEP 1126 - Check element h3#None.['headline']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['headline']")))
    print('PASS - step 1126')
except Exception as e:
    print('FAIL - step 1126' if isinstance(e, AssertionError) else f'ERROR - step 1126: {e}')

print("STEP 1127 - Check element p#None.['subhead']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['subhead']")))
    print('PASS - step 1127')
except Exception as e:
    print('FAIL - step 1127' if isinstance(e, AssertionError) else f'ERROR - step 1127: {e}')

print("STEP 1128 - Check element div#None.['cta-links']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['cta-links']")))
    print('PASS - step 1128')
except Exception as e:
    print('FAIL - step 1128' if isinstance(e, AssertionError) else f'ERROR - step 1128: {e}')

print("STEP 1129 - Check element a#None.['button', 'button-primary']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['button', 'button-primary']")))
    print('PASS - step 1129')
except Exception as e:
    print('FAIL - step 1129' if isinstance(e, AssertionError) else f'ERROR - step 1129: {e}')

print("STEP 1130 - Check element a#None.['button', 'button-tertiary']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['button', 'button-tertiary']")))
    print('PASS - step 1130')
except Exception as e:
    print('FAIL - step 1130' if isinstance(e, AssertionError) else f'ERROR - step 1130: {e}')

print("STEP 1131 - Check element div#None.['unit-image-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unit-image-wrapper']")))
    print('PASS - step 1131')
except Exception as e:
    print('FAIL - step 1131' if isinstance(e, AssertionError) else f'ERROR - step 1131: {e}')

print("STEP 1132 - Check element figure#None.['unit-image', 'unit-image-ipad-promo-ipad']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unit-image', 'unit-image-ipad-promo-ipad']")))
    print('PASS - step 1132')
except Exception as e:
    print('FAIL - step 1132' if isinstance(e, AssertionError) else f'ERROR - step 1132: {e}')

print("STEP 1133 - Check element div#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "div")))
    print('PASS - step 1133')
except Exception as e:
    print('FAIL - step 1133' if isinstance(e, AssertionError) else f'ERROR - step 1133: {e}')

print("STEP 1134 - Check element div#None.['module-content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['module-content']")))
    print('PASS - step 1134')
except Exception as e:
    print('FAIL - step 1134' if isinstance(e, AssertionError) else f'ERROR - step 1134: {e}')

print("STEP 1135 - Check element div#None.['unit-wrapper', 'split-copy-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unit-wrapper', 'split-copy-wrapper']")))
    print('PASS - step 1135')
except Exception as e:
    print('FAIL - step 1135' if isinstance(e, AssertionError) else f'ERROR - step 1135: {e}')

print("STEP 1136 - Check element a#None.['unit-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unit-link']")))
    print('PASS - step 1136')
except Exception as e:
    print('FAIL - step 1136' if isinstance(e, AssertionError) else f'ERROR - step 1136: {e}')

print("STEP 1137 - Check element div#None.['unit-copy-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unit-copy-wrapper']")))
    print('PASS - step 1137')
except Exception as e:
    print('FAIL - step 1137' if isinstance(e, AssertionError) else f'ERROR - step 1137: {e}')

print("STEP 1138 - Check element div#None.['split-wrapper-top']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['split-wrapper-top']")))
    print('PASS - step 1138')
except Exception as e:
    print('FAIL - step 1138' if isinstance(e, AssertionError) else f'ERROR - step 1138: {e}')

print("STEP 1139 - Check element h3#None.['headline']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['headline']")))
    print('PASS - step 1139')
except Exception as e:
    print('FAIL - step 1139' if isinstance(e, AssertionError) else f'ERROR - step 1139: {e}')

print("STEP 1140 - Check element p#None.['subhead']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['subhead']")))
    print('PASS - step 1140')
except Exception as e:
    print('FAIL - step 1140' if isinstance(e, AssertionError) else f'ERROR - step 1140: {e}')

print("STEP 1141 - Check element br#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "br")))
    print('PASS - step 1141')
except Exception as e:
    print('FAIL - step 1141' if isinstance(e, AssertionError) else f'ERROR - step 1141: {e}')

print("STEP 1142 - Check element div#None.['cta-links']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['cta-links']")))
    print('PASS - step 1142')
except Exception as e:
    print('FAIL - step 1142' if isinstance(e, AssertionError) else f'ERROR - step 1142: {e}')

print("STEP 1143 - Check element a#None.['button', 'button-primary']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['button', 'button-primary']")))
    print('PASS - step 1143')
except Exception as e:
    print('FAIL - step 1143' if isinstance(e, AssertionError) else f'ERROR - step 1143: {e}')

print("STEP 1144 - Check element a#None.['button', 'button-tertiary']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['button', 'button-tertiary']")))
    print('PASS - step 1144')
except Exception as e:
    print('FAIL - step 1144' if isinstance(e, AssertionError) else f'ERROR - step 1144: {e}')

print("STEP 1145 - Check element div#None.['split-wrapper-bottom']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['split-wrapper-bottom']")))
    print('PASS - step 1145')
except Exception as e:
    print('FAIL - step 1145' if isinstance(e, AssertionError) else f'ERROR - step 1145: {e}')

print("STEP 1146 - Check element div#None.['unit-image-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unit-image-wrapper']")))
    print('PASS - step 1146')
except Exception as e:
    print('FAIL - step 1146' if isinstance(e, AssertionError) else f'ERROR - step 1146: {e}')

print("STEP 1147 - Check element figure#None.['unit-image', 'unit-image-macbook-air-promo-macbook-air']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unit-image', 'unit-image-macbook-air-promo-macbook-air']")))
    print('PASS - step 1147')
except Exception as e:
    print('FAIL - step 1147' if isinstance(e, AssertionError) else f'ERROR - step 1147: {e}')

print("STEP 1148 - Check element div#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "div")))
    print('PASS - step 1148')
except Exception as e:
    print('FAIL - step 1148' if isinstance(e, AssertionError) else f'ERROR - step 1148: {e}')

print("STEP 1149 - Check element div#None.['module-content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['module-content']")))
    print('PASS - step 1149')
except Exception as e:
    print('FAIL - step 1149' if isinstance(e, AssertionError) else f'ERROR - step 1149: {e}')

print("STEP 1150 - Check element div#None.['unit-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unit-wrapper']")))
    print('PASS - step 1150')
except Exception as e:
    print('FAIL - step 1150' if isinstance(e, AssertionError) else f'ERROR - step 1150: {e}')

print("STEP 1151 - Check element a#None.['unit-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unit-link']")))
    print('PASS - step 1151')
except Exception as e:
    print('FAIL - step 1151' if isinstance(e, AssertionError) else f'ERROR - step 1151: {e}')

print("STEP 1152 - Check element div#None.['unit-copy-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unit-copy-wrapper']")))
    print('PASS - step 1152')
except Exception as e:
    print('FAIL - step 1152' if isinstance(e, AssertionError) else f'ERROR - step 1152: {e}')

print("STEP 1153 - Check element h3#None.['logo-image', 'logo-image-iphone-tradein-promo-logo-iphone-tradein', 'headline']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['logo-image', 'logo-image-iphone-tradein-promo-logo-iphone-tradein', 'headline']")))
    print('PASS - step 1153')
except Exception as e:
    print('FAIL - step 1153' if isinstance(e, AssertionError) else f'ERROR - step 1153: {e}')

print("STEP 1154 - Check element span#None.['visuallyhidden']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['visuallyhidden']")))
    print('PASS - step 1154')
except Exception as e:
    print('FAIL - step 1154' if isinstance(e, AssertionError) else f'ERROR - step 1154: {e}')

print("STEP 1155 - Check element p#None.['subhead']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['subhead']")))
    print('PASS - step 1155')
except Exception as e:
    print('FAIL - step 1155' if isinstance(e, AssertionError) else f'ERROR - step 1155: {e}')

print("STEP 1156 - Check element sup#None.['footnote', 'footnote-number']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['footnote', 'footnote-number']")))
    print('PASS - step 1156')
except Exception as e:
    print('FAIL - step 1156' if isinstance(e, AssertionError) else f'ERROR - step 1156: {e}')

print("STEP 1157 - Check element div#None.['cta-links']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['cta-links']")))
    print('PASS - step 1157')
except Exception as e:
    print('FAIL - step 1157' if isinstance(e, AssertionError) else f'ERROR - step 1157: {e}')

print("STEP 1158 - Check element a#None.['button', 'button-primary']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['button', 'button-primary']")))
    print('PASS - step 1158')
except Exception as e:
    print('FAIL - step 1158' if isinstance(e, AssertionError) else f'ERROR - step 1158: {e}')

print("STEP 1159 - Check element div#None.['unit-image-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unit-image-wrapper']")))
    print('PASS - step 1159')
except Exception as e:
    print('FAIL - step 1159' if isinstance(e, AssertionError) else f'ERROR - step 1159: {e}')

print("STEP 1160 - Check element figure#None.['unit-image', 'unit-image-iphone-tradein-promo-iphone-tradein']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unit-image', 'unit-image-iphone-tradein-promo-iphone-tradein']")))
    print('PASS - step 1160')
except Exception as e:
    print('FAIL - step 1160' if isinstance(e, AssertionError) else f'ERROR - step 1160: {e}')

print("STEP 1161 - Check element div#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "div")))
    print('PASS - step 1161')
except Exception as e:
    print('FAIL - step 1161' if isinstance(e, AssertionError) else f'ERROR - step 1161: {e}')

print("STEP 1162 - Check element div#None.['module-content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['module-content']")))
    print('PASS - step 1162')
except Exception as e:
    print('FAIL - step 1162' if isinstance(e, AssertionError) else f'ERROR - step 1162: {e}')

print("STEP 1163 - Check element div#None.['unit-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unit-wrapper']")))
    print('PASS - step 1163')
except Exception as e:
    print('FAIL - step 1163' if isinstance(e, AssertionError) else f'ERROR - step 1163: {e}')

print("STEP 1164 - Check element a#None.['unit-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unit-link']")))
    print('PASS - step 1164')
except Exception as e:
    print('FAIL - step 1164' if isinstance(e, AssertionError) else f'ERROR - step 1164: {e}')

print("STEP 1165 - Check element div#None.['unit-copy-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unit-copy-wrapper']")))
    print('PASS - step 1165')
except Exception as e:
    print('FAIL - step 1165' if isinstance(e, AssertionError) else f'ERROR - step 1165: {e}')

print("STEP 1166 - Check element h3#None.['logo-image', 'logo-image-apple-card-logo', 'headline']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['logo-image', 'logo-image-apple-card-logo', 'headline']")))
    print('PASS - step 1166')
except Exception as e:
    print('FAIL - step 1166' if isinstance(e, AssertionError) else f'ERROR - step 1166: {e}')

print("STEP 1167 - Check element span#None.['visuallyhidden']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['visuallyhidden']")))
    print('PASS - step 1167')
except Exception as e:
    print('FAIL - step 1167' if isinstance(e, AssertionError) else f'ERROR - step 1167: {e}')

print("STEP 1168 - Check element p#None.['subhead']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['subhead']")))
    print('PASS - step 1168')
except Exception as e:
    print('FAIL - step 1168' if isinstance(e, AssertionError) else f'ERROR - step 1168: {e}')

print("STEP 1169 - Check element div#None.['cta-links']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['cta-links']")))
    print('PASS - step 1169')
except Exception as e:
    print('FAIL - step 1169' if isinstance(e, AssertionError) else f'ERROR - step 1169: {e}')

print("STEP 1170 - Check element a#None.['button', 'button-primary']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['button', 'button-primary']")))
    print('PASS - step 1170')
except Exception as e:
    print('FAIL - step 1170' if isinstance(e, AssertionError) else f'ERROR - step 1170: {e}')

print("STEP 1171 - Check element a#None.['default', 'button', 'button-tertiary']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['default', 'button', 'button-tertiary']")))
    print('PASS - step 1171')
except Exception as e:
    print('FAIL - step 1171' if isinstance(e, AssertionError) else f'ERROR - step 1171: {e}')

print("STEP 1172 - Check element a#None.['ios', 'button', 'button-tertiary']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ios', 'button', 'button-tertiary']")))
    print('PASS - step 1172')
except Exception as e:
    print('FAIL - step 1172' if isinstance(e, AssertionError) else f'ERROR - step 1172: {e}')

print("STEP 1173 - Check element div#None.['unit-image-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unit-image-wrapper']")))
    print('PASS - step 1173')
except Exception as e:
    print('FAIL - step 1173' if isinstance(e, AssertionError) else f'ERROR - step 1173: {e}')

print("STEP 1174 - Check element figure#None.['unit-image', 'unit-image-apple-card-promo-apple-card']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['unit-image', 'unit-image-apple-card-promo-apple-card']")))
    print('PASS - step 1174')
except Exception as e:
    print('FAIL - step 1174' if isinstance(e, AssertionError) else f'ERROR - step 1174: {e}')

print("STEP 1175 - Check element section#None.['homepage-section', 'standalone-module']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['homepage-section', 'standalone-module']")))
    print('PASS - step 1175')
except Exception as e:
    print('FAIL - step 1175' if isinstance(e, AssertionError) else f'ERROR - step 1175: {e}')

print("STEP 1176 - Check element div#None.['module-content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['module-content']")))
    print('PASS - step 1176')
except Exception as e:
    print('FAIL - step 1176' if isinstance(e, AssertionError) else f'ERROR - step 1176: {e}')

print("STEP 1177 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 1177')
except Exception as e:
    print('FAIL - step 1177' if isinstance(e, AssertionError) else f'ERROR - step 1177: {e}')

print("STEP 1178 - Check element div#None.['endless-entertainment']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['endless-entertainment']")))
    print('PASS - step 1178')
except Exception as e:
    print('FAIL - step 1178' if isinstance(e, AssertionError) else f'ERROR - step 1178: {e}')

print("STEP 1179 - Check element div#None.['media-gallery-headline-container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-headline-container']")))
    print('PASS - step 1179')
except Exception as e:
    print('FAIL - step 1179' if isinstance(e, AssertionError) else f'ERROR - step 1179: {e}')

print("STEP 1180 - Check element h2#None.['media-gallery-headline']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-headline']")))
    print('PASS - step 1180')
except Exception as e:
    print('FAIL - step 1180' if isinstance(e, AssertionError) else f'ERROR - step 1180: {e}')

print("STEP 1181 - Check element div#None.['media-gallery-dotnav', 'dotnav', 'dotnav-scrim-solid', 'dotnav-timed', 'dotnav-timed-paused']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-dotnav', 'dotnav', 'dotnav-scrim-solid', 'dotnav-timed', 'dotnav-timed-paused']")))
    print('PASS - step 1181')
except Exception as e:
    print('FAIL - step 1181' if isinstance(e, AssertionError) else f'ERROR - step 1181: {e}')

print("STEP 1182 - Check element ul#None.['media-gallery-dotnav-items', 'dotnav-items']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-dotnav-items', 'dotnav-items']")))
    print('PASS - step 1182')
except Exception as e:
    print('FAIL - step 1182' if isinstance(e, AssertionError) else f'ERROR - step 1182: {e}')

print("STEP 1183 - Check element li#None.['media-gallery-dotnav-item', 'dotnav-item', 'current', 'dotnav-focused', 'dotnav-trunc-1', 'dotnav-incoming']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-dotnav-item', 'dotnav-item', 'current', 'dotnav-focused', 'dotnav-trunc-1', 'dotnav-incoming']")))
    print('PASS - step 1183')
except Exception as e:
    print('FAIL - step 1183' if isinstance(e, AssertionError) else f'ERROR - step 1183: {e}')

print("STEP 1184 - Check element a#endless-entertainment-gallery-item-1-trigger.['media-gallery-dotnav-link', 'dotnav-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "endless-entertainment-gallery-item-1-trigger")))
    print('PASS - step 1184')
except Exception as e:
    print('FAIL - step 1184' if isinstance(e, AssertionError) else f'ERROR - step 1184: {e}')

print("STEP 1185 - Check element span#None.['visuallyhidden']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['visuallyhidden']")))
    print('PASS - step 1185')
except Exception as e:
    print('FAIL - step 1185' if isinstance(e, AssertionError) else f'ERROR - step 1185: {e}')

print("STEP 1186 - Check element li#None.['media-gallery-dotnav-item', 'dotnav-item', 'dotnav-trunc-1']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-dotnav-item', 'dotnav-item', 'dotnav-trunc-1']")))
    print('PASS - step 1186')
except Exception as e:
    print('FAIL - step 1186' if isinstance(e, AssertionError) else f'ERROR - step 1186: {e}')

print("STEP 1187 - Check element a#endless-entertainment-gallery-item-2-trigger.['media-gallery-dotnav-link', 'dotnav-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "endless-entertainment-gallery-item-2-trigger")))
    print('PASS - step 1187')
except Exception as e:
    print('FAIL - step 1187' if isinstance(e, AssertionError) else f'ERROR - step 1187: {e}')

print("STEP 1188 - Check element span#None.['visuallyhidden']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['visuallyhidden']")))
    print('PASS - step 1188')
except Exception as e:
    print('FAIL - step 1188' if isinstance(e, AssertionError) else f'ERROR - step 1188: {e}')

print("STEP 1189 - Check element li#None.['media-gallery-dotnav-item', 'dotnav-item', 'dotnav-trunc-1']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-dotnav-item', 'dotnav-item', 'dotnav-trunc-1']")))
    print('PASS - step 1189')
except Exception as e:
    print('FAIL - step 1189' if isinstance(e, AssertionError) else f'ERROR - step 1189: {e}')

print("STEP 1190 - Check element a#endless-entertainment-gallery-item-3-trigger.['media-gallery-dotnav-link', 'dotnav-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "endless-entertainment-gallery-item-3-trigger")))
    print('PASS - step 1190')
except Exception as e:
    print('FAIL - step 1190' if isinstance(e, AssertionError) else f'ERROR - step 1190: {e}')

print("STEP 1191 - Check element span#None.['visuallyhidden']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['visuallyhidden']")))
    print('PASS - step 1191')
except Exception as e:
    print('FAIL - step 1191' if isinstance(e, AssertionError) else f'ERROR - step 1191: {e}')

print("STEP 1192 - Check element li#None.['media-gallery-dotnav-item', 'dotnav-item', 'dotnav-trunc-1']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-dotnav-item', 'dotnav-item', 'dotnav-trunc-1']")))
    print('PASS - step 1192')
except Exception as e:
    print('FAIL - step 1192' if isinstance(e, AssertionError) else f'ERROR - step 1192: {e}')

print("STEP 1193 - Check element a#endless-entertainment-gallery-item-4-trigger.['media-gallery-dotnav-link', 'dotnav-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "endless-entertainment-gallery-item-4-trigger")))
    print('PASS - step 1193')
except Exception as e:
    print('FAIL - step 1193' if isinstance(e, AssertionError) else f'ERROR - step 1193: {e}')

print("STEP 1194 - Check element span#None.['visuallyhidden']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['visuallyhidden']")))
    print('PASS - step 1194')
except Exception as e:
    print('FAIL - step 1194' if isinstance(e, AssertionError) else f'ERROR - step 1194: {e}')

print("STEP 1195 - Check element li#None.['media-gallery-dotnav-item', 'dotnav-item', 'dotnav-trunc-1']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-dotnav-item', 'dotnav-item', 'dotnav-trunc-1']")))
    print('PASS - step 1195')
except Exception as e:
    print('FAIL - step 1195' if isinstance(e, AssertionError) else f'ERROR - step 1195: {e}')

print("STEP 1196 - Check element a#endless-entertainment-gallery-item-5-trigger.['media-gallery-dotnav-link', 'dotnav-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "endless-entertainment-gallery-item-5-trigger")))
    print('PASS - step 1196')
except Exception as e:
    print('FAIL - step 1196' if isinstance(e, AssertionError) else f'ERROR - step 1196: {e}')

print("STEP 1197 - Check element span#None.['visuallyhidden']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['visuallyhidden']")))
    print('PASS - step 1197')
except Exception as e:
    print('FAIL - step 1197' if isinstance(e, AssertionError) else f'ERROR - step 1197: {e}')

print("STEP 1198 - Check element li#None.['media-gallery-dotnav-item', 'dotnav-item', 'dotnav-trunc-2']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-dotnav-item', 'dotnav-item', 'dotnav-trunc-2']")))
    print('PASS - step 1198')
except Exception as e:
    print('FAIL - step 1198' if isinstance(e, AssertionError) else f'ERROR - step 1198: {e}')

print("STEP 1199 - Check element a#endless-entertainment-gallery-item-6-trigger.['media-gallery-dotnav-link', 'dotnav-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "endless-entertainment-gallery-item-6-trigger")))
    print('PASS - step 1199')
except Exception as e:
    print('FAIL - step 1199' if isinstance(e, AssertionError) else f'ERROR - step 1199: {e}')

print("STEP 1200 - Check element span#None.['visuallyhidden']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['visuallyhidden']")))
    print('PASS - step 1200')
except Exception as e:
    print('FAIL - step 1200' if isinstance(e, AssertionError) else f'ERROR - step 1200: {e}')

print("STEP 1201 - Check element li#None.['media-gallery-dotnav-item', 'dotnav-item', 'dotnav-trunc-3']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-dotnav-item', 'dotnav-item', 'dotnav-trunc-3']")))
    print('PASS - step 1201')
except Exception as e:
    print('FAIL - step 1201' if isinstance(e, AssertionError) else f'ERROR - step 1201: {e}')

print("STEP 1202 - Check element a#endless-entertainment-gallery-item-7-trigger.['media-gallery-dotnav-link', 'dotnav-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "endless-entertainment-gallery-item-7-trigger")))
    print('PASS - step 1202')
except Exception as e:
    print('FAIL - step 1202' if isinstance(e, AssertionError) else f'ERROR - step 1202: {e}')

print("STEP 1203 - Check element span#None.['visuallyhidden']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['visuallyhidden']")))
    print('PASS - step 1203')
except Exception as e:
    print('FAIL - step 1203' if isinstance(e, AssertionError) else f'ERROR - step 1203: {e}')

print("STEP 1204 - Check element li#None.['media-gallery-dotnav-item', 'dotnav-item', 'dotnav-trunc-4']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-dotnav-item', 'dotnav-item', 'dotnav-trunc-4']")))
    print('PASS - step 1204')
except Exception as e:
    print('FAIL - step 1204' if isinstance(e, AssertionError) else f'ERROR - step 1204: {e}')

print("STEP 1205 - Check element a#endless-entertainment-gallery-item-8-trigger.['media-gallery-dotnav-link', 'dotnav-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "endless-entertainment-gallery-item-8-trigger")))
    print('PASS - step 1205')
except Exception as e:
    print('FAIL - step 1205' if isinstance(e, AssertionError) else f'ERROR - step 1205: {e}')

print("STEP 1206 - Check element span#None.['visuallyhidden']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['visuallyhidden']")))
    print('PASS - step 1206')
except Exception as e:
    print('FAIL - step 1206' if isinstance(e, AssertionError) else f'ERROR - step 1206: {e}')

print("STEP 1207 - Check element li#None.['media-gallery-dotnav-item', 'dotnav-item', 'dotnav-trunc-4']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-dotnav-item', 'dotnav-item', 'dotnav-trunc-4']")))
    print('PASS - step 1207')
except Exception as e:
    print('FAIL - step 1207' if isinstance(e, AssertionError) else f'ERROR - step 1207: {e}')

print("STEP 1208 - Check element a#endless-entertainment-gallery-item-9-trigger.['media-gallery-dotnav-link', 'dotnav-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "endless-entertainment-gallery-item-9-trigger")))
    print('PASS - step 1208')
except Exception as e:
    print('FAIL - step 1208' if isinstance(e, AssertionError) else f'ERROR - step 1208: {e}')

print("STEP 1209 - Check element span#None.['visuallyhidden']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['visuallyhidden']")))
    print('PASS - step 1209')
except Exception as e:
    print('FAIL - step 1209' if isinstance(e, AssertionError) else f'ERROR - step 1209: {e}')

print("STEP 1210 - Check element button#None.['media-gallery-dotnav-iconcontrol', 'dotnav-iconcontrol']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-dotnav-iconcontrol', 'dotnav-iconcontrol']")))
    print('PASS - step 1210')
except Exception as e:
    print('FAIL - step 1210' if isinstance(e, AssertionError) else f'ERROR - step 1210: {e}')

print("STEP 1211 - Check element span#None.['media-gallery-dotnav-iconcontrol-icon', 'dotnav-iconcontrol-icon']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-dotnav-iconcontrol-icon', 'dotnav-iconcontrol-icon']")))
    print('PASS - step 1211')
except Exception as e:
    print('FAIL - step 1211' if isinstance(e, AssertionError) else f'ERROR - step 1211: {e}')

print("STEP 1212 - Check element svg#None.['media-gallery-dotnav-iconcontrol-pause', 'dotnav-iconcontrol-pause']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-dotnav-iconcontrol-pause', 'dotnav-iconcontrol-pause']")))
    print('PASS - step 1212')
except Exception as e:
    print('FAIL - step 1212' if isinstance(e, AssertionError) else f'ERROR - step 1212: {e}')

print("STEP 1213 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 1213')
except Exception as e:
    print('FAIL - step 1213' if isinstance(e, AssertionError) else f'ERROR - step 1213: {e}')

print("STEP 1214 - Check element svg#None.['media-gallery-dotnav-iconcontrol-play', 'dotnav-iconcontrol-play']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-dotnav-iconcontrol-play', 'dotnav-iconcontrol-play']")))
    print('PASS - step 1214')
except Exception as e:
    print('FAIL - step 1214' if isinstance(e, AssertionError) else f'ERROR - step 1214: {e}')

print("STEP 1215 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 1215')
except Exception as e:
    print('FAIL - step 1215' if isinstance(e, AssertionError) else f'ERROR - step 1215: {e}')

print("STEP 1216 - Check element div#tv-media-gallery.['media-gallery', 'tv-media-gallery']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "tv-media-gallery")))
    print('PASS - step 1216')
except Exception as e:
    print('FAIL - step 1216' if isinstance(e, AssertionError) else f'ERROR - step 1216: {e}')

print("STEP 1217 - Check element ul#None.['media-gallery-item-container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-item-container']")))
    print('PASS - step 1217')
except Exception as e:
    print('FAIL - step 1217' if isinstance(e, AssertionError) else f'ERROR - step 1217: {e}')

print("STEP 1218 - Check element li#endless-entertainment-gallery-item-1.['media-gallery-item', 'theme-dark', 'current', 'current-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "endless-entertainment-gallery-item-1")))
    print('PASS - step 1218')
except Exception as e:
    print('FAIL - step 1218' if isinstance(e, AssertionError) else f'ERROR - step 1218: {e}')

print("STEP 1219 - Check element a#media-gallery-item-1-link.['media-gallery-wrapper-link', 'fam-media-gallery-wrapper-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "media-gallery-item-1-link")))
    print('PASS - step 1219')
except Exception as e:
    print('FAIL - step 1219' if isinstance(e, AssertionError) else f'ERROR - step 1219: {e}')

print("STEP 1220 - Check element div#None.['media-gallery-bg-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-bg-wrapper']")))
    print('PASS - step 1220')
except Exception as e:
    print('FAIL - step 1220' if isinstance(e, AssertionError) else f'ERROR - step 1220: {e}')

print("STEP 1221 - Check element picture#None.['media-gallery-bg']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-bg']")))
    print('PASS - step 1221')
except Exception as e:
    print('FAIL - step 1221' if isinstance(e, AssertionError) else f'ERROR - step 1221: {e}')

print("STEP 1222 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1222')
except Exception as e:
    print('FAIL - step 1222' if isinstance(e, AssertionError) else f'ERROR - step 1222: {e}')

print("STEP 1223 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1223')
except Exception as e:
    print('FAIL - step 1223' if isinstance(e, AssertionError) else f'ERROR - step 1223: {e}')

print("STEP 1224 - Check element noscript#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "noscript")))
    print('PASS - step 1224')
except Exception as e:
    print('FAIL - step 1224' if isinstance(e, AssertionError) else f'ERROR - step 1224: {e}')

print("STEP 1225 - Check element picture#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "picture")))
    print('PASS - step 1225')
except Exception as e:
    print('FAIL - step 1225' if isinstance(e, AssertionError) else f'ERROR - step 1225: {e}')

print("STEP 1226 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1226')
except Exception as e:
    print('FAIL - step 1226' if isinstance(e, AssertionError) else f'ERROR - step 1226: {e}')

print("STEP 1227 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1227')
except Exception as e:
    print('FAIL - step 1227' if isinstance(e, AssertionError) else f'ERROR - step 1227: {e}')

print("STEP 1228 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1228')
except Exception as e:
    print('FAIL - step 1228' if isinstance(e, AssertionError) else f'ERROR - step 1228: {e}')

print("STEP 1229 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1229')
except Exception as e:
    print('FAIL - step 1229' if isinstance(e, AssertionError) else f'ERROR - step 1229: {e}')

print("STEP 1230 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1230')
except Exception as e:
    print('FAIL - step 1230' if isinstance(e, AssertionError) else f'ERROR - step 1230: {e}')

print("STEP 1231 - Check element div#None.['media-gallery-contents']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-contents']")))
    print('PASS - step 1231')
except Exception as e:
    print('FAIL - step 1231' if isinstance(e, AssertionError) else f'ERROR - step 1231: {e}')

print("STEP 1232 - Check element div#None.['media-gallery-top-content', 'tv-gallery-top-content-s-only']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-top-content', 'tv-gallery-top-content-s-only']")))
    print('PASS - step 1232')
except Exception as e:
    print('FAIL - step 1232' if isinstance(e, AssertionError) else f'ERROR - step 1232: {e}')

print("STEP 1233 - Check element picture#None.['tv-gallery-atvplus-logo', 'hide-logo']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['tv-gallery-atvplus-logo', 'hide-logo']")))
    print('PASS - step 1233')
except Exception as e:
    print('FAIL - step 1233' if isinstance(e, AssertionError) else f'ERROR - step 1233: {e}')

print("STEP 1234 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1234')
except Exception as e:
    print('FAIL - step 1234' if isinstance(e, AssertionError) else f'ERROR - step 1234: {e}')

print("STEP 1235 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1235')
except Exception as e:
    print('FAIL - step 1235' if isinstance(e, AssertionError) else f'ERROR - step 1235: {e}')

print("STEP 1236 - Check element noscript#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "noscript")))
    print('PASS - step 1236')
except Exception as e:
    print('FAIL - step 1236' if isinstance(e, AssertionError) else f'ERROR - step 1236: {e}')

print("STEP 1237 - Check element picture#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "picture")))
    print('PASS - step 1237')
except Exception as e:
    print('FAIL - step 1237' if isinstance(e, AssertionError) else f'ERROR - step 1237: {e}')

print("STEP 1238 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1238')
except Exception as e:
    print('FAIL - step 1238' if isinstance(e, AssertionError) else f'ERROR - step 1238: {e}')

print("STEP 1239 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1239')
except Exception as e:
    print('FAIL - step 1239' if isinstance(e, AssertionError) else f'ERROR - step 1239: {e}')

print("STEP 1240 - Check element picture#None.['tv-gallery-media-logo']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['tv-gallery-media-logo']")))
    print('PASS - step 1240')
except Exception as e:
    print('FAIL - step 1240' if isinstance(e, AssertionError) else f'ERROR - step 1240: {e}')

print("STEP 1241 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1241')
except Exception as e:
    print('FAIL - step 1241' if isinstance(e, AssertionError) else f'ERROR - step 1241: {e}')

print("STEP 1242 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1242')
except Exception as e:
    print('FAIL - step 1242' if isinstance(e, AssertionError) else f'ERROR - step 1242: {e}')

print("STEP 1243 - Check element noscript#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "noscript")))
    print('PASS - step 1243')
except Exception as e:
    print('FAIL - step 1243' if isinstance(e, AssertionError) else f'ERROR - step 1243: {e}')

print("STEP 1244 - Check element picture#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "picture")))
    print('PASS - step 1244')
except Exception as e:
    print('FAIL - step 1244' if isinstance(e, AssertionError) else f'ERROR - step 1244: {e}')

print("STEP 1245 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1245')
except Exception as e:
    print('FAIL - step 1245' if isinstance(e, AssertionError) else f'ERROR - step 1245: {e}')

print("STEP 1246 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1246')
except Exception as e:
    print('FAIL - step 1246' if isinstance(e, AssertionError) else f'ERROR - step 1246: {e}')

print("STEP 1247 - Check element div#None.['media-gallery-bottom-content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-bottom-content']")))
    print('PASS - step 1247')
except Exception as e:
    print('FAIL - step 1247' if isinstance(e, AssertionError) else f'ERROR - step 1247: {e}')

print("STEP 1248 - Check element div#None.['button', 'button-neutral', 'media-gallery-button']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['button', 'button-neutral', 'media-gallery-button']")))
    print('PASS - step 1248')
except Exception as e:
    print('FAIL - step 1248' if isinstance(e, AssertionError) else f'ERROR - step 1248: {e}')

print("STEP 1249 - Check element p#None.['media-gallery-longnote']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-longnote']")))
    print('PASS - step 1249')
except Exception as e:
    print('FAIL - step 1249' if isinstance(e, AssertionError) else f'ERROR - step 1249: {e}')

print("STEP 1250 - Check element span#None.['media-gallery-genre']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-genre']")))
    print('PASS - step 1250')
except Exception as e:
    print('FAIL - step 1250' if isinstance(e, AssertionError) else f'ERROR - step 1250: {e}')

print("STEP 1251 - Check element li#endless-entertainment-gallery-item-2.['media-gallery-item', 'theme-dark']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "endless-entertainment-gallery-item-2")))
    print('PASS - step 1251')
except Exception as e:
    print('FAIL - step 1251' if isinstance(e, AssertionError) else f'ERROR - step 1251: {e}')

print("STEP 1252 - Check element a#media-gallery-item-2-link.['media-gallery-wrapper-link', 'fam-media-gallery-wrapper-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "media-gallery-item-2-link")))
    print('PASS - step 1252')
except Exception as e:
    print('FAIL - step 1252' if isinstance(e, AssertionError) else f'ERROR - step 1252: {e}')

print("STEP 1253 - Check element div#None.['media-gallery-bg-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-bg-wrapper']")))
    print('PASS - step 1253')
except Exception as e:
    print('FAIL - step 1253' if isinstance(e, AssertionError) else f'ERROR - step 1253: {e}')

print("STEP 1254 - Check element picture#None.['media-gallery-bg']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-bg']")))
    print('PASS - step 1254')
except Exception as e:
    print('FAIL - step 1254' if isinstance(e, AssertionError) else f'ERROR - step 1254: {e}')

print("STEP 1255 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1255')
except Exception as e:
    print('FAIL - step 1255' if isinstance(e, AssertionError) else f'ERROR - step 1255: {e}')

print("STEP 1256 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1256')
except Exception as e:
    print('FAIL - step 1256' if isinstance(e, AssertionError) else f'ERROR - step 1256: {e}')

print("STEP 1257 - Check element noscript#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "noscript")))
    print('PASS - step 1257')
except Exception as e:
    print('FAIL - step 1257' if isinstance(e, AssertionError) else f'ERROR - step 1257: {e}')

print("STEP 1258 - Check element picture#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "picture")))
    print('PASS - step 1258')
except Exception as e:
    print('FAIL - step 1258' if isinstance(e, AssertionError) else f'ERROR - step 1258: {e}')

print("STEP 1259 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1259')
except Exception as e:
    print('FAIL - step 1259' if isinstance(e, AssertionError) else f'ERROR - step 1259: {e}')

print("STEP 1260 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1260')
except Exception as e:
    print('FAIL - step 1260' if isinstance(e, AssertionError) else f'ERROR - step 1260: {e}')

print("STEP 1261 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1261')
except Exception as e:
    print('FAIL - step 1261' if isinstance(e, AssertionError) else f'ERROR - step 1261: {e}')

print("STEP 1262 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1262')
except Exception as e:
    print('FAIL - step 1262' if isinstance(e, AssertionError) else f'ERROR - step 1262: {e}')

print("STEP 1263 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1263')
except Exception as e:
    print('FAIL - step 1263' if isinstance(e, AssertionError) else f'ERROR - step 1263: {e}')

print("STEP 1264 - Check element div#None.['media-gallery-contents']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-contents']")))
    print('PASS - step 1264')
except Exception as e:
    print('FAIL - step 1264' if isinstance(e, AssertionError) else f'ERROR - step 1264: {e}')

print("STEP 1265 - Check element div#None.['media-gallery-top-content', 'tv-gallery-top-content-s-only']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-top-content', 'tv-gallery-top-content-s-only']")))
    print('PASS - step 1265')
except Exception as e:
    print('FAIL - step 1265' if isinstance(e, AssertionError) else f'ERROR - step 1265: {e}')

print("STEP 1266 - Check element picture#None.['tv-gallery-atvplus-logo', 'show-logo']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['tv-gallery-atvplus-logo', 'show-logo']")))
    print('PASS - step 1266')
except Exception as e:
    print('FAIL - step 1266' if isinstance(e, AssertionError) else f'ERROR - step 1266: {e}')

print("STEP 1267 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1267')
except Exception as e:
    print('FAIL - step 1267' if isinstance(e, AssertionError) else f'ERROR - step 1267: {e}')

print("STEP 1268 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1268')
except Exception as e:
    print('FAIL - step 1268' if isinstance(e, AssertionError) else f'ERROR - step 1268: {e}')

print("STEP 1269 - Check element noscript#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "noscript")))
    print('PASS - step 1269')
except Exception as e:
    print('FAIL - step 1269' if isinstance(e, AssertionError) else f'ERROR - step 1269: {e}')

print("STEP 1270 - Check element picture#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "picture")))
    print('PASS - step 1270')
except Exception as e:
    print('FAIL - step 1270' if isinstance(e, AssertionError) else f'ERROR - step 1270: {e}')

print("STEP 1271 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1271')
except Exception as e:
    print('FAIL - step 1271' if isinstance(e, AssertionError) else f'ERROR - step 1271: {e}')

print("STEP 1272 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1272')
except Exception as e:
    print('FAIL - step 1272' if isinstance(e, AssertionError) else f'ERROR - step 1272: {e}')

print("STEP 1273 - Check element picture#None.['tv-gallery-media-logo']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['tv-gallery-media-logo']")))
    print('PASS - step 1273')
except Exception as e:
    print('FAIL - step 1273' if isinstance(e, AssertionError) else f'ERROR - step 1273: {e}')

print("STEP 1274 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1274')
except Exception as e:
    print('FAIL - step 1274' if isinstance(e, AssertionError) else f'ERROR - step 1274: {e}')

print("STEP 1275 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1275')
except Exception as e:
    print('FAIL - step 1275' if isinstance(e, AssertionError) else f'ERROR - step 1275: {e}')

print("STEP 1276 - Check element noscript#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "noscript")))
    print('PASS - step 1276')
except Exception as e:
    print('FAIL - step 1276' if isinstance(e, AssertionError) else f'ERROR - step 1276: {e}')

print("STEP 1277 - Check element picture#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "picture")))
    print('PASS - step 1277')
except Exception as e:
    print('FAIL - step 1277' if isinstance(e, AssertionError) else f'ERROR - step 1277: {e}')

print("STEP 1278 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1278')
except Exception as e:
    print('FAIL - step 1278' if isinstance(e, AssertionError) else f'ERROR - step 1278: {e}')

print("STEP 1279 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1279')
except Exception as e:
    print('FAIL - step 1279' if isinstance(e, AssertionError) else f'ERROR - step 1279: {e}')

print("STEP 1280 - Check element div#None.['media-gallery-bottom-content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-bottom-content']")))
    print('PASS - step 1280')
except Exception as e:
    print('FAIL - step 1280' if isinstance(e, AssertionError) else f'ERROR - step 1280: {e}')

print("STEP 1281 - Check element div#None.['button', 'button-neutral', 'media-gallery-button']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['button', 'button-neutral', 'media-gallery-button']")))
    print('PASS - step 1281')
except Exception as e:
    print('FAIL - step 1281' if isinstance(e, AssertionError) else f'ERROR - step 1281: {e}')

print("STEP 1282 - Check element p#None.['media-gallery-longnote']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-longnote']")))
    print('PASS - step 1282')
except Exception as e:
    print('FAIL - step 1282' if isinstance(e, AssertionError) else f'ERROR - step 1282: {e}')

print("STEP 1283 - Check element span#None.['media-gallery-genre']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-genre']")))
    print('PASS - step 1283')
except Exception as e:
    print('FAIL - step 1283' if isinstance(e, AssertionError) else f'ERROR - step 1283: {e}')

print("STEP 1284 - Check element li#endless-entertainment-gallery-item-3.['media-gallery-item', 'theme-dark']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "endless-entertainment-gallery-item-3")))
    print('PASS - step 1284')
except Exception as e:
    print('FAIL - step 1284' if isinstance(e, AssertionError) else f'ERROR - step 1284: {e}')

print("STEP 1285 - Check element a#media-gallery-item-3-link.['media-gallery-wrapper-link', 'fam-media-gallery-wrapper-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "media-gallery-item-3-link")))
    print('PASS - step 1285')
except Exception as e:
    print('FAIL - step 1285' if isinstance(e, AssertionError) else f'ERROR - step 1285: {e}')

print("STEP 1286 - Check element div#None.['media-gallery-bg-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-bg-wrapper']")))
    print('PASS - step 1286')
except Exception as e:
    print('FAIL - step 1286' if isinstance(e, AssertionError) else f'ERROR - step 1286: {e}')

print("STEP 1287 - Check element picture#None.['media-gallery-bg']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-bg']")))
    print('PASS - step 1287')
except Exception as e:
    print('FAIL - step 1287' if isinstance(e, AssertionError) else f'ERROR - step 1287: {e}')

print("STEP 1288 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1288')
except Exception as e:
    print('FAIL - step 1288' if isinstance(e, AssertionError) else f'ERROR - step 1288: {e}')

print("STEP 1289 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1289')
except Exception as e:
    print('FAIL - step 1289' if isinstance(e, AssertionError) else f'ERROR - step 1289: {e}')

print("STEP 1290 - Check element noscript#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "noscript")))
    print('PASS - step 1290')
except Exception as e:
    print('FAIL - step 1290' if isinstance(e, AssertionError) else f'ERROR - step 1290: {e}')

print("STEP 1291 - Check element picture#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "picture")))
    print('PASS - step 1291')
except Exception as e:
    print('FAIL - step 1291' if isinstance(e, AssertionError) else f'ERROR - step 1291: {e}')

print("STEP 1292 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1292')
except Exception as e:
    print('FAIL - step 1292' if isinstance(e, AssertionError) else f'ERROR - step 1292: {e}')

print("STEP 1293 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1293')
except Exception as e:
    print('FAIL - step 1293' if isinstance(e, AssertionError) else f'ERROR - step 1293: {e}')

print("STEP 1294 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1294')
except Exception as e:
    print('FAIL - step 1294' if isinstance(e, AssertionError) else f'ERROR - step 1294: {e}')

print("STEP 1295 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1295')
except Exception as e:
    print('FAIL - step 1295' if isinstance(e, AssertionError) else f'ERROR - step 1295: {e}')

print("STEP 1296 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1296')
except Exception as e:
    print('FAIL - step 1296' if isinstance(e, AssertionError) else f'ERROR - step 1296: {e}')

print("STEP 1297 - Check element div#None.['media-gallery-contents']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-contents']")))
    print('PASS - step 1297')
except Exception as e:
    print('FAIL - step 1297' if isinstance(e, AssertionError) else f'ERROR - step 1297: {e}')

print("STEP 1298 - Check element div#None.['media-gallery-top-content', 'tv-gallery-top-content-s-only']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-top-content', 'tv-gallery-top-content-s-only']")))
    print('PASS - step 1298')
except Exception as e:
    print('FAIL - step 1298' if isinstance(e, AssertionError) else f'ERROR - step 1298: {e}')

print("STEP 1299 - Check element picture#None.['tv-gallery-atvplus-logo', 'show-logo']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['tv-gallery-atvplus-logo', 'show-logo']")))
    print('PASS - step 1299')
except Exception as e:
    print('FAIL - step 1299' if isinstance(e, AssertionError) else f'ERROR - step 1299: {e}')

print("STEP 1300 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1300')
except Exception as e:
    print('FAIL - step 1300' if isinstance(e, AssertionError) else f'ERROR - step 1300: {e}')

print("STEP 1301 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1301')
except Exception as e:
    print('FAIL - step 1301' if isinstance(e, AssertionError) else f'ERROR - step 1301: {e}')

print("STEP 1302 - Check element noscript#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "noscript")))
    print('PASS - step 1302')
except Exception as e:
    print('FAIL - step 1302' if isinstance(e, AssertionError) else f'ERROR - step 1302: {e}')

print("STEP 1303 - Check element picture#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "picture")))
    print('PASS - step 1303')
except Exception as e:
    print('FAIL - step 1303' if isinstance(e, AssertionError) else f'ERROR - step 1303: {e}')

print("STEP 1304 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1304')
except Exception as e:
    print('FAIL - step 1304' if isinstance(e, AssertionError) else f'ERROR - step 1304: {e}')

print("STEP 1305 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1305')
except Exception as e:
    print('FAIL - step 1305' if isinstance(e, AssertionError) else f'ERROR - step 1305: {e}')

print("STEP 1306 - Check element picture#None.['tv-gallery-media-logo']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['tv-gallery-media-logo']")))
    print('PASS - step 1306')
except Exception as e:
    print('FAIL - step 1306' if isinstance(e, AssertionError) else f'ERROR - step 1306: {e}')

print("STEP 1307 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1307')
except Exception as e:
    print('FAIL - step 1307' if isinstance(e, AssertionError) else f'ERROR - step 1307: {e}')

print("STEP 1308 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1308')
except Exception as e:
    print('FAIL - step 1308' if isinstance(e, AssertionError) else f'ERROR - step 1308: {e}')

print("STEP 1309 - Check element noscript#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "noscript")))
    print('PASS - step 1309')
except Exception as e:
    print('FAIL - step 1309' if isinstance(e, AssertionError) else f'ERROR - step 1309: {e}')

print("STEP 1310 - Check element picture#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "picture")))
    print('PASS - step 1310')
except Exception as e:
    print('FAIL - step 1310' if isinstance(e, AssertionError) else f'ERROR - step 1310: {e}')

print("STEP 1311 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1311')
except Exception as e:
    print('FAIL - step 1311' if isinstance(e, AssertionError) else f'ERROR - step 1311: {e}')

print("STEP 1312 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1312')
except Exception as e:
    print('FAIL - step 1312' if isinstance(e, AssertionError) else f'ERROR - step 1312: {e}')

print("STEP 1313 - Check element div#None.['media-gallery-bottom-content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-bottom-content']")))
    print('PASS - step 1313')
except Exception as e:
    print('FAIL - step 1313' if isinstance(e, AssertionError) else f'ERROR - step 1313: {e}')

print("STEP 1314 - Check element div#None.['button', 'button-neutral', 'media-gallery-button']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['button', 'button-neutral', 'media-gallery-button']")))
    print('PASS - step 1314')
except Exception as e:
    print('FAIL - step 1314' if isinstance(e, AssertionError) else f'ERROR - step 1314: {e}')

print("STEP 1315 - Check element p#None.['media-gallery-longnote']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-longnote']")))
    print('PASS - step 1315')
except Exception as e:
    print('FAIL - step 1315' if isinstance(e, AssertionError) else f'ERROR - step 1315: {e}')

print("STEP 1316 - Check element span#None.['media-gallery-genre']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-genre']")))
    print('PASS - step 1316')
except Exception as e:
    print('FAIL - step 1316' if isinstance(e, AssertionError) else f'ERROR - step 1316: {e}')

print("STEP 1317 - Check element li#endless-entertainment-gallery-item-4.['media-gallery-item', 'theme-dark']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "endless-entertainment-gallery-item-4")))
    print('PASS - step 1317')
except Exception as e:
    print('FAIL - step 1317' if isinstance(e, AssertionError) else f'ERROR - step 1317: {e}')

print("STEP 1318 - Check element a#media-gallery-item-4-link.['media-gallery-wrapper-link', 'fam-media-gallery-wrapper-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "media-gallery-item-4-link")))
    print('PASS - step 1318')
except Exception as e:
    print('FAIL - step 1318' if isinstance(e, AssertionError) else f'ERROR - step 1318: {e}')

print("STEP 1319 - Check element div#None.['media-gallery-bg-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-bg-wrapper']")))
    print('PASS - step 1319')
except Exception as e:
    print('FAIL - step 1319' if isinstance(e, AssertionError) else f'ERROR - step 1319: {e}')

print("STEP 1320 - Check element picture#None.['media-gallery-bg']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-bg']")))
    print('PASS - step 1320')
except Exception as e:
    print('FAIL - step 1320' if isinstance(e, AssertionError) else f'ERROR - step 1320: {e}')

print("STEP 1321 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1321')
except Exception as e:
    print('FAIL - step 1321' if isinstance(e, AssertionError) else f'ERROR - step 1321: {e}')

print("STEP 1322 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1322')
except Exception as e:
    print('FAIL - step 1322' if isinstance(e, AssertionError) else f'ERROR - step 1322: {e}')

print("STEP 1323 - Check element noscript#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "noscript")))
    print('PASS - step 1323')
except Exception as e:
    print('FAIL - step 1323' if isinstance(e, AssertionError) else f'ERROR - step 1323: {e}')

print("STEP 1324 - Check element picture#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "picture")))
    print('PASS - step 1324')
except Exception as e:
    print('FAIL - step 1324' if isinstance(e, AssertionError) else f'ERROR - step 1324: {e}')

print("STEP 1325 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1325')
except Exception as e:
    print('FAIL - step 1325' if isinstance(e, AssertionError) else f'ERROR - step 1325: {e}')

print("STEP 1326 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1326')
except Exception as e:
    print('FAIL - step 1326' if isinstance(e, AssertionError) else f'ERROR - step 1326: {e}')

print("STEP 1327 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1327')
except Exception as e:
    print('FAIL - step 1327' if isinstance(e, AssertionError) else f'ERROR - step 1327: {e}')

print("STEP 1328 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1328')
except Exception as e:
    print('FAIL - step 1328' if isinstance(e, AssertionError) else f'ERROR - step 1328: {e}')

print("STEP 1329 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1329')
except Exception as e:
    print('FAIL - step 1329' if isinstance(e, AssertionError) else f'ERROR - step 1329: {e}')

print("STEP 1330 - Check element div#None.['media-gallery-contents']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-contents']")))
    print('PASS - step 1330')
except Exception as e:
    print('FAIL - step 1330' if isinstance(e, AssertionError) else f'ERROR - step 1330: {e}')

print("STEP 1331 - Check element div#None.['media-gallery-top-content', 'tv-gallery-top-content-s-only']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-top-content', 'tv-gallery-top-content-s-only']")))
    print('PASS - step 1331')
except Exception as e:
    print('FAIL - step 1331' if isinstance(e, AssertionError) else f'ERROR - step 1331: {e}')

print("STEP 1332 - Check element picture#None.['tv-gallery-atvplus-logo', 'show-logo']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['tv-gallery-atvplus-logo', 'show-logo']")))
    print('PASS - step 1332')
except Exception as e:
    print('FAIL - step 1332' if isinstance(e, AssertionError) else f'ERROR - step 1332: {e}')

print("STEP 1333 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1333')
except Exception as e:
    print('FAIL - step 1333' if isinstance(e, AssertionError) else f'ERROR - step 1333: {e}')

print("STEP 1334 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1334')
except Exception as e:
    print('FAIL - step 1334' if isinstance(e, AssertionError) else f'ERROR - step 1334: {e}')

print("STEP 1335 - Check element noscript#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "noscript")))
    print('PASS - step 1335')
except Exception as e:
    print('FAIL - step 1335' if isinstance(e, AssertionError) else f'ERROR - step 1335: {e}')

print("STEP 1336 - Check element picture#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "picture")))
    print('PASS - step 1336')
except Exception as e:
    print('FAIL - step 1336' if isinstance(e, AssertionError) else f'ERROR - step 1336: {e}')

print("STEP 1337 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1337')
except Exception as e:
    print('FAIL - step 1337' if isinstance(e, AssertionError) else f'ERROR - step 1337: {e}')

print("STEP 1338 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1338')
except Exception as e:
    print('FAIL - step 1338' if isinstance(e, AssertionError) else f'ERROR - step 1338: {e}')

print("STEP 1339 - Check element picture#None.['tv-gallery-media-logo']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['tv-gallery-media-logo']")))
    print('PASS - step 1339')
except Exception as e:
    print('FAIL - step 1339' if isinstance(e, AssertionError) else f'ERROR - step 1339: {e}')

print("STEP 1340 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1340')
except Exception as e:
    print('FAIL - step 1340' if isinstance(e, AssertionError) else f'ERROR - step 1340: {e}')

print("STEP 1341 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1341')
except Exception as e:
    print('FAIL - step 1341' if isinstance(e, AssertionError) else f'ERROR - step 1341: {e}')

print("STEP 1342 - Check element noscript#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "noscript")))
    print('PASS - step 1342')
except Exception as e:
    print('FAIL - step 1342' if isinstance(e, AssertionError) else f'ERROR - step 1342: {e}')

print("STEP 1343 - Check element picture#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "picture")))
    print('PASS - step 1343')
except Exception as e:
    print('FAIL - step 1343' if isinstance(e, AssertionError) else f'ERROR - step 1343: {e}')

print("STEP 1344 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1344')
except Exception as e:
    print('FAIL - step 1344' if isinstance(e, AssertionError) else f'ERROR - step 1344: {e}')

print("STEP 1345 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1345')
except Exception as e:
    print('FAIL - step 1345' if isinstance(e, AssertionError) else f'ERROR - step 1345: {e}')

print("STEP 1346 - Check element div#None.['media-gallery-bottom-content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-bottom-content']")))
    print('PASS - step 1346')
except Exception as e:
    print('FAIL - step 1346' if isinstance(e, AssertionError) else f'ERROR - step 1346: {e}')

print("STEP 1347 - Check element div#None.['button', 'button-neutral', 'media-gallery-button']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['button', 'button-neutral', 'media-gallery-button']")))
    print('PASS - step 1347')
except Exception as e:
    print('FAIL - step 1347' if isinstance(e, AssertionError) else f'ERROR - step 1347: {e}')

print("STEP 1348 - Check element p#None.['media-gallery-longnote']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-longnote']")))
    print('PASS - step 1348')
except Exception as e:
    print('FAIL - step 1348' if isinstance(e, AssertionError) else f'ERROR - step 1348: {e}')

print("STEP 1349 - Check element span#None.['media-gallery-genre']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-genre']")))
    print('PASS - step 1349')
except Exception as e:
    print('FAIL - step 1349' if isinstance(e, AssertionError) else f'ERROR - step 1349: {e}')

print("STEP 1350 - Check element li#endless-entertainment-gallery-item-5.['media-gallery-item', 'theme-dark']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "endless-entertainment-gallery-item-5")))
    print('PASS - step 1350')
except Exception as e:
    print('FAIL - step 1350' if isinstance(e, AssertionError) else f'ERROR - step 1350: {e}')

print("STEP 1351 - Check element a#media-gallery-item-5-link.['media-gallery-wrapper-link', 'fam-media-gallery-wrapper-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "media-gallery-item-5-link")))
    print('PASS - step 1351')
except Exception as e:
    print('FAIL - step 1351' if isinstance(e, AssertionError) else f'ERROR - step 1351: {e}')

print("STEP 1352 - Check element div#None.['media-gallery-bg-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-bg-wrapper']")))
    print('PASS - step 1352')
except Exception as e:
    print('FAIL - step 1352' if isinstance(e, AssertionError) else f'ERROR - step 1352: {e}')

print("STEP 1353 - Check element picture#None.['media-gallery-bg']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-bg']")))
    print('PASS - step 1353')
except Exception as e:
    print('FAIL - step 1353' if isinstance(e, AssertionError) else f'ERROR - step 1353: {e}')

print("STEP 1354 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1354')
except Exception as e:
    print('FAIL - step 1354' if isinstance(e, AssertionError) else f'ERROR - step 1354: {e}')

print("STEP 1355 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1355')
except Exception as e:
    print('FAIL - step 1355' if isinstance(e, AssertionError) else f'ERROR - step 1355: {e}')

print("STEP 1356 - Check element noscript#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "noscript")))
    print('PASS - step 1356')
except Exception as e:
    print('FAIL - step 1356' if isinstance(e, AssertionError) else f'ERROR - step 1356: {e}')

print("STEP 1357 - Check element picture#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "picture")))
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

print("STEP 1360 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1360')
except Exception as e:
    print('FAIL - step 1360' if isinstance(e, AssertionError) else f'ERROR - step 1360: {e}')

print("STEP 1361 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1361')
except Exception as e:
    print('FAIL - step 1361' if isinstance(e, AssertionError) else f'ERROR - step 1361: {e}')

print("STEP 1362 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1362')
except Exception as e:
    print('FAIL - step 1362' if isinstance(e, AssertionError) else f'ERROR - step 1362: {e}')

print("STEP 1363 - Check element div#None.['media-gallery-contents']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-contents']")))
    print('PASS - step 1363')
except Exception as e:
    print('FAIL - step 1363' if isinstance(e, AssertionError) else f'ERROR - step 1363: {e}')

print("STEP 1364 - Check element div#None.['media-gallery-top-content', 'tv-gallery-top-content-s-only']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-top-content', 'tv-gallery-top-content-s-only']")))
    print('PASS - step 1364')
except Exception as e:
    print('FAIL - step 1364' if isinstance(e, AssertionError) else f'ERROR - step 1364: {e}')

print("STEP 1365 - Check element picture#None.['tv-gallery-atvplus-logo', 'show-logo']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['tv-gallery-atvplus-logo', 'show-logo']")))
    print('PASS - step 1365')
except Exception as e:
    print('FAIL - step 1365' if isinstance(e, AssertionError) else f'ERROR - step 1365: {e}')

print("STEP 1366 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1366')
except Exception as e:
    print('FAIL - step 1366' if isinstance(e, AssertionError) else f'ERROR - step 1366: {e}')

print("STEP 1367 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1367')
except Exception as e:
    print('FAIL - step 1367' if isinstance(e, AssertionError) else f'ERROR - step 1367: {e}')

print("STEP 1368 - Check element noscript#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "noscript")))
    print('PASS - step 1368')
except Exception as e:
    print('FAIL - step 1368' if isinstance(e, AssertionError) else f'ERROR - step 1368: {e}')

print("STEP 1369 - Check element picture#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "picture")))
    print('PASS - step 1369')
except Exception as e:
    print('FAIL - step 1369' if isinstance(e, AssertionError) else f'ERROR - step 1369: {e}')

print("STEP 1370 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1370')
except Exception as e:
    print('FAIL - step 1370' if isinstance(e, AssertionError) else f'ERROR - step 1370: {e}')

print("STEP 1371 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1371')
except Exception as e:
    print('FAIL - step 1371' if isinstance(e, AssertionError) else f'ERROR - step 1371: {e}')

print("STEP 1372 - Check element picture#None.['tv-gallery-media-logo']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['tv-gallery-media-logo']")))
    print('PASS - step 1372')
except Exception as e:
    print('FAIL - step 1372' if isinstance(e, AssertionError) else f'ERROR - step 1372: {e}')

print("STEP 1373 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1373')
except Exception as e:
    print('FAIL - step 1373' if isinstance(e, AssertionError) else f'ERROR - step 1373: {e}')

print("STEP 1374 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1374')
except Exception as e:
    print('FAIL - step 1374' if isinstance(e, AssertionError) else f'ERROR - step 1374: {e}')

print("STEP 1375 - Check element noscript#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "noscript")))
    print('PASS - step 1375')
except Exception as e:
    print('FAIL - step 1375' if isinstance(e, AssertionError) else f'ERROR - step 1375: {e}')

print("STEP 1376 - Check element picture#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "picture")))
    print('PASS - step 1376')
except Exception as e:
    print('FAIL - step 1376' if isinstance(e, AssertionError) else f'ERROR - step 1376: {e}')

print("STEP 1377 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1377')
except Exception as e:
    print('FAIL - step 1377' if isinstance(e, AssertionError) else f'ERROR - step 1377: {e}')

print("STEP 1378 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1378')
except Exception as e:
    print('FAIL - step 1378' if isinstance(e, AssertionError) else f'ERROR - step 1378: {e}')

print("STEP 1379 - Check element div#None.['media-gallery-bottom-content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-bottom-content']")))
    print('PASS - step 1379')
except Exception as e:
    print('FAIL - step 1379' if isinstance(e, AssertionError) else f'ERROR - step 1379: {e}')

print("STEP 1380 - Check element div#None.['button', 'button-neutral', 'media-gallery-button']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['button', 'button-neutral', 'media-gallery-button']")))
    print('PASS - step 1380')
except Exception as e:
    print('FAIL - step 1380' if isinstance(e, AssertionError) else f'ERROR - step 1380: {e}')

print("STEP 1381 - Check element p#None.['media-gallery-longnote']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-longnote']")))
    print('PASS - step 1381')
except Exception as e:
    print('FAIL - step 1381' if isinstance(e, AssertionError) else f'ERROR - step 1381: {e}')

print("STEP 1382 - Check element span#None.['media-gallery-genre']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-genre']")))
    print('PASS - step 1382')
except Exception as e:
    print('FAIL - step 1382' if isinstance(e, AssertionError) else f'ERROR - step 1382: {e}')

print("STEP 1383 - Check element li#endless-entertainment-gallery-item-6.['media-gallery-item', 'theme-dark']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "endless-entertainment-gallery-item-6")))
    print('PASS - step 1383')
except Exception as e:
    print('FAIL - step 1383' if isinstance(e, AssertionError) else f'ERROR - step 1383: {e}')

print("STEP 1384 - Check element a#media-gallery-item-6-link.['media-gallery-wrapper-link', 'fam-media-gallery-wrapper-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "media-gallery-item-6-link")))
    print('PASS - step 1384')
except Exception as e:
    print('FAIL - step 1384' if isinstance(e, AssertionError) else f'ERROR - step 1384: {e}')

print("STEP 1385 - Check element div#None.['media-gallery-bg-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-bg-wrapper']")))
    print('PASS - step 1385')
except Exception as e:
    print('FAIL - step 1385' if isinstance(e, AssertionError) else f'ERROR - step 1385: {e}')

print("STEP 1386 - Check element picture#None.['media-gallery-bg']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-bg']")))
    print('PASS - step 1386')
except Exception as e:
    print('FAIL - step 1386' if isinstance(e, AssertionError) else f'ERROR - step 1386: {e}')

print("STEP 1387 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1387')
except Exception as e:
    print('FAIL - step 1387' if isinstance(e, AssertionError) else f'ERROR - step 1387: {e}')

print("STEP 1388 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1388')
except Exception as e:
    print('FAIL - step 1388' if isinstance(e, AssertionError) else f'ERROR - step 1388: {e}')

print("STEP 1389 - Check element noscript#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "noscript")))
    print('PASS - step 1389')
except Exception as e:
    print('FAIL - step 1389' if isinstance(e, AssertionError) else f'ERROR - step 1389: {e}')

print("STEP 1390 - Check element picture#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "picture")))
    print('PASS - step 1390')
except Exception as e:
    print('FAIL - step 1390' if isinstance(e, AssertionError) else f'ERROR - step 1390: {e}')

print("STEP 1391 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1391')
except Exception as e:
    print('FAIL - step 1391' if isinstance(e, AssertionError) else f'ERROR - step 1391: {e}')

print("STEP 1392 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1392')
except Exception as e:
    print('FAIL - step 1392' if isinstance(e, AssertionError) else f'ERROR - step 1392: {e}')

print("STEP 1393 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1393')
except Exception as e:
    print('FAIL - step 1393' if isinstance(e, AssertionError) else f'ERROR - step 1393: {e}')

print("STEP 1394 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1394')
except Exception as e:
    print('FAIL - step 1394' if isinstance(e, AssertionError) else f'ERROR - step 1394: {e}')

print("STEP 1395 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1395')
except Exception as e:
    print('FAIL - step 1395' if isinstance(e, AssertionError) else f'ERROR - step 1395: {e}')

print("STEP 1396 - Check element div#None.['media-gallery-contents']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-contents']")))
    print('PASS - step 1396')
except Exception as e:
    print('FAIL - step 1396' if isinstance(e, AssertionError) else f'ERROR - step 1396: {e}')

print("STEP 1397 - Check element div#None.['media-gallery-top-content', 'tv-gallery-top-content-s-only']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-top-content', 'tv-gallery-top-content-s-only']")))
    print('PASS - step 1397')
except Exception as e:
    print('FAIL - step 1397' if isinstance(e, AssertionError) else f'ERROR - step 1397: {e}')

print("STEP 1398 - Check element picture#None.['tv-gallery-atvplus-logo', 'show-logo']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['tv-gallery-atvplus-logo', 'show-logo']")))
    print('PASS - step 1398')
except Exception as e:
    print('FAIL - step 1398' if isinstance(e, AssertionError) else f'ERROR - step 1398: {e}')

print("STEP 1399 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1399')
except Exception as e:
    print('FAIL - step 1399' if isinstance(e, AssertionError) else f'ERROR - step 1399: {e}')

print("STEP 1400 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1400')
except Exception as e:
    print('FAIL - step 1400' if isinstance(e, AssertionError) else f'ERROR - step 1400: {e}')

print("STEP 1401 - Check element noscript#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "noscript")))
    print('PASS - step 1401')
except Exception as e:
    print('FAIL - step 1401' if isinstance(e, AssertionError) else f'ERROR - step 1401: {e}')

print("STEP 1402 - Check element picture#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "picture")))
    print('PASS - step 1402')
except Exception as e:
    print('FAIL - step 1402' if isinstance(e, AssertionError) else f'ERROR - step 1402: {e}')

print("STEP 1403 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1403')
except Exception as e:
    print('FAIL - step 1403' if isinstance(e, AssertionError) else f'ERROR - step 1403: {e}')

print("STEP 1404 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1404')
except Exception as e:
    print('FAIL - step 1404' if isinstance(e, AssertionError) else f'ERROR - step 1404: {e}')

print("STEP 1405 - Check element picture#None.['tv-gallery-media-logo']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['tv-gallery-media-logo']")))
    print('PASS - step 1405')
except Exception as e:
    print('FAIL - step 1405' if isinstance(e, AssertionError) else f'ERROR - step 1405: {e}')

print("STEP 1406 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1406')
except Exception as e:
    print('FAIL - step 1406' if isinstance(e, AssertionError) else f'ERROR - step 1406: {e}')

print("STEP 1407 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1407')
except Exception as e:
    print('FAIL - step 1407' if isinstance(e, AssertionError) else f'ERROR - step 1407: {e}')

print("STEP 1408 - Check element noscript#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "noscript")))
    print('PASS - step 1408')
except Exception as e:
    print('FAIL - step 1408' if isinstance(e, AssertionError) else f'ERROR - step 1408: {e}')

print("STEP 1409 - Check element picture#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "picture")))
    print('PASS - step 1409')
except Exception as e:
    print('FAIL - step 1409' if isinstance(e, AssertionError) else f'ERROR - step 1409: {e}')

print("STEP 1410 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1410')
except Exception as e:
    print('FAIL - step 1410' if isinstance(e, AssertionError) else f'ERROR - step 1410: {e}')

print("STEP 1411 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1411')
except Exception as e:
    print('FAIL - step 1411' if isinstance(e, AssertionError) else f'ERROR - step 1411: {e}')

print("STEP 1412 - Check element div#None.['media-gallery-bottom-content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-bottom-content']")))
    print('PASS - step 1412')
except Exception as e:
    print('FAIL - step 1412' if isinstance(e, AssertionError) else f'ERROR - step 1412: {e}')

print("STEP 1413 - Check element div#None.['button', 'button-neutral', 'media-gallery-button']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['button', 'button-neutral', 'media-gallery-button']")))
    print('PASS - step 1413')
except Exception as e:
    print('FAIL - step 1413' if isinstance(e, AssertionError) else f'ERROR - step 1413: {e}')

print("STEP 1414 - Check element p#None.['media-gallery-longnote']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-longnote']")))
    print('PASS - step 1414')
except Exception as e:
    print('FAIL - step 1414' if isinstance(e, AssertionError) else f'ERROR - step 1414: {e}')

print("STEP 1415 - Check element span#None.['media-gallery-genre']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-genre']")))
    print('PASS - step 1415')
except Exception as e:
    print('FAIL - step 1415' if isinstance(e, AssertionError) else f'ERROR - step 1415: {e}')

print("STEP 1416 - Check element li#endless-entertainment-gallery-item-7.['media-gallery-item', 'theme-dark']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "endless-entertainment-gallery-item-7")))
    print('PASS - step 1416')
except Exception as e:
    print('FAIL - step 1416' if isinstance(e, AssertionError) else f'ERROR - step 1416: {e}')

print("STEP 1417 - Check element a#media-gallery-item-7-link.['media-gallery-wrapper-link', 'fam-media-gallery-wrapper-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "media-gallery-item-7-link")))
    print('PASS - step 1417')
except Exception as e:
    print('FAIL - step 1417' if isinstance(e, AssertionError) else f'ERROR - step 1417: {e}')

print("STEP 1418 - Check element div#None.['media-gallery-bg-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-bg-wrapper']")))
    print('PASS - step 1418')
except Exception as e:
    print('FAIL - step 1418' if isinstance(e, AssertionError) else f'ERROR - step 1418: {e}')

print("STEP 1419 - Check element picture#None.['media-gallery-bg']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-bg']")))
    print('PASS - step 1419')
except Exception as e:
    print('FAIL - step 1419' if isinstance(e, AssertionError) else f'ERROR - step 1419: {e}')

print("STEP 1420 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1420')
except Exception as e:
    print('FAIL - step 1420' if isinstance(e, AssertionError) else f'ERROR - step 1420: {e}')

print("STEP 1421 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1421')
except Exception as e:
    print('FAIL - step 1421' if isinstance(e, AssertionError) else f'ERROR - step 1421: {e}')

print("STEP 1422 - Check element noscript#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "noscript")))
    print('PASS - step 1422')
except Exception as e:
    print('FAIL - step 1422' if isinstance(e, AssertionError) else f'ERROR - step 1422: {e}')

print("STEP 1423 - Check element picture#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "picture")))
    print('PASS - step 1423')
except Exception as e:
    print('FAIL - step 1423' if isinstance(e, AssertionError) else f'ERROR - step 1423: {e}')

print("STEP 1424 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1424')
except Exception as e:
    print('FAIL - step 1424' if isinstance(e, AssertionError) else f'ERROR - step 1424: {e}')

print("STEP 1425 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1425')
except Exception as e:
    print('FAIL - step 1425' if isinstance(e, AssertionError) else f'ERROR - step 1425: {e}')

print("STEP 1426 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1426')
except Exception as e:
    print('FAIL - step 1426' if isinstance(e, AssertionError) else f'ERROR - step 1426: {e}')

print("STEP 1427 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1427')
except Exception as e:
    print('FAIL - step 1427' if isinstance(e, AssertionError) else f'ERROR - step 1427: {e}')

print("STEP 1428 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1428')
except Exception as e:
    print('FAIL - step 1428' if isinstance(e, AssertionError) else f'ERROR - step 1428: {e}')

print("STEP 1429 - Check element div#None.['media-gallery-contents']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-contents']")))
    print('PASS - step 1429')
except Exception as e:
    print('FAIL - step 1429' if isinstance(e, AssertionError) else f'ERROR - step 1429: {e}')

print("STEP 1430 - Check element div#None.['media-gallery-top-content', 'tv-gallery-top-content-s-only']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-top-content', 'tv-gallery-top-content-s-only']")))
    print('PASS - step 1430')
except Exception as e:
    print('FAIL - step 1430' if isinstance(e, AssertionError) else f'ERROR - step 1430: {e}')

print("STEP 1431 - Check element picture#None.['tv-gallery-atvplus-logo', 'show-logo']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['tv-gallery-atvplus-logo', 'show-logo']")))
    print('PASS - step 1431')
except Exception as e:
    print('FAIL - step 1431' if isinstance(e, AssertionError) else f'ERROR - step 1431: {e}')

print("STEP 1432 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1432')
except Exception as e:
    print('FAIL - step 1432' if isinstance(e, AssertionError) else f'ERROR - step 1432: {e}')

print("STEP 1433 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1433')
except Exception as e:
    print('FAIL - step 1433' if isinstance(e, AssertionError) else f'ERROR - step 1433: {e}')

print("STEP 1434 - Check element noscript#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "noscript")))
    print('PASS - step 1434')
except Exception as e:
    print('FAIL - step 1434' if isinstance(e, AssertionError) else f'ERROR - step 1434: {e}')

print("STEP 1435 - Check element picture#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "picture")))
    print('PASS - step 1435')
except Exception as e:
    print('FAIL - step 1435' if isinstance(e, AssertionError) else f'ERROR - step 1435: {e}')

print("STEP 1436 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1436')
except Exception as e:
    print('FAIL - step 1436' if isinstance(e, AssertionError) else f'ERROR - step 1436: {e}')

print("STEP 1437 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1437')
except Exception as e:
    print('FAIL - step 1437' if isinstance(e, AssertionError) else f'ERROR - step 1437: {e}')

print("STEP 1438 - Check element picture#None.['tv-gallery-media-logo']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['tv-gallery-media-logo']")))
    print('PASS - step 1438')
except Exception as e:
    print('FAIL - step 1438' if isinstance(e, AssertionError) else f'ERROR - step 1438: {e}')

print("STEP 1439 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1439')
except Exception as e:
    print('FAIL - step 1439' if isinstance(e, AssertionError) else f'ERROR - step 1439: {e}')

print("STEP 1440 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1440')
except Exception as e:
    print('FAIL - step 1440' if isinstance(e, AssertionError) else f'ERROR - step 1440: {e}')

print("STEP 1441 - Check element noscript#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "noscript")))
    print('PASS - step 1441')
except Exception as e:
    print('FAIL - step 1441' if isinstance(e, AssertionError) else f'ERROR - step 1441: {e}')

print("STEP 1442 - Check element picture#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "picture")))
    print('PASS - step 1442')
except Exception as e:
    print('FAIL - step 1442' if isinstance(e, AssertionError) else f'ERROR - step 1442: {e}')

print("STEP 1443 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1443')
except Exception as e:
    print('FAIL - step 1443' if isinstance(e, AssertionError) else f'ERROR - step 1443: {e}')

print("STEP 1444 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1444')
except Exception as e:
    print('FAIL - step 1444' if isinstance(e, AssertionError) else f'ERROR - step 1444: {e}')

print("STEP 1445 - Check element div#None.['media-gallery-bottom-content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-bottom-content']")))
    print('PASS - step 1445')
except Exception as e:
    print('FAIL - step 1445' if isinstance(e, AssertionError) else f'ERROR - step 1445: {e}')

print("STEP 1446 - Check element div#None.['button', 'button-neutral', 'media-gallery-button']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['button', 'button-neutral', 'media-gallery-button']")))
    print('PASS - step 1446')
except Exception as e:
    print('FAIL - step 1446' if isinstance(e, AssertionError) else f'ERROR - step 1446: {e}')

print("STEP 1447 - Check element p#None.['media-gallery-longnote']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-longnote']")))
    print('PASS - step 1447')
except Exception as e:
    print('FAIL - step 1447' if isinstance(e, AssertionError) else f'ERROR - step 1447: {e}')

print("STEP 1448 - Check element span#None.['media-gallery-genre']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-genre']")))
    print('PASS - step 1448')
except Exception as e:
    print('FAIL - step 1448' if isinstance(e, AssertionError) else f'ERROR - step 1448: {e}')

print("STEP 1449 - Check element li#endless-entertainment-gallery-item-8.['media-gallery-item', 'theme-dark']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "endless-entertainment-gallery-item-8")))
    print('PASS - step 1449')
except Exception as e:
    print('FAIL - step 1449' if isinstance(e, AssertionError) else f'ERROR - step 1449: {e}')

print("STEP 1450 - Check element a#media-gallery-item-8-link.['media-gallery-wrapper-link', 'fam-media-gallery-wrapper-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "media-gallery-item-8-link")))
    print('PASS - step 1450')
except Exception as e:
    print('FAIL - step 1450' if isinstance(e, AssertionError) else f'ERROR - step 1450: {e}')

print("STEP 1451 - Check element div#None.['media-gallery-bg-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-bg-wrapper']")))
    print('PASS - step 1451')
except Exception as e:
    print('FAIL - step 1451' if isinstance(e, AssertionError) else f'ERROR - step 1451: {e}')

print("STEP 1452 - Check element picture#None.['media-gallery-bg']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-bg']")))
    print('PASS - step 1452')
except Exception as e:
    print('FAIL - step 1452' if isinstance(e, AssertionError) else f'ERROR - step 1452: {e}')

print("STEP 1453 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1453')
except Exception as e:
    print('FAIL - step 1453' if isinstance(e, AssertionError) else f'ERROR - step 1453: {e}')

print("STEP 1454 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1454')
except Exception as e:
    print('FAIL - step 1454' if isinstance(e, AssertionError) else f'ERROR - step 1454: {e}')

print("STEP 1455 - Check element noscript#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "noscript")))
    print('PASS - step 1455')
except Exception as e:
    print('FAIL - step 1455' if isinstance(e, AssertionError) else f'ERROR - step 1455: {e}')

print("STEP 1456 - Check element picture#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "picture")))
    print('PASS - step 1456')
except Exception as e:
    print('FAIL - step 1456' if isinstance(e, AssertionError) else f'ERROR - step 1456: {e}')

print("STEP 1457 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1457')
except Exception as e:
    print('FAIL - step 1457' if isinstance(e, AssertionError) else f'ERROR - step 1457: {e}')

print("STEP 1458 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1458')
except Exception as e:
    print('FAIL - step 1458' if isinstance(e, AssertionError) else f'ERROR - step 1458: {e}')

print("STEP 1459 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1459')
except Exception as e:
    print('FAIL - step 1459' if isinstance(e, AssertionError) else f'ERROR - step 1459: {e}')

print("STEP 1460 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1460')
except Exception as e:
    print('FAIL - step 1460' if isinstance(e, AssertionError) else f'ERROR - step 1460: {e}')

print("STEP 1461 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1461')
except Exception as e:
    print('FAIL - step 1461' if isinstance(e, AssertionError) else f'ERROR - step 1461: {e}')

print("STEP 1462 - Check element div#None.['media-gallery-contents']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-contents']")))
    print('PASS - step 1462')
except Exception as e:
    print('FAIL - step 1462' if isinstance(e, AssertionError) else f'ERROR - step 1462: {e}')

print("STEP 1463 - Check element div#None.['media-gallery-top-content', 'tv-gallery-top-content-s-only']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-top-content', 'tv-gallery-top-content-s-only']")))
    print('PASS - step 1463')
except Exception as e:
    print('FAIL - step 1463' if isinstance(e, AssertionError) else f'ERROR - step 1463: {e}')

print("STEP 1464 - Check element picture#None.['tv-gallery-atvplus-logo', 'show-logo']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['tv-gallery-atvplus-logo', 'show-logo']")))
    print('PASS - step 1464')
except Exception as e:
    print('FAIL - step 1464' if isinstance(e, AssertionError) else f'ERROR - step 1464: {e}')

print("STEP 1465 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1465')
except Exception as e:
    print('FAIL - step 1465' if isinstance(e, AssertionError) else f'ERROR - step 1465: {e}')

print("STEP 1466 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1466')
except Exception as e:
    print('FAIL - step 1466' if isinstance(e, AssertionError) else f'ERROR - step 1466: {e}')

print("STEP 1467 - Check element noscript#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "noscript")))
    print('PASS - step 1467')
except Exception as e:
    print('FAIL - step 1467' if isinstance(e, AssertionError) else f'ERROR - step 1467: {e}')

print("STEP 1468 - Check element picture#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "picture")))
    print('PASS - step 1468')
except Exception as e:
    print('FAIL - step 1468' if isinstance(e, AssertionError) else f'ERROR - step 1468: {e}')

print("STEP 1469 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1469')
except Exception as e:
    print('FAIL - step 1469' if isinstance(e, AssertionError) else f'ERROR - step 1469: {e}')

print("STEP 1470 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1470')
except Exception as e:
    print('FAIL - step 1470' if isinstance(e, AssertionError) else f'ERROR - step 1470: {e}')

print("STEP 1471 - Check element picture#None.['tv-gallery-media-logo']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['tv-gallery-media-logo']")))
    print('PASS - step 1471')
except Exception as e:
    print('FAIL - step 1471' if isinstance(e, AssertionError) else f'ERROR - step 1471: {e}')

print("STEP 1472 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1472')
except Exception as e:
    print('FAIL - step 1472' if isinstance(e, AssertionError) else f'ERROR - step 1472: {e}')

print("STEP 1473 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1473')
except Exception as e:
    print('FAIL - step 1473' if isinstance(e, AssertionError) else f'ERROR - step 1473: {e}')

print("STEP 1474 - Check element noscript#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "noscript")))
    print('PASS - step 1474')
except Exception as e:
    print('FAIL - step 1474' if isinstance(e, AssertionError) else f'ERROR - step 1474: {e}')

print("STEP 1475 - Check element picture#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "picture")))
    print('PASS - step 1475')
except Exception as e:
    print('FAIL - step 1475' if isinstance(e, AssertionError) else f'ERROR - step 1475: {e}')

print("STEP 1476 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1476')
except Exception as e:
    print('FAIL - step 1476' if isinstance(e, AssertionError) else f'ERROR - step 1476: {e}')

print("STEP 1477 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1477')
except Exception as e:
    print('FAIL - step 1477' if isinstance(e, AssertionError) else f'ERROR - step 1477: {e}')

print("STEP 1478 - Check element div#None.['media-gallery-bottom-content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-bottom-content']")))
    print('PASS - step 1478')
except Exception as e:
    print('FAIL - step 1478' if isinstance(e, AssertionError) else f'ERROR - step 1478: {e}')

print("STEP 1479 - Check element div#None.['button', 'button-neutral', 'media-gallery-button']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['button', 'button-neutral', 'media-gallery-button']")))
    print('PASS - step 1479')
except Exception as e:
    print('FAIL - step 1479' if isinstance(e, AssertionError) else f'ERROR - step 1479: {e}')

print("STEP 1480 - Check element p#None.['media-gallery-longnote']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-longnote']")))
    print('PASS - step 1480')
except Exception as e:
    print('FAIL - step 1480' if isinstance(e, AssertionError) else f'ERROR - step 1480: {e}')

print("STEP 1481 - Check element span#None.['media-gallery-genre']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-genre']")))
    print('PASS - step 1481')
except Exception as e:
    print('FAIL - step 1481' if isinstance(e, AssertionError) else f'ERROR - step 1481: {e}')

print("STEP 1482 - Check element li#endless-entertainment-gallery-item-9.['media-gallery-item', 'theme-dark']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "endless-entertainment-gallery-item-9")))
    print('PASS - step 1482')
except Exception as e:
    print('FAIL - step 1482' if isinstance(e, AssertionError) else f'ERROR - step 1482: {e}')

print("STEP 1483 - Check element a#media-gallery-item-9-link.['media-gallery-wrapper-link', 'fam-media-gallery-wrapper-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "media-gallery-item-9-link")))
    print('PASS - step 1483')
except Exception as e:
    print('FAIL - step 1483' if isinstance(e, AssertionError) else f'ERROR - step 1483: {e}')

print("STEP 1484 - Check element div#None.['media-gallery-bg-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-bg-wrapper']")))
    print('PASS - step 1484')
except Exception as e:
    print('FAIL - step 1484' if isinstance(e, AssertionError) else f'ERROR - step 1484: {e}')

print("STEP 1485 - Check element picture#None.['media-gallery-bg']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-bg']")))
    print('PASS - step 1485')
except Exception as e:
    print('FAIL - step 1485' if isinstance(e, AssertionError) else f'ERROR - step 1485: {e}')

print("STEP 1486 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1486')
except Exception as e:
    print('FAIL - step 1486' if isinstance(e, AssertionError) else f'ERROR - step 1486: {e}')

print("STEP 1487 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1487')
except Exception as e:
    print('FAIL - step 1487' if isinstance(e, AssertionError) else f'ERROR - step 1487: {e}')

print("STEP 1488 - Check element noscript#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "noscript")))
    print('PASS - step 1488')
except Exception as e:
    print('FAIL - step 1488' if isinstance(e, AssertionError) else f'ERROR - step 1488: {e}')

print("STEP 1489 - Check element picture#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "picture")))
    print('PASS - step 1489')
except Exception as e:
    print('FAIL - step 1489' if isinstance(e, AssertionError) else f'ERROR - step 1489: {e}')

print("STEP 1490 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1490')
except Exception as e:
    print('FAIL - step 1490' if isinstance(e, AssertionError) else f'ERROR - step 1490: {e}')

print("STEP 1491 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1491')
except Exception as e:
    print('FAIL - step 1491' if isinstance(e, AssertionError) else f'ERROR - step 1491: {e}')

print("STEP 1492 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1492')
except Exception as e:
    print('FAIL - step 1492' if isinstance(e, AssertionError) else f'ERROR - step 1492: {e}')

print("STEP 1493 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1493')
except Exception as e:
    print('FAIL - step 1493' if isinstance(e, AssertionError) else f'ERROR - step 1493: {e}')

print("STEP 1494 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1494')
except Exception as e:
    print('FAIL - step 1494' if isinstance(e, AssertionError) else f'ERROR - step 1494: {e}')

print("STEP 1495 - Check element div#None.['media-gallery-contents']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-contents']")))
    print('PASS - step 1495')
except Exception as e:
    print('FAIL - step 1495' if isinstance(e, AssertionError) else f'ERROR - step 1495: {e}')

print("STEP 1496 - Check element div#None.['media-gallery-top-content', 'tv-gallery-top-content-s-only']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-top-content', 'tv-gallery-top-content-s-only']")))
    print('PASS - step 1496')
except Exception as e:
    print('FAIL - step 1496' if isinstance(e, AssertionError) else f'ERROR - step 1496: {e}')

print("STEP 1497 - Check element picture#None.['tv-gallery-atvplus-logo', 'show-logo']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['tv-gallery-atvplus-logo', 'show-logo']")))
    print('PASS - step 1497')
except Exception as e:
    print('FAIL - step 1497' if isinstance(e, AssertionError) else f'ERROR - step 1497: {e}')

print("STEP 1498 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1498')
except Exception as e:
    print('FAIL - step 1498' if isinstance(e, AssertionError) else f'ERROR - step 1498: {e}')

print("STEP 1499 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1499')
except Exception as e:
    print('FAIL - step 1499' if isinstance(e, AssertionError) else f'ERROR - step 1499: {e}')

print("STEP 1500 - Check element noscript#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "noscript")))
    print('PASS - step 1500')
except Exception as e:
    print('FAIL - step 1500' if isinstance(e, AssertionError) else f'ERROR - step 1500: {e}')

print("STEP 1501 - Check element picture#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "picture")))
    print('PASS - step 1501')
except Exception as e:
    print('FAIL - step 1501' if isinstance(e, AssertionError) else f'ERROR - step 1501: {e}')

print("STEP 1502 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1502')
except Exception as e:
    print('FAIL - step 1502' if isinstance(e, AssertionError) else f'ERROR - step 1502: {e}')

print("STEP 1503 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1503')
except Exception as e:
    print('FAIL - step 1503' if isinstance(e, AssertionError) else f'ERROR - step 1503: {e}')

print("STEP 1504 - Check element picture#None.['tv-gallery-media-logo']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['tv-gallery-media-logo']")))
    print('PASS - step 1504')
except Exception as e:
    print('FAIL - step 1504' if isinstance(e, AssertionError) else f'ERROR - step 1504: {e}')

print("STEP 1505 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1505')
except Exception as e:
    print('FAIL - step 1505' if isinstance(e, AssertionError) else f'ERROR - step 1505: {e}')

print("STEP 1506 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1506')
except Exception as e:
    print('FAIL - step 1506' if isinstance(e, AssertionError) else f'ERROR - step 1506: {e}')

print("STEP 1507 - Check element noscript#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "noscript")))
    print('PASS - step 1507')
except Exception as e:
    print('FAIL - step 1507' if isinstance(e, AssertionError) else f'ERROR - step 1507: {e}')

print("STEP 1508 - Check element picture#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "picture")))
    print('PASS - step 1508')
except Exception as e:
    print('FAIL - step 1508' if isinstance(e, AssertionError) else f'ERROR - step 1508: {e}')

print("STEP 1509 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1509')
except Exception as e:
    print('FAIL - step 1509' if isinstance(e, AssertionError) else f'ERROR - step 1509: {e}')

print("STEP 1510 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1510')
except Exception as e:
    print('FAIL - step 1510' if isinstance(e, AssertionError) else f'ERROR - step 1510: {e}')

print("STEP 1511 - Check element div#None.['media-gallery-bottom-content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-bottom-content']")))
    print('PASS - step 1511')
except Exception as e:
    print('FAIL - step 1511' if isinstance(e, AssertionError) else f'ERROR - step 1511: {e}')

print("STEP 1512 - Check element div#None.['button', 'button-neutral', 'media-gallery-button']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['button', 'button-neutral', 'media-gallery-button']")))
    print('PASS - step 1512')
except Exception as e:
    print('FAIL - step 1512' if isinstance(e, AssertionError) else f'ERROR - step 1512: {e}')

print("STEP 1513 - Check element p#None.['media-gallery-longnote']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-longnote']")))
    print('PASS - step 1513')
except Exception as e:
    print('FAIL - step 1513' if isinstance(e, AssertionError) else f'ERROR - step 1513: {e}')

print("STEP 1514 - Check element span#None.['media-gallery-genre']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-genre']")))
    print('PASS - step 1514')
except Exception as e:
    print('FAIL - step 1514' if isinstance(e, AssertionError) else f'ERROR - step 1514: {e}')

print("STEP 1515 - Check element div#fam-media-gallery.['media-gallery', 'fam-media-gallery']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "fam-media-gallery")))
    print('PASS - step 1515')
except Exception as e:
    print('FAIL - step 1515' if isinstance(e, AssertionError) else f'ERROR - step 1515: {e}')

print("STEP 1516 - Check element ul#None.['media-gallery-item-container']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-item-container']")))
    print('PASS - step 1516')
except Exception as e:
    print('FAIL - step 1516' if isinstance(e, AssertionError) else f'ERROR - step 1516: {e}')

print("STEP 1517 - Check element li#endless-entertainment-gallery-item-1.['media-gallery-item', 'theme-dark', 'current', 'current-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "endless-entertainment-gallery-item-1")))
    print('PASS - step 1517')
except Exception as e:
    print('FAIL - step 1517' if isinstance(e, AssertionError) else f'ERROR - step 1517: {e}')

print("STEP 1518 - Check element a#media-gallery-item-1.['media-gallery-wrapper-link', 'fam-media-gallery-wrapper-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "media-gallery-item-1")))
    print('PASS - step 1518')
except Exception as e:
    print('FAIL - step 1518' if isinstance(e, AssertionError) else f'ERROR - step 1518: {e}')

print("STEP 1519 - Check element div#None.['media-gallery-bg-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-bg-wrapper']")))
    print('PASS - step 1519')
except Exception as e:
    print('FAIL - step 1519' if isinstance(e, AssertionError) else f'ERROR - step 1519: {e}')

print("STEP 1520 - Check element picture#None.['media-gallery-bg']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-bg']")))
    print('PASS - step 1520')
except Exception as e:
    print('FAIL - step 1520' if isinstance(e, AssertionError) else f'ERROR - step 1520: {e}')

print("STEP 1521 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1521')
except Exception as e:
    print('FAIL - step 1521' if isinstance(e, AssertionError) else f'ERROR - step 1521: {e}')

print("STEP 1522 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1522')
except Exception as e:
    print('FAIL - step 1522' if isinstance(e, AssertionError) else f'ERROR - step 1522: {e}')

print("STEP 1523 - Check element noscript#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "noscript")))
    print('PASS - step 1523')
except Exception as e:
    print('FAIL - step 1523' if isinstance(e, AssertionError) else f'ERROR - step 1523: {e}')

print("STEP 1524 - Check element picture#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "picture")))
    print('PASS - step 1524')
except Exception as e:
    print('FAIL - step 1524' if isinstance(e, AssertionError) else f'ERROR - step 1524: {e}')

print("STEP 1525 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1525')
except Exception as e:
    print('FAIL - step 1525' if isinstance(e, AssertionError) else f'ERROR - step 1525: {e}')

print("STEP 1526 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1526')
except Exception as e:
    print('FAIL - step 1526' if isinstance(e, AssertionError) else f'ERROR - step 1526: {e}')

print("STEP 1527 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1527')
except Exception as e:
    print('FAIL - step 1527' if isinstance(e, AssertionError) else f'ERROR - step 1527: {e}')

print("STEP 1528 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1528')
except Exception as e:
    print('FAIL - step 1528' if isinstance(e, AssertionError) else f'ERROR - step 1528: {e}')

print("STEP 1529 - Check element div#None.['media-gallery-contents']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-contents']")))
    print('PASS - step 1529')
except Exception as e:
    print('FAIL - step 1529' if isinstance(e, AssertionError) else f'ERROR - step 1529: {e}')

print("STEP 1530 - Check element div#None.['media-gallery-top-content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-top-content']")))
    print('PASS - step 1530')
except Exception as e:
    print('FAIL - step 1530' if isinstance(e, AssertionError) else f'ERROR - step 1530: {e}')

print("STEP 1531 - Check element div#None.['media-gallery-logo', 'media-gallery-logo-fitness']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-logo', 'media-gallery-logo-fitness']")))
    print('PASS - step 1531')
except Exception as e:
    print('FAIL - step 1531' if isinstance(e, AssertionError) else f'ERROR - step 1531: {e}')

print("STEP 1532 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 1532')
except Exception as e:
    print('FAIL - step 1532' if isinstance(e, AssertionError) else f'ERROR - step 1532: {e}')

print("STEP 1533 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 1533')
except Exception as e:
    print('FAIL - step 1533' if isinstance(e, AssertionError) else f'ERROR - step 1533: {e}')

print("STEP 1534 - Check element div#None.['media-gallery-bottom-content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-bottom-content']")))
    print('PASS - step 1534')
except Exception as e:
    print('FAIL - step 1534' if isinstance(e, AssertionError) else f'ERROR - step 1534: {e}')

print("STEP 1535 - Check element div#None.['button', 'button-neutral', 'media-gallery-button']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['button', 'button-neutral', 'media-gallery-button']")))
    print('PASS - step 1535')
except Exception as e:
    print('FAIL - step 1535' if isinstance(e, AssertionError) else f'ERROR - step 1535: {e}')

print("STEP 1536 - Check element p#None.['media-gallery-longnote']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-longnote']")))
    print('PASS - step 1536')
except Exception as e:
    print('FAIL - step 1536' if isinstance(e, AssertionError) else f'ERROR - step 1536: {e}')

print("STEP 1537 - Check element li#endless-entertainment-gallery-item-2.['media-gallery-item', 'theme-dark', 'current-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "endless-entertainment-gallery-item-2")))
    print('PASS - step 1537')
except Exception as e:
    print('FAIL - step 1537' if isinstance(e, AssertionError) else f'ERROR - step 1537: {e}')

print("STEP 1538 - Check element a#media-gallery-item-2.['media-gallery-wrapper-link', 'fam-media-gallery-wrapper-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "media-gallery-item-2")))
    print('PASS - step 1538')
except Exception as e:
    print('FAIL - step 1538' if isinstance(e, AssertionError) else f'ERROR - step 1538: {e}')

print("STEP 1539 - Check element div#None.['media-gallery-bg-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-bg-wrapper']")))
    print('PASS - step 1539')
except Exception as e:
    print('FAIL - step 1539' if isinstance(e, AssertionError) else f'ERROR - step 1539: {e}')

print("STEP 1540 - Check element picture#None.['media-gallery-bg']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-bg']")))
    print('PASS - step 1540')
except Exception as e:
    print('FAIL - step 1540' if isinstance(e, AssertionError) else f'ERROR - step 1540: {e}')

print("STEP 1541 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1541')
except Exception as e:
    print('FAIL - step 1541' if isinstance(e, AssertionError) else f'ERROR - step 1541: {e}')

print("STEP 1542 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1542')
except Exception as e:
    print('FAIL - step 1542' if isinstance(e, AssertionError) else f'ERROR - step 1542: {e}')

print("STEP 1543 - Check element noscript#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "noscript")))
    print('PASS - step 1543')
except Exception as e:
    print('FAIL - step 1543' if isinstance(e, AssertionError) else f'ERROR - step 1543: {e}')

print("STEP 1544 - Check element picture#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "picture")))
    print('PASS - step 1544')
except Exception as e:
    print('FAIL - step 1544' if isinstance(e, AssertionError) else f'ERROR - step 1544: {e}')

print("STEP 1545 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1545')
except Exception as e:
    print('FAIL - step 1545' if isinstance(e, AssertionError) else f'ERROR - step 1545: {e}')

print("STEP 1546 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1546')
except Exception as e:
    print('FAIL - step 1546' if isinstance(e, AssertionError) else f'ERROR - step 1546: {e}')

print("STEP 1547 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1547')
except Exception as e:
    print('FAIL - step 1547' if isinstance(e, AssertionError) else f'ERROR - step 1547: {e}')

print("STEP 1548 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1548')
except Exception as e:
    print('FAIL - step 1548' if isinstance(e, AssertionError) else f'ERROR - step 1548: {e}')

print("STEP 1549 - Check element div#None.['media-gallery-contents']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-contents']")))
    print('PASS - step 1549')
except Exception as e:
    print('FAIL - step 1549' if isinstance(e, AssertionError) else f'ERROR - step 1549: {e}')

print("STEP 1550 - Check element div#None.['media-gallery-top-content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-top-content']")))
    print('PASS - step 1550')
except Exception as e:
    print('FAIL - step 1550' if isinstance(e, AssertionError) else f'ERROR - step 1550: {e}')

print("STEP 1551 - Check element div#None.['media-gallery-logo', 'media-gallery-logo-arcade']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-logo', 'media-gallery-logo-arcade']")))
    print('PASS - step 1551')
except Exception as e:
    print('FAIL - step 1551' if isinstance(e, AssertionError) else f'ERROR - step 1551: {e}')

print("STEP 1552 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 1552')
except Exception as e:
    print('FAIL - step 1552' if isinstance(e, AssertionError) else f'ERROR - step 1552: {e}')

print("STEP 1553 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 1553')
except Exception as e:
    print('FAIL - step 1553' if isinstance(e, AssertionError) else f'ERROR - step 1553: {e}')

print("STEP 1554 - Check element div#None.['media-gallery-bottom-content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-bottom-content']")))
    print('PASS - step 1554')
except Exception as e:
    print('FAIL - step 1554' if isinstance(e, AssertionError) else f'ERROR - step 1554: {e}')

print("STEP 1555 - Check element div#None.['button', 'button-neutral', 'media-gallery-button']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['button', 'button-neutral', 'media-gallery-button']")))
    print('PASS - step 1555')
except Exception as e:
    print('FAIL - step 1555' if isinstance(e, AssertionError) else f'ERROR - step 1555: {e}')

print("STEP 1556 - Check element p#None.['media-gallery-longnote']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-longnote']")))
    print('PASS - step 1556')
except Exception as e:
    print('FAIL - step 1556' if isinstance(e, AssertionError) else f'ERROR - step 1556: {e}')

print("STEP 1557 - Check element li#endless-entertainment-gallery-item-3.['media-gallery-item', 'theme-dark', 'current-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "endless-entertainment-gallery-item-3")))
    print('PASS - step 1557')
except Exception as e:
    print('FAIL - step 1557' if isinstance(e, AssertionError) else f'ERROR - step 1557: {e}')

print("STEP 1558 - Check element a#media-gallery-item-3.['media-gallery-wrapper-link', 'fam-media-gallery-wrapper-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "media-gallery-item-3")))
    print('PASS - step 1558')
except Exception as e:
    print('FAIL - step 1558' if isinstance(e, AssertionError) else f'ERROR - step 1558: {e}')

print("STEP 1559 - Check element div#None.['media-gallery-bg-wrapper', 'media-gallery-bg-wrapper-music']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-bg-wrapper', 'media-gallery-bg-wrapper-music']")))
    print('PASS - step 1559')
except Exception as e:
    print('FAIL - step 1559' if isinstance(e, AssertionError) else f'ERROR - step 1559: {e}')

print("STEP 1560 - Check element picture#None.['media-gallery-bg', 'media-gallery-bg-music']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-bg', 'media-gallery-bg-music']")))
    print('PASS - step 1560')
except Exception as e:
    print('FAIL - step 1560' if isinstance(e, AssertionError) else f'ERROR - step 1560: {e}')

print("STEP 1561 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1561')
except Exception as e:
    print('FAIL - step 1561' if isinstance(e, AssertionError) else f'ERROR - step 1561: {e}')

print("STEP 1562 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1562')
except Exception as e:
    print('FAIL - step 1562' if isinstance(e, AssertionError) else f'ERROR - step 1562: {e}')

print("STEP 1563 - Check element noscript#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "noscript")))
    print('PASS - step 1563')
except Exception as e:
    print('FAIL - step 1563' if isinstance(e, AssertionError) else f'ERROR - step 1563: {e}')

print("STEP 1564 - Check element picture#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "picture")))
    print('PASS - step 1564')
except Exception as e:
    print('FAIL - step 1564' if isinstance(e, AssertionError) else f'ERROR - step 1564: {e}')

print("STEP 1565 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1565')
except Exception as e:
    print('FAIL - step 1565' if isinstance(e, AssertionError) else f'ERROR - step 1565: {e}')

print("STEP 1566 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1566')
except Exception as e:
    print('FAIL - step 1566' if isinstance(e, AssertionError) else f'ERROR - step 1566: {e}')

print("STEP 1567 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1567')
except Exception as e:
    print('FAIL - step 1567' if isinstance(e, AssertionError) else f'ERROR - step 1567: {e}')

print("STEP 1568 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1568')
except Exception as e:
    print('FAIL - step 1568' if isinstance(e, AssertionError) else f'ERROR - step 1568: {e}')

print("STEP 1569 - Check element p#None.['media-gallery-longnote', 'media-gallery-longnote-music', 'media-gallery-longnote-music-hide-medium-small']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-longnote', 'media-gallery-longnote-music', 'media-gallery-longnote-music-hide-medium-small']")))
    print('PASS - step 1569')
except Exception as e:
    print('FAIL - step 1569' if isinstance(e, AssertionError) else f'ERROR - step 1569: {e}')

print("STEP 1570 - Check element div#None.['media-gallery-contents']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-contents']")))
    print('PASS - step 1570')
except Exception as e:
    print('FAIL - step 1570' if isinstance(e, AssertionError) else f'ERROR - step 1570: {e}')

print("STEP 1571 - Check element div#None.['media-gallery-top-content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-top-content']")))
    print('PASS - step 1571')
except Exception as e:
    print('FAIL - step 1571' if isinstance(e, AssertionError) else f'ERROR - step 1571: {e}')

print("STEP 1572 - Check element div#None.['media-gallery-logo', 'media-gallery-logo-music']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-logo', 'media-gallery-logo-music']")))
    print('PASS - step 1572')
except Exception as e:
    print('FAIL - step 1572' if isinstance(e, AssertionError) else f'ERROR - step 1572: {e}')

print("STEP 1573 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 1573')
except Exception as e:
    print('FAIL - step 1573' if isinstance(e, AssertionError) else f'ERROR - step 1573: {e}')

print("STEP 1574 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 1574')
except Exception as e:
    print('FAIL - step 1574' if isinstance(e, AssertionError) else f'ERROR - step 1574: {e}')

print("STEP 1575 - Check element div#None.['media-gallery-bottom-content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-bottom-content']")))
    print('PASS - step 1575')
except Exception as e:
    print('FAIL - step 1575' if isinstance(e, AssertionError) else f'ERROR - step 1575: {e}')

print("STEP 1576 - Check element div#None.['button', 'button-neutral', 'media-gallery-button']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['button', 'button-neutral', 'media-gallery-button']")))
    print('PASS - step 1576')
except Exception as e:
    print('FAIL - step 1576' if isinstance(e, AssertionError) else f'ERROR - step 1576: {e}')

print("STEP 1577 - Check element p#None.['media-gallery-longnote', 'media-gallery-longnote-music', 'media-gallery-longnote-music-hide-large']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-longnote', 'media-gallery-longnote-music', 'media-gallery-longnote-music-hide-large']")))
    print('PASS - step 1577')
except Exception as e:
    print('FAIL - step 1577' if isinstance(e, AssertionError) else f'ERROR - step 1577: {e}')

print("STEP 1578 - Check element li#endless-entertainment-gallery-item-4.['media-gallery-item', 'theme-dark']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "endless-entertainment-gallery-item-4")))
    print('PASS - step 1578')
except Exception as e:
    print('FAIL - step 1578' if isinstance(e, AssertionError) else f'ERROR - step 1578: {e}')

print("STEP 1579 - Check element a#media-gallery-item-4.['media-gallery-wrapper-link', 'fam-media-gallery-wrapper-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "media-gallery-item-4")))
    print('PASS - step 1579')
except Exception as e:
    print('FAIL - step 1579' if isinstance(e, AssertionError) else f'ERROR - step 1579: {e}')

print("STEP 1580 - Check element div#None.['media-gallery-bg-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-bg-wrapper']")))
    print('PASS - step 1580')
except Exception as e:
    print('FAIL - step 1580' if isinstance(e, AssertionError) else f'ERROR - step 1580: {e}')

print("STEP 1581 - Check element picture#None.['media-gallery-bg']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-bg']")))
    print('PASS - step 1581')
except Exception as e:
    print('FAIL - step 1581' if isinstance(e, AssertionError) else f'ERROR - step 1581: {e}')

print("STEP 1582 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1582')
except Exception as e:
    print('FAIL - step 1582' if isinstance(e, AssertionError) else f'ERROR - step 1582: {e}')

print("STEP 1583 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1583')
except Exception as e:
    print('FAIL - step 1583' if isinstance(e, AssertionError) else f'ERROR - step 1583: {e}')

print("STEP 1584 - Check element noscript#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "noscript")))
    print('PASS - step 1584')
except Exception as e:
    print('FAIL - step 1584' if isinstance(e, AssertionError) else f'ERROR - step 1584: {e}')

print("STEP 1585 - Check element picture#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "picture")))
    print('PASS - step 1585')
except Exception as e:
    print('FAIL - step 1585' if isinstance(e, AssertionError) else f'ERROR - step 1585: {e}')

print("STEP 1586 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1586')
except Exception as e:
    print('FAIL - step 1586' if isinstance(e, AssertionError) else f'ERROR - step 1586: {e}')

print("STEP 1587 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1587')
except Exception as e:
    print('FAIL - step 1587' if isinstance(e, AssertionError) else f'ERROR - step 1587: {e}')

print("STEP 1588 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1588')
except Exception as e:
    print('FAIL - step 1588' if isinstance(e, AssertionError) else f'ERROR - step 1588: {e}')

print("STEP 1589 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1589')
except Exception as e:
    print('FAIL - step 1589' if isinstance(e, AssertionError) else f'ERROR - step 1589: {e}')

print("STEP 1590 - Check element div#None.['media-gallery-contents']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-contents']")))
    print('PASS - step 1590')
except Exception as e:
    print('FAIL - step 1590' if isinstance(e, AssertionError) else f'ERROR - step 1590: {e}')

print("STEP 1591 - Check element div#None.['media-gallery-top-content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-top-content']")))
    print('PASS - step 1591')
except Exception as e:
    print('FAIL - step 1591' if isinstance(e, AssertionError) else f'ERROR - step 1591: {e}')

print("STEP 1592 - Check element div#None.['media-gallery-logo', 'media-gallery-logo-fitness']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-logo', 'media-gallery-logo-fitness']")))
    print('PASS - step 1592')
except Exception as e:
    print('FAIL - step 1592' if isinstance(e, AssertionError) else f'ERROR - step 1592: {e}')

print("STEP 1593 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 1593')
except Exception as e:
    print('FAIL - step 1593' if isinstance(e, AssertionError) else f'ERROR - step 1593: {e}')

print("STEP 1594 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 1594')
except Exception as e:
    print('FAIL - step 1594' if isinstance(e, AssertionError) else f'ERROR - step 1594: {e}')

print("STEP 1595 - Check element div#None.['media-gallery-bottom-content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-bottom-content']")))
    print('PASS - step 1595')
except Exception as e:
    print('FAIL - step 1595' if isinstance(e, AssertionError) else f'ERROR - step 1595: {e}')

print("STEP 1596 - Check element div#None.['button', 'button-neutral', 'media-gallery-button']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['button', 'button-neutral', 'media-gallery-button']")))
    print('PASS - step 1596')
except Exception as e:
    print('FAIL - step 1596' if isinstance(e, AssertionError) else f'ERROR - step 1596: {e}')

print("STEP 1597 - Check element p#None.['media-gallery-longnote']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-longnote']")))
    print('PASS - step 1597')
except Exception as e:
    print('FAIL - step 1597' if isinstance(e, AssertionError) else f'ERROR - step 1597: {e}')

print("STEP 1598 - Check element li#endless-entertainment-gallery-item-5.['media-gallery-item', 'theme-dark']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "endless-entertainment-gallery-item-5")))
    print('PASS - step 1598')
except Exception as e:
    print('FAIL - step 1598' if isinstance(e, AssertionError) else f'ERROR - step 1598: {e}')

print("STEP 1599 - Check element a#media-gallery-item-5.['media-gallery-wrapper-link', 'fam-media-gallery-wrapper-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "media-gallery-item-5")))
    print('PASS - step 1599')
except Exception as e:
    print('FAIL - step 1599' if isinstance(e, AssertionError) else f'ERROR - step 1599: {e}')

print("STEP 1600 - Check element div#None.['media-gallery-bg-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-bg-wrapper']")))
    print('PASS - step 1600')
except Exception as e:
    print('FAIL - step 1600' if isinstance(e, AssertionError) else f'ERROR - step 1600: {e}')

print("STEP 1601 - Check element picture#None.['media-gallery-bg']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-bg']")))
    print('PASS - step 1601')
except Exception as e:
    print('FAIL - step 1601' if isinstance(e, AssertionError) else f'ERROR - step 1601: {e}')

print("STEP 1602 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1602')
except Exception as e:
    print('FAIL - step 1602' if isinstance(e, AssertionError) else f'ERROR - step 1602: {e}')

print("STEP 1603 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1603')
except Exception as e:
    print('FAIL - step 1603' if isinstance(e, AssertionError) else f'ERROR - step 1603: {e}')

print("STEP 1604 - Check element noscript#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "noscript")))
    print('PASS - step 1604')
except Exception as e:
    print('FAIL - step 1604' if isinstance(e, AssertionError) else f'ERROR - step 1604: {e}')

print("STEP 1605 - Check element picture#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "picture")))
    print('PASS - step 1605')
except Exception as e:
    print('FAIL - step 1605' if isinstance(e, AssertionError) else f'ERROR - step 1605: {e}')

print("STEP 1606 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1606')
except Exception as e:
    print('FAIL - step 1606' if isinstance(e, AssertionError) else f'ERROR - step 1606: {e}')

print("STEP 1607 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1607')
except Exception as e:
    print('FAIL - step 1607' if isinstance(e, AssertionError) else f'ERROR - step 1607: {e}')

print("STEP 1608 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1608')
except Exception as e:
    print('FAIL - step 1608' if isinstance(e, AssertionError) else f'ERROR - step 1608: {e}')

print("STEP 1609 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1609')
except Exception as e:
    print('FAIL - step 1609' if isinstance(e, AssertionError) else f'ERROR - step 1609: {e}')

print("STEP 1610 - Check element div#None.['media-gallery-contents']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-contents']")))
    print('PASS - step 1610')
except Exception as e:
    print('FAIL - step 1610' if isinstance(e, AssertionError) else f'ERROR - step 1610: {e}')

print("STEP 1611 - Check element div#None.['media-gallery-top-content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-top-content']")))
    print('PASS - step 1611')
except Exception as e:
    print('FAIL - step 1611' if isinstance(e, AssertionError) else f'ERROR - step 1611: {e}')

print("STEP 1612 - Check element div#None.['media-gallery-logo', 'media-gallery-logo-arcade']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-logo', 'media-gallery-logo-arcade']")))
    print('PASS - step 1612')
except Exception as e:
    print('FAIL - step 1612' if isinstance(e, AssertionError) else f'ERROR - step 1612: {e}')

print("STEP 1613 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 1613')
except Exception as e:
    print('FAIL - step 1613' if isinstance(e, AssertionError) else f'ERROR - step 1613: {e}')

print("STEP 1614 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 1614')
except Exception as e:
    print('FAIL - step 1614' if isinstance(e, AssertionError) else f'ERROR - step 1614: {e}')

print("STEP 1615 - Check element div#None.['media-gallery-bottom-content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-bottom-content']")))
    print('PASS - step 1615')
except Exception as e:
    print('FAIL - step 1615' if isinstance(e, AssertionError) else f'ERROR - step 1615: {e}')

print("STEP 1616 - Check element div#None.['button', 'button-neutral', 'media-gallery-button']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['button', 'button-neutral', 'media-gallery-button']")))
    print('PASS - step 1616')
except Exception as e:
    print('FAIL - step 1616' if isinstance(e, AssertionError) else f'ERROR - step 1616: {e}')

print("STEP 1617 - Check element p#None.['media-gallery-longnote']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-longnote']")))
    print('PASS - step 1617')
except Exception as e:
    print('FAIL - step 1617' if isinstance(e, AssertionError) else f'ERROR - step 1617: {e}')

print("STEP 1618 - Check element li#endless-entertainment-gallery-item-6.['media-gallery-item', 'theme-dark']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "endless-entertainment-gallery-item-6")))
    print('PASS - step 1618')
except Exception as e:
    print('FAIL - step 1618' if isinstance(e, AssertionError) else f'ERROR - step 1618: {e}')

print("STEP 1619 - Check element a#media-gallery-item-6.['media-gallery-wrapper-link', 'fam-media-gallery-wrapper-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "media-gallery-item-6")))
    print('PASS - step 1619')
except Exception as e:
    print('FAIL - step 1619' if isinstance(e, AssertionError) else f'ERROR - step 1619: {e}')

print("STEP 1620 - Check element div#None.['media-gallery-bg-wrapper', 'media-gallery-bg-wrapper-music']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-bg-wrapper', 'media-gallery-bg-wrapper-music']")))
    print('PASS - step 1620')
except Exception as e:
    print('FAIL - step 1620' if isinstance(e, AssertionError) else f'ERROR - step 1620: {e}')

print("STEP 1621 - Check element picture#None.['media-gallery-bg', 'media-gallery-bg-music']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-bg', 'media-gallery-bg-music']")))
    print('PASS - step 1621')
except Exception as e:
    print('FAIL - step 1621' if isinstance(e, AssertionError) else f'ERROR - step 1621: {e}')

print("STEP 1622 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1622')
except Exception as e:
    print('FAIL - step 1622' if isinstance(e, AssertionError) else f'ERROR - step 1622: {e}')

print("STEP 1623 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1623')
except Exception as e:
    print('FAIL - step 1623' if isinstance(e, AssertionError) else f'ERROR - step 1623: {e}')

print("STEP 1624 - Check element noscript#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "noscript")))
    print('PASS - step 1624')
except Exception as e:
    print('FAIL - step 1624' if isinstance(e, AssertionError) else f'ERROR - step 1624: {e}')

print("STEP 1625 - Check element picture#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "picture")))
    print('PASS - step 1625')
except Exception as e:
    print('FAIL - step 1625' if isinstance(e, AssertionError) else f'ERROR - step 1625: {e}')

print("STEP 1626 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1626')
except Exception as e:
    print('FAIL - step 1626' if isinstance(e, AssertionError) else f'ERROR - step 1626: {e}')

print("STEP 1627 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1627')
except Exception as e:
    print('FAIL - step 1627' if isinstance(e, AssertionError) else f'ERROR - step 1627: {e}')

print("STEP 1628 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1628')
except Exception as e:
    print('FAIL - step 1628' if isinstance(e, AssertionError) else f'ERROR - step 1628: {e}')

print("STEP 1629 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1629')
except Exception as e:
    print('FAIL - step 1629' if isinstance(e, AssertionError) else f'ERROR - step 1629: {e}')

print("STEP 1630 - Check element p#None.['media-gallery-longnote', 'media-gallery-longnote-music', 'media-gallery-longnote-music-hide-medium-small']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-longnote', 'media-gallery-longnote-music', 'media-gallery-longnote-music-hide-medium-small']")))
    print('PASS - step 1630')
except Exception as e:
    print('FAIL - step 1630' if isinstance(e, AssertionError) else f'ERROR - step 1630: {e}')

print("STEP 1631 - Check element div#None.['media-gallery-contents']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-contents']")))
    print('PASS - step 1631')
except Exception as e:
    print('FAIL - step 1631' if isinstance(e, AssertionError) else f'ERROR - step 1631: {e}')

print("STEP 1632 - Check element div#None.['media-gallery-top-content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-top-content']")))
    print('PASS - step 1632')
except Exception as e:
    print('FAIL - step 1632' if isinstance(e, AssertionError) else f'ERROR - step 1632: {e}')

print("STEP 1633 - Check element div#None.['media-gallery-logo', 'media-gallery-logo-music']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-logo', 'media-gallery-logo-music']")))
    print('PASS - step 1633')
except Exception as e:
    print('FAIL - step 1633' if isinstance(e, AssertionError) else f'ERROR - step 1633: {e}')

print("STEP 1634 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 1634')
except Exception as e:
    print('FAIL - step 1634' if isinstance(e, AssertionError) else f'ERROR - step 1634: {e}')

print("STEP 1635 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 1635')
except Exception as e:
    print('FAIL - step 1635' if isinstance(e, AssertionError) else f'ERROR - step 1635: {e}')

print("STEP 1636 - Check element div#None.['media-gallery-bottom-content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-bottom-content']")))
    print('PASS - step 1636')
except Exception as e:
    print('FAIL - step 1636' if isinstance(e, AssertionError) else f'ERROR - step 1636: {e}')

print("STEP 1637 - Check element div#None.['button', 'button-neutral', 'media-gallery-button']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['button', 'button-neutral', 'media-gallery-button']")))
    print('PASS - step 1637')
except Exception as e:
    print('FAIL - step 1637' if isinstance(e, AssertionError) else f'ERROR - step 1637: {e}')

print("STEP 1638 - Check element p#None.['media-gallery-longnote', 'media-gallery-longnote-music', 'media-gallery-longnote-music-hide-large']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-longnote', 'media-gallery-longnote-music', 'media-gallery-longnote-music-hide-large']")))
    print('PASS - step 1638')
except Exception as e:
    print('FAIL - step 1638' if isinstance(e, AssertionError) else f'ERROR - step 1638: {e}')

print("STEP 1639 - Check element li#endless-entertainment-gallery-item-7.['media-gallery-item', 'theme-dark']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "endless-entertainment-gallery-item-7")))
    print('PASS - step 1639')
except Exception as e:
    print('FAIL - step 1639' if isinstance(e, AssertionError) else f'ERROR - step 1639: {e}')

print("STEP 1640 - Check element a#media-gallery-item-7.['media-gallery-wrapper-link', 'fam-media-gallery-wrapper-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "media-gallery-item-7")))
    print('PASS - step 1640')
except Exception as e:
    print('FAIL - step 1640' if isinstance(e, AssertionError) else f'ERROR - step 1640: {e}')

print("STEP 1641 - Check element div#None.['media-gallery-bg-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-bg-wrapper']")))
    print('PASS - step 1641')
except Exception as e:
    print('FAIL - step 1641' if isinstance(e, AssertionError) else f'ERROR - step 1641: {e}')

print("STEP 1642 - Check element picture#None.['media-gallery-bg']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-bg']")))
    print('PASS - step 1642')
except Exception as e:
    print('FAIL - step 1642' if isinstance(e, AssertionError) else f'ERROR - step 1642: {e}')

print("STEP 1643 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1643')
except Exception as e:
    print('FAIL - step 1643' if isinstance(e, AssertionError) else f'ERROR - step 1643: {e}')

print("STEP 1644 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1644')
except Exception as e:
    print('FAIL - step 1644' if isinstance(e, AssertionError) else f'ERROR - step 1644: {e}')

print("STEP 1645 - Check element noscript#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "noscript")))
    print('PASS - step 1645')
except Exception as e:
    print('FAIL - step 1645' if isinstance(e, AssertionError) else f'ERROR - step 1645: {e}')

print("STEP 1646 - Check element picture#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "picture")))
    print('PASS - step 1646')
except Exception as e:
    print('FAIL - step 1646' if isinstance(e, AssertionError) else f'ERROR - step 1646: {e}')

print("STEP 1647 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1647')
except Exception as e:
    print('FAIL - step 1647' if isinstance(e, AssertionError) else f'ERROR - step 1647: {e}')

print("STEP 1648 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1648')
except Exception as e:
    print('FAIL - step 1648' if isinstance(e, AssertionError) else f'ERROR - step 1648: {e}')

print("STEP 1649 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1649')
except Exception as e:
    print('FAIL - step 1649' if isinstance(e, AssertionError) else f'ERROR - step 1649: {e}')

print("STEP 1650 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1650')
except Exception as e:
    print('FAIL - step 1650' if isinstance(e, AssertionError) else f'ERROR - step 1650: {e}')

print("STEP 1651 - Check element div#None.['media-gallery-contents']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-contents']")))
    print('PASS - step 1651')
except Exception as e:
    print('FAIL - step 1651' if isinstance(e, AssertionError) else f'ERROR - step 1651: {e}')

print("STEP 1652 - Check element div#None.['media-gallery-top-content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-top-content']")))
    print('PASS - step 1652')
except Exception as e:
    print('FAIL - step 1652' if isinstance(e, AssertionError) else f'ERROR - step 1652: {e}')

print("STEP 1653 - Check element div#None.['media-gallery-logo', 'media-gallery-logo-fitness']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-logo', 'media-gallery-logo-fitness']")))
    print('PASS - step 1653')
except Exception as e:
    print('FAIL - step 1653' if isinstance(e, AssertionError) else f'ERROR - step 1653: {e}')

print("STEP 1654 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 1654')
except Exception as e:
    print('FAIL - step 1654' if isinstance(e, AssertionError) else f'ERROR - step 1654: {e}')

print("STEP 1655 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 1655')
except Exception as e:
    print('FAIL - step 1655' if isinstance(e, AssertionError) else f'ERROR - step 1655: {e}')

print("STEP 1656 - Check element div#None.['media-gallery-bottom-content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-bottom-content']")))
    print('PASS - step 1656')
except Exception as e:
    print('FAIL - step 1656' if isinstance(e, AssertionError) else f'ERROR - step 1656: {e}')

print("STEP 1657 - Check element div#None.['button', 'button-neutral', 'media-gallery-button']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['button', 'button-neutral', 'media-gallery-button']")))
    print('PASS - step 1657')
except Exception as e:
    print('FAIL - step 1657' if isinstance(e, AssertionError) else f'ERROR - step 1657: {e}')

print("STEP 1658 - Check element p#None.['media-gallery-longnote']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-longnote']")))
    print('PASS - step 1658')
except Exception as e:
    print('FAIL - step 1658' if isinstance(e, AssertionError) else f'ERROR - step 1658: {e}')

print("STEP 1659 - Check element li#endless-entertainment-gallery-item-8.['media-gallery-item', 'theme-dark', 'current-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "endless-entertainment-gallery-item-8")))
    print('PASS - step 1659')
except Exception as e:
    print('FAIL - step 1659' if isinstance(e, AssertionError) else f'ERROR - step 1659: {e}')

print("STEP 1660 - Check element a#media-gallery-item-8.['media-gallery-wrapper-link', 'fam-media-gallery-wrapper-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "media-gallery-item-8")))
    print('PASS - step 1660')
except Exception as e:
    print('FAIL - step 1660' if isinstance(e, AssertionError) else f'ERROR - step 1660: {e}')

print("STEP 1661 - Check element div#None.['media-gallery-bg-wrapper']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-bg-wrapper']")))
    print('PASS - step 1661')
except Exception as e:
    print('FAIL - step 1661' if isinstance(e, AssertionError) else f'ERROR - step 1661: {e}')

print("STEP 1662 - Check element picture#None.['media-gallery-bg']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-bg']")))
    print('PASS - step 1662')
except Exception as e:
    print('FAIL - step 1662' if isinstance(e, AssertionError) else f'ERROR - step 1662: {e}')

print("STEP 1663 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1663')
except Exception as e:
    print('FAIL - step 1663' if isinstance(e, AssertionError) else f'ERROR - step 1663: {e}')

print("STEP 1664 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1664')
except Exception as e:
    print('FAIL - step 1664' if isinstance(e, AssertionError) else f'ERROR - step 1664: {e}')

print("STEP 1665 - Check element noscript#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "noscript")))
    print('PASS - step 1665')
except Exception as e:
    print('FAIL - step 1665' if isinstance(e, AssertionError) else f'ERROR - step 1665: {e}')

print("STEP 1666 - Check element picture#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "picture")))
    print('PASS - step 1666')
except Exception as e:
    print('FAIL - step 1666' if isinstance(e, AssertionError) else f'ERROR - step 1666: {e}')

print("STEP 1667 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1667')
except Exception as e:
    print('FAIL - step 1667' if isinstance(e, AssertionError) else f'ERROR - step 1667: {e}')

print("STEP 1668 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1668')
except Exception as e:
    print('FAIL - step 1668' if isinstance(e, AssertionError) else f'ERROR - step 1668: {e}')

print("STEP 1669 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1669')
except Exception as e:
    print('FAIL - step 1669' if isinstance(e, AssertionError) else f'ERROR - step 1669: {e}')

print("STEP 1670 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1670')
except Exception as e:
    print('FAIL - step 1670' if isinstance(e, AssertionError) else f'ERROR - step 1670: {e}')

print("STEP 1671 - Check element div#None.['media-gallery-contents']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-contents']")))
    print('PASS - step 1671')
except Exception as e:
    print('FAIL - step 1671' if isinstance(e, AssertionError) else f'ERROR - step 1671: {e}')

print("STEP 1672 - Check element div#None.['media-gallery-top-content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-top-content']")))
    print('PASS - step 1672')
except Exception as e:
    print('FAIL - step 1672' if isinstance(e, AssertionError) else f'ERROR - step 1672: {e}')

print("STEP 1673 - Check element div#None.['media-gallery-logo', 'media-gallery-logo-arcade']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-logo', 'media-gallery-logo-arcade']")))
    print('PASS - step 1673')
except Exception as e:
    print('FAIL - step 1673' if isinstance(e, AssertionError) else f'ERROR - step 1673: {e}')

print("STEP 1674 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 1674')
except Exception as e:
    print('FAIL - step 1674' if isinstance(e, AssertionError) else f'ERROR - step 1674: {e}')

print("STEP 1675 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 1675')
except Exception as e:
    print('FAIL - step 1675' if isinstance(e, AssertionError) else f'ERROR - step 1675: {e}')

print("STEP 1676 - Check element div#None.['media-gallery-bottom-content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-bottom-content']")))
    print('PASS - step 1676')
except Exception as e:
    print('FAIL - step 1676' if isinstance(e, AssertionError) else f'ERROR - step 1676: {e}')

print("STEP 1677 - Check element div#None.['button', 'button-neutral', 'media-gallery-button']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['button', 'button-neutral', 'media-gallery-button']")))
    print('PASS - step 1677')
except Exception as e:
    print('FAIL - step 1677' if isinstance(e, AssertionError) else f'ERROR - step 1677: {e}')

print("STEP 1678 - Check element p#None.['media-gallery-longnote']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-longnote']")))
    print('PASS - step 1678')
except Exception as e:
    print('FAIL - step 1678' if isinstance(e, AssertionError) else f'ERROR - step 1678: {e}')

print("STEP 1679 - Check element li#endless-entertainment-gallery-item-9.['media-gallery-item', 'theme-dark', 'current-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "endless-entertainment-gallery-item-9")))
    print('PASS - step 1679')
except Exception as e:
    print('FAIL - step 1679' if isinstance(e, AssertionError) else f'ERROR - step 1679: {e}')

print("STEP 1680 - Check element a#media-gallery-item-9.['media-gallery-wrapper-link', 'fam-media-gallery-wrapper-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "media-gallery-item-9")))
    print('PASS - step 1680')
except Exception as e:
    print('FAIL - step 1680' if isinstance(e, AssertionError) else f'ERROR - step 1680: {e}')

print("STEP 1681 - Check element div#None.['media-gallery-bg-wrapper', 'media-gallery-bg-wrapper-music']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-bg-wrapper', 'media-gallery-bg-wrapper-music']")))
    print('PASS - step 1681')
except Exception as e:
    print('FAIL - step 1681' if isinstance(e, AssertionError) else f'ERROR - step 1681: {e}')

print("STEP 1682 - Check element picture#None.['media-gallery-bg', 'media-gallery-bg-music']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-bg', 'media-gallery-bg-music']")))
    print('PASS - step 1682')
except Exception as e:
    print('FAIL - step 1682' if isinstance(e, AssertionError) else f'ERROR - step 1682: {e}')

print("STEP 1683 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1683')
except Exception as e:
    print('FAIL - step 1683' if isinstance(e, AssertionError) else f'ERROR - step 1683: {e}')

print("STEP 1684 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1684')
except Exception as e:
    print('FAIL - step 1684' if isinstance(e, AssertionError) else f'ERROR - step 1684: {e}')

print("STEP 1685 - Check element noscript#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "noscript")))
    print('PASS - step 1685')
except Exception as e:
    print('FAIL - step 1685' if isinstance(e, AssertionError) else f'ERROR - step 1685: {e}')

print("STEP 1686 - Check element picture#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "picture")))
    print('PASS - step 1686')
except Exception as e:
    print('FAIL - step 1686' if isinstance(e, AssertionError) else f'ERROR - step 1686: {e}')

print("STEP 1687 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1687')
except Exception as e:
    print('FAIL - step 1687' if isinstance(e, AssertionError) else f'ERROR - step 1687: {e}')

print("STEP 1688 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1688')
except Exception as e:
    print('FAIL - step 1688' if isinstance(e, AssertionError) else f'ERROR - step 1688: {e}')

print("STEP 1689 - Check element source#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "source")))
    print('PASS - step 1689')
except Exception as e:
    print('FAIL - step 1689' if isinstance(e, AssertionError) else f'ERROR - step 1689: {e}')

print("STEP 1690 - Check element img#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    print('PASS - step 1690')
except Exception as e:
    print('FAIL - step 1690' if isinstance(e, AssertionError) else f'ERROR - step 1690: {e}')

print("STEP 1691 - Check element p#None.['media-gallery-longnote', 'media-gallery-longnote-music', 'media-gallery-longnote-music-hide-medium-small']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-longnote', 'media-gallery-longnote-music', 'media-gallery-longnote-music-hide-medium-small']")))
    print('PASS - step 1691')
except Exception as e:
    print('FAIL - step 1691' if isinstance(e, AssertionError) else f'ERROR - step 1691: {e}')

print("STEP 1692 - Check element div#None.['media-gallery-contents']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-contents']")))
    print('PASS - step 1692')
except Exception as e:
    print('FAIL - step 1692' if isinstance(e, AssertionError) else f'ERROR - step 1692: {e}')

print("STEP 1693 - Check element div#None.['media-gallery-top-content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-top-content']")))
    print('PASS - step 1693')
except Exception as e:
    print('FAIL - step 1693' if isinstance(e, AssertionError) else f'ERROR - step 1693: {e}')

print("STEP 1694 - Check element div#None.['media-gallery-logo', 'media-gallery-logo-music']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-logo', 'media-gallery-logo-music']")))
    print('PASS - step 1694')
except Exception as e:
    print('FAIL - step 1694' if isinstance(e, AssertionError) else f'ERROR - step 1694: {e}')

print("STEP 1695 - Check element svg#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "svg")))
    print('PASS - step 1695')
except Exception as e:
    print('FAIL - step 1695' if isinstance(e, AssertionError) else f'ERROR - step 1695: {e}')

print("STEP 1696 - Check element path#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "path")))
    print('PASS - step 1696')
except Exception as e:
    print('FAIL - step 1696' if isinstance(e, AssertionError) else f'ERROR - step 1696: {e}')

print("STEP 1697 - Check element div#None.['media-gallery-bottom-content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-bottom-content']")))
    print('PASS - step 1697')
except Exception as e:
    print('FAIL - step 1697' if isinstance(e, AssertionError) else f'ERROR - step 1697: {e}')

print("STEP 1698 - Check element div#None.['button', 'button-neutral', 'media-gallery-button']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['button', 'button-neutral', 'media-gallery-button']")))
    print('PASS - step 1698')
except Exception as e:
    print('FAIL - step 1698' if isinstance(e, AssertionError) else f'ERROR - step 1698: {e}')

print("STEP 1699 - Check element p#None.['media-gallery-longnote', 'media-gallery-longnote-music', 'media-gallery-longnote-music-hide-large']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['media-gallery-longnote', 'media-gallery-longnote-music', 'media-gallery-longnote-music-hide-large']")))
    print('PASS - step 1699')
except Exception as e:
    print('FAIL - step 1699' if isinstance(e, AssertionError) else f'ERROR - step 1699: {e}')

print("STEP 1700 - Check element footer#ac-globalfooter.['js']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "ac-globalfooter")))
    print('PASS - step 1700')
except Exception as e:
    print('FAIL - step 1700' if isinstance(e, AssertionError) else f'ERROR - step 1700: {e}')

print("STEP 1701 - Check element div#None.['ac-gf-content']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-content']")))
    print('PASS - step 1701')
except Exception as e:
    print('FAIL - step 1701' if isinstance(e, AssertionError) else f'ERROR - step 1701: {e}')

print("STEP 1702 - Check element h2#ac-gf-label.['ac-gf-label']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "ac-gf-label")))
    print('PASS - step 1702')
except Exception as e:
    print('FAIL - step 1702' if isinstance(e, AssertionError) else f'ERROR - step 1702: {e}')

print("STEP 1703 - Check element section#None.['ac-gf-sosumi']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-sosumi']")))
    print('PASS - step 1703')
except Exception as e:
    print('FAIL - step 1703' if isinstance(e, AssertionError) else f'ERROR - step 1703: {e}')

print("STEP 1704 - Check element ul#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "ul")))
    print('PASS - step 1704')
except Exception as e:
    print('FAIL - step 1704' if isinstance(e, AssertionError) else f'ERROR - step 1704: {e}')

print("STEP 1705 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 1705')
except Exception as e:
    print('FAIL - step 1705' if isinstance(e, AssertionError) else f'ERROR - step 1705: {e}')

print("STEP 1706 - Check element span#footnote-1.['tax-holiday-legal-hide']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "footnote-1")))
    print('PASS - step 1706')
except Exception as e:
    print('FAIL - step 1706' if isinstance(e, AssertionError) else f'ERROR - step 1706: {e}')

print("STEP 1707 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 1707')
except Exception as e:
    print('FAIL - step 1707' if isinstance(e, AssertionError) else f'ERROR - step 1707: {e}')

print("STEP 1708 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 1708')
except Exception as e:
    print('FAIL - step 1708' if isinstance(e, AssertionError) else f'ERROR - step 1708: {e}')

print("STEP 1709 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 1709')
except Exception as e:
    print('FAIL - step 1709' if isinstance(e, AssertionError) else f'ERROR - step 1709: {e}')

print("STEP 1710 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 1710')
except Exception as e:
    print('FAIL - step 1710' if isinstance(e, AssertionError) else f'ERROR - step 1710: {e}')

print("STEP 1711 - Check element a#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "a")))
    print('PASS - step 1711')
except Exception as e:
    print('FAIL - step 1711' if isinstance(e, AssertionError) else f'ERROR - step 1711: {e}')

print("STEP 1712 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 1712')
except Exception as e:
    print('FAIL - step 1712' if isinstance(e, AssertionError) else f'ERROR - step 1712: {e}')

print("STEP 1713 - Check element span#None.['fam-legal']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['fam-legal']")))
    print('PASS - step 1713')
except Exception as e:
    print('FAIL - step 1713' if isinstance(e, AssertionError) else f'ERROR - step 1713: {e}')

print("STEP 1714 - Check element li#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "li")))
    print('PASS - step 1714')
except Exception as e:
    print('FAIL - step 1714' if isinstance(e, AssertionError) else f'ERROR - step 1714: {e}')

print("STEP 1715 - Check element nav#None.['ac-gf-directory', 'with-5-columns']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory', 'with-5-columns']")))
    print('PASS - step 1715')
except Exception as e:
    print('FAIL - step 1715' if isinstance(e, AssertionError) else f'ERROR - step 1715: {e}')

print("STEP 1716 - Check element div#None.['ac-gf-directory-column']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column']")))
    print('PASS - step 1716')
except Exception as e:
    print('FAIL - step 1716' if isinstance(e, AssertionError) else f'ERROR - step 1716: {e}')

print("STEP 1717 - Check element div#None.['ac-gf-directory-column-section']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section']")))
    print('PASS - step 1717')
except Exception as e:
    print('FAIL - step 1717' if isinstance(e, AssertionError) else f'ERROR - step 1717: {e}')

print("STEP 1718 - Check element h3#None.['ac-gf-directory-column-section-title']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-title']")))
    print('PASS - step 1718')
except Exception as e:
    print('FAIL - step 1718' if isinstance(e, AssertionError) else f'ERROR - step 1718: {e}')

print("STEP 1719 - Check element span#None.['ac-gf-directory-column-section-title-text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-title-text']")))
    print('PASS - step 1719')
except Exception as e:
    print('FAIL - step 1719' if isinstance(e, AssertionError) else f'ERROR - step 1719: {e}')

print("STEP 1720 - Check element button#None.['ac-gf-directory-column-section-title-button']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-title-button']")))
    print('PASS - step 1720')
except Exception as e:
    print('FAIL - step 1720' if isinstance(e, AssertionError) else f'ERROR - step 1720: {e}')

print("STEP 1721 - Check element span#None.['ac-gf-directory-column-section-title-text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-title-text']")))
    print('PASS - step 1721')
except Exception as e:
    print('FAIL - step 1721' if isinstance(e, AssertionError) else f'ERROR - step 1721: {e}')

print("STEP 1722 - Check element span#None.['ac-gf-directory-column-section-title-icon']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-title-icon']")))
    print('PASS - step 1722')
except Exception as e:
    print('FAIL - step 1722' if isinstance(e, AssertionError) else f'ERROR - step 1722: {e}')

print("STEP 1723 - Check element svg#None.['footer-icon-svg']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['footer-icon-svg']")))
    print('PASS - step 1723')
except Exception as e:
    print('FAIL - step 1723' if isinstance(e, AssertionError) else f'ERROR - step 1723: {e}')

print("STEP 1724 - Check element polyline#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "polyline")))
    print('PASS - step 1724')
except Exception as e:
    print('FAIL - step 1724' if isinstance(e, AssertionError) else f'ERROR - step 1724: {e}')

print("STEP 1725 - Check element animate#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "animate")))
    print('PASS - step 1725')
except Exception as e:
    print('FAIL - step 1725' if isinstance(e, AssertionError) else f'ERROR - step 1725: {e}')

print("STEP 1726 - Check element animate#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "animate")))
    print('PASS - step 1726')
except Exception as e:
    print('FAIL - step 1726' if isinstance(e, AssertionError) else f'ERROR - step 1726: {e}')

print("STEP 1727 - Check element ul#footer-directory-column-section-products.['ac-gf-directory-column-section-list']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "footer-directory-column-section-products")))
    print('PASS - step 1727')
except Exception as e:
    print('FAIL - step 1727' if isinstance(e, AssertionError) else f'ERROR - step 1727: {e}')

print("STEP 1728 - Check element li#None.['ac-gf-directory-column-section-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-item']")))
    print('PASS - step 1728')
except Exception as e:
    print('FAIL - step 1728' if isinstance(e, AssertionError) else f'ERROR - step 1728: {e}')

print("STEP 1729 - Check element a#None.['ac-gf-directory-column-section-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-link']")))
    print('PASS - step 1729')
except Exception as e:
    print('FAIL - step 1729' if isinstance(e, AssertionError) else f'ERROR - step 1729: {e}')

print("STEP 1730 - Check element li#None.['ac-gf-directory-column-section-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-item']")))
    print('PASS - step 1730')
except Exception as e:
    print('FAIL - step 1730' if isinstance(e, AssertionError) else f'ERROR - step 1730: {e}')

print("STEP 1731 - Check element a#None.['ac-gf-directory-column-section-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-link']")))
    print('PASS - step 1731')
except Exception as e:
    print('FAIL - step 1731' if isinstance(e, AssertionError) else f'ERROR - step 1731: {e}')

print("STEP 1732 - Check element li#None.['ac-gf-directory-column-section-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-item']")))
    print('PASS - step 1732')
except Exception as e:
    print('FAIL - step 1732' if isinstance(e, AssertionError) else f'ERROR - step 1732: {e}')

print("STEP 1733 - Check element a#None.['ac-gf-directory-column-section-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-link']")))
    print('PASS - step 1733')
except Exception as e:
    print('FAIL - step 1733' if isinstance(e, AssertionError) else f'ERROR - step 1733: {e}')

print("STEP 1734 - Check element li#None.['ac-gf-directory-column-section-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-item']")))
    print('PASS - step 1734')
except Exception as e:
    print('FAIL - step 1734' if isinstance(e, AssertionError) else f'ERROR - step 1734: {e}')

print("STEP 1735 - Check element a#None.['ac-gf-directory-column-section-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-link']")))
    print('PASS - step 1735')
except Exception as e:
    print('FAIL - step 1735' if isinstance(e, AssertionError) else f'ERROR - step 1735: {e}')

print("STEP 1736 - Check element li#None.['ac-gf-directory-column-section-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-item']")))
    print('PASS - step 1736')
except Exception as e:
    print('FAIL - step 1736' if isinstance(e, AssertionError) else f'ERROR - step 1736: {e}')

print("STEP 1737 - Check element a#None.['ac-gf-directory-column-section-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-link']")))
    print('PASS - step 1737')
except Exception as e:
    print('FAIL - step 1737' if isinstance(e, AssertionError) else f'ERROR - step 1737: {e}')

print("STEP 1738 - Check element li#None.['ac-gf-directory-column-section-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-item']")))
    print('PASS - step 1738')
except Exception as e:
    print('FAIL - step 1738' if isinstance(e, AssertionError) else f'ERROR - step 1738: {e}')

print("STEP 1739 - Check element a#None.['ac-gf-directory-column-section-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-link']")))
    print('PASS - step 1739')
except Exception as e:
    print('FAIL - step 1739' if isinstance(e, AssertionError) else f'ERROR - step 1739: {e}')

print("STEP 1740 - Check element li#None.['ac-gf-directory-column-section-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-item']")))
    print('PASS - step 1740')
except Exception as e:
    print('FAIL - step 1740' if isinstance(e, AssertionError) else f'ERROR - step 1740: {e}')

print("STEP 1741 - Check element a#None.['ac-gf-directory-column-section-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-link']")))
    print('PASS - step 1741')
except Exception as e:
    print('FAIL - step 1741' if isinstance(e, AssertionError) else f'ERROR - step 1741: {e}')

print("STEP 1742 - Check element li#None.['ac-gf-directory-column-section-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-item']")))
    print('PASS - step 1742')
except Exception as e:
    print('FAIL - step 1742' if isinstance(e, AssertionError) else f'ERROR - step 1742: {e}')

print("STEP 1743 - Check element a#None.['ac-gf-directory-column-section-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-link']")))
    print('PASS - step 1743')
except Exception as e:
    print('FAIL - step 1743' if isinstance(e, AssertionError) else f'ERROR - step 1743: {e}')

print("STEP 1744 - Check element li#None.['ac-gf-directory-column-section-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-item']")))
    print('PASS - step 1744')
except Exception as e:
    print('FAIL - step 1744' if isinstance(e, AssertionError) else f'ERROR - step 1744: {e}')

print("STEP 1745 - Check element a#None.['ac-gf-directory-column-section-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-link']")))
    print('PASS - step 1745')
except Exception as e:
    print('FAIL - step 1745' if isinstance(e, AssertionError) else f'ERROR - step 1745: {e}')

print("STEP 1746 - Check element li#None.['ac-gf-directory-column-section-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-item']")))
    print('PASS - step 1746')
except Exception as e:
    print('FAIL - step 1746' if isinstance(e, AssertionError) else f'ERROR - step 1746: {e}')

print("STEP 1747 - Check element a#None.['ac-gf-directory-column-section-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-link']")))
    print('PASS - step 1747')
except Exception as e:
    print('FAIL - step 1747' if isinstance(e, AssertionError) else f'ERROR - step 1747: {e}')

print("STEP 1748 - Check element li#None.['ac-gf-directory-column-section-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-item']")))
    print('PASS - step 1748')
except Exception as e:
    print('FAIL - step 1748' if isinstance(e, AssertionError) else f'ERROR - step 1748: {e}')

print("STEP 1749 - Check element a#None.['ac-gf-directory-column-section-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-link']")))
    print('PASS - step 1749')
except Exception as e:
    print('FAIL - step 1749' if isinstance(e, AssertionError) else f'ERROR - step 1749: {e}')

print("STEP 1750 - Check element div#None.['ac-gf-directory-column-section']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section']")))
    print('PASS - step 1750')
except Exception as e:
    print('FAIL - step 1750' if isinstance(e, AssertionError) else f'ERROR - step 1750: {e}')

print("STEP 1751 - Check element h3#None.['ac-gf-directory-column-section-title']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-title']")))
    print('PASS - step 1751')
except Exception as e:
    print('FAIL - step 1751' if isinstance(e, AssertionError) else f'ERROR - step 1751: {e}')

print("STEP 1752 - Check element span#None.['ac-gf-directory-column-section-title-text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-title-text']")))
    print('PASS - step 1752')
except Exception as e:
    print('FAIL - step 1752' if isinstance(e, AssertionError) else f'ERROR - step 1752: {e}')

print("STEP 1753 - Check element button#None.['ac-gf-directory-column-section-title-button']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-title-button']")))
    print('PASS - step 1753')
except Exception as e:
    print('FAIL - step 1753' if isinstance(e, AssertionError) else f'ERROR - step 1753: {e}')

print("STEP 1754 - Check element span#None.['ac-gf-directory-column-section-title-text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-title-text']")))
    print('PASS - step 1754')
except Exception as e:
    print('FAIL - step 1754' if isinstance(e, AssertionError) else f'ERROR - step 1754: {e}')

print("STEP 1755 - Check element span#None.['ac-gf-directory-column-section-title-icon']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-title-icon']")))
    print('PASS - step 1755')
except Exception as e:
    print('FAIL - step 1755' if isinstance(e, AssertionError) else f'ERROR - step 1755: {e}')

print("STEP 1756 - Check element svg#None.['footer-icon-svg']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['footer-icon-svg']")))
    print('PASS - step 1756')
except Exception as e:
    print('FAIL - step 1756' if isinstance(e, AssertionError) else f'ERROR - step 1756: {e}')

print("STEP 1757 - Check element polyline#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "polyline")))
    print('PASS - step 1757')
except Exception as e:
    print('FAIL - step 1757' if isinstance(e, AssertionError) else f'ERROR - step 1757: {e}')

print("STEP 1758 - Check element animate#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "animate")))
    print('PASS - step 1758')
except Exception as e:
    print('FAIL - step 1758' if isinstance(e, AssertionError) else f'ERROR - step 1758: {e}')

print("STEP 1759 - Check element animate#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "animate")))
    print('PASS - step 1759')
except Exception as e:
    print('FAIL - step 1759' if isinstance(e, AssertionError) else f'ERROR - step 1759: {e}')

print("STEP 1760 - Check element ul#footer-directory-column-section-applewallet.['ac-gf-directory-column-section-list']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "footer-directory-column-section-applewallet")))
    print('PASS - step 1760')
except Exception as e:
    print('FAIL - step 1760' if isinstance(e, AssertionError) else f'ERROR - step 1760: {e}')

print("STEP 1761 - Check element li#None.['ac-gf-directory-column-section-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-item']")))
    print('PASS - step 1761')
except Exception as e:
    print('FAIL - step 1761' if isinstance(e, AssertionError) else f'ERROR - step 1761: {e}')

print("STEP 1762 - Check element a#None.['ac-gf-directory-column-section-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-link']")))
    print('PASS - step 1762')
except Exception as e:
    print('FAIL - step 1762' if isinstance(e, AssertionError) else f'ERROR - step 1762: {e}')

print("STEP 1763 - Check element li#None.['ac-gf-directory-column-section-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-item']")))
    print('PASS - step 1763')
except Exception as e:
    print('FAIL - step 1763' if isinstance(e, AssertionError) else f'ERROR - step 1763: {e}')

print("STEP 1764 - Check element a#None.['ac-gf-directory-column-section-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-link']")))
    print('PASS - step 1764')
except Exception as e:
    print('FAIL - step 1764' if isinstance(e, AssertionError) else f'ERROR - step 1764: {e}')

print("STEP 1765 - Check element li#None.['ac-gf-directory-column-section-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-item']")))
    print('PASS - step 1765')
except Exception as e:
    print('FAIL - step 1765' if isinstance(e, AssertionError) else f'ERROR - step 1765: {e}')

print("STEP 1766 - Check element a#None.['ac-gf-directory-column-section-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-link']")))
    print('PASS - step 1766')
except Exception as e:
    print('FAIL - step 1766' if isinstance(e, AssertionError) else f'ERROR - step 1766: {e}')

print("STEP 1767 - Check element li#None.['ac-gf-directory-column-section-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-item']")))
    print('PASS - step 1767')
except Exception as e:
    print('FAIL - step 1767' if isinstance(e, AssertionError) else f'ERROR - step 1767: {e}')

print("STEP 1768 - Check element a#None.['ac-gf-directory-column-section-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-link']")))
    print('PASS - step 1768')
except Exception as e:
    print('FAIL - step 1768' if isinstance(e, AssertionError) else f'ERROR - step 1768: {e}')

print("STEP 1769 - Check element div#None.['ac-gf-directory-column']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column']")))
    print('PASS - step 1769')
except Exception as e:
    print('FAIL - step 1769' if isinstance(e, AssertionError) else f'ERROR - step 1769: {e}')

print("STEP 1770 - Check element div#None.['ac-gf-directory-column-section']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section']")))
    print('PASS - step 1770')
except Exception as e:
    print('FAIL - step 1770' if isinstance(e, AssertionError) else f'ERROR - step 1770: {e}')

print("STEP 1771 - Check element h3#None.['ac-gf-directory-column-section-title']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-title']")))
    print('PASS - step 1771')
except Exception as e:
    print('FAIL - step 1771' if isinstance(e, AssertionError) else f'ERROR - step 1771: {e}')

print("STEP 1772 - Check element span#None.['ac-gf-directory-column-section-title-text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-title-text']")))
    print('PASS - step 1772')
except Exception as e:
    print('FAIL - step 1772' if isinstance(e, AssertionError) else f'ERROR - step 1772: {e}')

print("STEP 1773 - Check element button#None.['ac-gf-directory-column-section-title-button']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-title-button']")))
    print('PASS - step 1773')
except Exception as e:
    print('FAIL - step 1773' if isinstance(e, AssertionError) else f'ERROR - step 1773: {e}')

print("STEP 1774 - Check element span#None.['ac-gf-directory-column-section-title-text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-title-text']")))
    print('PASS - step 1774')
except Exception as e:
    print('FAIL - step 1774' if isinstance(e, AssertionError) else f'ERROR - step 1774: {e}')

print("STEP 1775 - Check element span#None.['ac-gf-directory-column-section-title-icon']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-title-icon']")))
    print('PASS - step 1775')
except Exception as e:
    print('FAIL - step 1775' if isinstance(e, AssertionError) else f'ERROR - step 1775: {e}')

print("STEP 1776 - Check element svg#None.['footer-icon-svg']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['footer-icon-svg']")))
    print('PASS - step 1776')
except Exception as e:
    print('FAIL - step 1776' if isinstance(e, AssertionError) else f'ERROR - step 1776: {e}')

print("STEP 1777 - Check element polyline#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "polyline")))
    print('PASS - step 1777')
except Exception as e:
    print('FAIL - step 1777' if isinstance(e, AssertionError) else f'ERROR - step 1777: {e}')

print("STEP 1778 - Check element animate#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "animate")))
    print('PASS - step 1778')
except Exception as e:
    print('FAIL - step 1778' if isinstance(e, AssertionError) else f'ERROR - step 1778: {e}')

print("STEP 1779 - Check element animate#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "animate")))
    print('PASS - step 1779')
except Exception as e:
    print('FAIL - step 1779' if isinstance(e, AssertionError) else f'ERROR - step 1779: {e}')

print("STEP 1780 - Check element ul#footer-directory-column-section-accounts.['ac-gf-directory-column-section-list']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "footer-directory-column-section-accounts")))
    print('PASS - step 1780')
except Exception as e:
    print('FAIL - step 1780' if isinstance(e, AssertionError) else f'ERROR - step 1780: {e}')

print("STEP 1781 - Check element li#None.['ac-gf-directory-column-section-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-item']")))
    print('PASS - step 1781')
except Exception as e:
    print('FAIL - step 1781' if isinstance(e, AssertionError) else f'ERROR - step 1781: {e}')

print("STEP 1782 - Check element a#None.['ac-gf-directory-column-section-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-link']")))
    print('PASS - step 1782')
except Exception as e:
    print('FAIL - step 1782' if isinstance(e, AssertionError) else f'ERROR - step 1782: {e}')

print("STEP 1783 - Check element li#None.['ac-gf-directory-column-section-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-item']")))
    print('PASS - step 1783')
except Exception as e:
    print('FAIL - step 1783' if isinstance(e, AssertionError) else f'ERROR - step 1783: {e}')

print("STEP 1784 - Check element a#None.['ac-gf-directory-column-section-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-link']")))
    print('PASS - step 1784')
except Exception as e:
    print('FAIL - step 1784' if isinstance(e, AssertionError) else f'ERROR - step 1784: {e}')

print("STEP 1785 - Check element li#None.['ac-gf-directory-column-section-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-item']")))
    print('PASS - step 1785')
except Exception as e:
    print('FAIL - step 1785' if isinstance(e, AssertionError) else f'ERROR - step 1785: {e}')

print("STEP 1786 - Check element a#None.['ac-gf-directory-column-section-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-link']")))
    print('PASS - step 1786')
except Exception as e:
    print('FAIL - step 1786' if isinstance(e, AssertionError) else f'ERROR - step 1786: {e}')

print("STEP 1787 - Check element div#None.['ac-gf-directory-column-section']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section']")))
    print('PASS - step 1787')
except Exception as e:
    print('FAIL - step 1787' if isinstance(e, AssertionError) else f'ERROR - step 1787: {e}')

print("STEP 1788 - Check element h3#None.['ac-gf-directory-column-section-title']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-title']")))
    print('PASS - step 1788')
except Exception as e:
    print('FAIL - step 1788' if isinstance(e, AssertionError) else f'ERROR - step 1788: {e}')

print("STEP 1789 - Check element span#None.['ac-gf-directory-column-section-title-text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-title-text']")))
    print('PASS - step 1789')
except Exception as e:
    print('FAIL - step 1789' if isinstance(e, AssertionError) else f'ERROR - step 1789: {e}')

print("STEP 1790 - Check element button#None.['ac-gf-directory-column-section-title-button']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-title-button']")))
    print('PASS - step 1790')
except Exception as e:
    print('FAIL - step 1790' if isinstance(e, AssertionError) else f'ERROR - step 1790: {e}')

print("STEP 1791 - Check element span#None.['ac-gf-directory-column-section-title-text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-title-text']")))
    print('PASS - step 1791')
except Exception as e:
    print('FAIL - step 1791' if isinstance(e, AssertionError) else f'ERROR - step 1791: {e}')

print("STEP 1792 - Check element span#None.['ac-gf-directory-column-section-title-icon']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-title-icon']")))
    print('PASS - step 1792')
except Exception as e:
    print('FAIL - step 1792' if isinstance(e, AssertionError) else f'ERROR - step 1792: {e}')

print("STEP 1793 - Check element svg#None.['footer-icon-svg']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['footer-icon-svg']")))
    print('PASS - step 1793')
except Exception as e:
    print('FAIL - step 1793' if isinstance(e, AssertionError) else f'ERROR - step 1793: {e}')

print("STEP 1794 - Check element polyline#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "polyline")))
    print('PASS - step 1794')
except Exception as e:
    print('FAIL - step 1794' if isinstance(e, AssertionError) else f'ERROR - step 1794: {e}')

print("STEP 1795 - Check element animate#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "animate")))
    print('PASS - step 1795')
except Exception as e:
    print('FAIL - step 1795' if isinstance(e, AssertionError) else f'ERROR - step 1795: {e}')

print("STEP 1796 - Check element animate#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "animate")))
    print('PASS - step 1796')
except Exception as e:
    print('FAIL - step 1796' if isinstance(e, AssertionError) else f'ERROR - step 1796: {e}')

print("STEP 1797 - Check element ul#footer-directory-column-section-entertainment.['ac-gf-directory-column-section-list']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "footer-directory-column-section-entertainment")))
    print('PASS - step 1797')
except Exception as e:
    print('FAIL - step 1797' if isinstance(e, AssertionError) else f'ERROR - step 1797: {e}')

print("STEP 1798 - Check element li#None.['ac-gf-directory-column-section-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-item']")))
    print('PASS - step 1798')
except Exception as e:
    print('FAIL - step 1798' if isinstance(e, AssertionError) else f'ERROR - step 1798: {e}')

print("STEP 1799 - Check element a#None.['ac-gf-directory-column-section-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-link']")))
    print('PASS - step 1799')
except Exception as e:
    print('FAIL - step 1799' if isinstance(e, AssertionError) else f'ERROR - step 1799: {e}')

print("STEP 1800 - Check element li#None.['ac-gf-directory-column-section-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-item']")))
    print('PASS - step 1800')
except Exception as e:
    print('FAIL - step 1800' if isinstance(e, AssertionError) else f'ERROR - step 1800: {e}')

print("STEP 1801 - Check element a#None.['ac-gf-directory-column-section-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-link']")))
    print('PASS - step 1801')
except Exception as e:
    print('FAIL - step 1801' if isinstance(e, AssertionError) else f'ERROR - step 1801: {e}')

print("STEP 1802 - Check element li#None.['ac-gf-directory-column-section-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-item']")))
    print('PASS - step 1802')
except Exception as e:
    print('FAIL - step 1802' if isinstance(e, AssertionError) else f'ERROR - step 1802: {e}')

print("STEP 1803 - Check element a#None.['ac-gf-directory-column-section-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-link']")))
    print('PASS - step 1803')
except Exception as e:
    print('FAIL - step 1803' if isinstance(e, AssertionError) else f'ERROR - step 1803: {e}')

print("STEP 1804 - Check element li#None.['ac-gf-directory-column-section-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-item']")))
    print('PASS - step 1804')
except Exception as e:
    print('FAIL - step 1804' if isinstance(e, AssertionError) else f'ERROR - step 1804: {e}')

print("STEP 1805 - Check element a#None.['ac-gf-directory-column-section-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-link']")))
    print('PASS - step 1805')
except Exception as e:
    print('FAIL - step 1805' if isinstance(e, AssertionError) else f'ERROR - step 1805: {e}')

print("STEP 1806 - Check element li#None.['ac-gf-directory-column-section-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-item']")))
    print('PASS - step 1806')
except Exception as e:
    print('FAIL - step 1806' if isinstance(e, AssertionError) else f'ERROR - step 1806: {e}')

print("STEP 1807 - Check element a#None.['ac-gf-directory-column-section-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-link']")))
    print('PASS - step 1807')
except Exception as e:
    print('FAIL - step 1807' if isinstance(e, AssertionError) else f'ERROR - step 1807: {e}')

print("STEP 1808 - Check element li#None.['ac-gf-directory-column-section-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-item']")))
    print('PASS - step 1808')
except Exception as e:
    print('FAIL - step 1808' if isinstance(e, AssertionError) else f'ERROR - step 1808: {e}')

print("STEP 1809 - Check element a#None.['ac-gf-directory-column-section-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-link']")))
    print('PASS - step 1809')
except Exception as e:
    print('FAIL - step 1809' if isinstance(e, AssertionError) else f'ERROR - step 1809: {e}')

print("STEP 1810 - Check element li#None.['ac-gf-directory-column-section-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-item']")))
    print('PASS - step 1810')
except Exception as e:
    print('FAIL - step 1810' if isinstance(e, AssertionError) else f'ERROR - step 1810: {e}')

print("STEP 1811 - Check element a#None.['ac-gf-directory-column-section-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-link']")))
    print('PASS - step 1811')
except Exception as e:
    print('FAIL - step 1811' if isinstance(e, AssertionError) else f'ERROR - step 1811: {e}')

print("STEP 1812 - Check element li#None.['ac-gf-directory-column-section-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-item']")))
    print('PASS - step 1812')
except Exception as e:
    print('FAIL - step 1812' if isinstance(e, AssertionError) else f'ERROR - step 1812: {e}')

print("STEP 1813 - Check element a#None.['ac-gf-directory-column-section-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-link']")))
    print('PASS - step 1813')
except Exception as e:
    print('FAIL - step 1813' if isinstance(e, AssertionError) else f'ERROR - step 1813: {e}')

print("STEP 1814 - Check element li#None.['ac-gf-directory-column-section-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-item']")))
    print('PASS - step 1814')
except Exception as e:
    print('FAIL - step 1814' if isinstance(e, AssertionError) else f'ERROR - step 1814: {e}')

print("STEP 1815 - Check element a#None.['ac-gf-directory-column-section-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-link']")))
    print('PASS - step 1815')
except Exception as e:
    print('FAIL - step 1815' if isinstance(e, AssertionError) else f'ERROR - step 1815: {e}')

print("STEP 1816 - Check element div#None.['ac-gf-directory-column']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column']")))
    print('PASS - step 1816')
except Exception as e:
    print('FAIL - step 1816' if isinstance(e, AssertionError) else f'ERROR - step 1816: {e}')

print("STEP 1817 - Check element div#None.['ac-gf-directory-column-section']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section']")))
    print('PASS - step 1817')
except Exception as e:
    print('FAIL - step 1817' if isinstance(e, AssertionError) else f'ERROR - step 1817: {e}')

print("STEP 1818 - Check element h3#None.['ac-gf-directory-column-section-title']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-title']")))
    print('PASS - step 1818')
except Exception as e:
    print('FAIL - step 1818' if isinstance(e, AssertionError) else f'ERROR - step 1818: {e}')

print("STEP 1819 - Check element span#None.['ac-gf-directory-column-section-title-text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-title-text']")))
    print('PASS - step 1819')
except Exception as e:
    print('FAIL - step 1819' if isinstance(e, AssertionError) else f'ERROR - step 1819: {e}')

print("STEP 1820 - Check element button#None.['ac-gf-directory-column-section-title-button']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-title-button']")))
    print('PASS - step 1820')
except Exception as e:
    print('FAIL - step 1820' if isinstance(e, AssertionError) else f'ERROR - step 1820: {e}')

print("STEP 1821 - Check element span#None.['ac-gf-directory-column-section-title-text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-title-text']")))
    print('PASS - step 1821')
except Exception as e:
    print('FAIL - step 1821' if isinstance(e, AssertionError) else f'ERROR - step 1821: {e}')

print("STEP 1822 - Check element span#None.['ac-gf-directory-column-section-title-icon']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-title-icon']")))
    print('PASS - step 1822')
except Exception as e:
    print('FAIL - step 1822' if isinstance(e, AssertionError) else f'ERROR - step 1822: {e}')

print("STEP 1823 - Check element svg#None.['footer-icon-svg']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['footer-icon-svg']")))
    print('PASS - step 1823')
except Exception as e:
    print('FAIL - step 1823' if isinstance(e, AssertionError) else f'ERROR - step 1823: {e}')

print("STEP 1824 - Check element polyline#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "polyline")))
    print('PASS - step 1824')
except Exception as e:
    print('FAIL - step 1824' if isinstance(e, AssertionError) else f'ERROR - step 1824: {e}')

print("STEP 1825 - Check element animate#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "animate")))
    print('PASS - step 1825')
except Exception as e:
    print('FAIL - step 1825' if isinstance(e, AssertionError) else f'ERROR - step 1825: {e}')

print("STEP 1826 - Check element animate#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "animate")))
    print('PASS - step 1826')
except Exception as e:
    print('FAIL - step 1826' if isinstance(e, AssertionError) else f'ERROR - step 1826: {e}')

print("STEP 1827 - Check element ul#footer-directory-column-section-storeservices.['ac-gf-directory-column-section-list']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "footer-directory-column-section-storeservices")))
    print('PASS - step 1827')
except Exception as e:
    print('FAIL - step 1827' if isinstance(e, AssertionError) else f'ERROR - step 1827: {e}')

print("STEP 1828 - Check element li#None.['ac-gf-directory-column-section-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-item']")))
    print('PASS - step 1828')
except Exception as e:
    print('FAIL - step 1828' if isinstance(e, AssertionError) else f'ERROR - step 1828: {e}')

print("STEP 1829 - Check element a#None.['ac-gf-directory-column-section-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-link']")))
    print('PASS - step 1829')
except Exception as e:
    print('FAIL - step 1829' if isinstance(e, AssertionError) else f'ERROR - step 1829: {e}')

print("STEP 1830 - Check element li#None.['ac-gf-directory-column-section-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-item']")))
    print('PASS - step 1830')
except Exception as e:
    print('FAIL - step 1830' if isinstance(e, AssertionError) else f'ERROR - step 1830: {e}')

print("STEP 1831 - Check element a#None.['ac-gf-directory-column-section-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-link']")))
    print('PASS - step 1831')
except Exception as e:
    print('FAIL - step 1831' if isinstance(e, AssertionError) else f'ERROR - step 1831: {e}')

print("STEP 1832 - Check element li#None.['ac-gf-directory-column-section-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-item']")))
    print('PASS - step 1832')
except Exception as e:
    print('FAIL - step 1832' if isinstance(e, AssertionError) else f'ERROR - step 1832: {e}')

print("STEP 1833 - Check element a#None.['ac-gf-directory-column-section-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-link']")))
    print('PASS - step 1833')
except Exception as e:
    print('FAIL - step 1833' if isinstance(e, AssertionError) else f'ERROR - step 1833: {e}')

print("STEP 1834 - Check element li#None.['ac-gf-directory-column-section-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-item']")))
    print('PASS - step 1834')
except Exception as e:
    print('FAIL - step 1834' if isinstance(e, AssertionError) else f'ERROR - step 1834: {e}')

print("STEP 1835 - Check element a#None.['ac-gf-directory-column-section-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-link']")))
    print('PASS - step 1835')
except Exception as e:
    print('FAIL - step 1835' if isinstance(e, AssertionError) else f'ERROR - step 1835: {e}')

print("STEP 1836 - Check element li#None.['ac-gf-directory-column-section-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-item']")))
    print('PASS - step 1836')
except Exception as e:
    print('FAIL - step 1836' if isinstance(e, AssertionError) else f'ERROR - step 1836: {e}')

print("STEP 1837 - Check element a#None.['ac-gf-directory-column-section-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-link']")))
    print('PASS - step 1837')
except Exception as e:
    print('FAIL - step 1837' if isinstance(e, AssertionError) else f'ERROR - step 1837: {e}')

print("STEP 1838 - Check element li#None.['ac-gf-directory-column-section-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-item']")))
    print('PASS - step 1838')
except Exception as e:
    print('FAIL - step 1838' if isinstance(e, AssertionError) else f'ERROR - step 1838: {e}')

print("STEP 1839 - Check element a#None.['ac-gf-directory-column-section-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-link']")))
    print('PASS - step 1839')
except Exception as e:
    print('FAIL - step 1839' if isinstance(e, AssertionError) else f'ERROR - step 1839: {e}')

print("STEP 1840 - Check element li#None.['ac-gf-directory-column-section-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-item']")))
    print('PASS - step 1840')
except Exception as e:
    print('FAIL - step 1840' if isinstance(e, AssertionError) else f'ERROR - step 1840: {e}')

print("STEP 1841 - Check element a#None.['ac-gf-directory-column-section-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-link']")))
    print('PASS - step 1841')
except Exception as e:
    print('FAIL - step 1841' if isinstance(e, AssertionError) else f'ERROR - step 1841: {e}')

print("STEP 1842 - Check element li#None.['ac-gf-directory-column-section-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-item']")))
    print('PASS - step 1842')
except Exception as e:
    print('FAIL - step 1842' if isinstance(e, AssertionError) else f'ERROR - step 1842: {e}')

print("STEP 1843 - Check element a#None.['ac-gf-directory-column-section-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-link']")))
    print('PASS - step 1843')
except Exception as e:
    print('FAIL - step 1843' if isinstance(e, AssertionError) else f'ERROR - step 1843: {e}')

print("STEP 1844 - Check element li#None.['ac-gf-directory-column-section-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-item']")))
    print('PASS - step 1844')
except Exception as e:
    print('FAIL - step 1844' if isinstance(e, AssertionError) else f'ERROR - step 1844: {e}')

print("STEP 1845 - Check element a#None.['ac-gf-directory-column-section-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-link']")))
    print('PASS - step 1845')
except Exception as e:
    print('FAIL - step 1845' if isinstance(e, AssertionError) else f'ERROR - step 1845: {e}')

print("STEP 1846 - Check element li#None.['ac-gf-directory-column-section-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-item']")))
    print('PASS - step 1846')
except Exception as e:
    print('FAIL - step 1846' if isinstance(e, AssertionError) else f'ERROR - step 1846: {e}')

print("STEP 1847 - Check element a#None.['ac-gf-directory-column-section-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-link']")))
    print('PASS - step 1847')
except Exception as e:
    print('FAIL - step 1847' if isinstance(e, AssertionError) else f'ERROR - step 1847: {e}')

print("STEP 1848 - Check element li#None.['ac-gf-directory-column-section-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-item']")))
    print('PASS - step 1848')
except Exception as e:
    print('FAIL - step 1848' if isinstance(e, AssertionError) else f'ERROR - step 1848: {e}')

print("STEP 1849 - Check element a#None.['ac-gf-directory-column-section-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-link']")))
    print('PASS - step 1849')
except Exception as e:
    print('FAIL - step 1849' if isinstance(e, AssertionError) else f'ERROR - step 1849: {e}')

print("STEP 1850 - Check element li#None.['ac-gf-directory-column-section-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-item']")))
    print('PASS - step 1850')
except Exception as e:
    print('FAIL - step 1850' if isinstance(e, AssertionError) else f'ERROR - step 1850: {e}')

print("STEP 1851 - Check element a#None.['ac-gf-directory-column-section-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-link']")))
    print('PASS - step 1851')
except Exception as e:
    print('FAIL - step 1851' if isinstance(e, AssertionError) else f'ERROR - step 1851: {e}')

print("STEP 1852 - Check element div#None.['ac-gf-directory-column']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column']")))
    print('PASS - step 1852')
except Exception as e:
    print('FAIL - step 1852' if isinstance(e, AssertionError) else f'ERROR - step 1852: {e}')

print("STEP 1853 - Check element div#None.['ac-gf-directory-column-section']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section']")))
    print('PASS - step 1853')
except Exception as e:
    print('FAIL - step 1853' if isinstance(e, AssertionError) else f'ERROR - step 1853: {e}')

print("STEP 1854 - Check element h3#None.['ac-gf-directory-column-section-title']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-title']")))
    print('PASS - step 1854')
except Exception as e:
    print('FAIL - step 1854' if isinstance(e, AssertionError) else f'ERROR - step 1854: {e}')

print("STEP 1855 - Check element span#None.['ac-gf-directory-column-section-title-text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-title-text']")))
    print('PASS - step 1855')
except Exception as e:
    print('FAIL - step 1855' if isinstance(e, AssertionError) else f'ERROR - step 1855: {e}')

print("STEP 1856 - Check element button#None.['ac-gf-directory-column-section-title-button']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-title-button']")))
    print('PASS - step 1856')
except Exception as e:
    print('FAIL - step 1856' if isinstance(e, AssertionError) else f'ERROR - step 1856: {e}')

print("STEP 1857 - Check element span#None.['ac-gf-directory-column-section-title-text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-title-text']")))
    print('PASS - step 1857')
except Exception as e:
    print('FAIL - step 1857' if isinstance(e, AssertionError) else f'ERROR - step 1857: {e}')

print("STEP 1858 - Check element span#None.['ac-gf-directory-column-section-title-icon']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-title-icon']")))
    print('PASS - step 1858')
except Exception as e:
    print('FAIL - step 1858' if isinstance(e, AssertionError) else f'ERROR - step 1858: {e}')

print("STEP 1859 - Check element svg#None.['footer-icon-svg']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['footer-icon-svg']")))
    print('PASS - step 1859')
except Exception as e:
    print('FAIL - step 1859' if isinstance(e, AssertionError) else f'ERROR - step 1859: {e}')

print("STEP 1860 - Check element polyline#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "polyline")))
    print('PASS - step 1860')
except Exception as e:
    print('FAIL - step 1860' if isinstance(e, AssertionError) else f'ERROR - step 1860: {e}')

print("STEP 1861 - Check element animate#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "animate")))
    print('PASS - step 1861')
except Exception as e:
    print('FAIL - step 1861' if isinstance(e, AssertionError) else f'ERROR - step 1861: {e}')

print("STEP 1862 - Check element animate#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "animate")))
    print('PASS - step 1862')
except Exception as e:
    print('FAIL - step 1862' if isinstance(e, AssertionError) else f'ERROR - step 1862: {e}')

print("STEP 1863 - Check element ul#footer-directory-column-section-business.['ac-gf-directory-column-section-list']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "footer-directory-column-section-business")))
    print('PASS - step 1863')
except Exception as e:
    print('FAIL - step 1863' if isinstance(e, AssertionError) else f'ERROR - step 1863: {e}')

print("STEP 1864 - Check element li#None.['ac-gf-directory-column-section-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-item']")))
    print('PASS - step 1864')
except Exception as e:
    print('FAIL - step 1864' if isinstance(e, AssertionError) else f'ERROR - step 1864: {e}')

print("STEP 1865 - Check element a#None.['ac-gf-directory-column-section-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-link']")))
    print('PASS - step 1865')
except Exception as e:
    print('FAIL - step 1865' if isinstance(e, AssertionError) else f'ERROR - step 1865: {e}')

print("STEP 1866 - Check element li#None.['ac-gf-directory-column-section-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-item']")))
    print('PASS - step 1866')
except Exception as e:
    print('FAIL - step 1866' if isinstance(e, AssertionError) else f'ERROR - step 1866: {e}')

print("STEP 1867 - Check element a#None.['ac-gf-directory-column-section-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-link']")))
    print('PASS - step 1867')
except Exception as e:
    print('FAIL - step 1867' if isinstance(e, AssertionError) else f'ERROR - step 1867: {e}')

print("STEP 1868 - Check element div#None.['ac-gf-directory-column-section']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section']")))
    print('PASS - step 1868')
except Exception as e:
    print('FAIL - step 1868' if isinstance(e, AssertionError) else f'ERROR - step 1868: {e}')

print("STEP 1869 - Check element h3#None.['ac-gf-directory-column-section-title']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-title']")))
    print('PASS - step 1869')
except Exception as e:
    print('FAIL - step 1869' if isinstance(e, AssertionError) else f'ERROR - step 1869: {e}')

print("STEP 1870 - Check element span#None.['ac-gf-directory-column-section-title-text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-title-text']")))
    print('PASS - step 1870')
except Exception as e:
    print('FAIL - step 1870' if isinstance(e, AssertionError) else f'ERROR - step 1870: {e}')

print("STEP 1871 - Check element button#None.['ac-gf-directory-column-section-title-button']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-title-button']")))
    print('PASS - step 1871')
except Exception as e:
    print('FAIL - step 1871' if isinstance(e, AssertionError) else f'ERROR - step 1871: {e}')

print("STEP 1872 - Check element span#None.['ac-gf-directory-column-section-title-text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-title-text']")))
    print('PASS - step 1872')
except Exception as e:
    print('FAIL - step 1872' if isinstance(e, AssertionError) else f'ERROR - step 1872: {e}')

print("STEP 1873 - Check element span#None.['ac-gf-directory-column-section-title-icon']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-title-icon']")))
    print('PASS - step 1873')
except Exception as e:
    print('FAIL - step 1873' if isinstance(e, AssertionError) else f'ERROR - step 1873: {e}')

print("STEP 1874 - Check element svg#None.['footer-icon-svg']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['footer-icon-svg']")))
    print('PASS - step 1874')
except Exception as e:
    print('FAIL - step 1874' if isinstance(e, AssertionError) else f'ERROR - step 1874: {e}')

print("STEP 1875 - Check element polyline#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "polyline")))
    print('PASS - step 1875')
except Exception as e:
    print('FAIL - step 1875' if isinstance(e, AssertionError) else f'ERROR - step 1875: {e}')

print("STEP 1876 - Check element animate#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "animate")))
    print('PASS - step 1876')
except Exception as e:
    print('FAIL - step 1876' if isinstance(e, AssertionError) else f'ERROR - step 1876: {e}')

print("STEP 1877 - Check element animate#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "animate")))
    print('PASS - step 1877')
except Exception as e:
    print('FAIL - step 1877' if isinstance(e, AssertionError) else f'ERROR - step 1877: {e}')

print("STEP 1878 - Check element ul#footer-directory-column-section-education.['ac-gf-directory-column-section-list']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "footer-directory-column-section-education")))
    print('PASS - step 1878')
except Exception as e:
    print('FAIL - step 1878' if isinstance(e, AssertionError) else f'ERROR - step 1878: {e}')

print("STEP 1879 - Check element li#None.['ac-gf-directory-column-section-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-item']")))
    print('PASS - step 1879')
except Exception as e:
    print('FAIL - step 1879' if isinstance(e, AssertionError) else f'ERROR - step 1879: {e}')

print("STEP 1880 - Check element a#None.['ac-gf-directory-column-section-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-link']")))
    print('PASS - step 1880')
except Exception as e:
    print('FAIL - step 1880' if isinstance(e, AssertionError) else f'ERROR - step 1880: {e}')

print("STEP 1881 - Check element li#None.['ac-gf-directory-column-section-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-item']")))
    print('PASS - step 1881')
except Exception as e:
    print('FAIL - step 1881' if isinstance(e, AssertionError) else f'ERROR - step 1881: {e}')

print("STEP 1882 - Check element a#None.['ac-gf-directory-column-section-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-link']")))
    print('PASS - step 1882')
except Exception as e:
    print('FAIL - step 1882' if isinstance(e, AssertionError) else f'ERROR - step 1882: {e}')

print("STEP 1883 - Check element li#None.['ac-gf-directory-column-section-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-item']")))
    print('PASS - step 1883')
except Exception as e:
    print('FAIL - step 1883' if isinstance(e, AssertionError) else f'ERROR - step 1883: {e}')

print("STEP 1884 - Check element a#None.['ac-gf-directory-column-section-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-link']")))
    print('PASS - step 1884')
except Exception as e:
    print('FAIL - step 1884' if isinstance(e, AssertionError) else f'ERROR - step 1884: {e}')

print("STEP 1885 - Check element div#None.['ac-gf-directory-column-section']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section']")))
    print('PASS - step 1885')
except Exception as e:
    print('FAIL - step 1885' if isinstance(e, AssertionError) else f'ERROR - step 1885: {e}')

print("STEP 1886 - Check element h3#None.['ac-gf-directory-column-section-title']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-title']")))
    print('PASS - step 1886')
except Exception as e:
    print('FAIL - step 1886' if isinstance(e, AssertionError) else f'ERROR - step 1886: {e}')

print("STEP 1887 - Check element span#None.['ac-gf-directory-column-section-title-text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-title-text']")))
    print('PASS - step 1887')
except Exception as e:
    print('FAIL - step 1887' if isinstance(e, AssertionError) else f'ERROR - step 1887: {e}')

print("STEP 1888 - Check element button#None.['ac-gf-directory-column-section-title-button']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-title-button']")))
    print('PASS - step 1888')
except Exception as e:
    print('FAIL - step 1888' if isinstance(e, AssertionError) else f'ERROR - step 1888: {e}')

print("STEP 1889 - Check element span#None.['ac-gf-directory-column-section-title-text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-title-text']")))
    print('PASS - step 1889')
except Exception as e:
    print('FAIL - step 1889' if isinstance(e, AssertionError) else f'ERROR - step 1889: {e}')

print("STEP 1890 - Check element span#None.['ac-gf-directory-column-section-title-icon']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-title-icon']")))
    print('PASS - step 1890')
except Exception as e:
    print('FAIL - step 1890' if isinstance(e, AssertionError) else f'ERROR - step 1890: {e}')

print("STEP 1891 - Check element svg#None.['footer-icon-svg']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['footer-icon-svg']")))
    print('PASS - step 1891')
except Exception as e:
    print('FAIL - step 1891' if isinstance(e, AssertionError) else f'ERROR - step 1891: {e}')

print("STEP 1892 - Check element polyline#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "polyline")))
    print('PASS - step 1892')
except Exception as e:
    print('FAIL - step 1892' if isinstance(e, AssertionError) else f'ERROR - step 1892: {e}')

print("STEP 1893 - Check element animate#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "animate")))
    print('PASS - step 1893')
except Exception as e:
    print('FAIL - step 1893' if isinstance(e, AssertionError) else f'ERROR - step 1893: {e}')

print("STEP 1894 - Check element animate#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "animate")))
    print('PASS - step 1894')
except Exception as e:
    print('FAIL - step 1894' if isinstance(e, AssertionError) else f'ERROR - step 1894: {e}')

print("STEP 1895 - Check element ul#footer-directory-column-section-healthcare.['ac-gf-directory-column-section-list']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "footer-directory-column-section-healthcare")))
    print('PASS - step 1895')
except Exception as e:
    print('FAIL - step 1895' if isinstance(e, AssertionError) else f'ERROR - step 1895: {e}')

print("STEP 1896 - Check element li#None.['ac-gf-directory-column-section-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-item']")))
    print('PASS - step 1896')
except Exception as e:
    print('FAIL - step 1896' if isinstance(e, AssertionError) else f'ERROR - step 1896: {e}')

print("STEP 1897 - Check element a#None.['ac-gf-directory-column-section-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-link']")))
    print('PASS - step 1897')
except Exception as e:
    print('FAIL - step 1897' if isinstance(e, AssertionError) else f'ERROR - step 1897: {e}')

print("STEP 1898 - Check element div#None.['ac-gf-directory-column-section']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section']")))
    print('PASS - step 1898')
except Exception as e:
    print('FAIL - step 1898' if isinstance(e, AssertionError) else f'ERROR - step 1898: {e}')

print("STEP 1899 - Check element h3#None.['ac-gf-directory-column-section-title']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-title']")))
    print('PASS - step 1899')
except Exception as e:
    print('FAIL - step 1899' if isinstance(e, AssertionError) else f'ERROR - step 1899: {e}')

print("STEP 1900 - Check element span#None.['ac-gf-directory-column-section-title-text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-title-text']")))
    print('PASS - step 1900')
except Exception as e:
    print('FAIL - step 1900' if isinstance(e, AssertionError) else f'ERROR - step 1900: {e}')

print("STEP 1901 - Check element button#None.['ac-gf-directory-column-section-title-button']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-title-button']")))
    print('PASS - step 1901')
except Exception as e:
    print('FAIL - step 1901' if isinstance(e, AssertionError) else f'ERROR - step 1901: {e}')

print("STEP 1902 - Check element span#None.['ac-gf-directory-column-section-title-text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-title-text']")))
    print('PASS - step 1902')
except Exception as e:
    print('FAIL - step 1902' if isinstance(e, AssertionError) else f'ERROR - step 1902: {e}')

print("STEP 1903 - Check element span#None.['ac-gf-directory-column-section-title-icon']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-title-icon']")))
    print('PASS - step 1903')
except Exception as e:
    print('FAIL - step 1903' if isinstance(e, AssertionError) else f'ERROR - step 1903: {e}')

print("STEP 1904 - Check element svg#None.['footer-icon-svg']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['footer-icon-svg']")))
    print('PASS - step 1904')
except Exception as e:
    print('FAIL - step 1904' if isinstance(e, AssertionError) else f'ERROR - step 1904: {e}')

print("STEP 1905 - Check element polyline#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "polyline")))
    print('PASS - step 1905')
except Exception as e:
    print('FAIL - step 1905' if isinstance(e, AssertionError) else f'ERROR - step 1905: {e}')

print("STEP 1906 - Check element animate#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "animate")))
    print('PASS - step 1906')
except Exception as e:
    print('FAIL - step 1906' if isinstance(e, AssertionError) else f'ERROR - step 1906: {e}')

print("STEP 1907 - Check element animate#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "animate")))
    print('PASS - step 1907')
except Exception as e:
    print('FAIL - step 1907' if isinstance(e, AssertionError) else f'ERROR - step 1907: {e}')

print("STEP 1908 - Check element ul#footer-directory-column-section-government.['ac-gf-directory-column-section-list']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "footer-directory-column-section-government")))
    print('PASS - step 1908')
except Exception as e:
    print('FAIL - step 1908' if isinstance(e, AssertionError) else f'ERROR - step 1908: {e}')

print("STEP 1909 - Check element li#None.['ac-gf-directory-column-section-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-item']")))
    print('PASS - step 1909')
except Exception as e:
    print('FAIL - step 1909' if isinstance(e, AssertionError) else f'ERROR - step 1909: {e}')

print("STEP 1910 - Check element a#None.['ac-gf-directory-column-section-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-link']")))
    print('PASS - step 1910')
except Exception as e:
    print('FAIL - step 1910' if isinstance(e, AssertionError) else f'ERROR - step 1910: {e}')

print("STEP 1911 - Check element li#None.['ac-gf-directory-column-section-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-item']")))
    print('PASS - step 1911')
except Exception as e:
    print('FAIL - step 1911' if isinstance(e, AssertionError) else f'ERROR - step 1911: {e}')

print("STEP 1912 - Check element a#None.['ac-gf-directory-column-section-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-link']")))
    print('PASS - step 1912')
except Exception as e:
    print('FAIL - step 1912' if isinstance(e, AssertionError) else f'ERROR - step 1912: {e}')

print("STEP 1913 - Check element li#None.['ac-gf-directory-column-section-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-item']")))
    print('PASS - step 1913')
except Exception as e:
    print('FAIL - step 1913' if isinstance(e, AssertionError) else f'ERROR - step 1913: {e}')

print("STEP 1914 - Check element a#None.['ac-gf-directory-column-section-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-link']")))
    print('PASS - step 1914')
except Exception as e:
    print('FAIL - step 1914' if isinstance(e, AssertionError) else f'ERROR - step 1914: {e}')

print("STEP 1915 - Check element li#None.['ac-gf-directory-column-section-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-item']")))
    print('PASS - step 1915')
except Exception as e:
    print('FAIL - step 1915' if isinstance(e, AssertionError) else f'ERROR - step 1915: {e}')

print("STEP 1916 - Check element a#None.['ac-gf-directory-column-section-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-link']")))
    print('PASS - step 1916')
except Exception as e:
    print('FAIL - step 1916' if isinstance(e, AssertionError) else f'ERROR - step 1916: {e}')

print("STEP 1917 - Check element div#None.['ac-gf-directory-column']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column']")))
    print('PASS - step 1917')
except Exception as e:
    print('FAIL - step 1917' if isinstance(e, AssertionError) else f'ERROR - step 1917: {e}')

print("STEP 1918 - Check element div#None.['ac-gf-directory-column-section']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section']")))
    print('PASS - step 1918')
except Exception as e:
    print('FAIL - step 1918' if isinstance(e, AssertionError) else f'ERROR - step 1918: {e}')

print("STEP 1919 - Check element h3#None.['ac-gf-directory-column-section-title']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-title']")))
    print('PASS - step 1919')
except Exception as e:
    print('FAIL - step 1919' if isinstance(e, AssertionError) else f'ERROR - step 1919: {e}')

print("STEP 1920 - Check element span#None.['ac-gf-directory-column-section-title-text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-title-text']")))
    print('PASS - step 1920')
except Exception as e:
    print('FAIL - step 1920' if isinstance(e, AssertionError) else f'ERROR - step 1920: {e}')

print("STEP 1921 - Check element button#None.['ac-gf-directory-column-section-title-button']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-title-button']")))
    print('PASS - step 1921')
except Exception as e:
    print('FAIL - step 1921' if isinstance(e, AssertionError) else f'ERROR - step 1921: {e}')

print("STEP 1922 - Check element span#None.['ac-gf-directory-column-section-title-text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-title-text']")))
    print('PASS - step 1922')
except Exception as e:
    print('FAIL - step 1922' if isinstance(e, AssertionError) else f'ERROR - step 1922: {e}')

print("STEP 1923 - Check element span#None.['ac-gf-directory-column-section-title-icon']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-title-icon']")))
    print('PASS - step 1923')
except Exception as e:
    print('FAIL - step 1923' if isinstance(e, AssertionError) else f'ERROR - step 1923: {e}')

print("STEP 1924 - Check element svg#None.['footer-icon-svg']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['footer-icon-svg']")))
    print('PASS - step 1924')
except Exception as e:
    print('FAIL - step 1924' if isinstance(e, AssertionError) else f'ERROR - step 1924: {e}')

print("STEP 1925 - Check element polyline#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "polyline")))
    print('PASS - step 1925')
except Exception as e:
    print('FAIL - step 1925' if isinstance(e, AssertionError) else f'ERROR - step 1925: {e}')

print("STEP 1926 - Check element animate#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "animate")))
    print('PASS - step 1926')
except Exception as e:
    print('FAIL - step 1926' if isinstance(e, AssertionError) else f'ERROR - step 1926: {e}')

print("STEP 1927 - Check element animate#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "animate")))
    print('PASS - step 1927')
except Exception as e:
    print('FAIL - step 1927' if isinstance(e, AssertionError) else f'ERROR - step 1927: {e}')

print("STEP 1928 - Check element ul#footer-directory-column-section-responsibility.['ac-gf-directory-column-section-list']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "footer-directory-column-section-responsibility")))
    print('PASS - step 1928')
except Exception as e:
    print('FAIL - step 1928' if isinstance(e, AssertionError) else f'ERROR - step 1928: {e}')

print("STEP 1929 - Check element li#None.['ac-gf-directory-column-section-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-item']")))
    print('PASS - step 1929')
except Exception as e:
    print('FAIL - step 1929' if isinstance(e, AssertionError) else f'ERROR - step 1929: {e}')

print("STEP 1930 - Check element a#None.['ac-gf-directory-column-section-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-link']")))
    print('PASS - step 1930')
except Exception as e:
    print('FAIL - step 1930' if isinstance(e, AssertionError) else f'ERROR - step 1930: {e}')

print("STEP 1931 - Check element li#None.['ac-gf-directory-column-section-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-item']")))
    print('PASS - step 1931')
except Exception as e:
    print('FAIL - step 1931' if isinstance(e, AssertionError) else f'ERROR - step 1931: {e}')

print("STEP 1932 - Check element a#None.['ac-gf-directory-column-section-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-link']")))
    print('PASS - step 1932')
except Exception as e:
    print('FAIL - step 1932' if isinstance(e, AssertionError) else f'ERROR - step 1932: {e}')

print("STEP 1933 - Check element li#None.['ac-gf-directory-column-section-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-item']")))
    print('PASS - step 1933')
except Exception as e:
    print('FAIL - step 1933' if isinstance(e, AssertionError) else f'ERROR - step 1933: {e}')

print("STEP 1934 - Check element a#None.['ac-gf-directory-column-section-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-link']")))
    print('PASS - step 1934')
except Exception as e:
    print('FAIL - step 1934' if isinstance(e, AssertionError) else f'ERROR - step 1934: {e}')

print("STEP 1935 - Check element li#None.['ac-gf-directory-column-section-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-item']")))
    print('PASS - step 1935')
except Exception as e:
    print('FAIL - step 1935' if isinstance(e, AssertionError) else f'ERROR - step 1935: {e}')

print("STEP 1936 - Check element a#None.['ac-gf-directory-column-section-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-link']")))
    print('PASS - step 1936')
except Exception as e:
    print('FAIL - step 1936' if isinstance(e, AssertionError) else f'ERROR - step 1936: {e}')

print("STEP 1937 - Check element li#None.['ac-gf-directory-column-section-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-item']")))
    print('PASS - step 1937')
except Exception as e:
    print('FAIL - step 1937' if isinstance(e, AssertionError) else f'ERROR - step 1937: {e}')

print("STEP 1938 - Check element a#None.['ac-gf-directory-column-section-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-link']")))
    print('PASS - step 1938')
except Exception as e:
    print('FAIL - step 1938' if isinstance(e, AssertionError) else f'ERROR - step 1938: {e}')

print("STEP 1939 - Check element li#None.['ac-gf-directory-column-section-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-item']")))
    print('PASS - step 1939')
except Exception as e:
    print('FAIL - step 1939' if isinstance(e, AssertionError) else f'ERROR - step 1939: {e}')

print("STEP 1940 - Check element a#None.['ac-gf-directory-column-section-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-link']")))
    print('PASS - step 1940')
except Exception as e:
    print('FAIL - step 1940' if isinstance(e, AssertionError) else f'ERROR - step 1940: {e}')

print("STEP 1941 - Check element li#None.['ac-gf-directory-column-section-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-item']")))
    print('PASS - step 1941')
except Exception as e:
    print('FAIL - step 1941' if isinstance(e, AssertionError) else f'ERROR - step 1941: {e}')

print("STEP 1942 - Check element a#None.['ac-gf-directory-column-section-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-link']")))
    print('PASS - step 1942')
except Exception as e:
    print('FAIL - step 1942' if isinstance(e, AssertionError) else f'ERROR - step 1942: {e}')

print("STEP 1943 - Check element div#None.['ac-gf-directory-column-section']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section']")))
    print('PASS - step 1943')
except Exception as e:
    print('FAIL - step 1943' if isinstance(e, AssertionError) else f'ERROR - step 1943: {e}')

print("STEP 1944 - Check element h3#None.['ac-gf-directory-column-section-title']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-title']")))
    print('PASS - step 1944')
except Exception as e:
    print('FAIL - step 1944' if isinstance(e, AssertionError) else f'ERROR - step 1944: {e}')

print("STEP 1945 - Check element span#None.['ac-gf-directory-column-section-title-text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-title-text']")))
    print('PASS - step 1945')
except Exception as e:
    print('FAIL - step 1945' if isinstance(e, AssertionError) else f'ERROR - step 1945: {e}')

print("STEP 1946 - Check element button#None.['ac-gf-directory-column-section-title-button']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-title-button']")))
    print('PASS - step 1946')
except Exception as e:
    print('FAIL - step 1946' if isinstance(e, AssertionError) else f'ERROR - step 1946: {e}')

print("STEP 1947 - Check element span#None.['ac-gf-directory-column-section-title-text']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-title-text']")))
    print('PASS - step 1947')
except Exception as e:
    print('FAIL - step 1947' if isinstance(e, AssertionError) else f'ERROR - step 1947: {e}')

print("STEP 1948 - Check element span#None.['ac-gf-directory-column-section-title-icon']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-title-icon']")))
    print('PASS - step 1948')
except Exception as e:
    print('FAIL - step 1948' if isinstance(e, AssertionError) else f'ERROR - step 1948: {e}')

print("STEP 1949 - Check element svg#None.['footer-icon-svg']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['footer-icon-svg']")))
    print('PASS - step 1949')
except Exception as e:
    print('FAIL - step 1949' if isinstance(e, AssertionError) else f'ERROR - step 1949: {e}')

print("STEP 1950 - Check element polyline#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "polyline")))
    print('PASS - step 1950')
except Exception as e:
    print('FAIL - step 1950' if isinstance(e, AssertionError) else f'ERROR - step 1950: {e}')

print("STEP 1951 - Check element animate#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "animate")))
    print('PASS - step 1951')
except Exception as e:
    print('FAIL - step 1951' if isinstance(e, AssertionError) else f'ERROR - step 1951: {e}')

print("STEP 1952 - Check element animate#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "animate")))
    print('PASS - step 1952')
except Exception as e:
    print('FAIL - step 1952' if isinstance(e, AssertionError) else f'ERROR - step 1952: {e}')

print("STEP 1953 - Check element ul#footer-directory-column-section-about.['ac-gf-directory-column-section-list']")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "footer-directory-column-section-about")))
    print('PASS - step 1953')
except Exception as e:
    print('FAIL - step 1953' if isinstance(e, AssertionError) else f'ERROR - step 1953: {e}')

print("STEP 1954 - Check element li#None.['ac-gf-directory-column-section-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-item']")))
    print('PASS - step 1954')
except Exception as e:
    print('FAIL - step 1954' if isinstance(e, AssertionError) else f'ERROR - step 1954: {e}')

print("STEP 1955 - Check element a#None.['ac-gf-directory-column-section-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-link']")))
    print('PASS - step 1955')
except Exception as e:
    print('FAIL - step 1955' if isinstance(e, AssertionError) else f'ERROR - step 1955: {e}')

print("STEP 1956 - Check element li#None.['ac-gf-directory-column-section-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-item']")))
    print('PASS - step 1956')
except Exception as e:
    print('FAIL - step 1956' if isinstance(e, AssertionError) else f'ERROR - step 1956: {e}')

print("STEP 1957 - Check element a#None.['ac-gf-directory-column-section-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-link']")))
    print('PASS - step 1957')
except Exception as e:
    print('FAIL - step 1957' if isinstance(e, AssertionError) else f'ERROR - step 1957: {e}')

print("STEP 1958 - Check element li#None.['ac-gf-directory-column-section-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-item']")))
    print('PASS - step 1958')
except Exception as e:
    print('FAIL - step 1958' if isinstance(e, AssertionError) else f'ERROR - step 1958: {e}')

print("STEP 1959 - Check element a#None.['ac-gf-directory-column-section-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-link']")))
    print('PASS - step 1959')
except Exception as e:
    print('FAIL - step 1959' if isinstance(e, AssertionError) else f'ERROR - step 1959: {e}')

print("STEP 1960 - Check element li#None.['ac-gf-directory-column-section-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-item']")))
    print('PASS - step 1960')
except Exception as e:
    print('FAIL - step 1960' if isinstance(e, AssertionError) else f'ERROR - step 1960: {e}')

print("STEP 1961 - Check element a#None.['ac-gf-directory-column-section-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-link']")))
    print('PASS - step 1961')
except Exception as e:
    print('FAIL - step 1961' if isinstance(e, AssertionError) else f'ERROR - step 1961: {e}')

print("STEP 1962 - Check element li#None.['ac-gf-directory-column-section-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-item']")))
    print('PASS - step 1962')
except Exception as e:
    print('FAIL - step 1962' if isinstance(e, AssertionError) else f'ERROR - step 1962: {e}')

print("STEP 1963 - Check element a#None.['ac-gf-directory-column-section-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-link']")))
    print('PASS - step 1963')
except Exception as e:
    print('FAIL - step 1963' if isinstance(e, AssertionError) else f'ERROR - step 1963: {e}')

print("STEP 1964 - Check element li#None.['ac-gf-directory-column-section-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-item']")))
    print('PASS - step 1964')
except Exception as e:
    print('FAIL - step 1964' if isinstance(e, AssertionError) else f'ERROR - step 1964: {e}')

print("STEP 1965 - Check element a#None.['ac-gf-directory-column-section-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-link']")))
    print('PASS - step 1965')
except Exception as e:
    print('FAIL - step 1965' if isinstance(e, AssertionError) else f'ERROR - step 1965: {e}')

print("STEP 1966 - Check element li#None.['ac-gf-directory-column-section-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-item']")))
    print('PASS - step 1966')
except Exception as e:
    print('FAIL - step 1966' if isinstance(e, AssertionError) else f'ERROR - step 1966: {e}')

print("STEP 1967 - Check element a#None.['ac-gf-directory-column-section-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-directory-column-section-link']")))
    print('PASS - step 1967')
except Exception as e:
    print('FAIL - step 1967' if isinstance(e, AssertionError) else f'ERROR - step 1967: {e}')

print("STEP 1968 - Check element section#None.['ac-gf-footer']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-footer']")))
    print('PASS - step 1968')
except Exception as e:
    print('FAIL - step 1968' if isinstance(e, AssertionError) else f'ERROR - step 1968: {e}')

print("STEP 1969 - Check element div#None.['ac-gf-footer-shop']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-footer-shop']")))
    print('PASS - step 1969')
except Exception as e:
    print('FAIL - step 1969' if isinstance(e, AssertionError) else f'ERROR - step 1969: {e}')

print("STEP 1970 - Check element a#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "a")))
    print('PASS - step 1970')
except Exception as e:
    print('FAIL - step 1970' if isinstance(e, AssertionError) else f'ERROR - step 1970: {e}')

print("STEP 1971 - Check element a#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "a")))
    print('PASS - step 1971')
except Exception as e:
    print('FAIL - step 1971' if isinstance(e, AssertionError) else f'ERROR - step 1971: {e}')

print("STEP 1972 - Check element span#None.['nowrap']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['nowrap']")))
    print('PASS - step 1972')
except Exception as e:
    print('FAIL - step 1972' if isinstance(e, AssertionError) else f'ERROR - step 1972: {e}')

print("STEP 1973 - Check element a#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "a")))
    print('PASS - step 1973')
except Exception as e:
    print('FAIL - step 1973' if isinstance(e, AssertionError) else f'ERROR - step 1973: {e}')

print("STEP 1974 - Check element div#None.['ac-gf-footer-locale']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-footer-locale']")))
    print('PASS - step 1974')
except Exception as e:
    print('FAIL - step 1974' if isinstance(e, AssertionError) else f'ERROR - step 1974: {e}')

print("STEP 1975 - Check element a#None.['ac-gf-footer-locale-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-footer-locale-link']")))
    print('PASS - step 1975')
except Exception as e:
    print('FAIL - step 1975' if isinstance(e, AssertionError) else f'ERROR - step 1975: {e}')

print("STEP 1976 - Check element div#None.['ac-gf-footer-legal']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-footer-legal']")))
    print('PASS - step 1976')
except Exception as e:
    print('FAIL - step 1976' if isinstance(e, AssertionError) else f'ERROR - step 1976: {e}')

print("STEP 1977 - Check element div#None.['ac-gf-footer-legal-copyright']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-footer-legal-copyright']")))
    print('PASS - step 1977')
except Exception as e:
    print('FAIL - step 1977' if isinstance(e, AssertionError) else f'ERROR - step 1977: {e}')

print("STEP 1978 - Check element ul#None.['ac-gf-footer-legal-links']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-footer-legal-links']")))
    print('PASS - step 1978')
except Exception as e:
    print('FAIL - step 1978' if isinstance(e, AssertionError) else f'ERROR - step 1978: {e}')

print("STEP 1979 - Check element li#None.['ac-gf-footer-legal-links-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-footer-legal-links-item']")))
    print('PASS - step 1979')
except Exception as e:
    print('FAIL - step 1979' if isinstance(e, AssertionError) else f'ERROR - step 1979: {e}')

print("STEP 1980 - Check element a#None.['ac-gf-footer-legal-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-footer-legal-link']")))
    print('PASS - step 1980')
except Exception as e:
    print('FAIL - step 1980' if isinstance(e, AssertionError) else f'ERROR - step 1980: {e}')

print("STEP 1981 - Check element li#None.['ac-gf-footer-legal-links-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-footer-legal-links-item']")))
    print('PASS - step 1981')
except Exception as e:
    print('FAIL - step 1981' if isinstance(e, AssertionError) else f'ERROR - step 1981: {e}')

print("STEP 1982 - Check element a#None.['ac-gf-footer-legal-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-footer-legal-link']")))
    print('PASS - step 1982')
except Exception as e:
    print('FAIL - step 1982' if isinstance(e, AssertionError) else f'ERROR - step 1982: {e}')

print("STEP 1983 - Check element li#None.['ac-gf-footer-legal-links-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-footer-legal-links-item']")))
    print('PASS - step 1983')
except Exception as e:
    print('FAIL - step 1983' if isinstance(e, AssertionError) else f'ERROR - step 1983: {e}')

print("STEP 1984 - Check element a#None.['ac-gf-footer-legal-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-footer-legal-link']")))
    print('PASS - step 1984')
except Exception as e:
    print('FAIL - step 1984' if isinstance(e, AssertionError) else f'ERROR - step 1984: {e}')

print("STEP 1985 - Check element li#None.['ac-gf-footer-legal-links-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-footer-legal-links-item']")))
    print('PASS - step 1985')
except Exception as e:
    print('FAIL - step 1985' if isinstance(e, AssertionError) else f'ERROR - step 1985: {e}')

print("STEP 1986 - Check element a#None.['ac-gf-footer-legal-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-footer-legal-link']")))
    print('PASS - step 1986')
except Exception as e:
    print('FAIL - step 1986' if isinstance(e, AssertionError) else f'ERROR - step 1986: {e}')

print("STEP 1987 - Check element li#None.['ac-gf-footer-legal-links-item']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-footer-legal-links-item']")))
    print('PASS - step 1987')
except Exception as e:
    print('FAIL - step 1987' if isinstance(e, AssertionError) else f'ERROR - step 1987: {e}')

print("STEP 1988 - Check element a#None.['ac-gf-footer-legal-link']")
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "['ac-gf-footer-legal-link']")))
    print('PASS - step 1988')
except Exception as e:
    print('FAIL - step 1988' if isinstance(e, AssertionError) else f'ERROR - step 1988: {e}')

print("STEP 1989 - Check element script#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "script")))
    print('PASS - step 1989')
except Exception as e:
    print('FAIL - step 1989' if isinstance(e, AssertionError) else f'ERROR - step 1989: {e}')

print("STEP 1990 - Check element script#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "script")))
    print('PASS - step 1990')
except Exception as e:
    print('FAIL - step 1990' if isinstance(e, AssertionError) else f'ERROR - step 1990: {e}')

print("STEP 1991 - Check element script#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "script")))
    print('PASS - step 1991')
except Exception as e:
    print('FAIL - step 1991' if isinstance(e, AssertionError) else f'ERROR - step 1991: {e}')

print("STEP 1992 - Check element script#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "script")))
    print('PASS - step 1992')
except Exception as e:
    print('FAIL - step 1992' if isinstance(e, AssertionError) else f'ERROR - step 1992: {e}')

print("STEP 1993 - Check element script#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "script")))
    print('PASS - step 1993')
except Exception as e:
    print('FAIL - step 1993' if isinstance(e, AssertionError) else f'ERROR - step 1993: {e}')

print("STEP 1994 - Check element script#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "script")))
    print('PASS - step 1994')
except Exception as e:
    print('FAIL - step 1994' if isinstance(e, AssertionError) else f'ERROR - step 1994: {e}')

print("STEP 1995 - Check element span#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "span")))
    print('PASS - step 1995')
except Exception as e:
    print('FAIL - step 1995' if isinstance(e, AssertionError) else f'ERROR - step 1995: {e}')

print("STEP 1996 - Check element iframe#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
    print('PASS - step 1996')
except Exception as e:
    print('FAIL - step 1996' if isinstance(e, AssertionError) else f'ERROR - step 1996: {e}')

print("STEP 1997 - Check element div#viewport-emitter.None")
try:
    element = wait.until(EC.presence_of_element_located((By.ID, "viewport-emitter")))
    print('PASS - step 1997')
except Exception as e:
    print('FAIL - step 1997' if isinstance(e, AssertionError) else f'ERROR - step 1997: {e}')

print("STEP 1998 - Check element script#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "script")))
    print('PASS - step 1998')
except Exception as e:
    print('FAIL - step 1998' if isinstance(e, AssertionError) else f'ERROR - step 1998: {e}')

print("STEP 1999 - Check element script#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "script")))
    print('PASS - step 1999')
except Exception as e:
    print('FAIL - step 1999' if isinstance(e, AssertionError) else f'ERROR - step 1999: {e}')

print("STEP 2000 - Check element link#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "link")))
    print('PASS - step 2000')
except Exception as e:
    print('FAIL - step 2000' if isinstance(e, AssertionError) else f'ERROR - step 2000: {e}')

print("STEP 2001 - Check element script#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "script")))
    print('PASS - step 2001')
except Exception as e:
    print('FAIL - step 2001' if isinstance(e, AssertionError) else f'ERROR - step 2001: {e}')

print("STEP 2002 - Check element script#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "script")))
    print('PASS - step 2002')
except Exception as e:
    print('FAIL - step 2002' if isinstance(e, AssertionError) else f'ERROR - step 2002: {e}')

print("STEP 2003 - Check element script#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "script")))
    print('PASS - step 2003')
except Exception as e:
    print('FAIL - step 2003' if isinstance(e, AssertionError) else f'ERROR - step 2003: {e}')

print("STEP 2004 - Check element div#None.None")
try:
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "div")))
    print('PASS - step 2004')
except Exception as e:
    print('FAIL - step 2004' if isinstance(e, AssertionError) else f'ERROR - step 2004: {e}')

driver.quit()