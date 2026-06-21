from pathlib import Path

import pytest
from slugify import slugify
import allure


@pytest.fixture()
def set_up_tear_down(page):
    page.set_viewport_size({"width": 1536, "height": 800})
    page.goto("https://www.saucedemo.com")
    yield page


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    pytest_html = item.config.pluginmanager.getplugin("html")

    outcome = yield
    report = outcome.get_result()

    extra = getattr(report, "extra", [])

    if report.when == "call":

        xfail = hasattr(report, "wasxfail")

        if (report.failed or xfail) and "page" in item.funcargs:

            page = item.funcargs["page"]

            screenshot_dir = Path("screenshots")
            screenshot_dir.mkdir(exist_ok=True)

            screen_file = str(
                screenshot_dir / f"{slugify(item.nodeid)}.png"
            )

            page.screenshot(path=screen_file)

            if pytest_html:
                extra.append(
                    pytest_html.extras.png(screen_file)
                )

            allure.attach.file(
                screen_file,
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )

        report.extra = extra