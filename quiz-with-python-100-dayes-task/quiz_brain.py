class QuizBrain:


    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.choice = ''
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        self.choice = input(f"Q.{self.question_number}:{current_question.text}:  ")
        self.check_answer()



    def still_has_question(self):
        if(self.question_number >= len(self.question_list)):
            return False
        else:
            return True

    def check_answer(self):
        if(self.choice == self.question_list[self.question_number - 1].answer):
            print("Good, U got it, Correct answer")
            self.score += 1
        else:
            print(f"Its Worng answer, correct answer is {self.question_list[self.question_number-1].answer}")