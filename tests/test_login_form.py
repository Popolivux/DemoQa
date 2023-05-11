from pages.form_page import FormPages
import time

def test_login_form(browser):
    login_form = FormPages(browser)

    login_form.visit()
    assert not login_form.modal_dialog.exist()
    time.sleep(2)
    login_form.first_name.send_keys("tester")
    login_form.last_name.send_keys("testerovich")
    login_form.user_email.send_keys("test@ttt.tt")
    login_form.gender_radio_1.click()
    login_form.user_number.send_keys("9992223344")
    time.sleep(2)
    login_form.btn_submit.click()
    time.sleep(2)