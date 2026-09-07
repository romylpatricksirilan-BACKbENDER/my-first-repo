from operator import add

"""
Author: April Lhen Paniza
Section: BSIT 4-A
"""

def greet(name):
    print(f"Hello, {name}!")

greet("World")

print("--------ADD---------")
add_a = int(input("Enter a number: "))
add_b = int(input("Enter another number: "))
addresult_c = add(add_a, add_b) 
print(f"{add_a} + {add_b} = {addresult_c}")

print("------SUBTRACT------")
sub_a = int(input("Enter a number: "))
sub_b = int(input("Enter another number: "))
def substract(sub_a, sub_b):
    return sub_a - sub_b
subresult_c = substract(sub_a, sub_b)

print(f"{sub_a} - {sub_b} = {subresult_c}")