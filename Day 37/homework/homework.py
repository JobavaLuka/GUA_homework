#I დავალება: მომხმარებელს შემოატანინეთ სიტყვა.
#-> იტერაციით გაიარეთ თითო ასო
#-> თუ შეხვდებით ასო 'e'-ს ან 'E'-ს გაჩერდით (break)
#-> დაბეჭდეთ მხოლოდ ის ასოები, რაც მანამდე იყო

print()

random_word = input("Enter a word: ")

for i in random_word:
    if i == 'e' or i == 'E':
        break
    print(i)

print()
print()


#II დავალება: მომხმარებელს შემოატანინეთ წინადადება.
#-> შეამოწმეთ არის თუ არა ტექსტში სიტყვა 'bad'
#-> თუ არის, დაპრინტეთ "აკრძალული სიტყვა!"
#-> თუ არაა, დაპრინტეთ "ყველაფერი რიგზეა"

sentence = input("enter a sentence: ")

if "bad" in sentence:
    print("აკრძალული სიტყვა!")
else:
    print("ყველაფერი რიგზეა")

print()
print()


#III დავალება: მომხმარებელს შემოატანინეთ წინადადება.  
#-> დაუარეთ ტექსტს for ციკლით
#-> გამოტოვეთ ყველა space => ' '
#-> დაბეჭდეთ ყველა დანარჩენი სიმბოლო

sentence = input("Enter a sentence: ")

for i in sentence:
    if i == ' ':
        continue
    print(i)

print()
print()


#IV დავალება: მომხმარებელს შემოატანინეთ წინადადება.
#-> დაუარეთ მას for ლუპით
#-> გამოტოვეთ ხმოვნები (a, e, i, o, u)
#-> დაბეჭდეთ მხოლოდ თანხმოვნები და თავისთავათ ყველა სხვა სიმბოლო

sentence = input("Enter a sentence: ")

for i in sentence:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
        continue
    print(i)

print()
print()


#V დავალება: მომხმარებელს შემოაყვანიეთ ორი რიცხვი
#--> დაუარეთ ყველა რიცვს ამ დიაპაზონში
#--> დაბეჭდეთ მხოლოდ რიგით პირველი რიცხვი ამ შუალედში რომელიც იყოფა 15-ზე (შეწყვიტეთ ციკლი თუ არის ეგეთი)

num1 = int(input("First number: "))
num2 = int(input("Second number: "))

for i in range(num1,num2):
    if i % 15 == 0:
        print(i)
        break

print()
print()


#VI დავალება: შექმენით უსასრულო while loop:
#--> სანამ მომხმარებელი არ შემოიყვანს 'python is best', მანამდე დაპრინტეთ 'you should learn python'

while True:
    text = input("what do you think about python: ")
    if text == "python is best":
        break
    print("you should learn python")

print()
print()


#VII დავალება: \<.BOSS.>/ 
#მომხმარებელს შემოაყვანიეთ ორი რიცხვი
#--> დაუარეთ ყველა რიცვს ამ დიაპაზონში
#--> დაბეჭდეთ მხოლოდ რიგით მესამე რიცხვი ამ შუალედში რომელიც იყოფა 3-ზე(შეწყვიტეთ ციკლი თუ არის ეგეთი)

num1 = int(input("First number: "))
num2 = int(input("Second number: "))

count = 0

for i in range(num1, num2 + 1, 3):
    if i % 3 == 0:
        print(i)
        break

print()