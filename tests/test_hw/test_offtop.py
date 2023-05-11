from pages.offtop_pages import Offtoppages
import time

def test_offtop(browser):
    login_form = Offtoppages(browser)

    login_form.visit()
    login_form.username.send_keys("standard_user")
    login_form.password.send_keys("secret_sauce")
    login_form.login.click()
    time.sleep(2)

    assert browser.current_url == "https://www.saucedemo.com/inventory.html"

