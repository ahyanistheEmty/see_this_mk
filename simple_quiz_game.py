def run_quiz():
    questions = {
        "What is the capital of France?": "Paris",
        "What is the largest planet in our solar system?": "Jupiter",
        "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
        "What is the chemical symbol for gold?": "Au",
        "Which ocean is the largest?": "Pacific"
    }
    
    score = 0
    print("Welcome to the Simple Quiz Game!")
    print("-------------------------------")
    
    for question, answer in questions.items():
        user_answer = input(f"{question} ")
        if user_answer.strip().lower() == answer.lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {answer}.\n")
            
    print(f"Quiz Complete! Your final score is {score}/{len(questions)}.")

if __name__ == "__main__":
    run_quiz()
