# Playwright Auth 🚀

A simple UI login automation project built with **Python**, **Playwright**, and **Pytest** using the **Page Object Model (POM)**.

## Tech Stack

* Python
* Playwright
* Pytest

## Features

* ✅ Positive Login Test
* ✅ Invalid Username Test
* ✅ Invalid Password Test
* ✅ Empty Credentials Test
* ✅ Logout Test
* ✅ Page Object Model (POM)
* ✅ Pytest Fixtures
* ✅ HTML Test Reports
* ✅ Pytest Configuration

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

The tests are written against the Practice Test Automation login page:

https://practicetestautomation.com/practice-test-login/

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Tests

```bash
python -m pytest
```

## Generate HTML Report

```bash
python -m pytest --html=reports/report.html --self-contained-html
```
