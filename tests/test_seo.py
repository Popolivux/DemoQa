from pages.demoqa import DemoQA

def test_seo(browser):
    demo_qa_pages = DemoQA(browser)

    demo_qa_pages.visit()
    assert browser.title == demo_qa_pages.pageData['title']
