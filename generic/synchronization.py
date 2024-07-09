from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import ElementNotInteractableException


def _wait(func):
    def wrapper(*args,**kwargs):
        print(*args)
        instance = args[0]
        locator = args[1]
        wait_element = WebDriverWait(instance.driver,10)
        element = wait_element.until(expected_conditions.visibility_of_element_located(locator),message=f"{locator} not found")
        print(*args)
        if element.is_enabled():
            return func(*args,**kwargs)
        raise ElementNotInteractableException(f"{locator} not interactable")

    return wrapper()