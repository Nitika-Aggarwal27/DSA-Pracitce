# Day: 4
# Recursion Practice

# Ques 1: Sum of Digits of a Number.
# sol:
def sum(n):
    if(n == 0):
        return 0
    return n%10 +sum(n//10)

print(sum(245))


# Ques 2: Number of Steps to Reduce a Number to Zero.
# sol:
def reduce(num):
    if(num==0):
        return 0
    if num%2==0:
        return 1 + reduce(num//2)
    return 1 + reduce(num - 1)

print(reduce(433))


# Ques 3: Power of Two.
# sol:
def power(num):
    if(num==1):
        return True
    if num<=0 or num % 2 != 0:
        return False

    return power(num//2)

print(power(255))


# Ques 4: Fibonacci Number.
# sol:
def fibbo(n):
    if n <= 1:
        return n
    return fibbo(n -1) + fibbo(n -2)


for i in range(7):
    print(fibbo(i))
 



# Day: 3
# function practice 

# Ques 1: Sum of Digits of a Number.
# sol:
def add(num1):
    sum=0
    while num1 :
        num = num1 % 10
        sum += num
        num1 //=10
    print(sum)


add(122)


# Ques 2: Number of Steps to Reduce a Number to Zero.
# sol:
def zero(n):
    steps = 0
    while n>0:
        if(n % 2 == 0):
            n//=2
        else:
            n-=1
        steps += 1
    return steps

print(zero(24567))
        

# Ques 3: Power of Two.
# sol:
def power(n):
    if(n<=0):
        return False
    while (n % 2 == 0):
        n//=2
    return n==1

print(power(8))


# Ques 4: Fibonacci Number.
# sol:
def fibo(n):
    a, b = 0 , 1   
    print(a)
    print(b)
    for _ in range(n-2):     
        c = a + b
        print(c)
        a = b 
        b = c

fibo(5)
