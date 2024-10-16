import re

def check_password(password):
    criteria = {
        'length': len(password) >= 8,
        'uppercase': re.search(r'[A-Z]', password) is not None,
        'lowercase': re.search(r'[a-z]', password) is not None,
        'digit': re.search(r'\d', password) is not None,
        'special': re.search(r'[@$!%*?&]', password) is not None,
    }

    score = sum(criteria.values())
    feedback = []
    if not criteria['length']:
        feedback.append("Password must be at least 8 characters long.")
    if not criteria['uppercase']:
        feedback.append("Password must contain at least one uppercase letter.")
    if not criteria['lowercase']:
        feedback.append("Password must contain at least one lowercase letter.")
    if not criteria['digit']:
        feedback.append("Password must contain at least one number.")
    if not criteria['special']:
        feedback.append("Password must contain at least one special character (e.g., @, $, !, %, *, ?).")
    if score == 5:
        strength = "Strong"
    elif score == 4:
        strength = "Moderate"
    elif score == 3:
        strength = "Weak"
    else:
        strength = "Very Weak"
    return strength, feedback

password = input("Enter a password to assess: ")
strength, feedback = check_password(password)

print(f"Password Strength: {strength}")
if feedback:
    print("Feedback:")
    for message in feedback:
        print(f"- {message}")
