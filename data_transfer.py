import sqlite3


class DataTransfer:
    @classmethod
    def create(cls):
        """Создаёт базу данных из двух таблиц, если
        не находит уже существующую.
        """

        connect = sqlite3.connect("db.sqlite")
        cursor = connect.cursor()
        print("Preparing db...")
        cursor.executescript(
            """
            CREATE TABLE IF NOT EXISTS questions(
                id INTEGER PRIMARY KEY,
                question_text TEXT NOT NULL
            ); 
    
            CREATE TABLE IF NOT EXISTS answers(
                id INTEGER PRIMARY KEY,
                answer_text TEXT NOT NULL,
                question_id INTEGER NOT NULL,
                correct BOOL NOT NULL,
                FOREIGN KEY(question_id) REFERENCES questions(id)
            );
        """
        )

        connect.commit()
        connect.close()

    @classmethod
    def insert(cls, questions_list, answers_list):
        """Добавляет данные в соответствующие таблицы."""

        connect = sqlite3.connect("db.sqlite")
        cursor = connect.cursor()

        cursor.executemany("INSERT INTO questions VALUES(NULL, ?);", questions_list)

        cursor.executemany("INSERT INTO answers VALUES(NULL, ?, ?, ?);", answers_list)

        connect.commit()
        connect.close()

    @classmethod
    def read(cls):
        """Читает все данные из таблиц Question и Answer."""

        connect = sqlite3.connect("db.sqlite")
        cursor = connect.cursor()

        questions = []
        answers = []

        cursor.execute(
            """
            SELECT *
            FROM questions;
            """
        )

        for element in cursor:
            questions.append(element)

        cursor.execute(
            """
            SELECT answer_text, question_id, correct
            FROM answers;
            """
        )

        for element in cursor:
            answers.append(element)

        connect.close()

        return questions, answers

    @classmethod
    def count(cls):
        """Считает количество записей в таблице Questions."""

        connect = sqlite3.connect("db.sqlite")
        cursor = connect.cursor()

        cursor.execute(
            """
            SELECT COUNT(id)
            FROM questions;
        """
        )
        res = []
        for el in cursor:
            res.append(el)

        connect.close()

        return res[0]

    @classmethod
    def corrects(cls, answers_list):
        """Возвращает список индексов правильных ответов,
        чтобы в дальнейшем сформировать запись в БД. Также
        убирает маркер 'CORRECT' из текста ответа.

        Returns the list of indexes of correct answers
        to construct a record in db later. Also strips 'CORRECT'
        marker from the answer.
        """
        correct_indexes = []

        for answer in answers_list:
            index = answers_list.index(answer)
            answers_list[index] = answer[3:]

            if answer.endswith("CORRECT"):
                correct_indexes.append(index)
                answers_list[index] = answer[3:].rstrip("CORRECT")

        return correct_indexes

    # The amount of labels and radiobuttons in the GUI correlates
    # with the number of answers in every question, please don`t forget!


if __name__ == "__main__":

    test_answers = [
        ("the first answer", 1, 1),
        ("the second answer", 1, 2),
        ("the third answer", 0, 1),
        ("the fourth question", 0, 2),
    ]

    test_questions = [
        ("the first question",),
        ("the second question",),
    ]

    DataTransfer.create()
    print(DataTransfer.read())
