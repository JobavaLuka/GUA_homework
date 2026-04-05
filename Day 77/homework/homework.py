#I codewars დავალება: Don't give me five!
#In this kata you get the start number and the end number of a region and should return the count of all numbers except numbers 
#with a 5 in it. The start and the end number are both inclusive!

#Examples:
#1,9 -> 1,2,3,4,6,7,8,9 -> Result 8
#4,17 -> 4,6,7,8,9,10,11,12,13,14,16,17 -> Result 12

#The result may contain fives. ;-)
#The start number will always be smaller than the end number. Both numbers can be also negative!

print()

def dont_give_me_five(start, end):

    count = 0

    for i in range(start, end + 1):
        if "5" not in str(i):
            count = count + 1

    return count

print()
print()


#II codewars დავალება: String ends with?
#Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

#Examples:

#Inputs: "abc", "bc"
#Output: true

#Inputs: "abc", "d"
#Output: false

def solution(text, ending):
    return text[len(text) - len(ending):] == ending

print()
print()


#III codewars დავალება: Mumbling
#This time no story, no theory. The examples below show you how to write function accum:

#Examples:
#accum("abcd") -> "A-Bb-Ccc-Dddd"
#accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
#accum("cwAt") -> "C-Ww-Aaa-Tttt"

#The parameter of accum is a string which includes only letters from a..z and A..Z.



print()
print()


#IV codewars დავალება: Number of People in the Bus
#There is a bus moving in the city which takes and drops some people at each bus stop.

#You are provided with a list (or array) of integer pairs. Elements of each pair represent the number of people that get on the 
#bus (the first item) and the number of people that get off the bus (the second item) at a bus stop.

#Your task is to return the number of people who are still on the bus after the last bus stop (after the last array). Even though 
#it is the last bus stop, the bus might not be empty and some people might still be inside the bus, they are probably sleeping 
#there :D

#Take a look on the test cases.

#Please keep in mind that the test cases ensure that the number of people in the bus is always >= 0. So the returned integer 
#can't be negative.

#The second value in the first pair in the array is 0, since the bus is empty in the first bus stop.



print()
print()


#V codewars დავალება: Convert string to camel case
#Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output 
#should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). 
#The next words should be always capitalized.

#Examples
#"the-stealth-warrior" gets converted to "theStealthWarrior"
#"The_Stealth_Warrior" gets converted to "TheStealthWarrior"
#"The_Stealth-Warrior" gets converted to "TheStealthWarrior"



print()