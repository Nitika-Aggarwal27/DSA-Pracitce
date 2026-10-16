# Time complexity and Space complexity

    # Time Complexity: Time complexity tells us how the time taken by a program increases when the input size increases.

        # Common Time complexities:

            # description:          | Time c.:   | Ex:                               | N value:
            # 1. Constant Time:     | O(1)       | [Accessing an array element]      |
            # 2. Logarithimic Time: | O(log n)   | [Binary Search]                   | (n > 10^8)
            # 3. Linear Time:       | O(n)       | [1D Array loop]                   | (n <= 10^8)
            # 4. Log-linear Time:   | O(n log n) | [Merge Sort, Quick Sort(average)] | (n <= 10^6)
            # 5. Quadratic Time:    | O(n^2)     | [Nested Loop (2 for loop)]        | (n <= 10^4)
            # 6. Cubic Time:        | O(n^3)     | [3 for loop]                      | (n <= 500)
            # 7.Exponential Time:   | O(2^n)     | [Recursive Fibonacci]             | (n <= 25)
            # 8. Factorial Time:    | O(n!)      | [N-Queens (brute force)]          | (n <= 12)


        # Comparision between Time complexities
            # 1. when we go from bottom to top then the value of worst case will be decreasing.
            # 2. when we go from bottom to top then the value and range of n will be increasing.

        # we always check the Big O which is worst case.

# ------------------------------------------------------------------------------------------------------------------------------------->

    # Space Complexity: Space complexity tells us how much extra memory a program needs when the input size increases.
        # It includes:
            # -> Function call stack
            # -> Auxiliary arrays or data structures
            # -> Variables used in computation
        # (Input storage is usually not couted.)

        # Common space compleities:

            # Space C.:     |  Description:         | ex:
            # 1. O(1)       |  Constant space       | Few Variables only
            # 2. O(n)       |  Linear space         | Extra Array
            # 3. O(log n)   |  Logarithmic space    | Binary Search Recursion
            # 4. O(n^2)     |  Quadratic space      | Matrix / 2D array problems

# --------------------------------------------------------------------------------------------------------->

# How to Caluculate Time Complexity?
    # 1. Count loops and recursive calls.
    # 2. Focus on the dominant term.
    # 3. Ignore constants.
        #  Example: O(2n) -> O(n)

# --------------------------------------------------------------------------------------------------------->

# How to Calculate Space Complexity?
    # 1. Count extra memory used.
    # 2. Include arrays, recursion stack, hash maps etc.
    # 3. Ignore input storage.

# --------------------------------------------------------------------------------------------------------->

# Beginner Tips:
    # 1. Single loop: -> O(n)
    # 2. Nested loops: -> O(n^2)
    # 3. Recursion: -> consider call stack size
    # 4. Efficient sorting: -> O(n log n)
    # 5. Hashing access: -> usually O(1)