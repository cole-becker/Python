def main():
    # part 1

    defense = 5
    attack = 8
    hp = 10

    if attack <= defense:
        print("No damage, since the defense stat is too high.")

    if attack > defense:
        damage = attack - defense
        hp -= damage
        print(f"{damage} damage inflicted, enemy HP is now {hp}.")

    # part 2

    lab_mark = 9
    midterm_mark = 40
    final_exam_mark = 135

    student_final_mark = ((lab_mark/10)*30) + ((midterm_mark/80)*30) + ((final_exam_mark/180)*40)
    
    if student_final_mark < 50:
        print("This student's final grade is F.")
    
    elif student_final_mark < 60:
        print("This student's final grade is D.")
    
    elif student_final_mark < 70:
        print("This student's final grade is C.")
    
    elif student_final_mark < 80:
        print("This student's final grade is B.")
    
    else:
        print("This student's final grade is A.")

    # part 3
    
    long_string = 'the quick brown fox'
    vowels = "a", "e", "i", "o", "u"
    vowel_count = 0
    consonant = 0
    
    for letter in long_string:
        if letter in vowels:
            vowel_count += 1
        elif letter != ' ':
            consonant += 1
    
    print(f"The vowel to consonant ratio of '{long_string}' is {vowel_count} / {consonant} = {round(vowel_count/consonant, 2)}.")


if __name__ == "__main__":
    main()