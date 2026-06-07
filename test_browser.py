import pytest
from playwright.sync_api import Page, expect

def test_successful_login(page: Page):
    
    page.goto("https://the-internet.herokuapp.com/login")
    
    
    page.fill("#username", "tomsmith")
    
    page.fill("#password", "SuperSecretPassword!")
    
    
    page.click("button[type='submit']")
    
    
    expect(page.locator(".flash.success")).to_be_visible()
    
    print("Test PASS: Login successful")
    
def test_failed_login(page: Page):
    # Step 1 - Go to the login page
    page.goto("https://the-internet.herokuapp.com/login")
    
    # Step 2 - Fill in wrong username
    page.fill("#username", "wronguser")
    
    # Step 3 - Fill in wrong password
    page.fill("#password", "wrongpassword")
    
    # Step 4 - Click login
    page.click("button[type='submit']")
    
    # Step 5 - Verify error message appears
    expect(page.locator(".flash.error")).to_be_visible()
    
    print("Test PASS: Error message shown for invalid login")