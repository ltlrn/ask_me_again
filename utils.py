from random import sample

from data_transfer import DataTransfer
from main import Answer, Question


class Tools:
    def clear_fields(self, *fields) -> None:
        """Clear some fields."""
        for field in fields:
            field.clear()

    def answers_distribution(self, answers_list: list) -> str:

        strings = []
        corrects = []

        answers_list = sample(answers_list, len(answers_list))

        for number, answer in enumerate(answers_list, start=1):
            string = f"{number}). {answer.text}"
            strings.append(string.rstrip())
            if answer.is_correct():
                corrects.append(number)

        output = ("\n\n".join(strings), corrects)

        return output

    def get_choices(self, button_box):
        """Принимает на вход набор радиокнопок или флажков.
        Возвращает номера активированных кнопок из набора."""
        choices = []

        for button in button_box:
            if button.isChecked():
                choices.append(int(button.text()))

        return choices

    def forming_questions(self) -> None:
        """Adds to self.quiz_list Question and Answer class
        instances with data returned by db_read function.
        """

        question_sets, answer_sets = DataTransfer.read()

        # answers may be sorted by question_id

        answers_list = []

        for question_set in question_sets:
            self.quiz_list.append(Question(question_set))

        for answer_set in answer_sets:
            answers_list.append(Answer(answer_set))

        for question in self.quiz_list:
            for answer in answers_list:
                if question.number == answer.question_id:
                    question.answers.append(answer)

        self.game.quiz_list = (
            self.quiz_list
        )  # may be some sort of deep copy would match better
