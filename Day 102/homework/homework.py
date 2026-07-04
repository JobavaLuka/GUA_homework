#I codewars დავალება: Largest 5 digit number in a series
#In the following 6 digit number:

#283910
#91 is the greatest sequence of 2 consecutive digits.

#In the following 10 digit number:

#1234567890
#67890 is the greatest sequence of 5 consecutive digits.

#Complete the solution so that it returns the greatest sequence of five consecutive 
#digits found within the number given. The number will be passed in as a string of 
#only digits. It should return a five digit integer. The number passed may be as 
#large as 1000 digits.

print()



print()
print()


#II codewars დავალება: Breaking chocolate problem
#Your task is to split the chocolate bar of given dimension n x m into small squares. 
#Each square is of size 1x1 and unbreakable. Implement a function that will return 
#minimum number of breaks needed.

#For example if you are given a chocolate bar of size 2 x 1 you can split it to single 
#squares in just one break, but for size 3 x 1 you must do two breaks.

#If input data is invalid you should return 0 (as in no breaks are needed if we do not 
#have any chocolate to split). Input will always be a non-negative integer.



print()
print()


#III codewars დავალება: Anagram Detection
#An anagram is the result of rearranging the letters of a word to produce a new word 
#(see wikipedia).

#Note: anagrams are case insensitive

#Complete the function to return true if the two arguments given are anagrams of each 
#other; return false otherwise.

#Examples
#"foefet" is an anagram of "toffee"

#"Buckethead" is an anagram of "DeathCubeK"



print()
print()


#IV codewars დავალება: Over The Road
#Task
#You've just moved into a perfectly straight street with exactly n identical houses on 
#either side of the road. Naturally, you would like to find out the house number of the 
#people on the other side of the street. The street looks something like this:

#Street
#1|   |6
#3|   |4
#5|   |2
#  you
#Evens increase on the right; odds decrease on the left. House numbers start at 1 and 
#increase without gaps. When n = 3, 1 is opposite 6, 3 opposite 4, and 5 opposite 2.

#Example (address, n --> output)
#Given your house number address and length of street n, give the house number on the 
#opposite side of the street.

#1, 3 --> 6
#3, 3 --> 4
#2, 3 --> 5
#3, 5 --> 8
#Note about errors
#If you are timing out, running out of memory, or get any kind of "error", read on. 
#Both n and address could get upto 500 billion with over 200 random tests. If you try 
#to store the addresses of 500 billion houses in a list then you will run out of memory 
#and the tests will crash. This is not a kata problem so please don't post an issue. 
#Similarly if the tests don't complete within 12 seconds then you also fail.

#To solve this, you need to think of a way to do the kata without making massive lists 
#or huge for loops. Read the discourse for some inspiration :)



print()