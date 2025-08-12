for i in range(1,11):
    print(i)


i = 5
while i <= 19:
    print(i)
    i += 1


# Conditional statement => პირობითი განცხადებები.
# ამოწმებს პირობას (True ან False) და შედეგის მიხედვით წყვეტს, რომელი კოდი შესრულდეს.
# ვიყენებთ if და else-ს. მაგ:

age = 18

if age >= 18:
    print("You're an adult")
else:
    print("You're not an adult")


age = int(input("Put in your age: "))

if age >= 18:
    print("You're an adult.")
else:
    print("You're not an adult.")