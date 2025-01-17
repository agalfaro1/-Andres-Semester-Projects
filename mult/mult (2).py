import random
import time

def ask_question():
    """Ask a multiplication question and check the user's answer."""
    num1 = random.randint(1, 12)
    num2 = random.randint(1, 12)
    correct_answer = num1 * num2

    # Ask the question
    start_time = time.time()  # Start the timer
    user_answer = int(input(f"What is {num1} x {num2}? "))
    end_time = time.time()  # End the timer

    # Calculate time taken for the question
    time_taken = end_time - start_time

    # Check if the answer is correct
    correct = user_answer == correct_answer
    return correct, time_taken

def main():
    print("Welcome to the multiplication quiz!")

    # Ask the user if they want a set number of questions or endless mode
    mode = input("Choose a mode:\n1. Set number of questions\n2. Endless mode\n> ")

    if mode == '1':
        num_questions = int(input("How many questions would you like to answer? "))
        total_score = 0
        total_time = 0

        for i in range(num_questions):
            print(f"\nQuestion {i + 1}:")
            correct, time_taken = ask_question()
            if correct:
                print(f"Correct! Time taken: {time_taken:.2f} seconds.")
                total_score += 1
                total_time += time_taken
            else:
                print(f"Incorrect. Time taken: {time_taken:.2f} seconds.")

        # Calculate and display final score and time
        print(f"\nQuiz complete! Your score: {total_score}/{num_questions}")
        if total_score > 0:
            average_time = total_time / total_score
            print(f"Your average response time for correct answers: {average_time:.2f} seconds.")
        else:
            print("You didn't get any questions correct.")

    elif mode == '2':
        total_score = 0
        total_time = 0
        question_count = 1

        print("Endless mode started! Press 'Ctrl+C' to quit.")
        while True:
            print(f"\nQuestion {question_count}:")
            correct, time_taken = ask_question()
            if correct:
                print(f"Correct! Time taken: {time_taken:.2f} seconds.")
                total_score += 1
                total_time += time_taken
            else:
                print(f"Incorrect. Time taken: {time_taken:.2f} seconds.")

            question_count += 1

    else:
        print("Invalid mode selected. Exiting the program.")

if __name__ == "__main__":
    main()
