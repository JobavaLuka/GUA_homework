random = input("შეიყვანეთ სიტყვა ან ტექსტი: ")

print(len(random))
print()

for i in range(len(random)):
    print(random[i])


words = ["word", "Word", "wOrd", "woRd", "worD"]

for i in words:
    print("ეს სიტყვა შედგება ", len(i), "სიმბოლოსგან")
    if len(i) % 2 == 0:
        print("ლუწია")
    else:
        print("კენტია")