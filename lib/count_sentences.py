#!/usr/bin/env python3

class MyString:
    

    def __init__(self, value=''):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if not isinstance(val, str):
            raise TypeError("Value must be a string")
        self._value = val

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        import re
        # Replace multiple punctuation marks with a single period
        text = re.sub(r'[.!?]+', '.', self.value)
        # Split the text by period and count non-empty parts
        sentences = [sentence for sentence in text.split('.') if sentence.strip()]
        return len(sentences)

string = MyString("This is a string! It has three sentences. Right?")
print(string.count_sentences()) 

