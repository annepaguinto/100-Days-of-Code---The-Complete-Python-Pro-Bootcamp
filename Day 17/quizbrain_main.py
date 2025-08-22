from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

import random

question_bank = []

for question in question_data:
    new_q = Question(question["question"], question["correct_answer"])
    question_bank.append(new_q)


quiz_item = QuizBrain(question_bank)

while quiz_item.still_has_questions():
    quiz_item.next_question()

print("You've completed the quiz.")
print(f"Your final score is {quiz_item.score} / {len(quiz_item.question_list)}")
