def get_value(letter):
    for character_index in range(ord("a"), ord("z")+1):
        if character_index == ord(letter):
            its_value = ord(letter)-96
            return its_value
    for character_index in range(ord("A"), ord("Z")+1):
        if character_index == ord(letter):
            its_value = ord(letter)-38
            return its_value
    raise Exception (f"Letter {letter} not supported!")

def get_common_letter(rucksack1, rucksack2, rucksack3):
    for letter in rucksack1:
        if is_in_string(letter,rucksack2) and is_in_string(letter,rucksack3):
            return letter

def is_in_string(character, string):
    for letter in string:
        if letter == character:
            return True
    return False

with open('input.txt') as file_object:
    sum_of_values = 0
    rucksacks = []
    for line in file_object:
        rucksacks.append(line.rstrip('\n'))

    current_group = []
    for rucksack in rucksacks:
        current_group.append(rucksack)
        if len(current_group) == 3:
            [rucksack1,rucksack2,rucksack3] = current_group[0:3]
            sum_of_values += get_value(get_common_letter(rucksack1,rucksack2,rucksack3))
            current_group = []
    print(sum_of_values)