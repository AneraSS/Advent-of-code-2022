def extract_first_number(string):
    digits = ""
    for character in string:
        if character.isdigit():
            digits += character
        else:
            break
    return int(digits), string[len(digits):]

def parse_range(string):        # returns ((int, int), rest)
    number_one, reduced_string_one = extract_first_number(string)
    number_two, reduced_string_two = extract_first_number(reduced_string_one[1:])
    return (number_one, number_two), reduced_string_two

def parse_pair_of_ranges(string):    # returns four numbers as two pairs: ((a,b),(c,d)) - as tuple
    range1, reduced_string = parse_range(string)
    range2, twice_reduced_string = parse_range(reduced_string[1:]) # [1:] due to comma in str
    return (range1, range2)

def do_ranges_overlap(range1, range2):      # bool
    a, b = range1   # pattern-matching! bc range1 is (a, b)
    c, d = range2
    return not ((d<a) or (b<c)) # only situation when they cannot overlap

with open('input.txt') as file_object:
    count = 0
    for line in file_object:
        (range1, range2) = parse_pair_of_ranges(line)
        if do_ranges_overlap(range1, range2):
            count += 1
    print(count)