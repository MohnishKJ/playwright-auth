from playwright.sync_api import sync_playwright


def test_valid_login():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        page.goto("https://practicetestautomation.com/practice-test-login/")

        page.fill("#username", "student")

        page.fill("#password", "Password123")

        page.click("#submit")

        assert "logged-in-successfully" in page.url

        browser.close()