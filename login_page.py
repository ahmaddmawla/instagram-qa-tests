import pytest
from playwright.sync_api import Page, expect
from login_page import LoginPage

def test_successful_login(page: Page):
    # Create the login page object
    login_page = LoginPage(page)
    
    # Use clean, readable actions
    login_page.go_to()
    login_page.login("tomsmith", "SuperSecretPassword!")
    
    # Verify success
    expect(page.locator(login_page.success_message)).to_be_visible()
    print("Test PASS: Login successful")

def test_failed_login(page: Page):
    # Create the login page object
    login_page = LoginPage(page)
    
    # Use clean, readable actions
    login_page.go_to()
    login_page.login("wronguser", "wrongpassword")
    
    # Verify error
    expect(page.locator(login_page.error_message)).to_be_visible()
    print("Test PASS: Error message shown")