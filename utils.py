import random


def clear_fields(*fields):
    for field in fields:
        field.clear()


def randomize(some_list):
    new_list = random.sample(some_list, len(some_list))
    return new_list


def answers_distribution(answers_list: list) -> str:

    strings = []
    corrects = []

    answers_list = randomize(answers_list)

    for number, answer in enumerate(answers_list, start=1):
        string = f"{number}). {answer.text}"
        strings.append(string.rstrip())
        if answer.is_correct():
            corrects.append(number)

    output = ("\n\n".join(strings), corrects)

    return output


def get_choices(button_box):
    """Принимает на вход набор радиокнопок или флажков.
    Возвращает номера активированных кнопок из набора."""
    choices = []

    for button in button_box:
        if button.isChecked():
            choices.append(int(button.text()))

    return choices
