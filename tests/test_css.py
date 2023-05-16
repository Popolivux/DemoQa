from pages.text_box import TextBox
import time

def test_css(browser):
    text_box = TextBox(browser)

    text_box.visit()

    assert text_box.btn_text_box_submit.check_css("color", 'rgba(255, 255, 255, 1)')