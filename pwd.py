import random
import string

def generate_password(length):
    return ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))

def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        print("Generated password:", generate_password(length))
    except ValueError:
        print("Please enter a valid integer for the password length.")

if __name__ == "__main__":
    main()
