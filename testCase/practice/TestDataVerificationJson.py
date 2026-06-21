import pytest
from playwright.sync_api import Page
import json

with open("testCase/testData/test_data.json", "r") as file:
    test_data = json.load(file)

@pytest.mark.parametrize(
    "name, mail, phone",
    [(data["name"], data["mail"], data["phone"]) for data in test_data]
)
def test_verify_page(page: Page, name, mail, phone):
    page.goto("https://testautomationpractice.blogspot.com/")

    page.locator("#name").fill(name)
    page.locator("#email").fill(mail)
    page.locator("#phone").fill(phone)
    page.wait_for_timeout(2000)