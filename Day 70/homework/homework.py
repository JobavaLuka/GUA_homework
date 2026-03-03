#I codewars დავალება:
#Complete the solution so that it reverses the string passed into it.

#'world'  =>  'dlrow'
#'word'   =>  'drow'

print()

def solution(string):
    result = ""
    for i in string:
        result = i + result
    return result

print()
print()


#II codewars დავალება:
#You get an array of numbers, return the sum of all of the positives ones.

#Example:
#[1, -4, 7, 12] => 1+7+12=20

#Note
#If there is nothing to sum, the sum is default to 0.

def positive_sum(arr):
    
    total = 0
    
    for i in arr:
        if i > 0:
            total += i
    
    return total

print()
print()


#III codewars დავალება:
#Write a function that accepts a non-negative integer n and a string s as parameters, and returns a string of s repeated exactly n times.

#Examples (input -> output):
#6, "I"     -> "IIIIII"
#5, "Hello" -> "HelloHelloHelloHelloHello"

def repeat_str(n, s):
    return s * n

print()
print()


#IV codewars დავალება:
#Complete the square sum function so that it squares each number passed into it and then sums the results together.
#For example, for [1, 2, 2] it should return 9

def square_sum(numbers):
    total = 0
    for i in numbers:
        total += i ** 2
    return total

print()
print()


#V codewars დავალება:
#We need a function that can transform a string into a number. What ways of achieving this do you know?
#Note: Don't worry, all inputs will be strings, and every string is a perfectly valid representation of an integral number.

def string_to_number(s):
    return int(s)

print()