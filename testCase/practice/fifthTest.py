import re
from playwright.sync_api import Page,expect

#CSS

#tag#id
# tag.class
#tag[attribute=value]
#tag.class[attribute=value]


# page.get_by_alt_text() to locate an element, usually image, by its text alternative.
def test_verify_page(page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    page.wait_for_timeout(5000)
    page.locator("input#small-searchterms").fill("iphone")
    page.locator("#small-searchterms").fill("phone")

    # tag.class
    page.locator("div.view-all").click()

    #tag[]
    page.locator("input[name='NewsletterEmail']").fill("test@gmail.com")
    page.locator("#newsletter-subscribe-button").click()
    page.wait_for_timeout(2000)

    #tag.class[attribute=value]
    page.locator("div.product-item[data-productid='16']").click()
    page.wait_for_timeout(2000)
