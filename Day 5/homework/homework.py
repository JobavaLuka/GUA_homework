#I დავალება: კომენტარის სახით ახსენი თუ რომელი ოპერატორები ვისწავლეთ და რა დანიშნულება აქვთ მათ.
# ჩვენ ვისწავლეთ შედარების, "and" და "or" ოპერაციები.

# შედარების ოპერაციები (ოპერატორები)
# შედარების ოპერატორებია: >, < (მეტია ან ნაკლებია) და == (ტოლია თუ არა). მაგ:
print(68>67) # true, იმიტომ რომ 68 მეტია 67-ზე.
print(420<333) # false, იმიტომ რომ 333 ნაკლებია 420-ზე.
print(23==23) # true, იმიტომ რომ 23 უდრის 23-ს.
print(45==55) # false, იმიტომ რომ 45 არ უდრის 55-ს.

# "and" და "or" ოპერაციები
# "and" ოპერატორის გამოყენების დროს, თუ ერთი პირობა მაინც არის მცდარი (ანუ False), ყველა პირობა იქნება მცდარი. ესენია:
# True and False, False and True და False and False. მაგ:
print(True and False)
print(False and True)
print(False and False)
# "or" ოპერატორის გამოყენების დროს, თუ ერთი პირობა მაინც არის ჭეშმარიტი (ანუ True), ყველა პირობა იქნება ჭეშმარიტი. ესენია:
# True or False, False or True და True and True. მაგ:
print(True or False)
print(False or True)
print(True or True)


#II დავალება: მომხმარებელს შემოაყვანინეთ ორი რიცხვი, შეადარეთ თუ პირველი რიცხვი მეტია მეორეზე, ასევე შეადარე თუ პირველი რიცხვი ნაკლებია მეორე რიცხვზე, და ასევე შეადარე თუ პირველი რიცხვი უდრის მეორე რიცხვს.
# ორი რიცხვის შეყვანა:
num1 = int(input("Put in first number: "))
num2 = float(input("Put in second number: "))

# შედარებები:
print(num1 > num2)
print(num1 < num2)


#III დავალება: მომხმარებელს შემოატანინეთ 5 სტრინგ ტიპის მნიშვნელობა, შენი დავალებაა მოახდინო მათი კონკატინაცია.
# 5 სტრინგის შეყვანა:
string1 = input("Put in first number: ")
string2 = input("Put in first second: ")
string3 = input("Put in first third: ")
string4 = input("Put in first fourth: ")
string5 = input("Put in first fifth: ")

# სტრინგების კონკატინაცია:
concatination = string1 + string2 + string3 + string4 + string5

# შედეგი:
print(concatination)


#IV დავალება: 
# 4 რიცხვის შეყვანა: მომხმარებელს შემოატანინე 4 რიცხვი, შენი დავალებაა გაიგო ამ რიცხვების საშუალო არითმეტიკული.
num1 = float(input("Put in first number "))
num2 = float(input("Put in seconnd number "))
num3 = float(input("Put in third number "))
num4 = float(input("Put in fourth number: "))

# საშუალო არითმეტიკულის გამოთვლა:
average = (num1 + num2 + num3 + num4) / 4

# შედეგი:
print(average)


#V დავალება: შექმენი 4 ცვლადი, ამ ცვლადებში შეინახე 4 განსხვავებული მონაცემთა ტიპის ელემენტები და დაპრინტე მათ ტიპი (გამოიყენეთ შესაბამისი ფუნქცია).
# 4 განსხვავებული მონაცემის ტიპის ცვლადი: 
number = 67                  # მთელი რიცხვი (int)
flo_number = 93.1            # წილადი რიცხვი (float)
name = "ლუკა"               # სტრინგი (str)
status = True                # მნიშვნელობა (bool)

# თითოეული ცვლადის ტიპის დაბეჭდვა:
print(type(number))
print(type(flo_number))
print(type(name))
print(type(status))


#VI დავალება: შექმენი 2 ცვლადი, შეინახე ორივე ცვლადში სტრინგ ტიპის მნიშვნელობები და შეადარე ისინი არიან თუ არა ერთნაირები (უდრის თუ არა ერთმანეთს).
# 2 სტრინგ ტიპის ცვლადი:
str1 = "Chino Moreno"
str2 = "Chi Cheng"

# შედარება:
print(str1 == str2)


#VII დავალება: შექმენი 4 ცვლადი, სადაც გექნება მოთავსებული რიცხვები ოღონდ სტრინგის სახით მაგ: "40", გადაიყვანე ეს სტრინგი რიცხვები ინტეჯერში (გამოიყენე შესაბამისი ფუნქცია) და გაიგე ამ ოთხი რიცხვის ჯამი.
# 4 რიცხვი სტრინგის სახით:
string_num1 = "75"
string_num2 = "32"
string_num3 = "11"
string_num4 = "96"

# სტრინგების გადაყვანა მთელი რიცხვების ტიპში:
num1 = int(string_num1)
num2 = int(string_num2)
num3 = int(string_num3)
num4 = int(string_num4)

# ჯამის გამოთვლა:
total = num1 + num2 + num3 + num4

# შედეგი:
print(total)


#VIII დავალება: შექმენი 3 ცვლადი, ამ ცვლადებში შეინახეთ ინტეჯერ ტიპის მონაცემები, შენი დავალებაა ეს რიცხვები გაასტრინგო (გამოიყენე შესაბამისი ფუნქცია) და გამოიტანო ეს რიცხვები ერთ წინადადებაში. მაგ: 304050.
# 3 მთელი რიცხვის ცვლადი:
num1 = 30
num2 = 40
num3 = 50

# რიცხვების გასტრინგება და ერთმანეთზე დაკავშირება:
result = str(num1) + str(num2) + str(num3)

# შედეგის დაბეჭდვა:
print(result)