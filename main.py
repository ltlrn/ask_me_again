import random


class Question:
    """Describes question object with"""

    def __init__(self, question_set): # *answers
        self.number = question_set[0]
        self.text = question_set[1]  # may it be a dict, enumerate one
        self.answers = []

    def randomize_answers(self):
        """Shaffle the answers."""
        pass


class Answer:
    """
    A single answer for the current question,
    may be correct sometimes...
    """

    def __init__(self, answer_set): # optimize sql querys!
        self.text = answer_set[1]
        self.question_id = answer_set[2]
        self.correct = answer_set[3]

    def is_correct(self) -> bool:
        """Returns answer status."""
        return self.correct


class Game:
    """Класс сеанса игры. Содержит методы управления, поля с вопросами 
    и счетчиками, флаги состояния, генератор."""
    def __init__(self):
        self.WAITS = True

        self.quiz_list = []
        self.generator = None
        self.current_question = None

    def restart(self, order='random'):
        self.generator = (question for question in self.quiz_list)

    def change_variant(self):
        pass

    def next_question(self):
        try:
            self.current_question = self.generator.__next__()
        except StopIteration:
            pass # some sort of game ending
