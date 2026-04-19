import re

def check_password_strength(password):
    \"\"\"
    Evaluates the strength of a password based on length and character variety.
    \"\"\"
    strength = 0
    remarks = []
    
    # Length check
    if len(password) >= 8:
        strength += 1
    else:
        remarks.append(\"Password should be at least 8 characters long.\")
        
    # Case check
    if re.search(r\"[a-z]\", password) and re.search(r\"[A-Z]\", password):
        strength += 1
    else:
        remarks.append(\"Password should contain both uppercase and lowercase letters.\")
        
    # Digit check
    if re.search(r\"\\d\", password):
        strength += 1
    else:
        remarks.append(\"Password should contain at least one digit.\")
        
    # Special character check
    if re.search(r\"[ !@#$%^&*(),.?\":{}|<>]\", password):
        strength += 1
    else:
        remarks.append(\"Password should contain at least one special character.\")
        
    # Strength mapping
    strength_levels = {
        0: \"Very Weak\",
        1: \"Weak\",
        2: \"Medium\",
        3: \"Strong\",
        4: \"Very Strong\"
    }
    
    result = strength_levels.get(strength, \"Unknown\")
    feedback = \" \".join(remarks) if remarks else \"Great password!\"
    
    return result, feedback

if __name__ == \"__main__\":
    print(\"--- Password Strength Checker ---\")
    user_password = input(\"Enter a password to evaluate: \")
    rating, feedback = check_password_strength(user_password)
    print(f\"Rating: {rating}\")
    print(f\"Feedback: {feedback}\")
