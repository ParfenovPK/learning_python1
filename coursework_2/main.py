import utils
from classes.player import Player
from config import PATH

print("Введите имя пользователя")

user_input = input()
player = Player(user_input)

print(f"Привет, {player.user_name}")

basic_word = utils.load_random_words(PATH)

print(f"Составьте {basic_word.counting_words()} слов из слова {basic_word.original_word.upper()}")
print("Слова должны быть не короче 3 букв")
print("Чтобы закончить игру, угадайте все слова или напишите слово \"stop\"")
print("Поехали, ваше первое слово?")

# цикл выполняется до тех пор пока пользователь угадал меньше чем подслов базового слова
while player.count_words() < basic_word.counting_words():

    print()

    user_input = input().strip().lower()

    if user_input in ["стоп", "stop"]:
        print("Игра завершена!")
        break

    if not basic_word.check_word(user_input):
        print("Такого слова нет")
        continue

    if not player.check_user_words(user_input):
        print("Такое слово уже было использовано")
        continue

    player.add_word(user_input)
    print(f"верно, вы угадали вот столько {player.count_words()}")

print("Слова закончились, игра завершена!")

print(f"Вы угадали {player.count_words()} слов!")