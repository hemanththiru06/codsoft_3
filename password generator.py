import string
import random

def generate_password(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
        while True:
            try:
                length = int(input("Enter the desired length of the password: "))
                if length <= 0:
                    print("Please enter a positive integer.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    
   
        password = generate_password(length)
        print("Generated Password:", password)
main()
