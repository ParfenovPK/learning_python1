class Player:
    """Этот клас обрабатывает информацию о пользователе"""

    def __init__(self, user_name):
        self.user_name = user_name  # получаем str  -  имя пользователя
        self.used_words = []  # получаем LEST - использованные слова пользователя

    def count_words(self):
        # Возвращает количество совпавших слов угаданных ипользователем (возвращает int)
        return len(self.used_words)

    def add_word(self, word):
        """Добавляет слово в список использованных слов"""
        self.used_words.append(word)

    def check_user_words(self, word):
        # Проверяет не использовалось ли слово ранее
        if word not in self.used_words:
            return True
        return False

    def get_name(self):
        """Возвращает имя"""
        return self.user_name

    def __repr__(self):
        return f"\
        \nИмя пользователя: {self.user_name}\
        \nУгаданные подслова {self.used_words}\
        "
