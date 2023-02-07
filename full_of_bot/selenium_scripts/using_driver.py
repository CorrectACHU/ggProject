from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


class Driver:
    _options = Options()

    def __init__(self, type_driver):
        self.type_driver = type_driver

    @property
    def type_driver(self):
        return self._type_driver

    @type_driver.setter
    def type_driver(self, value: str):
        if type(value) == str and value.upper() not in ["remote".upper(), "local".upper()]:
            raise Exception("[-] Driver can be only 'REMOTE' or 'LOCAL'")
        else:
            self._type_driver = value

    def get_driver(self):
        if self._type_driver.upper() == 'Remote'.upper():
            options = webdriver.ChromeOptions()
            print(f'[+] REMOTE DRIVER ARE PREPARING')
            driver = webdriver.Remote(command_executor="http://127.0.0.1:4444/wd/hub", options=options)
            print(f'[+] YOUR DRIVER IS {driver.name}')
            return driver
        else:
            options = Options()
            service = Service("/usr/bin/chromedriver")
            service.start()
            print('[+] LOCAL DRIVER ARE PREPARING')
            driver = webdriver.Chrome(service=service, options=options)
            print(f'[+] YOUR DRIVER IS {driver.name}')
            return driver
