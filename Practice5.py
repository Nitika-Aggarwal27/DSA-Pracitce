# Question with find the time and space complexit:

# Ques 1. Linear Search
# sol:
arr=[1,2,3,4,5,6]

def find(arr, x):
    for i in arr:
        if i == x:
            return True
    return False

print(find(5))

    # Time Complexity: O(n)  -> [One loop through array]
    # Space Complexity: O(1)  -> [Only few variables used]


# Ques 2. Recursive Fibonacci
# sol:
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(4))

    # Time Complexity: O(2^n)  -> [Many repeated recursive calls]
    # Space Complexity: O(n)  -> [Recursion call stack depth]