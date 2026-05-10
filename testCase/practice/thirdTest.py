import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demowebshop.tricentis.com/")
    page.locator("#small-searchterms").click()
    page.locator("#small-searchterms").fill("apple phone")
    page.get_by_role("button", name="Search").click()
    page.get_by_role("link", name="Electronics").nth(1).click()
    page.get_by_role("link", name="Apparel & Shoes").first.click()
    page.locator("#small-searchterms").click()