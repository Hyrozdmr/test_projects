from lib.age_verifier import *

"""Given age 16 and over 16 
it will return  access granted
"""
def test_given_age_16_granted():
    result = age_verifier("2007-02-05")
    assert result == "Access granted"

def test_given_age_over_16_granted():
    result=age_verifier("2005-08-17")
    result=age_verifier("2000-08-17")
    assert result == "Access granted"

def test_given_age_under_16_dined():
    result = age_verifier("2008-05-23")
    assert result == "Access denied: You are 15 years old.Minimum age required 16"

def test_if_different_format():
    notvalid = age_verifier(16)
    assert notvalid == "the date of birth isn't right type or format"

# def test_if_different_format():
#     with pytest.raises(Exception) as error:
#         age_verifier(16)
#     notvalid = str(error.valu)
#     assert notvalid == "the date of birth isn't right type or format"