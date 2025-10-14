#I დავალება: მოცემულია სტრინგი "PythonProgramming".
#ამოიღე პირველი 6 სიმბოლო და დაბეჭდე, გამოიყენეთ slicing

print()

string = "PythonProgramming"
print(string[:6])

print()
print()


#II დავალება: მოცემულია სია numbers = [10, 20, 30, 40, 50, 60, 70].
#ამოიღე მხოლოდ შუა 3 ელემენტი და დაბეჭდე, გამოიყენეთ slicing (მინუს ინდექსებითაც)

numbers = [10, 20, 30, 40, 50, 60, 70]
print(numbers[2:5])
print(numbers[-5:-2])

print()
print()


#III დავალება: მოცემულია სტრინგი "HelloWorld".
#დაბეჭდეთ Hello ტერმინალში slicing ის გამოყენებით (მინუს ინდექსებითაც)

string = "HelloWorld"
print(string[:5])
print(string[:-5])

print()
print()


#IV დავალება: მოცემულია სია letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g'].
#დაბეჭდე ყოველი პირველი, მესამე, მეხუთე ელემენტები, გამოიყენეთ indexing (მინუს ინდექსებითაც)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[0])
print(letters[2])
print(letters[4])

print(letters[-7])
print(letters[-5])
print(letters[-3])

print()
print()


#V დავალება: მოცემულია სტრინგი "Information".
#ამოიღე "forma" ნაწყვეტი slicing-ით (მინუს ინდექსებითაც)

string = "Information"
print(string[2:7])
print(string[-9:-4])

print()
print()


#VI დავალება: მოცემულია სტრინგი "abcdefghijklmno".
#შექმენი სამი სხვადასხვა სლაისი:
#პირველი შეიცავდეს მხოლოდ a დან d მდე ასოებს
#მეორე – შეიცავდეს j დან o მდე ასოებს
#მესამე – შეიცავდეს f დან j მდე ასოებს

string = "abcdefghijklmno"
print(string[0:3])
print(string[-6:-1])
print(string[5:-6])

print()