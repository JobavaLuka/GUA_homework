#I codewars დავალება: Stop gninnipS My sdroW!
#Write a function that takes in a string of one or more words, and returns the same string, but with all words 
#that have five or more letters reversed (just like the name of this kata). Strings passed in will consist of 
#only letters and spaces. Spaces will be included only when more than one word is present.

#Examples:
#"Hey fellow warriors"  --> "Hey wollef sroirraw" 
#"This is a test        --> "This is a test" 
#"This is another test" --> "This is rehtona test"

print()

def spin_words(sentence):
    words = sentence.split()
    result = ""

    for i in range(len(words)):
        word = words[i]

        if len(word) >= 5:
            word = word[::-1]

        result += word

        if i != len(words) - 1:
            result += " "

    return result

print()
print()


#II codewars დავალება: Alternate capitalization
#Given a string, capitalize the letters that occupy even indexes and odd indexes separately, and return as shown 
#below. Index 0 will be considered even.

#For example, capitalize("abcdef") = ['AbCdEf', 'aBcDeF']. See test cases for more examples.

#The input will be a lowercase string with no spaces.

def capitalize(s):
    even = ""
    odd = ""

    for i in range(len(s)):
        if i % 2 == 0:
            even += s[i].upper()
            odd += s[i]
        else:
            even += s[i]
            odd += s[i].upper()

    return [even, odd]

print()
print()


#III codewars დავალება: Reverse words
#Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the 
#string should be retained.

#Examples
#"This is an example!" ==> "sihT si na !elpmaxe"
#"double  spaces"      ==> "elbuod  secaps"

def reverse_words(text):
    words = text.split(" ")
    result = ""

    for i in range(len(words)):
        result += words[i][::-1]
        if i != len(words) - 1:
            result += " "

    return result

print()
print()


#IV codewars დავალება: Find the vowels
#We want to know the index of the vowels in a given word, for example, there are two vowels in the word super 
#(the second and fourth letters).

#So given a string "super", we should return a list of [2, 4].

#Some examples:
#Mmmm  => []
#Super => [2,4]
#Apple => [1,5]
#YoMama -> [1,2,4,6]

#NOTES
#Vowels in this context refers to: a e i o u y (including upper case)
#This is indexed from [1..n] (not zero indexed!)

def vowel_indices(word):
    result = []

    for i in range(len(word)):
        if word[i] in "aeiouyAEIOUY":
            result.append(i + 1)

    return result

print()
print()


#V codewars დავალება: Nikoloz Tsereteli

#Sainteresoa mas.. Tqven rato xart davaleba?

print()
print()


#VI codewars დავალება: Sum of numbers from 0 to N
#Description:
#We want to generate a function that computes the series starting from 0 and ending until the given number.

#Example:
#Input:
#> 6

#Output:
#"0+1+2+3+4+5+6 = 21"

#Input:
#> -15

#Output:
#"-15<0"

#Input:
#> 0

#Output:
#"0=0"



print()
print()


#VII codewars დავალება: Largest 5 digit number in a series
#In the following 6 digit number:
#283910
#91 is the greatest sequence of 2 consecutive digits.

#In the following 10 digit number:
#1234567890
#67890 is the greatest sequence of 5 consecutive digits.

#Complete the solution so that it returns the greatest sequence of five consecutive digits found within the 
#number given. The number will be passed in as a string of only digits. It should return a five digit integer. 
#The number passed may be as large as 1000 digits.



print()