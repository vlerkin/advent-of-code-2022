# advent of code 2022 - day 2

# O(n) complexity of algorithm 
with open('input_problem_2.txt', 'r') as input:
    # part 1
    #points_per_combination = {'AX': 4, 'AY':8, 'AZ': 3, 'BX': 1, 'BY': 5, 'BZ': 9, 'CX': 7, 'CY': 2, 'CZ': 6}
    # part 2
    points_per_combination = {'AX': 3, 'AY':4, 'AZ': 8, 'BX': 1, 'BY': 5, 'BZ': 9, 'CX': 2, 'CY': 6, 'CZ': 7}
    sum_points = 0
    for line in input:
        stripped = ''.join(line.strip().split(" "))
        sum_points = sum_points + points_per_combination[stripped]
    print(sum_points)