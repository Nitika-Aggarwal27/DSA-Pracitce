# Print numbers from 1 to 10 using loop.
# sol.
print("From 1 to 10 numbers are:")
for i in range(1, 11):
    print(i)


# Print numbers from 10 to 1 in reverse order.
# sol.
print("From 10 to 1 numbers are:")
for y in range(10, 0, -1):
    print(y)


# Print all even numbers from 1 to 50.
# sol.
print("From 1 to 50 even numbers are:")
for e in range(1,51):
    if(e% 2==0):
        print(e)

# 2nd approach:
print("From 1 to 50 even numbers with 2nd optimised approach are:")
for e2 in range(2,51,2):
    print(e2)

# Print all odd numbers from 1 to 50.
# sol.
print("From 1 to 50 Odd numbers are:")
for o in range(1,51):
    if(o % 2 ==1):
        print(o)

# 2nd approach:
print("From 1 to 50 odd numbers with 2nd optimised approach are:")
for o2 in range(1,51,2):
    print(o2)


# Print the multiplication table of a number entered by the user.
# sol.
n = int(input("Enter a Number:"))
print(f"Multiplication table of {n}")
for table in range(1, 11):
    print(f"{n} * {table} = {n * table} ") 


# Find the sum of first N natural numbers.
# sol.
print("Sum of first N natural numbers:")
num = int(input("Enter a Number:"))
sum = 0
for natural in range(1, num+1):
    sum += natural

print(f"sum of {num} numbers:", sum)


# Find the factorial of a number.
# sol.
print("Factorial of a number:")
number = int(input("Enter a Number:"))
fact = 1
for w in range(1, number+1):
    fact *= w

print(f"factorial of {number}:", fact)


# Count digits in a number.
# sol.
print("Count digits in a number:")
number2 = int(input("Enter a Number:"))
count = 0
og = number2

while(number2>0):
    count += 1
    number2//=10

print(f"Count digits in {og}:", count)

# Reverse a number.
# sol.
print("Reverse a number:")
real_number = int(input("Enter a Number:"))
rev = 0
org = real_number

while(real_number>0):
    rev = rev * 10 + real_number % 10
    real_number//=10

print(f"Reverse Number of {org} is:", rev)
