import random

def get_int(prompt):
    while True:
        entry = input(prompt)
        try:
            return int(entry)
        except ValueError:
           print('Invalid entry, try again')
    return result

print('How many questions?')
n_questions = get_int('>>> ')
numbers = range(10)

for i in range(n_questions):
    a = random.choice(numbers)
    b = random.choice(numbers)
    print(f'{a} + {b} =')
    guess = get_int('>>> ')
    answer = a + b
    if guess == answer:
        print('Correct!')
    else:
        print(f'Incorrect. {a} + {b} = {answer}')


