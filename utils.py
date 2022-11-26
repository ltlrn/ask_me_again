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

    # main button mechanism elements:

    def counters_to_null(self):
        self.game.counters_drop()
        self.correct.setText("0")
        self.errors.setText("0")

    def fields_and_indicators_clear(self):
        self.clear_fields(self.answer_field, self.question_field)

        for indicator in self.indicators_box:
            indicator.setStyleSheet("background-color: rgb(202, 175, 255);")

    def current_question_appearance(self):
        self.total.setText(
            f"{self.game.counter_total} из {self.game.questions_count()}"
        )

        answers, corrects = self.answers_distribution(
            self.game.current_question.answers
        )

        self.game.current_question.corrects = corrects
        number = f"{self.game.current_question.number})."
        question = self.game.current_question.text
        self.question_field.setPlainText(f"{number} {question}")
        self.answer_field.setPlainText(answers)
    
    def user_answers_right(self, choices):
        for choice in choices:
            indicator = self.indicators_box[choice - 1]
            indicator.setStyleSheet("background-color: green;")
            self.game.counter_corrects += 1
            self.correct.setText(str(self.game.counter_corrects))

    def user_answers_wrong(self, choices):
        for correct in self.game.current_question.corrects:
            indicator = self.indicators_box[correct - 1]
            indicator.setStyleSheet("background-color: green;")
            
        for choice in choices:
            indicator = self.indicators_box[choice - 1]
            indicator.setStyleSheet("background-color: red;")
            self.game.counter_errors += 1
            self.errors.setText(str(self.game.counter_errors))

    def set_game_mode(self):
        if self.action_2.isChecked():
            self.game.RANDOM = True
        else:
            self.game.RANDOM = False