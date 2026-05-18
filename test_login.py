# Instagram QA Tests
# Module: Login Feature
# Author: Ahmad

def test_login_valid_credentials():
    username = "ahmad_test"
    password = "Test1234!"
    
    # Assert that username is not empty
    assert username != ""
    
    # Assert that password is at least 8 characters
    assert len(password) >= 8
    
    print("Test 1 PASS: Valid credentials accepted")

def test_login_wrong_password():
    username = "ahmad_test"
    password = "abc"
    
    # Assert that short password fails length check
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
