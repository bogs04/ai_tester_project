from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://quotes.toscrape.com")
time.sleep(1)  # simple wait

print("STEP 1 - Check element html_1")
try:
    element = driver.find_element(By.TAG_NAME, "html")
    print('PASS - step 1')
except Exception as e:
    print('FAIL - step 1' if isinstance(e, AssertionError) else f'ERROR - step 1: {e}')

print("STEP 2 - Check element head_2")
try:
    element = driver.find_element(By.TAG_NAME, "head")
    print('PASS - step 2')
except Exception as e:
    print('FAIL - step 2' if isinstance(e, AssertionError) else f'ERROR - step 2: {e}')

print("STEP 3 - Check element meta_3")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 3')
except Exception as e:
    print('FAIL - step 3' if isinstance(e, AssertionError) else f'ERROR - step 3: {e}')

print("STEP 4 - Check element title_4")
try:
    element = driver.find_element(By.TAG_NAME, "title")
    print('PASS - step 4')
except Exception as e:
    print('FAIL - step 4' if isinstance(e, AssertionError) else f'ERROR - step 4: {e}')

print("STEP 5 - Check element link_5")
try:
    element = driver.find_element(By.TAG_NAME, "link")
    print('PASS - step 5')
except Exception as e:
    print('FAIL - step 5' if isinstance(e, AssertionError) else f'ERROR - step 5: {e}')

print("STEP 6 - Check element link_6")
try:
    element = driver.find_element(By.TAG_NAME, "link")
    print('PASS - step 6')
except Exception as e:
    print('FAIL - step 6' if isinstance(e, AssertionError) else f'ERROR - step 6: {e}')

print("STEP 7 - Check element body_7")
try:
    element = driver.find_element(By.TAG_NAME, "body")
    print('PASS - step 7')
except Exception as e:
    print('FAIL - step 7' if isinstance(e, AssertionError) else f'ERROR - step 7: {e}')

print("STEP 8 - Check element div_8")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 8')
except Exception as e:
    print('FAIL - step 8' if isinstance(e, AssertionError) else f'ERROR - step 8: {e}')

print("STEP 9 - Check element div_9")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 9')
except Exception as e:
    print('FAIL - step 9' if isinstance(e, AssertionError) else f'ERROR - step 9: {e}')

print("STEP 10 - Check element div_10")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 10')
except Exception as e:
    print('FAIL - step 10' if isinstance(e, AssertionError) else f'ERROR - step 10: {e}')

print("STEP 11 - Check element h1_11")
try:
    element = driver.find_element(By.TAG_NAME, "h1")
    print('PASS - step 11')
except Exception as e:
    print('FAIL - step 11' if isinstance(e, AssertionError) else f'ERROR - step 11: {e}')

print("STEP 12 - Check element a_12")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 12')
except Exception as e:
    print('FAIL - step 12' if isinstance(e, AssertionError) else f'ERROR - step 12: {e}')

print("STEP 13 - Check element div_13")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 13')
except Exception as e:
    print('FAIL - step 13' if isinstance(e, AssertionError) else f'ERROR - step 13: {e}')

print("STEP 14 - Check element p_14")
try:
    element = driver.find_element(By.TAG_NAME, "p")
    print('PASS - step 14')
except Exception as e:
    print('FAIL - step 14' if isinstance(e, AssertionError) else f'ERROR - step 14: {e}')

print("STEP 15 - Check element a_15")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 15')
except Exception as e:
    print('FAIL - step 15' if isinstance(e, AssertionError) else f'ERROR - step 15: {e}')

print("STEP 16 - Check element div_16")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 16')
except Exception as e:
    print('FAIL - step 16' if isinstance(e, AssertionError) else f'ERROR - step 16: {e}')

print("STEP 17 - Check element div_17")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 17')
except Exception as e:
    print('FAIL - step 17' if isinstance(e, AssertionError) else f'ERROR - step 17: {e}')

print("STEP 18 - Check element div_18")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 18')
except Exception as e:
    print('FAIL - step 18' if isinstance(e, AssertionError) else f'ERROR - step 18: {e}')

print("STEP 19 - Check element span_19")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 19')
except Exception as e:
    print('FAIL - step 19' if isinstance(e, AssertionError) else f'ERROR - step 19: {e}')

print("STEP 20 - Check element span_20")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 20')
except Exception as e:
    print('FAIL - step 20' if isinstance(e, AssertionError) else f'ERROR - step 20: {e}')

print("STEP 21 - Check element small_21")
try:
    element = driver.find_element(By.TAG_NAME, "small")
    print('PASS - step 21')
except Exception as e:
    print('FAIL - step 21' if isinstance(e, AssertionError) else f'ERROR - step 21: {e}')

print("STEP 22 - Check element a_22")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 22')
except Exception as e:
    print('FAIL - step 22' if isinstance(e, AssertionError) else f'ERROR - step 22: {e}')

print("STEP 23 - Check element div_23")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 23')
except Exception as e:
    print('FAIL - step 23' if isinstance(e, AssertionError) else f'ERROR - step 23: {e}')

print("STEP 24 - Check element meta_24")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 24')
except Exception as e:
    print('FAIL - step 24' if isinstance(e, AssertionError) else f'ERROR - step 24: {e}')

print("STEP 25 - Check element a_25")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 25')
except Exception as e:
    print('FAIL - step 25' if isinstance(e, AssertionError) else f'ERROR - step 25: {e}')

print("STEP 26 - Check element a_26")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 26')
except Exception as e:
    print('FAIL - step 26' if isinstance(e, AssertionError) else f'ERROR - step 26: {e}')

print("STEP 27 - Check element a_27")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 27')
except Exception as e:
    print('FAIL - step 27' if isinstance(e, AssertionError) else f'ERROR - step 27: {e}')

print("STEP 28 - Check element a_28")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 28')
except Exception as e:
    print('FAIL - step 28' if isinstance(e, AssertionError) else f'ERROR - step 28: {e}')

print("STEP 29 - Check element div_29")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 29')
except Exception as e:
    print('FAIL - step 29' if isinstance(e, AssertionError) else f'ERROR - step 29: {e}')

print("STEP 30 - Check element span_30")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 30')
except Exception as e:
    print('FAIL - step 30' if isinstance(e, AssertionError) else f'ERROR - step 30: {e}')

print("STEP 31 - Check element span_31")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 31')
except Exception as e:
    print('FAIL - step 31' if isinstance(e, AssertionError) else f'ERROR - step 31: {e}')

print("STEP 32 - Check element small_32")
try:
    element = driver.find_element(By.TAG_NAME, "small")
    print('PASS - step 32')
except Exception as e:
    print('FAIL - step 32' if isinstance(e, AssertionError) else f'ERROR - step 32: {e}')

print("STEP 33 - Check element a_33")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 33')
except Exception as e:
    print('FAIL - step 33' if isinstance(e, AssertionError) else f'ERROR - step 33: {e}')

print("STEP 34 - Check element div_34")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 34')
except Exception as e:
    print('FAIL - step 34' if isinstance(e, AssertionError) else f'ERROR - step 34: {e}')

print("STEP 35 - Check element meta_35")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 35')
except Exception as e:
    print('FAIL - step 35' if isinstance(e, AssertionError) else f'ERROR - step 35: {e}')

print("STEP 36 - Check element a_36")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 36')
except Exception as e:
    print('FAIL - step 36' if isinstance(e, AssertionError) else f'ERROR - step 36: {e}')

print("STEP 37 - Check element a_37")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 37')
except Exception as e:
    print('FAIL - step 37' if isinstance(e, AssertionError) else f'ERROR - step 37: {e}')

print("STEP 38 - Check element div_38")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 38')
except Exception as e:
    print('FAIL - step 38' if isinstance(e, AssertionError) else f'ERROR - step 38: {e}')

print("STEP 39 - Check element span_39")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 39')
except Exception as e:
    print('FAIL - step 39' if isinstance(e, AssertionError) else f'ERROR - step 39: {e}')

print("STEP 40 - Check element span_40")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 40')
except Exception as e:
    print('FAIL - step 40' if isinstance(e, AssertionError) else f'ERROR - step 40: {e}')

print("STEP 41 - Check element small_41")
try:
    element = driver.find_element(By.TAG_NAME, "small")
    print('PASS - step 41')
except Exception as e:
    print('FAIL - step 41' if isinstance(e, AssertionError) else f'ERROR - step 41: {e}')

print("STEP 42 - Check element a_42")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 42')
except Exception as e:
    print('FAIL - step 42' if isinstance(e, AssertionError) else f'ERROR - step 42: {e}')

print("STEP 43 - Check element div_43")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 43')
except Exception as e:
    print('FAIL - step 43' if isinstance(e, AssertionError) else f'ERROR - step 43: {e}')

print("STEP 44 - Check element meta_44")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 44')
except Exception as e:
    print('FAIL - step 44' if isinstance(e, AssertionError) else f'ERROR - step 44: {e}')

print("STEP 45 - Check element a_45")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 45')
except Exception as e:
    print('FAIL - step 45' if isinstance(e, AssertionError) else f'ERROR - step 45: {e}')

print("STEP 46 - Check element a_46")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 46')
except Exception as e:
    print('FAIL - step 46' if isinstance(e, AssertionError) else f'ERROR - step 46: {e}')

print("STEP 47 - Check element a_47")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 47')
except Exception as e:
    print('FAIL - step 47' if isinstance(e, AssertionError) else f'ERROR - step 47: {e}')

print("STEP 48 - Check element a_48")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 48')
except Exception as e:
    print('FAIL - step 48' if isinstance(e, AssertionError) else f'ERROR - step 48: {e}')

print("STEP 49 - Check element a_49")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 49')
except Exception as e:
    print('FAIL - step 49' if isinstance(e, AssertionError) else f'ERROR - step 49: {e}')

print("STEP 50 - Check element div_50")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 50')
except Exception as e:
    print('FAIL - step 50' if isinstance(e, AssertionError) else f'ERROR - step 50: {e}')

print("STEP 51 - Check element span_51")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 51')
except Exception as e:
    print('FAIL - step 51' if isinstance(e, AssertionError) else f'ERROR - step 51: {e}')

print("STEP 52 - Check element span_52")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 52')
except Exception as e:
    print('FAIL - step 52' if isinstance(e, AssertionError) else f'ERROR - step 52: {e}')

print("STEP 53 - Check element small_53")
try:
    element = driver.find_element(By.TAG_NAME, "small")
    print('PASS - step 53')
except Exception as e:
    print('FAIL - step 53' if isinstance(e, AssertionError) else f'ERROR - step 53: {e}')

print("STEP 54 - Check element a_54")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 54')
except Exception as e:
    print('FAIL - step 54' if isinstance(e, AssertionError) else f'ERROR - step 54: {e}')

print("STEP 55 - Check element div_55")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 55')
except Exception as e:
    print('FAIL - step 55' if isinstance(e, AssertionError) else f'ERROR - step 55: {e}')

print("STEP 56 - Check element meta_56")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 56')
except Exception as e:
    print('FAIL - step 56' if isinstance(e, AssertionError) else f'ERROR - step 56: {e}')

print("STEP 57 - Check element a_57")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 57')
except Exception as e:
    print('FAIL - step 57' if isinstance(e, AssertionError) else f'ERROR - step 57: {e}')

print("STEP 58 - Check element a_58")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 58')
except Exception as e:
    print('FAIL - step 58' if isinstance(e, AssertionError) else f'ERROR - step 58: {e}')

print("STEP 59 - Check element a_59")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 59')
except Exception as e:
    print('FAIL - step 59' if isinstance(e, AssertionError) else f'ERROR - step 59: {e}')

print("STEP 60 - Check element a_60")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 60')
except Exception as e:
    print('FAIL - step 60' if isinstance(e, AssertionError) else f'ERROR - step 60: {e}')

print("STEP 61 - Check element div_61")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 61')
except Exception as e:
    print('FAIL - step 61' if isinstance(e, AssertionError) else f'ERROR - step 61: {e}')

print("STEP 62 - Check element span_62")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 62')
except Exception as e:
    print('FAIL - step 62' if isinstance(e, AssertionError) else f'ERROR - step 62: {e}')

print("STEP 63 - Check element span_63")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 63')
except Exception as e:
    print('FAIL - step 63' if isinstance(e, AssertionError) else f'ERROR - step 63: {e}')

print("STEP 64 - Check element small_64")
try:
    element = driver.find_element(By.TAG_NAME, "small")
    print('PASS - step 64')
except Exception as e:
    print('FAIL - step 64' if isinstance(e, AssertionError) else f'ERROR - step 64: {e}')

print("STEP 65 - Check element a_65")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 65')
except Exception as e:
    print('FAIL - step 65' if isinstance(e, AssertionError) else f'ERROR - step 65: {e}')

print("STEP 66 - Check element div_66")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 66')
except Exception as e:
    print('FAIL - step 66' if isinstance(e, AssertionError) else f'ERROR - step 66: {e}')

print("STEP 67 - Check element meta_67")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 67')
except Exception as e:
    print('FAIL - step 67' if isinstance(e, AssertionError) else f'ERROR - step 67: {e}')

print("STEP 68 - Check element a_68")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 68')
except Exception as e:
    print('FAIL - step 68' if isinstance(e, AssertionError) else f'ERROR - step 68: {e}')

print("STEP 69 - Check element a_69")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 69')
except Exception as e:
    print('FAIL - step 69' if isinstance(e, AssertionError) else f'ERROR - step 69: {e}')

print("STEP 70 - Check element div_70")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 70')
except Exception as e:
    print('FAIL - step 70' if isinstance(e, AssertionError) else f'ERROR - step 70: {e}')

print("STEP 71 - Check element span_71")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 71')
except Exception as e:
    print('FAIL - step 71' if isinstance(e, AssertionError) else f'ERROR - step 71: {e}')

print("STEP 72 - Check element span_72")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 72')
except Exception as e:
    print('FAIL - step 72' if isinstance(e, AssertionError) else f'ERROR - step 72: {e}')

print("STEP 73 - Check element small_73")
try:
    element = driver.find_element(By.TAG_NAME, "small")
    print('PASS - step 73')
except Exception as e:
    print('FAIL - step 73' if isinstance(e, AssertionError) else f'ERROR - step 73: {e}')

print("STEP 74 - Check element a_74")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 74')
except Exception as e:
    print('FAIL - step 74' if isinstance(e, AssertionError) else f'ERROR - step 74: {e}')

print("STEP 75 - Check element div_75")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 75')
except Exception as e:
    print('FAIL - step 75' if isinstance(e, AssertionError) else f'ERROR - step 75: {e}')

print("STEP 76 - Check element meta_76")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 76')
except Exception as e:
    print('FAIL - step 76' if isinstance(e, AssertionError) else f'ERROR - step 76: {e}')

print("STEP 77 - Check element a_77")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 77')
except Exception as e:
    print('FAIL - step 77' if isinstance(e, AssertionError) else f'ERROR - step 77: {e}')

print("STEP 78 - Check element a_78")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 78')
except Exception as e:
    print('FAIL - step 78' if isinstance(e, AssertionError) else f'ERROR - step 78: {e}')

print("STEP 79 - Check element a_79")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 79')
except Exception as e:
    print('FAIL - step 79' if isinstance(e, AssertionError) else f'ERROR - step 79: {e}')

print("STEP 80 - Check element div_80")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 80')
except Exception as e:
    print('FAIL - step 80' if isinstance(e, AssertionError) else f'ERROR - step 80: {e}')

print("STEP 81 - Check element span_81")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 81')
except Exception as e:
    print('FAIL - step 81' if isinstance(e, AssertionError) else f'ERROR - step 81: {e}')

print("STEP 82 - Check element span_82")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 82')
except Exception as e:
    print('FAIL - step 82' if isinstance(e, AssertionError) else f'ERROR - step 82: {e}')

print("STEP 83 - Check element small_83")
try:
    element = driver.find_element(By.TAG_NAME, "small")
    print('PASS - step 83')
except Exception as e:
    print('FAIL - step 83' if isinstance(e, AssertionError) else f'ERROR - step 83: {e}')

print("STEP 84 - Check element a_84")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 84')
except Exception as e:
    print('FAIL - step 84' if isinstance(e, AssertionError) else f'ERROR - step 84: {e}')

print("STEP 85 - Check element div_85")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 85')
except Exception as e:
    print('FAIL - step 85' if isinstance(e, AssertionError) else f'ERROR - step 85: {e}')

print("STEP 86 - Check element meta_86")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 86')
except Exception as e:
    print('FAIL - step 86' if isinstance(e, AssertionError) else f'ERROR - step 86: {e}')

print("STEP 87 - Check element a_87")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 87')
except Exception as e:
    print('FAIL - step 87' if isinstance(e, AssertionError) else f'ERROR - step 87: {e}')

print("STEP 88 - Check element a_88")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 88')
except Exception as e:
    print('FAIL - step 88' if isinstance(e, AssertionError) else f'ERROR - step 88: {e}')

print("STEP 89 - Check element div_89")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 89')
except Exception as e:
    print('FAIL - step 89' if isinstance(e, AssertionError) else f'ERROR - step 89: {e}')

print("STEP 90 - Check element span_90")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 90')
except Exception as e:
    print('FAIL - step 90' if isinstance(e, AssertionError) else f'ERROR - step 90: {e}')

print("STEP 91 - Check element span_91")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 91')
except Exception as e:
    print('FAIL - step 91' if isinstance(e, AssertionError) else f'ERROR - step 91: {e}')

print("STEP 92 - Check element small_92")
try:
    element = driver.find_element(By.TAG_NAME, "small")
    print('PASS - step 92')
except Exception as e:
    print('FAIL - step 92' if isinstance(e, AssertionError) else f'ERROR - step 92: {e}')

print("STEP 93 - Check element a_93")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 93')
except Exception as e:
    print('FAIL - step 93' if isinstance(e, AssertionError) else f'ERROR - step 93: {e}')

print("STEP 94 - Check element div_94")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 94')
except Exception as e:
    print('FAIL - step 94' if isinstance(e, AssertionError) else f'ERROR - step 94: {e}')

print("STEP 95 - Check element meta_95")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 95')
except Exception as e:
    print('FAIL - step 95' if isinstance(e, AssertionError) else f'ERROR - step 95: {e}')

print("STEP 96 - Check element a_96")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 96')
except Exception as e:
    print('FAIL - step 96' if isinstance(e, AssertionError) else f'ERROR - step 96: {e}')

print("STEP 97 - Check element a_97")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 97')
except Exception as e:
    print('FAIL - step 97' if isinstance(e, AssertionError) else f'ERROR - step 97: {e}')

print("STEP 98 - Check element a_98")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 98')
except Exception as e:
    print('FAIL - step 98' if isinstance(e, AssertionError) else f'ERROR - step 98: {e}')

print("STEP 99 - Check element a_99")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 99')
except Exception as e:
    print('FAIL - step 99' if isinstance(e, AssertionError) else f'ERROR - step 99: {e}')

print("STEP 100 - Check element div_100")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 100')
except Exception as e:
    print('FAIL - step 100' if isinstance(e, AssertionError) else f'ERROR - step 100: {e}')

print("STEP 101 - Check element span_101")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 101')
except Exception as e:
    print('FAIL - step 101' if isinstance(e, AssertionError) else f'ERROR - step 101: {e}')

print("STEP 102 - Check element span_102")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 102')
except Exception as e:
    print('FAIL - step 102' if isinstance(e, AssertionError) else f'ERROR - step 102: {e}')

print("STEP 103 - Check element small_103")
try:
    element = driver.find_element(By.TAG_NAME, "small")
    print('PASS - step 103')
except Exception as e:
    print('FAIL - step 103' if isinstance(e, AssertionError) else f'ERROR - step 103: {e}')

print("STEP 104 - Check element a_104")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 104')
except Exception as e:
    print('FAIL - step 104' if isinstance(e, AssertionError) else f'ERROR - step 104: {e}')

print("STEP 105 - Check element div_105")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 105')
except Exception as e:
    print('FAIL - step 105' if isinstance(e, AssertionError) else f'ERROR - step 105: {e}')

print("STEP 106 - Check element meta_106")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 106')
except Exception as e:
    print('FAIL - step 106' if isinstance(e, AssertionError) else f'ERROR - step 106: {e}')

print("STEP 107 - Check element a_107")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 107')
except Exception as e:
    print('FAIL - step 107' if isinstance(e, AssertionError) else f'ERROR - step 107: {e}')

print("STEP 108 - Check element div_108")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 108')
except Exception as e:
    print('FAIL - step 108' if isinstance(e, AssertionError) else f'ERROR - step 108: {e}')

print("STEP 109 - Check element span_109")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 109')
except Exception as e:
    print('FAIL - step 109' if isinstance(e, AssertionError) else f'ERROR - step 109: {e}')

print("STEP 110 - Check element span_110")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 110')
except Exception as e:
    print('FAIL - step 110' if isinstance(e, AssertionError) else f'ERROR - step 110: {e}')

print("STEP 111 - Check element small_111")
try:
    element = driver.find_element(By.TAG_NAME, "small")
    print('PASS - step 111')
except Exception as e:
    print('FAIL - step 111' if isinstance(e, AssertionError) else f'ERROR - step 111: {e}')

print("STEP 112 - Check element a_112")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 112')
except Exception as e:
    print('FAIL - step 112' if isinstance(e, AssertionError) else f'ERROR - step 112: {e}')

print("STEP 113 - Check element div_113")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 113')
except Exception as e:
    print('FAIL - step 113' if isinstance(e, AssertionError) else f'ERROR - step 113: {e}')

print("STEP 114 - Check element meta_114")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 114')
except Exception as e:
    print('FAIL - step 114' if isinstance(e, AssertionError) else f'ERROR - step 114: {e}')

print("STEP 115 - Check element a_115")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 115')
except Exception as e:
    print('FAIL - step 115' if isinstance(e, AssertionError) else f'ERROR - step 115: {e}')

print("STEP 116 - Check element a_116")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 116')
except Exception as e:
    print('FAIL - step 116' if isinstance(e, AssertionError) else f'ERROR - step 116: {e}')

print("STEP 117 - Check element a_117")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 117')
except Exception as e:
    print('FAIL - step 117' if isinstance(e, AssertionError) else f'ERROR - step 117: {e}')

print("STEP 118 - Check element nav_118")
try:
    element = driver.find_element(By.TAG_NAME, "nav")
    print('PASS - step 118')
except Exception as e:
    print('FAIL - step 118' if isinstance(e, AssertionError) else f'ERROR - step 118: {e}')

print("STEP 119 - Check element ul_119")
try:
    element = driver.find_element(By.TAG_NAME, "ul")
    print('PASS - step 119')
except Exception as e:
    print('FAIL - step 119' if isinstance(e, AssertionError) else f'ERROR - step 119: {e}')

print("STEP 120 - Check element li_120")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 120')
except Exception as e:
    print('FAIL - step 120' if isinstance(e, AssertionError) else f'ERROR - step 120: {e}')

print("STEP 121 - Check element a_121")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 121')
except Exception as e:
    print('FAIL - step 121' if isinstance(e, AssertionError) else f'ERROR - step 121: {e}')

print("STEP 122 - Check element span_122")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 122')
except Exception as e:
    print('FAIL - step 122' if isinstance(e, AssertionError) else f'ERROR - step 122: {e}')

print("STEP 123 - Check element div_123")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 123')
except Exception as e:
    print('FAIL - step 123' if isinstance(e, AssertionError) else f'ERROR - step 123: {e}')

print("STEP 124 - Check element h2_124")
try:
    element = driver.find_element(By.TAG_NAME, "h2")
    print('PASS - step 124')
except Exception as e:
    print('FAIL - step 124' if isinstance(e, AssertionError) else f'ERROR - step 124: {e}')

print("STEP 125 - Check element span_125")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 125')
except Exception as e:
    print('FAIL - step 125' if isinstance(e, AssertionError) else f'ERROR - step 125: {e}')

print("STEP 126 - Check element a_126")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 126')
except Exception as e:
    print('FAIL - step 126' if isinstance(e, AssertionError) else f'ERROR - step 126: {e}')

print("STEP 127 - Check element span_127")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 127')
except Exception as e:
    print('FAIL - step 127' if isinstance(e, AssertionError) else f'ERROR - step 127: {e}')

print("STEP 128 - Check element a_128")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 128')
except Exception as e:
    print('FAIL - step 128' if isinstance(e, AssertionError) else f'ERROR - step 128: {e}')

print("STEP 129 - Check element span_129")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 129')
except Exception as e:
    print('FAIL - step 129' if isinstance(e, AssertionError) else f'ERROR - step 129: {e}')

print("STEP 130 - Check element a_130")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 130')
except Exception as e:
    print('FAIL - step 130' if isinstance(e, AssertionError) else f'ERROR - step 130: {e}')

print("STEP 131 - Check element span_131")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 131')
except Exception as e:
    print('FAIL - step 131' if isinstance(e, AssertionError) else f'ERROR - step 131: {e}')

print("STEP 132 - Check element a_132")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 132')
except Exception as e:
    print('FAIL - step 132' if isinstance(e, AssertionError) else f'ERROR - step 132: {e}')

print("STEP 133 - Check element span_133")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 133')
except Exception as e:
    print('FAIL - step 133' if isinstance(e, AssertionError) else f'ERROR - step 133: {e}')

print("STEP 134 - Check element a_134")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 134')
except Exception as e:
    print('FAIL - step 134' if isinstance(e, AssertionError) else f'ERROR - step 134: {e}')

print("STEP 135 - Check element span_135")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 135')
except Exception as e:
    print('FAIL - step 135' if isinstance(e, AssertionError) else f'ERROR - step 135: {e}')

print("STEP 136 - Check element a_136")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 136')
except Exception as e:
    print('FAIL - step 136' if isinstance(e, AssertionError) else f'ERROR - step 136: {e}')

print("STEP 137 - Check element span_137")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 137')
except Exception as e:
    print('FAIL - step 137' if isinstance(e, AssertionError) else f'ERROR - step 137: {e}')

print("STEP 138 - Check element a_138")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 138')
except Exception as e:
    print('FAIL - step 138' if isinstance(e, AssertionError) else f'ERROR - step 138: {e}')

print("STEP 139 - Check element span_139")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 139')
except Exception as e:
    print('FAIL - step 139' if isinstance(e, AssertionError) else f'ERROR - step 139: {e}')

print("STEP 140 - Check element a_140")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 140')
except Exception as e:
    print('FAIL - step 140' if isinstance(e, AssertionError) else f'ERROR - step 140: {e}')

print("STEP 141 - Check element span_141")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 141')
except Exception as e:
    print('FAIL - step 141' if isinstance(e, AssertionError) else f'ERROR - step 141: {e}')

print("STEP 142 - Check element a_142")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 142')
except Exception as e:
    print('FAIL - step 142' if isinstance(e, AssertionError) else f'ERROR - step 142: {e}')

print("STEP 143 - Check element span_143")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 143')
except Exception as e:
    print('FAIL - step 143' if isinstance(e, AssertionError) else f'ERROR - step 143: {e}')

print("STEP 144 - Check element a_144")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 144')
except Exception as e:
    print('FAIL - step 144' if isinstance(e, AssertionError) else f'ERROR - step 144: {e}')

print("STEP 145 - Check element footer_145")
try:
    element = driver.find_element(By.TAG_NAME, "footer")
    print('PASS - step 145')
except Exception as e:
    print('FAIL - step 145' if isinstance(e, AssertionError) else f'ERROR - step 145: {e}')

print("STEP 146 - Check element div_146")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 146')
except Exception as e:
    print('FAIL - step 146' if isinstance(e, AssertionError) else f'ERROR - step 146: {e}')

print("STEP 147 - Check element p_147")
try:
    element = driver.find_element(By.TAG_NAME, "p")
    print('PASS - step 147')
except Exception as e:
    print('FAIL - step 147' if isinstance(e, AssertionError) else f'ERROR - step 147: {e}')

print("STEP 148 - Check element a_148")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 148')
except Exception as e:
    print('FAIL - step 148' if isinstance(e, AssertionError) else f'ERROR - step 148: {e}')

print("STEP 149 - Check element p_149")
try:
    element = driver.find_element(By.TAG_NAME, "p")
    print('PASS - step 149')
except Exception as e:
    print('FAIL - step 149' if isinstance(e, AssertionError) else f'ERROR - step 149: {e}')

print("STEP 150 - Check element span_150")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 150')
except Exception as e:
    print('FAIL - step 150' if isinstance(e, AssertionError) else f'ERROR - step 150: {e}')

print("STEP 151 - Check element a_151")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 151')
except Exception as e:
    print('FAIL - step 151' if isinstance(e, AssertionError) else f'ERROR - step 151: {e}')

driver.quit()