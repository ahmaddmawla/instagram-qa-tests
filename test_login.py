# Instagram QA Tests
# Module: Login Feature
# Author: Ahmad

# Test Case TC_001 - Login with valid credentials
def test_login_valid_credentials():
    # Precondition: User has a registered account
    username = "ahmad_test"
    password = "Test1234!"
    
    # Expected: Login successful
    print(f"Testing login with username: {username}")
    print("Expected Result: User redirected to home feed")

# Test Case TC_002 - Login with wrong password
def test_login_wrong_password():
    # Precondition: User has a registered account
    username = "ahmad_test"
    password = "WrongPass!"
    
    # Expected: Error message displayed
    print(f"Testing login with wrong password: {password}")
    print("Expected Result: Error message displayed")