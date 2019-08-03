"""
    Word collection related utilities.
"""
class WordList:
    def __init__(self, name, list):
        self.name = name
        self.description = ""
        self.list = list

    def __init__(self, name, description, list):
        self.name = name
        self.description = description
        self.list = list
