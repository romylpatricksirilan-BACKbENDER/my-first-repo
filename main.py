from operator import add


def greet(name):
    print(f"Hello, {name}!")

greet("World")

print("--------CALCULATOR---------")
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = add(a, b)
print(f"{a} + {b} = {c}")
