
# Bare outline of the question that takes in the text and the answer for a question. This class will be used to convert raw 
# data into question format
class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer