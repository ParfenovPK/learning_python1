import json
import requests as request

import random

from coursework_2.classes.basic_word import BasicWord


def load_words_from_jsonkeeper(path):
    """Загружает список слов из внешнего хранилища"""
    response = request.get(path)
    list_fo_words = response.json()
    return list_fo_words


def load_random_words(path):
    """Получает одно слово на основе списка слов из внешнего хранилища"""
    list_of_words = load_words_from_jsonkeeper(path)
    random_word = random.choice(list_of_words)

    word = random_word["word"]
    sub_words = random_word["subwords"]

    basic_word = BasicWord(word, sub_words)
    return basic_word
