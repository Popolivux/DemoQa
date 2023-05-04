from pages.demoqa import DemoQA
from pages.element_page import ElementsPage


def test_demo_page(browser):
    demo_qa_page = DemoQA(browser)
    elements_page = ElementsPage(browser)
    demo_qa_page.visit()
    assert demo_qa_page.equal_url()
    demo_qa_page.btn_elements.click()
    assert elements_page.equal_url()



