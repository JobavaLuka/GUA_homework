#I დავალება: შექმენით სია სადაც შეინახავთ სხვადასხვა ქალაქების სახელებს.  
#for loop ით დაბეჭდეთ მხოლოდ ის ქალაქები, რომელთა სახელის სიგრძე მეტია 6-ზე.

print()

cities = ["Tbilisi", "Batumi", "Kutaisi", "Rustavi", "Telavi", "Mtskheta", "Zugdidi"]

for i in range(len(cities)):
    if len(cities[i]) > 6:
        print(cities[i])

print()
print()


#II დავალება: შექმენით სია სხვადასხვა სიტყვებით.  
#-> for loop-ით დაბეჭდეთ მხოლოდ ის სიტყვები, რომელთა სიგრძე ზუსტად იყოფა 15-ზე.

words = ["schizophrenia", "accommodatingly", "zamindaris", "pseudopseudohypoparathyroidism"]

for i in range(len(words)):
    if len(words[i]) % 15 == 0:
        print(words[i])

print()
print()


#III დავალება: შექმენით სია რიცხვებით.  
#-> გამოიყენეთ for loop რათა დათვალოთ რამდენი რიცხვია სიაში.  
#-> არ გამოიყენოთ len() — დაითვალეთ ხელით.

numbers = [1, 2, 3, 4, 5, 6, 7]
count = 0

for i in range(0, len(numbers)):
    count += 1

print("რიცხვების რაოდენობაა:", count)

print()
print()


#IV დავალება: შექმენით სია სხვადასხვა სიტყვებით.  
#-> for loop-ით დაბეჭდეთ მხოლოდ ის სიტყვები, რომელთა სიგრძე ზუსტად 5 სიმბოლოა.

words = ["carpenter", "guitar", "woods", "food", "pencil", "dispatch"]

for i in range(len(words)):
    if len(words[i]) == 5:
        print(words[i])

print()
print()


#V დავალება: მომხმარებელს შემოატანინე წინადადება.  
#-> გაიგე რამდენი სიმბოლოა წინადადებაში.  
#-> for ციკლით დათვალე რამდენი აso "a" ან "A" არის ტექსტში.

sentence = input("შეიყვანე წინადადება: ")

print("სულ არის", len(sentence), "სიმბოლო")

count = 0
for i in range(len(sentence)):
    if sentence[i] == "a" or sentence[i] == "A":
        count += 1

print("'a' ან 'A' სიმბოლოების რაოდენობაა:", count)

print()
print()


#VI დავალება: <= Boss Level =>
#შექმენით სია სადაც შეინახავთ სხვადასხვა სტრინგებს.
#--> დაპრინტეთ ამ სიიდან ყველაზე გრძელი სტრინგი

strings = ["car", "airplane", "university", "python", "mountain", "sun"]

longest = ""
for i in range(len(strings)):
    if len(strings[i]) > len(longest):
        longest = strings[i]

print("ყველაზე გრძელი სტრინგია:", longest)

print()