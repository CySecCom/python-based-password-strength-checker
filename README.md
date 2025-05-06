# Password Strength Checker

A simple Python script to check the strength of a password and provide suggestions for improvement.

## Features
- Evaluates password strength based on length, character variety, and common patterns
- Provides a score (0-5) and assessment (Very Weak to Very Strong)
- Offers actionable suggestions to improve password strength

## How It Works
The script checks for:
- Minimum length (8 characters recommended, 12+ is best)
- Use of numbers, uppercase, lowercase, and special characters
- Avoidance of repeated characters and common patterns (e.g., '123', 'password')

## Usage
1. Make sure you have Python 3 installed.
2. Run the script:
   ```bash
   python "Password Strength Checker.py"
   ```
3. Enter a password when prompted. Type `q` to quit.

## Example
```
Enter a password to check (or 'q' to quit): password123

Password Strength: Weak (Score: 2/5)

Suggestions for improvement:
- Add uppercase letters
- Add special characters
- Avoid common patterns and words

--------------------------------------------------
```

## License
This project is licensed under the MIT License. 
