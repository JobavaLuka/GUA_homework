#I codewars დავალება: Convert to Binary
#Task Overview
#Given a non-negative integer b, write a function which returns an integer d such that 
#the binary representation of b is the same as the decimal representation of d.

#Examples:

#n = 1 should return 1
#n = 5 should return 101
#n = 11 should return 1011

print()

def to_binary(n):

    if n == 0:
        return 0

    binary = ""

    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2

    return int(binary)

print()
print()


#II codewars დავალება: Find the number of trailing zeros, in its binary representation , of a number.
#Given a number n, find the number of trailing zeros in its binary representation.

#Examples:
#4  ->  2, because 4 is represented as 100
#5  ->  0, because 5 is represented as 101

#Limits:
#0 < n <= 10^4



print()
print()


#III დავალება: დაწერეთ ფუნქცია, რომელშიც მომხმარებელს შემოატანინებთ ბინარულ - ორობით სტრინგს, 
#და ამ ორობით სტრინგს გადააქცევთ ათობით რიცხვად. მაგალითად: "101" → 5

def binary_to_decimal(n):

    binary_str = input("შეიყვანეთ ორობითი რიცხვი: ")
    result = 0
    new_string = binary_str[::-1]

    for i in range(len(new_string)):
        if new_string[i] == "1":
            result += 2 ** i

    return result

print(binary_to_decimal(100))

# print()
# print()


#IV დავალება: დაწერეთ ფუნქცია, რომელშიც მომხმარებელს შემოატანინებთ დადებით მთელ რიცხვს, 
#და მას გადააქცევთ ორობით რიცხვად. მაგალითად: 5 → "101"

def decimal_to_binary():

    number = int(input("შეიყვანეთ დადებითი რიცხვი: "))
    binary_str = ""

    while number > 0:
        binary_str = str(number % 2) + binary_str
        number = number // 2

    return binary_str

print(decimal_to_binary())

print()