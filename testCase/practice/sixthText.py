import re
from playwright.sync_api import Page,expect

#Xpath


# page.get_by_alt_text() to locate an element, usually image, by its text alternative.
def test_verify_page(page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    page.wait_for_timeout(5000)
    #xpath path examples
    page.locator("//input[@id='small-searchterms']").fill("books")
    page.locator("//input[@value='Search']").click()

    #
    page.goto("https://demowebshop.tricentis.com/")
    products = page.locator("//h2/a[contains(@href,'computer')]")
    print("Computer product count",products.count)
    
    print("first product",products.first.text_content())
    print("last product",products.last.text_content())
    print("third product",products.nth(2).text_content())

    product_title = products.all_text_contents()
    print("All titles", product_title)

    for i in product_title:
        if (i == 'Simple Computer'):
            print('Test case Pass')



