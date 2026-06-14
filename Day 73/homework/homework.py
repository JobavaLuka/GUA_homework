#I codewars დავალება: Credit Card Mask
#Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still 
#correct. However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.

#Your task is to write a function maskify, which changes all but the last four characters into '#'.

#Examples (input --> output):
#"4556364607935616" --> "############5616"
#     "64607935616" -->      "#######5616"
#               "1" -->                "1"
#                "" -->                 ""

#// "What was the name of your first pet?"
#"Skippy" --> "##ippy"
#"Nananananananananananananananana Batman!" --> "####################################man!"

def maskify(cc):

    masked = ""

    for i in range(len(cc)):
        if i < len(cc) - 4: 
            masked += "#"
        else:            
            masked += cc[i]

    return masked

print()
print()


#II codewars დავალება: Beginner Series #3 Sum of Numbers
#Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. 
#If the two numbers are equal return a or b.

#Note: a and b are not ordered!

#Examples (a, b) --> output (explanation)
#(1, 0) --> 1 (1 + 0 = 1)
#(1, 2) --> 3 (1 + 2 = 3)
#(0, 1) --> 1 (0 + 1 = 1)
#(1, 1) --> 1 (1 since both are same)
#(-1, 0) --> -1 (-1 + 0 = -1)
#(-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)
#Your function should only return a number, not the explanation about how you get that number.

def get_sum(a,b):

    total = 0

    if a < b:
        for i in range(a, b + 1):
            total += i
    else:
        for i in range(b, a + 1):
            total += i

    return total

print()
print()


#III codewars დავალება: Isograms
#An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string 
#that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

#Example: (Input --> Output)

#"Dermatoglyphics" --> true
#"aba" --> false
#"moOse" --> false (ignore letter case)

def is_isogram(string):

    string = string.lower()
    seen = ""

    for i in string:
        if i in seen:
            return False
        seen += i

    return True

print()
print()


#IV codewars დავალება: Well of Ideas - Easy Version
#For every good kata idea there seem to be quite a few bad ones!
#In this kata you need to check the provided array (x) for good ideas 'good' and bad ideas 'bad'. If there are one or two good ideas, 
#return 'Publish!', if there are more than 2 return 'I smell a series!'. If there are no good ideas, as is often the case, return 'Fail!'.

def well(x):

    count = 0

    for i in x:
        if i == "good":
            count += 1

    if count == 0:
        return "Fail!"
    elif count <= 2:
        return "Publish!"
    else:
        return "I smell a series!"

print()
print()


#V codewars დავალება: A wolf in sheep's clothing
#Wolves have been reintroduced to Great Britain. You are a sheep farmer, and are now plagued by wolves which pretend to be sheep. Fortunately, 
#you are good at spotting them.

#Warn the sheep in front of the wolf that it is about to be eaten. Remember that you are standing at the front of the queue which is at the end 
#of the array:
#[sheep, sheep, sheep, sheep, sheep, wolf, sheep, sheep]      (YOU ARE HERE AT THE FRONT OF THE QUEUE)
#   7      6      5      4      3            2      1

#If the wolf is the closest animal to you, return "Pls go away and stop eating my sheep". Otherwise, return "Oi! Sheep number N! You are about 
#to be eaten by a wolf!" where N is the sheep's position in the queue.

#Note: there will always be exactly one wolf in the array.

#Examples
#Input: ["sheep", "sheep", "sheep", "wolf", "sheep"]
#Output: "Oi! Sheep number 1! You are about to be eaten by a wolf!"

#Input: ["sheep", "sheep", "wolf"]
#Output: "Pls go away and stop eating my sheep"



print()
print()


#VI codewars დავალება: Summing a number's digits
#Write a function which takes a number as input and returns the sum of the absolute value of each of the number's decimal digits.

#For example: (Input --> Output)

#10 --> 1
#99 --> 18
#-32 --> 5
#Let's assume that all numbers in the input will be integer values.

def sum_digits(number):
    if number < 0:
        number = -number

    num = str(number)

    total = 0
    for i in num:
        total += int(i)

    return total

print()
print()


#VII codewars დავალება: Testing 1-2-3
#Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

#Write a function which takes a list of strings and returns each line prepended by the correct number.

#The numbering starts at 1. The format is n: string. Notice the colon and space in between.

#Examples: (Input --> Output)

#[] --> []
#["a", "b", "c"] --> ["1: a", "2: b", "3: c"]

def number(lines):

    numbers = []
    li = 1

    for i in lines:
        number = str(li) + ": " + i
        numbers.append(number)
        li += 1

    return numbers

print()
print()


#VIII codewars დავალება: Remove anchor from URL
#Complete the function/method so that it returns the url with anything after the anchor (#) removed.

#Examples
#"www.codewars.com#about" --> "www.codewars.com"
#"www.codewars.com?page=1" -->"www.codewars.com?page=1"

def remove_url_anchor(url):

    if '#' in url:
        index = 0
        for i in range(len(url)):
            if url[i] == '#':
                index = i
                break
        return url[:index]
    else:
        return url

print()
print()


#IX codewars დავალება: 

#ver gavige

print()
print()


#X codewars დავალება: 

#ver gavige

print()