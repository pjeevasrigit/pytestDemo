import re
from playwright.sync_api import Page,expect

def test_verify_page(page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    page.wait_for_timeout(2000)
    products = page.locator("//h2[@class='product-title']//a")

    originalList = [text.strip() for text in products.all_text_contents()]
    print("original List options",originalList)

    sortedList = sorted(originalList)
    print("Sorted List options",sortedList)

    if (originalList == sortedList):
        print("The list is sorted")
    else:
        print("The list is not sorted")

