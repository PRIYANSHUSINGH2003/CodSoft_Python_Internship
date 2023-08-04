import random  #import file
import string

def generate_password(length):
    # Define the characters that can be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a password of the specified length by randomly selecting characters from the defined set
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

def main():                                # Thank You for Watching
    try:
        # Prompt the user to specify the desired length of the password
        password_length = int(input("Enter the desired length of the password: "))

        # Generate the password
        password = generate_password(password_length)

        # Display the generated password on the screen
        print("Generated Password:", password)

    except ValueError: #Exception
        print("Please enter a valid integer for the password length.")

if __name__ == "__main__":
    main()
