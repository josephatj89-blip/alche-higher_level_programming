#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

r1 = Rectangle(3, 5)
print(r1)
try:
    print(r1.__width)
except AttributeError as e:
    print("AttributeError:", e)

try:
    r2 = Rectangle(3, -5)
except Exception as e:
    print(type(e).__name__, ":", e)

try:
    r3 = Rectangle("3", 5)
except Exception as e:
    print(type(e).__name__, ":", e)
