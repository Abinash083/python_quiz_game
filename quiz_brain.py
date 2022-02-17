class QuizBrain:

    def __init__(self, list):
        self.qn = 0
        self.qn_list = list
        self.score = 0

    def next_question(self):
        current_question = self.qn_list[self.qn]
        self.qn += 1
        user_answer = input(f"\nQ.N{self.qn} {current_question.question} (True/False)")
        self.check_answer(user_answer, current_question.answer)
        print(f"Current Score : {self.score}/{self.qn}")

    def still_has_questions(self):
        return self.qn < len(self.qn_list)

    def check_answer(self, user_answer, answer):
        if user_answer.lower() == answer.lower():
            print("You, got it right")
            self.score += 1
        else:
            print(f"Wrong Answer! Answer is {answer}")

