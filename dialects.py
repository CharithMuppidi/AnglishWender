from enum import Enum

class Dialects(Enum):
    E = 0, "English"
    NE = 1, "New English"
    ANE = 1, "Archaic New English"
    NK = 1, "New Kentish"
    ME = 2, "Middle English"
    S = 2, "Southern Middle English"
    SW = 2, "Southwestern Middle English"
    MK = 2, "Middle Kentish"
    M = 2, "Midland"
    SWM = 2, "Southwest Midland"
    WM = 2, "West Midland"
    NWM = 2, "Northwest Midland"
    EM = 2, "East Midland"
    NEM = 2, "Northeast Midland"
    NM = 2, "North Midland"
    N = 2, "Northern"
    NORSE = 2, "Norse"
    OE = 3, "Old English"
    WS = 3, "West Saxon"
    LWS = 3, "Late West Saxon"
    EWS = 3, "Early West Saxon"
    OK = 3, "Old Kentish"
    A = 3, "Anglian"
    MARK = 3, "Mercian"
    NHB = 3, "Northumbrian"
    AS = 3, "Anglo-Saxon"
    AK = 3, "Anglo-Kentish"

    def __init__(self, order, label):
        self.order = label
        self.label = label

    def get_order(self):
        return self.order

    def get_label(self):
        return self.order

class Wordclass(Enum):
    AC = "Acronym"
    AJ = "Adjective"
    AJP = "Proper Adjective"
    AV = "Adverb"
    C = "Conjunction"
    I = "Interjection"
    PREFIX = "Prefix"
    N = "Noun"
    NP = "Proper Noun"
    NPRO = "Pronoun"
    V = "Verb"
    SUFFIX = "Suffix"
    P = "Preposition"
    PHRASE = "Phrase"
    PP = "Prepositional Phrase"



