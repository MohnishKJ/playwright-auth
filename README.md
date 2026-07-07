# Playwright Auth 🚀

Simple UI login automation project built with Python, Playwright, and Pytest.

## Tech Stack

- Python
- Playwright
- Pytest

## Features

- Positive Login Test
- Invalid Username Test
- Invalid Password Test
- Empty Credentials Test
- Logout Test
- Page Object Model (POM)
- Pytest Fixtures
- HTML Test Reports
- Pytest Configuration

## Project Structure

```text
playwright-auth/
├── pages/
│   └── login_page.py
├── reports/
├── screenshots/
├── tests/
│   └── test_login.py
├── conftest.py
├── pytest.ini
├── requirements.txt
├── README.md
└── .gitignore
```

## Test Website

Tests are written against the Practice Test Automation login page:

https://practicetestautomation.com/practice-test-login/

## Run

```bash
python -m pytest
```

## Generate HTML Report

```bash
python -m pytest --html=reports/report.html --self-contained-html
```
