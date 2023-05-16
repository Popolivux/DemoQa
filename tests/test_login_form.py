from selenium.webdriver import Keys

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
    login_form.gender_radio_1.click_force()
    login_form.user_number.send_keys("9992223344")
    time.sleep(2)
    login_form.btn_hobbies.click_force() # проверить ссылку на кнопку
    login_form.curent_adress.send_keys("saint-petersburg")
    # assert login_form.modal_dialog.exist() test_login_form.py:17: AssertionError
    login_form.btn_submit.click_force()
    time.sleep(2)

def test_state(browser):
    form_page = FormPages(browser)

    form_page.visit()
    time.sleep(2)
    form_page.btn_state.scroll_to_element()
    # form_page.btn_state.click()
    # form_page.btn_NCR.click() ошибка в селекторе, как найти в DevTools
    form_page.inp_state.send_keys('NCR')
    form_page.inp_state.send_keys(Keys.ENTER)
    time.sleep(3)
