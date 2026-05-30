import re
from playwright.sync_api import Page,expect

def test_verify_page(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(2000)
    datePicker =page.locator('#txtDate') 
    datePicker.click()
    page.locator('.ui-datepicker-month').select_option("May")
    page.locator('.ui-datepicker-year').select_option("2027")

    allDates = page.locator(".ui-datepicker-calendar td a")
    page.wait_for_timeout(2000)

    for i in range(allDates.count()):
        date = allDates.nth(i)
        if date.inner_text().strip() == "25":
            date.click()
            break

    expect(datePicker).to_have_value("25/05/2027")
    