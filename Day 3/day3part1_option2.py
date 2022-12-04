with open('test.txt') as file_object:
    for line in file_object:
        compartment_one = line[:int((len(line)/2))]
        print(compartment_one)
        compartment_two = line[int(len(line)/2):]
        print(compartment_two)


def get_common_character(string1,string2):
    for letter1 in string1:
        for letter2 in string2:
            if letter1 == letter2:
                return True
    return False


def is_in_string(character, string):
    for letter in string:
        if letter == character:
            return True
    return False


def get_value():
    for character in range(ord("a"), ord("z")):
        print(character)


alphabetic_value()