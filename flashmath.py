from collections import defaultdict as ddict
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
numbers = range(10)

def get_operator():
    if operator_type in [1, 2, 3, 4]:
        operator = operators[operator_type - 1]
    elif operator_type == 5:
        operator = random.choice(operators)
    return operator

n_correct = 0
operators = ['+', '-', '*', '/']
times = ddict(list)
for i in range(n_problems):
    # Choose problem operator
    operator = get_operator()
    operator_times = times[operator]

    # Choose problem LHS
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

    # Prompt user
    print()
    print(f"Problem {i}/{n_problems}")
    print(f"Correct: {n_correct}")
    problem = f'{a} {operator} {b}'
    print(problem + ' = ')
    start = time.time()
    guess = get_int('>>> ')
    stop = time.time()

    # Check if user correct
    answer = eval(problem)
    dt = stop - start
    operator_times.append(dt)
    times[operator] = operator_times
    print(f"Answered in {dt:0.2f} sec")
    if guess == answer:
        print('Correct!')
        n_correct += 1
    else:
        print(f'Incorrect. {problem} = {answer}')
    print()

if operator_type in [1, 2, 3, 4]:
    operator = operators[operator_type - 1]
    print()
    print(f"You got {n_correct}/{n_problems} correct!")
    print(f"Your accuracy was {n_correct/n_problems * 100}%")
    print()

    print(f"Your response times:")
    print(f"  Median = {statistics.median(times[operator]):0.2f} seconds")
    print(f"  Mean = {statistics.mean(times[operator]):0.2f} seconds")
    print(f"  Total = {sum(times[operator]):0.2f} seconds")
    print()
elif operator_type == 5:
    print()
    print(f"You got {n_correct}/{n_problems} correct!")
    print(f"Your accuracy was {n_correct/n_problems * 100}%")
    print()

    print(f"Your response times:")
    for operator in operators:
        t = times[operator]
        print(operator)
        if t:
            print(f"  Median = {statistics.median(t):0.2f} seconds")
            print(f"  Mean = {statistics.mean(t):0.2f} seconds")
            print(f"  Total = {sum(t):0.2f} seconds")
            print(f"  Count = {len(t)} problems")
        else:
            print(f"  No data for {operator}")

