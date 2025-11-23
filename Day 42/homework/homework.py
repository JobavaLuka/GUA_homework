#I დავალება: კომენტარის სახით ჩამოწერე თითეული სიის ფუნქცია რაც ვისწავლეთ და მიუწერეთ გვერდით ახსნა განმარტება თუ რა გადაეცემა თითეულს და რას 
#აკეთებს ის

print()

# .append() ფუნქციის დახმარებით შეგვიძლია სიაში ელემენტების ჩამატება, ოღონდ ელემენტებს ამატებს ყოველთვის სიის ბოლოში.
# გადავცემ იმ ელემენტს რაც მინდა რომ სიის ბოლოში ჩავამატო.

names = ["goga", "saba", "luka"]

names.append("natali")

print(names)

# .insert() ფუნქცია გვეხმარება, რომ ჩავამატოთ სიაში ელემენტები ნებისმიერ პოზიციაზე (სადაც გვინდა, რომელ ინდექსზეც გვინდა).
# გადავცემ რიცხვს (ინდექსი), რომელიც აღნიშნავს რომელ ინდექსზე მინდა ელემენტის ჩამატება (ამ შემთხვევაში 2-ს). ასევე გადავცემ რა ელემენტი მინდა რომ 
# ჩავამატო. ეს ჩვენი არჩევანია რას ჩავამატებთ, ანუ ნებისმიერი რამ რაც გვინდა (ამ შემთხვევაში ჩავამატე "mate").

names = ["goga", "saba", "luka"]

names.insert( 2 , "mate" )

print(names)

# .pop() ფუნქციის დახმარებით შეგვიძლია ამოვშალოთ ელემენტები სიიდან (არგუმენტად გადაეცემა ინდექსი თუ რომელ ინდექსზე მდგომი ელემენტის ამოშლა 
# გვსურს სიიდან). თუ .pop()-ს ფრჩხილებში არაფერი არ გადაეცემა მაშინ ის სიიდან ამოშლის ყოველთვის ბოლო ელემენტს.

names = ["goga", "saba", "luka"]

names.pop(1)

print(names)

# .remove() ფუნქციის დახმარებით შეგვიძლია ამოვშალოთ ელემენტი სიიდან (გადაეცემა თვითონ ის ელემენტი რომელიც გვინდა ამოვშალოთ სიიდან(ანუ 
# ელემენტის სახელი))

names = ["goga", 120, "saba", "luka", 290]

names.remove(120)
names.remove("saba")

print(names)

print()
print()


#II დავალება: შექმენი რიცხვების სია.
#append() ფუნქციით დაამატე მასში რიცხვი 10 ბოლოში.
#დაბეჭდე სია რომ ნახო ჩაემატა თუ არა

nums = [1, 2, 3, 4, 5]
nums.append(10)
print(nums)

print()
print()


#III დავალება: შექმენი სახელების სია.
#append() ფუნქციით დაამატე შენი სახელი სიის ბოლოში
#დაბეჭდე სია.

names = ["goga", "saba", "luka"]
names.append("Luka")
print(names)

print()
print()


#IV დავალება: შექმენი სია სადაც შეიყვან სახელებს, შენი დავალებაა მომხმარებელს შემოატანინო რაიმე სახელი და შეინახო ცვლადში, შემდეგ ჩაამატე append()ის 
#დახმარებით სიის ბოლოში მომხმარებლის შემოტანილი სიტყვა ~
#დაბეჭდე სია რომნახო ჩაემატა თუ არა

names = ["goga", "saba", "luka"]
input_name = input("შეიყვანე სახელი: ")
names.append(input_name)
print(names)

print()
print()


#V დავალება: შექმენი სია სადაც შეიყვანთ 5 სახეკს
#.insert() დახმარებით სიაში ჩაამატე მესამე ინდექსზე შენი სახელი

names = ["natali", "goga", "mate", "mari", "nikolozi"]
names.insert( 3 , "Luka")
print(names)

print()
print()


#VI დავალება: მომხმარებელს შემოატანინე სახელი და რიცხვი (integer 0 იდან 6 ჩათვლით)
#შენი დავალებაა შექმნა სია მინიმუმ 6 ელემენტიანი
#insert() დახმარებით დაამატე სიაში მომხმარებლის მიერ შემოტანილი რიცხვი, მომხმარებლის მიერ შემოტანილ ინდექსზე
#მაგ: მომხმარებელმა სახელი შემოიტანა საბა და რიცხვი 4 , შენი დავალებაა რომ საბა დაამატო მეოთხე ინდექსზე (გამოიყენე ცვლადის სახელები იმიტომ რომ არ 
#იცი მომხმარებელი რა მნშვნელობებს შემოიტანს
#დაბეჭდე სია რომ ნახო ჩაემატა თუ არა

my_list = ["a", "b", "c", "d", "e", "f"]

input_name = input("შეიყვანე სახელი: ")
input_num = int(input("შეიყვანე რიცხვი (0-დან 6-მდე): "))

my_list.insert(input_num, input_name)
print(my_list)

print()
print()


#VII დავალება: შექმენი სია:
#fruits = ["apple", "banana"]
#insert() ფუნქციით ჩასვი "orange" 1 ინდექსზე.

fruits = ["apple", "banana"]
fruits.insert( 1 , "orange")
print(fruits)

print()
print()


#VIII დავალება: შექმენი სია:
#names = ["goga", "saba", "luka"]
#insert()-ით ჩასვი "irakli" ბოლოს წინა პოზიციაზე ანუ ლუკას წინ

names = ["goga", "saba", "luka"]
names.insert( 2 , "irakli")
print(names)

print()
print()


#IX დავალება: შექმენი სია:
#foods = ["bread", "milk", "cheese"]
#insert() ფუნქციით ჩასვი "water" სიის დასაწყისში.

random = ["bread", "milk", "cheese"]
random.insert( 0 , "water")
print(random)

print()
print()


#X დავალება: შექმენი სია:numbers = [5, 10, 15]
#pop() ფუნქციით წაშალე ბოლო ელემენტი და დაბეჭდე განახლებული სია.

numbers = [5, 10, 15]
numbers.pop()
print(numbers)

print()
print()


#XI დავალება: შექმენი სია:
#fruits = ["apple", "banana", "orange"]
#pop -ით ამოშალე "banana" და დაბეჭდე დარჩენილი სია.

fruits = ["apple", "banana", "orange"]
fruits.pop(1)
print(fruits)

print()
print()


#XII დავალება: შექმენი სია:
#names = ["goga", "saba", "luka"]
#ამოშალე "saba" pop()-ით  — შემდეგ დაბეჭდე სია რომ ნახო ამოიშალა თუ არა

names = ["goga", "saba", "luka"]
names.pop(1)
print(names)

print()
print()


#XIII დავალება: შექმენი სია:
#colors = ["red", "green", "blue" , "yellow" , "black" , "purple"]
#pop()-ით წაშალე "red" და დაბეჭდე განახლებული სია.
#შემდეგ სიიდან ასევე ამოშალე yellow
#დაბეჭდე სია და ნახე შედეგი

colors = ["red", "green", "blue", "yellow", "black", "purple"]

colors.pop(0)
print(colors)

colors.pop("yellow")
print(colors)

print()
print()


#XIV დავალება: მომხმარებელს შემოტანინე რიცხვი(0 იდან 4 მდე და შეინახე ცვლადში
#შექმენი სია tems = ["pen", "pencil", "book", "eraser"] 
#pop ის დახმარებით სიიდან ამოშალე მომხმარებლის მიერ შემოტანილ რიცხვზე(ინდექსზე) მდგომი ელემენტი

school_items = ["pen", "pencil", "book", "eraser"]
user_num = int(input("შეიყვანე რიცხვი 0-დან 4-მდე: "))

school_items.pop(user_num)
print(school_items)

print()
print()


#XV დავალება: შექმენი სია:
#fruits = ["apple", "banana", "orange"]
#remove() ფუნქციით სიისდან წაშალე "banana".
#დაბეჭდე სია ნახე ამოიშალა თუ არა

fruits = ["apple", "banana", "orange"]
fruits.remove("banana")
print(fruits)

print()
print()


#XVI დავალება: შექმენი სია:
#nums = [3, 5, 3, 7]
#remove()-ით წაშალე 3 და დააკვირდი, მხოლოდ პირველი 3 იანი შაიშლება.
#დაბეჭდე სია რომ დარწმუნდე

nums = [3, 5, 3, 7]
nums.remove(3)
print(nums)

print()
print()


#XVII დავალება: შექმენი სია:
#colors = ["red", "blue", "green"]
#remove() ფუნქციით წაშალე "blue" და დაბეჭდე განახლებული სია.

colors = ["red", "blue", "green"]
colors.remove("blue")
print(colors)

print()
print()


#XVIII დავალება: შექმენი სია:
#names = ["goga", "saba", "luka"]
#მომხმარებელს შემოატანინე ამ სამიდან რომელიმე სახელი შეინახე ცვლადში და remove()-ით წაშალე მომხმარებლის შემოტანილი სახელი სიიდან.
#დაბეჭდე სია რომ გაიგო მართლა ამოიშალა თუ არა

names = ["goga", "saba", "luka"]
user_input = input("რომელი გინდა წაშალო (goga, saba, luka): ")

names.remove(user_input)
print(names)

print()
print()


#XIX დავალება: შექმენი სია:
#items = ["pen", "pencil", "book", "pencil"]
#remove()-ით წაშალე "pencil" და დაბეჭდე დარჩენილი სია.

school_items = ["pen", "pencil", "book", "pencil"]
school_items.remove("pencil")
print(school_items)

print()