float_input = input("Enter a float value: ")
integer_input = input("Enter an integer value: ")
string_input = input("Enter a string value: ")

# გარდაქმნა შესაბამის ტიპებად:
# float ტიპის მნიშვნელობა გარდაქმნის შემდეგ ხდება boolean
float_to_boolean = bool(float_input)

# integer ტიპის მნიშვნელობა გარდაქმნის შემდეგ ხდება integer
integer_to_integer = int(integer_input)

# string ტიპის მნიშვნელობა რჩება string-ად
string_value = str(string_input)

# შედეგების დაბეჭდვა:
print(float_to_boolean)
print(integer_to_integer)
print(string_value)