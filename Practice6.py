# queation on array -1D, 2D, dynamic array

# Ques1: Running Sum of 1d array (leetcode-1480)
# Explanation: Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# sol:
print("Running Sum of 1d array:")
arr1 = [1,3,4,5]
sum = 0
for row in arr1:
    sum+=row
    print(sum)

# 2nd method:
array1 = [1,3,4,5]
sum = 0
for row in range(1, len(array1)):
    array1[row] += array1[row-1]

print(array1)


# Ques2: Concatenation of 1d array (leetcode-1929)
# Explanation: Input: nums = [1,2,1]
# Output: [1,2,1,1,2,1]
# sol:
print("Concatenation of 1d array:")
arr2 = [1,3,4,5]
for row in arr2:
    


# 2nd method:
# def getConcatenation(nums):
#     return nums + nums


# Ques4: Kids with Greatest Candies (leetcode-1431)
# Explanation: Input: candies = [2,3,5,1,3], extraCandies = 3
# Output: [true,true,true,false,true] 
# sol:
print("Kids with Greatest Candies:")
arr4 = [1,3,4,5]




# Ques5: Smaller Numbers Than Current (leetcode-1365)
# Explanation: Input: nums = [8,1,2,2,3]
# Output: [4,0,1,1,3]
# sol:
print("Smaller Numbers Than Current:")
arr5 = [1,3,4,5]




# Ques6: Subarray Sum Equals K (O(n^2)) (leetcode-560)
# Explanation: Input: nums = [1,1,1], k = 2
# Output: 2
# sol:
print("Subarray Sum Equals K (O(n^2)):")
arr6 = [1,3,4,5]






# 2D array:
# Ques3: Richest Customer Wealth (leetcode-1672)
# Explanation: Input: accounts = [[1,2,3],[3,2,1]]
# Output: 6
# sol:
print("Richest Customer Wealth:")
arr3 = [[1,2,5],[3,2,1]]
max = 0
for row in arr3:
    sum = 0
    for val in row:
        sum+=val
    if max < sum:
        max = sum
print(max)

# another short method
# def maximumWealth(accounts):
#     return max(map(sum, accounts))



# Ques7: print matrix
# sol:
print("Print Matrix:")
arr7 = [[1,2,3,4], [3,5,7,8]]
print(arr7)

# or:
print("Print Matrix with another method:")
for row in arr7:
    for val in row:
        print(val)
    print()


# Ques8: Sum of Elements
# sol:
print("Sum of Elements:")
arr8 = [[1,2,3,4], [3,5,7,8]]
for row in arr8:
    sum = 0
    for val in row:
        sum+=val
    print(sum)


# Ques9: Transpose
# sol:
print("Transpose:")
arr9 = [[1,2,3,4], [3,5,7,8]]
n = len(arr9)
m = len(arr9[0])
for i in range(m):
    for j in range(n):
        print(arr9[j] [i])


# Ques10: Maximum Element
# sol:
print("Maxium Element:")
arr10 = [[1,2,3,4], [3,5,7,8]]
for row in arr10:
    max = 0
    for val in row:
        if(max < val):
            max = val
    print(max)


# Ques11: Count Even & Odd
# sol:
print("Count even or odd:")
arr11 = [[1,2,3,4], [3,5,7,8]]
even, odd = 0, 0
for row in arr11:
    for val in row:
        if(val % 2 == 0):
            even+=1
        else:
            odd+=1
print("even:",even )
print("odd:",odd )



# Dynamic Array
# Ques12: Append
# sol:
print("Dynamic Array with append method:")
arr12 =[1,2,3,4]
arr12.append(23)
print(arr12)


# Ques13: pop
# sol: 
print("Dynamic Array with pop method:")
arr13 =[1,2,3,4]
arr13.pop()
print(arr13)




