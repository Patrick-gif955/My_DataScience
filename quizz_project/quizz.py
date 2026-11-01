import requests
from urllib.parse import unquote
import random

url = "https://opentdb.com/api.php?amount=5&category=9&difficulty=medium&type=multiple&encode=url3986"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    score = 0
    
    question_list = data["results"]
    for number, questions in enumerate (question_list, start=1):
        print(f"Question {number}: {unquote(questions["question"])}")
        correct_ans = unquote(questions["correct_answer"])
        answer_list = questions["incorrect_answers"]
        answer_list.append(correct_ans)
        decode_answers = []
        letters = ["A","B","C","D"]
        
        for item in answer_list:
            decode_answers.append(unquote(item))
        random.shuffle(decode_answers)
        for index,answer in enumerate(decode_answers):
            print(f"{letters[index]}. {answer}")
        while True:
            try:
                user_ans = input("Choose your answer (A, B, C, D): ").strip().upper()
                selected_ans = decode_answers[letters.index(user_ans)]
                if selected_ans == correct_ans:
                    score +=1
                    print("Correct!")
                else:
                    print(f"You got it wrong, the correct answer is {correct_ans}")
                break
            except ValueError:
                print(f"{user_ans} is not in the options")
    final_score = f"{score}/{len(question_list)}"
    print(f"Your score is {final_score}")    