import abc
import random

def get_int(prompt):
    while True:
        entry = input(prompt)
        try:
            return int(entry)
        except ValueError:
           print('Invalid entry, try again')
    return result

# Prompt for operator
print('What kind of questions?')
print('1 Addition')
print('2 Subtraction')
print('3 Multiplication')
print('4 Division')
operator_type = get_int('>>> ')
if operator_type not in [1, 2, 3, 4]:
    raise RuntimeError(f'No option for {operator_type}')

# Prompt for questions
print('How many questions?')
n_questions = get_int('>>> ')
numbers = range(10)

operators = ['+', '-', '*', '/']
operator = operators[operator_type - 1]
for i in range(n_questions):
    if operator in ['+', '*']:
        a = random.choice(numbers)
        b = random.choice(numbers)
    elif operator == '-':
        x = random.choice(numbers)
        y = random.choice(numbers)
        a = max(x, y)
        b = min(x, y)
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
    problem = f'{a} {operator} {b}'
    print(problem + ' = ')
    guess = get_int('>>> ')
    answer = eval(problem)
    if guess == answer:
        print('Correct!')
    else:
        print(f'Incorrect. {problem} = {answer}')


