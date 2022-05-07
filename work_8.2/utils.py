import json
from question import Question

PATH = "questions.json"

def load_data(path=PATH):
    """чтение данных из файла questions.json и сохранение их в список """

    # Получаем все вопросы из файла
    with open(path, "r", encoding="utf8") as file:
        return json.load(file)

#print(load_data(path="tests/questions.json"))

def load_questions(path=PATH):

    questions_data = load_data(path)
    questions = []
    # переводим список словарей в список экземпляров класса Question
    for question_data in questions_data:

        question = Question(question_data["q"], question_data["d"], question_data["a"])
        questions.append(question)

    return questions
#print(load_questions(path="tests/questions.json"))

def build_statistics(questions):
    """ выводится статистика на основе списка questions"""

    correct_answers, total_answers, score = 0, 0, 0

    for question in questions:
        total_answers += 1
        if question.is_correct():
            correct_answers += 1
            score += question.get_points()

    return f"Отвечено {correct_answers} вопроса из {total_answers}\nНабрано баллов: {score}"
