from pages.element_page import ElementsPage

def test_page_element(browser):
    elements_page = ElementsPage(browser)
    elements_page.visit()
    assert elements_page.text_elements.get_text() == "Elements"

# def test_check_text(browser):
#     element_page = ElementsPage(browser)
#     element_page.visit()
#     assert element_page.text_elements.get_text() == "Please select an item from left to start practice."
#
#

