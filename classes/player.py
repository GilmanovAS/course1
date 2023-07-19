class Player:
    """This class contans """

    def __init__(self, name):
        self.name = name
        self.use_word = None

    def count_used_words(self):
        return len(self.use_word)

    def add_word(self, word):
        self.use_word += word

    def is_used(self, word):
        return word in self.use_word

    def __repr__(self):
        return f"Hi, {self.name} you guessed {0}"
