# Qs1. Write a Python program that adds two numbers entered by the user and prints the result.
num1 = int(input("Enter the first number: "))
num2 =  int(input("Enter the second number: "))
add = num1 + num2
print("The sum of the two numbers is:", add)

# Qs2. Write a Python program that calculates the difference between two numbers and prints the result.
x = 7
y = 4
sub = x - y
print("The different of the two numbers is:", sub)

# Qs3. Write a Python program that multiplies two numbers and displays the result.
a = 4
b = 3
mul = a * b
print("The multiple of the two numbers is:", mul)

# Qs4. Write a Python program that divides two numbers and prints the result. Handle division by zero using a try-except block.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
try:
    resul = num1 / num2
    print("The result of the division is:", resul)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# Qs6. Write a Python program that calculates the remainder when dividing two numbers (modulus operation) and prints the result.
