from pages.demoqa import DemoQA


# def test_icon_exist(browser):
    # browser.get("https://demoqa.com/")
    # icon = browser.find_element(By.CSS_SELECTOR, "#app > header > a")
    #
    # if icon is None:
    #     print("не найден")
    # else:
    #     print("найден")
def test_icon_exist(browser):
    demo_qa_page = DemoQA(browser)
    demo_qa_page.visit()
    demo_qa_page.icon.click()
    assert demo_qa_page.equal_url()
    assert demo_qa_page.exit_icon()



