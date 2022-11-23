import sqlite3


class DataTransfer:
    @classmethod
    def create(self):
        """Create simple db of two related tables,
        if it not already exists in current directory.
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
    def insert(self, questions_list, answers_list):

        connect = sqlite3.connect("db.sqlite")
        cursor = connect.cursor()

        cursor.executemany("INSERT INTO questions VALUES(NULL, ?);", questions_list)

        cursor.executemany("INSERT INTO answers VALUES(NULL, ?, ?, ?);", answers_list)

        connect.commit()
        connect.close()

    @classmethod
    def read(self):
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
            SELECT *
            FROM answers;
            """
        )

        for element in cursor:
            answers.append(element)

        connect.close()

        return questions, answers

    @classmethod
    def count(self):
        """Counts records in db to know the number of next
        adding question.
        """
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
    def corrects(self, answers_list):
        """Returns the list of indexes of correct answers
        to construct a record in db later. Also strips 'CORRECT'
        marker from the answer.
        """
        correct_indexes = []

        for answer in answers_list:
            if answer.endswith("CORRECT"):
                index = answers_list.index(answer)
                correct_indexes.append(index)
                answers_list[index] = answer.rstrip("CORRECT")

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
