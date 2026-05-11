import re
from playwright.sync_api import Page,expect

def test_verify_page(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(2000)
    #method 1
    page.locator("#colors").select_option("Red")
    page.wait_for_timeout(2000)
    #method 2
    page.locator("#colors").select_option(value=["green","white"])
    page.wait_for_timeout(2000)
    #method 3
    page.locator("#colors").select_option(label=["Blue","Red"])
    page.wait_for_timeout(2000)
    #method 4 - index
    page.locator("#colors").select_option(index=[0,3])
    page.wait_for_timeout(2000)

    dropdown_multi = page.locator("#colors>option")
    expect(dropdown_multi).to_have_count(7)