from validators.validate_pin import validate_pin

from validators.validate_name import validate_card

print("Введите ваш номер карты")
card_number = input()
print(validate_card(card_number))
print("Введите ваш пин-код")
card_pin = input()
print(validate_pin(card_pin))
