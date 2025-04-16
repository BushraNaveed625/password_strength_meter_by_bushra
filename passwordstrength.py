import re
import random
import string

# List of commonly used weak passwords
common_passwords = {"password", "password123", "123456", "12345678", "qwerty", "iloveyou", "admin", "welcome"}

def check_password_strength(password):
    score = 0
    feedback = []

    # 1. Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # 2. Uppercase and Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    # 3. Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    # 4. Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    # 5. Common Password Blacklist
    if password.lower() not in common_passwords:
        score += 1
    else:
        feedback.append("❌ Avoid common or easily guessable passwords like 'password123'.")

    # Strength Output
    print("\n🔐 Password Evaluation:")
    if score == 5:
        print("✅ Strong Password!")
    elif 3 <= score <= 4:
        print("⚠️ Moderate Password - Consider the suggestions below to improve it.")
    else:
        print("❌ Weak Password - Please improve it using the suggestions below.")

    # Show feedback
    for tip in feedback:
        print(tip)

def generate_strong_password(length=12):
    if length < 8:
        length = 8  # Enforce minimum length

    # Ensure password includes all required character types
    characters = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice("!@#$%^&*")
    ]

    # Fill the rest with random choices from all character sets
    all_chars = string.ascii_letters + string.digits + "!@#$%^&*"
    characters += random.choices(all_chars, k=length - 4)

    # Shuffle to prevent predictable patterns
    random.shuffle(characters)
    return ''.join(characters)

# Main menu
def main():
    print("🔐 Password Strength Meter")
    print("1️⃣  Check password")
    print("2️⃣  Generate strong password")

    choice = input("Choose an option (1 or 2): ").strip()

    if choice == "1":
        password = input("Enter your password: ")
        check_password_strength(password)
    elif choice == "2":
        new_password = generate_strong_password()
        print(f"🔑 Suggested Strong Password: {new_password}")
    else:
        print("❌ Invalid option. Please choose 1 or 2.")

# Run the program
if __name__ == "__main__":
    main()
