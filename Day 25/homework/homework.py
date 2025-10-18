#I დავალება: შექმენი სია 7 რიცხვით.
#დაბეჭდე პირველი და ბოლო ელემენტების ნამრავლი ისე, რომ ორივეჯერ უარყოფითი ინდექსი გამოიყენო.
#დაბეჭდე მესამე ელემენტი მარცხნიდან და მესამე ელემენტი მარჯვნიდან (უარყოფითიინდექსის გამოყენებით).
numbers = [4, 1, 6, 7, 6, 9, 10]

result = numbers[-7] * numbers[-1]
print(result)

print(numbers[-5])
print(numbers[-3])


#II დავალება: შექმენი სია "apple", "banana", "cherry", "grape", "kiwi", "orange".
#დაბეჭდე შუა 2 ელემენტი (ორივე(დადებითი და უარყოფითი)) ინდექსით.
fruits = ["apple", "banana", "cherry", "grape", "kiwi", "orange"]

print(fruits[2])
print(fruits[3])

print(fruits[-4])
print(fruits[-3])


#III დავალება: შექმენი [3,4,5,6,7,1,2,9,8,11]
#მომხმარებელს შემოატანინე ერთი ინდექსი(რიცხვი) 0 დან 10 მდე.
#თუ მომხმარებლის ინდექსი დადებითია → დაბეჭდე ის ელემენტი
#თუ უარყოფით რიცხვი ან  10 ზე მეტი მაღალირიცხვი შემოიყვანა დაბეჭდეთ --> "you entered negative or more than 10  number "
nums = [3,4,5,6,7,1,2,9,8,11]

random_num = int(input("აირჩიე ერთი ინდექსი(რიცხვი) 0-10 მდე: "))

if random_num<0 or random_num>9:
    print("you entered negative or more than 10  number")
elif random_num>=0 and random_num<=9:
    print(nums[random_num])


#IV დავალება: შექმენით სია ["dog" ," most" ,"is" ,"angry" ,"running"  , "forest", "fast", "in" , "cat" ,"human", "very"]
#--- მინუს ინდექსების გამოყენებით შეადგინეთ შემდეგი წინადადება და დაბეჭდეთ --> "dog is running in forest very fast"
#--- აასწყვეთ ზემოთ მოცემული წინადადება ოღონდ დადებითი ინდექსებით
#--- დადებით ინდექსების გამოყენებით ააწყვეთ შემდეგი წინადადება ---> "cat is very angry"
random_list = ["dog" ," most" ,"is" ,"angry" ,"running"  , "forest", "fast", "in" , "cat" ,"human", "very"]

list_word = random_list[-11] + " " + random_list[-9] + " " + random_list[-7] + " " + random_list[-4] + " " + random_list[-6] + " " + random_list[-1] + " " + random_list[-5]
print(list_word)

list_word2 = random_list[0] + " " + random_list[2] + " " + random_list[4] + " " + random_list[7] + " " + random_list[5] + " " + random_list[10] + " " + random_list[6]
print(list_word2)

list_word3 = random_list[8] + " " + random_list[2] + " " + random_list[10] + " " + random_list[3]
print(list_word3)


#V დავალება: შექმენი სია ცხოველებით: ["dog", "cat", "horse", "cow", "sheep", "goat"].
#მომხმარებელს შემოიტანინე ინდექსი(რიცხვი)
#თუ მომხმარებლის მიერ შემოყვანილ ინდექსზე მდგომი ელემენტი არის  "cat", დაბეჭდე "შენ აირჩიე კატა".
#თუ არის "goat", დაბეჭდე "შენ აირჩიე თხა".
#სხვა შემთხვევაში დაბეჭდე "სხვა ცხოველი აირჩიე".
animals = ["dog", "cat", "horse", "cow", "sheep", "goat"]

random_animal = int(input("აირჩიე ერთი ინდექსი(რიცხვი): "))

if animals[random_animal] == "cat":
    print("შენ აირჩიე კატა")
elif animals[random_animal] == "goat":
    print("შენ აირჩიე თხა")
else:
    print("სხვა ცხოველი აირჩიე")


#VI დავალება: შექმენი სია 6 ქალაქით.
#მომხმარებელი შემოიტანს ორ ინდექსს(რიცხვს).
#თუ პირველი ინდექსი ნაკლებია მეორეზე → დაბეჭდე ამ ინდექსებზე მდგომი ორივე ელემენტი.
#თუ მეორე ნაკლებია პირველზე → დაბეჭდე "შეცვალე ინდექსები ადგილებით"--->ზემოთ თუ დაპრინტე a და b ამ შემთხვევაში დაპრინტე b და a.
#თუ ინდექსები ერთნაირია → დაბეჭდე "ორივე ერთია" და გამოიტანე ამ ინდექსზე მდგომი ელემენტი ვთქვათ თუ შემოიყვანა მომხმარებელმა 5 და 5
#დაუბეჭდე მე 5 ინდექსზე მდგომი ელემენტი.
cities = ["თბილისი", "რეიკიავიკი", "ნიუ-იორკ სიტი", "ბერნი", "რიო-დე-ჟანეირო", "ათენი"]

a = int(input("შეიყვანე პირველი ინდექსი (0-დან 5-მდე): "))
b = int(input("შეიყვანე მეორე ინდექსი (0-დან 5-მდე): "))

if a < b:
    print(cities[a] + " " + " " + cities[b])
elif b < a:
    print("შეცვალე ინდექსები ადგილებით")
    print(cities[b] + " " + " " + cities[a])
else:
    print("ორივე ერთია")
    print(cities[a])


#VII დავალება: მომხმარებელი შემოიტანს სიტყვას.
#თუ პირველი ასო "a"-ა → დაბეჭდე "სიტყვა იწყება a-თი".
#თუ ბოლო ასო "z"-ია → დაბეჭდე "სიტყვა მთავრდება z-ით".
#სხვაგვარად → დაბეჭდე "სიტყვა არც a-თი იწყება და არც z-ით მთავრდება".
word = str(input("Type in a random word: "))

if word[0] == "a":
    print("სიტყვა იწყება a-თი")
elif word[-1] == "z":
    print("სიტყვა მთავრდება z-ით")
else:
    print("სიტყვა არც a-თი იწყება და არც z-ით მთავრდება")


#VIII დავალება: მომხმარებელი შემოიტანს სიტყვას.
#თუ პირველი და ბოლო ასო ერთმანეთს ემთხვევა → დაბეჭდე "პირველი და ბოლო ერთნაირია".
#თუ განსხვავდება → "პირველი და ბოლო განსხვავებულია".
word = str(input("Type in a random word: "))

if word[0] == word[-1]:
    print("პირველი და ბოლო ერთნაირია")
else:
    print("პირველი და ბოლო განსხვავებულია")


#IX დავალება: შექმენი ცვლადი სადაც შეინახავთ შემდეგ ასოებს ---> "agivorsbgitr"
#----ამ სიიდან შეადგინე სიტყვა "goga, 
#----ამ სიტყვიდან შეადგინე სიტყვა "saba"
#----ამ სიტყვიდან შეადგინე სიტყვა "bativar"
random = "agivorsbgitr"

name1 = random[1] + random[4] + random[1] + random[0]
print(name1)

name2 = random[6] + random[0] + random[-5] + random[0]
print(name2)

name3 = random[-5] + random[0] + random[-2] + random[2] + random[3] + random[0] + random[-1]
print(name3)


#X დავალება: შექმენი შემდეგი სტრინგი --> 'giorgi'
#შენი დავალებააა რომ for და while loop ის დახმარებით გამოიტანო ამ სტრინგის თითეული ასო ცალ ცალკე
name = "giorgi"

for i in range(0,6):
    print(name[i])

print()

i = 0
while i < 6:
    print(name[i])
    i += 1