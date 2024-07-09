
from generic.wrapper import Selenium_wrapper

class LoginPage(Selenium_wrapper):
    login_id=("id", "email")
    login_pass=("id", "pass")
    login_click=("xpath","//button[@type='submit']")

    def __init__(self,driver,username,password):
        self.driver = driver
        self.username = username
        self.password = password

    def login(self):
        self.click_element(*self.login_id).send_keys(ussername=self.username)
        self.enter_text(*self.login_pass).send_keys(password=self.password)
        self.click_element(*self.login_click).click()
