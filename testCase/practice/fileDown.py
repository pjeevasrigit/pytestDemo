
import re
from playwright.sync_api import Page,expect

def test_verify_filedownload(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
   # file download
    page.wait_for_timeout(2000)
    page.locator("a:has-text('Download Files')").click()
    page.wait_for_timeout(2000)
    page.locator("#inputText").nth(0).fill("Creating download file")
    def handleDownload(download):
        download.save_as("downloads/testfile.txt")

    page.on("download",handleDownload)
    page.locator("#generateTxt").click()
    page.wait_for_timeout(2000)