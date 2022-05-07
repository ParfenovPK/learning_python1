import json
from basic_word import BasicWord

PATH = "words.json"


def load_data(path=PATH):
    """чтение данных из файла words.json и сохранение их в список """

    # Получаем все вопросы из файла n
    with open(path, "r", encoding="utf8") as file:
        return json.load(file)
# print(load_data())
