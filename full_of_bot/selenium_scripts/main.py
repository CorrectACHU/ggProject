import os
import time
from selenium.webdriver import Chrome

from dotenv import load_dotenv
from selenium.webdriver.common.by import By

from bot_linkedin.selenium_scripts.using_driver import Driver

load_dotenv()


def enter_the_matrix():
    driver_type = os.getenv('DRIVER_TYPE')
    status = "[-] Status wasn't changed"
    try:
        driver = Driver(driver_type).get_driver()
        driver.get('https://linkedin.com')
        time.sleep(2)

        status = '[+] Your driver was received'
        # *********LOG IN************
        username = driver.find_element(by=By.XPATH, value="//input[@name='session_key']")
        password = driver.find_element(by=By.XPATH, value="//input[@name='session_password']")

        # INPUT YOURS LOGIN AND PASSWORD HERE
        username.send_keys(os.getenv('EMAIL'))
        password.send_keys(os.getenv('PASSWORD'))
        time.sleep(2)

        driver.find_element(by=By.XPATH, value="//button[@type='submit']").click()

        return driver
    except AttributeError:
        status = "[-] Your driver wasn't received"
        print("[-] wrong type of driver, should be 'local' or 'remote' ")
    finally:
        print(f"[+] enter_the_matrix function was executed  with STATUS: {status}")


def get_filters(driver: Chrome = None) -> dict:
    if driver:
        url = "https://www.linkedin.com/search/results/people/?origin=SWITCH_SEARCH_VERTICAL&sid=%3AXL"
        driver.get(url)
        time.sleep(2)

        look_filters = driver.find_element(by=By.XPATH,
                                           value="//button[@aria-label='Show all filters. Clicking this button displays all available filter options.']")
        look_filters.click()
        time.sleep(2)

        count_fltr_groups = driver.find_elements(By.XPATH,
                                                 value="//ul/li[@class='search-reusables__secondary-filters-filter']")
        prepared_dict = {}
        for i in range(1, len(count_fltr_groups) + 1):
            h3 = driver.find_element(by=By.XPATH,
                                     value=f"//ul/li[@class='search-reusables__secondary-filters-filter']{[i]}//h3")
            find_spans = driver.find_elements(by=By.XPATH,
                                              value=f"//ul/li[@class='search-reusables__secondary-filters-filter']{[i]}//span[@class='t-14 t-black--light t-normal']")
            if find_spans:
                prepared_dict[h3.text] = [f.text for f in find_spans]

        print("[+] " + "Your filters got prepared!")
        return prepared_dict
    else:
        raise Exception("[-] driver wasn't received")


def set_filters(driver: Chrome = None, filters: dict = None):
    filters_list = ['1st', 'Poland', 'Computer Software']
    filters = filters
    filters_by_fieldset = [ftrs for ftrs in driver.find_elements(by=By.XPATH,
                                                                 value="//span[@class='t-14 t-black--light t-normal']")]
    for f in filters_by_fieldset:
        for f_l in filters_list:
            if f.text == f_l:
                f.click()


def main():
    driver = enter_the_matrix()
    filters = get_filters(driver)
    set_filters(driver, filters)


if __name__ == '__main__':
    main()
