def validate_card(card_number):
    """ Проверяет, является ли номер карты 4 группами цифр через пробелы """
    card_segments = card_number.split(" ")
    if len(card_segments) != 4:
        return "Номер карты недопустимый"
    for segment in card_segments:
        if len(segment) != 4:
            return "Номер карты недопустимый"
        if not segment.isdigit():
            return "Номер карты недопустимый"
    return "Номер карты допустимый"
