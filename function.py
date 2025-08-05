# . Write calc(a,b,op).


def calc (a,b,op):

    if op == "+":
        return a+b
    elif op == "-":
        return a -b
    elif op == "*":
        return a *b
    elif op == "/":
        return  a / b
    else:
        return "invalid operation"

print (calc(6,5,"/"))


# Write factorial(n) recursive.


def factorial(n):
    if n == 0 or n == 1:  # Base Case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive Call

# Input
num = int(input("Enter your number: "))
print("Factorial =", factorial(num))
