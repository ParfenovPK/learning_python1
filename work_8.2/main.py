import random
import utils

def main():
    # Присваеваем переменнной questions список экземпляров класса Question
    questions = utils.load_questions()

    random.shuffle(questions)

    #Запускаем все вопросы по очереди
    for question in questions:

        #Выводим вопрос
        print(question.build_question())

        # Получаем ответ от пользователя
        print("Ответ: ")
        user_answer = input().lower()

        # Заносим новые данные в переменные  user_answer и is_asked
        question.user_answer = user_answer
        question.is_asked = True

        # Выводим результат правильности ответа и колличество баллов за ответ
        print(question.build_positive_or_negative_feedback())

    # Благодарим и прощаемся
    print()
    print("Вот и всё!")

    # Выводим общую статистику по игре
    print(utils.build_statistics(questions))

if __name__ == "__main__":
    main()
