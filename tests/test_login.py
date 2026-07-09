from pages.login_page import LoginPage


def test_valid_login(page):

    login_page = LoginPage(page)

    login_page.open()

    login_page.login(
        "student",
        "Password123"
    )

    assert "logged-in-successfully" in page.url
    assert login_page.get_success_message() == "Logged In Successfully"
    assert login_page.is_logout_visible()


def test_logout(page):

    login_page = LoginPage(page)

    login_page.open()

    login_page.login(
        "student",
        "Password123"
    )

    login_page.logout()

    assert "practice-test-login" in page.url