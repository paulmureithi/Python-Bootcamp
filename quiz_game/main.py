from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    our_question = Question(question_text, question_answer)

    question_bank.append(our_question)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
else:
    print("You have completed the trivia.")
    print(f"Your total score was: {quiz.score}/{len(question_bank)}")

