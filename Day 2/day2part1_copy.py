# calculations:
# shape: rock (X=1), paper (Y= 2 ), sissors (Z = 3)
# outcome: win (6), draw (3), loose (0)

with open('input.txt') as file_object:
    result = 0
    for line in file_object:
        if line[0] == 'A':
            if line[2] == 'X':
                result += 1 + 3
            if line[2] == 'Y':
                result +=2 + 6
            if line[2] == 'Z':
                result +=3 + 0
        if line[0] == 'B':
            if line[2] == 'X':
                result += 1 + 0
            if line[2] == 'Y':
                result += 2 + 3
            if line[2] == 'Z':
                result += 3 + 6
        if line[0] == 'C':
            if line[2] == 'X':
                result += 1 + 6
            if line[2] == 'Y':
                result += 2 + 0
            if line[2] == 'Z':
                result += 3 + 3

print(result)