from PyQt6 import QtCore, QtGui, QtWidgets

from data_transfer import db_read
from main import Question, Answer, Game
from utils import clear_fields, answers_distribution, get_choices


class Ui_MainWindow(object):
    def __init__(self):
        super().__init__()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.question_field = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.question_field.setGeometry(QtCore.QRect(170, 29, 611, 141))
        self.question_field.setObjectName("question_field")
        self.answer_field = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.answer_field.setGeometry(QtCore.QRect(250, 220, 531, 321))
        self.answer_field.setObjectName("answer_field")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 6, 71, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(260, 195, 151, 21))
        self.label_2.setObjectName("label_2")
        self.radioButton_1 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_1.setGeometry(QtCore.QRect(170, 210, 41, 31))
        self.radioButton_1.setMaximumSize(QtCore.QSize(61, 31))
        self.radioButton_1.setChecked(True)
        self.radioButton_1.setObjectName("radioButton_1")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(170, 260, 41, 21))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(170, 310, 41, 20))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(170, 360, 41, 20))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_5.setGeometry(QtCore.QRect(170, 410, 41, 20))
        self.radioButton_5.setObjectName("radioButton_5")
        self.main_button = QtWidgets.QPushButton(self.centralwidget)
        self.main_button.setGeometry(QtCore.QRect(20, 490, 211, 51))
        self.main_button.setObjectName("main_button")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 460, 171, 16))
        self.label_3.setObjectName("label_3")
        self.total = QtWidgets.QLineEdit(self.centralwidget)
        self.total.setGeometry(QtCore.QRect(40, 30, 81, 22))
        self.total.setObjectName("total")
        self.correct = QtWidgets.QLineEdit(self.centralwidget)
        self.correct.setGeometry(QtCore.QRect(40, 90, 51, 22))
        self.correct.setObjectName("correct")
        self.errors = QtWidgets.QLineEdit(self.centralwidget)
        self.errors.setGeometry(QtCore.QRect(40, 150, 51, 22))
        self.errors.setObjectName("errors")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 5, 111, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 70, 61, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 130, 61, 16))
        self.label_6.setObjectName("label_6")
        self.indicator_1 = QtWidgets.QLabel(self.centralwidget)
        self.indicator_1.setGeometry(QtCore.QRect(60, 215, 101, 21))
        self.indicator_1.setStyleSheet("background-color: rgb(202, 175, 255);")
        self.indicator_1.setText("")
        self.indicator_1.setObjectName("indicator_1")
        self.indicator_2 = QtWidgets.QLabel(self.centralwidget)
        self.indicator_2.setGeometry(QtCore.QRect(60, 260, 101, 21))
        self.indicator_2.setStyleSheet("background-color: rgb(202, 175, 255);")
        self.indicator_2.setText("")
        self.indicator_2.setObjectName("indicator_2")
        self.indicator_3 = QtWidgets.QLabel(self.centralwidget)
        self.indicator_3.setGeometry(QtCore.QRect(60, 310, 101, 21))
        self.indicator_3.setStyleSheet("background-color: rgb(202, 175, 255);")
        self.indicator_3.setText("")
        self.indicator_3.setObjectName("indicator_3")
        self.indicator_5 = QtWidgets.QLabel(self.centralwidget)
        self.indicator_5.setGeometry(QtCore.QRect(60, 410, 101, 21))
        self.indicator_5.setStyleSheet("background-color: rgb(202, 175, 255);")
        self.indicator_5.setText("")
        self.indicator_5.setObjectName("indicator_5")
        self.indicator_4 = QtWidgets.QLabel(self.centralwidget)
        self.indicator_4.setGeometry(QtCore.QRect(60, 360, 101, 21))
        self.indicator_4.setStyleSheet("background-color: rgb(202, 175, 255);")
        self.indicator_4.setText("")
        self.indicator_4.setObjectName("indicator_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 19))
        self.menubar.setDefaultUp(False)
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menu)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_2 = QtGui.QAction(MainWindow)
        self.action_2.setCheckable(True)
        self.action_2.setChecked(True)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtGui.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.menu_2.addAction(self.action_2)
        self.menu.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

# my code below

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

    def forming_questions(self) -> None:
        """Adds to self.quiz_list Question and Answer class
        instances with data returned by db_read function.
        """

        question_sets, answer_sets = db_read()

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
           
            self.game.RANDOM = self.action_2.isChecked()
          

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

            self.main_button.setText("...вперёд!")
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ask Me Again"))
        self.label.setText(_translate("MainWindow", "вопрос"))
        self.label_2.setText(_translate("MainWindow", "варианты ответов"))
        self.radioButton_1.setText(_translate("MainWindow", "1"))
        self.radioButton_2.setText(_translate("MainWindow", "2"))
        self.radioButton_3.setText(_translate("MainWindow", "3"))
        self.radioButton_4.setText(_translate("MainWindow", "4"))
        self.radioButton_5.setText(_translate("MainWindow", "5"))
        self.main_button.setText(_translate("MainWindow", "ЖМИ!"))
        self.label_3.setText(_translate("MainWindow", "самая главная кнопка"))
        self.total.setText(_translate("MainWindow", "0 из 0"))
        self.correct.setText(_translate("MainWindow", "0"))
        self.errors.setText(_translate("MainWindow", "0"))
        self.label_4.setText(_translate("MainWindow", "всего вопросов"))
        self.label_5.setText(_translate("MainWindow", "верно"))
        self.label_6.setText(_translate("MainWindow", "неверно"))
        self.menu.setTitle(_translate("MainWindow", "опции"))
        self.menu_2.setTitle(_translate("MainWindow", "порядок"))
        self.action_2.setText(_translate("MainWindow", "случайный"))
        self.action_3.setText(_translate("MainWindow", "прямой"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
