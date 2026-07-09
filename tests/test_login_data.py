import pytest
from pages.login_page import LoginPage


@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        ("wronguser", "Password123", "Your username is invalid!"),
        ("student", "WrongPassword", "Your password is invalid!"),
        ("", "", "Your username is invalid!")
    ]
)
def test_invalid_login(page, username, password, expected_error):
    login_page = LoginPage(page)

    login_page.open()

    login_page.login(username, password)

    assert login_page.get_error_message() == expected_error