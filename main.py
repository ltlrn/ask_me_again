from utils import randomize


class Question:
    """Описывает объект Вопроса, содержит номер вопроса,
    его текст и варианты ответов.
    """

    def __init__(self, question_set):
        self.number: int = question_set[0]
        self.text: str = question_set[1]
        self.answers: list = []


class Answer:
    """
    Описывает объект Ответа, который имеет поля текста,
    номера вопроса, к которому относитя, значения истинности.
    """

    def __init__(self, answer_set):
        self.text: str = answer_set[1]
        self.question_id: int = answer_set[2]
        self.correct: bool = bool(answer_set[3])

    def is_correct(self) -> bool:
        """Возвращает, верен ответ или нет."""
        return self.correct


class Game:
    """Класс сеанса игры. Содержит методы управления, поля с вопросами
    и счетчиками, флаги состояния, генератор."""

    def __init__(self):

        # флаги:

        self.WAITS: bool = True
        self.RANDOM: bool = True
        self.STAGE: str = "CHOOSE"

        # счётчики:

        self.counter_total: int = 0
        self.counter_corrects: int = 0
        self.counter_errors: int = 0

        # доступ к вопросам:

        self.quiz_list: list = []
        self.generator = None
        self.current_question = None

    def restart(self) -> None:
        """Пререзагружает игру, может менять последовательность
        вывода вопросов.
        """
        if self.RANDOM:
            self.generator = (question for question in randomize(self.quiz_list))
        else:
            self.generator = (question for question in self.quiz_list)

    def next_question(self) -> None:
        """Переход к следующем вопросу."""
        try:
            self.current_question = self.generator.__next__()
            self.counter_total += 1
        except StopIteration:
            self.current_question = None
            self.WAITS = True  # не очевидно, меняется в двух местах

    def counters_drop(self) -> None:
        """Сброс счётчиков."""

        self.counter_total = 0
        self.counter_corrects = 0
        self.counter_errors = 0

    def questions_count(self) -> int:
        """Возвращает количество вопросов в текущем варианте игры."""
        return len(self.quiz_list)

    def change_variant(self) -> None:
        pass
