# loops and switch statement questions


# prime number with loop
n = 1344
is_prime= True
if(n<= 1):
    is_prime = False
else:
    for i in range(2, n-1):
       if n % i == 0:
           is_prime = False
           break

if(is_prime == True):
    print(n, "Prime")
else: 
    print(n,"not prime")
       
# switch statement general question for syntax
day = int(input("Enter the Day number:"))
match day:
    case 1:
        print("Monday")
    case 2: 
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6: 
        print("Saturday")
    case 7:
        print("Sunday") 
    case _:
        print("Invalid Day")