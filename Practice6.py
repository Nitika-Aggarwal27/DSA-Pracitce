# queation on array -1D, 2D, dynamic array

# Ques1: Running Sum of 1d array (leetcode-1480)
# sol:



# Ques2: Concatenation of 1d array (leetcode-1929)
# sol:



# Ques4: Kids with Greatest Candies (leetcode-1431)
# sol:



# Ques5: Smaller Numbers Than Current (leetcode-1365)
# sol:




# Ques6: Subarray Sum Equals K (O(n^2)) (leetcode-560)
# sol:





# 2D array:
# Ques3: Richest Customer Wealth (leetcode-1672)
# sol:




# Ques7: print matrix
# sol:
arr7 = [[1,2,3,4], [3,5,7,8]]
print(arr7)

# or:
for row in arr7:
    for val in row:
        print(val)
    print()


# Ques8: Sum of Elements
# sol:
arr8 = [[1,2,3,4], [3,5,7,8]]
for row in arr8:
    sum = 0
    for val in row:
        sum+=val
    print(sum)


# Ques9: Transpose
# sol:
# arr9 = [[1,2,3,4], [3,5,7,8]]
# for row in arr9:
#     for val in row:
#         print(val,row)


# Ques10: Maximum Element
# sol:
arr10 = [[1,2,3,4], [3,5,7,8]]
for row in arr10:
    max = 0
    for val in row:
        if(max < val):
            max = val
    print(max)


# Ques11: Count Even & Odd
# sol:
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
arr12 =[1,2,3,4]
arr12.append(23)
print(arr12)


# Ques13: pop
# sol: 
arr13 =[1,2,3,4]
arr13.pop()
print(arr13)




