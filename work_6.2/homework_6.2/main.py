import functions



def main():
    user_name = input("Введите ваше имя")

    words = functions.get_words("words.txt")
    points_sum = 0

    for word in words:
        shuffled_word = functions.guessed_word(word)

        print(f"Угадай слово: {shuffled_word}")
        user_answer = input("Ваш ответ: ")
        user_answer = user_answer.lower()

        if user_answer == word:
            print("Верно! Вы получаете 10 очков!")
            points_sum += 10
        else:
            print(f"Неверно! Верный ответ - {word}")

    functions.save_game_to_history(user_name, points_sum)

    functions.game_history()


main()
