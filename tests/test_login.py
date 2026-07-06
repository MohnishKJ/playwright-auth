from pages.login_page import LoginPage


def test_valid_login(page):

    login_page = LoginPage(page)

    login_page.open()

    login_page.login(
        "student",
        "Password123"
    )

    assert "logged-in-successfully" in page.url


def test_invalid_username(page):

    login_page = LoginPage(page)

    login_page.open()

    login_page.login(
        "wronguser",
        "Password123"
    )

    assert login_page.get_error_message() == "Your username is invalid!"

def test_empty_credentials(page):

    login_page = LoginPage(page)

    login_page.open()

    login_page.login(
        "",
        ""
    )

    assert login_page.get_error_message() == "Your username is invalid!"

def test_invalid_password(page):

    login_page = LoginPage(page)

    login_page.open()

    login_page.login(
        "student",
        "WrongPassword"
    )

    assert login_page.get_error_message() == "Your password is invalid!"

def test_logout(page):

    login_page = LoginPage(page)

    login_page.open()

    login_page.login(
        "student",
        "Password123"
    )

    login_page.logout()

    assert "practice-test-login" in page.url