class Word:
    def __init__(self, name):
        self.name = name
        self.shortdef = ""
        self.category = ""
        self.stems = ""

    def __init__(self, name, category):
        self.name = name
        self.shortdef = ""
        self.category = category
        self.stems = ""

    def __init__(self, name, stems):
        self.name = name
        self.shortdef = ""
        self.category = ""
        self.stems = stems

    def __init__(self, name, category, stems):
        self.name = name
        self.shortdef = ""
        self.category = category
        self.stems = stems

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

    def setStems(self,stems):
        self.stems = stems

    def getStems(self):
        return self.stems
