def validate_pin(card_pin):
    """ проверяет является ли пин код последовательностью 4 цифр """
    if not card_pin.isdigit():
        return "Пин код недопустимый"
    if len(card_pin) != 4:
        return "Пин код недопустимый"
    return "Пин код допустимый"

