"""
try:
    x = int(input("Enter a integer: "))
    print(type(x))
except ValueError():
    print("Invalid type entered.")
"""

try:
    x = int(input("Type an integer: "))
    print("Correct type.", type(x))
except ValueError:
    print("Invalid type.\n", "This isn't an integer")
