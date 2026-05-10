import re
from playwright.sync_api import Page,expect

#Xpath


# page.get_by_alt_text() to locate an element, usually image, by its text alternative.
def test_verify_page(page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    page.wait_for_timeout(5000)
    #xpath path examples
    search=page.locator("//input[@id='small-searchterms']")
    submitButton=page.locator("//input[@value='Search']")
    expect(search).to_be_enabled()
    expect(search).to_be_visible()
    search.fill("books")
    enteredValue=search.input_value()
    print("Entered value in Search box",enteredValue)
    submitButton.click()
    page.wait_for_timeout(2000)

    products = page.locator("//h2/a[contains(@href,'computer')]")
    expect(products).not_to_be_visible()

    
