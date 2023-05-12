from pages.modal_dialog import ModalDialog
from pages.demoqa import DemoQA

def test_modal_elements(browser):
    modaldialog = ModalDialog(browser)
    demo_qa_pages = DemoQA(browser)
    modaldialog.visit()

    assert modaldialog.btn_sidebar_first_child.check_count_elements(count=5)

    browser.refresh()
    modaldialog.icon.click()
    browser.back()
    browser.set_window_size(900, 400)
    browser.forward()
    assert browser.current_url == demo_qa_pages.base_url
           # "https://demoqa.com/" #уточнить овозможности подтянуть из demoqa
    assert browser.title == demo_qa_pages.pageData["title"]
    browser.set_window_size(1000, 1000)