class BasicWord:
    """This class contains function  """
    def __init__(self, word, sub_words):
        self.word = word
        self.sub_words = sub_words

    def has_subword(self, word):
        return word.lower() in self.sub_words

    def count_subword(self):
        return len(self.sub_words)

    def __repr__(self):
        return f"The {self.word} contains next {len(self.sub_words)}"




