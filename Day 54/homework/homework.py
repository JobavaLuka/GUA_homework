#I დავალება: შექმენით სიტყვებით სავსე სია, თუ სიტყვის ყველა ასო არის პატარა და პირველი ასო არის g, მაშინ ახალ სიაში ჩაამატეთ სახელი "Goga", თუ 
#სიტყვის ყველა ასო არის დიდი ან იწყება ასო N-თი, მაშინ სიაში ჩაამატეთ სახელი "Nika", სხვა შემთხვევაში სიაში ჩაამატეთ სიტყვა "ლიდერი". დაპრინტეთ 
#მიღებული სია.

print()

words = ["goga", "nose", "microphone", "NUCLEAR", "market", "gotham", "hive"]

empty_list = []

for i in words:
    if i == i.lower() and i[0] == "g":
        empty_list.append("Goga")
    elif i == i.upper() or i[0] == "N":
        empty_list.append("Nika")
    else:
        empty_list.append("ლიდერი")

print(empty_list)

print()
print()


#II დავალება: შექმენით რიცხვებით სავსე სია, თუ რიცხვი არის ლუწი ან დგას ლუწ ინდექსზე, ჩაამატეთ მისი კვადრატი ახალ სიაში - გამოიყენეთ შესაბამისი 
#მათემატიკური ოპერატორი, ხოლო თუ რიცხვი არის კენტი ან დგას კენტ ინდექსზე, ახალ სიაში ჩაამატეთ 2-ჯერ დიდი რიცხვი. გამოიყენეთ while ციკლი.

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

empty_list = []

i = 0
while i < len(nums):
    if nums[i] % 2 == 0 or i % 2 == 0:
        empty_list.append(nums[i] ** 2)
    else:
        empty_list.append(nums[i] * 2)
    i += 1

print(empty_list)

print()
print()


#III დავალება: შექმენით სიტყვებით სავსე სია, თუ სიტყვის სიგრძე არის 6-ზე მეტი ან მისი ყველა ასო არის დიდი, ამ სიტყვის ყველა ასო გახადეთ პატარა და 
#ჩაამატეთ ახალ სიაში. ყველა სხვა შემთხვევაში ახალ სიაში ჩაამატეთ შეუცვლელი სიტყვა ოღონდ გადაბმულად ორჯერ, მაგალითად თუ მოცემული იქნება სიტყვა 
#"Nika", ჩაამატეთ "NikaNika". გამოიყენეთ while ციკლი.

words = ["Left", "WEST", "North", "CENTER", "South", "east", "right"]
empty_list = []

i = 0
while i < len(words):
    if len(words[i]) > 6 or words[i] == words[i].upper():
        empty_list.append(words[i].lower())
    else:
        empty_list.append(words[i] + words[i])
    i += 1

print(empty_list)

print()
print()


#IV დავალება: მოცემული გაქვთ სტრინგის ცვლადი: numbers = "0123456789", ამ სტრინგიდან ახალ სიაში ჩაამატეთ ყველა ის რიცხვი რომელიც დგას ამ 
#სტრინგის ლუწ ინდექსზე ან არის 7-ზე მეტი, სიაში ეს რიცხვები იყოს როგორც integer ტიპის მონაცემები და არა სტრინგები. დაწერეთ ორივე ხერხით, for 
#ციკლით და while ციკლით.

nums = "0123456789"
empty_list = []

for i in range(len(nums)):
    if i % 2 == 0 or int(nums[i]) > 7:
        empty_list.append(int(nums[i]))

print(empty_list)

print()