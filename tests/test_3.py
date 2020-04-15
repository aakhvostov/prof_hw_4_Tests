from config import *
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


url = 'https://passport.yandex.ru/auth/'

class TestBrowser:
    def __init__(self, url):
        self.driver = webdriver.Firefox(executable_path='\\Geckodriver\\geckodriver.exe')
        self.url = url

    def openUrl(self):
        self.driver.get(url)

    # LOGIN и PASSWORD передаётся как string
    def logIn(self):
        login = self.driver.find_element_by_xpath('//*[@id="passp-field-login"]')
        login.send_keys(LOGIN)
        enterButton = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/div[3]/div[2]/div/div/div[1]/form/div[3]/button[1]')
        enterButton.click()
        password = self.driver.find_element_by_xpath('//*[@id="passp-field-passwd"]')
        password.send_keys(PASSWORD)
        enterButton = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/div[3]/div[2]/div/div/form/div[2]/button[1]')
        enterButton.click()




if __name__ == '__main__':
    test = TestBrowser(url)
    test.openUrl()
    test.logIn()