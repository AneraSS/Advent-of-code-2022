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


with open('input.txt') as file_object:
    sum_of_values = 0
    for line in file_object:
        compartment_one = line[:int((len(line)/2))]
        compartment_two = line[int(len(line)/2):]
        common_letter = get_common_character(compartment_one,compartment_two)
        letter_value = get_value(common_letter)
        sum_of_values += letter_value
    print(sum_of_values)


