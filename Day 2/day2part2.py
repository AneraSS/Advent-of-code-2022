# calculations:
# shape: rock (X=1), paper (Y= 2 ), scissors (Z = 3)
# outcome: win (6), draw (3), loose (0)

with open('input.txt') as file_object:
    result = 0
    for line in file_object:
        if line[2] == 'X':
            # X means 'loose' (0)
            if line[0] == 'A':
                # A = rock, scissors (3)
                result += 0 + 3
            if line[0] == 'B':
                # B = paper, rock (1)
                result += 0 +1
            if line[0] == 'C':
                # C = scissors, paper (2)
                result += 0+2
        if line[2] == 'Y':
            # Y means 'draw' (3)
            if line[0] == 'A':
                # A = rock, rock (1)
                result += 3 + 1
            if line[0] == 'B':
                # B = paper, paper (2)
                result += 3 +2
            if line[0] == 'C':
                # C = scissors, scissors (3)
                result += 3 +3
        if line[2] == 'Z':
            # Z means 'win' (6)
            if line[0] == 'A':
                # A = rock, paper (2)
                result += 6 + 2
            if line[0] == 'B':
                # B = paper, scissors (3)
                result += 6 +3
            if line[0] == 'C':
                # C = scissors, rock (1)
                result += 6+1

print(result)