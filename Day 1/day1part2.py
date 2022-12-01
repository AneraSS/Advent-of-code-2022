with open('input.txt') as file_object:
    current_elf_calories = 0
    list_of_total_calories = []
    for line in file_object:
        if not line.isspace():
            current_elf_calories += int(line)
        else:
            list_of_total_calories.append(current_elf_calories)
            current_elf_calories = 0

    # because the last set of numbers doesn't have an empty space
    # in order to include the last elf in the data set
    list_of_total_calories.append(current_elf_calories)

    list_of_total_calories.sort(reverse=True)

print(sum(list_of_total_calories[0:3]))