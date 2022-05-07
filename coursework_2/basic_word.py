class BasicWord:

    def __init__(self, original_word, set_of_under_words):
        self.original_word = original_word  # str
        self.set_of_under_words = set_of_under_words  # len(raeng(set_of_under_words)

        self.user_answer = None

    def __repr__(self):
        return f"\
               \nИсходное слово: {self.original_word}\
               \nНабор допустимых подслов: {self.set_of_under_words}\
               \nВвведите имя игрока: {self.user_answer}\
               "

    def word_comparison(self):
        """проверку введенного слова в списке допустимых подслов (вернет bool)"""
        return self.user_answer in self.set_of_under_word

    def counting_word_comparison(self):
        """подсчет количества подслов (вернет int)"""
        return len(self.set_of_under_words)

    def build_task(self):
        """Возвращает задание в понятном пользователю виде, например:
        задание: Составьте 8 слов из слова ПИТОН
        Слова должны быть не короче 3 букв
        Поехали, ваше первое слово?
        """
        return f"Составьте: {len(self.set_of_under_words)} слов из слова {self.original_word}\nСлова должны быть не короче 3 букв\nЧтобы закончить игру, угадайте все слова или напишите \"\stop\"\\nПоехали, ваше первое слово?"

    def build_feedback(self):
        """
        Возвращает : слова закончились, игра завершена!
        Возвращает : вы угадали 8 слов
        """
        if self.word_comparison():
            return f"Ответ верный, получено {self.points} баллов"
        return f"Ответ неверный, верный ответ {self.correct_answer} баллов"


class Player:

    def __init__(self, user_name, words_used):
        self.user_name = user_name  # имя пользователя
        self.words_used = words_used  # использованные слова пользователя

    def getting_the_number_of_words(self):
        pass
