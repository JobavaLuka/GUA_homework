#I დავალება: შექმენით რიცხვებით სავსე სია, ამ სიიდან იპოვეთ და დაპრინტეთ მეორე ყველაზე დიდი რიცხვი, გამოიყენეთ for ციკლი.

print()

nums = [34, 98, 12, 23, 65, 60, 43, 76, 54]

biggest = nums[0]
for i in nums:
    if i > biggest:
        biggest = i

second_biggest = nums[0]
for i in nums:
    if i > second_biggest and i != biggest:
        second_biggest = i

print(second_biggest)

print()
print()


#II დავალება: მომხმარებელს შემოატანინეთ წინადადება და დაითვალეთ თუ ამ წინადადებაში რამდენი სიტყვის სიგრძე არის 4-ზე მეტი, დაპრინტეთ ასეთი 
#სიტყვების რაოდენობა, მაგალითად 4. გამოიყენეთ while ციკლი.

random_sentence = input("შეიყვანეთ რაიმე წინადადება: ")

yvela = 0
i = 0
sigrdze = 0

while i < len(random_sentence):
    if random_sentence[i] != " ":
        sigrdze += 1

    else:
        if sigrdze > 4:
            yvela += 1
        sigrdze = 0

    i += 0

if sigrdze > 4:
    yvela += 1

print(yvela)

print()
print()


#III დავალება:  მომხმარებელს შემოატანინეთ სიტყვა და გაიგეთ ეს სიტყვა არის თუ არა პალინდრომი - ანუ ეს სიტყვა წინიდანაც და უკნიდანაც თუ 
#ზუსტად იგივენაირად იკითხება. თუ კი მაშინ დაპრინტეთ True, თუ არა დაპრინტეთ False, გამოიყენეთ for ციკლი, არ გამოიყენოთ slicing - [::-1].

random_sentence = input("შეიყვანეთ რაიმე წინადადება: ")

empty = ""

for i in random_sentence:
    empty = i + empty

print(random_sentence == empty)

print()
print()


#IV დავალება: შექმენით არეული რიცხვებით სავსე გრძელი სია და 2 ცარიელი სია, ერთ სიაში ჩააგდეთ ყველა ის რიცხვი რომელიც არის ლუწი და დგას 
#კენტ ინდექსზე, ხოლო მეორე სიაში ჩააგდეთ ყველა ის რიცხვი რომელიც არის ლუწი და დგას კენტ ინდექსზე, გამოიყენეთ for ციკლი.

nums = [5, 8, 3, 12, 7, 6, 9, 10, 4, 11]
nums1 = []
nums2 = []

for i in range(len(nums)):
    if i % 2 == 1:
        if nums[i] % 2 == 0:
            nums1.append(nums[i])
        else:
            nums2.append(nums[i])

print(nums1)
print(nums2)

print()
print()


#V დავალება: შექმენით ყველანაირი მონაცემთა ტიპების ელემენტებით სავსე სია, ამოშალეთ ყველა დუპლიკატები - ყველაფერი რაც მეორდება 2-ზე მეტჯერ, 
#გამოიყენეთ remove() ფუნქცია და while ციკლი.

everything_list = ["microwave", "microphone", "microwave", "yellow", 1, 2, 1, 1, True, True, False, False, 23.3, 67.7, 420.0, 41.14]

i = 0
while i < len(everything_list):
    if everything_list.count(everything_list[i]) > 1:
        everything_list.remove(everything_list[i])
    else:
        i += 1

print(everything_list)

print()
print()


#VI დავალება: მომხმარებელს შემოატანინეთ წინადადება და დაპრინტეთ ამ წინადადებაში მყოფი ყველაზე გრძელი სიტყვა, გამოიყენეთ while ციკლი, არ 
#გამოიყენოთ max() ფუნქცია.

random_sentence = input("შეიყვანეთ რაიმე წინადადება: ")

words = random_sentence.split(" ")

longest_word = ""
i = 0

while i < len(words):
    if len(words[i]) > len(longest_word):
        longest_word = words [i]
    i += 1

print(longest_word)

print()