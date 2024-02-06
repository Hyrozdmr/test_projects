# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE
def age_verifier(dof):
    #Parameter:
    # date format: User enter date of birth
    # it will be loop condition if user ager over 16 
    #return : string message "Access granted"
    # else "Access denied"
    # telling them their current age and the required age 
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""Given age 16 and over 16 
it will return  access granted
"""
result.age_verifier(16)
result.age_verifield(18)
result.age_verifield(23)
assert result.age_verifier == "Access granted"

"""
Given age under 16 , it will return access denied
"""
result.age_verifier(15)
assert result.age_verifier == "Acces denied, You are 15 , your age should be 16 or more"

"""
if dof in different format
Raise Exception ("birth isn't right type or format")
```


_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE
!
