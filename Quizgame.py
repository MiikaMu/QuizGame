def ask_questions():
    score = 0

    questions = [
        {"question": "What year Finland won its first gold in ice hockey world championship", "answer": "1995"},
        {"question": "What is the chemical symbol for water?", "answer": "H2O"},
        {"question": "What year did the Titanic sink?", "answer": "1912"},
        {"question": "What is the capital of France?", "answer": "Paris"}
    ]

    for q in questions:
        print(q["question"])
        answer = input("Answer: ")

        if answer.lower() == q["answer"].lower():
            print("Correct!!\n")
            score +=1
        else:
            print("Wrong :(\n")

    return score, len(questions)

def quiz_game():
    while True:
        start = input("Start Quiz Game? (yes/no) ")

        if start == "yes":
            print("Game starting..\n")
            score, total = ask_questions()
            print(f"You got {score}/{total} correct!\n")
        else:
            print("Sad, goodbye")
            break

#start
quiz_game()