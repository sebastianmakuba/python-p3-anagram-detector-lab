# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        return [w for w in word_list if self.is_anagram(w)]

    def is_anagram(self, other_word):
        if len(self.word) != len(other_word):
            return False

        return sorted(self.word.lower()) == sorted(other_word.lower())
