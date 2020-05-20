import random

def get_int(prompt):
    try_again = True
    result = None
    while try_again:
        entry = input(prompt)
        try:
            result = int(entry)
            try_again = False
        except ValueError:
           print('Invalid entry, try again')
           try_again = True
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


