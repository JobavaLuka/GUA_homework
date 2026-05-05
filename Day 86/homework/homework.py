#I codewars დავალება: Who likes it?
#You probably know the "like" system from Facebook and other pages. People can "like" blog posts, 
#pictures or other items. We want to create the text that should be displayed next to such an item.

#Implement the function which takes an array containing the names of people that like an item. It 
#must return the display text as shown in the examples:

#[]                                -->  "no one likes this"
#["Peter"]                         -->  "Peter likes this"
#["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
#["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
#["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

#Note: For 4 or more names, the number in "and 2 others" simply increases.

print()

def likes(names):
    if len(names) == 0:
        return "no one likes this"
    
    if len(names) == 1:
        return names[0] + " likes this"
    
    if len(names) == 2:
        return names[0] + " and " + names[1] + " like this"
    
    if len(names) == 3:
        return names[0] + ", " + names[1] + " and " + names[2] + " like this"
    
    return names[0] + ", " + names[1] + " and " + str(len(names) - 2) + " others like this"

print()
print()


#II codewars დავალება: Convert an array of strings to array of numbers
#Oh no!
#Some really funny web dev gave you a sequence of numbers from his API response as an sequence of 
#strings!

#You need to cast the whole array to the correct type.

#Create the function that takes as a parameter a sequence of numbers represented as strings and 
#outputs a sequence of numbers.

#ie:["1", "2", "3"] to [1, 2, 3]

#Note that you can receive floats as well.

def to_float_array(arr):

    result = []
    
    for i in arr:
        result.append(float(i))
    
    return result

print()
print()


#III codewars დავალება: Most digits
#Find the number with the most digits.

#If two numbers in the argument array have the same number of digits, return the first one in the 
#array.

def find_longest(arr):

    longest = arr[0]
    
    for i in arr:
        if len(str(i)) > len(str(longest)):
            longest = i
    
    return longest

print()