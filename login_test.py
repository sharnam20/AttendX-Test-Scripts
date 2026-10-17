
# AttendX Login Test
# Sample test case for a student attendance application

def test_login_with_valid_credentials():
    username = "student01"
    password = "valid_password"

    # Simulate checking the login inputs
    assert username != ""
    assert password != ""

    print("PASS: Username and password are provided")


test_login_with_valid_credentials()
