def get_common_character(string1,string2):
    for letter in string1:
        if is_in_string(letter,string2):
            return letter


def is_in_string(character, string):
    for letter in string:
        if letter == character:
            return True
    return False


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

def common_letter(rucksack1, rucksack2, rucksack3):
    for letter in rucksack1:
        if is_in_string(letter,rucksack2) and is_in_string(letter,rucksack3):
            return letter


sum_of_values = 0
with open('test.txt') as file_object:
    rucksacks = []
    for line in file_object:
        rucksacks.append(line.rstrip('\n'))

    current_group = []
    for rucksack in rucksacks:
        if len(current_group) < 3:
            current_group.append(rucksack)
        else:
            rucksack1 = current_group[0]
            rucksack2 = current_group[1]
            rucksack3 = current_group[2]
            print(rucksack1)
            common_letter = common_letter(rucksack1,rucksack2,rucksack3)
            its_value = get_value(common_letter)
            sum_of_values += its_value
            current_group = []
            current_group.append(rucksack)
            # last rucksack is not added!!! see other .py
    print(sum_of_values)