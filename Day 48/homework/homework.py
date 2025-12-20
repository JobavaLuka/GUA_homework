#I დავალება: შექმენით სახელებით სავსე სია და ასევე ცარიელი სია: Upper_name = [].  სახელების სიიდან ცარიელ სიაში ჩაამატეთ ყველა ის სახელი რომელიც 
#იწყება დიდი ასოთი, გამოიყენეთ for ციკლი და შესაფერისი სიის და სტრინგის ფუნქციები.

print()

names1 = ["goga", "luka", "mate"]

names2 = []

for name in names1:
    if name[0].upper():
        names2.append(name)

print(names2)

print()
print()


#II დავალება: შექმენით 2 სია - სახელების და გვარების. for ციკლის და ფუნქციების გამოყენებით სახელების სიაში ყველა სახელის ყველა ასო გახადეთ დიდი, 
#ხოლო გვარების სიაში ყველა გვარის თითოეული ასო გახადეთ პატარა, სულ ბოლოს კი გააერთიანეთ სახელების სია გვარის სიასთან და დაპრინტეთ მიღებული 
#შედეგი.

names = ["rezi", "goga", "nika"]
surnames = ["rezesidze", "chalauri", "talaxadze"]

for i in range(len(names)):
    names[i] = names[i].upper()

for i in range(len(surnames)):
    surnames[i] = surnames[i].lower()

names.extend(surnames)

print(names)

print()
print()


#III დავალება: შექმენით სტრინგებით სავსე სია და ამ სიიდან ამოშალეთ ყველა ის სიტყვა რომელიც არის ან 6-ზე ნაკლები სიგრძეში, ან რომელიც მთავრდება 
#დიდი ასოთი.

list1 = ["goga", "luka", "saba"]

list2 = []

for i in list1:
    if len(i) < 6 or i[-1].isupper():
        continue
    else:
        list2.append(i)

print(list2)

print()
print()


#IV დავალება: შექმენით float მონაცემთა ტიპის ელემენტებით სავსე სია რომელშიც იქნება 10 float ელემენტი და ამ სიიდან ახალ ცარიელ სიაში ჩაამატეთ ის 
#რიცხვები რომლებიც არიან 10-ზე მეტი და 100-ზე ნაკლები.

numbers1 = [6.7, 6.1, 2.1, 8.9]

numbers2 = []

for i in numbers1:
    if 10 < i < 100:
        numbers2.append(i)

print(numbers2)

print()
print()


#V დავალება: შექმენით 2 სია, პირველი სია იყოს სავსე 5 ცალი ქალაქის სახელებით, და მეორე სიაში მოთავსებული იყოს 10 ქვეყნის სახელი. თქვენი დავალებაა 
#რომ ქვეყნის სახელებში ჩაამატოთ ყველა ქალაქის სახელები ცალ-ცალკე მენულე ინდექსიდან მეოთხე ინდექსის ჩათვლით. გამოიყენეთ for ციკლი და შესაბამისი 
#ფუნქციები.

cities = ["tbilisi", "qutaisi", "zugdidi", "batumi", "ozurgeti"]

countries = ["georgia", "switzerland", "austria", "germany", "netherlands", "belgium", "norway", "finland", "denmark", "sweden"]

for i in range(5):
    countries.insert(i, cities[i])

print(countries)

print()