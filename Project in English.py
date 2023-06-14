import random
import time

# Define the minimum number for each operation
min_num = 1
# Allow user to define the maximum number for each operation
max_num = int(input("Défine the highest number for each problem : "))


# Allow user to define the number of operations to generate
num_problems = int(input("How many math problems would you like to generate ? : "))

# Define the types of operations
operations = ['addition', 'subtraction', 'multiplication', 'division']

# Define a function to randomly generate maths problems
def generate_problem(operation):
    
    if operation == 'addition':
        a = random.randint(min_num, max_num)
        b = random.randint(min_num, max_num)
        problem = f'{a} + {b}'
        answer = a + b
    elif operation == 'subtraction':
        a = random.randint(min_num, max_num)
        b = random.randint(min_num, max_num)
        problem = f'{a} - {b}'
        answer = a - b
    elif operation == 'multiplication':
        a = random.randint(min_num, max_num)
        b = random.randint(min_num, max_num)
        problem = f'{a} x {b}'
        answer = a * b
    elif operation == 'division':
        b = random.randint(min_num, max_num)
        answer = random.randint(min_num, max_num)
        a = b * answer
        while a > max_num:
            b = random.randint(min_num, max_num)
            a = b * answer
        problem = f'{a} / {b}'
    return problem, answer

# Define a fonction to run the game
def play_game():
    score = 0
    for i in range(num_problems):
        # Random selection of the math problem
        operation = random.choice(operations)

        # Generate a math problem randomly 
        problem, answer = generate_problem(operation)

        # Display the problem on the screen
        print(f'Problem {i+1}: {problem}')

        # Start a timer 
        start_time = time.time()

        # Allow user to input answer
        user_answer = input('Your answer: ')

        # Verify user's answer against the correct answer
        if int(user_answer) == answer:
            print('Correct!')
            score += 1
        else:
            print(f'Incorrect, the right answer is {answer}.')

        # Display time taken to answer each problem
        elapsed_time = time.time() - start_time
        print(f'Time taken: {elapsed_time:.2f} seconds\n')

    # Display the final score
    print(f'Final score: {score}/{num_problems}')

# Call the function
play_game()
