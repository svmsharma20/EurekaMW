class Word:
    def __init__(self, name, xdef):
        self.name = name
        self.shortdef = ""
        self.category = ""
        self.stems = ""
        self.xdef = xdef;

    def __init__(self, name, category, xdef):
        self.name = name
        self.shortdef = ""
        self.category = category
        self.stems = ""
        self.xdef = xdef;

    def __init__(self, name, stems, xdef):
        self.name = name
        self.shortdef = ""
        self.category = ""
        self.stems = stems
        self.xdef = xdef;

    def __init__(self, name, category, stems, xdef):
        self.name = name
        self.shortdef = ""
        self.category = category
        self.stems = stems
        self.xdef = xdef;

    def __init__(self, name, category, stems, shortdef, xdef):
        self.name = name
        self.shortdef = shortdef
        self.category = category
        self.stems = stems
        self.xdef = xdef;

    def set_name(self,name):
        self.name = name

    def get_name(self):
        return self.name

    def setShortDef(self,shortdef):
        self.shortdef = shortdef

    def get_short_def(self):
        return self.shortdef

    def set_category(self,category):
        self.category = category

    def get_category(self):
        return self.category

    def set_stems(self,stems):
        self.stems = stems

    def get_stems(self):
        return self.stems
