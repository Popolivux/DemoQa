from pages.text_box import TextBox
import time

def test_text_box(browser):
    text_box = TextBox(browser)

    text_box.visit()
    text_box.full_name.send_keys("tester")
    time.sleep(2)
    text_box.current_adress.send_keys('saintP')
    time.sleep(2)
    text_box.btn_text_box_submit.click_force()
    assert text_box.full_name.get_text() == "Full Name"
    assert text_box.current_adress.get_text() == "Current Address"
