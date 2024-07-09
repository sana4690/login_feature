

class Selenium_wrapper:
    def __init__(self,driver):
        self.driver = driver


    def click_element(self, locator):
        self.driver.find_element(*locator).click()


    def enter_text(self, locator, *, value):
        self.driver.find_element(*locator).send_keys(value)