
# advent of code 2022 - day 1

with open('input_problem_1.txt', 'r') as input:
    calories_per_elf = {}
    current_value = 0
    #sum_of_calories = 0
    i = 0
    for line in input:
        stripped = line.strip()
        if stripped != "":
            current_value = current_value + int(stripped)
        else:
            calories_per_elf[i] = current_value
            current_value = 0
            i += 1
    # part 1 
    # highest_calories =  sorted(calories_per_elf.values(), reverse=True)[0]
    # part 2       
    highest_calories =  sum(sorted(calories_per_elf.values(), reverse=True)[:3])   
    print(highest_calories)