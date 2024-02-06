from lib.contains_todo import *

def test_check_string_contains_todo():
    result = contains_todo('#TODO')
    assert result == True 

def test_if_strings_does_not_contains_todo():
    result = contains_todo('#Todo')
    assert result == False