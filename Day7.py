# Strings (Immutable)

# syntax: s ="Nitika"

# string practice: 

# ques1:Valid Anagram (LeetCode 242)
# sol: 1st method
print("Valid Anagram or not:")
str1 = "anagram"
str2= "naagram"

reverse_sorted = "".join(sorted(str1))
reverse_sorted2 = "".join(sorted(str2))


if(reverse_sorted== reverse_sorted2):
    print(True)
else:
    print(False)

# 2nd method
# def ana(s,t):
#     return sorted(s)==sorted(t)



# ques2: Valid Palindrome (LeetCode 125)
# sol: 1st method:
print("Valid Palindrome or not:")
str3 = "mom"
str4 = ""

for i in range(len(str3)-1, -1, -1):
    str4 += (str3[i])
print(str4)

if(str3==str4):
    print(True)
else:
    print(False)

# 2nd method:
# def isPalindrome(s: str) -> bool:
    # cleaned = ""
    # for c in s:
    # if c.isalnum():
    # cleaned += c.lower()
# return cleaned == cleaned[::-1]



# ques3: Length of Last Word (LeetCode 58)
# sol:






# Ques4: Longest Common Prefix(LeetCode 14)
# sol:
