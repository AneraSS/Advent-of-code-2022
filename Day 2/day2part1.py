# calculations:
# shape: rock (X=1), paper (Y= 2 ), sissors (Z = 3)
# outcome: win (6), draw (3), loose (0)

with open('input.txt') as file_object:
    calculator_end = 0
    calculator_X = 0
    calculator_Y = 0
    calculator_Z = 0
    for line in file_object:
        if line[0] == 'A':
            if line[2] == 'X':
                calculator_X += 1
                calculator_end += 3
            if line[2] == 'Y':
                calculator_Y +=2
                calculator_end += 6
            if line[2] == 'Z':
                calculator_Z +=3
                calculator_end +=0
        if line[0] == 'B':
            if line[2] == 'X':
                calculator_X += 1
                calculator_end += 0
            if line[2] == 'Y':
                calculator_Y += 2
                calculator_end += 3
            if line[2] == 'Z':
                calculator_Z += 3
                calculator_end += 6
        if line[0] == 'C':
            if line[2] == 'X':
                calculator_X += 1
                calculator_end += 6
            if line[2] == 'Y':
                calculator_Y += 2
                calculator_end += 0
            if line[2] == 'Z':
                calculator_Z += 3
                calculator_end += 3

end_points = calculator_end + calculator_X + calculator_Y + calculator_Z
print(end_points)