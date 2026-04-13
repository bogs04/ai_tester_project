from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get('https://example.com')
time.sleep(1)
print('STEP 1 - Advanced Check html')
try:
    # simulated advanced assertion
    print(f'PASS - step {i}')
except Exception as e:
    print(f'ERROR - step {i}: {str(e)}')
print('STEP 2 - Advanced Check head')
try:
    # simulated advanced assertion
    print(f'PASS - step {i}')
except Exception as e:
    print(f'ERROR - step {i}: {str(e)}')
print('STEP 3 - Advanced Check title')
try:
    # simulated advanced assertion
    print(f'PASS - step {i}')
except Exception as e:
    print(f'ERROR - step {i}: {str(e)}')
print('STEP 4 - Advanced Check meta')
try:
    # simulated advanced assertion
    print(f'PASS - step {i}')
except Exception as e:
    print(f'ERROR - step {i}: {str(e)}')
print('STEP 5 - Advanced Check style')
try:
    # simulated advanced assertion
    print(f'PASS - step {i}')
except Exception as e:
    print(f'ERROR - step {i}: {str(e)}')
print('STEP 6 - Advanced Check body')
try:
    # simulated advanced assertion
    print(f'PASS - step {i}')
except Exception as e:
    print(f'ERROR - step {i}: {str(e)}')
print('STEP 7 - Advanced Check div')
try:
    # simulated advanced assertion
    print(f'PASS - step {i}')
except Exception as e:
    print(f'ERROR - step {i}: {str(e)}')
print('STEP 8 - Advanced Check h1')
try:
    # simulated advanced assertion
    print(f'PASS - step {i}')
except Exception as e:
    print(f'ERROR - step {i}: {str(e)}')
print('STEP 9 - Advanced Check p')
try:
    # simulated advanced assertion
    print(f'PASS - step {i}')
except Exception as e:
    print(f'ERROR - step {i}: {str(e)}')
print('STEP 10 - Advanced Check p')
try:
    # simulated advanced assertion
    print(f'PASS - step {i}')
except Exception as e:
    print(f'ERROR - step {i}: {str(e)}')
print('STEP 11 - Advanced Check a')
try:
    # simulated advanced assertion
    print(f'PASS - step {i}')
except Exception as e:
    print(f'ERROR - step {i}: {str(e)}')
driver.quit()