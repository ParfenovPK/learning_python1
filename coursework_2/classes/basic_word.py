
class BasicWord:
    """Этот класс обрабатывает слова """
    def __init__(self, original_word, under_words):
        self.original_word = original_word  # str  основное слово
        self.under_words = under_words  # получаем lest подслов

    def __repr__(self):
        return f"\
           \nИсходное слово: {self.original_word}\
           \nНабор допустимых подслов: {self.under_words}\
            "
    def get_word(self):
        """Возвращает оригинальное слово"""
        return self.original_word


    def check_word(self, user_word):
        """проверка введенного слова в списке допустимых подслов (вернет bool)"""
        if user_word in self.under_words:
            return True
        return False

    def counting_words(self):
        """подсчет количества подслов (вернет int)"""
        return len(self.under_words)
