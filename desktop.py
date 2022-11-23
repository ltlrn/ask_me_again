from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow

from desktop_new import Ui_MainWindow
from data_transfer import DataTransfer
from main import Question, Answer, Game
from utils import clear_fields, answers_distribution, get_choices


class MyQ(Ui_MainWindow):
    def __init__(self, MainWindow):
        super().setupUi(MainWindow)

        self.quiz_list = []
        self.game = Game()  # экземпляр сеанса игры

        self.radio_box = [
            self.radioButton_1,
            self.radioButton_2,
            self.radioButton_3,
            self.radioButton_4,
            self.radioButton_5,
        ]

        self.indicators_box = [
            self.indicator_1,
            self.indicator_2,
            self.indicator_3,
            self.indicator_4,
            self.indicator_5,
        ]

        self.radio_box[0].setChecked(True)

        self.add_functions()

    def add_functions(self) -> None:
        self.main_button.clicked.connect(lambda: self.main_button_mechanism())

    def check_answer(self):
        rb = self.sender()
        if rb.isChecked():
            print(rb.text())

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

    def main_button_mechanism(self) -> None:
        """Механизм главной кнопки, собссно. Срабатывает при нажатии, часто по-разному,
        интуитивно понятен.
        """

        if self.game.WAITS and self.game.STAGE == "CHOOSE":
            if not self.quiz_list:
                self.forming_questions()

            self.game.WAITS = False

            if self.action_2.isChecked():
                self.game.RANDOM = True
            else:
                self.game.RANDOM = False

            self.game.counters_drop()

            self.correct.setText("0")
            self.errors.setText("0")

            clear_fields(self.answer_field, self.question_field)
            for indicator in self.indicators_box:
                indicator.setStyleSheet("background-color: rgb(202, 175, 255);")

            self.game.restart()
            self.game.next_question()

            self.total.setText(
                f"{self.game.counter_total} из {self.game.questions_count()}"
            )

            # may be reimplement it like Game class method...
            answers, corrects = answers_distribution(self.game.current_question.answers)
            self.game.current_question.corrects = corrects
            number = f"{self.game.current_question.number})."
            question = self.game.current_question.text

            self.question_field.setPlainText(f"{number} {question}")
            self.answer_field.setPlainText(answers)

            self.main_button.setText("Проверить...")  # may be func...
            self.game.STAGE = "CHECK"

        elif self.game.STAGE == "CHECK":

            choices = get_choices(
                self.radio_box
            )  # switch на количество правильных ответов

            if choices == self.game.current_question.corrects:
                for choice in choices:
                    indicator = self.indicators_box[choice - 1]
                    indicator.setStyleSheet("background-color: green;")

                    self.game.counter_corrects += 1
                    self.correct.setText(str(self.game.counter_corrects))

            else:
                for correct in self.game.current_question.corrects:
                    indicator = self.indicators_box[correct - 1]
                    indicator.setStyleSheet("background-color: green;")
                for choice in choices:
                    indicator = self.indicators_box[choice - 1]
                    indicator.setStyleSheet("background-color: red;")

                    self.game.counter_errors += 1
                    self.errors.setText(str(self.game.counter_errors))

            self.main_button.setText("...вперде!")
            self.game.STAGE = "CHOOSE"

        elif (not self.game.WAITS) and self.game.STAGE == "CHOOSE":
            clear_fields(self.answer_field, self.question_field)
            for indicator in self.indicators_box:
                indicator.setStyleSheet("background-color: rgb(202, 175, 255);")

            self.game.next_question()

            if self.game.current_question:

                self.total.setText(
                    f"{self.game.counter_total} из {self.game.questions_count()}"
                )

                answers, corrects = answers_distribution(
                    self.game.current_question.answers
                )
                self.game.current_question.corrects = corrects
                number = f"{self.game.current_question.number})."
                question = self.game.current_question.text

                self.question_field.setPlainText(f"{number} {question}")
                self.answer_field.setPlainText(answers)

                self.main_button.setText("Проверить...")
                self.game.STAGE = "CHECK"

            else:
                self.main_button.setText("СНОВА!")
                self.game.STAGE = "CHOOSE"
                self.game.WAITS = True


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QMainWindow()
    MyQ(MainWindow)

    MainWindow.show()
    sys.exit(app.exec())
