import re
import string
from typing import Tuple

def check_password_strength(password: str) -> Tuple[int, str, list]:
    """
    Check password strength and return score, assessment and improvement suggestions
    
    Args:
        password: The password to check
        
    Returns:
        Tuple containing:
        - Score (0-5)
        - Assessment message
        - List of improvement suggestions
    """
    score = 0
    suggestions = []
    
    # Check length
    if len(password) < 8:
        suggestions.append("Make password at least 8 characters long")
    elif len(password) >= 12:
        score += 2
    else:
        score += 1
        
    # Check for different character types
    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Add numbers")
        
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters")
        
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters")
        
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("Add special characters")
    
    # Check for common patterns
    if re.search(r"(.)\1\1", password):  # Repeated characters
        score -= 1
        suggestions.append("Avoid repeated characters")
        
    if re.search(r"(123|abc|qwerty|password)", password.lower()):
        score -= 1
        suggestions.append("Avoid common patterns and words")
    
    # Determine assessment
    if score <= 1:
        assessment = "Very Weak"
    elif score == 2:
        assessment = "Weak"
    elif score == 3:
        assessment = "Moderate"
    elif score == 4:
        assessment = "Strong"
    else:
        assessment = "Very Strong"
        
    return score, assessment, suggestions

def main():
    """Example usage of password strength checker"""
    while True:
        password = input("Enter a password to check (or 'q' to quit): ")
        if password.lower() == 'q':
            break
            
        score, assessment, suggestions = check_password_strength(password)
        print(f"\nPassword Strength: {assessment} (Score: {score}/5)")
        
        if suggestions:
            print("\nSuggestions for improvement:")
            for suggestion in suggestions:
                print(f"- {suggestion}")
        else:
            print("\nGreat password! No improvements needed.")
        print("\n" + "-"*50 + "\n")

if __name__ == "__main__":
    main()
