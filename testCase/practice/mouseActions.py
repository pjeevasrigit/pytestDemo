from cmath import exp
import re
from playwright.sync_api import Page,expect

def test_verify_page(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
   # left click and hover
    page.wait_for_timeout(2000)
    pointMe = page.locator("button:has-text('Point Me')")
    pointMe.hover()
    mobileOptions = page.locator(".dropdown-content a").nth(0)
    print('text',mobileOptions.text_content())
    page.wait_for_timeout(2000)
    mobileOptions.click()
    page.wait_for_timeout(2000)
    
    # right click
    pointMe.click(button='right')
    page.wait_for_timeout(2000)
    pointMe.hover()
    
    # scroll to end
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    page.wait_for_timeout(2000)
    
    # double click 
    copyText = page.locator("button:has-text('Copy Text')")
    copyText.dblclick()
    field2 = page.locator("#field2")
    expect(field2).to_have_value("Hello World!")
    page.wait_for_timeout(2000)
    
    #drag and drop
    source = page.locator("#draggable")
    target = page.locator("#droppable")

    #Approach 1
    source.hover()
    page.mouse.down()
    target.hover()
    page.mouse.up()
    page.wait_for_timeout(2000)

    #approach 2
    source.drag_to(target)
