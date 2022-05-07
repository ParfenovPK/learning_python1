import random

SPLITTER = "::"

def get_words(filenames):
    with open(filenames, 'r', encoding="utf-8") as file:
        words = file.read().splitlines()
    return words


def guessed_word(word):
    word_list = list(word)
    shake_word = random.sample(word_list, len(word_list))
    return "".join(shake_word)


def save_game_to_history(user_name, points_sum):
    with open("history.txt", "a", encoding="utf-8") as file:
        file.write(f"{user_name}{SPLITTER}{points_sum}\n")


def game_history():
    with open("history.txt", "r", encoding="utf-8") as file:
        data = file.read().splitlines()
        total_count_games = len(data)
        points_list = list()
        for note in data:
            _, points = note.split("::")
            points_list.append(points)
        max_record = max(points_list)

        print(f"Всего игор сыгранно: {total_count_games}")
        print(f"Максимальный рекорд: {max_record}")
