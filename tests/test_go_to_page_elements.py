from pages.demoqa import DemoQA
from pages.element_page import ElementsPage


def test_demo_page(browser):
    # demo_qa_page = DemoQA(browser)
    elements_page = ElementsPage(browser)
    elements_page.visit()
    # demo_qa_page.visit()
    # assert demo_qa_page.equal_url()
    # demo_qa_page.btn_elements.click()
    assert elements_page.equal_url()
    assert elements_page.icon.exist()
    assert elements_page.btn_sidebar_first.exist()
    assert elements_page.btn_sidebar_first_textbox.exist()


