import re
from playwright.sync_api import Page,expect

def test_verify_page(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(2000)
    #Approach 1
    #page.locator('#datepicker').fill('12/12/2026')
    page.wait_for_timeout(2000)
    targetDate = "15"
    targetMonth = "December"
    targetYear = "2024"
    is_future = False
    datePicker = page.locator('#datepicker')
    datePicker.click()
    selectDate(page, targetDate, targetMonth, targetYear, is_future)
    page.wait_for_timeout(3000)
    expect(datePicker).to_have_value("12/15/2024")


def selectDate(page,targetDate,targetMonth,targetYear,is_future):
    while True:
        current_month = page.locator('.ui-datepicker-month').text_content()
        current_year=page.locator('.ui-datepicker-year').text_content()

        if current_month==targetMonth and current_year==targetYear:
            break
        if is_future==True:
            page.locator('.ui-datepicker-next').click()
        else:
            page.locator('.ui-datepicker-prev').click()

    allDates = page.locator(".ui-datepicker-calendar td").all()

    for date in allDates:
        date_text = date.inner_text()
        if(date_text==targetDate):
            date.click()
            break


