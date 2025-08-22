#I დავალება: კომენტარების სახით თავიდან ახსენით რა არის conditional statement, რა დანიშუნლება გააჩნიათ და როგორი სახის
#განცხადებები გვაქვს.
# Conditional statement => პირობითი განცხადებები.
# ამოწმებს პირობას (True ან False) და შედეგის მიხედვით წყვეტს, რომელი კოდი შესრულდეს.
# if ოპერატორი გამოიყენება რაიმე კოდის შესასრულებლად, მხოლოდ იმ შემთხვევაში, თუ რაიმე პირობა ჭეშმარიტია.
# Else - ჩვენ შეგვიძლია სხვა რამის გაკეთება. ეს გადაწყვეტილების მიღების ძირითადი ფორმაა.
# if და else-ის მაგალითი:
age = 18

if age >= 18:
    print("You're an adult")
else:
    print("You're not an adult")


#II დავალება: for ციკლის მეშვეობით გამოიტანეთ "hello world" 50-ჯერ.
for i in range(50):
    print("hello world")


#III დავალება: while ციკლის მეშვეობით გამოიტანეთ რიცხვები 3-დან 17-ის ჩათვლით.
i = 3
while i <= 17:
    print(i)
    i = i + 1


#IV დავალება: მომხმარებელს შემოატანინეთ პაროლი, შემდეგ კი შედეგი შეინახეთ ცვლადში. შექმენით პირობა თუ ის უდრის "1234"-ს
#დაბეჭდეთ "Password is correct", სხვა შემთხვევაში დაბეჭდეთ "Password is incorrect".
password = input("Type in a password: ")

if password == "Kronos":
    print("Password is correct")
else:
    print("Password is incorrect")


#V დავალება: შექმენით ცვლადი სადაც შეინახავთ მომხმარებლის მიერ შემოყვანილი ცხოველის სახეობას. თუ სახეობა უდრის "ძაღლი"
#დაბეჭდეთ "woaf! woaf!", სხვა შემთხვევაში "შენ არ გყავს ძაღლი".
animal = input("Type in an animal: ")

if animal == "ძაღლი":
    print("Woaf! Woaf!")
else:
    print("შენ არ გყავს ძაღლი")


#VI დავალება: უყურეთ შემდეგ ვიდეო წყაროსს:

# -- https://youtu.be/FvMPfrgGeKs --

# ვუყურე✅