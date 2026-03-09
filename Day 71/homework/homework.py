#I codewars დავალება: Function 1 - hello world
#Make a simple function called greet that returns the most-famous "hello world!".

#Style Points
#Sure, this is about as easy as it gets. But how clever can you be to create the most creative "hello world" you can think of? What is 
#a "hello world" solution you would want to show your friends?

def greet():
    return "hello world!"

print()
print()


#II codewars დავალება: Grasshopper - Summation
#Write a program that finds the summation of every number from 1 to num (both inclusive). The number will always be a positive integer 
#greater than 0. Your function only needs to return the result, what is shown between parentheses in the example below is how you reach 
#that result and it's not part of it, see the sample tests.

#For example (Input -> Output):
#2 -> 3 (1 + 2)
#8 -> 36 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8)

def summation(num):
    return num * (num + 1) // 2

print()
print()


#III codewars დავალება: Sum Arrays
#Write a function that takes an array of numbers and returns the sum of the numbers. The numbers can be negative. If the array is empty, 
#return 0.

#Examples
#Input: [1, 5.2, 4, 0, -1]
#Output: 9.2

#Input: [-2.398]
#Output: -2.398

#Input: []
#Output: 0

#Assumptions
#You can assume that you are given a (possibly empty) valid array containing only numbers.

def sum_array(a):
    total = 0
    for i in a:
        total += i
    return total

print()
print()


#IV codewars დავალება: Convert number to reversed array of digits
#Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

#Example (Input => Output):
#35231 => [1,3,2,5,3]
#0     => [0]

def digitize(n):
    
    number = []
    
    for i in str(n):
        number.append(int(i))
        
    return number[::-1]

print()
print()


#V codewars დავალება: Are You Playing Banjo?
#Create a function which answers the question "Are you playing banjo?".
#If your name starts with the letter "R" or lower case "r", you are playing banjo!

#The function takes a name as its only argument, and returns one of the following strings:
#name + " plays banjo" 
#name + " does not play banjo"

#Names given are always valid strings.

def are_you_playing_banjo(name):
    if name[0].lower() == "r" or name[0].upper() == "R":
        return name + " plays banjo"
    else:
        return name + " does not play banjo"

print()
print()


#VI codewars დავალება: Abbreviate a Two Word Name
#Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

#The output should be two capital letters with a dot separating them.

#It should look like this:
#Sam Harris => S.H
#patrick feeney => P.F

def abbrev_name(name):
    words = name.split()
    return words[0][0].upper() + "." + words[1][0].upper()

print()
print()


#VII codewars დავალება: Calculate average
#Write a function which calculates the average of the numbers in a given array.

#Note: Empty arrays should return 0.

def find_average(numbers):
    if len(numbers) == 0:
        return 0

    total = 0

    for i in numbers:
        total += i

    return total / len(numbers)

print()
print()


#VIII codewars დავალება: Sentence Smash
#Write a function that takes an array of words and smashes them together into a sentence and returns the sentence. You can ignore any need 
#to sanitize words or add punctuation, but you should add spaces between each word. Be careful, there shouldn't be a space at the beginning 
#or the end of the sentence!

#Example
#['hello', 'world', 'this', 'is', 'great']  =>  'hello world this is great'

#Assumptions
#You can assume that you are only given words.
#You cannot assume the size of the array.
#You can assume that you do get an array.

def smash(words):
    sentence = ""
    
    for i in range(len(words)):
        sentence += words[i]
        
        if i != len(words) - 1:
            sentence += " "
            
    return sentence

print()