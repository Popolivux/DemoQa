from pages.accordion import Accordion
import time

# def test_visible(browser):
#     element_page = Accordion(browser)
#     element_page.visit()
#     assert element_page.text_content.visible()
def test_visible2(browser):
    element_page = Accordion(browser)
    element_page.visit()
    assert element_page.text_content.visible()
    element_page.headding.click()
    time.sleep(2)
    assert element_page.text_content.visible()