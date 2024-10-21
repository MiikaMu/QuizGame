import json

def load_questions(file_path):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            return data["questions"]
    except FileNotFoundError:
        print("No file found")
        return []

def ask_questions(questions):
    score = 0

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
            questions = load_questions("questions.json")
            score, total = ask_questions(questions)
            print(f"You got {score}/{total} correct!\n")
        else:
            print("Sad, goodbye")
            break

#start
quiz_game()