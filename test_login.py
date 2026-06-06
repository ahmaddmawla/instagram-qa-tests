# Instagram QA Tests
# Module: Login Feature
# Author: Ahmad

import pytest


def test_login_valid_credentials():
    username = "ahmad_test"
    password = "Test1234!"
    
    
    assert username != ""
    
    
    assert len(password) >= 8
    
    print("Test 1 PASS: Valid credentials accepted")

def test_login_wrong_password():
    username = "ahmad_test"
    password = "abc"
    
    
    assert len(password) >= 8, "Password too short!"
    
    print("Test 2 PASS: Wrong password rejected")
    
def test_empty_username():
    username = ""
    assert username != "", "Username cannot be empty!"

def test_valid_email():
    email = "ahmad@gmail.com"
    assert "@" in email, "Email must contain @"

def test_invalid_email():
    email = "ahmadgmail.com"
    assert "@" in email, "Email must contain @"

@pytest.mark.parametrize("email", [
    "ahmad@gmail.com",
    "test@yahoo.com",
    "user@hotmail.com",
])
def test_multiple_valid_emails(email):
    assert "@" in email, f"Invalid email: {email}"

@pytest.mark.parametrize("password", [
    "short",
    "ab",
    "1234567",
])
def test_multiple_weak_passwords(password):
    assert len(password) >= 8, f"Password too short: {password}"