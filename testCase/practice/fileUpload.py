
import re
from playwright.sync_api import Page,expect

def test_verify_page(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
   # single file upload
    page.wait_for_timeout(2000)
    page.locator("#singleFileInput").set_input_files("pytestDemo\\uploads\\test1.txt")
    page.locator("button:has-text('Upload Single File')").click()
    page.wait_for_timeout(2000)
    # multi file upload
    fileList = ["pytestDemo/uploads/test1.txt",
        "pytestDemo/uploads/test2.txt"]
    page.locator("#multipleFilesInput").set_input_files(fileList)
    page.locator("button:has-text('Upload Multiple Files')").click()
    page.wait_for_timeout(2000)





    