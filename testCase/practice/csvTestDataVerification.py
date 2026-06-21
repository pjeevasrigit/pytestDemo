import pytest
from playwright.sync_api import Page
import csv

test_data = []

with open("testCase/testData/test_data.csv", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        test_data.append(
            (row["name"], row["mail"], row["phone"])
        )

@pytest.mark.parametrize("name, mail, phone", test_data)
def test_verify_page(page: Page, name, mail, phone):
    page.goto("https://testautomationpractice.blogspot.com/")

    page.locator("#name").fill(name)
    page.locator("#email").fill(mail)
    page.locator("#phone").fill(phone)