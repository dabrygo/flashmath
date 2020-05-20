import random

n_questions = 10
numbers = range(10)

for i in range(n_questions):
    a = random.choice(numbers)
    b = random.choice(numbers)
    print(f'{a} + {b} =')
    guess = int(input('>>> '))
    answer = a + b
    if guess == answer:
        print("Correct!")
    else:
        print(f"Incorrect. {a} + {b} = {answer}")


