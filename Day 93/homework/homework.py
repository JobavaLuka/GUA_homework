#I codewars დავალება: 16+18=214
#For this kata you will have to forget how to add two numbers.

#In simple terms, our method does not like the principle of carrying over numbers 
#and just writes down every number it calculates :-)

#You may assume both integers are positive integers.

print()



print()
print()


#II codewars დავალება: Palindrome chain length
#Number is a palindrome if it is equal to the number with digits in reversed order. 
#For example, 5, 44, 171, 4884 are palindromes, and 43, 194, 4773 are not.

#Write a function which takes a positive integer and returns the number of special 
#steps needed to obtain a palindrome. The special step is: "reverse the digits, and 
#add to the original number". If the resulting number is not a palindrome, repeat the 
#procedure with the sum until the resulting number is a palindrome.

#If the input number is already a palindrome, the number of steps is 0.

#All inputs are guaranteed to have a final palindrome smaller than 
#2^63

#Example
#For example, start with 87:

#  87 +   78 =  165     - step 1, not a palindrome
# 165 +  561 =  726     - step 2, not a palindrome
# 726 +  627 = 1353     - step 3, not a palindrome
#1353 + 3531 = 4884     - step 4, palindrome!
#4884 is a palindrome and we needed 4 steps to obtain it, so answer for 87 is 4.

def palindrome_chain_length(n):
    steps = 0

    while str(n) != str(n)[::-1]:
        reversed = int(str(n)[::-1])
        
        n = n + reversed

        steps += 1

    return steps

print()
print()


#III codewars დავალება: Nth Smallest Element (Array Series #4)
#Introduction and warm-up (highly recommended): Playing With Lists/Arrays Series

#Task
#Given an array/list of integers, find the Nth smallest element in the array.

#Notes
#Array/list size is at least 3.
#Array/list's numbers could be a mixture of positives , negatives and zeros.
#Repetition in array/list's numbers could occur, so don't remove duplications.

#Input >> Output Examples
#arr=[3,1,2]            n=2    ==> return 2 
#arr=[15,20,7,10,4,3]   n=3    ==> return 7 
#arr=[2,169,13,-5,0,-1] n=4    ==> return 2 
#arr=[2,1,3,3,1,2],     n=3    ==> return 2 

def nth_smallest(arr, pos):
    arr.sort()

    return arr[pos - 1]

print()
print()


#IV codewars დავალება: Cats and shelves
#Description
#An infinite number of shelves are arranged one above the other in a staggered fashion.
#The cat can jump either one or three shelves at a time: from shelf i to shelf i+1 or 
#i+3 (the cat cannot climb on the shelf directly above its head)

#Input
#Start and finish shelf numbers (always positive integers, finish no smaller than start)

#Task
#Find the minimum number of jumps to go from start to finish

#Example
#Start 1, finish 5, then answer is 2 (1 => 4 => 5 or 1 => 2 => 5)

def solution(start, finish):  
    sashualo = finish - start

    patara = sashualo // 3

    didi = sashualo % 3

    return didi + patara

print()
print()


#V codewars დავალება: Incrementer
#Given an input of an array of digits, return the array with each digit incremented by 
#its position in the array: the first digit will be incremented by 1, the second digit 
#by 2, etc. Make sure to start counting your positions from 1 ( and not 0 ).

#Your result can only contain single digit numbers, so if adding a digit with its position 
#gives you a multiple-digit number, only the last digit of the number should be returned.

#Notes:
#return an empty array if your array is empty
#arrays will only contain numbers so don't worry about checking that

#Examples:
#[1, 2, 3]  -->  [2, 4, 6]   #  [1+1, 2+2, 3+3]

# [4, 6, 9, 1, 3]  -->  [5, 8, 2, 5, 8]  #  [4+1, 6+2, 9+3, 1+4, 3+5]
#                                        #  9+3 = 12  -->  2



print()
print()


#VI codewars დავალება: Basic Sequence Practice
#A sequence or a series, in mathematics, is a string of objects, like numbers, that follow 
#a particular pattern. The individual elements in a sequence are called terms. A simple 
#example is 3, 6, 9, 12, 15, 18, 21, ..., where the pattern is: "add 3 to the previous term".

#In this kata, we will be using a more complicated sequence: 0, 1, 3, 6, 10, 15, 21, 28, ... 
#This sequence is generated with the pattern: "the nth term is the sum of numbers from 0 to 
#n, inclusive".

#[ 0,  1,    3,      6,   ...]
#  0  0+1  0+1+2  0+1+2+3

#Your Task
#Complete the function that takes an integer n and returns a list/array of length abs(n) + 1 
#of the arithmetic series explained above. Whenn < 0 return the sequence with negative terms.

#Examples
# 5  -->  [0,  1,  3,  6,  10,  15]
#-5  -->  [0, -1, -3, -6, -10, -15]
# 7  -->  [0,  1,  3,  6,  10,  15,  21,  28]



print()
print()


#VII codewars დავალება: Largest Elements
# Write a program that outputs the top n elements from a list.

#Example:
#k = 2; list = [7, 6, 5, 4, 3, 2, 1]
#==> [6, 7]

def largest(n, xs):
    xs.sort()

    if n == 0:
        return []

    return xs[-n:]

print()