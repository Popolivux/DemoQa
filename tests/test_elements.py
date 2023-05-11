from pages.element_page import ElementsPage

def test_find_elements(browser):
    elem_pages = ElementsPage(browser)
    elem_pages.visit()

    assert elem_pages.btn_first_menu.check_count_elements(count=9)