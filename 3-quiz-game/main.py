
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
# Make a list of questions in a format we can work with (not raw data)
for item in question_data:
    q_text = item["question"]
    q_answer = item["correct_answer"]
    new_q = Question(q_text, q_answer)
    question_bank.append(new_q)

# Add all the questions to the QuizBrain class
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")