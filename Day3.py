# Functions and Recursion

# Day: 3
# Functions

# Ques: Add two integers
# sol:
sum = 0
def sum(a,b):
    sum = a+b
    print("Sum:", sum)
sum(45,57)

# by using return
def add(a,b):
    return a + b

print(add(435,57))


# Ques: Subtract Product and Sum of Digits
# sol:

def sub(a):
    s = 0
    p = 1
    while a:
        digit = a % 10
        s += digit
        p *= digit
        a //= 10
    return p - s

print(sub(23))



# Ques: Number of Steps to Reduce Number to Zero
# sol:
def stepsToZero(num):
    steps = 0
    while num:
        if(num%2==0):
            num //=2
        else:
            num-=1
        steps +=1
    return steps

print(stepsToZero(10))


# Day: 4
# Recursion
# Ques: Print Numbers from 1 to N using Recursion
# sol:
def printn(n):
    if(n==0):
        return 
    printn(n-1)
    return print(n)

printn(34)


# Ques: Print Numbers from N to 1 using Recursion
# sol:
def printn(n):
    if(n==0):
        return 
    print(n)
    printn(n-1)


printn(34)


# Ques: Factorial
# sol:
def fact(n):
    if n ==0:
        return 1
    return n * fact(n-1)

print(fact(5))

