from collections import defaultdict as ddict
import matplotlib.pyplot as plt
import numpy as np
import random
import statistics
import time

def get_int(prompt):
    while True:
        entry = input(prompt)
        try:
            return int(entry)
        except ValueError:
           print('Invalid entry, try again')
    return result

# Prompt for operator
print('What kind of problems?')
print('1 Addition')
print('2 Subtraction')
print('3 Multiplication')
print('4 Division')
print('5 Random')
operator_type = get_int('>>> ')
if operator_type not in [1, 2, 3, 4, 5]:
    raise RuntimeError(f'No option for {operator_type}')

# Prompt for problems
print('How many problems?')
n_problems = get_int('>>> ')

# Prompt for maximum number
print('Highest number?')
max_number = get_int('>>> ')
numbers = range(max_number)

operators = ['+', '-', '*', '/']
def get_operator():
    '''Choose problem operator'''
    if operator_type in [1, 2, 3, 4]:
        operator = operators[operator_type - 1]
    elif operator_type == 5:
        operator = random.choice(operators)
    return operator

def get_operands():
    '''Choose problem LHS'''
    if operator in ['+', '*']:
        a = random.choice(numbers)
        b = random.choice(numbers)
    elif operator == '-':
        x = random.choice(numbers)
        y = random.choice(numbers)
        z = x + y
        a = z
        use_x = random.choice([0, 1])
        b = x if use_x else y
    elif operator == '/':
        z = 0
        while z == 0:
            x = random.choice(numbers)
            y = random.choice(numbers)
            z = x * y
        a = z
        use_x = random.choice([0, 1])
        b = x if use_x else y
    else:
        raise NotImplementedError(f'Operator {operator} not yet supported')
    return a, b

n_correct = 0
corrects = ddict(list)
times = ddict(list)
for i in range(n_problems):
    # Prompt user
    operator = get_operator()
    a, b = get_operands()
    print()
    print(f"Problem {i}/{n_problems}")
    print(f"Correct: {n_correct}")
    problem = f'{a} {operator} {b}'
    print(problem + ' = ')

    # Time user for response
    start = time.time()
    guess = get_int('>>> ')
    stop = time.time()
    dt = stop - start
    operator_times = times[operator]
    operator_times.append(dt)

    # Check if user correct
    answer = eval(problem)
    times[operator] = operator_times
    print(f"Answered in {dt:0.2f} sec")
    operator_corrects = corrects[operator]
    if guess == answer:
        print('Correct!')
        n_correct += 1
        operator_corrects.append(True)
    else:
        print(f'Incorrect. {problem} = {answer}')
        operator_corrects.append(False)
        input("Press ENTER to continue\n")
    corrects[operator] = operator_corrects
    print()


if operator_type in [1, 2, 3, 4]:
    operator = operators[operator_type - 1]
    print()
    print(f"You got {n_correct}/{n_problems} correct!")
    print(f"Your accuracy was {n_correct/n_problems * 100:0.2f}%")
    print()

    plt.hist(times[operator])
    plt.xlabel("Time (s)")
    plt.ylabel("Count")
    plt.show()
elif operator_type == 5:
    print()
    print(f"You got {n_correct}/{n_problems} correct!")
    print(f"Your accuracy was {n_correct/n_problems * 100:0.2f}%")
    for operator in operators:
        c = corrects[operator]
        print(operator)
        if c:
            print(f"  Correct: {sum(c)}")
            print(f"  Accuracy: {sum(c)/len(c) * 100:0.2f}%")
            print(f"  Count = {len(c)} problems")
        else:
            print(f"  No data for {operator}")

    colors = ['red', 'orange', 'yellow', 'blue']
    fig, axes = plt.subplots(2, 2)
    plt.suptitle("Times")
    for i, operator in enumerate(operators):
        t = times[operator]
        row = i // 2
        col = i % 2
        ax = axes[row, col]
        ax.hist(t, color=colors[i])
        ax.set_title(f'{operator} ({len(t)} Problems)')
        ax.set(xlabel='Time (s)', ylabel='Count')
    plt.xlabel("Time (s)")
    plt.ylabel("Count")
    plt.show()

