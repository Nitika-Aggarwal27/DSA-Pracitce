# ques 1: even or odd - Subtract 2 again and again using for loop.
# sol: 1st approach using modulus
def check(num):
    if num%2==0:
        print(num, "This is a even number.")
    else:
        print(num, "This is a odd number.")

check(253567)

# 2nd approach: using bitwise operator
def checkbit(num):
    if (num & 1) == 0:
        print(num," This is a even number.")
    else:
        print(num, "This is a odd number.")

checkbit(345678)

# 3rd approach: subtract again and again
def checksub(num):
    og_num = num
    while num>=0:
        if(num == 0):
            print(og_num, "This is a even number.")
        if(num == 1):
            print(og_num, "This is a odd number.")
        num = num - 2

checksub(2345)

# 4th approach: divide and multiply until you didn't get 1 or 0 as a output
def checkdiv(num):
    half = num//2
    res = half*2
    if res==num:
        print(num, "This is a even number.")
    else: 
        print(num, "This is a odd number.")

checkdiv(34567)

# 3rd approach one more using for loop

def checkfor(num):
    number = num
    num = abs(num)

    for _ in range(num // 2):
        num -= 2
    if(num == 0):
        print(number, "This is a even number.")
    else:
        print(number, "This is a odd number.")

checkfor(2345566)


# ques 2: vowel or consonant - Check wether a given alphabet is vowel or consonant.
# sol:
def char(a):
    org_char = a
    if(a.lower() in "aeiou"):
        print(org_char, "Yes, this character is a vowel.")
    else:
        print(org_char, "This is consonant.")

char("A")


# ques 3: leap year - Check whether a year is a leap year or not.
# sol:
def year(num):
    if(num % 400 == 0 or (num% 4 == 0 and num %100 != 0)):
        print(num, "This is a leap year.")
    else:
        print(num, "This is not a leap year.")

year(2003)


# ques 4: HCF - Find the Highest Common Factor of two numbers.
# sol:
def hcf(a,b):
    x,y = a,b
    while y !=0:
        x,y = y,x % y
    print("HCF is:", x)

hcf(35,46)


# ques 5: LCM - Find the Least Common Multiple of two numbers.
# sol: Formula = (LCM * HCF = a * b) 
# 1st approach: using Euclidean algorithm (more optimised)
def hcf2(a,b):
    x,y=a,b
    while y != 0:
        x,y= y, x%y
    hcf2 = x
    lcm = (a * b)//hcf2
    print("Hcf is: ", hcf2, "and Lcm is:", lcm)

hcf2(22,20)

# 2nd approach: common factor
def hcf_lcm1(a,b):
    hcf = 1

    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            hcf = i

    lcm = 1
    while lcm % a != 0 or lcm % b != 0:
        lcm += 1

    print("HCF:", hcf, "LCM:", lcm)

hcf_lcm1(22, 20)


# 3rd approach: python built-in functions
import math

def hcf_lcm(a,b):
    hcf = math.gcd(a,b)
    lcm = abs(a*b) // hcf if hcf != 0 else 0
    print("HCF:", hcf, "LCM:", lcm)

hcf_lcm(22,20)