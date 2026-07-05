from pages.login_page import LoginPage


def test_valid_login(page):

    login_page = LoginPage(page)

    login_page.open()

    login_page.login(
        "student",
        "Password123"
    )

    assert "logged-in-successfully" in page.url