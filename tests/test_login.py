from pages.login_page import LoginPage

VALID_USERNAME = "standard_user"
VALID_PASSWORD = "secret_sauce"

LOCKED_USERNAME = "locked_out_user"


def test_successful_login(page):
    """Happy path: valid credentials should land on the inventory page."""
    login_page = LoginPage(page)
    login_page.login(VALID_USERNAME, VALID_PASSWORD)

    # After login, SauceDemo redirects to /inventory.html
    assert "inventory.html" in page.url


def test_locked_out_user_shows_error(page):
    """Negative case: locked-out user should see a specific error message."""
    login_page = LoginPage(page)
    login_page.login(LOCKED_USERNAME, VALID_PASSWORD)

    error_text = login_page.get_error_text()
    assert "locked out" in error_text.lower()


def test_invalid_password_shows_error(page):
    """Negative case: wrong password should not log the user in."""
    login_page = LoginPage(page)
    login_page.login(VALID_USERNAME, "wrong_password")

    error_text = login_page.get_error_text()
    assert "do not match" in error_text.lower()
    assert "inventory.html" not in page.url