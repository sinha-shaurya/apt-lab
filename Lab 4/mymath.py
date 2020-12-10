# find sine, square root, log of given number
import math

n = float(input("Enter number: "))
assert (n>0),"Number has to greater than 0 to find logarithm"
print("Sine of n=", math.sin(n), "\nSquare root of n=",
      math.sqrt(n), "\nNatural Log of n=", math.log(n))
