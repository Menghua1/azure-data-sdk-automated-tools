from selenium import webdriver
from selenium.webdriver import EdgeOptions
from selenium.webdriver.common.by import By
import time

option = EdgeOptions()
# option.add_argument('--start-maximized')
option.add_experimental_option('excludeSwitches',['enable-automation'])
prefs = {'credential_enable_service': False, 'profile.password_manager_enable': False}
option.add_experimental_option('prefs', prefs)
option.add_argument('--disable-blink-features=AutomationControlled')
option.add_argument('--disable-gpu')

driver = webdriver.Edge(options=option)
driver.get("https://login.taobao.com/member/login.jhtml?redirectURL=http%3A%2F%2Fi.taobao.com%2Fmy_itaobao%3Fspm%3Da21n57.sem.1997525045.1.53983903FTfzhG")
time.sleep(60)
driver.maximize_window()
button_cart = driver.find_element(By.ID, 'J_MiniCart')
button_cart.click()
time.sleep(10)

button_input1 = driver.find_element(By.XPATH, '//*[@id="shopCard_s_2214235872491"]/div[2]/div/div[1]/label/span/input')
button_input1.click()

# button_input2 = driver.find_element(By.XPATH, '//*[@id="shopCard_s_2214235872491"]/div[3]/div/div[1]/label/span/input')
# button_input2.click()
time.sleep(10)

button_check = driver.find_element(By.XPATH, '//*[@id="settlementContainer_1"]/div[4]/div/div[2]')
button_check.click()
time.sleep(5)

count_failed = 0
while True:
    try:
        button_submit_order = driver.find_element(By.XPATH, '//*[@id="submitOrder"]/div/div[2]/div')
        button_submit_order.click()
    except:
        count_failed += 1
        print('Failed: %d'%(count_failed))
        if count_failed == 600:
            break
    else:
        print('Success!')
        break

time.sleep(5)
driver.quit()