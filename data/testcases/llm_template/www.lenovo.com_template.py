from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.lenovo.com")
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

print("STEP 4 - Check element meta_4")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 4')
except Exception as e:
    print('FAIL - step 4' if isinstance(e, AssertionError) else f'ERROR - step 4: {e}')

print("STEP 5 - Check element meta_5")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 5')
except Exception as e:
    print('FAIL - step 5' if isinstance(e, AssertionError) else f'ERROR - step 5: {e}')

print("STEP 6 - Check element script_6")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 6')
except Exception as e:
    print('FAIL - step 6' if isinstance(e, AssertionError) else f'ERROR - step 6: {e}')

print("STEP 7 - Check element script_7")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 7')
except Exception as e:
    print('FAIL - step 7' if isinstance(e, AssertionError) else f'ERROR - step 7: {e}')

print("STEP 8 - Check element script_8")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 8')
except Exception as e:
    print('FAIL - step 8' if isinstance(e, AssertionError) else f'ERROR - step 8: {e}')

print("STEP 9 - Check element script_9")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 9')
except Exception as e:
    print('FAIL - step 9' if isinstance(e, AssertionError) else f'ERROR - step 9: {e}')

print("STEP 10 - Check element script_10")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 10')
except Exception as e:
    print('FAIL - step 10' if isinstance(e, AssertionError) else f'ERROR - step 10: {e}')

print("STEP 11 - Check element script_11")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 11')
except Exception as e:
    print('FAIL - step 11' if isinstance(e, AssertionError) else f'ERROR - step 11: {e}')

print("STEP 12 - Check element script_12")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 12')
except Exception as e:
    print('FAIL - step 12' if isinstance(e, AssertionError) else f'ERROR - step 12: {e}')

print("STEP 13 - Check element script_13")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 13')
except Exception as e:
    print('FAIL - step 13' if isinstance(e, AssertionError) else f'ERROR - step 13: {e}')

print("STEP 14 - Check element script_14")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 14')
except Exception as e:
    print('FAIL - step 14' if isinstance(e, AssertionError) else f'ERROR - step 14: {e}')

print("STEP 15 - Check element script_15")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 15')
except Exception as e:
    print('FAIL - step 15' if isinstance(e, AssertionError) else f'ERROR - step 15: {e}')

print("STEP 16 - Check element script_16")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 16')
except Exception as e:
    print('FAIL - step 16' if isinstance(e, AssertionError) else f'ERROR - step 16: {e}')

print("STEP 17 - Check element script_17")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 17')
except Exception as e:
    print('FAIL - step 17' if isinstance(e, AssertionError) else f'ERROR - step 17: {e}')

print("STEP 18 - Check element script_18")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 18')
except Exception as e:
    print('FAIL - step 18' if isinstance(e, AssertionError) else f'ERROR - step 18: {e}')

print("STEP 19 - Check element script_19")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 19')
except Exception as e:
    print('FAIL - step 19' if isinstance(e, AssertionError) else f'ERROR - step 19: {e}')

print("STEP 20 - Check element script_20")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 20')
except Exception as e:
    print('FAIL - step 20' if isinstance(e, AssertionError) else f'ERROR - step 20: {e}')

print("STEP 21 - Check element script_21")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 21')
except Exception as e:
    print('FAIL - step 21' if isinstance(e, AssertionError) else f'ERROR - step 21: {e}')

print("STEP 22 - Check element script_22")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 22')
except Exception as e:
    print('FAIL - step 22' if isinstance(e, AssertionError) else f'ERROR - step 22: {e}')

print("STEP 23 - Check element script_23")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 23')
except Exception as e:
    print('FAIL - step 23' if isinstance(e, AssertionError) else f'ERROR - step 23: {e}')

print("STEP 24 - Check element script_24")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 24')
except Exception as e:
    print('FAIL - step 24' if isinstance(e, AssertionError) else f'ERROR - step 24: {e}')

print("STEP 25 - Check element script_25")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 25')
except Exception as e:
    print('FAIL - step 25' if isinstance(e, AssertionError) else f'ERROR - step 25: {e}')

print("STEP 26 - Check element meta_26")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 26')
except Exception as e:
    print('FAIL - step 26' if isinstance(e, AssertionError) else f'ERROR - step 26: {e}')

print("STEP 27 - Check element meta_27")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 27')
except Exception as e:
    print('FAIL - step 27' if isinstance(e, AssertionError) else f'ERROR - step 27: {e}')

print("STEP 28 - Check element meta_28")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 28')
except Exception as e:
    print('FAIL - step 28' if isinstance(e, AssertionError) else f'ERROR - step 28: {e}')

print("STEP 29 - Check element meta_29")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 29')
except Exception as e:
    print('FAIL - step 29' if isinstance(e, AssertionError) else f'ERROR - step 29: {e}')

print("STEP 30 - Check element meta_30")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 30')
except Exception as e:
    print('FAIL - step 30' if isinstance(e, AssertionError) else f'ERROR - step 30: {e}')

print("STEP 31 - Check element meta_31")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 31')
except Exception as e:
    print('FAIL - step 31' if isinstance(e, AssertionError) else f'ERROR - step 31: {e}')

print("STEP 32 - Check element meta_32")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 32')
except Exception as e:
    print('FAIL - step 32' if isinstance(e, AssertionError) else f'ERROR - step 32: {e}')

print("STEP 33 - Check element meta_33")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 33')
except Exception as e:
    print('FAIL - step 33' if isinstance(e, AssertionError) else f'ERROR - step 33: {e}')

print("STEP 34 - Check element meta_34")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 34')
except Exception as e:
    print('FAIL - step 34' if isinstance(e, AssertionError) else f'ERROR - step 34: {e}')

print("STEP 35 - Check element meta_35")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 35')
except Exception as e:
    print('FAIL - step 35' if isinstance(e, AssertionError) else f'ERROR - step 35: {e}')

print("STEP 36 - Check element meta_36")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 36')
except Exception as e:
    print('FAIL - step 36' if isinstance(e, AssertionError) else f'ERROR - step 36: {e}')

print("STEP 37 - Check element meta_37")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 37')
except Exception as e:
    print('FAIL - step 37' if isinstance(e, AssertionError) else f'ERROR - step 37: {e}')

print("STEP 38 - Check element link_38")
try:
    element = driver.find_element(By.TAG_NAME, "link")
    print('PASS - step 38')
except Exception as e:
    print('FAIL - step 38' if isinstance(e, AssertionError) else f'ERROR - step 38: {e}')

print("STEP 39 - Check element link_39")
try:
    element = driver.find_element(By.TAG_NAME, "link")
    print('PASS - step 39')
except Exception as e:
    print('FAIL - step 39' if isinstance(e, AssertionError) else f'ERROR - step 39: {e}')

print("STEP 40 - Check element link_40")
try:
    element = driver.find_element(By.TAG_NAME, "link")
    print('PASS - step 40')
except Exception as e:
    print('FAIL - step 40' if isinstance(e, AssertionError) else f'ERROR - step 40: {e}')

print("STEP 41 - Check element link_41")
try:
    element = driver.find_element(By.TAG_NAME, "link")
    print('PASS - step 41')
except Exception as e:
    print('FAIL - step 41' if isinstance(e, AssertionError) else f'ERROR - step 41: {e}')

print("STEP 42 - Check element link_42")
try:
    element = driver.find_element(By.TAG_NAME, "link")
    print('PASS - step 42')
except Exception as e:
    print('FAIL - step 42' if isinstance(e, AssertionError) else f'ERROR - step 42: {e}')

print("STEP 43 - Check element link_43")
try:
    element = driver.find_element(By.TAG_NAME, "link")
    print('PASS - step 43')
except Exception as e:
    print('FAIL - step 43' if isinstance(e, AssertionError) else f'ERROR - step 43: {e}')

print("STEP 44 - Check element title_44")
try:
    element = driver.find_element(By.TAG_NAME, "title")
    print('PASS - step 44')
except Exception as e:
    print('FAIL - step 44' if isinstance(e, AssertionError) else f'ERROR - step 44: {e}')

print("STEP 45 - Check element link_45")
try:
    element = driver.find_element(By.TAG_NAME, "link")
    print('PASS - step 45')
except Exception as e:
    print('FAIL - step 45' if isinstance(e, AssertionError) else f'ERROR - step 45: {e}')

print("STEP 46 - Check element link_46")
try:
    element = driver.find_element(By.TAG_NAME, "link")
    print('PASS - step 46')
except Exception as e:
    print('FAIL - step 46' if isinstance(e, AssertionError) else f'ERROR - step 46: {e}')

print("STEP 47 - Check element meta_47")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 47')
except Exception as e:
    print('FAIL - step 47' if isinstance(e, AssertionError) else f'ERROR - step 47: {e}')

print("STEP 48 - Check element meta_48")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 48')
except Exception as e:
    print('FAIL - step 48' if isinstance(e, AssertionError) else f'ERROR - step 48: {e}')

print("STEP 49 - Check element meta_49")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 49')
except Exception as e:
    print('FAIL - step 49' if isinstance(e, AssertionError) else f'ERROR - step 49: {e}')

print("STEP 50 - Check element meta_50")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 50')
except Exception as e:
    print('FAIL - step 50' if isinstance(e, AssertionError) else f'ERROR - step 50: {e}')

print("STEP 51 - Check element meta_51")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 51')
except Exception as e:
    print('FAIL - step 51' if isinstance(e, AssertionError) else f'ERROR - step 51: {e}')

print("STEP 52 - Check element meta_52")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 52')
except Exception as e:
    print('FAIL - step 52' if isinstance(e, AssertionError) else f'ERROR - step 52: {e}')

print("STEP 53 - Check element script_53")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 53')
except Exception as e:
    print('FAIL - step 53' if isinstance(e, AssertionError) else f'ERROR - step 53: {e}')

print("STEP 54 - Check element meta_54")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 54')
except Exception as e:
    print('FAIL - step 54' if isinstance(e, AssertionError) else f'ERROR - step 54: {e}')

print("STEP 55 - Check element meta_55")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 55')
except Exception as e:
    print('FAIL - step 55' if isinstance(e, AssertionError) else f'ERROR - step 55: {e}')

print("STEP 56 - Check element meta_56")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 56')
except Exception as e:
    print('FAIL - step 56' if isinstance(e, AssertionError) else f'ERROR - step 56: {e}')

print("STEP 57 - Check element meta_57")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 57')
except Exception as e:
    print('FAIL - step 57' if isinstance(e, AssertionError) else f'ERROR - step 57: {e}')

print("STEP 58 - Check element meta_58")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 58')
except Exception as e:
    print('FAIL - step 58' if isinstance(e, AssertionError) else f'ERROR - step 58: {e}')

print("STEP 59 - Check element meta_59")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 59')
except Exception as e:
    print('FAIL - step 59' if isinstance(e, AssertionError) else f'ERROR - step 59: {e}')

print("STEP 60 - Check element meta_60")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 60')
except Exception as e:
    print('FAIL - step 60' if isinstance(e, AssertionError) else f'ERROR - step 60: {e}')

print("STEP 61 - Check element meta_61")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 61')
except Exception as e:
    print('FAIL - step 61' if isinstance(e, AssertionError) else f'ERROR - step 61: {e}')

print("STEP 62 - Check element meta_62")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 62')
except Exception as e:
    print('FAIL - step 62' if isinstance(e, AssertionError) else f'ERROR - step 62: {e}')

print("STEP 63 - Check element meta_63")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 63')
except Exception as e:
    print('FAIL - step 63' if isinstance(e, AssertionError) else f'ERROR - step 63: {e}')

print("STEP 64 - Check element meta_64")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 64')
except Exception as e:
    print('FAIL - step 64' if isinstance(e, AssertionError) else f'ERROR - step 64: {e}')

print("STEP 65 - Check element link_65")
try:
    element = driver.find_element(By.TAG_NAME, "link")
    print('PASS - step 65')
except Exception as e:
    print('FAIL - step 65' if isinstance(e, AssertionError) else f'ERROR - step 65: {e}')

print("STEP 66 - Check element link_66")
try:
    element = driver.find_element(By.TAG_NAME, "link")
    print('PASS - step 66')
except Exception as e:
    print('FAIL - step 66' if isinstance(e, AssertionError) else f'ERROR - step 66: {e}')

print("STEP 67 - Check element link_67")
try:
    element = driver.find_element(By.TAG_NAME, "link")
    print('PASS - step 67')
except Exception as e:
    print('FAIL - step 67' if isinstance(e, AssertionError) else f'ERROR - step 67: {e}')

print("STEP 68 - Check element link_68")
try:
    element = driver.find_element(By.TAG_NAME, "link")
    print('PASS - step 68')
except Exception as e:
    print('FAIL - step 68' if isinstance(e, AssertionError) else f'ERROR - step 68: {e}')

print("STEP 69 - Check element style_69")
try:
    element = driver.find_element(By.TAG_NAME, "style")
    print('PASS - step 69')
except Exception as e:
    print('FAIL - step 69' if isinstance(e, AssertionError) else f'ERROR - step 69: {e}')

print("STEP 70 - Check element meta_70")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 70')
except Exception as e:
    print('FAIL - step 70' if isinstance(e, AssertionError) else f'ERROR - step 70: {e}')

print("STEP 71 - Check element meta_71")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 71')
except Exception as e:
    print('FAIL - step 71' if isinstance(e, AssertionError) else f'ERROR - step 71: {e}')

print("STEP 72 - Check element meta_72")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 72')
except Exception as e:
    print('FAIL - step 72' if isinstance(e, AssertionError) else f'ERROR - step 72: {e}')

print("STEP 73 - Check element meta_73")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 73')
except Exception as e:
    print('FAIL - step 73' if isinstance(e, AssertionError) else f'ERROR - step 73: {e}')

print("STEP 74 - Check element meta_74")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 74')
except Exception as e:
    print('FAIL - step 74' if isinstance(e, AssertionError) else f'ERROR - step 74: {e}')

print("STEP 75 - Check element meta_75")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 75')
except Exception as e:
    print('FAIL - step 75' if isinstance(e, AssertionError) else f'ERROR - step 75: {e}')

print("STEP 76 - Check element meta_76")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 76')
except Exception as e:
    print('FAIL - step 76' if isinstance(e, AssertionError) else f'ERROR - step 76: {e}')

print("STEP 77 - Check element meta_77")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 77')
except Exception as e:
    print('FAIL - step 77' if isinstance(e, AssertionError) else f'ERROR - step 77: {e}')

print("STEP 78 - Check element meta_78")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 78')
except Exception as e:
    print('FAIL - step 78' if isinstance(e, AssertionError) else f'ERROR - step 78: {e}')

print("STEP 79 - Check element meta_79")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 79')
except Exception as e:
    print('FAIL - step 79' if isinstance(e, AssertionError) else f'ERROR - step 79: {e}')

print("STEP 80 - Check element meta_80")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 80')
except Exception as e:
    print('FAIL - step 80' if isinstance(e, AssertionError) else f'ERROR - step 80: {e}')

print("STEP 81 - Check element meta_81")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 81')
except Exception as e:
    print('FAIL - step 81' if isinstance(e, AssertionError) else f'ERROR - step 81: {e}')

print("STEP 82 - Check element meta_82")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 82')
except Exception as e:
    print('FAIL - step 82' if isinstance(e, AssertionError) else f'ERROR - step 82: {e}')

print("STEP 83 - Check element meta_83")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 83')
except Exception as e:
    print('FAIL - step 83' if isinstance(e, AssertionError) else f'ERROR - step 83: {e}')

print("STEP 84 - Check element meta_84")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 84')
except Exception as e:
    print('FAIL - step 84' if isinstance(e, AssertionError) else f'ERROR - step 84: {e}')

print("STEP 85 - Check element meta_85")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 85')
except Exception as e:
    print('FAIL - step 85' if isinstance(e, AssertionError) else f'ERROR - step 85: {e}')

print("STEP 86 - Check element meta_86")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 86')
except Exception as e:
    print('FAIL - step 86' if isinstance(e, AssertionError) else f'ERROR - step 86: {e}')

print("STEP 87 - Check element meta_87")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 87')
except Exception as e:
    print('FAIL - step 87' if isinstance(e, AssertionError) else f'ERROR - step 87: {e}')

print("STEP 88 - Check element meta_88")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 88')
except Exception as e:
    print('FAIL - step 88' if isinstance(e, AssertionError) else f'ERROR - step 88: {e}')

print("STEP 89 - Check element meta_89")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 89')
except Exception as e:
    print('FAIL - step 89' if isinstance(e, AssertionError) else f'ERROR - step 89: {e}')

print("STEP 90 - Check element meta_90")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 90')
except Exception as e:
    print('FAIL - step 90' if isinstance(e, AssertionError) else f'ERROR - step 90: {e}')

print("STEP 91 - Check element meta_91")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 91')
except Exception as e:
    print('FAIL - step 91' if isinstance(e, AssertionError) else f'ERROR - step 91: {e}')

print("STEP 92 - Check element meta_92")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 92')
except Exception as e:
    print('FAIL - step 92' if isinstance(e, AssertionError) else f'ERROR - step 92: {e}')

print("STEP 93 - Check element meta_93")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 93')
except Exception as e:
    print('FAIL - step 93' if isinstance(e, AssertionError) else f'ERROR - step 93: {e}')

print("STEP 94 - Check element meta_94")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 94')
except Exception as e:
    print('FAIL - step 94' if isinstance(e, AssertionError) else f'ERROR - step 94: {e}')

print("STEP 95 - Check element meta_95")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 95')
except Exception as e:
    print('FAIL - step 95' if isinstance(e, AssertionError) else f'ERROR - step 95: {e}')

print("STEP 96 - Check element meta_96")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 96')
except Exception as e:
    print('FAIL - step 96' if isinstance(e, AssertionError) else f'ERROR - step 96: {e}')

print("STEP 97 - Check element meta_97")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 97')
except Exception as e:
    print('FAIL - step 97' if isinstance(e, AssertionError) else f'ERROR - step 97: {e}')

print("STEP 98 - Check element meta_98")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 98')
except Exception as e:
    print('FAIL - step 98' if isinstance(e, AssertionError) else f'ERROR - step 98: {e}')

print("STEP 99 - Check element meta_99")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 99')
except Exception as e:
    print('FAIL - step 99' if isinstance(e, AssertionError) else f'ERROR - step 99: {e}')

print("STEP 100 - Check element meta_100")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 100')
except Exception as e:
    print('FAIL - step 100' if isinstance(e, AssertionError) else f'ERROR - step 100: {e}')

print("STEP 101 - Check element meta_101")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 101')
except Exception as e:
    print('FAIL - step 101' if isinstance(e, AssertionError) else f'ERROR - step 101: {e}')

print("STEP 102 - Check element meta_102")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 102')
except Exception as e:
    print('FAIL - step 102' if isinstance(e, AssertionError) else f'ERROR - step 102: {e}')

print("STEP 103 - Check element meta_103")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 103')
except Exception as e:
    print('FAIL - step 103' if isinstance(e, AssertionError) else f'ERROR - step 103: {e}')

print("STEP 104 - Check element meta_104")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 104')
except Exception as e:
    print('FAIL - step 104' if isinstance(e, AssertionError) else f'ERROR - step 104: {e}')

print("STEP 105 - Check element meta_105")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 105')
except Exception as e:
    print('FAIL - step 105' if isinstance(e, AssertionError) else f'ERROR - step 105: {e}')

print("STEP 106 - Check element meta_106")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 106')
except Exception as e:
    print('FAIL - step 106' if isinstance(e, AssertionError) else f'ERROR - step 106: {e}')

print("STEP 107 - Check element meta_107")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 107')
except Exception as e:
    print('FAIL - step 107' if isinstance(e, AssertionError) else f'ERROR - step 107: {e}')

print("STEP 108 - Check element link_108")
try:
    element = driver.find_element(By.TAG_NAME, "link")
    print('PASS - step 108')
except Exception as e:
    print('FAIL - step 108' if isinstance(e, AssertionError) else f'ERROR - step 108: {e}')

print("STEP 109 - Check element script_109")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 109')
except Exception as e:
    print('FAIL - step 109' if isinstance(e, AssertionError) else f'ERROR - step 109: {e}')

print("STEP 110 - Check element link_110")
try:
    element = driver.find_element(By.TAG_NAME, "link")
    print('PASS - step 110')
except Exception as e:
    print('FAIL - step 110' if isinstance(e, AssertionError) else f'ERROR - step 110: {e}')

print("STEP 111 - Check element script_111")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 111')
except Exception as e:
    print('FAIL - step 111' if isinstance(e, AssertionError) else f'ERROR - step 111: {e}')

print("STEP 112 - Check element script_112")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 112')
except Exception as e:
    print('FAIL - step 112' if isinstance(e, AssertionError) else f'ERROR - step 112: {e}')

print("STEP 113 - Check element style_113")
try:
    element = driver.find_element(By.TAG_NAME, "style")
    print('PASS - step 113')
except Exception as e:
    print('FAIL - step 113' if isinstance(e, AssertionError) else f'ERROR - step 113: {e}')

print("STEP 114 - Check element style_114")
try:
    element = driver.find_element(By.TAG_NAME, "style")
    print('PASS - step 114')
except Exception as e:
    print('FAIL - step 114' if isinstance(e, AssertionError) else f'ERROR - step 114: {e}')

print("STEP 115 - Check element style_115")
try:
    element = driver.find_element(By.TAG_NAME, "style")
    print('PASS - step 115')
except Exception as e:
    print('FAIL - step 115' if isinstance(e, AssertionError) else f'ERROR - step 115: {e}')

print("STEP 116 - Check element script_116")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 116')
except Exception as e:
    print('FAIL - step 116' if isinstance(e, AssertionError) else f'ERROR - step 116: {e}')

print("STEP 117 - Check element script_117")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 117')
except Exception as e:
    print('FAIL - step 117' if isinstance(e, AssertionError) else f'ERROR - step 117: {e}')

print("STEP 118 - Check element script_118")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 118')
except Exception as e:
    print('FAIL - step 118' if isinstance(e, AssertionError) else f'ERROR - step 118: {e}')

print("STEP 119 - Check element script_119")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 119')
except Exception as e:
    print('FAIL - step 119' if isinstance(e, AssertionError) else f'ERROR - step 119: {e}')

print("STEP 120 - Check element link_120")
try:
    element = driver.find_element(By.TAG_NAME, "link")
    print('PASS - step 120')
except Exception as e:
    print('FAIL - step 120' if isinstance(e, AssertionError) else f'ERROR - step 120: {e}')

print("STEP 121 - Check element link_121")
try:
    element = driver.find_element(By.TAG_NAME, "link")
    print('PASS - step 121')
except Exception as e:
    print('FAIL - step 121' if isinstance(e, AssertionError) else f'ERROR - step 121: {e}')

print("STEP 122 - Check element script_122")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 122')
except Exception as e:
    print('FAIL - step 122' if isinstance(e, AssertionError) else f'ERROR - step 122: {e}')

print("STEP 123 - Check element script_123")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 123')
except Exception as e:
    print('FAIL - step 123' if isinstance(e, AssertionError) else f'ERROR - step 123: {e}')

print("STEP 124 - Check element meta_124")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 124')
except Exception as e:
    print('FAIL - step 124' if isinstance(e, AssertionError) else f'ERROR - step 124: {e}')

print("STEP 125 - Check element script_125")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 125')
except Exception as e:
    print('FAIL - step 125' if isinstance(e, AssertionError) else f'ERROR - step 125: {e}')

print("STEP 126 - Check element script_126")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 126')
except Exception as e:
    print('FAIL - step 126' if isinstance(e, AssertionError) else f'ERROR - step 126: {e}')

print("STEP 127 - Check element script_127")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 127')
except Exception as e:
    print('FAIL - step 127' if isinstance(e, AssertionError) else f'ERROR - step 127: {e}')

print("STEP 128 - Check element script_128")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 128')
except Exception as e:
    print('FAIL - step 128' if isinstance(e, AssertionError) else f'ERROR - step 128: {e}')

print("STEP 129 - Check element script_129")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 129')
except Exception as e:
    print('FAIL - step 129' if isinstance(e, AssertionError) else f'ERROR - step 129: {e}')

print("STEP 130 - Check element link_130")
try:
    element = driver.find_element(By.TAG_NAME, "link")
    print('PASS - step 130')
except Exception as e:
    print('FAIL - step 130' if isinstance(e, AssertionError) else f'ERROR - step 130: {e}')

print("STEP 131 - Check element script_131")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 131')
except Exception as e:
    print('FAIL - step 131' if isinstance(e, AssertionError) else f'ERROR - step 131: {e}')

print("STEP 132 - Check element script_132")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 132')
except Exception as e:
    print('FAIL - step 132' if isinstance(e, AssertionError) else f'ERROR - step 132: {e}')

print("STEP 133 - Check element style_133")
try:
    element = driver.find_element(By.TAG_NAME, "style")
    print('PASS - step 133')
except Exception as e:
    print('FAIL - step 133' if isinstance(e, AssertionError) else f'ERROR - step 133: {e}')

print("STEP 134 - Check element style_134")
try:
    element = driver.find_element(By.TAG_NAME, "style")
    print('PASS - step 134')
except Exception as e:
    print('FAIL - step 134' if isinstance(e, AssertionError) else f'ERROR - step 134: {e}')

print("STEP 135 - Check element style_135")
try:
    element = driver.find_element(By.TAG_NAME, "style")
    print('PASS - step 135')
except Exception as e:
    print('FAIL - step 135' if isinstance(e, AssertionError) else f'ERROR - step 135: {e}')

print("STEP 136 - Check element style_136")
try:
    element = driver.find_element(By.TAG_NAME, "style")
    print('PASS - step 136')
except Exception as e:
    print('FAIL - step 136' if isinstance(e, AssertionError) else f'ERROR - step 136: {e}')

print("STEP 137 - Check element script_137")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 137')
except Exception as e:
    print('FAIL - step 137' if isinstance(e, AssertionError) else f'ERROR - step 137: {e}')

print("STEP 138 - Check element style_138")
try:
    element = driver.find_element(By.TAG_NAME, "style")
    print('PASS - step 138')
except Exception as e:
    print('FAIL - step 138' if isinstance(e, AssertionError) else f'ERROR - step 138: {e}')

print("STEP 139 - Check element style_139")
try:
    element = driver.find_element(By.TAG_NAME, "style")
    print('PASS - step 139')
except Exception as e:
    print('FAIL - step 139' if isinstance(e, AssertionError) else f'ERROR - step 139: {e}')

print("STEP 140 - Check element style_140")
try:
    element = driver.find_element(By.TAG_NAME, "style")
    print('PASS - step 140')
except Exception as e:
    print('FAIL - step 140' if isinstance(e, AssertionError) else f'ERROR - step 140: {e}')

print("STEP 141 - Check element style_141")
try:
    element = driver.find_element(By.TAG_NAME, "style")
    print('PASS - step 141')
except Exception as e:
    print('FAIL - step 141' if isinstance(e, AssertionError) else f'ERROR - step 141: {e}')

print("STEP 142 - Check element script_142")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 142')
except Exception as e:
    print('FAIL - step 142' if isinstance(e, AssertionError) else f'ERROR - step 142: {e}')

print("STEP 143 - Check element script_143")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 143')
except Exception as e:
    print('FAIL - step 143' if isinstance(e, AssertionError) else f'ERROR - step 143: {e}')

print("STEP 144 - Check element script_144")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 144')
except Exception as e:
    print('FAIL - step 144' if isinstance(e, AssertionError) else f'ERROR - step 144: {e}')

print("STEP 145 - Check element script_145")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 145')
except Exception as e:
    print('FAIL - step 145' if isinstance(e, AssertionError) else f'ERROR - step 145: {e}')

print("STEP 146 - Check element script_146")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 146')
except Exception as e:
    print('FAIL - step 146' if isinstance(e, AssertionError) else f'ERROR - step 146: {e}')

print("STEP 147 - Check element script_147")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 147')
except Exception as e:
    print('FAIL - step 147' if isinstance(e, AssertionError) else f'ERROR - step 147: {e}')

print("STEP 148 - Check element script_148")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 148')
except Exception as e:
    print('FAIL - step 148' if isinstance(e, AssertionError) else f'ERROR - step 148: {e}')

print("STEP 149 - Check element style_149")
try:
    element = driver.find_element(By.TAG_NAME, "style")
    print('PASS - step 149')
except Exception as e:
    print('FAIL - step 149' if isinstance(e, AssertionError) else f'ERROR - step 149: {e}')

print("STEP 150 - Check element style_150")
try:
    element = driver.find_element(By.TAG_NAME, "style")
    print('PASS - step 150')
except Exception as e:
    print('FAIL - step 150' if isinstance(e, AssertionError) else f'ERROR - step 150: {e}')

print("STEP 151 - Check element script_151")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 151')
except Exception as e:
    print('FAIL - step 151' if isinstance(e, AssertionError) else f'ERROR - step 151: {e}')

print("STEP 152 - Check element style_152")
try:
    element = driver.find_element(By.TAG_NAME, "style")
    print('PASS - step 152')
except Exception as e:
    print('FAIL - step 152' if isinstance(e, AssertionError) else f'ERROR - step 152: {e}')

print("STEP 153 - Check element style_153")
try:
    element = driver.find_element(By.TAG_NAME, "style")
    print('PASS - step 153')
except Exception as e:
    print('FAIL - step 153' if isinstance(e, AssertionError) else f'ERROR - step 153: {e}')

print("STEP 154 - Check element style_154")
try:
    element = driver.find_element(By.TAG_NAME, "style")
    print('PASS - step 154')
except Exception as e:
    print('FAIL - step 154' if isinstance(e, AssertionError) else f'ERROR - step 154: {e}')

print("STEP 155 - Check element style_155")
try:
    element = driver.find_element(By.TAG_NAME, "style")
    print('PASS - step 155')
except Exception as e:
    print('FAIL - step 155' if isinstance(e, AssertionError) else f'ERROR - step 155: {e}')

print("STEP 156 - Check element style_156")
try:
    element = driver.find_element(By.TAG_NAME, "style")
    print('PASS - step 156')
except Exception as e:
    print('FAIL - step 156' if isinstance(e, AssertionError) else f'ERROR - step 156: {e}')

print("STEP 157 - Check element style_157")
try:
    element = driver.find_element(By.TAG_NAME, "style")
    print('PASS - step 157')
except Exception as e:
    print('FAIL - step 157' if isinstance(e, AssertionError) else f'ERROR - step 157: {e}')

print("STEP 158 - Check element style_158")
try:
    element = driver.find_element(By.TAG_NAME, "style")
    print('PASS - step 158')
except Exception as e:
    print('FAIL - step 158' if isinstance(e, AssertionError) else f'ERROR - step 158: {e}')

print("STEP 159 - Check element style_159")
try:
    element = driver.find_element(By.TAG_NAME, "style")
    print('PASS - step 159')
except Exception as e:
    print('FAIL - step 159' if isinstance(e, AssertionError) else f'ERROR - step 159: {e}')

print("STEP 160 - Check element style_160")
try:
    element = driver.find_element(By.TAG_NAME, "style")
    print('PASS - step 160')
except Exception as e:
    print('FAIL - step 160' if isinstance(e, AssertionError) else f'ERROR - step 160: {e}')

print("STEP 161 - Check element style_161")
try:
    element = driver.find_element(By.TAG_NAME, "style")
    print('PASS - step 161')
except Exception as e:
    print('FAIL - step 161' if isinstance(e, AssertionError) else f'ERROR - step 161: {e}')

print("STEP 162 - Check element style_162")
try:
    element = driver.find_element(By.TAG_NAME, "style")
    print('PASS - step 162')
except Exception as e:
    print('FAIL - step 162' if isinstance(e, AssertionError) else f'ERROR - step 162: {e}')

print("STEP 163 - Check element script_163")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 163')
except Exception as e:
    print('FAIL - step 163' if isinstance(e, AssertionError) else f'ERROR - step 163: {e}')

print("STEP 164 - Check element meta_164")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 164')
except Exception as e:
    print('FAIL - step 164' if isinstance(e, AssertionError) else f'ERROR - step 164: {e}')

print("STEP 165 - Check element meta_165")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 165')
except Exception as e:
    print('FAIL - step 165' if isinstance(e, AssertionError) else f'ERROR - step 165: {e}')

print("STEP 166 - Check element script_166")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 166')
except Exception as e:
    print('FAIL - step 166' if isinstance(e, AssertionError) else f'ERROR - step 166: {e}')

print("STEP 167 - Check element script_167")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 167')
except Exception as e:
    print('FAIL - step 167' if isinstance(e, AssertionError) else f'ERROR - step 167: {e}')

print("STEP 168 - Check element script_168")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 168')
except Exception as e:
    print('FAIL - step 168' if isinstance(e, AssertionError) else f'ERROR - step 168: {e}')

print("STEP 169 - Check element script_169")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 169')
except Exception as e:
    print('FAIL - step 169' if isinstance(e, AssertionError) else f'ERROR - step 169: {e}')

print("STEP 170 - Check element script_170")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 170')
except Exception as e:
    print('FAIL - step 170' if isinstance(e, AssertionError) else f'ERROR - step 170: {e}')

print("STEP 171 - Check element script_171")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 171')
except Exception as e:
    print('FAIL - step 171' if isinstance(e, AssertionError) else f'ERROR - step 171: {e}')

print("STEP 172 - Check element script_172")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 172')
except Exception as e:
    print('FAIL - step 172' if isinstance(e, AssertionError) else f'ERROR - step 172: {e}')

print("STEP 173 - Check element script_173")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 173')
except Exception as e:
    print('FAIL - step 173' if isinstance(e, AssertionError) else f'ERROR - step 173: {e}')

print("STEP 174 - Check element script_174")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 174')
except Exception as e:
    print('FAIL - step 174' if isinstance(e, AssertionError) else f'ERROR - step 174: {e}')

print("STEP 175 - Check element script_175")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 175')
except Exception as e:
    print('FAIL - step 175' if isinstance(e, AssertionError) else f'ERROR - step 175: {e}')

print("STEP 176 - Check element script_176")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 176')
except Exception as e:
    print('FAIL - step 176' if isinstance(e, AssertionError) else f'ERROR - step 176: {e}')

print("STEP 177 - Check element script_177")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 177')
except Exception as e:
    print('FAIL - step 177' if isinstance(e, AssertionError) else f'ERROR - step 177: {e}')

print("STEP 178 - Check element script_178")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 178')
except Exception as e:
    print('FAIL - step 178' if isinstance(e, AssertionError) else f'ERROR - step 178: {e}')

print("STEP 179 - Check element script_179")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 179')
except Exception as e:
    print('FAIL - step 179' if isinstance(e, AssertionError) else f'ERROR - step 179: {e}')

print("STEP 180 - Check element script_180")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 180')
except Exception as e:
    print('FAIL - step 180' if isinstance(e, AssertionError) else f'ERROR - step 180: {e}')

print("STEP 181 - Check element script_181")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 181')
except Exception as e:
    print('FAIL - step 181' if isinstance(e, AssertionError) else f'ERROR - step 181: {e}')

print("STEP 182 - Check element script_182")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 182')
except Exception as e:
    print('FAIL - step 182' if isinstance(e, AssertionError) else f'ERROR - step 182: {e}')

print("STEP 183 - Check element script_183")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 183')
except Exception as e:
    print('FAIL - step 183' if isinstance(e, AssertionError) else f'ERROR - step 183: {e}')

print("STEP 184 - Check element script_184")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 184')
except Exception as e:
    print('FAIL - step 184' if isinstance(e, AssertionError) else f'ERROR - step 184: {e}')

print("STEP 185 - Check element script_185")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 185')
except Exception as e:
    print('FAIL - step 185' if isinstance(e, AssertionError) else f'ERROR - step 185: {e}')

print("STEP 186 - Check element script_186")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 186')
except Exception as e:
    print('FAIL - step 186' if isinstance(e, AssertionError) else f'ERROR - step 186: {e}')

print("STEP 187 - Check element script_187")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 187')
except Exception as e:
    print('FAIL - step 187' if isinstance(e, AssertionError) else f'ERROR - step 187: {e}')

print("STEP 188 - Check element script_188")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 188')
except Exception as e:
    print('FAIL - step 188' if isinstance(e, AssertionError) else f'ERROR - step 188: {e}')

print("STEP 189 - Check element link_189")
try:
    element = driver.find_element(By.TAG_NAME, "link")
    print('PASS - step 189')
except Exception as e:
    print('FAIL - step 189' if isinstance(e, AssertionError) else f'ERROR - step 189: {e}')

print("STEP 190 - Check element style_190")
try:
    element = driver.find_element(By.TAG_NAME, "style")
    print('PASS - step 190')
except Exception as e:
    print('FAIL - step 190' if isinstance(e, AssertionError) else f'ERROR - step 190: {e}')

print("STEP 191 - Check element style_191")
try:
    element = driver.find_element(By.TAG_NAME, "style")
    print('PASS - step 191')
except Exception as e:
    print('FAIL - step 191' if isinstance(e, AssertionError) else f'ERROR - step 191: {e}')

print("STEP 192 - Check element script_192")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 192')
except Exception as e:
    print('FAIL - step 192' if isinstance(e, AssertionError) else f'ERROR - step 192: {e}')

print("STEP 193 - Check element script_193")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 193')
except Exception as e:
    print('FAIL - step 193' if isinstance(e, AssertionError) else f'ERROR - step 193: {e}')

print("STEP 194 - Check element body_194")
try:
    element = driver.find_element(By.TAG_NAME, "body")
    print('PASS - step 194')
except Exception as e:
    print('FAIL - step 194' if isinstance(e, AssertionError) else f'ERROR - step 194: {e}')

print("STEP 195 - Check element h1_195")
try:
    element = driver.find_element(By.TAG_NAME, "h1")
    print('PASS - step 195')
except Exception as e:
    print('FAIL - step 195' if isinstance(e, AssertionError) else f'ERROR - step 195: {e}')

print("STEP 196 - Check element h2_196")
try:
    element = driver.find_element(By.TAG_NAME, "h2")
    print('PASS - step 196')
except Exception as e:
    print('FAIL - step 196' if isinstance(e, AssertionError) else f'ERROR - step 196: {e}')

print("STEP 197 - Check element h3_197")
try:
    element = driver.find_element(By.TAG_NAME, "h3")
    print('PASS - step 197')
except Exception as e:
    print('FAIL - step 197' if isinstance(e, AssertionError) else f'ERROR - step 197: {e}')

print("STEP 198 - Check element div_198")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 198')
except Exception as e:
    print('FAIL - step 198' if isinstance(e, AssertionError) else f'ERROR - step 198: {e}')

print("STEP 199 - Check element div_199")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 199')
except Exception as e:
    print('FAIL - step 199' if isinstance(e, AssertionError) else f'ERROR - step 199: {e}')

print("STEP 200 - Check element div_200")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 200')
except Exception as e:
    print('FAIL - step 200' if isinstance(e, AssertionError) else f'ERROR - step 200: {e}')

print("STEP 201 - Check element div_201")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 201')
except Exception as e:
    print('FAIL - step 201' if isinstance(e, AssertionError) else f'ERROR - step 201: {e}')

print("STEP 202 - Check element div_202")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 202')
except Exception as e:
    print('FAIL - step 202' if isinstance(e, AssertionError) else f'ERROR - step 202: {e}')

print("STEP 203 - Check element script_203")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 203')
except Exception as e:
    print('FAIL - step 203' if isinstance(e, AssertionError) else f'ERROR - step 203: {e}')

print("STEP 204 - Check element script_204")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 204')
except Exception as e:
    print('FAIL - step 204' if isinstance(e, AssertionError) else f'ERROR - step 204: {e}')

print("STEP 205 - Check element div_205")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 205')
except Exception as e:
    print('FAIL - step 205' if isinstance(e, AssertionError) else f'ERROR - step 205: {e}')

print("STEP 206 - Check element meta_206")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 206')
except Exception as e:
    print('FAIL - step 206' if isinstance(e, AssertionError) else f'ERROR - step 206: {e}')

print("STEP 207 - Check element meta_207")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 207')
except Exception as e:
    print('FAIL - step 207' if isinstance(e, AssertionError) else f'ERROR - step 207: {e}')

print("STEP 208 - Check element link_208")
try:
    element = driver.find_element(By.TAG_NAME, "link")
    print('PASS - step 208')
except Exception as e:
    print('FAIL - step 208' if isinstance(e, AssertionError) else f'ERROR - step 208: {e}')

print("STEP 209 - Check element script_209")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 209')
except Exception as e:
    print('FAIL - step 209' if isinstance(e, AssertionError) else f'ERROR - step 209: {e}')

print("STEP 210 - Check element div_210")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 210')
except Exception as e:
    print('FAIL - step 210' if isinstance(e, AssertionError) else f'ERROR - step 210: {e}')

print("STEP 211 - Check element div_211")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 211')
except Exception as e:
    print('FAIL - step 211' if isinstance(e, AssertionError) else f'ERROR - step 211: {e}')

print("STEP 212 - Check element div_212")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 212')
except Exception as e:
    print('FAIL - step 212' if isinstance(e, AssertionError) else f'ERROR - step 212: {e}')

print("STEP 213 - Check element div_213")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 213')
except Exception as e:
    print('FAIL - step 213' if isinstance(e, AssertionError) else f'ERROR - step 213: {e}')

print("STEP 214 - Check element div_214")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 214')
except Exception as e:
    print('FAIL - step 214' if isinstance(e, AssertionError) else f'ERROR - step 214: {e}')

print("STEP 215 - Check element div_215")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 215')
except Exception as e:
    print('FAIL - step 215' if isinstance(e, AssertionError) else f'ERROR - step 215: {e}')

print("STEP 216 - Check element div_216")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 216')
except Exception as e:
    print('FAIL - step 216' if isinstance(e, AssertionError) else f'ERROR - step 216: {e}')

print("STEP 217 - Check element nav_217")
try:
    element = driver.find_element(By.TAG_NAME, "nav")
    print('PASS - step 217')
except Exception as e:
    print('FAIL - step 217' if isinstance(e, AssertionError) else f'ERROR - step 217: {e}')

print("STEP 218 - Check element div_218")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 218')
except Exception as e:
    print('FAIL - step 218' if isinstance(e, AssertionError) else f'ERROR - step 218: {e}')

print("STEP 219 - Check element ul_219")
try:
    element = driver.find_element(By.TAG_NAME, "ul")
    print('PASS - step 219')
except Exception as e:
    print('FAIL - step 219' if isinstance(e, AssertionError) else f'ERROR - step 219: {e}')

print("STEP 220 - Check element li_220")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 220')
except Exception as e:
    print('FAIL - step 220' if isinstance(e, AssertionError) else f'ERROR - step 220: {e}')

print("STEP 221 - Check element a_221")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 221')
except Exception as e:
    print('FAIL - step 221' if isinstance(e, AssertionError) else f'ERROR - step 221: {e}')

print("STEP 222 - Check element div_222")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 222')
except Exception as e:
    print('FAIL - step 222' if isinstance(e, AssertionError) else f'ERROR - step 222: {e}')

print("STEP 223 - Check element div_223")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 223')
except Exception as e:
    print('FAIL - step 223' if isinstance(e, AssertionError) else f'ERROR - step 223: {e}')

print("STEP 224 - Check element span_224")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 224')
except Exception as e:
    print('FAIL - step 224' if isinstance(e, AssertionError) else f'ERROR - step 224: {e}')

print("STEP 225 - Check element li_225")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 225')
except Exception as e:
    print('FAIL - step 225' if isinstance(e, AssertionError) else f'ERROR - step 225: {e}')

print("STEP 226 - Check element a_226")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 226')
except Exception as e:
    print('FAIL - step 226' if isinstance(e, AssertionError) else f'ERROR - step 226: {e}')

print("STEP 227 - Check element div_227")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 227')
except Exception as e:
    print('FAIL - step 227' if isinstance(e, AssertionError) else f'ERROR - step 227: {e}')

print("STEP 228 - Check element div_228")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 228')
except Exception as e:
    print('FAIL - step 228' if isinstance(e, AssertionError) else f'ERROR - step 228: {e}')

print("STEP 229 - Check element span_229")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 229')
except Exception as e:
    print('FAIL - step 229' if isinstance(e, AssertionError) else f'ERROR - step 229: {e}')

print("STEP 230 - Check element li_230")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 230')
except Exception as e:
    print('FAIL - step 230' if isinstance(e, AssertionError) else f'ERROR - step 230: {e}')

print("STEP 231 - Check element a_231")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 231')
except Exception as e:
    print('FAIL - step 231' if isinstance(e, AssertionError) else f'ERROR - step 231: {e}')

print("STEP 232 - Check element div_232")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 232')
except Exception as e:
    print('FAIL - step 232' if isinstance(e, AssertionError) else f'ERROR - step 232: {e}')

print("STEP 233 - Check element div_233")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 233')
except Exception as e:
    print('FAIL - step 233' if isinstance(e, AssertionError) else f'ERROR - step 233: {e}')

print("STEP 234 - Check element span_234")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 234')
except Exception as e:
    print('FAIL - step 234' if isinstance(e, AssertionError) else f'ERROR - step 234: {e}')

print("STEP 235 - Check element li_235")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 235')
except Exception as e:
    print('FAIL - step 235' if isinstance(e, AssertionError) else f'ERROR - step 235: {e}')

print("STEP 236 - Check element a_236")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 236')
except Exception as e:
    print('FAIL - step 236' if isinstance(e, AssertionError) else f'ERROR - step 236: {e}')

print("STEP 237 - Check element div_237")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 237')
except Exception as e:
    print('FAIL - step 237' if isinstance(e, AssertionError) else f'ERROR - step 237: {e}')

print("STEP 238 - Check element div_238")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 238')
except Exception as e:
    print('FAIL - step 238' if isinstance(e, AssertionError) else f'ERROR - step 238: {e}')

print("STEP 239 - Check element span_239")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 239')
except Exception as e:
    print('FAIL - step 239' if isinstance(e, AssertionError) else f'ERROR - step 239: {e}')

print("STEP 240 - Check element li_240")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 240')
except Exception as e:
    print('FAIL - step 240' if isinstance(e, AssertionError) else f'ERROR - step 240: {e}')

print("STEP 241 - Check element a_241")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 241')
except Exception as e:
    print('FAIL - step 241' if isinstance(e, AssertionError) else f'ERROR - step 241: {e}')

print("STEP 242 - Check element div_242")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 242')
except Exception as e:
    print('FAIL - step 242' if isinstance(e, AssertionError) else f'ERROR - step 242: {e}')

print("STEP 243 - Check element div_243")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 243')
except Exception as e:
    print('FAIL - step 243' if isinstance(e, AssertionError) else f'ERROR - step 243: {e}')

print("STEP 244 - Check element span_244")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 244')
except Exception as e:
    print('FAIL - step 244' if isinstance(e, AssertionError) else f'ERROR - step 244: {e}')

print("STEP 245 - Check element style_245")
try:
    element = driver.find_element(By.TAG_NAME, "style")
    print('PASS - step 245')
except Exception as e:
    print('FAIL - step 245' if isinstance(e, AssertionError) else f'ERROR - step 245: {e}')

print("STEP 246 - Check element div_246")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 246')
except Exception as e:
    print('FAIL - step 246' if isinstance(e, AssertionError) else f'ERROR - step 246: {e}')

print("STEP 247 - Check element label_247")
try:
    element = driver.find_element(By.TAG_NAME, "label")
    print('PASS - step 247')
except Exception as e:
    print('FAIL - step 247' if isinstance(e, AssertionError) else f'ERROR - step 247: {e}')

print("STEP 248 - Check element form_248")
try:
    element = driver.find_element(By.TAG_NAME, "form")
    print('PASS - step 248')
except Exception as e:
    print('FAIL - step 248' if isinstance(e, AssertionError) else f'ERROR - step 248: {e}')

print("STEP 249 - Check element div_249")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 249')
except Exception as e:
    print('FAIL - step 249' if isinstance(e, AssertionError) else f'ERROR - step 249: {e}')

print("STEP 250 - Check element div_250")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 250')
except Exception as e:
    print('FAIL - step 250' if isinstance(e, AssertionError) else f'ERROR - step 250: {e}')

print("STEP 251 - Check element div_251")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 251')
except Exception as e:
    print('FAIL - step 251' if isinstance(e, AssertionError) else f'ERROR - step 251: {e}')

print("STEP 252 - Check element span_252")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 252')
except Exception as e:
    print('FAIL - step 252' if isinstance(e, AssertionError) else f'ERROR - step 252: {e}')

print("STEP 253 - Check element input_253")
try:
    element = driver.find_element(By.TAG_NAME, "input")
    print('PASS - step 253')
except Exception as e:
    print('FAIL - step 253' if isinstance(e, AssertionError) else f'ERROR - step 253: {e}')

print("STEP 254 - Check element input_254")
try:
    element = driver.find_element(By.TAG_NAME, "input")
    print('PASS - step 254')
except Exception as e:
    print('FAIL - step 254' if isinstance(e, AssertionError) else f'ERROR - step 254: {e}')

print("STEP 255 - Check element img_255")
try:
    element = driver.find_element(By.TAG_NAME, "img")
    print('PASS - step 255')
except Exception as e:
    print('FAIL - step 255' if isinstance(e, AssertionError) else f'ERROR - step 255: {e}')

print("STEP 256 - Check element span_256")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 256')
except Exception as e:
    print('FAIL - step 256' if isinstance(e, AssertionError) else f'ERROR - step 256: {e}')

print("STEP 257 - Check element script_257")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 257')
except Exception as e:
    print('FAIL - step 257' if isinstance(e, AssertionError) else f'ERROR - step 257: {e}')

print("STEP 258 - Check element div_258")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 258')
except Exception as e:
    print('FAIL - step 258' if isinstance(e, AssertionError) else f'ERROR - step 258: {e}')

print("STEP 259 - Check element div_259")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 259')
except Exception as e:
    print('FAIL - step 259' if isinstance(e, AssertionError) else f'ERROR - step 259: {e}')

print("STEP 260 - Check element a_260")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 260')
except Exception as e:
    print('FAIL - step 260' if isinstance(e, AssertionError) else f'ERROR - step 260: {e}')

print("STEP 261 - Check element img_261")
try:
    element = driver.find_element(By.TAG_NAME, "img")
    print('PASS - step 261')
except Exception as e:
    print('FAIL - step 261' if isinstance(e, AssertionError) else f'ERROR - step 261: {e}')

print("STEP 262 - Check element div_262")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 262')
except Exception as e:
    print('FAIL - step 262' if isinstance(e, AssertionError) else f'ERROR - step 262: {e}')

print("STEP 263 - Check element div_263")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 263')
except Exception as e:
    print('FAIL - step 263' if isinstance(e, AssertionError) else f'ERROR - step 263: {e}')

print("STEP 264 - Check element div_264")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 264')
except Exception as e:
    print('FAIL - step 264' if isinstance(e, AssertionError) else f'ERROR - step 264: {e}')

print("STEP 265 - Check element ul_265")
try:
    element = driver.find_element(By.TAG_NAME, "ul")
    print('PASS - step 265')
except Exception as e:
    print('FAIL - step 265' if isinstance(e, AssertionError) else f'ERROR - step 265: {e}')

print("STEP 266 - Check element li_266")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 266')
except Exception as e:
    print('FAIL - step 266' if isinstance(e, AssertionError) else f'ERROR - step 266: {e}')

print("STEP 267 - Check element div_267")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 267')
except Exception as e:
    print('FAIL - step 267' if isinstance(e, AssertionError) else f'ERROR - step 267: {e}')

print("STEP 268 - Check element span_268")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 268')
except Exception as e:
    print('FAIL - step 268' if isinstance(e, AssertionError) else f'ERROR - step 268: {e}')

print("STEP 269 - Check element span_269")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 269')
except Exception as e:
    print('FAIL - step 269' if isinstance(e, AssertionError) else f'ERROR - step 269: {e}')

print("STEP 270 - Check element span_270")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 270')
except Exception as e:
    print('FAIL - step 270' if isinstance(e, AssertionError) else f'ERROR - step 270: {e}')

print("STEP 271 - Check element span_271")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 271')
except Exception as e:
    print('FAIL - step 271' if isinstance(e, AssertionError) else f'ERROR - step 271: {e}')

print("STEP 272 - Check element div_272")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 272')
except Exception as e:
    print('FAIL - step 272' if isinstance(e, AssertionError) else f'ERROR - step 272: {e}')

print("STEP 273 - Check element div_273")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 273')
except Exception as e:
    print('FAIL - step 273' if isinstance(e, AssertionError) else f'ERROR - step 273: {e}')

print("STEP 274 - Check element span_274")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 274')
except Exception as e:
    print('FAIL - step 274' if isinstance(e, AssertionError) else f'ERROR - step 274: {e}')

print("STEP 275 - Check element div_275")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 275')
except Exception as e:
    print('FAIL - step 275' if isinstance(e, AssertionError) else f'ERROR - step 275: {e}')

print("STEP 276 - Check element style_276")
try:
    element = driver.find_element(By.TAG_NAME, "style")
    print('PASS - step 276')
except Exception as e:
    print('FAIL - step 276' if isinstance(e, AssertionError) else f'ERROR - step 276: {e}')

print("STEP 277 - Check element div_277")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 277')
except Exception as e:
    print('FAIL - step 277' if isinstance(e, AssertionError) else f'ERROR - step 277: {e}')

print("STEP 278 - Check element div_278")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 278')
except Exception as e:
    print('FAIL - step 278' if isinstance(e, AssertionError) else f'ERROR - step 278: {e}')

print("STEP 279 - Check element h4_279")
try:
    element = driver.find_element(By.TAG_NAME, "h4")
    print('PASS - step 279')
except Exception as e:
    print('FAIL - step 279' if isinstance(e, AssertionError) else f'ERROR - step 279: {e}')

print("STEP 280 - Check element div_280")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 280')
except Exception as e:
    print('FAIL - step 280' if isinstance(e, AssertionError) else f'ERROR - step 280: {e}')

print("STEP 281 - Check element br_281")
try:
    element = driver.find_element(By.TAG_NAME, "br")
    print('PASS - step 281')
except Exception as e:
    print('FAIL - step 281' if isinstance(e, AssertionError) else f'ERROR - step 281: {e}')

print("STEP 282 - Check element div_282")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 282')
except Exception as e:
    print('FAIL - step 282' if isinstance(e, AssertionError) else f'ERROR - step 282: {e}')

print("STEP 283 - Check element h4_283")
try:
    element = driver.find_element(By.TAG_NAME, "h4")
    print('PASS - step 283')
except Exception as e:
    print('FAIL - step 283' if isinstance(e, AssertionError) else f'ERROR - step 283: {e}')

print("STEP 284 - Check element div_284")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 284')
except Exception as e:
    print('FAIL - step 284' if isinstance(e, AssertionError) else f'ERROR - step 284: {e}')

print("STEP 285 - Check element br_285")
try:
    element = driver.find_element(By.TAG_NAME, "br")
    print('PASS - step 285')
except Exception as e:
    print('FAIL - step 285' if isinstance(e, AssertionError) else f'ERROR - step 285: {e}')

print("STEP 286 - Check element br_286")
try:
    element = driver.find_element(By.TAG_NAME, "br")
    print('PASS - step 286')
except Exception as e:
    print('FAIL - step 286' if isinstance(e, AssertionError) else f'ERROR - step 286: {e}')

print("STEP 287 - Check element div_287")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 287')
except Exception as e:
    print('FAIL - step 287' if isinstance(e, AssertionError) else f'ERROR - step 287: {e}')

print("STEP 288 - Check element h4_288")
try:
    element = driver.find_element(By.TAG_NAME, "h4")
    print('PASS - step 288')
except Exception as e:
    print('FAIL - step 288' if isinstance(e, AssertionError) else f'ERROR - step 288: {e}')

print("STEP 289 - Check element div_289")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 289')
except Exception as e:
    print('FAIL - step 289' if isinstance(e, AssertionError) else f'ERROR - step 289: {e}')

print("STEP 290 - Check element br_290")
try:
    element = driver.find_element(By.TAG_NAME, "br")
    print('PASS - step 290')
except Exception as e:
    print('FAIL - step 290' if isinstance(e, AssertionError) else f'ERROR - step 290: {e}')

print("STEP 291 - Check element br_291")
try:
    element = driver.find_element(By.TAG_NAME, "br")
    print('PASS - step 291')
except Exception as e:
    print('FAIL - step 291' if isinstance(e, AssertionError) else f'ERROR - step 291: {e}')

print("STEP 292 - Check element div_292")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 292')
except Exception as e:
    print('FAIL - step 292' if isinstance(e, AssertionError) else f'ERROR - step 292: {e}')

print("STEP 293 - Check element div_293")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 293')
except Exception as e:
    print('FAIL - step 293' if isinstance(e, AssertionError) else f'ERROR - step 293: {e}')

print("STEP 294 - Check element ul_294")
try:
    element = driver.find_element(By.TAG_NAME, "ul")
    print('PASS - step 294')
except Exception as e:
    print('FAIL - step 294' if isinstance(e, AssertionError) else f'ERROR - step 294: {e}')

print("STEP 295 - Check element li_295")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 295')
except Exception as e:
    print('FAIL - step 295' if isinstance(e, AssertionError) else f'ERROR - step 295: {e}')

print("STEP 296 - Check element a_296")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 296')
except Exception as e:
    print('FAIL - step 296' if isinstance(e, AssertionError) else f'ERROR - step 296: {e}')

print("STEP 297 - Check element div_297")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 297')
except Exception as e:
    print('FAIL - step 297' if isinstance(e, AssertionError) else f'ERROR - step 297: {e}')

print("STEP 298 - Check element span_298")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 298')
except Exception as e:
    print('FAIL - step 298' if isinstance(e, AssertionError) else f'ERROR - step 298: {e}')

print("STEP 299 - Check element p_299")
try:
    element = driver.find_element(By.TAG_NAME, "p")
    print('PASS - step 299')
except Exception as e:
    print('FAIL - step 299' if isinstance(e, AssertionError) else f'ERROR - step 299: {e}')

print("STEP 300 - Check element div_300")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 300')
except Exception as e:
    print('FAIL - step 300' if isinstance(e, AssertionError) else f'ERROR - step 300: {e}')

print("STEP 301 - Check element div_301")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 301')
except Exception as e:
    print('FAIL - step 301' if isinstance(e, AssertionError) else f'ERROR - step 301: {e}')

print("STEP 302 - Check element ul_302")
try:
    element = driver.find_element(By.TAG_NAME, "ul")
    print('PASS - step 302')
except Exception as e:
    print('FAIL - step 302' if isinstance(e, AssertionError) else f'ERROR - step 302: {e}')

print("STEP 303 - Check element li_303")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 303')
except Exception as e:
    print('FAIL - step 303' if isinstance(e, AssertionError) else f'ERROR - step 303: {e}')

print("STEP 304 - Check element div_304")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 304')
except Exception as e:
    print('FAIL - step 304' if isinstance(e, AssertionError) else f'ERROR - step 304: {e}')

print("STEP 305 - Check element span_305")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 305')
except Exception as e:
    print('FAIL - step 305' if isinstance(e, AssertionError) else f'ERROR - step 305: {e}')

print("STEP 306 - Check element strong_306")
try:
    element = driver.find_element(By.TAG_NAME, "strong")
    print('PASS - step 306')
except Exception as e:
    print('FAIL - step 306' if isinstance(e, AssertionError) else f'ERROR - step 306: {e}')

print("STEP 307 - Check element a_307")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 307')
except Exception as e:
    print('FAIL - step 307' if isinstance(e, AssertionError) else f'ERROR - step 307: {e}')

print("STEP 308 - Check element span_308")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 308')
except Exception as e:
    print('FAIL - step 308' if isinstance(e, AssertionError) else f'ERROR - step 308: {e}')

print("STEP 309 - Check element a_309")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 309')
except Exception as e:
    print('FAIL - step 309' if isinstance(e, AssertionError) else f'ERROR - step 309: {e}')

print("STEP 310 - Check element span_310")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 310')
except Exception as e:
    print('FAIL - step 310' if isinstance(e, AssertionError) else f'ERROR - step 310: {e}')

print("STEP 311 - Check element a_311")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 311')
except Exception as e:
    print('FAIL - step 311' if isinstance(e, AssertionError) else f'ERROR - step 311: {e}')

print("STEP 312 - Check element span_312")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 312')
except Exception as e:
    print('FAIL - step 312' if isinstance(e, AssertionError) else f'ERROR - step 312: {e}')

print("STEP 313 - Check element a_313")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 313')
except Exception as e:
    print('FAIL - step 313' if isinstance(e, AssertionError) else f'ERROR - step 313: {e}')

print("STEP 314 - Check element span_314")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 314')
except Exception as e:
    print('FAIL - step 314' if isinstance(e, AssertionError) else f'ERROR - step 314: {e}')

print("STEP 315 - Check element a_315")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 315')
except Exception as e:
    print('FAIL - step 315' if isinstance(e, AssertionError) else f'ERROR - step 315: {e}')

print("STEP 316 - Check element span_316")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 316')
except Exception as e:
    print('FAIL - step 316' if isinstance(e, AssertionError) else f'ERROR - step 316: {e}')

print("STEP 317 - Check element a_317")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 317')
except Exception as e:
    print('FAIL - step 317' if isinstance(e, AssertionError) else f'ERROR - step 317: {e}')

print("STEP 318 - Check element span_318")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 318')
except Exception as e:
    print('FAIL - step 318' if isinstance(e, AssertionError) else f'ERROR - step 318: {e}')

print("STEP 319 - Check element li_319")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 319')
except Exception as e:
    print('FAIL - step 319' if isinstance(e, AssertionError) else f'ERROR - step 319: {e}')

print("STEP 320 - Check element div_320")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 320')
except Exception as e:
    print('FAIL - step 320' if isinstance(e, AssertionError) else f'ERROR - step 320: {e}')

print("STEP 321 - Check element span_321")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 321')
except Exception as e:
    print('FAIL - step 321' if isinstance(e, AssertionError) else f'ERROR - step 321: {e}')

print("STEP 322 - Check element strong_322")
try:
    element = driver.find_element(By.TAG_NAME, "strong")
    print('PASS - step 322')
except Exception as e:
    print('FAIL - step 322' if isinstance(e, AssertionError) else f'ERROR - step 322: {e}')

print("STEP 323 - Check element a_323")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 323')
except Exception as e:
    print('FAIL - step 323' if isinstance(e, AssertionError) else f'ERROR - step 323: {e}')

print("STEP 324 - Check element span_324")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 324')
except Exception as e:
    print('FAIL - step 324' if isinstance(e, AssertionError) else f'ERROR - step 324: {e}')

print("STEP 325 - Check element a_325")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 325')
except Exception as e:
    print('FAIL - step 325' if isinstance(e, AssertionError) else f'ERROR - step 325: {e}')

print("STEP 326 - Check element span_326")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 326')
except Exception as e:
    print('FAIL - step 326' if isinstance(e, AssertionError) else f'ERROR - step 326: {e}')

print("STEP 327 - Check element a_327")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 327')
except Exception as e:
    print('FAIL - step 327' if isinstance(e, AssertionError) else f'ERROR - step 327: {e}')

print("STEP 328 - Check element span_328")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 328')
except Exception as e:
    print('FAIL - step 328' if isinstance(e, AssertionError) else f'ERROR - step 328: {e}')

print("STEP 329 - Check element a_329")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 329')
except Exception as e:
    print('FAIL - step 329' if isinstance(e, AssertionError) else f'ERROR - step 329: {e}')

print("STEP 330 - Check element span_330")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 330')
except Exception as e:
    print('FAIL - step 330' if isinstance(e, AssertionError) else f'ERROR - step 330: {e}')

print("STEP 331 - Check element a_331")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 331')
except Exception as e:
    print('FAIL - step 331' if isinstance(e, AssertionError) else f'ERROR - step 331: {e}')

print("STEP 332 - Check element span_332")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 332')
except Exception as e:
    print('FAIL - step 332' if isinstance(e, AssertionError) else f'ERROR - step 332: {e}')

print("STEP 333 - Check element a_333")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 333')
except Exception as e:
    print('FAIL - step 333' if isinstance(e, AssertionError) else f'ERROR - step 333: {e}')

print("STEP 334 - Check element span_334")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 334')
except Exception as e:
    print('FAIL - step 334' if isinstance(e, AssertionError) else f'ERROR - step 334: {e}')

print("STEP 335 - Check element li_335")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 335')
except Exception as e:
    print('FAIL - step 335' if isinstance(e, AssertionError) else f'ERROR - step 335: {e}')

print("STEP 336 - Check element li_336")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 336')
except Exception as e:
    print('FAIL - step 336' if isinstance(e, AssertionError) else f'ERROR - step 336: {e}')

print("STEP 337 - Check element li_337")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 337')
except Exception as e:
    print('FAIL - step 337' if isinstance(e, AssertionError) else f'ERROR - step 337: {e}')

print("STEP 338 - Check element a_338")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 338')
except Exception as e:
    print('FAIL - step 338' if isinstance(e, AssertionError) else f'ERROR - step 338: {e}')

print("STEP 339 - Check element div_339")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 339')
except Exception as e:
    print('FAIL - step 339' if isinstance(e, AssertionError) else f'ERROR - step 339: {e}')

print("STEP 340 - Check element span_340")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 340')
except Exception as e:
    print('FAIL - step 340' if isinstance(e, AssertionError) else f'ERROR - step 340: {e}')

print("STEP 341 - Check element p_341")
try:
    element = driver.find_element(By.TAG_NAME, "p")
    print('PASS - step 341')
except Exception as e:
    print('FAIL - step 341' if isinstance(e, AssertionError) else f'ERROR - step 341: {e}')

print("STEP 342 - Check element div_342")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 342')
except Exception as e:
    print('FAIL - step 342' if isinstance(e, AssertionError) else f'ERROR - step 342: {e}')

print("STEP 343 - Check element div_343")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 343')
except Exception as e:
    print('FAIL - step 343' if isinstance(e, AssertionError) else f'ERROR - step 343: {e}')

print("STEP 344 - Check element ul_344")
try:
    element = driver.find_element(By.TAG_NAME, "ul")
    print('PASS - step 344')
except Exception as e:
    print('FAIL - step 344' if isinstance(e, AssertionError) else f'ERROR - step 344: {e}')

print("STEP 345 - Check element li_345")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 345')
except Exception as e:
    print('FAIL - step 345' if isinstance(e, AssertionError) else f'ERROR - step 345: {e}')

print("STEP 346 - Check element div_346")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 346')
except Exception as e:
    print('FAIL - step 346' if isinstance(e, AssertionError) else f'ERROR - step 346: {e}')

print("STEP 347 - Check element span_347")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 347')
except Exception as e:
    print('FAIL - step 347' if isinstance(e, AssertionError) else f'ERROR - step 347: {e}')

print("STEP 348 - Check element strong_348")
try:
    element = driver.find_element(By.TAG_NAME, "strong")
    print('PASS - step 348')
except Exception as e:
    print('FAIL - step 348' if isinstance(e, AssertionError) else f'ERROR - step 348: {e}')

print("STEP 349 - Check element a_349")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 349')
except Exception as e:
    print('FAIL - step 349' if isinstance(e, AssertionError) else f'ERROR - step 349: {e}')

print("STEP 350 - Check element span_350")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 350')
except Exception as e:
    print('FAIL - step 350' if isinstance(e, AssertionError) else f'ERROR - step 350: {e}')

print("STEP 351 - Check element a_351")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 351')
except Exception as e:
    print('FAIL - step 351' if isinstance(e, AssertionError) else f'ERROR - step 351: {e}')

print("STEP 352 - Check element span_352")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 352')
except Exception as e:
    print('FAIL - step 352' if isinstance(e, AssertionError) else f'ERROR - step 352: {e}')

print("STEP 353 - Check element a_353")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 353')
except Exception as e:
    print('FAIL - step 353' if isinstance(e, AssertionError) else f'ERROR - step 353: {e}')

print("STEP 354 - Check element span_354")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 354')
except Exception as e:
    print('FAIL - step 354' if isinstance(e, AssertionError) else f'ERROR - step 354: {e}')

print("STEP 355 - Check element a_355")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 355')
except Exception as e:
    print('FAIL - step 355' if isinstance(e, AssertionError) else f'ERROR - step 355: {e}')

print("STEP 356 - Check element span_356")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 356')
except Exception as e:
    print('FAIL - step 356' if isinstance(e, AssertionError) else f'ERROR - step 356: {e}')

print("STEP 357 - Check element li_357")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 357')
except Exception as e:
    print('FAIL - step 357' if isinstance(e, AssertionError) else f'ERROR - step 357: {e}')

print("STEP 358 - Check element div_358")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 358')
except Exception as e:
    print('FAIL - step 358' if isinstance(e, AssertionError) else f'ERROR - step 358: {e}')

print("STEP 359 - Check element span_359")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 359')
except Exception as e:
    print('FAIL - step 359' if isinstance(e, AssertionError) else f'ERROR - step 359: {e}')

print("STEP 360 - Check element strong_360")
try:
    element = driver.find_element(By.TAG_NAME, "strong")
    print('PASS - step 360')
except Exception as e:
    print('FAIL - step 360' if isinstance(e, AssertionError) else f'ERROR - step 360: {e}')

print("STEP 361 - Check element a_361")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 361')
except Exception as e:
    print('FAIL - step 361' if isinstance(e, AssertionError) else f'ERROR - step 361: {e}')

print("STEP 362 - Check element span_362")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 362')
except Exception as e:
    print('FAIL - step 362' if isinstance(e, AssertionError) else f'ERROR - step 362: {e}')

print("STEP 363 - Check element a_363")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 363')
except Exception as e:
    print('FAIL - step 363' if isinstance(e, AssertionError) else f'ERROR - step 363: {e}')

print("STEP 364 - Check element span_364")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 364')
except Exception as e:
    print('FAIL - step 364' if isinstance(e, AssertionError) else f'ERROR - step 364: {e}')

print("STEP 365 - Check element a_365")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 365')
except Exception as e:
    print('FAIL - step 365' if isinstance(e, AssertionError) else f'ERROR - step 365: {e}')

print("STEP 366 - Check element span_366")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 366')
except Exception as e:
    print('FAIL - step 366' if isinstance(e, AssertionError) else f'ERROR - step 366: {e}')

print("STEP 367 - Check element li_367")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 367')
except Exception as e:
    print('FAIL - step 367' if isinstance(e, AssertionError) else f'ERROR - step 367: {e}')

print("STEP 368 - Check element li_368")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 368')
except Exception as e:
    print('FAIL - step 368' if isinstance(e, AssertionError) else f'ERROR - step 368: {e}')

print("STEP 369 - Check element li_369")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 369')
except Exception as e:
    print('FAIL - step 369' if isinstance(e, AssertionError) else f'ERROR - step 369: {e}')

print("STEP 370 - Check element a_370")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 370')
except Exception as e:
    print('FAIL - step 370' if isinstance(e, AssertionError) else f'ERROR - step 370: {e}')

print("STEP 371 - Check element div_371")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 371')
except Exception as e:
    print('FAIL - step 371' if isinstance(e, AssertionError) else f'ERROR - step 371: {e}')

print("STEP 372 - Check element span_372")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 372')
except Exception as e:
    print('FAIL - step 372' if isinstance(e, AssertionError) else f'ERROR - step 372: {e}')

print("STEP 373 - Check element p_373")
try:
    element = driver.find_element(By.TAG_NAME, "p")
    print('PASS - step 373')
except Exception as e:
    print('FAIL - step 373' if isinstance(e, AssertionError) else f'ERROR - step 373: {e}')

print("STEP 374 - Check element div_374")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 374')
except Exception as e:
    print('FAIL - step 374' if isinstance(e, AssertionError) else f'ERROR - step 374: {e}')

print("STEP 375 - Check element div_375")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 375')
except Exception as e:
    print('FAIL - step 375' if isinstance(e, AssertionError) else f'ERROR - step 375: {e}')

print("STEP 376 - Check element ul_376")
try:
    element = driver.find_element(By.TAG_NAME, "ul")
    print('PASS - step 376')
except Exception as e:
    print('FAIL - step 376' if isinstance(e, AssertionError) else f'ERROR - step 376: {e}')

print("STEP 377 - Check element li_377")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 377')
except Exception as e:
    print('FAIL - step 377' if isinstance(e, AssertionError) else f'ERROR - step 377: {e}')

print("STEP 378 - Check element div_378")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 378')
except Exception as e:
    print('FAIL - step 378' if isinstance(e, AssertionError) else f'ERROR - step 378: {e}')

print("STEP 379 - Check element span_379")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 379')
except Exception as e:
    print('FAIL - step 379' if isinstance(e, AssertionError) else f'ERROR - step 379: {e}')

print("STEP 380 - Check element strong_380")
try:
    element = driver.find_element(By.TAG_NAME, "strong")
    print('PASS - step 380')
except Exception as e:
    print('FAIL - step 380' if isinstance(e, AssertionError) else f'ERROR - step 380: {e}')

print("STEP 381 - Check element a_381")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 381')
except Exception as e:
    print('FAIL - step 381' if isinstance(e, AssertionError) else f'ERROR - step 381: {e}')

print("STEP 382 - Check element span_382")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 382')
except Exception as e:
    print('FAIL - step 382' if isinstance(e, AssertionError) else f'ERROR - step 382: {e}')

print("STEP 383 - Check element a_383")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 383')
except Exception as e:
    print('FAIL - step 383' if isinstance(e, AssertionError) else f'ERROR - step 383: {e}')

print("STEP 384 - Check element span_384")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 384')
except Exception as e:
    print('FAIL - step 384' if isinstance(e, AssertionError) else f'ERROR - step 384: {e}')

print("STEP 385 - Check element a_385")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 385')
except Exception as e:
    print('FAIL - step 385' if isinstance(e, AssertionError) else f'ERROR - step 385: {e}')

print("STEP 386 - Check element span_386")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 386')
except Exception as e:
    print('FAIL - step 386' if isinstance(e, AssertionError) else f'ERROR - step 386: {e}')

print("STEP 387 - Check element li_387")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 387')
except Exception as e:
    print('FAIL - step 387' if isinstance(e, AssertionError) else f'ERROR - step 387: {e}')

print("STEP 388 - Check element div_388")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 388')
except Exception as e:
    print('FAIL - step 388' if isinstance(e, AssertionError) else f'ERROR - step 388: {e}')

print("STEP 389 - Check element span_389")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 389')
except Exception as e:
    print('FAIL - step 389' if isinstance(e, AssertionError) else f'ERROR - step 389: {e}')

print("STEP 390 - Check element strong_390")
try:
    element = driver.find_element(By.TAG_NAME, "strong")
    print('PASS - step 390')
except Exception as e:
    print('FAIL - step 390' if isinstance(e, AssertionError) else f'ERROR - step 390: {e}')

print("STEP 391 - Check element a_391")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 391')
except Exception as e:
    print('FAIL - step 391' if isinstance(e, AssertionError) else f'ERROR - step 391: {e}')

print("STEP 392 - Check element span_392")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 392')
except Exception as e:
    print('FAIL - step 392' if isinstance(e, AssertionError) else f'ERROR - step 392: {e}')

print("STEP 393 - Check element a_393")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 393')
except Exception as e:
    print('FAIL - step 393' if isinstance(e, AssertionError) else f'ERROR - step 393: {e}')

print("STEP 394 - Check element span_394")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 394')
except Exception as e:
    print('FAIL - step 394' if isinstance(e, AssertionError) else f'ERROR - step 394: {e}')

print("STEP 395 - Check element li_395")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 395')
except Exception as e:
    print('FAIL - step 395' if isinstance(e, AssertionError) else f'ERROR - step 395: {e}')

print("STEP 396 - Check element li_396")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 396')
except Exception as e:
    print('FAIL - step 396' if isinstance(e, AssertionError) else f'ERROR - step 396: {e}')

print("STEP 397 - Check element li_397")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 397')
except Exception as e:
    print('FAIL - step 397' if isinstance(e, AssertionError) else f'ERROR - step 397: {e}')

print("STEP 398 - Check element a_398")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 398')
except Exception as e:
    print('FAIL - step 398' if isinstance(e, AssertionError) else f'ERROR - step 398: {e}')

print("STEP 399 - Check element div_399")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 399')
except Exception as e:
    print('FAIL - step 399' if isinstance(e, AssertionError) else f'ERROR - step 399: {e}')

print("STEP 400 - Check element span_400")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 400')
except Exception as e:
    print('FAIL - step 400' if isinstance(e, AssertionError) else f'ERROR - step 400: {e}')

print("STEP 401 - Check element p_401")
try:
    element = driver.find_element(By.TAG_NAME, "p")
    print('PASS - step 401')
except Exception as e:
    print('FAIL - step 401' if isinstance(e, AssertionError) else f'ERROR - step 401: {e}')

print("STEP 402 - Check element div_402")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 402')
except Exception as e:
    print('FAIL - step 402' if isinstance(e, AssertionError) else f'ERROR - step 402: {e}')

print("STEP 403 - Check element div_403")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 403')
except Exception as e:
    print('FAIL - step 403' if isinstance(e, AssertionError) else f'ERROR - step 403: {e}')

print("STEP 404 - Check element ul_404")
try:
    element = driver.find_element(By.TAG_NAME, "ul")
    print('PASS - step 404')
except Exception as e:
    print('FAIL - step 404' if isinstance(e, AssertionError) else f'ERROR - step 404: {e}')

print("STEP 405 - Check element li_405")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 405')
except Exception as e:
    print('FAIL - step 405' if isinstance(e, AssertionError) else f'ERROR - step 405: {e}')

print("STEP 406 - Check element div_406")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 406')
except Exception as e:
    print('FAIL - step 406' if isinstance(e, AssertionError) else f'ERROR - step 406: {e}')

print("STEP 407 - Check element span_407")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 407')
except Exception as e:
    print('FAIL - step 407' if isinstance(e, AssertionError) else f'ERROR - step 407: {e}')

print("STEP 408 - Check element strong_408")
try:
    element = driver.find_element(By.TAG_NAME, "strong")
    print('PASS - step 408')
except Exception as e:
    print('FAIL - step 408' if isinstance(e, AssertionError) else f'ERROR - step 408: {e}')

print("STEP 409 - Check element a_409")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 409')
except Exception as e:
    print('FAIL - step 409' if isinstance(e, AssertionError) else f'ERROR - step 409: {e}')

print("STEP 410 - Check element span_410")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 410')
except Exception as e:
    print('FAIL - step 410' if isinstance(e, AssertionError) else f'ERROR - step 410: {e}')

print("STEP 411 - Check element li_411")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 411')
except Exception as e:
    print('FAIL - step 411' if isinstance(e, AssertionError) else f'ERROR - step 411: {e}')

print("STEP 412 - Check element li_412")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 412')
except Exception as e:
    print('FAIL - step 412' if isinstance(e, AssertionError) else f'ERROR - step 412: {e}')

print("STEP 413 - Check element a_413")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 413')
except Exception as e:
    print('FAIL - step 413' if isinstance(e, AssertionError) else f'ERROR - step 413: {e}')

print("STEP 414 - Check element div_414")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 414')
except Exception as e:
    print('FAIL - step 414' if isinstance(e, AssertionError) else f'ERROR - step 414: {e}')

print("STEP 415 - Check element span_415")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 415')
except Exception as e:
    print('FAIL - step 415' if isinstance(e, AssertionError) else f'ERROR - step 415: {e}')

print("STEP 416 - Check element li_416")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 416')
except Exception as e:
    print('FAIL - step 416' if isinstance(e, AssertionError) else f'ERROR - step 416: {e}')

print("STEP 417 - Check element a_417")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 417')
except Exception as e:
    print('FAIL - step 417' if isinstance(e, AssertionError) else f'ERROR - step 417: {e}')

print("STEP 418 - Check element div_418")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 418')
except Exception as e:
    print('FAIL - step 418' if isinstance(e, AssertionError) else f'ERROR - step 418: {e}')

print("STEP 419 - Check element span_419")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 419')
except Exception as e:
    print('FAIL - step 419' if isinstance(e, AssertionError) else f'ERROR - step 419: {e}')

print("STEP 420 - Check element div_420")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 420')
except Exception as e:
    print('FAIL - step 420' if isinstance(e, AssertionError) else f'ERROR - step 420: {e}')

print("STEP 421 - Check element div_421")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 421')
except Exception as e:
    print('FAIL - step 421' if isinstance(e, AssertionError) else f'ERROR - step 421: {e}')

print("STEP 422 - Check element ul_422")
try:
    element = driver.find_element(By.TAG_NAME, "ul")
    print('PASS - step 422')
except Exception as e:
    print('FAIL - step 422' if isinstance(e, AssertionError) else f'ERROR - step 422: {e}')

print("STEP 423 - Check element li_423")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 423')
except Exception as e:
    print('FAIL - step 423' if isinstance(e, AssertionError) else f'ERROR - step 423: {e}')

print("STEP 424 - Check element div_424")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 424')
except Exception as e:
    print('FAIL - step 424' if isinstance(e, AssertionError) else f'ERROR - step 424: {e}')

print("STEP 425 - Check element span_425")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 425')
except Exception as e:
    print('FAIL - step 425' if isinstance(e, AssertionError) else f'ERROR - step 425: {e}')

print("STEP 426 - Check element a_426")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 426')
except Exception as e:
    print('FAIL - step 426' if isinstance(e, AssertionError) else f'ERROR - step 426: {e}')

print("STEP 427 - Check element span_427")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 427')
except Exception as e:
    print('FAIL - step 427' if isinstance(e, AssertionError) else f'ERROR - step 427: {e}')

print("STEP 428 - Check element a_428")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 428')
except Exception as e:
    print('FAIL - step 428' if isinstance(e, AssertionError) else f'ERROR - step 428: {e}')

print("STEP 429 - Check element span_429")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 429')
except Exception as e:
    print('FAIL - step 429' if isinstance(e, AssertionError) else f'ERROR - step 429: {e}')

print("STEP 430 - Check element a_430")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 430')
except Exception as e:
    print('FAIL - step 430' if isinstance(e, AssertionError) else f'ERROR - step 430: {e}')

print("STEP 431 - Check element span_431")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 431')
except Exception as e:
    print('FAIL - step 431' if isinstance(e, AssertionError) else f'ERROR - step 431: {e}')

print("STEP 432 - Check element a_432")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 432')
except Exception as e:
    print('FAIL - step 432' if isinstance(e, AssertionError) else f'ERROR - step 432: {e}')

print("STEP 433 - Check element span_433")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 433')
except Exception as e:
    print('FAIL - step 433' if isinstance(e, AssertionError) else f'ERROR - step 433: {e}')

print("STEP 434 - Check element a_434")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 434')
except Exception as e:
    print('FAIL - step 434' if isinstance(e, AssertionError) else f'ERROR - step 434: {e}')

print("STEP 435 - Check element span_435")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 435')
except Exception as e:
    print('FAIL - step 435' if isinstance(e, AssertionError) else f'ERROR - step 435: {e}')

print("STEP 436 - Check element li_436")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 436')
except Exception as e:
    print('FAIL - step 436' if isinstance(e, AssertionError) else f'ERROR - step 436: {e}')

print("STEP 437 - Check element div_437")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 437')
except Exception as e:
    print('FAIL - step 437' if isinstance(e, AssertionError) else f'ERROR - step 437: {e}')

print("STEP 438 - Check element span_438")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 438')
except Exception as e:
    print('FAIL - step 438' if isinstance(e, AssertionError) else f'ERROR - step 438: {e}')

print("STEP 439 - Check element a_439")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 439')
except Exception as e:
    print('FAIL - step 439' if isinstance(e, AssertionError) else f'ERROR - step 439: {e}')

print("STEP 440 - Check element span_440")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 440')
except Exception as e:
    print('FAIL - step 440' if isinstance(e, AssertionError) else f'ERROR - step 440: {e}')

print("STEP 441 - Check element a_441")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 441')
except Exception as e:
    print('FAIL - step 441' if isinstance(e, AssertionError) else f'ERROR - step 441: {e}')

print("STEP 442 - Check element span_442")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 442')
except Exception as e:
    print('FAIL - step 442' if isinstance(e, AssertionError) else f'ERROR - step 442: {e}')

print("STEP 443 - Check element a_443")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 443')
except Exception as e:
    print('FAIL - step 443' if isinstance(e, AssertionError) else f'ERROR - step 443: {e}')

print("STEP 444 - Check element span_444")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 444')
except Exception as e:
    print('FAIL - step 444' if isinstance(e, AssertionError) else f'ERROR - step 444: {e}')

print("STEP 445 - Check element a_445")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 445')
except Exception as e:
    print('FAIL - step 445' if isinstance(e, AssertionError) else f'ERROR - step 445: {e}')

print("STEP 446 - Check element span_446")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 446')
except Exception as e:
    print('FAIL - step 446' if isinstance(e, AssertionError) else f'ERROR - step 446: {e}')

print("STEP 447 - Check element a_447")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 447')
except Exception as e:
    print('FAIL - step 447' if isinstance(e, AssertionError) else f'ERROR - step 447: {e}')

print("STEP 448 - Check element span_448")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 448')
except Exception as e:
    print('FAIL - step 448' if isinstance(e, AssertionError) else f'ERROR - step 448: {e}')

print("STEP 449 - Check element li_449")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 449')
except Exception as e:
    print('FAIL - step 449' if isinstance(e, AssertionError) else f'ERROR - step 449: {e}')

print("STEP 450 - Check element li_450")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 450')
except Exception as e:
    print('FAIL - step 450' if isinstance(e, AssertionError) else f'ERROR - step 450: {e}')

print("STEP 451 - Check element li_451")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 451')
except Exception as e:
    print('FAIL - step 451' if isinstance(e, AssertionError) else f'ERROR - step 451: {e}')

print("STEP 452 - Check element a_452")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 452')
except Exception as e:
    print('FAIL - step 452' if isinstance(e, AssertionError) else f'ERROR - step 452: {e}')

print("STEP 453 - Check element div_453")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 453')
except Exception as e:
    print('FAIL - step 453' if isinstance(e, AssertionError) else f'ERROR - step 453: {e}')

print("STEP 454 - Check element span_454")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 454')
except Exception as e:
    print('FAIL - step 454' if isinstance(e, AssertionError) else f'ERROR - step 454: {e}')

print("STEP 455 - Check element div_455")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 455')
except Exception as e:
    print('FAIL - step 455' if isinstance(e, AssertionError) else f'ERROR - step 455: {e}')

print("STEP 456 - Check element div_456")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 456')
except Exception as e:
    print('FAIL - step 456' if isinstance(e, AssertionError) else f'ERROR - step 456: {e}')

print("STEP 457 - Check element ul_457")
try:
    element = driver.find_element(By.TAG_NAME, "ul")
    print('PASS - step 457')
except Exception as e:
    print('FAIL - step 457' if isinstance(e, AssertionError) else f'ERROR - step 457: {e}')

print("STEP 458 - Check element li_458")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 458')
except Exception as e:
    print('FAIL - step 458' if isinstance(e, AssertionError) else f'ERROR - step 458: {e}')

print("STEP 459 - Check element a_459")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 459')
except Exception as e:
    print('FAIL - step 459' if isinstance(e, AssertionError) else f'ERROR - step 459: {e}')

print("STEP 460 - Check element span_460")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 460')
except Exception as e:
    print('FAIL - step 460' if isinstance(e, AssertionError) else f'ERROR - step 460: {e}')

print("STEP 461 - Check element strong_461")
try:
    element = driver.find_element(By.TAG_NAME, "strong")
    print('PASS - step 461')
except Exception as e:
    print('FAIL - step 461' if isinstance(e, AssertionError) else f'ERROR - step 461: {e}')

print("STEP 462 - Check element a_462")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 462')
except Exception as e:
    print('FAIL - step 462' if isinstance(e, AssertionError) else f'ERROR - step 462: {e}')

print("STEP 463 - Check element span_463")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 463')
except Exception as e:
    print('FAIL - step 463' if isinstance(e, AssertionError) else f'ERROR - step 463: {e}')

print("STEP 464 - Check element a_464")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 464')
except Exception as e:
    print('FAIL - step 464' if isinstance(e, AssertionError) else f'ERROR - step 464: {e}')

print("STEP 465 - Check element span_465")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 465')
except Exception as e:
    print('FAIL - step 465' if isinstance(e, AssertionError) else f'ERROR - step 465: {e}')

print("STEP 466 - Check element a_466")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 466')
except Exception as e:
    print('FAIL - step 466' if isinstance(e, AssertionError) else f'ERROR - step 466: {e}')

print("STEP 467 - Check element span_467")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 467')
except Exception as e:
    print('FAIL - step 467' if isinstance(e, AssertionError) else f'ERROR - step 467: {e}')

print("STEP 468 - Check element a_468")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 468')
except Exception as e:
    print('FAIL - step 468' if isinstance(e, AssertionError) else f'ERROR - step 468: {e}')

print("STEP 469 - Check element span_469")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 469')
except Exception as e:
    print('FAIL - step 469' if isinstance(e, AssertionError) else f'ERROR - step 469: {e}')

print("STEP 470 - Check element a_470")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 470')
except Exception as e:
    print('FAIL - step 470' if isinstance(e, AssertionError) else f'ERROR - step 470: {e}')

print("STEP 471 - Check element span_471")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 471')
except Exception as e:
    print('FAIL - step 471' if isinstance(e, AssertionError) else f'ERROR - step 471: {e}')

print("STEP 472 - Check element a_472")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 472')
except Exception as e:
    print('FAIL - step 472' if isinstance(e, AssertionError) else f'ERROR - step 472: {e}')

print("STEP 473 - Check element span_473")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 473')
except Exception as e:
    print('FAIL - step 473' if isinstance(e, AssertionError) else f'ERROR - step 473: {e}')

print("STEP 474 - Check element a_474")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 474')
except Exception as e:
    print('FAIL - step 474' if isinstance(e, AssertionError) else f'ERROR - step 474: {e}')

print("STEP 475 - Check element span_475")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 475')
except Exception as e:
    print('FAIL - step 475' if isinstance(e, AssertionError) else f'ERROR - step 475: {e}')

print("STEP 476 - Check element a_476")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 476')
except Exception as e:
    print('FAIL - step 476' if isinstance(e, AssertionError) else f'ERROR - step 476: {e}')

print("STEP 477 - Check element span_477")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 477')
except Exception as e:
    print('FAIL - step 477' if isinstance(e, AssertionError) else f'ERROR - step 477: {e}')

print("STEP 478 - Check element a_478")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 478')
except Exception as e:
    print('FAIL - step 478' if isinstance(e, AssertionError) else f'ERROR - step 478: {e}')

print("STEP 479 - Check element span_479")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 479')
except Exception as e:
    print('FAIL - step 479' if isinstance(e, AssertionError) else f'ERROR - step 479: {e}')

print("STEP 480 - Check element li_480")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 480')
except Exception as e:
    print('FAIL - step 480' if isinstance(e, AssertionError) else f'ERROR - step 480: {e}')

print("STEP 481 - Check element div_481")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 481')
except Exception as e:
    print('FAIL - step 481' if isinstance(e, AssertionError) else f'ERROR - step 481: {e}')

print("STEP 482 - Check element span_482")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 482')
except Exception as e:
    print('FAIL - step 482' if isinstance(e, AssertionError) else f'ERROR - step 482: {e}')

print("STEP 483 - Check element strong_483")
try:
    element = driver.find_element(By.TAG_NAME, "strong")
    print('PASS - step 483')
except Exception as e:
    print('FAIL - step 483' if isinstance(e, AssertionError) else f'ERROR - step 483: {e}')

print("STEP 484 - Check element a_484")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 484')
except Exception as e:
    print('FAIL - step 484' if isinstance(e, AssertionError) else f'ERROR - step 484: {e}')

print("STEP 485 - Check element span_485")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 485')
except Exception as e:
    print('FAIL - step 485' if isinstance(e, AssertionError) else f'ERROR - step 485: {e}')

print("STEP 486 - Check element a_486")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 486')
except Exception as e:
    print('FAIL - step 486' if isinstance(e, AssertionError) else f'ERROR - step 486: {e}')

print("STEP 487 - Check element span_487")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 487')
except Exception as e:
    print('FAIL - step 487' if isinstance(e, AssertionError) else f'ERROR - step 487: {e}')

print("STEP 488 - Check element a_488")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 488')
except Exception as e:
    print('FAIL - step 488' if isinstance(e, AssertionError) else f'ERROR - step 488: {e}')

print("STEP 489 - Check element span_489")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 489')
except Exception as e:
    print('FAIL - step 489' if isinstance(e, AssertionError) else f'ERROR - step 489: {e}')

print("STEP 490 - Check element strong_490")
try:
    element = driver.find_element(By.TAG_NAME, "strong")
    print('PASS - step 490')
except Exception as e:
    print('FAIL - step 490' if isinstance(e, AssertionError) else f'ERROR - step 490: {e}')

print("STEP 491 - Check element a_491")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 491')
except Exception as e:
    print('FAIL - step 491' if isinstance(e, AssertionError) else f'ERROR - step 491: {e}')

print("STEP 492 - Check element span_492")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 492')
except Exception as e:
    print('FAIL - step 492' if isinstance(e, AssertionError) else f'ERROR - step 492: {e}')

print("STEP 493 - Check element a_493")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 493')
except Exception as e:
    print('FAIL - step 493' if isinstance(e, AssertionError) else f'ERROR - step 493: {e}')

print("STEP 494 - Check element span_494")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 494')
except Exception as e:
    print('FAIL - step 494' if isinstance(e, AssertionError) else f'ERROR - step 494: {e}')

print("STEP 495 - Check element a_495")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 495')
except Exception as e:
    print('FAIL - step 495' if isinstance(e, AssertionError) else f'ERROR - step 495: {e}')

print("STEP 496 - Check element span_496")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 496')
except Exception as e:
    print('FAIL - step 496' if isinstance(e, AssertionError) else f'ERROR - step 496: {e}')

print("STEP 497 - Check element a_497")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 497')
except Exception as e:
    print('FAIL - step 497' if isinstance(e, AssertionError) else f'ERROR - step 497: {e}')

print("STEP 498 - Check element span_498")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 498')
except Exception as e:
    print('FAIL - step 498' if isinstance(e, AssertionError) else f'ERROR - step 498: {e}')

print("STEP 499 - Check element a_499")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 499')
except Exception as e:
    print('FAIL - step 499' if isinstance(e, AssertionError) else f'ERROR - step 499: {e}')

print("STEP 500 - Check element span_500")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 500')
except Exception as e:
    print('FAIL - step 500' if isinstance(e, AssertionError) else f'ERROR - step 500: {e}')

print("STEP 501 - Check element a_501")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 501')
except Exception as e:
    print('FAIL - step 501' if isinstance(e, AssertionError) else f'ERROR - step 501: {e}')

print("STEP 502 - Check element span_502")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 502')
except Exception as e:
    print('FAIL - step 502' if isinstance(e, AssertionError) else f'ERROR - step 502: {e}')

print("STEP 503 - Check element li_503")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 503')
except Exception as e:
    print('FAIL - step 503' if isinstance(e, AssertionError) else f'ERROR - step 503: {e}')

print("STEP 504 - Check element a_504")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 504')
except Exception as e:
    print('FAIL - step 504' if isinstance(e, AssertionError) else f'ERROR - step 504: {e}')

print("STEP 505 - Check element span_505")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 505')
except Exception as e:
    print('FAIL - step 505' if isinstance(e, AssertionError) else f'ERROR - step 505: {e}')

print("STEP 506 - Check element strong_506")
try:
    element = driver.find_element(By.TAG_NAME, "strong")
    print('PASS - step 506')
except Exception as e:
    print('FAIL - step 506' if isinstance(e, AssertionError) else f'ERROR - step 506: {e}')

print("STEP 507 - Check element a_507")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 507')
except Exception as e:
    print('FAIL - step 507' if isinstance(e, AssertionError) else f'ERROR - step 507: {e}')

print("STEP 508 - Check element span_508")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 508')
except Exception as e:
    print('FAIL - step 508' if isinstance(e, AssertionError) else f'ERROR - step 508: {e}')

print("STEP 509 - Check element a_509")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 509')
except Exception as e:
    print('FAIL - step 509' if isinstance(e, AssertionError) else f'ERROR - step 509: {e}')

print("STEP 510 - Check element span_510")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 510')
except Exception as e:
    print('FAIL - step 510' if isinstance(e, AssertionError) else f'ERROR - step 510: {e}')

print("STEP 511 - Check element a_511")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 511')
except Exception as e:
    print('FAIL - step 511' if isinstance(e, AssertionError) else f'ERROR - step 511: {e}')

print("STEP 512 - Check element span_512")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 512')
except Exception as e:
    print('FAIL - step 512' if isinstance(e, AssertionError) else f'ERROR - step 512: {e}')

print("STEP 513 - Check element a_513")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 513')
except Exception as e:
    print('FAIL - step 513' if isinstance(e, AssertionError) else f'ERROR - step 513: {e}')

print("STEP 514 - Check element span_514")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 514')
except Exception as e:
    print('FAIL - step 514' if isinstance(e, AssertionError) else f'ERROR - step 514: {e}')

print("STEP 515 - Check element strong_515")
try:
    element = driver.find_element(By.TAG_NAME, "strong")
    print('PASS - step 515')
except Exception as e:
    print('FAIL - step 515' if isinstance(e, AssertionError) else f'ERROR - step 515: {e}')

print("STEP 516 - Check element a_516")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 516')
except Exception as e:
    print('FAIL - step 516' if isinstance(e, AssertionError) else f'ERROR - step 516: {e}')

print("STEP 517 - Check element span_517")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 517')
except Exception as e:
    print('FAIL - step 517' if isinstance(e, AssertionError) else f'ERROR - step 517: {e}')

print("STEP 518 - Check element a_518")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 518')
except Exception as e:
    print('FAIL - step 518' if isinstance(e, AssertionError) else f'ERROR - step 518: {e}')

print("STEP 519 - Check element span_519")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 519')
except Exception as e:
    print('FAIL - step 519' if isinstance(e, AssertionError) else f'ERROR - step 519: {e}')

print("STEP 520 - Check element a_520")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 520')
except Exception as e:
    print('FAIL - step 520' if isinstance(e, AssertionError) else f'ERROR - step 520: {e}')

print("STEP 521 - Check element span_521")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 521')
except Exception as e:
    print('FAIL - step 521' if isinstance(e, AssertionError) else f'ERROR - step 521: {e}')

print("STEP 522 - Check element a_522")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 522')
except Exception as e:
    print('FAIL - step 522' if isinstance(e, AssertionError) else f'ERROR - step 522: {e}')

print("STEP 523 - Check element span_523")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 523')
except Exception as e:
    print('FAIL - step 523' if isinstance(e, AssertionError) else f'ERROR - step 523: {e}')

print("STEP 524 - Check element li_524")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 524')
except Exception as e:
    print('FAIL - step 524' if isinstance(e, AssertionError) else f'ERROR - step 524: {e}')

print("STEP 525 - Check element a_525")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 525')
except Exception as e:
    print('FAIL - step 525' if isinstance(e, AssertionError) else f'ERROR - step 525: {e}')

print("STEP 526 - Check element div_526")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 526')
except Exception as e:
    print('FAIL - step 526' if isinstance(e, AssertionError) else f'ERROR - step 526: {e}')

print("STEP 527 - Check element span_527")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 527')
except Exception as e:
    print('FAIL - step 527' if isinstance(e, AssertionError) else f'ERROR - step 527: {e}')

print("STEP 528 - Check element div_528")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 528')
except Exception as e:
    print('FAIL - step 528' if isinstance(e, AssertionError) else f'ERROR - step 528: {e}')

print("STEP 529 - Check element div_529")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 529')
except Exception as e:
    print('FAIL - step 529' if isinstance(e, AssertionError) else f'ERROR - step 529: {e}')

print("STEP 530 - Check element ul_530")
try:
    element = driver.find_element(By.TAG_NAME, "ul")
    print('PASS - step 530')
except Exception as e:
    print('FAIL - step 530' if isinstance(e, AssertionError) else f'ERROR - step 530: {e}')

print("STEP 531 - Check element li_531")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 531')
except Exception as e:
    print('FAIL - step 531' if isinstance(e, AssertionError) else f'ERROR - step 531: {e}')

print("STEP 532 - Check element div_532")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 532')
except Exception as e:
    print('FAIL - step 532' if isinstance(e, AssertionError) else f'ERROR - step 532: {e}')

print("STEP 533 - Check element span_533")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 533')
except Exception as e:
    print('FAIL - step 533' if isinstance(e, AssertionError) else f'ERROR - step 533: {e}')

print("STEP 534 - Check element strong_534")
try:
    element = driver.find_element(By.TAG_NAME, "strong")
    print('PASS - step 534')
except Exception as e:
    print('FAIL - step 534' if isinstance(e, AssertionError) else f'ERROR - step 534: {e}')

print("STEP 535 - Check element a_535")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 535')
except Exception as e:
    print('FAIL - step 535' if isinstance(e, AssertionError) else f'ERROR - step 535: {e}')

print("STEP 536 - Check element span_536")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 536')
except Exception as e:
    print('FAIL - step 536' if isinstance(e, AssertionError) else f'ERROR - step 536: {e}')

print("STEP 537 - Check element a_537")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 537')
except Exception as e:
    print('FAIL - step 537' if isinstance(e, AssertionError) else f'ERROR - step 537: {e}')

print("STEP 538 - Check element span_538")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 538')
except Exception as e:
    print('FAIL - step 538' if isinstance(e, AssertionError) else f'ERROR - step 538: {e}')

print("STEP 539 - Check element a_539")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 539')
except Exception as e:
    print('FAIL - step 539' if isinstance(e, AssertionError) else f'ERROR - step 539: {e}')

print("STEP 540 - Check element span_540")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 540')
except Exception as e:
    print('FAIL - step 540' if isinstance(e, AssertionError) else f'ERROR - step 540: {e}')

print("STEP 541 - Check element a_541")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 541')
except Exception as e:
    print('FAIL - step 541' if isinstance(e, AssertionError) else f'ERROR - step 541: {e}')

print("STEP 542 - Check element span_542")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 542')
except Exception as e:
    print('FAIL - step 542' if isinstance(e, AssertionError) else f'ERROR - step 542: {e}')

print("STEP 543 - Check element a_543")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 543')
except Exception as e:
    print('FAIL - step 543' if isinstance(e, AssertionError) else f'ERROR - step 543: {e}')

print("STEP 544 - Check element span_544")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 544')
except Exception as e:
    print('FAIL - step 544' if isinstance(e, AssertionError) else f'ERROR - step 544: {e}')

print("STEP 545 - Check element a_545")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 545')
except Exception as e:
    print('FAIL - step 545' if isinstance(e, AssertionError) else f'ERROR - step 545: {e}')

print("STEP 546 - Check element span_546")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 546')
except Exception as e:
    print('FAIL - step 546' if isinstance(e, AssertionError) else f'ERROR - step 546: {e}')

print("STEP 547 - Check element li_547")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 547')
except Exception as e:
    print('FAIL - step 547' if isinstance(e, AssertionError) else f'ERROR - step 547: {e}')

print("STEP 548 - Check element div_548")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 548')
except Exception as e:
    print('FAIL - step 548' if isinstance(e, AssertionError) else f'ERROR - step 548: {e}')

print("STEP 549 - Check element span_549")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 549')
except Exception as e:
    print('FAIL - step 549' if isinstance(e, AssertionError) else f'ERROR - step 549: {e}')

print("STEP 550 - Check element strong_550")
try:
    element = driver.find_element(By.TAG_NAME, "strong")
    print('PASS - step 550')
except Exception as e:
    print('FAIL - step 550' if isinstance(e, AssertionError) else f'ERROR - step 550: {e}')

print("STEP 551 - Check element a_551")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 551')
except Exception as e:
    print('FAIL - step 551' if isinstance(e, AssertionError) else f'ERROR - step 551: {e}')

print("STEP 552 - Check element span_552")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 552')
except Exception as e:
    print('FAIL - step 552' if isinstance(e, AssertionError) else f'ERROR - step 552: {e}')

print("STEP 553 - Check element a_553")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 553')
except Exception as e:
    print('FAIL - step 553' if isinstance(e, AssertionError) else f'ERROR - step 553: {e}')

print("STEP 554 - Check element span_554")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 554')
except Exception as e:
    print('FAIL - step 554' if isinstance(e, AssertionError) else f'ERROR - step 554: {e}')

print("STEP 555 - Check element a_555")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 555')
except Exception as e:
    print('FAIL - step 555' if isinstance(e, AssertionError) else f'ERROR - step 555: {e}')

print("STEP 556 - Check element span_556")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 556')
except Exception as e:
    print('FAIL - step 556' if isinstance(e, AssertionError) else f'ERROR - step 556: {e}')

print("STEP 557 - Check element a_557")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 557')
except Exception as e:
    print('FAIL - step 557' if isinstance(e, AssertionError) else f'ERROR - step 557: {e}')

print("STEP 558 - Check element span_558")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 558')
except Exception as e:
    print('FAIL - step 558' if isinstance(e, AssertionError) else f'ERROR - step 558: {e}')

print("STEP 559 - Check element a_559")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 559')
except Exception as e:
    print('FAIL - step 559' if isinstance(e, AssertionError) else f'ERROR - step 559: {e}')

print("STEP 560 - Check element span_560")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 560')
except Exception as e:
    print('FAIL - step 560' if isinstance(e, AssertionError) else f'ERROR - step 560: {e}')

print("STEP 561 - Check element a_561")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 561')
except Exception as e:
    print('FAIL - step 561' if isinstance(e, AssertionError) else f'ERROR - step 561: {e}')

print("STEP 562 - Check element span_562")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 562')
except Exception as e:
    print('FAIL - step 562' if isinstance(e, AssertionError) else f'ERROR - step 562: {e}')

print("STEP 563 - Check element div_563")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 563')
except Exception as e:
    print('FAIL - step 563' if isinstance(e, AssertionError) else f'ERROR - step 563: {e}')

print("STEP 564 - Check element div_564")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 564')
except Exception as e:
    print('FAIL - step 564' if isinstance(e, AssertionError) else f'ERROR - step 564: {e}')

print("STEP 565 - Check element div_565")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 565')
except Exception as e:
    print('FAIL - step 565' if isinstance(e, AssertionError) else f'ERROR - step 565: {e}')

print("STEP 566 - Check element div_566")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 566')
except Exception as e:
    print('FAIL - step 566' if isinstance(e, AssertionError) else f'ERROR - step 566: {e}')

print("STEP 567 - Check element div_567")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 567')
except Exception as e:
    print('FAIL - step 567' if isinstance(e, AssertionError) else f'ERROR - step 567: {e}')

print("STEP 568 - Check element div_568")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 568')
except Exception as e:
    print('FAIL - step 568' if isinstance(e, AssertionError) else f'ERROR - step 568: {e}')

print("STEP 569 - Check element a_569")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 569')
except Exception as e:
    print('FAIL - step 569' if isinstance(e, AssertionError) else f'ERROR - step 569: {e}')

print("STEP 570 - Check element div_570")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 570')
except Exception as e:
    print('FAIL - step 570' if isinstance(e, AssertionError) else f'ERROR - step 570: {e}')

print("STEP 571 - Check element div_571")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 571')
except Exception as e:
    print('FAIL - step 571' if isinstance(e, AssertionError) else f'ERROR - step 571: {e}')

print("STEP 572 - Check element div_572")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 572')
except Exception as e:
    print('FAIL - step 572' if isinstance(e, AssertionError) else f'ERROR - step 572: {e}')

print("STEP 573 - Check element div_573")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 573')
except Exception as e:
    print('FAIL - step 573' if isinstance(e, AssertionError) else f'ERROR - step 573: {e}')

print("STEP 574 - Check element div_574")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 574')
except Exception as e:
    print('FAIL - step 574' if isinstance(e, AssertionError) else f'ERROR - step 574: {e}')

print("STEP 575 - Check element div_575")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 575')
except Exception as e:
    print('FAIL - step 575' if isinstance(e, AssertionError) else f'ERROR - step 575: {e}')

print("STEP 576 - Check element div_576")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 576')
except Exception as e:
    print('FAIL - step 576' if isinstance(e, AssertionError) else f'ERROR - step 576: {e}')

print("STEP 577 - Check element div_577")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 577')
except Exception as e:
    print('FAIL - step 577' if isinstance(e, AssertionError) else f'ERROR - step 577: {e}')

print("STEP 578 - Check element div_578")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 578')
except Exception as e:
    print('FAIL - step 578' if isinstance(e, AssertionError) else f'ERROR - step 578: {e}')

print("STEP 579 - Check element div_579")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 579')
except Exception as e:
    print('FAIL - step 579' if isinstance(e, AssertionError) else f'ERROR - step 579: {e}')

print("STEP 580 - Check element div_580")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 580')
except Exception as e:
    print('FAIL - step 580' if isinstance(e, AssertionError) else f'ERROR - step 580: {e}')

print("STEP 581 - Check element div_581")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 581')
except Exception as e:
    print('FAIL - step 581' if isinstance(e, AssertionError) else f'ERROR - step 581: {e}')

print("STEP 582 - Check element div_582")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 582')
except Exception as e:
    print('FAIL - step 582' if isinstance(e, AssertionError) else f'ERROR - step 582: {e}')

print("STEP 583 - Check element div_583")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 583')
except Exception as e:
    print('FAIL - step 583' if isinstance(e, AssertionError) else f'ERROR - step 583: {e}')

print("STEP 584 - Check element div_584")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 584')
except Exception as e:
    print('FAIL - step 584' if isinstance(e, AssertionError) else f'ERROR - step 584: {e}')

print("STEP 585 - Check element div_585")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 585')
except Exception as e:
    print('FAIL - step 585' if isinstance(e, AssertionError) else f'ERROR - step 585: {e}')

print("STEP 586 - Check element div_586")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 586')
except Exception as e:
    print('FAIL - step 586' if isinstance(e, AssertionError) else f'ERROR - step 586: {e}')

print("STEP 587 - Check element div_587")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 587')
except Exception as e:
    print('FAIL - step 587' if isinstance(e, AssertionError) else f'ERROR - step 587: {e}')

print("STEP 588 - Check element div_588")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 588')
except Exception as e:
    print('FAIL - step 588' if isinstance(e, AssertionError) else f'ERROR - step 588: {e}')

print("STEP 589 - Check element div_589")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 589')
except Exception as e:
    print('FAIL - step 589' if isinstance(e, AssertionError) else f'ERROR - step 589: {e}')

print("STEP 590 - Check element div_590")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 590')
except Exception as e:
    print('FAIL - step 590' if isinstance(e, AssertionError) else f'ERROR - step 590: {e}')

print("STEP 591 - Check element div_591")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 591')
except Exception as e:
    print('FAIL - step 591' if isinstance(e, AssertionError) else f'ERROR - step 591: {e}')

print("STEP 592 - Check element div_592")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 592')
except Exception as e:
    print('FAIL - step 592' if isinstance(e, AssertionError) else f'ERROR - step 592: {e}')

print("STEP 593 - Check element div_593")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 593')
except Exception as e:
    print('FAIL - step 593' if isinstance(e, AssertionError) else f'ERROR - step 593: {e}')

print("STEP 594 - Check element div_594")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 594')
except Exception as e:
    print('FAIL - step 594' if isinstance(e, AssertionError) else f'ERROR - step 594: {e}')

print("STEP 595 - Check element div_595")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 595')
except Exception as e:
    print('FAIL - step 595' if isinstance(e, AssertionError) else f'ERROR - step 595: {e}')

print("STEP 596 - Check element div_596")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 596')
except Exception as e:
    print('FAIL - step 596' if isinstance(e, AssertionError) else f'ERROR - step 596: {e}')

print("STEP 597 - Check element div_597")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 597')
except Exception as e:
    print('FAIL - step 597' if isinstance(e, AssertionError) else f'ERROR - step 597: {e}')

print("STEP 598 - Check element div_598")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 598')
except Exception as e:
    print('FAIL - step 598' if isinstance(e, AssertionError) else f'ERROR - step 598: {e}')

print("STEP 599 - Check element div_599")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 599')
except Exception as e:
    print('FAIL - step 599' if isinstance(e, AssertionError) else f'ERROR - step 599: {e}')

print("STEP 600 - Check element div_600")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 600')
except Exception as e:
    print('FAIL - step 600' if isinstance(e, AssertionError) else f'ERROR - step 600: {e}')

print("STEP 601 - Check element script_601")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 601')
except Exception as e:
    print('FAIL - step 601' if isinstance(e, AssertionError) else f'ERROR - step 601: {e}')

print("STEP 602 - Check element main_602")
try:
    element = driver.find_element(By.TAG_NAME, "main")
    print('PASS - step 602')
except Exception as e:
    print('FAIL - step 602' if isinstance(e, AssertionError) else f'ERROR - step 602: {e}')

print("STEP 603 - Check element div_603")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 603')
except Exception as e:
    print('FAIL - step 603' if isinstance(e, AssertionError) else f'ERROR - step 603: {e}')

print("STEP 604 - Check element div_604")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 604')
except Exception as e:
    print('FAIL - step 604' if isinstance(e, AssertionError) else f'ERROR - step 604: {e}')

print("STEP 605 - Check element div_605")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 605')
except Exception as e:
    print('FAIL - step 605' if isinstance(e, AssertionError) else f'ERROR - step 605: {e}')

print("STEP 606 - Check element div_606")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 606')
except Exception as e:
    print('FAIL - step 606' if isinstance(e, AssertionError) else f'ERROR - step 606: {e}')

print("STEP 607 - Check element div_607")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 607')
except Exception as e:
    print('FAIL - step 607' if isinstance(e, AssertionError) else f'ERROR - step 607: {e}')

print("STEP 608 - Check element div_608")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 608')
except Exception as e:
    print('FAIL - step 608' if isinstance(e, AssertionError) else f'ERROR - step 608: {e}')

print("STEP 609 - Check element div_609")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 609')
except Exception as e:
    print('FAIL - step 609' if isinstance(e, AssertionError) else f'ERROR - step 609: {e}')

print("STEP 610 - Check element div_610")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 610')
except Exception as e:
    print('FAIL - step 610' if isinstance(e, AssertionError) else f'ERROR - step 610: {e}')

print("STEP 611 - Check element div_611")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 611')
except Exception as e:
    print('FAIL - step 611' if isinstance(e, AssertionError) else f'ERROR - step 611: {e}')

print("STEP 612 - Check element div_612")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 612')
except Exception as e:
    print('FAIL - step 612' if isinstance(e, AssertionError) else f'ERROR - step 612: {e}')

print("STEP 613 - Check element div_613")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 613')
except Exception as e:
    print('FAIL - step 613' if isinstance(e, AssertionError) else f'ERROR - step 613: {e}')

print("STEP 614 - Check element div_614")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 614')
except Exception as e:
    print('FAIL - step 614' if isinstance(e, AssertionError) else f'ERROR - step 614: {e}')

print("STEP 615 - Check element div_615")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 615')
except Exception as e:
    print('FAIL - step 615' if isinstance(e, AssertionError) else f'ERROR - step 615: {e}')

print("STEP 616 - Check element img_616")
try:
    element = driver.find_element(By.TAG_NAME, "img")
    print('PASS - step 616')
except Exception as e:
    print('FAIL - step 616' if isinstance(e, AssertionError) else f'ERROR - step 616: {e}')

print("STEP 617 - Check element img_617")
try:
    element = driver.find_element(By.TAG_NAME, "img")
    print('PASS - step 617')
except Exception as e:
    print('FAIL - step 617' if isinstance(e, AssertionError) else f'ERROR - step 617: {e}')

print("STEP 618 - Check element div_618")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 618')
except Exception as e:
    print('FAIL - step 618' if isinstance(e, AssertionError) else f'ERROR - step 618: {e}')

print("STEP 619 - Check element div_619")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 619')
except Exception as e:
    print('FAIL - step 619' if isinstance(e, AssertionError) else f'ERROR - step 619: {e}')

print("STEP 620 - Check element img_620")
try:
    element = driver.find_element(By.TAG_NAME, "img")
    print('PASS - step 620')
except Exception as e:
    print('FAIL - step 620' if isinstance(e, AssertionError) else f'ERROR - step 620: {e}')

print("STEP 621 - Check element h2_621")
try:
    element = driver.find_element(By.TAG_NAME, "h2")
    print('PASS - step 621')
except Exception as e:
    print('FAIL - step 621' if isinstance(e, AssertionError) else f'ERROR - step 621: {e}')

print("STEP 622 - Check element span_622")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 622')
except Exception as e:
    print('FAIL - step 622' if isinstance(e, AssertionError) else f'ERROR - step 622: {e}')

print("STEP 623 - Check element span_623")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 623')
except Exception as e:
    print('FAIL - step 623' if isinstance(e, AssertionError) else f'ERROR - step 623: {e}')

print("STEP 624 - Check element p_624")
try:
    element = driver.find_element(By.TAG_NAME, "p")
    print('PASS - step 624')
except Exception as e:
    print('FAIL - step 624' if isinstance(e, AssertionError) else f'ERROR - step 624: {e}')

print("STEP 625 - Check element p_625")
try:
    element = driver.find_element(By.TAG_NAME, "p")
    print('PASS - step 625')
except Exception as e:
    print('FAIL - step 625' if isinstance(e, AssertionError) else f'ERROR - step 625: {e}')

print("STEP 626 - Check element a_626")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 626')
except Exception as e:
    print('FAIL - step 626' if isinstance(e, AssertionError) else f'ERROR - step 626: {e}')

print("STEP 627 - Check element a_627")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 627')
except Exception as e:
    print('FAIL - step 627' if isinstance(e, AssertionError) else f'ERROR - step 627: {e}')

print("STEP 628 - Check element div_628")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 628')
except Exception as e:
    print('FAIL - step 628' if isinstance(e, AssertionError) else f'ERROR - step 628: {e}')

print("STEP 629 - Check element div_629")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 629')
except Exception as e:
    print('FAIL - step 629' if isinstance(e, AssertionError) else f'ERROR - step 629: {e}')

print("STEP 630 - Check element div_630")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 630')
except Exception as e:
    print('FAIL - step 630' if isinstance(e, AssertionError) else f'ERROR - step 630: {e}')

print("STEP 631 - Check element a_631")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 631')
except Exception as e:
    print('FAIL - step 631' if isinstance(e, AssertionError) else f'ERROR - step 631: {e}')

print("STEP 632 - Check element img_632")
try:
    element = driver.find_element(By.TAG_NAME, "img")
    print('PASS - step 632')
except Exception as e:
    print('FAIL - step 632' if isinstance(e, AssertionError) else f'ERROR - step 632: {e}')

print("STEP 633 - Check element div_633")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 633')
except Exception as e:
    print('FAIL - step 633' if isinstance(e, AssertionError) else f'ERROR - step 633: {e}')

print("STEP 634 - Check element div_634")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 634')
except Exception as e:
    print('FAIL - step 634' if isinstance(e, AssertionError) else f'ERROR - step 634: {e}')

print("STEP 635 - Check element a_635")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 635')
except Exception as e:
    print('FAIL - step 635' if isinstance(e, AssertionError) else f'ERROR - step 635: {e}')

print("STEP 636 - Check element img_636")
try:
    element = driver.find_element(By.TAG_NAME, "img")
    print('PASS - step 636')
except Exception as e:
    print('FAIL - step 636' if isinstance(e, AssertionError) else f'ERROR - step 636: {e}')

print("STEP 637 - Check element div_637")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 637')
except Exception as e:
    print('FAIL - step 637' if isinstance(e, AssertionError) else f'ERROR - step 637: {e}')

print("STEP 638 - Check element div_638")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 638')
except Exception as e:
    print('FAIL - step 638' if isinstance(e, AssertionError) else f'ERROR - step 638: {e}')

print("STEP 639 - Check element a_639")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 639')
except Exception as e:
    print('FAIL - step 639' if isinstance(e, AssertionError) else f'ERROR - step 639: {e}')

print("STEP 640 - Check element img_640")
try:
    element = driver.find_element(By.TAG_NAME, "img")
    print('PASS - step 640')
except Exception as e:
    print('FAIL - step 640' if isinstance(e, AssertionError) else f'ERROR - step 640: {e}')

print("STEP 641 - Check element div_641")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 641')
except Exception as e:
    print('FAIL - step 641' if isinstance(e, AssertionError) else f'ERROR - step 641: {e}')

print("STEP 642 - Check element div_642")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 642')
except Exception as e:
    print('FAIL - step 642' if isinstance(e, AssertionError) else f'ERROR - step 642: {e}')

print("STEP 643 - Check element a_643")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 643')
except Exception as e:
    print('FAIL - step 643' if isinstance(e, AssertionError) else f'ERROR - step 643: {e}')

print("STEP 644 - Check element img_644")
try:
    element = driver.find_element(By.TAG_NAME, "img")
    print('PASS - step 644')
except Exception as e:
    print('FAIL - step 644' if isinstance(e, AssertionError) else f'ERROR - step 644: {e}')

print("STEP 645 - Check element div_645")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 645')
except Exception as e:
    print('FAIL - step 645' if isinstance(e, AssertionError) else f'ERROR - step 645: {e}')

print("STEP 646 - Check element script_646")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 646')
except Exception as e:
    print('FAIL - step 646' if isinstance(e, AssertionError) else f'ERROR - step 646: {e}')

print("STEP 647 - Check element meta_647")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 647')
except Exception as e:
    print('FAIL - step 647' if isinstance(e, AssertionError) else f'ERROR - step 647: {e}')

print("STEP 648 - Check element meta_648")
try:
    element = driver.find_element(By.TAG_NAME, "meta")
    print('PASS - step 648')
except Exception as e:
    print('FAIL - step 648' if isinstance(e, AssertionError) else f'ERROR - step 648: {e}')

print("STEP 649 - Check element link_649")
try:
    element = driver.find_element(By.TAG_NAME, "link")
    print('PASS - step 649')
except Exception as e:
    print('FAIL - step 649' if isinstance(e, AssertionError) else f'ERROR - step 649: {e}')

print("STEP 650 - Check element script_650")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 650')
except Exception as e:
    print('FAIL - step 650' if isinstance(e, AssertionError) else f'ERROR - step 650: {e}')

print("STEP 651 - Check element div_651")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 651')
except Exception as e:
    print('FAIL - step 651' if isinstance(e, AssertionError) else f'ERROR - step 651: {e}')

print("STEP 652 - Check element div_652")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 652')
except Exception as e:
    print('FAIL - step 652' if isinstance(e, AssertionError) else f'ERROR - step 652: {e}')

print("STEP 653 - Check element div_653")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 653')
except Exception as e:
    print('FAIL - step 653' if isinstance(e, AssertionError) else f'ERROR - step 653: {e}')

print("STEP 654 - Check element div_654")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 654')
except Exception as e:
    print('FAIL - step 654' if isinstance(e, AssertionError) else f'ERROR - step 654: {e}')

print("STEP 655 - Check element div_655")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 655')
except Exception as e:
    print('FAIL - step 655' if isinstance(e, AssertionError) else f'ERROR - step 655: {e}')

print("STEP 656 - Check element div_656")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 656')
except Exception as e:
    print('FAIL - step 656' if isinstance(e, AssertionError) else f'ERROR - step 656: {e}')

print("STEP 657 - Check element footer_657")
try:
    element = driver.find_element(By.TAG_NAME, "footer")
    print('PASS - step 657')
except Exception as e:
    print('FAIL - step 657' if isinstance(e, AssertionError) else f'ERROR - step 657: {e}')

print("STEP 658 - Check element div_658")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 658')
except Exception as e:
    print('FAIL - step 658' if isinstance(e, AssertionError) else f'ERROR - step 658: {e}')

print("STEP 659 - Check element div_659")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 659')
except Exception as e:
    print('FAIL - step 659' if isinstance(e, AssertionError) else f'ERROR - step 659: {e}')

print("STEP 660 - Check element div_660")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 660')
except Exception as e:
    print('FAIL - step 660' if isinstance(e, AssertionError) else f'ERROR - step 660: {e}')

print("STEP 661 - Check element div_661")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 661')
except Exception as e:
    print('FAIL - step 661' if isinstance(e, AssertionError) else f'ERROR - step 661: {e}')

print("STEP 662 - Check element a_662")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 662')
except Exception as e:
    print('FAIL - step 662' if isinstance(e, AssertionError) else f'ERROR - step 662: {e}')

print("STEP 663 - Check element div_663")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 663')
except Exception as e:
    print('FAIL - step 663' if isinstance(e, AssertionError) else f'ERROR - step 663: {e}')

print("STEP 664 - Check element form_664")
try:
    element = driver.find_element(By.TAG_NAME, "form")
    print('PASS - step 664')
except Exception as e:
    print('FAIL - step 664' if isinstance(e, AssertionError) else f'ERROR - step 664: {e}')

print("STEP 665 - Check element label_665")
try:
    element = driver.find_element(By.TAG_NAME, "label")
    print('PASS - step 665')
except Exception as e:
    print('FAIL - step 665' if isinstance(e, AssertionError) else f'ERROR - step 665: {e}')

print("STEP 666 - Check element input_666")
try:
    element = driver.find_element(By.TAG_NAME, "input")
    print('PASS - step 666')
except Exception as e:
    print('FAIL - step 666' if isinstance(e, AssertionError) else f'ERROR - step 666: {e}')

print("STEP 667 - Check element button_667")
try:
    element = driver.find_element(By.TAG_NAME, "button")
    print('PASS - step 667')
except Exception as e:
    print('FAIL - step 667' if isinstance(e, AssertionError) else f'ERROR - step 667: {e}')

print("STEP 668 - Check element div_668")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 668')
except Exception as e:
    print('FAIL - step 668' if isinstance(e, AssertionError) else f'ERROR - step 668: {e}')

print("STEP 669 - Check element div_669")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 669')
except Exception as e:
    print('FAIL - step 669' if isinstance(e, AssertionError) else f'ERROR - step 669: {e}')

print("STEP 670 - Check element div_670")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 670')
except Exception as e:
    print('FAIL - step 670' if isinstance(e, AssertionError) else f'ERROR - step 670: {e}')

print("STEP 671 - Check element div_671")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 671')
except Exception as e:
    print('FAIL - step 671' if isinstance(e, AssertionError) else f'ERROR - step 671: {e}')

print("STEP 672 - Check element div_672")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 672')
except Exception as e:
    print('FAIL - step 672' if isinstance(e, AssertionError) else f'ERROR - step 672: {e}')

print("STEP 673 - Check element button_673")
try:
    element = driver.find_element(By.TAG_NAME, "button")
    print('PASS - step 673')
except Exception as e:
    print('FAIL - step 673' if isinstance(e, AssertionError) else f'ERROR - step 673: {e}')

print("STEP 674 - Check element iframe_674")
try:
    element = driver.find_element(By.TAG_NAME, "iframe")
    print('PASS - step 674')
except Exception as e:
    print('FAIL - step 674' if isinstance(e, AssertionError) else f'ERROR - step 674: {e}')

print("STEP 675 - Check element div_675")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 675')
except Exception as e:
    print('FAIL - step 675' if isinstance(e, AssertionError) else f'ERROR - step 675: {e}')

print("STEP 676 - Check element div_676")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 676')
except Exception as e:
    print('FAIL - step 676' if isinstance(e, AssertionError) else f'ERROR - step 676: {e}')

print("STEP 677 - Check element div_677")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 677')
except Exception as e:
    print('FAIL - step 677' if isinstance(e, AssertionError) else f'ERROR - step 677: {e}')

print("STEP 678 - Check element span_678")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 678')
except Exception as e:
    print('FAIL - step 678' if isinstance(e, AssertionError) else f'ERROR - step 678: {e}')

print("STEP 679 - Check element div_679")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 679')
except Exception as e:
    print('FAIL - step 679' if isinstance(e, AssertionError) else f'ERROR - step 679: {e}')

print("STEP 680 - Check element img_680")
try:
    element = driver.find_element(By.TAG_NAME, "img")
    print('PASS - step 680')
except Exception as e:
    print('FAIL - step 680' if isinstance(e, AssertionError) else f'ERROR - step 680: {e}')

print("STEP 681 - Check element div_681")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 681')
except Exception as e:
    print('FAIL - step 681' if isinstance(e, AssertionError) else f'ERROR - step 681: {e}')

print("STEP 682 - Check element input_682")
try:
    element = driver.find_element(By.TAG_NAME, "input")
    print('PASS - step 682')
except Exception as e:
    print('FAIL - step 682' if isinstance(e, AssertionError) else f'ERROR - step 682: {e}')

print("STEP 683 - Check element span_683")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 683')
except Exception as e:
    print('FAIL - step 683' if isinstance(e, AssertionError) else f'ERROR - step 683: {e}')

print("STEP 684 - Check element ul_684")
try:
    element = driver.find_element(By.TAG_NAME, "ul")
    print('PASS - step 684')
except Exception as e:
    print('FAIL - step 684' if isinstance(e, AssertionError) else f'ERROR - step 684: {e}')

print("STEP 685 - Check element div_685")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 685')
except Exception as e:
    print('FAIL - step 685' if isinstance(e, AssertionError) else f'ERROR - step 685: {e}')

print("STEP 686 - Check element div_686")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 686')
except Exception as e:
    print('FAIL - step 686' if isinstance(e, AssertionError) else f'ERROR - step 686: {e}')

print("STEP 687 - Check element div_687")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 687')
except Exception as e:
    print('FAIL - step 687' if isinstance(e, AssertionError) else f'ERROR - step 687: {e}')

print("STEP 688 - Check element h2_688")
try:
    element = driver.find_element(By.TAG_NAME, "h2")
    print('PASS - step 688')
except Exception as e:
    print('FAIL - step 688' if isinstance(e, AssertionError) else f'ERROR - step 688: {e}')

print("STEP 689 - Check element ul_689")
try:
    element = driver.find_element(By.TAG_NAME, "ul")
    print('PASS - step 689')
except Exception as e:
    print('FAIL - step 689' if isinstance(e, AssertionError) else f'ERROR - step 689: {e}')

print("STEP 690 - Check element li_690")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 690')
except Exception as e:
    print('FAIL - step 690' if isinstance(e, AssertionError) else f'ERROR - step 690: {e}')

print("STEP 691 - Check element a_691")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 691')
except Exception as e:
    print('FAIL - step 691' if isinstance(e, AssertionError) else f'ERROR - step 691: {e}')

print("STEP 692 - Check element li_692")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 692')
except Exception as e:
    print('FAIL - step 692' if isinstance(e, AssertionError) else f'ERROR - step 692: {e}')

print("STEP 693 - Check element a_693")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 693')
except Exception as e:
    print('FAIL - step 693' if isinstance(e, AssertionError) else f'ERROR - step 693: {e}')

print("STEP 694 - Check element li_694")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 694')
except Exception as e:
    print('FAIL - step 694' if isinstance(e, AssertionError) else f'ERROR - step 694: {e}')

print("STEP 695 - Check element a_695")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 695')
except Exception as e:
    print('FAIL - step 695' if isinstance(e, AssertionError) else f'ERROR - step 695: {e}')

print("STEP 696 - Check element li_696")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 696')
except Exception as e:
    print('FAIL - step 696' if isinstance(e, AssertionError) else f'ERROR - step 696: {e}')

print("STEP 697 - Check element a_697")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 697')
except Exception as e:
    print('FAIL - step 697' if isinstance(e, AssertionError) else f'ERROR - step 697: {e}')

print("STEP 698 - Check element li_698")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 698')
except Exception as e:
    print('FAIL - step 698' if isinstance(e, AssertionError) else f'ERROR - step 698: {e}')

print("STEP 699 - Check element a_699")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 699')
except Exception as e:
    print('FAIL - step 699' if isinstance(e, AssertionError) else f'ERROR - step 699: {e}')

print("STEP 700 - Check element li_700")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 700')
except Exception as e:
    print('FAIL - step 700' if isinstance(e, AssertionError) else f'ERROR - step 700: {e}')

print("STEP 701 - Check element a_701")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 701')
except Exception as e:
    print('FAIL - step 701' if isinstance(e, AssertionError) else f'ERROR - step 701: {e}')

print("STEP 702 - Check element div_702")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 702')
except Exception as e:
    print('FAIL - step 702' if isinstance(e, AssertionError) else f'ERROR - step 702: {e}')

print("STEP 703 - Check element h2_703")
try:
    element = driver.find_element(By.TAG_NAME, "h2")
    print('PASS - step 703')
except Exception as e:
    print('FAIL - step 703' if isinstance(e, AssertionError) else f'ERROR - step 703: {e}')

print("STEP 704 - Check element ul_704")
try:
    element = driver.find_element(By.TAG_NAME, "ul")
    print('PASS - step 704')
except Exception as e:
    print('FAIL - step 704' if isinstance(e, AssertionError) else f'ERROR - step 704: {e}')

print("STEP 705 - Check element li_705")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 705')
except Exception as e:
    print('FAIL - step 705' if isinstance(e, AssertionError) else f'ERROR - step 705: {e}')

print("STEP 706 - Check element a_706")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 706')
except Exception as e:
    print('FAIL - step 706' if isinstance(e, AssertionError) else f'ERROR - step 706: {e}')

print("STEP 707 - Check element li_707")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 707')
except Exception as e:
    print('FAIL - step 707' if isinstance(e, AssertionError) else f'ERROR - step 707: {e}')

print("STEP 708 - Check element a_708")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 708')
except Exception as e:
    print('FAIL - step 708' if isinstance(e, AssertionError) else f'ERROR - step 708: {e}')

print("STEP 709 - Check element li_709")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 709')
except Exception as e:
    print('FAIL - step 709' if isinstance(e, AssertionError) else f'ERROR - step 709: {e}')

print("STEP 710 - Check element a_710")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 710')
except Exception as e:
    print('FAIL - step 710' if isinstance(e, AssertionError) else f'ERROR - step 710: {e}')

print("STEP 711 - Check element li_711")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 711')
except Exception as e:
    print('FAIL - step 711' if isinstance(e, AssertionError) else f'ERROR - step 711: {e}')

print("STEP 712 - Check element a_712")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 712')
except Exception as e:
    print('FAIL - step 712' if isinstance(e, AssertionError) else f'ERROR - step 712: {e}')

print("STEP 713 - Check element li_713")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 713')
except Exception as e:
    print('FAIL - step 713' if isinstance(e, AssertionError) else f'ERROR - step 713: {e}')

print("STEP 714 - Check element a_714")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 714')
except Exception as e:
    print('FAIL - step 714' if isinstance(e, AssertionError) else f'ERROR - step 714: {e}')

print("STEP 715 - Check element li_715")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 715')
except Exception as e:
    print('FAIL - step 715' if isinstance(e, AssertionError) else f'ERROR - step 715: {e}')

print("STEP 716 - Check element a_716")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 716')
except Exception as e:
    print('FAIL - step 716' if isinstance(e, AssertionError) else f'ERROR - step 716: {e}')

print("STEP 717 - Check element li_717")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 717')
except Exception as e:
    print('FAIL - step 717' if isinstance(e, AssertionError) else f'ERROR - step 717: {e}')

print("STEP 718 - Check element a_718")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 718')
except Exception as e:
    print('FAIL - step 718' if isinstance(e, AssertionError) else f'ERROR - step 718: {e}')

print("STEP 719 - Check element li_719")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 719')
except Exception as e:
    print('FAIL - step 719' if isinstance(e, AssertionError) else f'ERROR - step 719: {e}')

print("STEP 720 - Check element a_720")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 720')
except Exception as e:
    print('FAIL - step 720' if isinstance(e, AssertionError) else f'ERROR - step 720: {e}')

print("STEP 721 - Check element div_721")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 721')
except Exception as e:
    print('FAIL - step 721' if isinstance(e, AssertionError) else f'ERROR - step 721: {e}')

print("STEP 722 - Check element h2_722")
try:
    element = driver.find_element(By.TAG_NAME, "h2")
    print('PASS - step 722')
except Exception as e:
    print('FAIL - step 722' if isinstance(e, AssertionError) else f'ERROR - step 722: {e}')

print("STEP 723 - Check element ul_723")
try:
    element = driver.find_element(By.TAG_NAME, "ul")
    print('PASS - step 723')
except Exception as e:
    print('FAIL - step 723' if isinstance(e, AssertionError) else f'ERROR - step 723: {e}')

print("STEP 724 - Check element li_724")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 724')
except Exception as e:
    print('FAIL - step 724' if isinstance(e, AssertionError) else f'ERROR - step 724: {e}')

print("STEP 725 - Check element a_725")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 725')
except Exception as e:
    print('FAIL - step 725' if isinstance(e, AssertionError) else f'ERROR - step 725: {e}')

print("STEP 726 - Check element li_726")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 726')
except Exception as e:
    print('FAIL - step 726' if isinstance(e, AssertionError) else f'ERROR - step 726: {e}')

print("STEP 727 - Check element a_727")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 727')
except Exception as e:
    print('FAIL - step 727' if isinstance(e, AssertionError) else f'ERROR - step 727: {e}')

print("STEP 728 - Check element div_728")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 728')
except Exception as e:
    print('FAIL - step 728' if isinstance(e, AssertionError) else f'ERROR - step 728: {e}')

print("STEP 729 - Check element h2_729")
try:
    element = driver.find_element(By.TAG_NAME, "h2")
    print('PASS - step 729')
except Exception as e:
    print('FAIL - step 729' if isinstance(e, AssertionError) else f'ERROR - step 729: {e}')

print("STEP 730 - Check element ul_730")
try:
    element = driver.find_element(By.TAG_NAME, "ul")
    print('PASS - step 730')
except Exception as e:
    print('FAIL - step 730' if isinstance(e, AssertionError) else f'ERROR - step 730: {e}')

print("STEP 731 - Check element li_731")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 731')
except Exception as e:
    print('FAIL - step 731' if isinstance(e, AssertionError) else f'ERROR - step 731: {e}')

print("STEP 732 - Check element a_732")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 732')
except Exception as e:
    print('FAIL - step 732' if isinstance(e, AssertionError) else f'ERROR - step 732: {e}')

print("STEP 733 - Check element li_733")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 733')
except Exception as e:
    print('FAIL - step 733' if isinstance(e, AssertionError) else f'ERROR - step 733: {e}')

print("STEP 734 - Check element a_734")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 734')
except Exception as e:
    print('FAIL - step 734' if isinstance(e, AssertionError) else f'ERROR - step 734: {e}')

print("STEP 735 - Check element li_735")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 735')
except Exception as e:
    print('FAIL - step 735' if isinstance(e, AssertionError) else f'ERROR - step 735: {e}')

print("STEP 736 - Check element a_736")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 736')
except Exception as e:
    print('FAIL - step 736' if isinstance(e, AssertionError) else f'ERROR - step 736: {e}')

print("STEP 737 - Check element div_737")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 737')
except Exception as e:
    print('FAIL - step 737' if isinstance(e, AssertionError) else f'ERROR - step 737: {e}')

print("STEP 738 - Check element h2_738")
try:
    element = driver.find_element(By.TAG_NAME, "h2")
    print('PASS - step 738')
except Exception as e:
    print('FAIL - step 738' if isinstance(e, AssertionError) else f'ERROR - step 738: {e}')

print("STEP 739 - Check element ul_739")
try:
    element = driver.find_element(By.TAG_NAME, "ul")
    print('PASS - step 739')
except Exception as e:
    print('FAIL - step 739' if isinstance(e, AssertionError) else f'ERROR - step 739: {e}')

print("STEP 740 - Check element li_740")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 740')
except Exception as e:
    print('FAIL - step 740' if isinstance(e, AssertionError) else f'ERROR - step 740: {e}')

print("STEP 741 - Check element a_741")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 741')
except Exception as e:
    print('FAIL - step 741' if isinstance(e, AssertionError) else f'ERROR - step 741: {e}')

print("STEP 742 - Check element li_742")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 742')
except Exception as e:
    print('FAIL - step 742' if isinstance(e, AssertionError) else f'ERROR - step 742: {e}')

print("STEP 743 - Check element a_743")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 743')
except Exception as e:
    print('FAIL - step 743' if isinstance(e, AssertionError) else f'ERROR - step 743: {e}')

print("STEP 744 - Check element li_744")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 744')
except Exception as e:
    print('FAIL - step 744' if isinstance(e, AssertionError) else f'ERROR - step 744: {e}')

print("STEP 745 - Check element a_745")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 745')
except Exception as e:
    print('FAIL - step 745' if isinstance(e, AssertionError) else f'ERROR - step 745: {e}')

print("STEP 746 - Check element li_746")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 746')
except Exception as e:
    print('FAIL - step 746' if isinstance(e, AssertionError) else f'ERROR - step 746: {e}')

print("STEP 747 - Check element a_747")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 747')
except Exception as e:
    print('FAIL - step 747' if isinstance(e, AssertionError) else f'ERROR - step 747: {e}')

print("STEP 748 - Check element li_748")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 748')
except Exception as e:
    print('FAIL - step 748' if isinstance(e, AssertionError) else f'ERROR - step 748: {e}')

print("STEP 749 - Check element a_749")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 749')
except Exception as e:
    print('FAIL - step 749' if isinstance(e, AssertionError) else f'ERROR - step 749: {e}')

print("STEP 750 - Check element li_750")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 750')
except Exception as e:
    print('FAIL - step 750' if isinstance(e, AssertionError) else f'ERROR - step 750: {e}')

print("STEP 751 - Check element a_751")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 751')
except Exception as e:
    print('FAIL - step 751' if isinstance(e, AssertionError) else f'ERROR - step 751: {e}')

print("STEP 752 - Check element li_752")
try:
    element = driver.find_element(By.TAG_NAME, "li")
    print('PASS - step 752')
except Exception as e:
    print('FAIL - step 752' if isinstance(e, AssertionError) else f'ERROR - step 752: {e}')

print("STEP 753 - Check element a_753")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 753')
except Exception as e:
    print('FAIL - step 753' if isinstance(e, AssertionError) else f'ERROR - step 753: {e}')

print("STEP 754 - Check element div_754")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 754')
except Exception as e:
    print('FAIL - step 754' if isinstance(e, AssertionError) else f'ERROR - step 754: {e}')

print("STEP 755 - Check element div_755")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 755')
except Exception as e:
    print('FAIL - step 755' if isinstance(e, AssertionError) else f'ERROR - step 755: {e}')

print("STEP 756 - Check element div_756")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 756')
except Exception as e:
    print('FAIL - step 756' if isinstance(e, AssertionError) else f'ERROR - step 756: {e}')

print("STEP 757 - Check element div_757")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 757')
except Exception as e:
    print('FAIL - step 757' if isinstance(e, AssertionError) else f'ERROR - step 757: {e}')

print("STEP 758 - Check element div_758")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 758')
except Exception as e:
    print('FAIL - step 758' if isinstance(e, AssertionError) else f'ERROR - step 758: {e}')

print("STEP 759 - Check element div_759")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 759')
except Exception as e:
    print('FAIL - step 759' if isinstance(e, AssertionError) else f'ERROR - step 759: {e}')

print("STEP 760 - Check element a_760")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 760')
except Exception as e:
    print('FAIL - step 760' if isinstance(e, AssertionError) else f'ERROR - step 760: {e}')

print("STEP 761 - Check element a_761")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 761')
except Exception as e:
    print('FAIL - step 761' if isinstance(e, AssertionError) else f'ERROR - step 761: {e}')

print("STEP 762 - Check element a_762")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 762')
except Exception as e:
    print('FAIL - step 762' if isinstance(e, AssertionError) else f'ERROR - step 762: {e}')

print("STEP 763 - Check element div_763")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 763')
except Exception as e:
    print('FAIL - step 763' if isinstance(e, AssertionError) else f'ERROR - step 763: {e}')

print("STEP 764 - Check element script_764")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 764')
except Exception as e:
    print('FAIL - step 764' if isinstance(e, AssertionError) else f'ERROR - step 764: {e}')

print("STEP 765 - Check element script_765")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 765')
except Exception as e:
    print('FAIL - step 765' if isinstance(e, AssertionError) else f'ERROR - step 765: {e}')

print("STEP 766 - Check element script_766")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 766')
except Exception as e:
    print('FAIL - step 766' if isinstance(e, AssertionError) else f'ERROR - step 766: {e}')

print("STEP 767 - Check element script_767")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 767')
except Exception as e:
    print('FAIL - step 767' if isinstance(e, AssertionError) else f'ERROR - step 767: {e}')

print("STEP 768 - Check element script_768")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 768')
except Exception as e:
    print('FAIL - step 768' if isinstance(e, AssertionError) else f'ERROR - step 768: {e}')

print("STEP 769 - Check element style_769")
try:
    element = driver.find_element(By.TAG_NAME, "style")
    print('PASS - step 769')
except Exception as e:
    print('FAIL - step 769' if isinstance(e, AssertionError) else f'ERROR - step 769: {e}')

print("STEP 770 - Check element div_770")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 770')
except Exception as e:
    print('FAIL - step 770' if isinstance(e, AssertionError) else f'ERROR - step 770: {e}')

print("STEP 771 - Check element button_771")
try:
    element = driver.find_element(By.TAG_NAME, "button")
    print('PASS - step 771')
except Exception as e:
    print('FAIL - step 771' if isinstance(e, AssertionError) else f'ERROR - step 771: {e}')

print("STEP 772 - Check element div_772")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 772')
except Exception as e:
    print('FAIL - step 772' if isinstance(e, AssertionError) else f'ERROR - step 772: {e}')

print("STEP 773 - Check element div_773")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 773')
except Exception as e:
    print('FAIL - step 773' if isinstance(e, AssertionError) else f'ERROR - step 773: {e}')

print("STEP 774 - Check element div_774")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 774')
except Exception as e:
    print('FAIL - step 774' if isinstance(e, AssertionError) else f'ERROR - step 774: {e}')

print("STEP 775 - Check element div_775")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 775')
except Exception as e:
    print('FAIL - step 775' if isinstance(e, AssertionError) else f'ERROR - step 775: {e}')

print("STEP 776 - Check element a_776")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 776')
except Exception as e:
    print('FAIL - step 776' if isinstance(e, AssertionError) else f'ERROR - step 776: {e}')

print("STEP 777 - Check element div_777")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 777')
except Exception as e:
    print('FAIL - step 777' if isinstance(e, AssertionError) else f'ERROR - step 777: {e}')

print("STEP 778 - Check element span_778")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 778')
except Exception as e:
    print('FAIL - step 778' if isinstance(e, AssertionError) else f'ERROR - step 778: {e}')

print("STEP 779 - Check element span_779")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 779')
except Exception as e:
    print('FAIL - step 779' if isinstance(e, AssertionError) else f'ERROR - step 779: {e}')

print("STEP 780 - Check element span_780")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 780')
except Exception as e:
    print('FAIL - step 780' if isinstance(e, AssertionError) else f'ERROR - step 780: {e}')

print("STEP 781 - Check element div_781")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 781')
except Exception as e:
    print('FAIL - step 781' if isinstance(e, AssertionError) else f'ERROR - step 781: {e}')

print("STEP 782 - Check element div_782")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 782')
except Exception as e:
    print('FAIL - step 782' if isinstance(e, AssertionError) else f'ERROR - step 782: {e}')

print("STEP 783 - Check element div_783")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 783')
except Exception as e:
    print('FAIL - step 783' if isinstance(e, AssertionError) else f'ERROR - step 783: {e}')

print("STEP 784 - Check element div_784")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 784')
except Exception as e:
    print('FAIL - step 784' if isinstance(e, AssertionError) else f'ERROR - step 784: {e}')

print("STEP 785 - Check element div_785")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 785')
except Exception as e:
    print('FAIL - step 785' if isinstance(e, AssertionError) else f'ERROR - step 785: {e}')

print("STEP 786 - Check element a_786")
try:
    element = driver.find_element(By.TAG_NAME, "a")
    print('PASS - step 786')
except Exception as e:
    print('FAIL - step 786' if isinstance(e, AssertionError) else f'ERROR - step 786: {e}')

print("STEP 787 - Check element i_787")
try:
    element = driver.find_element(By.TAG_NAME, "i")
    print('PASS - step 787')
except Exception as e:
    print('FAIL - step 787' if isinstance(e, AssertionError) else f'ERROR - step 787: {e}')

print("STEP 788 - Check element span_788")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 788')
except Exception as e:
    print('FAIL - step 788' if isinstance(e, AssertionError) else f'ERROR - step 788: {e}')

print("STEP 789 - Check element pre_789")
try:
    element = driver.find_element(By.TAG_NAME, "pre")
    print('PASS - step 789')
except Exception as e:
    print('FAIL - step 789' if isinstance(e, AssertionError) else f'ERROR - step 789: {e}')

print("STEP 790 - Check element span_790")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 790')
except Exception as e:
    print('FAIL - step 790' if isinstance(e, AssertionError) else f'ERROR - step 790: {e}')

print("STEP 791 - Check element div_791")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 791')
except Exception as e:
    print('FAIL - step 791' if isinstance(e, AssertionError) else f'ERROR - step 791: {e}')

print("STEP 792 - Check element script_792")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 792')
except Exception as e:
    print('FAIL - step 792' if isinstance(e, AssertionError) else f'ERROR - step 792: {e}')

print("STEP 793 - Check element script_793")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 793')
except Exception as e:
    print('FAIL - step 793' if isinstance(e, AssertionError) else f'ERROR - step 793: {e}')

print("STEP 794 - Check element script_794")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 794')
except Exception as e:
    print('FAIL - step 794' if isinstance(e, AssertionError) else f'ERROR - step 794: {e}')

print("STEP 795 - Check element div_795")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 795')
except Exception as e:
    print('FAIL - step 795' if isinstance(e, AssertionError) else f'ERROR - step 795: {e}')

print("STEP 796 - Check element div_796")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 796')
except Exception as e:
    print('FAIL - step 796' if isinstance(e, AssertionError) else f'ERROR - step 796: {e}')

print("STEP 797 - Check element div_797")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 797')
except Exception as e:
    print('FAIL - step 797' if isinstance(e, AssertionError) else f'ERROR - step 797: {e}')

print("STEP 798 - Check element div_798")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 798')
except Exception as e:
    print('FAIL - step 798' if isinstance(e, AssertionError) else f'ERROR - step 798: {e}')

print("STEP 799 - Check element div_799")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 799')
except Exception as e:
    print('FAIL - step 799' if isinstance(e, AssertionError) else f'ERROR - step 799: {e}')

print("STEP 800 - Check element button_800")
try:
    element = driver.find_element(By.TAG_NAME, "button")
    print('PASS - step 800')
except Exception as e:
    print('FAIL - step 800' if isinstance(e, AssertionError) else f'ERROR - step 800: {e}')

print("STEP 801 - Check element span_801")
try:
    element = driver.find_element(By.TAG_NAME, "span")
    print('PASS - step 801')
except Exception as e:
    print('FAIL - step 801' if isinstance(e, AssertionError) else f'ERROR - step 801: {e}')

print("STEP 802 - Check element div_802")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 802')
except Exception as e:
    print('FAIL - step 802' if isinstance(e, AssertionError) else f'ERROR - step 802: {e}')

print("STEP 803 - Check element div_803")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 803')
except Exception as e:
    print('FAIL - step 803' if isinstance(e, AssertionError) else f'ERROR - step 803: {e}')

print("STEP 804 - Check element script_804")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 804')
except Exception as e:
    print('FAIL - step 804' if isinstance(e, AssertionError) else f'ERROR - step 804: {e}')

print("STEP 805 - Check element script_805")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 805')
except Exception as e:
    print('FAIL - step 805' if isinstance(e, AssertionError) else f'ERROR - step 805: {e}')

print("STEP 806 - Check element script_806")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 806')
except Exception as e:
    print('FAIL - step 806' if isinstance(e, AssertionError) else f'ERROR - step 806: {e}')

print("STEP 807 - Check element script_807")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 807')
except Exception as e:
    print('FAIL - step 807' if isinstance(e, AssertionError) else f'ERROR - step 807: {e}')

print("STEP 808 - Check element noscript_808")
try:
    element = driver.find_element(By.TAG_NAME, "noscript")
    print('PASS - step 808')
except Exception as e:
    print('FAIL - step 808' if isinstance(e, AssertionError) else f'ERROR - step 808: {e}')

print("STEP 809 - Check element img_809")
try:
    element = driver.find_element(By.TAG_NAME, "img")
    print('PASS - step 809')
except Exception as e:
    print('FAIL - step 809' if isinstance(e, AssertionError) else f'ERROR - step 809: {e}')

print("STEP 810 - Check element style_810")
try:
    element = driver.find_element(By.TAG_NAME, "style")
    print('PASS - step 810')
except Exception as e:
    print('FAIL - step 810' if isinstance(e, AssertionError) else f'ERROR - step 810: {e}')

print("STEP 811 - Check element div_811")
try:
    element = driver.find_element(By.TAG_NAME, "div")
    print('PASS - step 811')
except Exception as e:
    print('FAIL - step 811' if isinstance(e, AssertionError) else f'ERROR - step 811: {e}')

print("STEP 812 - Check element script_812")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 812')
except Exception as e:
    print('FAIL - step 812' if isinstance(e, AssertionError) else f'ERROR - step 812: {e}')

print("STEP 813 - Check element script_813")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 813')
except Exception as e:
    print('FAIL - step 813' if isinstance(e, AssertionError) else f'ERROR - step 813: {e}')

print("STEP 814 - Check element script_814")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 814')
except Exception as e:
    print('FAIL - step 814' if isinstance(e, AssertionError) else f'ERROR - step 814: {e}')

print("STEP 815 - Check element script_815")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 815')
except Exception as e:
    print('FAIL - step 815' if isinstance(e, AssertionError) else f'ERROR - step 815: {e}')

print("STEP 816 - Check element script_816")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 816')
except Exception as e:
    print('FAIL - step 816' if isinstance(e, AssertionError) else f'ERROR - step 816: {e}')

print("STEP 817 - Check element script_817")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 817')
except Exception as e:
    print('FAIL - step 817' if isinstance(e, AssertionError) else f'ERROR - step 817: {e}')

print("STEP 818 - Check element script_818")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 818')
except Exception as e:
    print('FAIL - step 818' if isinstance(e, AssertionError) else f'ERROR - step 818: {e}')

print("STEP 819 - Check element script_819")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 819')
except Exception as e:
    print('FAIL - step 819' if isinstance(e, AssertionError) else f'ERROR - step 819: {e}')

print("STEP 820 - Check element script_820")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 820')
except Exception as e:
    print('FAIL - step 820' if isinstance(e, AssertionError) else f'ERROR - step 820: {e}')

print("STEP 821 - Check element script_821")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 821')
except Exception as e:
    print('FAIL - step 821' if isinstance(e, AssertionError) else f'ERROR - step 821: {e}')

print("STEP 822 - Check element script_822")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 822')
except Exception as e:
    print('FAIL - step 822' if isinstance(e, AssertionError) else f'ERROR - step 822: {e}')

print("STEP 823 - Check element script_823")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 823')
except Exception as e:
    print('FAIL - step 823' if isinstance(e, AssertionError) else f'ERROR - step 823: {e}')

print("STEP 824 - Check element script_824")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 824')
except Exception as e:
    print('FAIL - step 824' if isinstance(e, AssertionError) else f'ERROR - step 824: {e}')

print("STEP 825 - Check element script_825")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 825')
except Exception as e:
    print('FAIL - step 825' if isinstance(e, AssertionError) else f'ERROR - step 825: {e}')

print("STEP 826 - Check element script_826")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 826')
except Exception as e:
    print('FAIL - step 826' if isinstance(e, AssertionError) else f'ERROR - step 826: {e}')

print("STEP 827 - Check element script_827")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 827')
except Exception as e:
    print('FAIL - step 827' if isinstance(e, AssertionError) else f'ERROR - step 827: {e}')

print("STEP 828 - Check element script_828")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 828')
except Exception as e:
    print('FAIL - step 828' if isinstance(e, AssertionError) else f'ERROR - step 828: {e}')

print("STEP 829 - Check element script_829")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 829')
except Exception as e:
    print('FAIL - step 829' if isinstance(e, AssertionError) else f'ERROR - step 829: {e}')

print("STEP 830 - Check element script_830")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 830')
except Exception as e:
    print('FAIL - step 830' if isinstance(e, AssertionError) else f'ERROR - step 830: {e}')

print("STEP 831 - Check element script_831")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 831')
except Exception as e:
    print('FAIL - step 831' if isinstance(e, AssertionError) else f'ERROR - step 831: {e}')

print("STEP 832 - Check element script_832")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 832')
except Exception as e:
    print('FAIL - step 832' if isinstance(e, AssertionError) else f'ERROR - step 832: {e}')

print("STEP 833 - Check element iframe_833")
try:
    element = driver.find_element(By.TAG_NAME, "iframe")
    print('PASS - step 833')
except Exception as e:
    print('FAIL - step 833' if isinstance(e, AssertionError) else f'ERROR - step 833: {e}')

print("STEP 834 - Check element script_834")
try:
    element = driver.find_element(By.TAG_NAME, "script")
    print('PASS - step 834')
except Exception as e:
    print('FAIL - step 834' if isinstance(e, AssertionError) else f'ERROR - step 834: {e}')

print("STEP 835 - Check element style_835")
try:
    element = driver.find_element(By.TAG_NAME, "style")
    print('PASS - step 835')
except Exception as e:
    print('FAIL - step 835' if isinstance(e, AssertionError) else f'ERROR - step 835: {e}')

driver.quit()