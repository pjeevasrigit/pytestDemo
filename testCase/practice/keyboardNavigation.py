from cmath import exp
import re
from playwright.sync_api import Page,expect

def test_verify_page(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
   # keyboard actions
    page.wait_for_timeout(2000)
    field1=page.locator("#input1")
    field1.focus()
    page.keyboard.insert_text("welcome")
    page.wait_for_timeout(2000)
    page.keyboard.press("Control+A")
    page.keyboard.press("Control+C")
    page.keyboard.press("Tab")
    page.keyboard.press("Tab")
    page.wait_for_timeout(4000)
    page.keyboard.press("Control+V")
    page.wait_for_timeout(2000)