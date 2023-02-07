from selenium import webdriver
import time

driver = webdriver.Chrome('C:/Users/lyaas/Desktop/webdriver/chromedriver.exe')
driver.get('https://linkedin.com')
time.sleep(2)

# *********LOG IN************

username = driver.find_element_by_xpath("//input[@name='session_key']")
password = driver.find_element_by_xpath("//input[@name='session_password']")

username.send_keys('**************')
password.send_keys('*******')
time.sleep(2)

submit = driver.find_element_by_xpath("//button[@type='submit']").click()

# ************ ACTION **********




def action(x):
    driver.get(
        f'https://www.linkedin.com/search/results/people/?geoUrn=%5B%22105072130%22%5D&network=%5B%22S%22%5D&origin=FACETED_SEARCH&page={x}&sid=Hoc')
    time.sleep(2)
    all_buttons = driver.find_elements_by_tag_name("button")
    connect_buttons = [btn for btn in all_buttons if btn.text == "Connect"]
    texts_buttons = [btn.text for btn in all_buttons]
    print('-'*50, '\n', texts_buttons, '\n', '-'*50)
    for btn in connect_buttons:
        driver.execute_script("arguments[0].click();", btn)
        time.sleep(2)
        send = driver.find_element_by_xpath("//button[@aria-label='Send now']")
        driver.execute_script("arguments[0].click();", send)
    time.sleep(2)
    print('-------', '\n', 'This itterable stoped')
    x=x+1
    action(x)

action(3)
