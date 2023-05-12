from pages.offtop_pages import Offtoppages
import time

def test_oftop3(browser):
    login_form = Offtoppages(browser)

    login_form.visit()
    login_form.username.send_keys("standard_user")
    login_form.password.send_keys("secret_sauce")
    login_form.login.click()
    time.sleep(2)
    login_form.btn_1_item.click()
    login_form.btn_2_item.click()
    time.sleep(1)
    login_form.btn_shop.click()
    time.sleep(2)
    login_form.btn_main_menu.click()
    login_form.btn_logout.click()
    login_form.username.send_keys("standard_user")
    login_form.password.send_keys("secret_sauce")
    login_form.login.click()
    login_form.btn_shop.click()
    assert login_form.card_1_item.exist()
    assert login_form.card_2_item.exist()
    login_form.btn_1_item_remove.click()
    login_form.btn_2_item_remove.click()
    assert not login_form.card_1_item.exist()
    assert not login_form.card_2_item.exist()