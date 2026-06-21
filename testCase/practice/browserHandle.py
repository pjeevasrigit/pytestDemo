from playwright.sync_api import Playwright, expect

def test_browser(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)

    context = browser.new_context()

    page1 = context.new_page()
    page2 = context.new_page()

    page1.goto("https://playwright.dev/")
    page1.wait_for_timeout(3000)
    page2.goto("https://testautomationpractice.blogspot.com/")
    page2.wait_for_timeout(3000)

    expect(page1).to_have_title("Fast and reliable end-to-end testing for modern web apps | Playwright")
    expect(page2).to_have_title("Automation Testing Practice")
