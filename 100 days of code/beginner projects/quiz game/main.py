
# START TRIVIA GAME

from question_model import Question
from question_data import Data
from quiz_brain import QuizBrain


question_bank = []
for question in Data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("\n\nYou've completed the quiz")
print(f"Your final score was: {quiz.score} /{len(question_bank)}")


#quiz_brain.py
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        guess = input(f"Q.{self.question_number}: {current_question.text} (True / False)?: ")
        self.check_answer(guess, current_question.answer)

    def check_answer(self, guess, correct_answer):

        if guess.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")

        else:
            print("That's wrong. :(")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}\n\n")


