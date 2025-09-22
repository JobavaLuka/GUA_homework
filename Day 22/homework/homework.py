#I დავალება: კომენტარის სახით ახსენით თუ რა არის index და რაში ვიყენებთ მას.
# პითონში სიის ელემენტებს აქვთ თავიანთი "მისამართი" და ამ მისამართებს ედოებათ "ინდექსი".
# რისთვის ვიყენებთ: რომ მივწვდეთ სიაში რომელიმე კონკრეტულ ელემენტს, ამისათვის ვწერთ იმ სიის სახელს რომელი სიიდანაც მინდა რომ ამოვიღო ელემენტი.


#II დავალება: შექმენით ცვლადი სადაც შეინახავთ ამ სიას [4,6,1,5,9,8,4], თქვენი დავალებაა რომ მიწვდეთ ამ სიაში ელემენტებს ინდექსინგის გამოყენებით,
#შეკრიბეთ ორი რიცხვი რომ მიიღთ შემდეგი რიცხვები --> 10 , 2 , 14 , 20 , 4 , 7 , 27 , გამოიყენეთ მათემატიკური ოპერატოები.
numbers = [4, 6, 1, 5, 9, 8, 4]

result1 = numbers[0] + numbers[1]
result2 = numbers[2] + numbers[2]
result3 = numbers[3] + numbers[4]
result4 = numbers[3] + numbers[1] + numbers[4]
result5 = numbers[3] - numbers[2]
result6 = numbers[1] + numbers[2]
result7 = numbers[4] + numbers[5] + numbers[1] + numbers[0]

print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)
print(result7)


#III დავალება: შექმენით სია სადაც შეიყვანთ ადამიანის სახელებს, უნდა გქონდეთ სულ 10 სახელი, თქვენი დავალებაა რომ გამოიტანოთ, მე-5, მე-9, მე-3, მე-7
#და პირველ ინდექსზე მდგომი ელემენტები ცალ ცალკე, გამოიყენეთ ინდექსინგი.
box = ["luka", "nika", "goga", "gio", "giga", "gegi", "nuca", "lizi", "nikoli", "saba"]

print(box[4])
print(box[8])
print(box[2])
print(box[6])
print(box[0])


#IV დავალება: შექმენით სია სადაც მოათავსებთ სტრინგ ტიპის მონაცემებს, თქვენი დავალებაა რომ for loop და while loop (ორივე)-ს დახმარებით გამოიტანოთ
#თითოეული ელემენტი ცალ ცალკე.
Planguages = ["Python", "CSS", "JavaScript", "HTML", "C#"]

for i in range(0,5):
    print(Planguages[i])

i = 0
while i < 5:
    print(Planguages[i])
    i += 1


#V დავალება: შექმენით სია სადაც შეინახავთ 7 ცალ ელემენტს (მონაცემის ტიპს არ აქვს მნიშვნელობა), თქვენი დავალებაა რომ ამ სიაში შეცვალოთ მე-3 ინდექსზე
#მდგომი ელემენტი და ჩაანაცვლო "vashli"-ით, ასევე შეცვალე მე-6 ინდექსზე მდგომი ელემენტი და ჩაანაცვლე 'msxali'-ით, ასევე შეცვალე მე-4 ინდექსზე
#მდგომი ელემენტი და ჩაანაცვლე ის 'atami"-ით, გამოიტანე საბოლოო სია ტერმინალში, სადაც ეს სალი ელემენტი იქნება განახლებული~
items = [67, "headphones", 41.0, "concert", False, True, "python"]

items[3] = "vashli"
items[6] = "msxali"
items[4] = "atami"

print(items)


#VI დავალება: იპოვეთ საბოლოო პასუხი--> True and False or False and True or false and false or true ---> ...
# ამ მოქმედებაში საერთოდ პირველი სრულდება სულ "and"-ები.
# 1: True and False = False ---> False or False and True or False and False or True
# 2: False and True = False ---> False or False or False and False or True
# 3: False and False = False ---> False or False or False or True
# 4: False or False = False ---> False or False = False ===> False or True = True
True and False or False and True or False and False or True


#VII დავალება: შექმენით სია სადაც მოთავსებული გექნებათ ცხოველების სახელები, თქვენი დავალებაა რომ -->  თუ ამ სიაში მოთავსებული მე-3 ინდექსზე
#მდგომი ელემენტი არის ლომი მაშინ დაპრინტე --> "there is lion on index 3" სხვა შემთხვევაში დაუპრინტე რომ --> "there is no lion on index 3".
animals = ["კურდღელი", "ციყვი", "მელია", "ლომი", "ცხენი"]

if animals[3] == "ლომი":
    print("there is lion on index 3")
else:
    print("there is no lion on index 3")


#VIII დავალება: basket = ["ვაშლი", "ბანანი", "საზამთრო", "ატამი", "ყურძენი"]

#დაბეჭდეთ კალათის პირველი ხილი.

#დაბეჭდეთ კალათის მესამე ხილი.

#შეცვალეთ მეორე ხილი "ბანანი" სხვა ხილით (თქვენი არჩევანით).

#დაბეჭდეთ თავიდან ბოლომდე ყველა ხილი ცალ–ცალკე, ინდექსების გამოყენებით (არა for-ით).

FRUITS = ["ვაშლი", "ბანანი", "საზამთრო", "ატამი", "ყურძენი"]

print(FRUITS[0])

print(FRUITS[2])

FRUITS[1] = "კივი"

print("ყველა ხილი ინდექსებით:")
print(FRUITS[0])
print(FRUITS[1])
print(FRUITS[2])
print(FRUITS[3])
print(FRUITS[4])


#IX დავალება: letters = ["ა", "ბ", "გ", "ო", "ლ", "ა", "მ", "ა", "ტ", "ე"]

#დაბეჭდეთ მესამე ასო.

#დაბეჭდეთ მე–5 და მე–6 ასო.

#დაბეჭდეთ ბოლო ასო.

#ააწყვეთ სიტყვა "მამა" ინდექსებით (ყველა ასო ინდექსით უნდა აიღონ და შეაერთონ).

#ააწყვეთ სიტყვა "გოლა".

#ააწყვეთ სიტყვა "გოგა".

letters = ["ა", "ბ", "გ", "ო", "ლ", "ა", "მ", "ა", "ტ", "ე"]

print(letters[2])

print(letters[4], letters[5])

print(letters[-1])

word1 = letters[6] + letters[0] + letters[6] + letters[5]
print(word1)

word2 = letters[2] + letters[3] + letters[4] + letters[5]
print(word2)

word3 = letters[2] + letters[3] + letters[2] + letters[5]
print(word3)


#X დავალება: letters = ["ა", "ბ", "გ", "ო", "ლ", "ა", "მ", "ა", "ტ", "ე"]

#აიღეთ მე–4 ინდექსზე არსებული ასო და შეინახე ცვლადში

#თუ ეს ასო არის "ლ", დაბეჭდეთ: "სწორია! ასო ლ ა"

#სხვა შემთხვევაში დაბეჭდეთ: "არასწორია, სცადე თავიდან"

#=========================
#აიღეთ ბოლო ასო და შეინახე ცვლადში

#თუ ეს "ე"–ა, დაბეჭდეთ "საიდუმლო სიტყვა იწყება სწორად".

#სხვა შემთხვევაში – "საიდუმლო სიტყვა არასწორია".
#==========================

#ააწყვეთ სიტყვა "გელა" და შეინახე ცვლადში 

#თუ ცვლადში შენახული სიტყვა "გელა"–ს ტოლია, დაბეჭდეთ "გაარტყი სახელი!"

#სხვა შემთხვევაში – "შტერი ხარ!დ".

letters = ["ა", "ბ", "გ", "ო", "ლ", "ა", "მ", "ა", "ტ", "ე"]

if letters[4] == "ლ":
    print("სწორია! ასო ლ ა")
else:
    print("არასწორია, სცადე თავიდან")

if letters[9] == "ე":
    print("საიდუმლო სიტყვა იწყება სწორად")
else:
    print("საიდუმლო სიტყვა არასწორია")

word = letters[2] + letters[9] + letters[4] + letters[5]

if word == "გელა":
    print("გაარტყი სახელი!")
else:
    print("შტერი ხარ!დ")


#XI დავალება: შექმენი სია რომელიც იქნება სტრინგებით სავსე, შენი დავალებაა რომ მომხმარებელს შემოატანინო რაიმე რიცხვი, შენი დავალებაა რომ ამ სიიდან
#გამოიტანო მომხმარებლის მიერ შემოტანილ რიცხვზე (ინდექსზე) მდგომი ელემენტი.
film_roles = ["Director", "Producer", "Executive producer", "Principal cast", "Casting director"]

pick_a_role = int(input("შეიყვანე რიცხვი: "))

if pick_a_role >= 0 and pick_a_role <= 5:
    print(film_roles[pick_a_role])
else:
    print("Chat ძმას ჰგონია რომ ეს რიცხვი არსებობს")