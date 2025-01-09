user_input = input("Prompt message: ")
print(user_input)

name = input("What is your name: ")
print("Hello", name)

age = int(input("Enter your age: "))
price = float(input("Enter the price: "))
is_member = bool(input("Are you a member (True/False)? "))
print(age)
print(price)
print(is_member)

age = int(input("Enter your age: "))
height = float(input("Enter your height: "))
print("Your age is", age, "and your height is", height)

name = age = input("Enter you name and age: "). split()
print("Name:", name, "Age:", age)