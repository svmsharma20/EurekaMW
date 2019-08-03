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
