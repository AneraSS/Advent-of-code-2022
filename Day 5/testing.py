def get_stacks(line):
    containers = []
    i = 0
    while i < len(line):
        current_char = line[i]
        if current_char == '[':
            containers.append(line[i + 1])
            i += 3  # tu mu kazem da preskoci tri znaka, dakle [A] npr.
        if current_char == ' ':
            containers.append(None)
            i += 3  # tu preskoci tri spacea
        i += 1  # tu preskocim sljedeci space
    return containers

with open('test.txt') as file_object:
    for line in file_object:
        print(get_stacks(line))