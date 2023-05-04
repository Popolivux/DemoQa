from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class WebElement:
    def __init__(self, driver, locator=''):
        self.driver = driver
        self.locator = locator


    def click(self):
        """" Click the element. """
        self.driver.find_element().click()

    def find_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.locator)

    def exist:
        try:
            self.icfind_element()
        except NoSuchElementException:
            return False
        return True