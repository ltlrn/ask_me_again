from random import sample

from data_transfer import DataTransfer
from main import Answer, Question


class Tools:
    def declare_button_groups(self):
        """ "Группирует два набора радиокнопок и индикаторов
        для удобства итерирования по ним."""
        self.frames = [
            self.frame,            
            self.frame_2,
            self.frame_3,
            self.frame_4,
            self.frame_5,
        ]

        self.radio_box_1 = [
            self.radioButton_1,
            self.radioButton_2,
            self.radioButton_3,
            self.radioButton_4,
            self.radioButton_5,
        ]

        self.check_box_1 = [
            self.checkBox,
            self.checkBox_2,
            self.checkBox_3,
            self.checkBox_4,
            self.checkBox_5,
        ]

        self.indicators_box_1 = [
            self.indicator_1,
            self.indicator_2,
            self.indicator_3,
            self.indicator_4,
            self.indicator_5,
        ]

        self.check_indicators_box_1 = [
            self.indicator_6,
            self.indicator_7,
            self.indicator_8,
            self.indicator_9,
            self.indicator_10,
        ]

        self.radio_box_2 = [
            self.radioButton_7,
            self.radioButton_8,
            self.radioButton_9,
            self.radioButton_10,
        ]

        self.indicators_box_2 = [
            self.indicator_11,
            self.indicator_12,
            self.indicator_13,
            self.indicator_14,
        ]

        self.check_box_2 = [
            self.checkBox_6,
            self.checkBox_7,
            self.checkBox_8,
            self.checkBox_9,
        ]

        self.check_indicators_box_2 = [
            self.indicator_15,
            self.indicator_16,
            self.indicator_17,
            self.indicator_18,
        ]

        self.check_box_3 = [
            self.checkBox_10,
            self.checkBox_11,
            self.checkBox_12,
            self.checkBox_13,
            self.checkBox_14,
            self.checkBox_15,
            self.checkBox_16,
            self.checkBox_17,
        ]

        self.check_indicators_box_3 = [
            self.indicator_19,
            self.indicator_20,
            self.indicator_21,
            self.indicator_22,
            self.indicator_23,
            self.indicator_24,
            self.indicator_25,
            self.indicator_26,
        ]


    def clear_fields(self, *fields) -> None:
        """Очищает поля вопроса и ответа."""
        for field in fields:
            field.clear()

    def answers_distribution(self, answers_list: list) -> tuple:
        """Принимает список объектов Answer вопроса. Возвращает кортеж из
        строки, содержащей пронумерованные варианты ответа для текущего вопроса,
        расположенные в случайном порядке, для размещения в поле ответов и списка
        номеров правильных ответов."""
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

    def get_choices(self):
        """Принимает на вход набор радиокнопок или флажков.
        Возвращает номера активированных кнопок из набора."""
        # if len(self.game.current_question.corrects) > 1:
        #     button_box = self.check_box
        # else:
        #     button_box = self.radio_box
        
        try:
            button_box = self.game.current_question.buttons
        except AttributeError:
            print(self.game.current_question.number)
        
        choices = []

        for button in button_box:
            if button.isChecked():
                choices.append(int(button.text()))

        return choices

    def forming_questions(self) -> None:
        """Добавляет в список self.quiz_list экземплры Question и Answer,
        полученные из БД.
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

    def counters_to_null(self) -> None:
        """Сбрасывает все счетчики."""
        self.game.counters_drop()
        self.correct.setText("0")
        self.errors.setText("0")

    def fields_and_indicators_clear(self) -> None:
        """Очищает поля и сбрасывает индикаторы."""
        self.clear_fields(self.answer_field, self.question_field)

        for indicator in self.game.current_question.indicators:
            indicator.setStyleSheet("background-color: rgb(202, 175, 255);")

        # for indicator in self.check_indicators_box:
        #     indicator.setStyleSheet("background-color: rgb(202, 175, 255);")

        for flag in self.game.current_question.buttons:
            flag.setChecked(False)

    def current_question_appearance(self) -> None:
        """Распределение элементов текущего вопроса по виджетам интерфейса.
        Установка списка номеров правильных ответов в поле corrects текущего
        вопроса."""
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

    def user_answers_right(self, choices) -> None:
        """Вызывается при проверке текущего вопроса, если пользователь
        ответил правильно. Меняет цвет индикатора, соответствующего
        ответу(-ам), на зелёный, увеличивает соответствующий счетчик."""
        # indicators = self.indicators_box

        # if len(self.game.current_question.corrects) > 1:
        #     indicators = self.check_indicators_box


        indicators = self.game.current_question.indicators

        for choice in choices:
            indicator = indicators[choice - 1]
            indicator.setStyleSheet("background-color: green;")

        self.game.counter_corrects += 1
        self.correct.setText(str(self.game.counter_corrects))

    def user_answers_wrong(self, choices) -> None:
        """Вызывается при проверке текущего вопроса, если пользователь
        ошибся. Меняет цвет индикатора, соответствующего ответу(-ам),
        на красный, а соответствующего верному варианту - на зеленый;
        увеличивает соответствующий счетчик."""

        indicators = self.game.current_question.indicators
        print(len(indicators))

        # if len(self.game.current_question.corrects) > 1:
        #     indicators = self.check_indicators_box
        if choices:
            for choice in choices:
                indicator = indicators[choice - 1]
                indicator.setStyleSheet("background-color: red;")
        else:
            print('no choices') # remove
        print(self.game.current_question.corrects)
        for correct in self.game.current_question.corrects:
            indicator = indicators[correct - 1]
            indicator.setStyleSheet("background-color: green;")

        self.game.counter_errors += 1
        self.errors.setText(str(self.game.counter_errors))

    def set_game_mode(self) -> None:
        """Устанавливает порядок вопросов в игре: прямой или случайный."""
        if self.action_2.isChecked():
            self.game.RANDOM = True
        else:
            self.game.RANDOM = False

    def buttons_show(self, number):
        
        for frame in self.frames:
            frame.hide()

        self.frames[number].show()


    def check_or_radiobuttons_set(self) -> None:
        """В зависимости от количества верных вариантов ответов
        в текущем вопросе скрывает набор радиокнопок и показывает
        набор флажков - или наоборот."""

        if len(self.game.current_question.corrects) > 1:
            if len(self.game.current_question.answers) == 4:
                self.buttons_show(3)
                self.game.current_question.buttons = self.check_box_2 
                self.game.current_question.indicators = self.check_indicators_box_2

            elif len(self.game.current_question.answers) == 5:
                self.buttons_show(1)
                self.game.current_question.buttons = self.check_box_1
                self.game.current_question.indicators = self.check_indicators_box_1
            else:
                self.buttons_show(4)
                self.game.current_question.buttons = self.check_box_3 
                self.game.current_question.indicators = self.check_indicators_box_3

        elif len(self.game.current_question.corrects) == 1:            
            if len(self.game.current_question.answers) == 4:
                self.buttons_show(2)
                self.game.current_question.buttons = self.radio_box_2
                self.game.current_question.indicators = self.indicators_box_2
            elif len(self.game.current_question.answers) == 5:
                self.buttons_show(0)
                self.game.current_question.buttons = self.radio_box_1
                self.game.current_question.indicators = self.indicators_box_1
        # when corrects are strange, refactor it
        else:
            self.buttons_show(0)
            self.game.current_question.buttons = self.radio_box_1
            self.game.current_question.indicators = self.indicators_box_1

            