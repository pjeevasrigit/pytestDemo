import re
from playwright.sync_api import Page,expect

def test_verify_page(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(2000)
    page.locator("#name").fill("tester")
    page.locator("#email").fill("test@gmail.com")
    page.locator("#phone").fill("989777788222")
    GenderValue = "male"
    page.locator(f"//input[@class='form-check-input' and @value='{GenderValue}']").click()
    page.wait_for_timeout(2000)


    #Select all days - method 1
    daysCheckbox = page.locator("//input[@class='form-check-input' and @type='checkbox']")
    count = daysCheckbox.count()

    for i in range(count):
        daysCheckbox.nth(i).check()

    getDaysCheckbox = page.locator("//input[@class='form-check-input' and @type='checkbox']//label")    
    print(getDaysCheckbox.all_text_contents())
  

    #method -2 
    days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    checkboxes = []

    for day in days:
        checkbox = page.get_by_label(day)
        checkboxes.append(checkbox)
    print("total number of days method 2:", len(checkboxes))
    print("Print days list:", days)
    

    #method - 3
    allCheckboxes = [page.get_by_label(day) for day in days]
    print("total number of days method 3:", len(allCheckboxes))

    for checkbox in checkboxes:
        checkbox.uncheck()
        expect(checkbox).not_to_be_checked()

    page.wait_for_timeout(2000)
    for checkbox in checkboxes[-3:]:
        page.wait_for_timeout(1000)
        checkbox.check()
        expect(checkbox).to_be_checked()