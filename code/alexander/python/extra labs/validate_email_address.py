import re


# Validate an Email Address
# Write a function `validate_email_address` which returns `True` if the given string is an email address, `False` is it isn't.

def validate_email_address(email):
    ...


def test_validate_email_address():
    assert validate_email_address('test@gmail.com') == True
    assert validate_email_address('abc123@gmail.com') == True
    assert validate_email_address('test') == False
    assert validate_email_address('test@gmail') == False
    assert validate_email_address('test@gmail@com') == False