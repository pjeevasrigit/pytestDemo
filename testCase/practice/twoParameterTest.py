import pytest
from playwright.sync_api import Page

test_data = [
    ("jeevasri", "jeevasri@gmail.com", "9894455"),
    ("mukesh", "mukesh@gmail.com", "9876543"),
    ("yukesh", "yukesh@gmail.com", "9876543")
]

@pytest.mark.parametrize("name, mail, phoneNumber", test_data)
def test_verify_page(page: Page, name, mail, phoneNumber):
    page.goto("https://testautomationpractice.blogspot.com/")

    page.locator("#name").fill(name)
    page.locator("#email").fill(mail)
    page.locator("#phone1").fill(phoneNumber)