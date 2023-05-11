from pages.demoqa import DemoQA
from pages.element_page import ElementsPage
def test_navigation(browser):
    demo_qa_page = DemoQA(browser)
    elements_page = ElementsPage(browser)

    demo_qa_page.visit()
    DemoQA.click()
    ElementsPage.refresh()
    browser.refresh()
    browser.back()
    browser.forward()
    elements_page.equal_url()
