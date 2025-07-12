#I დავალება:
num_1 = 75
num_2 = 10

sum_of_numbers = num_1 + num_2
difference_of_numbers = num_1 - num_2
product_of_numbers = num_1 * num_2
quotient_of_numbers = num_1 / num_2

print(sum_of_numbers)
print(difference_of_numbers)
print(product_of_numbers)
print(quotient_of_numbers)


#II დავალება:
name = "Luka"
name = "Dato"
name = "Nika"
name = "Toma"
name = "Tiko"
name = "Maria"

print(name)


#III დავალება:
name = "Nick Diaz"
Name = "Dustin Poirier"
NAME = "Charles Oliveira"
NaMe = "George ST Pierre"
nAmE = "Nate Diaz"

print(name)
print(Name)
print(NAME)
print(NaMe)
print(nAmE)


#IV დავალება:
# 2name = "giorgi"
# შეცდომა: ცვლადის სახელი არ შეიძლება დაიწყოს ციფრით.
# გამოსწორება:
name2 = "giorgi"

# user{name = "bubunauri"
# შეცდომა: ცვლადების სახელებში არ შეიძლება "{" და "}".
# გამოსწორება:
user_name = "bubunauri"

# user_name = goga
# შეცდომა: "goga" არ არის ბრჭყალებში.
# გამოსწორება:
user_name = "goga"

# user-surname = axalaia
# შეცდომა: ცვლადში ტირე "-" არ შეიძლება, რადგან Python ამას აღიქვამს როგორც გამოკლებას და ასევე `"axalaia"` ბრჭყალებში უნდა იყოს.
# გამოსწორება:
user_surname = "axalaia"


#V დავალება:
first_name = "ლუკა"
last_name = "ჯობავა"
city_name = "თბილისი"
favorite_TV_show = "Dexter"
hobby_name = "ბერძნულ-რომაული ჭიდაობა"

# ქვემოთ სტრინგების გაერთიანებას ეწოდება "კონკატენაცია" (Concatenation)
full_sentence = first_name + last_name + " ცხოვრობს ქალაქში " + city_name + ", უყვარს სერიალი " + favorite_TV_show + " და ჰობად აქვს " + hobby_name

print(full_sentence)


#VI დავალება:
Name = "Luka"
Number = 10

# სახელის გამრავლება
Multiplication = (Name * Number)

# ტერმინალში გამოტანა
print(Multiplication)


#VII დავალება:
name = "ლუკა"
number = 5

#1)
# name * number  — შეიძლება (სტრინგი გამრავლდეს რიცხვზე)
result = name * number
print(result)
# შედეგი: ლუკალუკალუკალუკალუკა

#2)
# name + number — არ შეიძლება
# კომენტარი: სტრინგსა და რიცხვს ვერ დავუმატებთ ერთმანეთს პირდაპირ, გამოიწვევს შეცდომას (TypeError)
# print(name + number)  # ეს გამოიწვევს შეცდომას:
# TypeError: can only concatenate str (not "int") to str

#3)
# name - number, name / number, name ** number — არ შეიძლება
# კომენტარი: გამოკლება, გაყოფა, ხარისხში აყვანა და სხვა რიცხვითი ოპერაციები სტრინგზე არ მუშაობს.

#მაგ:
# print(name - number)  # შეცდომა
# print(name / number)  # შეცდომა
# print(name ** number) # შეცდომა

# გამოსავალი: თუ მაინც მინდა სტრინგსა და რიცხვს შეაერთო, რიცხვი უნდა გადაიყვანო სტრინგად:
print(name + str(number))  # შედეგი: ლუკა5

#მოკლე შეჯამება:
# მხოლოდ ორი ოპერაციაა დაშვებული სტრინგსა და ინტეჯერზე:
# 1) str * int — სტრინგის გამრავლება (გაიმეორება)
# 2) str + str — სტრინგების გაერთიანება (თუ int გადაიქცევა str-ად)

# შემდეგი ოპერაციები სტრინგზე და ინტეჯერზე არ შეიძლება:
# str + int
# str - int
# str / int
# str ** int
# შედეგი: TypeError