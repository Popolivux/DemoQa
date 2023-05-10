from pages.base_page import BasePage
from components.components import WebElement
class Accordion(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)

        self.text_content = WebElement(driver, "#section1Content > p")
        self.headding = WebElement(driver, '##section1Heading')
