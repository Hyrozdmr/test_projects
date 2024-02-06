# Text Contains Function Desing Recioe

 ## 1. Describe the problem 

# write the user story here. Add any clarifying notes you might have

> As a user
> so that I can keep track of my tasks
> I want to check if a text includes the string '#TODO'.

## 2. Desing the Function signature

_Include the name of the function, its parameter, return value, and side effects.

'''python
def contains_todo(text):
    # parameters:
    # text: A string representing the text to check the function will return a boolean value.
    # Return:
    # The function will return boolean value.
    'True': If text contains the string '#TODO'.
    "False': If text does not contains the string '#TODO'.
    # There is no side effects.
'''
## 3. Create Examples as tests

_Make a list of examples of What the method will take and return.

'python'
'''
Given a text contains '#TODO'
It will return 'True'
'''
contains_todo('#TODO')
# => True

'''
Given a text does not contains '#TODO'
It will return 'False'
'''

contains_todo('#Todo')
# => False

## 4. Implement the Behaviour

_Ater each test you write, follow the test_drving process of red, green, refactor to implement the behaviour.