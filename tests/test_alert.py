from pages.allerts import Alerts
import time

def test_alert(browser):
    alert_page = Alerts(browser)
    alert_page.visit()
    assert not alert_page.alert() #причина ошибки (не подтягивается метод)
    alert_page.alertButton.click()
    time.sleep(2)
    assert alert_page.alert()
    alert_page.alert().accept()

def test_text_alert(browser):
    alert_page = Alerts(browser)
    alert_page.visit()
    alert_page.alertButton.click()
    time.sleep(2)
    assert alert_page.alert().text == "You clicked a button"
    alert_page.alert().accept()
    assert not alert_page.alert()