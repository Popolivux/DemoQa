from pages.modal_dialog import ModalDialog

def test_modal_elements(browser):
    modaldialog = ModalDialog(browser)
    modaldialog.visit()

    assert modaldialog.btn_modal_dialogs.check_count_elements(count=5)