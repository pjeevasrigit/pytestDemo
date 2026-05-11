import re
from playwright.sync_api import Page,expect

def test_verify_page(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(2000)
    #method 1
    page.locator("#country").select_option("India")
    page.wait_for_timeout(2000)
    #method 2
    page.locator("#country").select_option(value="canada")
    page.wait_for_timeout(2000)
    #method 3
    page.locator("#country").select_option(label="France")
    page.wait_for_timeout(2000)
    #method 4
    page.locator("#country").select_option(index=3)
    page.wait_for_timeout(2000)

    countryDropdown = page.locator("#country>option")
    print("dropdown count",countryDropdown.count())
    expect(countryDropdown).to_have_count(10)
    print("dropdown options",countryDropdown.all_text_contents())

    dropdown_options = [text.strip() for text in countryDropdown.all_text_contents()]
    print("list values:",dropdown_options)
    
    for i in dropdown_options:
        print (i)