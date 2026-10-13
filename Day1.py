# if else and loop questions 


# ques: find even or odd number 

# 1st approach: modulus operator

def check(num):
    if num % 2 == 0:
        print(num, "is even number.")
    else:
        print(num, "is odd number.")

check(4)

# 2nd approach: bitwise operator

def check2(num):
    if(num & 1)==0:
        print(num,"is even")
    else: 
        print(num, "is odd")

check2(1245673)

# 3rd approach: sbtarct by 2 again and again until you did not get the output as 0 or 1 if output is 0 it is even, else its odd.

def subcheck(num):
    while num >= 0:
        if num == 0:
            print(num, "is sure even.")
            break
        if num == 1:
            print(num,"is odd.")
            break
        num = num - 2


subcheck(3457899)

# 4th approach: divide and multiply by 2 and then match the output with the given value.

def check3(num):
    half = num // 2
    ans = half * 2
    if num == ans:
        print(num, "is even")
    else:
        print(num, "is odd")

check3(35679)



# Write a program to check whether a given number is a prime number using the brute force method.

# 1st approach: by brute aproach

n = 21362
is_prime = True
if(n<=1):
    is_prime= False      #num <= 1 are not primes
else: 
    for i in range( 2, n-1):
        if n% i == 0:
            is_prime = False
            break

if(is_prime == True):
    print(n, "is prime")
else: 
    print(n, "is not prime")


# 2nd approach: optimised logic.
import math
n = 21
is_prime = True
if(n<=1):
    is_prime= False      #num <= 1 are not primes
else: 
    for i in range( 2, int(math.sqrt(n))+1):
        if n% i == 0:
            is_prime = False
            break

if(is_prime == True):
    print(n, "is prime")
else: 
    print(n, "is not prime")
