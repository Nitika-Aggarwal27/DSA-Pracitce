# Day: 3
# Recursion Practice

# Ques 1: Sum of Digits of a Number.
# sol:



# Ques 2: Number of Steps to Reduce a Number to Zero.
# sol:



# Ques 3: Power of Two.
# sol:



# Ques 4: Fibonacci Number.
# sol:





# Day: 4
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
