from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow

from data_transfer import DataTransfer
from desktop_new import Ui_MainWindow
from main import Answer, Game, Question
from utils import Tools

# clear_fields, answers_distribution, get_choices


class MyQ(Ui_MainWindow, Tools):
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

    def main_button_mechanism(self) -> None:
        """Механизм главной кнопки, собссно. Срабатывает при нажатии, часто по-разному,
        интуитивно понятен.
        """

        if self.game.WAITS and self.game.STAGE == "CHOOSE":
            if not self.quiz_list:
                self.forming_questions()
           
            self.game.WAITS = False

            self.set_game_mode()           
            self.counters_to_null()
            self.fields_and_indicators_clear()
            self.game.restart()
            self.current_question_appearance()

            self.main_button.setText("Проверить...")
            self.game.STAGE = "CHECK"

        elif self.game.STAGE == "CHECK":
            choices = self.get_choices(
                self.radio_box
            )  # switch на количество правильных ответов

            if choices == self.game.current_question.corrects:
                self.user_answers_right(choices)

            else:
                self.user_answers_wrong(choices)
               
            self.main_button.setText("...вперёд!")
            self.game.STAGE = "CHOOSE"

        elif (not self.game.WAITS) and self.game.STAGE == "CHOOSE":
            self.fields_and_indicators_clear() 
            self.game.next_question()

            if self.game.current_question:
                self.current_question_appearance()
                
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
