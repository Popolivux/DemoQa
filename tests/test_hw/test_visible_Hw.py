from pages.accordion import Accordion
import time

def test_visible(browser):
    element_page = Accordion(browser)
    element_page.visit()
    assert element_page.section1_content.visible()
    element_page.headding.click()
    time.sleep(2)
    assert not element_page.section1_content.visible()

def test_visible_accordion_default(browser):
    element_page = Accordion(browser)
    element_page.visit()

    assert not element_page.section2_p_1.visible()
    assert not element_page.section2_p_2.visible()
    assert not element_page.section3_p.visible()
