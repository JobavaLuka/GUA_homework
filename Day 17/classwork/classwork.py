num1 = int(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = int(input("შეიყვანეთ მეორე რიცხვი: "))
num3 = int(input("შეიყვანეთ მესამე რიცხვი: "))

if num1 == num2 == num3:
    print("სამივე ტოლია")
elif num1 == num2:
    print("1 და 2 ტოლია")
elif num1 == num3:
    print("1 და 3 ტოლია")
elif num2 == num3:
    print("2 და 3 ტოლია")
else:
    print("არცერთი არ არის ტოლი")


month = int(input("შეიყვანეთ რიცხვი 1-დან 12-მდე: "))

if month < 1:
    print("არასწორი რიცხვია! 1-დან 12-მდე შეიყვანეთ.")
elif month > 12:
    print("არასწორი რიცხვია! 1-დან 12-მდე შეიყვანეთ.")

elif month == 12:
    print("ზამთარი")
elif month == 1:
    print("ზამთარი")
elif month == 2:
    print("ზამთარი")
elif month == 3:
    print("გაზაფხული")
elif month == 4:
    print("გაზაფხული")
elif month == 5:
    print("გაზაფხული")
elif month == 6:
    print("ზაფხული")
elif month == 7:
    print("ზაფხული")
elif month == 8:
    print("ზაფხული")
elif month == 9:
    print("შემოდგომა")
elif month == 10:
    print("შემოდგომა")
elif month == 11:
    print("შემოდგომა")


name = input("შეიყვანეთ თქვენი სახელი: ")

if name == "admin":
    password = input("შეიყვანეთ ადმინის პაროლი: ")
    if password == "adminpassword123":
        print("სალამი ადმინ")
    else:
        print("წვდომა არ გაქვს")
else:
    print("სალამი მომხმარებელო")