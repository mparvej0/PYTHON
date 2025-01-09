# Qs1. What will the following code output if the user enters Hello?
user_input = input("Enter something: ")
print(user_input)

# Qs2. How would you convert the user input (which is by default a string) into an integer and then print it? For example, if the user enters 25, you should print 25 as an integer.
num = int(input())
print(num)

# Qs3. Write a Python program that asks the user for their name and age, and then prints a message saying: "Hello [name], you are [age] years old."
name = input("What is your name? ")
age = input("How old are you? ")
print(f"Hello {name}, you are {age} years old.")

# Qs4. How can you take multiple inputs from the user in one line (e.g., "10 20 30") and convert them into a list of integers?
user