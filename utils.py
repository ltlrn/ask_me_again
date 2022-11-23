import random


class Tools:
    @staticmethod
    def randomize(some_list):
        new_list = random.sample(some_list, len(some_list))
        return new_list

    def clear_fields(self, *fields) -> None:
        """Clear some fields."""
        for field in fields:
            field.clear()

    def answers_distribution(self, answers_list: list) -> str:

        strings = []
        corrects = []

        answers_list = self.randomize(answers_list)

        for number, answer in enumerate(answers_list, start=1):
            string = f"{number}). {answer.text}"
            strings.append(string.rstrip())
            if answer.is_correct():
                corrects.append(number)

        output = ("\n\n".join(strings), corrects)

        return output

    def get_choices(self, button_box):
        """Принимает на вход набор радиокнопок или флажков.
        Возвращает номера активированных кнопок из набора."""
        choices = []

        for button in button_box:
            if button.isChecked():
                choices.append(int(button.text()))

        return choices
