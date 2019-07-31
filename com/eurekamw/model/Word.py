class Word:
    def __init__(self, name):
        self.name = name
        self.shortdef = ""
        self.category = ""

    def __init__(self, name, category):
        self.name = name
        self.shortdef = ""
        self.category = category

    def setName(self,name):
        self.name = name

    def getName(self):
        return self.name

    def setShortDef(self,shortdef):
        self.shortdef = shortdef

    def getShortDef(self):
        return self.shortdef

    def setCategory(self,category):
        self.category = category

    def getCategory(self):
        return self.category
