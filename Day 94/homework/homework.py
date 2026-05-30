#I codewars დავალება: Simple remove duplicates
#Remove the duplicates from a list of integers, keeping the last ( rightmost ) 
#occurrence of each element.

#Example:
#For input: [3, 4, 4, 3, 6, 3]

#remove the 3 at index 0
#remove the 4 at index 1
#remove the 3 at index 3
#Expected output: [4, 6, 3]

#More examples can be found in the test cases.

#Good luck!

print()

def solve(arr): 

    elements = []

    for i in reversed(arr):
        if i not in elements:
            elements.append(i)

    return elements[::-1]

print()
print()


#II codewars დავალება: Tail Swap
#You'll be given a list of two strings, and each will contain exactly one colon 
#(":") in the middle (but not at beginning or end). The length of the strings, 
#before and after the colon, are random.

#Your job is to return a list of two strings (in the same order as the original 
#list), but with the characters after each colon swapped.

#Examples
#["abc:123", "cde:456"]  -->  ["abc:456", "cde:123"]
#["a:12345", "777:xyz"]  -->  ["a:xyz", "777:12345"]

#ver gavige

print()
print()


#III codewars დავალება: Detect Pangram
#A pangram is a sentence that contains every single letter of the alphabet at least 
#once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a 
#pangram, because it uses the letters A-Z at least once (case is irrelevant).

#Given a string, detect whether or not it is a pangram. Return True if it is, False 
#if not. Ignore numbers and punctuation.

def is_pangram(st):

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    panagram  = st.lower()

    for i in alphabet:
        if i not in panagram:
            return False

    return True

print()
print()


#IV codewars დავალება: Convert string to camel case
#Complete the method/function so that it converts dash/underscore delimited words into 
#camel casing. The first word within the output should be capitalized only if the original 
#word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). 
#The next words should be always capitalized.

#Examples
#"the-stealth-warrior" gets converted to "theStealthWarrior"

#"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

#"The_Stealth-Warrior" gets converted to "TheStealthWarrior"

def to_camel_case(text):

    result = ""
    capitalize = False

    for i in text:
        if i == "-" or i == "_":
            capitalize = True
        else:
            if capitalize:
                result += i.upper()
                capitalize = False
            else:
                result += i

    return result

print()
print()


#V codewars დავალება: Debug the functions EASY
#Debug the functions
#Should be easy, begin by looking at the code. Debug the code and the functions should work.

#There are three functions: Multiplication (x) Addition (+) and Reverse (!esreveR)

def multi(l_st):

    result = 1

    for i in l_st:
        result = result * i

    return result


def add(l_st):

    result = 0

    for i in l_st:
        result = result + i

    return result


def reverse(text):

    result = ""

    for i in text:
        result = i + result

    return result

print()
print()


#VI codewars დავალება: Factorial
# Your task is to write function factorial.

# https://en.wikipedia.org/wiki/Factorial

def factorial(n):

    result = 1

    for i in range(1, n + 1):
        result = result * i

    return result

print()