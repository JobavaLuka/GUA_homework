#I codewars დავალება: Binary Addition
#Implement a function that adds two numbers together and returns their sum in binary. 
#The conversion can be done before, or after the addition.

#The binary number returned should be a string.

#Examples:(Input1, Input2 --> Output (explanation)))

#1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
#5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary)

print()

def add_binary(a,b):

    total = a + b

    if total == 0:
        return "0"
    
    binary = ""
    
    while total > 0:
        binary = str(total % 2) + binary
        total = total // 2

    return binary

print()
print()


#II codewars დავალება: Interlocking Binary Pairs
#Task
#Write a function that checks if two non-negative integers make an "interlocking binary pair".

#Interlock ?
#numbers can be interlocked if their binary representations have no 1's in the same place
#comparisons are made by bit position, starting from right to left (see the examples below)
#when representations are of different lengths, the unmatched left-most bits are ignored

#Examples
#1. a = 9, b = 4
#Stacking representations shows how they can interlock.
# 9    1001
# 4     100
#Here, no 1's share any position, so the function returns true.


#2. a = 3, b = 6
#These representations do not interlock.
# 3      11
# 6     110
#Finding they both have a 1 in the same position, the function returns false.

#Input
#Two non-negative integers.

#Output
#Boolean true or false whether or not these integers are interlockable.

def interlockable(a, b):

    while a > 0 and b > 0:
        if a % 2 == 1 and b % 2 == 1:
            return False

        a = a // 2
        b = b // 2

    return True

print()
print()


#III codewars დავალება: Word to binary
#Write a function that takes a string and returns an array containing binary numbers equivalent 
#to the ASCII codes of the characters of the string. The binary strings should be eight digits long.

#Example: 'man' should return [ '01101101', '01100001', '01101110' ]



print()
print()


#IV codewars დავალება: Binary Pyramid 101
#Given two numbers m and n, such that 0 ≤ m ≤ n :

#convert all numbers from m to n (inclusive) to binary
#sum them as if they were in base 10
#convert the result to binary
#return as a string

#Example
#1, 4  -->  1111010

#because:
#    1  // 1 in binary is 1
#+  10  // 2 in binary is 10
#+  11  // 3 in binary is 11
#+ 100  // 4 in binary is 100
#-----
#  122  // 122 in binary is 1111010

def binary_pyramid(m,n):

    total = 0

    for i in range(m, n + 1):
        num = i
        binary = ""

        if num == 0:
            binary = "0"
        else:
            while num > 0:
                binary = str(num % 2) + binary
                num = num // 2

        total += int(binary)

    result = ""

    if total == 0:
        return "0"

    while total > 0:
        result = str(total % 2) + result
        total = total // 2

    return result

print()
print()


#V codewars დავალება: Sum of odd numbers
#Given the triangle of consecutive odd numbers:

#             1
#          3     5
#       7     9    11
#   13    15    17    19
#21    23    25    27    29
#...

#Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) 
#e.g.: (Input --> Output)

#1 -->  1
#2 --> 3 + 5 = 8

def row_sum_odd_numbers(n):
    return n ** 3

print()