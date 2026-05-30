import re
from playwright.sync_api import Playwright, expect


def test_verify_page(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(
        record_video_dir="videos/",
        record_video_size={"width":1024,"height":768}
    )
    page = context.new_page()

    page.goto("https://testautomationpractice.blogspot.com/")

    # Wait for popup
    with page.expect_popup() as popup_info:
        page.locator("#PopUp").click()

    popup = popup_info.value
    popup.wait_for_load_state()

    all_popups = context.pages
    print("Total pages:", len(all_popups))

    for pw in all_popups:
        print("Pop up URL ==========>", pw.url)

        title = pw.title()
        print("Title:", title)

        if "Playwright" in title:
            pw.locator(".getStarted_Sjon").click()
            expect(pw).to_have_title("Installation.*Playwright")
            

    context.close()
    browser.close()