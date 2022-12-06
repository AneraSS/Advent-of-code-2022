# arg 1 : string - line in .txt
def get_stacks(string): # eg., [[a,b,c],[c,d],[e],[]]
    for character in string:
        stack_one = []
        if character == "[":
            if character.isalpha():
                stack_one.append(character)
            elif character == "    ":
                break
        return


def parse_line(line):   # returns: e.g., [None,B,None,D] ; None = 3x space



def parse_stack(string):    #returns A or None, and the rest of input string: [A, rest] or [None, rest]
    if string[0] == '[':
        return (string[1], string[4:])
    elif string[0] == " ":
        return (None, string[4:])

def parse_line(line):   # return
    while len(line) > 0: # as long as there is something in the line
    stack, remaining_string = parse_stack(line)
    stacks.append()

def get_stacks(line):
    i = 0
    while i < len(line):
        current_character = line[i]
        stack = []
        if current_character == '[':
            stack.append(line[i+1])
            i += 4
        elif current_character == ' ':
            stack.append(None)
            i += 4 #  da preskočimo space ispred sljedećeg broja
        return (stack)


# a sto je s /n kako to cita
# result:
# ['[P]     [L]         [T]            \n', '[L]     [M] [G]     [G]     [S]    \n', '[M]     [Q] [W]     [H] [R] [G]    \n', '[N]     [F] [M]     [D] [V] [R] [N]\n', '[W]     [G] [Q] [P] [J] [F] [M] [C]\n', '[V] [H] [B] [F] [H] [M] [B] [H] [B]\n', '[B] [Q] [D] [T] [T] [B] [N] [L] [D]\n', '[H] [M] [N] [Z] [M] [C] [M] [P] [P]\n', ' 1   2   3   4   5   6   7   8   9 \n', '\n', 'move 8 from 3 to 2\n', 'move 1 from 9 to 5']



with open('test.txt') as file_object:
    for line in file_object:
        print(get_stacks(line))