#I დავალება:
# Input - ფუნქცია, რომელიც საშუალებას გვაძლევს, მომხმარებელს კერძოდ ტერმინალში შემოვატანინოთ რაღაც მნიშვნელობა, მივიღოთ ამ მნიშვნელობაზე წვდომა და დავამუშავოთ იგი.
# Input-ის მაგალითია, როცა პროგრამა გვეკითხება ჩვენს სახელს და ჩვენ ვწერთ მას კლავიატურით.

name = input("Enter your name in: ")  # ეს არის input — ჩვენი შეყვანილი მონაცემი ინახება ცვლადში "name".

# Output - პასუხი, რომელიც გამოგვაქ მომხმარებლისთვის რაღაც მნიშვნელობის სახით.
# Output-ის მაგალითია, როცა პროგრამა გვეუბნება: "თქვენი სახელი არის: ლუკა".

print(name)  # ეს არის output — პროგრამა ბეჭდავს ეკრანზე შედეგს.


#II დავალება:
# მომხმარებლისგან შემოვიღოთ მნიშვნელობა
value = input("შევიყვანოთ ნებისმიერი მნიშვნელობა: ")

# ვბეჭდავთ ამ ცვლადის მონაცემთა ტიპს
print(type(value))


#III დავალება:
# string ტიპის ცვლადები
name = "ლუკა"            # ეს არის string
city = "თბილისი"         # ეს არის string
language = "Python"       # ეს არის string
hobby = "კითხვა"          # ეს არის string
color = "ლურჯი"         # ეს არის string

# integer ტიპის ცვლადები
age = 16                  # ეს არის int
year = 2049               # ეს არის int
days_in_week = 7          # ეს არის int
temperature = 30          # ეს არის int
aura = 100                # ეს არის int

# float ტიპის ცვლადები
height = 1.75             # ეს არის float
price = 9.99              # ეს არის float
weight = 60.4             # ეს არის float
speed = 317.2             # ეს არის float
average = 1.45            # ეს არის float


#IV დავალება:
# 3 ცვლადი სხვადასხვა მონაცემთა ტიპით
name = "ლუკა"       # string ტიპი
age = 16            # integer ტიპი
height = 1.75       # float ტიპი

# ვამოწმებთ თითოეული ცვლადის მონაცემთა ტიპს და ვბეჭდავთ
print(type(name))
print(type(age))
print(type(height))


#V დავალება:
# მომხმარებლისგან ორი სიტყვის მიღება
word1 = input("Put in first word: ")
word2 = input("Put in second word: ")

# სიტყვის კონკატინაცია
result = word1 + " " + word2

# შედეგის დაბეჭდვა
print(result)


#VI დავალება:
# მომხმარებლისგან 5 რიცხვის მიღება
num1 = float(input("Put in first number: "))
num2 = float(input("Put in second number: "))
num3 = float(input("Put in third number: "))
num4 = float(input("Put in fourth number: "))
num5 = float(input("Put in fifth number: "))

# საშუალო არითმეტიკულის გამოთვლა
average = (num1 + num2 + num3 + num4 + num5) / 5

# შედეგის დაბეჭდვა
print(average)


#VII დავალება:
# მონაცემების მიღება მომხმარებლისგან
name = input("Put in your first name: ")
surname = input("Put in your last name: ")
age = input("Put in your age: ")
height = input("Put in your height: ")
weight = input("Put in your weight: ")

# წინადადების დაბეჭდვა
print("მე ვარ", name, surname + ",", "ვარ", age, "წლის,", "სიმაღლე:", height, "სმ,", "წონა:", weight, "კგ.")