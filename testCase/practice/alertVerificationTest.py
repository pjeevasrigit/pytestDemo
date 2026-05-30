from cmath import exp
import re
from playwright.sync_api import Page,expect

def test_verify_page(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
   #simple Alert
    page.wait_for_timeout(2000)
    def handle_dialog(dialog):
        dialog.accept()

    page.on("dialog",handle_dialog)
    page.wait_for_timeout(2000)

    page.locator('#alertBtn').click()
    page.wait_for_timeout(2000)
    
    #confirmation alert

    #confirmBtn

    page.on(
        "dialog",lambda dialog: (
            print("Alert message:", dialog.message),
            dialog.accept()      # Use dialog.dismiss() to cancel
        )
    )

    # Click confirmation alert button
    page.wait_for_timeout(2000)
    page.locator("#confirmBtn").click()

