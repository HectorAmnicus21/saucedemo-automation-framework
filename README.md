# SauceDemo Automation Framework

UI test automation framework for [saucedemo.com](https://www.saucedemo.com/) built with Python, pytest and Playwright, using the Page Object pattern.

## What is covered
- Successful login (standard_user)
- Locked-out user error message
- Invalid password error message

## Project structure
```
conftest.py        # pytest fixture: fresh browser/page per test
pages/             # Page Objects (LoginPage)
tests/             # test cases
```

## How to run
```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium
pytest tests -v
```

## Tech stack
Python, pytest, Playwright