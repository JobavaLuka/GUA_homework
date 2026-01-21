#I დავალება: შექმენით სიტყვებით სავსე სია, თუ სიტყვის ყველა ასო არის პატარა, ანუ წერია lowercase-ში, ამ სიტყვის ყველა ასო გახადეთ დიდი.
#თუ სიტყვა შეიცავს თუნდაც ერთ uppercase ასოს, ეს სიტყვა ამოშალეთ სიიდან. ბოლოს დაპრინტეთ მიღებული სია. (არ შექმნათ ახალი სია, იმუშავეთ 
#პირველ სიტყვების სიაში) გამოიყენეთ while ციკლი.

print()

words = ["MicroWave", "microphone", "WiZarD", "MathemaTICS", "vinyl", "radio"]

i = 0
while i < len(words):
    if words[i] == words[i].lower():
        words[i] = words[i].upper()
        i += 1
    else:
        words.pop(i)

print(words)

print()
print()


#II დავალება: შექმენით სტრინგის ცვლადი და ცარიელი სია. სტრინგში მყოფი დიდი ასოები გახადეთ პატარა და ამ სიაში ჩაამატეთ, ხოლო სტრინგში მყოფი 
#პატარა ასოები გახადეთ დიდი და ასევე ჩააგდეთ ამ სიაში. დაპრინტეთ საბოლოო სია, გამოიყენეთ while ციკლი.

random_word = "WazzUp"
new_random_word = []

i = 0
while i < len(random_word):
    if random_word[i] == random_word[i].upper():
        new_random_word.append(random_word[i].lower())
    else:
        new_random_word.append(random_word[i].upper())
    i += 1

print(new_random_word)

print()
print()


#III დავალება: შექმენით სახელებით სავსე სია, ასევე შექმენით ცარიელი სია, თუ სიტყვის ყველა ასო არის პატარა, მაშინ ამ სიტყვის ყველა ასო გახადეთ 
#დიდი და შესაბამისი სიის ფუნქციის გამოყენებით ჩასვით ეს სიტყვა ცარიელი სიის დასაწყისში, ხოლო თუ სიტყვის ყველა ასო არის დიდი, მაშინ ამ 
#სიტყვის ყველა ასო გახადეთ პატარა და შესაბამისი სიის ფუნქციის გამოყენებით ჩასვით ეს სიტყვა ცარიელი სიის ბოლოში. ბოლოს დაპრინტეთ მიღებული სია. 
#გამოიყენეთ for ციკლი.

names = ["LUKA", "nikolozi", "GOGA", "NATALi", "mate", "DAVITI", "nikoli", "giorgi"]
empty_ahh_list = []

for i in names:
    if i == i.lower():
        empty_ahh_list.insert(0 , i.upper())
    elif i == i.upper():
        empty_ahh_list.append(i.lower())

print(empty_ahh_list)

print()
print()


#IV დავალება: შექმენით ქალაქების სია, წაშალეთ pop() ან remove() ფუნქციით ყველა ის სიტყვა რომლის ყველა ასო არის დიდი, ხოლო ყველა სხვა სიტყვას 
#ყველა ასო გაუხადეთ დიდი. დაპრინტეთ საბოლოო შედეგი. გამოიყენეთ while ციკლი.

Georgian_cities = ["tbilisi", "QUTAISI", "batumi", "zugdidi", "GORI", "BAKURIANI", "borjomi"]

i = 0

while i < len(Georgian_cities):
    if Georgian_cities[i] == Georgian_cities[i].upper():
        Georgian_cities.pop(i)
    else:
        Georgian_cities[i] = Georgian_cities[i].upper()
        i += 1

print(Georgian_cities)

print()
print()


#V დავალება: შექმენით გვარებით სავსე სია, თუ სიტყვის ყველა ასო არის პატარა, მაშინ ეს სიტყვა ამოშალეთ ამ სიიდან და თავიდან ჩაამატეთ იგივე სიაში, 
#ოღონდ ერთი ინდექსით მარჯვნივ, და ყველა ასო ჰქონდეს დიდი. ხოლო თუ სიტყვის ყველა ასო არის დიდი, მაშინ ეს სიტყვა ამოშალეთ ამ სიიდან და 
#თავიდან ჩაამატეთ იგივე სიაში, ოღონდ ერთი ინდექსით მარცხნივ, და ყველა ასო ჰქონდეს პატარა. იმუშავეთ ერთ სიაში, გამოიყენეთ while ციკლი.

last_names = ["chalauri", "JOBAVA", "TYEMALADZE", "arabuli", "CHKADUA"]

i = 0
while i < len(last_names):
    word = last_names[i]

    if word == word.lower():
        last_names.pop(i)
        an_index = i + 1

        if an_index > len(last_names):
            last_names.append(word.upper())
        else:
            last_names.insert(an_index , word.upper())
        i += 1
    elif word == word.upper():
        last_names.pop(i)
        new_index = i - 1

        if an_index < 0:
            last_names.insert(0 , word.lower())
        else:
            last_names.insert(an_index , word.lower())
        i += 1
    else:
        i += 1

print(last_names)

print()
print()


#VI დავალება: შექმენით სტრინგის ცვლადი და ცარიელი სია, თუ სტრინგის ასო არის პატარა, მაშინ ცარიელ სიაში ჩაამატეთ "+" ნიშანი, ხოლო თუ 
#სტრინგის ასო არის დიდი, მაშინ ცარიელ სიაში ჩაამატეთ "-" ნიშანი. თუ მინუსების რაოდენობა სიაში არის ლუწი, მაშინ წაშალე ყველა "+" ნიშანი, ხოლო 
#თუ მინუსების რაოდენობა სიაში არის კენტი, წაშალე ყველა "-" ნიშანი. "+" და "-" -ების თავიდან სიაში ჩასაგდებად გამოიყენეთ for ციკლი, ხოლო "+" 
#ან "-" -ების წასაშლელად გამოიყენეთ while ციკლი.

random = "QweRtYuIoPLKjhGFDSaZxCVbNm"
empty_list = []

for i in random:
    if i == i.lower():
        empty_list.append("+")
    else:
        empty_list.append("-")

minus = 0
for i in empty_list:
    if i == "-":
        minus = minus + 1

if minus % 2 == 0:
    while "+" in empty_list:
        empty_list.remove("+")
else:
    while "-" in empty_list:
        empty_list.remove("-")

print(empty_list)

print()
print()


#VII დავალება: შექმენით წინადადების სტრინგის ცვლადი და ცარიელი სია, ცარიელ სიაში ჩაამატეთ სიტყვები ცალ-ცალკე, არა ასოები, არამედ მთლიანი 
#სიტყვები. ამაზე იჭყლიტეთ ტვინი, წარმატებებს გისურვებთ.

random_sentence = "Whats up Goga mas"
empty_list = []

word = ""
for i in random_sentence:
    if i != " ":
        word += i
        print(word)
    elif i == " ":
        empty_list.append(word)
        word = ""
        continue
if word:
    empty_list.append(word)

print(empty_list)

print()
print()


#VIII დავალება: შექმენით სტრინგის ცვლადი და შემოაბრუნეთ ეს სტრინგი. არ გამოიყენოთ slicing. და ყველა ასო გაუხადეთ დიდი. დაპრინტეთ საბოლოო 
#სტრინგი.

string_ahh = "Bazinga"
empty = ""

for i in string_ahh:
    empty = i.upper() + empty

print(empty)

print()