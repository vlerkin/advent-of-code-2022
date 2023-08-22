# advent of code 2022 - day 3


"""
#part 1
with open('input_mock.txt', 'r') as input:
    lowercase_priority = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
                          'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
    uppercase_priority = {char.upper(): value + 26 for char,
                          value in lowercase_priority.items()}
    
    sum_priority = 0
    for i, line in enumerate(input):
        stripped = line.strip()
        first_compartment = stripped[:len(stripped)//2]
        second_compartment= stripped[len(stripped)//2:]
        repeated_values = []
        for letter in first_compartment:
            if letter in second_compartment and letter not in repeated_values:
                repeated_values.append(letter)
                if lowercase_priority.get(letter) != None:
                    sum_priority = sum_priority + lowercase_priority[letter]
                else:
                    sum_priority = sum_priority + uppercase_priority[letter]
    print(sum_priority)
"""
# part 2
with open('input_problem_3.txt', 'r') as input:
    lowercase_priority = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
                          'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
    uppercase_priority = {char.upper(): value + 26 for char,
                          value in lowercase_priority.items()}
    lines = input.readlines()
    grouped_lines = [lines[i:i+3] for i in range(0, len(lines), 3)]
    sum_priority = 0
    for group in grouped_lines:
        repeated_values = []
        if len(group) == 3:
            line1 = group[0].strip()
            line2 = group[1].strip()
            line3 = group[2].strip()
            for letter in line1:
                if letter in line2 and letter in line3 and letter not in repeated_values:
                    repeated_values.append(letter)
                    if lowercase_priority.get(letter) != None:
                        sum_priority = sum_priority + \
                            lowercase_priority[letter]
                    else:
                        sum_priority = sum_priority + \
                            uppercase_priority[letter]
        else:
            print('the number of lines is not multiple of 3!')
    print(sum_priority)
