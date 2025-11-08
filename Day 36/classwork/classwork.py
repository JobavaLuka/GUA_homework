random = input("შეიყვანე სიტყვა ან ტექსტი: ")

print("a" in random)
print("A" in random)

print("car" not in random)


text = input("შეიყვანეთ ტექსტი: ")

for i in text:
    if i == 'a' or i == 'A':
        continue
    print(i)