from PyQt6 import QtCore, QtGui, QtWidgets
from data_transfer import db_create, db_insert, db_count, corrects


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(631, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.question_field = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.question_field.setGeometry(QtCore.QRect(50, 40, 521, 131))
        self.question_field.setObjectName("question_field")
        self.answers_field = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.answers_field.setGeometry(QtCore.QRect(50, 210, 521, 301))
        self.answers_field.setObjectName("answers_field")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 190, 51, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 10, 51, 20))
        self.label_2.setObjectName("label_2")
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(480, 530, 91, 31))
        self.save_button.setObjectName("save_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 631, 19))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_functions()

    def add_functions(self):
        self.save_button.clicked.connect(lambda: db_create())
        self.save_button.clicked.connect(lambda: self.parser())

    def parser(self):
        q_number = db_count()[0] + 1  # make it better!

        questions_list = []
        questions_list.append(((self.question_field.toPlainText()).rstrip(),))

        answers_list = []
        answers = self.answers_field.toPlainText()

        answers_list = answers.split("\n\n")

        question_id = [q_number] * len(answers_list)

        corr_status = [0] * len(answers_list)

        for i in corrects(answers_list):
            corr_status[i] = 1

        print("corrects: ", corr_status)

        answers_to_db = []

        for text, q_id, corr in zip(answers_list, question_id, corr_status):
            answers_to_db.append((text, q_id, corr))

        print(f"{q_number} question created...")

        db_insert(questions_list, answers_to_db)
        self.answers_field.clear()
        self.question_field.clear()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Question Adder"))
        self.question_field.setPlainText(
            _translate("MainWindow", "please, write your question here\n" "")
        )
        self.answers_field.setPlainText(
            _translate("MainWindow", "...and some answers - here")
        )
        self.label.setText(_translate("MainWindow", "answers"))
        self.label_2.setText(_translate("MainWindow", "question"))
        self.save_button.setText(_translate("MainWindow", "Save"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
