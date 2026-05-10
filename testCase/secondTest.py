#CSS

#tag#id
# tag.class
#tag[attribute=value]
#tag.class[attribute=value]
import re
from playwright.sync_api import Page,expect


# page.get_by_alt_text() to locate an element, usually image, by its text alternative.
def test_verify_page(page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    page.wait_for_timeout(5000)
    page.locator("input#small-searchterms").fill("iphone")
    page.locator("#small-searchterms").fill("phone")

    #class
    page.locator(".ico-register").click()
    page.goto("https://demowebshop.tricentis.com/")
    page.wait_for_timeout(2000)
    #page.locator("a#ico-register").click()
    page.wait_for_timeout(5000)

    #attribute
    page.locator("input[name='NewsletterEmail']").fill("test@gmail.com")
    page.locator("[name='NewsletterEmail']").fill("1test@gmail.com")

    #class with attribute
    page.locator("input.search-box-text[id=small-searchterms]").fill("laptop")

   



