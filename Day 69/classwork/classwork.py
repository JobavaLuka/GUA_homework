def multiply(a, b):
    return a * b



def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"



def number_to_string(num):
    return str(num)



def make_negative( number ):
    if number < 0:
        return number
    elif number > 0:
        return -number
    else:
        return 0



def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    else:
        return "No"