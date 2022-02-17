class QuizBrain:

    def __init__(self, list):
        self.qn = 0
        self.qn_list = list

    def next_question(self):
        current_question = self.qn_list[self.qn]
        self.qn += 1
        input(f"\nQ.N{self.qn} {current_question.question} (True/False)")

    def still_has_questions(self):
        return self.qn < len(self.qn_list)
