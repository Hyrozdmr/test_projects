from datetime import datetime

def age_verifier(dob):
    try:
        test = datetime.strptime(dob, "%Y-%m-%d")
    except:
        return "the date of birth isn't right type or format"
    else:
        dob = datetime.strptime(dob, "%Y-%m-%d")
        age = datetime.now().year - dob.year - ((datetime.now().month, datetime.now().day) < (dob.month, dob.day))
        if age >= 16:
            return "Access granted"
        else:
            return f"Access denied: You are {age} years old.Minimum age required 16"
