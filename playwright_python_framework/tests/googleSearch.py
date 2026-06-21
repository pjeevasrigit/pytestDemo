from playwright.sync_api import expect
from pages.googlePage import GooglePage


def test_google_search(page):

    google = GooglePage(page)

    google.open_google()

    google.search("Playwright Python")

    expect(page).to_have_title(
        lambda title: "Playwright" in title
    )