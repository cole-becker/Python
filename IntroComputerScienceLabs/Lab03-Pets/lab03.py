def main():
    # part 1

    pets = ['Spot', 'Boots', 'Mrs. Fluffington', 'Lenny', 'Bowser', 'Gina']
    count = 0
    pet_name_lengths = []

    # TODO: YOUR CODE TO COUNT THE NUMBER OF PETS AND THE LENGTH OF PET NAMES GOES HERE

    for pet in pets:
        count += 1

    for pet in pets:
        pet_name_lengths.append(len(pet))

    print(f'There are {count} pets in the list.')
    print(f'The word lengths of each pet name are {pet_name_lengths}.')

    # part 2

    words = ['the', 'quick', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog']
    word_vowel_ratios = []

    # TODO: YOUR CODE TO COUNT THE NUMBER OF VOWELS AND CONSONANTS IN EACH WORD TO CALCULATE THE RATIOS
    
    vowels = ['a', 'i', 'o', 'e', 'u']

    for word in words:
        vowel_count = 0
        consonant_count = 0
        for letter in word:
            if letter in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
        word_vowel_ratios.append(vowel_count/consonant_count)
    
    print(f"The vowel to consonant ratios of each word are {word_vowel_ratios}.")

if __name__ == "__main__":
    main()