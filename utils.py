def clear_fields(*fields):
    for field in fields:
        field.clear()


def answers_destribution(answers_list: list) -> str:
        
    strings = []
    
    # randomize answers list
    for number, answer in enumerate(answers_list, start=1):
        string  = f'{number}). {answer.text}'
        strings.append(string)

    output = "\n\n".join(strings)

    return output   