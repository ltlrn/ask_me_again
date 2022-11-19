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
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.question_field = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.question_field.setGeometry(QtCore.QRect(40, 50, 731, 201))
        self.question_field.setObjectName("question_field")
        self.answer_field = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.answer_field.setGeometry(QtCore.QRect(300, 280, 471, 261))
        self.answer_field.setObjectName("answer_field")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 21, 61, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(310, 260, 121, 16))
        self.label_2.setObjectName("label_2")
        self.radioButton_1 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_1.setGeometry(QtCore.QRect(230, 290, 41, 20))
        self.radioButton_1.setObjectName("radioButton_1")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(230, 330, 41, 21))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(230, 370, 41, 20))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(230, 410, 41, 20))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_5.setGeometry(QtCore.QRect(230, 450, 41, 20))
        self.radioButton_5.setObjectName("radioButton_5")
        self.main_button = QtWidgets.QPushButton(self.centralwidget)
        self.main_button.setGeometry(QtCore.QRect(40, 490, 221, 51))
        self.main_button.setObjectName("main_button")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 470, 151, 16))
        self.label_3.setObjectName("label_3")
        self.total = QtWidgets.QLineEdit(self.centralwidget)
        self.total.setGeometry(QtCore.QRect(40, 300, 51, 22))
        self.total.setObjectName("total")
        self.correct = QtWidgets.QLineEdit(self.centralwidget)
        self.correct.setGeometry(QtCore.QRect(40, 360, 31, 22))
        self.correct.setObjectName("correct")
        self.errors = QtWidgets.QLineEdit(self.centralwidget)
        self.errors.setGeometry(QtCore.QRect(40, 420, 31, 22))
        self.errors.setObjectName("errors")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 280, 91, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 340, 57, 14))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 400, 57, 14))
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 19))
        self.menubar.setDefaultUp(False)
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.quiz_list = []
        self.game = Game()  # экземпляр сеанса игры

        self.radio_box = [
            self.radioButton_1,
            self.radioButton_2,
            self.radioButton_3,
            self.radioButton_4,
            self.radioButton_5,
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

            clear_fields(self.answer_field, self.question_field)

            self.game.restart()
            self.game.next_question()

            # may be reimplement it like Game class method...
            answers, corrects = answers_distribution(self.game.current_question.answers)
            self.game.current_question.corrects = corrects

            self.question_field.setPlainText(self.game.current_question.text)
            self.answer_field.setPlainText(answers)

            self.main_button.setText("Проверить...")  # may be func...
            self.game.STAGE = "CHECK"  #

        elif self.game.STAGE == "CHECK":

            choices = get_choices(
                self.radio_box
            )  # switch на количество правильных ответов

            print("choices:", choices)
            print("corrects:", self.game.current_question.corrects)

            # if corrects is [] - index error!

            if choices == self.game.current_question.corrects:
                print("CORRECT")
            else:
                print(f"Errror!, correct is {self.game.current_question.corrects[0]}")

            self.main_button.setText("...вперде!")
            self.game.STAGE = "CHOOSE"

        elif (not self.game.WAITS) and self.game.STAGE == "CHOOSE":
            clear_fields(self.answer_field, self.question_field)

            self.game.next_question()

            answers, corrects = answers_distribution(self.game.current_question.answers)
            self.game.current_question.corrects = corrects

            if self.game.current_question:
                self.question_field.setPlainText(self.game.current_question.text)
                self.answer_field.setPlainText(answers)

                self.main_button.setText("Проверить...")
                self.game.STAGE = "CHECK"

            else:
                self.main_button.setText("СНОВА!")
                self.game.STAGE = "CHOOSE"

    # def quiz_mapping(self, quiz_list: list, order: str = "random"):
    #     if order == "random":
    #         pass

    def test_read(self):
        for q in self.quiz_list:
            print(q.text, q.answers[0].text)

        # q, a = db_read()

        # print(q)
        # print('+'* 50)
        # print(a)

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


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
