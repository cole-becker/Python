# Lab 05

# TODO: YOUR is_vowel() FUNCTION FROM THE PREVIOUS LAB GOES HERE

def is_vowel(character):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if character in vowels:
        return True
    
    else:
        return False

# part 1

# TODO: YOUR count_vowels_rec() FUNCTION FROM THE PREVIOUS LAB GOES HERE

def count_vowels_rec(sentence):
    if sentence == "":
        return 0
    
    if sentence[0].lower() in 'aeiou':
        return 1 + count_vowels_rec(sentence[1:])
    else:
        return count_vowels_rec(sentence[1:])

# part 2

# TODO: YOUR count_vowels_ho() FUNCTION GOES HERE

def count_vowels_ho(sentence):
    vowels = filter(is_vowel, sentence)

    return len(list(vowels))

# part 3

# TODO: YOUR my_reduce_iter() FUNCTION GOES HERE

def my_reduce_iter(values, start_val, op):
    current_value = start_val
    
    for value in values:
        current_value = op(current_value, value)

    return current_value

# part 4

# TODO: YOUR my_reduce_rec() FUNCTION GOES HERE

def my_reduce_rec(values, start_val, op):
    if not values:
        return start_val
    
    return op(values[0], my_reduce_rec(values[1:], start_val, op))