from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow

from data_transfer import DataTransfer

# from desktop_new import Ui_MainWindow
from dsk import Ui_MainWindow
from main import Answer, Game, Question
from utils import Tools


class MyQ(Ui_MainWindow, Tools):
    def __init__(self, MainWindow):
        super().setupUi(MainWindow)

        self.quiz_list = []
        self.game = Game()  # экземпляр сеанса игры

        self.declare_button_groups()
        self.frame_2.hide()

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

            self.check_or_radiobuttons_set()

            self.main_button.setText("Проверить...")
            self.game.STAGE = "CHECK"

        elif self.game.STAGE == "CHECK":
            choices = self.get_choices()  # switch на количество правильных ответов

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

                self.check_or_radiobuttons_set()

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
