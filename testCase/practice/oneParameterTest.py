import re
import pytest
from playwright.sync_api import Page, expect

search_names = ["phone", "laptop", "desktop"]

@pytest.mark.parametrize("item", search_names)
def test_verify_page(page: Page, item):
    page.goto("https://demowebshop.tricentis.com/")

    page.locator("#small-searchterms").fill(item)
    page.locator(".button-1.search-box-button").click()
    page.wait_for_timeout(3000)

    first_result = page.locator("h2 a").first

    expect(first_result).to_have_text(
        re.compile(item, re.IGNORECASE)
    )