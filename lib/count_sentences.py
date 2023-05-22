#!/usr/bin/env python3

class MyString:
      def __init__(self, value=''):
        if isinstance(value, str):
            self.value = value
        else:
            print("The value must be a string.")


      def is_sentence(self):
        return self.value.endswith('.')

      def is_question(self):
        return self.value.endswith('?')

      def is_exclamation(self):
        return self.value.endswith('!')

      def count_sentences(self):
        sentences = [sentence.strip() for sentence in self.value.split('.') if sentence.strip()]
        return len(sentences)
    
string = MyString("Hello World. How Wonderful is it to be in this great great world!?")
