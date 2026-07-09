import os
import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def page(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        yield page

        if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
            os.makedirs("screenshots", exist_ok=True)
            page.screenshot(
                path=f"screenshots/{request.node.name}.png",
                full_page=True
            )

        browser.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)