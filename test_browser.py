import pytest
from playwright.sync_api import Page, expect
from login_page import LoginPage

def test_successful_login(page: Page):
    login_page = LoginPage(page)
    login_page.go_to()
    login_page.login("tomsmith", "SuperSecretPassword!")
    expect(page.locator(login_page.success_message)).to_be_visible()
    page.screenshot(path="screenshots/successful_login.png")
    print("Test PASS: Login successful - screenshot saved")

def test_failed_login(page: Page):
    login_page = LoginPage(page)
    login_page.go_to()
    login_page.login("wronguser", "wrongpassword")
    expect(page.locator(login_page.error_message)).to_be_visible()
    page.screenshot(path="screenshots/failed_login.png")
    print("Test PASS: Error shown - screenshot saved")