from fractions import Fraction
num1=int(input("Give the first number\n"))
num2=int(input("Give your second number\n"))
av1=(num1+num2)/2
print("First number between ", num2, "and", num1, "is:", Fraction(av1))
av2=(num2+av1)/2
print("--- --- --- --- ")
print("Second number between ", num2, "and", num1, "is:", Fraction(av2))