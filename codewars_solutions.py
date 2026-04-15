# even or odd

def even_or_odd(number):
    if number%2 == 0:
        return ("Even")
    else:
        return ("Odd")
    

# convert number to string

def number_to_string(num):
    return str(num)


#remove string spaces
def no_space(x):
    return x.replace(" ","")

#vowel count

def get_count(sentence):
    count = 0
    
    for char in sentence:
        if char in "aeiou":
            count += 1
            
    return count