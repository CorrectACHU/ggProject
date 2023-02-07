# ENTER YOUR TEXT HERE
import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

prepared_text = 'test'


def test_post(driver: Chrome):
    text = "Hello world!"

    for p in driver.find_elements(by=By.TAG_NAME, value='span'):
        if p.text == 'Start a post':
            p.click()
            break
    time.sleep(2)

    post = driver.find_element(by=By.XPATH, value='//div[@aria-label="Text editor for creating content"]')
    post.send_keys(f'{text}')
    time.sleep(2)

    buttons = [b for b in driver.find_elements(by=By.TAG_NAME, value='button') if b.text == 'Post']
    buttons[0].click()
    time.sleep(4)

    print(f"The text '{text}', was posted!")

    driver.find_element(by=By.XPATH, value='//button[@aria-label="Dismiss"]').click()
    time.sleep(2)


