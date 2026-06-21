from playwright.sync_api import Playwright, expect

def test_browser(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)

    context = browser.new_context()

    page1 = context.new_page()
    page1.goto("https://testautomationpractice.blogspot.com/")
    
    with page1.expect_popup() as popup_info:
        page1.locator("#PopUp").click()

    popup = popup_info.value
    popup.wait_for_load_state()

    all_popups = context.pages
    print("Total pages:", len(all_popups))

    for window in all_popups:
        print("Pop up URL ==========>", window.url)

        title = window.title()
        print("Title:", title)

        if "Selenium" in title:
            window.wait_for_timeout(3000)
            window.locator("span:has-text('Documentation')").click()
            expect(window.locator("#print")).to_have_text(" Print entire section") 
            window.wait_for_timeout(3000)
            window.close()           
    
    context.close()
    browser.close()
