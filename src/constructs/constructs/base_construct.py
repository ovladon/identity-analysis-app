# constructs/base_construct.py

class BaseConstruct:
    def __init__(self, name):
        self.name = name

    def analyze_text(self, text):
        raise NotImplementedError("This method should be overridden by subclasses.")

