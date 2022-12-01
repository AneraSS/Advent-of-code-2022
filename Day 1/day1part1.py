with open('input.txt') as file_object:
    current_elf_calories = 0
    max_sum = 0
    for line in file_object:
        if not line.isspace():
            current_elf_calories += int(line)
        else:
            if current_elf_calories > max_sum:
                max_sum = current_elf_calories
            current_elf_calories = 0

    # because the last set of numbers doesn't have an empty space
    # in order to include the last elf in the data set
    if current_elf_calories > max_sum:
        max_sum = current_elf_calories
    current_elf_calories = 0

print(max_sum)