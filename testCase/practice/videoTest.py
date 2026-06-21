import re
from playwright.sync_api import Playwright,expect 

def test_verify_page(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(
        record_video_dir="videos/",
        record_video_size={"width":1024,"height":768}
    )
    page = context.new_page()

    page.goto("https://demowebshop.tricentis.com/")
    logo = page.get_by_alt_text("Tricentis Demo Web Shop")
    expect(logo).to_be_visible
    logo.click()


    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html#")
    page.wait_for_timeout(2000)
    page.get_by_label("Email Address").fill("test@gmail.com")
    page.wait_for_timeout(2000)
    page.get_by_label("Password").fill("pass@123")
    page.get_by_label("Your Age").fill("12")
    page.wait_for_timeout(2000)