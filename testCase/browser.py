import re
from playwright.sync_api import Page,expect, Playwright

def test_verify_page(playwright:Playwright):
    chromium=playwright.chromium
    browser=chromium.launch(headless=False)
    context=browser.new_context()
    page1=context.new_page()
    page2=context.new_page()

    page1.goto("https://playwright.dev/")
    page1.wait_for_timeout(2000)
    
    expect(page1).to_have_title('Fast and reliable end-to-end testing for modern web apps | Playwright')

    page2.goto("https://www.selenium.dev/")

    page2.wait_for_timeout(2000)
    
    expect(page2).to_have_title('Selenium')

    
