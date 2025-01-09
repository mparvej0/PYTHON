# Qs1. What are the four main data types you have learned so far? Define each one with a simple example.
name = "Mr. Raju"
age = 22
price = 30.29
is_sunny = False
print(name, type(name))
print(age, type(age))
print(price, type(price))
print(is_sunny, type(is_sunny))

""" Qs2. Which data type would you use to store the following values?
a) Your name
b) Your age
c) A temperature reading with decimals
d) A statement that is either true or false"""
my_name = str("Mr. Raju")
my_age = int(22)
temperature = float(17.67)
is_winter = bool(True)
print(my_name, type(my_name))
print(my_age, type(my_age))
print(temperature, type(temperature))
print(is_winter, type(is_winter))

# Qs3. Explain the difference between an int and a float with an example.
a = int(27)
b = float(27.5)
print(a, type(a))
print(b, type(b))

# Qs4. Why is "10" a string while 10 is an integer?
x = str("10")
X = 10
print(x, type(x))
print(X, type(X))

# Qs5. What is the output type when you add an integer to a float?
a = 87
b = 67.77
c = a + b
print(c, type(c))

# Qs6. Which data type would be used to store the result of a comparison like 5 > 3?
num = 5 > 3
print(num, type(num))

# Qs7. What happens when you divide two integers in Python? What type is the result?
n_div = 5
nu_div = 2
num_div = n_div / nu_div
print(num_div)

# Qs8. Predict the output and type of the following:
n = 5 + 2.0
n1 = 5 // 2
n2 = n/ 2
print(n, type(n))
print(n1, type(n1))
print(n2, type(n2))

# Qs9. How do you add an element to a list? Try to append the value 25 to this list: numbers = [10, 20, 30].
num = [10, 20, 30]
num.append(25)
print(num, type(num))

# Qs10. What is the index of the value 25 in the list [10, 20, 25, 30, 40]?
value = [10, 20, 25, 30, 40]
indes_of_25 = value.index(25)
print(indes_of_25, type(value))

# Qs11. How can you access the last element of a tuple? Try it with the tuple my_tuple = (5, 10, 15, 20).
my_tuple = (5, 10, 15, 20)
print(my_tuple, type(my_tuple))

# Qs12. How would you retrieve the value associated with the key "name" from the dictionary person = {"name": "John", "city": "New York"}?
info = {
    "name": "Adiba Maher",
    "ciyt": "Dubai"
}
print(info, type(info))

# Qs13. What is the difference between a list and a set? How does the following code behave?
my_set = {1, 2, 2, 3, 4}
print(my_set, type(my_set))

# Qs14. What is the output of the following code?
my_var = None
print(my_var, type(my_var))

