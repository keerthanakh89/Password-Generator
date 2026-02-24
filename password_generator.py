import random
import string
def generate_password(length):
    if length < 4:
        return "Password length should be at least 4."
    # Character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    # Ensure at least one character from each category
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]
    # Fill remaining length
    all_characters = lower + upper + digits + symbols
    password += random.choices(all_characters, k=length - 4)

    # Shuffle password
    random.shuffle(password)

    return "".join(password)


# Main Program
print("🔐 Welcome to Password Generator 🔐")
length = int(input("Enter password length: "))

result = generate_password(length)
print("Generated Password:", result)
