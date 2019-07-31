class WordList:
    def __init__(self, name):
        self.name = name
        self.description = ""

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def getName(self):
        return self.name

    def setName(self,name):
        self.name = name

    def getDescription(self):
        return self.description

    def setDescription(self,description):
        self.description = description