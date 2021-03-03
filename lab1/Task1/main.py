from math import *

try:
    a = float(input())
    b = float(input())
    print("%.2f" % (sin(a + b) * sin(a - b)))
except:
    print("Wrong input")