class VariablePart:
    def __init__(self, type, text):
        self.type = type
        self.text = text
    def __str__(self):
        return self.text
    def __repr__(self):
        return self.__str__()