import re
from playwright.sync_api import Page,expect

def test_verify_page(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(2000)
    maleRadioButton = page.locator("#male")
    expect(maleRadioButton).not_to_be_checked()
    maleRadioButton.click()
    page.wait_for_timeout(2000)
    expect(maleRadioButton).to_be_checked()    

    nameTextBox = page.locator("#name")
    print("maxlength:", nameTextBox.get_attribute("maxlength"))
    expect(nameTextBox).to_have_attribute('maxlength','15')

    expect(page.locator("#email")).to_have_attribute('placeholder','Enter EMail')

    