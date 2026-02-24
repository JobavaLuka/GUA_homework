#I დავალება: შექმენი ფუნქცია, რომელსაც აქვს ერთი პარამეტრი —name.
#ფუნქციამ უნდა დააბრუნოს ტექსტი:
#გამარჯობა, [სახელი]!
#ფუნქცია გამოიძახე სხვადასხვა არგუმენტით მინიმუმ 3-ჯერ.

print()

def greet(name):
    return "გამარჯობა, " + name + "!"

print(greet("ლუკა"))
print(greet("გოგა"))
print(greet("ნატალი"))

print()
print()


#II დავალება: შექმენი ფუნქცია, რომელსაც აქვს ორი პარამეტრი — num1 და num2.
#ფუნქციამ უნდა დააბრუნოს მათი ჯამი.
#გამოიძახე ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტებით

def numbers(num1, num2):
    return num1 + num2

print(numbers(6, 7))
print(numbers(34, 33))

print()
print()


#III დავალება: შექმენი ფუნქცია ერთი პარამეტრით num.
#ფუნქციამ უნდა დააბრუნოს (return) გადაცემული რიცხვის კვადრატი.
#გამოიძახე ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტებით

def number(num):
    return num ** 2

print(number(6))
print(number(7))

print()
print()


#IV დავალება: შექმენი ფუნქცია ერთი პარამეტრით — age.
#თუ ასაკი არის 18 ან მეტი, დააბრუნოს:
#სრულწლოვანი ხარ
#სხვა შემთხვევაში:
#არ ხარ სრულწლოვანი

def age_check(age):
    if age >= 18:
        return "სრულწლოვანი ხარ"
    else:
        return "არ ხარ სრულწლოვანი"

print(age_check(60))
print(age_check(7))

print()
print()


#V დავალება: შექმენი ფუნქცია ერთი პარამეტრით — (string).
#ფუნქციამ უნდა დაბეჭდოს ტექსტის სიმბოლოების რაოდენობა.
#გამოიძახე ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტებით

def count(string):
    print(len(string))

count("Goga")
count("Maswavlebeli")

print()
print()


#VI დავალება: შექმენი ფუნქცია ორი პარამეტრით num1 და nuk2.
#ფუნქციამ უნდა დააბრუნოს მათი ნამრავლი.
#გამოიძახე ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტებით

def multiply(num1, num2):
    return num1 * num2

print(multiply(6, 7))
print(multiply(60, 70))

print()
print()


#VII დავალება: შექმენი ფუნქცია ერთი პარამეტრით — score.
#თუ ქულა ≥ 90 → დააბრუნოს "შესანიშნავი ქულა"
#თუ ქულა >= 70 და ნაკლებია ან <=89 → დააბრუნოს "კარგი ქულა"
#თუ ქულა >= 50 და <= 69 → დააბრუნოს "დამაკმაყოფილებელი ქულა"
#სხვა შემთხვევაში დააბრუნოს "ჩაჭრილი"
#გამოიძახე ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტებით

def score_check(score):
    if score >= 90:
        return "შესანიშნავი ქულა"
    elif score >= 70 and score <= 89:
        return "კარგი ქულა"
    elif score >= 50 and score <= 69:
        return "დამაკმაყოფილებელი ქულა"
    else:
        return "ჩაჭრილი"

print(score_check(76))
print(score_check(67))

print()
print()


#VIII დავალება: შექმენი ფუნქცია ერთი პარამეტრით — number.
#ფუნქციამ უნდა დააბრუნოს, ლუწია თუ კენტი.
#გამოიძახე ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტებით

def even_or_odd(number):
    if number % 2 == 0:
        return "ლუწია"
    else:
        return "კენტია"

print(even_or_odd(67))
print(even_or_odd(76))

print()
print()


#IX დავალება: შექმენი ფუნქცია ერთი პარამეტრით — name
#ფუნქციამ უნდა დააბრუნოს მხოლოდ პირველი ასო.
#მაგალითად:
#„Giorgi“ → G
#გამოიძახე ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტებით

def first_letter(name):
    return name[0]

print(first_letter("Goga"))
print(first_letter("Luka"))

print()
print()


#X დავალება: შექმენი ფუნქცია სამი num1 num2 num3.
#ფუნქციამ უნდა დააბრუნოს ამ სამი რიცხვის საშუალო არითმეტიკული.
#გამოიძახე ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტებით

def average_arithmetic(num1, num2, num3):
    return (num1 + num2 + num3) / 3

print(average_arithmetic(6, 7, 67))
print(average_arithmetic(600, 700, 67))

print()
print()


#XI დავალება: შექმენი ფუნქცია ერთი პარამეტრით —password.
#თუ პაროლი უდრის "python123" → დააბრუნოს  "წვდომა დაშვებულია"
#სხვა შემთხვევაში → "არასწორი პაროლი"
#გამოიძახე ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტებით

def password_check(password):
    if password == "python123":
        return "წვდომა დაშვებულია"
    else:
        return "არასწორი პაროლი"

print(password_check("python123"))
print(password_check("html123"))

print()
print()


#XII დავალება: შექმენი ფუნქცია ერთი პარამეტრით — text.
#ფუნქციამ უნდა დააბრუნოს ეს ტექსტი მთლიანად დიდი ასოებით.
#გამოიძახე ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტებით

def upper_text(text):
    return text.upper()

print(upper_text("me miyvars goa"))
print(upper_text("hakathon"))

print()