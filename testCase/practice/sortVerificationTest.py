import re
from playwright.sync_api import Page,expect

def test_verify_page(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(2000)
    listDropdown = page.locator("#colors>option")

    originalList = [text.strip() for text in listDropdown.all_text_contents()]
    print("original List options",originalList)

    sortedList = sorted(originalList)
    print("Sorted List options",sortedList)

    if (originalList == sortedList):
        print("The list is sorted")
    else:
        print("The list is not sorted")

    from playwright.sync_api import Page


def handle_confirmation_alert(page: Page):

    # Handle confirmation dialog
    page.on(
        "dialog",
        lambda dialog: (
            print("Alert message:", dialog.message),
            dialog.accept()      # Use dialog.dismiss() to cancel
        )
    )

    # Click confirmation alert button
    page.locator("#confirmBtn").click()

def test_confirmation_alert(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    handle_confirmation_alert(page)
