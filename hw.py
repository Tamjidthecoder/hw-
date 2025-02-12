

import random
import string

def generate_password(length=12):
    # Define the character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    # Combine all character sets
    all_characters = lower + upper + digits + special

    # Ensure the password has at least one character from each set
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]

    # Fill the rest of the password length with random choices from all characters
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password list to ensure randomness
    random.shuffle(password)

    # Convert the list to a string and return
    return ''.join(password)

# Example usage
print(generate_password(12))
print(generate_password(16))
print(generate_password(20))
