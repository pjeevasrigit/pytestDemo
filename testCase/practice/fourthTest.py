import re
from playwright.sync_api import Page,expect


# page.get_by_alt_text() to locate an element, usually image, by its text alternative.
def test_verify_page(page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    logo = page.get_by_alt_text("Tricentis Demo Web Shop")
    expect(logo).to_be_visible
    logo.click()

    #get_by_text Example
    page.goto("https://demowebshop.tricentis.com/")
    text = page.get_by_text("Popular")
    expect (text).to_be_visible

    #get_by_role
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html#")
    #computerButton = page.get_by_role("input",name="Accept terms")
    page.wait_for_timeout(2000)
   # computerButton.click()
    

    page.get_by_label("Email Address").fill("test@gmail.com")
    page.wait_for_timeout(2000)
    page.get_by_label("Password").fill("pass@123")
    page.get_by_label("Your Age").fill("12")
    page.wait_for_timeout(2000)

    page.get_by_placeholder("Enter your full name").fill("myFullName")

    page.get_by_title("HyperText Markup Language").click

    page.get_by_test_id("edit-profile-btn").click()
    page.wait_for_timeout(2000)


    



