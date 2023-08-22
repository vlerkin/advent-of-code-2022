# advent of code 2022 - day 4

# part 1
"""
with open('input_problem_4.txt', 'r') as input:
    count_overlaps = 0
    for line in input:
        stripped = line.strip()
        ranges = stripped.split(',')
        e1_start, e1_end = map(int, ranges[0].split('-'))
        e2_start, e2_end = map(int, ranges[1].split('-'))
        if (e2_start >= e1_start and e2_end <= e1_end) or (e1_start >= e2_start and e1_end <= e2_end):
            count_overlaps += 1
    print(count_overlaps)
"""

# part 2
with open('input_problem_4.txt', 'r') as input:
    count_overlaps = 0
    for line in input:
        stripped = line.strip()
        ranges = stripped.split(',')
        e1_start, e1_end = map(int, ranges[0].split('-'))
        e2_start, e2_end = map(int, ranges[1].split('-'))
        if (e2_start >= e1_start and e2_end <= e1_end) or (e1_start >= e2_start and e1_end <= e2_end) or (e2_start <= e1_end and e2_end > e1_end) or (e1_start <= e2_end and e1_end > e2_end):
            count_overlaps += 1
    print(count_overlaps)
