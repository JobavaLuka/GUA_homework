#I დავალება: შექმენი სია ხილებზე და დაამატე მასში კიდევ 2 ხილი extend() ფუნქციით.

print()

fruits1 = ["apple", "banana", "orange"]
fruits2 = ["kiwi", "mango"]

fruits1.extend(fruits2)
print(fruits1)

print()
print()


#II დავალება: შექმენი სია numbers და დაამატე მასში [40, 50] extend()-ით.

numbers = [10, 20, 30]
numbers2 = [40, 50]

numbers.extend(numbers2)
print(numbers)

print()
print()


#III დავალება: შექმენი სია names და შეაბრუნე reverse()-ით.

names = ["luka", "saba", "goga"]
names.reverse()
print(names)

print()
print()


#IV დავალება: შექმენი სია სახელად nums და დათვალე რამდენი ცალი 5 არის მასში count()-ით.

nums = [5, 1, 2, 5, 3, 4, 5, 5, 6, 7, 5, 8, 5, 9, 10]
print(nums.count(5))

print()
print()


#V დავალება: შექმენი letters = ["a","b","a","c"] და დაბეჭდე რამდენი ცალი "a" არის ჩვენს სიაში.

letters = ["a","b","a","c"]
print(letters.count("a"))

print()
print()


#VI დავალება: შექმენი სია სახელად names და იპოვე "saba"-ს ინდექსი index()-ით.

names = ["goga", "saba", "luka"]
print(names.index("saba"))

print()
print()


#VII დავალება: შექმენი list = ["red","green","blue"] და იპოვე რომელ ინდექსზე დგას "blue". გამოიყენე შესაბამისი ფუნქცია.

list1 = ["red","green","blue"]
print(list1.index("blue"))

print()
print()


#VIII დავალება: შექმენი სია სახელად nums და დამატე მასში extend()-ით [7, 8, 9].

nums = [1, 2, 3, 4, 5, 6]
nums2 = [7, 8, 9]

nums.extend(nums2)
print(nums)

print()
print()


#IX დავალება: შექმენი სია სახელად foods და დააბრუნე შებრუნებული სია.

foods = ["khinkali", "megruli khachapuri", "qababi"]
foods.reverse()
print(foods)

print()
print()


#X დავალება: შექმენი სია cities და იპოვე რომელ ინდექსზე დგას "tbilisi".

cities = ["zugdidi", "batumi", "tbilisi", "qutaisi", "foti"]
print(cities.index("tbilisi"))

print()
print()


#XI დავალება: შექმენი animals = ["cat","dog","cat","cow"] და დაითვალე ამ სიაში რამდენი "cat" არის.

animals = ["cat","dog","cat","cow"]
print(animals.count("cat"))

print()
print()


#XII დავალება: შექმენი სია fruits = ["apple", "banana"] და append ფუნქციით დაამატე "grape". დაბეჭდე სია.

fruits = ["apple", "banana"]
fruits.append("grape")
print(fruits)

print()
print()


#XIII დავალება: შექმენი სია numbers = [1, 2, 3] და extend()-ით დაუმატე [4, 5]. დაბეჭდე სია.

numbers = [1, 2, 3]
numbers2 = [4, 5]

numbers.extend(numbers2)
print(numbers)

print()
print()


#XIV დავალება: შექმენი სია names = ["goga", "saba"] და insert()-ით ჩასვი "luka" პირველ ინდექსზე. დაბეჭდე სია.

names = ["goga", "saba"]
names.insert(1, "luka")
print(names)

print()
print()


#XV დავალება: შექმენი სია items = ["pen", "pencil", "eraser"] და pop()-ით წაშალე ბოლო ელემენტი; დაბეჭდე განახლებული სია.

items = ["pen", "pencil", "eraser"]
items.pop()
print(items)

print()
print()


#XVI დავალება: შექმენი სია colors = ["red", "green", "blue"] და remove()-ით წაშალე "green". დაბეჭდე შედეგი.

colors = ["red", "green", "blue"]
colors.remove("green")
print(colors)

print()
print()


#XVII დავალება: შექმენი სია foods = ["bread", "milk"]. შეამოწმე სიაში 2 ელემენტია თუ მეტი — თუ ორია, append()-ით დაამატე "cheese", შემდეგ დაბეჭდე 
#სია, სხვა შემთხვევაში append()-ით დაამატე "meat" და დაბეჭდე სია.

foods = ["bread", "milk"]

if len(foods) == 2:
    foods.append("cheese")
else:
    foods.append("meat")

print(foods)

print()
print()


#XVIII დავალება: შექმენი სია nums = [10, 20, 30]. მომხმარებელს შემოატანინე მთელი რიცხვი. თუ რიცხვი nums სიაშია, დაბეჭდე "Already in list", 
#თუ არა — append()-ით დაამატე 40 და დაბეჭდე სია.

nums = [10, 20, 30]
input_num = int(input("Enter a number: "))

if input_num in nums:
    print("Already in list")
else:
    nums.append(40)
    print(nums)

print()
print()


#XIX დავალება: შექმენი სია letters = ["a", "b", "c"]. მომხმარებელს შემოატანინე ასო, შემდეგ insert()-ით ჩასვი ის სიის შუაში (ცენტრალურ ინდექსზე). 
#დაბეჭდე სია.

letters = ["a", "b", "c"]
input_letter = input("Enter a letter")

letters.insert( 1 , input_letter)

print(letters)

print()
print()


#XX დავალება: შექმენი სია values = [1, 2, 3, 4]. მომხმარებელს შემოატანინე ინდექსი. თუ ინდექსი სიის ფარგლებშია, pop()-ით ამოშალე შესაბამისი 
#ელემენტი; თუ არა, დაბეჭდე "Index out of range". ბოლოს დაბეჭდე სია.

values = [1, 2, 3, 4]
input_index = int(input("Enter index: "))

if input_index in values:
    values.pop(input_index)
else:
    print("Index out of range")

print(values)

print()
print()


#XXI დავალება: შექმენი სია pets = ["cat", "dog", "hamster"]. მომხმარებელს შემოატანინე შინაური ცხოველის სახელი. თუ იგი არის სიის შიგნით, 
#remove()-ით ამოშალე და დაბეჭდე "Removed", თუ არა — დაბეჭდე "Not found" და სია უცვლელი დატოვე; საბოლოოდ დაბეჭდე სია.

pets = ["cat", "dog", "hamster"]
pet_name = input("Enter pet name: ")

if pet_name in pets:
    pets.remove(pet_name)
    print(pet_name , "Removed")
else:
    print("Not found")

print(pets)

print()
print()


#XXII დავალება: შექმენი სია a = [5, 5, 7]. მომხმარებელს შემოატანინე რიცხვი. თუ რიცხვი არის სიის ელემენტი, დაბეჭდე რამდენჯერ არის სიაში - count() 
#ფუნქციის გამოყენებით. სხვა შემთხვევაში append()-ით ჩასვი ის სიაში და დაბეჭდე სია.

a = [5, 5, 7]
input_num = int(input("Enter a number: "))

if input_num in a:
    a.count(input_num)
    print(a)
else:
    a.append(input_num)
    print(a)

print()
print()


#XXIII დავალება: შექმენი სია queue = ["first", "second"].  მომხმარებელს შემოატანინე ახალი ელემენტი და insert()-ით ჩასვი სიის დასაწყისში. შემდეგ 
#if-ით შეამოწმე სიის სიგრძე — თუ უფრო დიდია 5-ზე, pop()-ით ამოშალე ბოლო ელემენტი; ბოლოს დაბეჭდე სია, თუ არ არის 5-ზე მეტი დაბეჭდე 
#შებრუნებული სია.

queue = ["first", "second"]
new_element = input("Enter a new element: ")

queue.insert( 0 , new_element)

if len(queue) > 5:
    queue.pop()
    print(queue.reverse())
else:
    print(queue)

print()
print()


#XXIV დავალება: შექმენი სია nums = [2, 4, 6].  მომხმარებელს შემოატანინე რიცხვი. თუ რიცხვი დადებულია, append()-ით დაამატე; თუ 0-ია ან ნაკლებია 
#ნულზე, დაბეჭდე "Only positive allowed". ბოლოს დაბეჭდე სია.

nums = [2, 4, 6]
input_num = int(input("Enter a number: "))

if input_num > 0:
    nums.append(input_num)
else:
    print("Only positive allowed")

print(nums)

print()
print()


#XXV დავალება: შექმენი სია mix = ["x", "y", "z"]. extend()-ით დაუმატე [1, 2, 3]. შემდეგ მომხმარებელს შემოატანინე ასო; თუ ეს ასო არის სიაში, 
#remove()-ით წაშალე პირველად როცა შეგხვდება და დაბეჭდე "Removed", თუ არა — დაბეჭდე "No such element". ბოლოს დაბეჭდე სია.

mix = ["x", "y", "z"]
mix.extend([1, 2, 3])

input_letter = input("Enter a letter: ")

if input_letter in mix:
    mix.remove(input_letter)
    print("Removed")
else:
    print("No such element")

print(mix)

print()