list1 = ["ina" , "givi" , "nika" , "daviti" , "ia" , "lizi"]

list1[:2] = ["irina" , "milana" , "kira", "mate"]
list1[-2:] = ["gia" , "emzari" , "xvicha"]

print(list1)


num = int(input("შეიყვანეთ რიცხვი: "))

if num % 2 == 0:
    print("EVEN")
else:
    print("ODD")