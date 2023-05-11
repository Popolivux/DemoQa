from pages.offtop_pages import Offtoppages
import time

def test_offtop_2(browser):
    login_form = Offtoppages(browser)

    login_form.visit()
    login_form.username.send_keys("standard_user")
    login_form.password.send_keys("secret_sauce")
    login_form.login.click()
    time.sleep(2)
    login_form.btn_1_item.click()
    time.sleep(2)
    login_form.btn_2_item.click()
    login_form.btn_shop.click()
    time.sleep(2) # проверить
    assert login_form.btn_1_item_remove.visible()
    assert login_form.btn_2_item_remove.visible()
    login_form.btn_1_item_remove.click()
    login_form.btn_2_item_remove.click()
    time.sleep(3)
    # assert not login_form.btn_1_item_remove.visible()
    # assert not login_form.btn_2_item_remove.visible()