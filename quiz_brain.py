class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)


    def next_question(self):
        current_q = self.questions_list[self.question_number]
        self.question_number += 1
        q_answer = input(f"Q.{self.question_number}: {current_q.text}. (True/False)").lower()
        self.check_answer(q_answer, current_q.answer)

    def check_answer(self, q_answer, correct_answer):
        if q_answer.lower() == correct_answer.lower():
            print("You are correct")
            self.score +=1
        else:
            print("That's right")
        print(f"The correct answer was {correct_answer}")
        if self.question_number == len(self.questions_list) - 1:
            print("You've completed the quiz")
            print(f"Your final score is {self.score}/{self.question_number}")
        else:
            print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")

