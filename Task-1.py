# 1. Ask the user for their information. Ask the user for their information. Ask the user for their information
# 1. Ask the user for their information
# The input() function gets text from the user
user_name = input("Hello! What is your name? ")
user_age_str = input("How old are you? ")
user_hobby = input("What is your favorite hobby? ")

# 2. Display a friendly welcome message using the collected information
print("\n--- Your Introduction ---") # \n creates a new line

# Concatenation and variable insertion (f-strings are a common way to do this)
print(f"Hello, {user_name}! We're thrilled to have you.")
print(f"It's great to hear that you are {user_age_str} years old.")
print(f"We hope you get to enjoy {user_hobby} often!")

print("--------------------------")
print("Keep coding!")
