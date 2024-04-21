def fact(n):
    if n == 0:
        return 1
    else:
        return fact(n-1) * n
n = int(input("Enter a natural number:"))
print ("It's factorial is",fact(n))

