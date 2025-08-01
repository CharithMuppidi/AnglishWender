from typing import Any
from dialects import *

class Word:
    def __init__(self,normal,wordclass,etymology,glosses=None,anglish=None, uttering=None,tenses=None):
        self.normal = normal
        self.anglish = anglish
        self.uttering = uttering
        self.glosses = glosses
        self.wordclass = wordclass
        self.etymology = etymology
        self.tenses = tenses


def main():
    

    yif = Word(
        normal = {
            Dialects.A: "if",
            Dialects.WS: "yif",
            Dialects.NK: "yef"
        },
        anglish = {
            Dialects.WS: "gif",
            Dialects.NK: "gef"
        },
        wordclass = "conjunction",
        etymology= {
            Dialects.MK: "yef",
            Dialects.SW: "yif",
            Dialects.M: "if",
            Dialects.OE: ["gif","gyf"]
        })

    prepart = Word(
        normal = {
            Dialects.S:"ind",
            Dialects.M:"end",
            Dialects.N:"and",
            Dialects.NE:"ing"
        },
        etymology= {
            Dialects.S: "-inde",
            Dialects.M: "-ende",
            Dialects.N: "-ande",
        }
    )

    pastpart = Word(
        normal= {
            Dialects.N:"",
            Dialects.M:"a-",
            Dialects.S:"i-"
        },
        etymology="ge-"
    )

    plural = Word(
        normal={
            Dialects.A:["es","s"],
            Dialects.S: ["en", "n"]
        },
        wordclass=Wordclass.SUFFIX
    )

    gain = Word(
        normal={
            Dialects.NORSE: "gain",
            Dialects.S:"yen",
            Dialects.A:"yain"
        },
        anglish={
            Dialects.NORSE: "gagn",
            Dialects.S: "gen",
            Dialects.A:"gegn"
        },
        etymology={
            Dialects.NORSE:"gegn",
            Dialects.WS: "ġēan",
            Dialects.MARK:"gegn",
            Dialects.NHB:"gægn"
        },
        glosses="gain",
        wordclass=Wordclass.PREFIX
    )

    swain = Word(
        normal= {
            Dialects.NORSE:"swain",
            Dialects.E:"swoon"
        },
        anglish={
            Dialects.NORSE:"sƿagn",
            Dialects.E:"sƿoon"
        },
        etymology={
            Dialects.NORSE:"swegen",
            Dialects.E:"swān"
        },
        glosses="swain"
    )

    evil = Word(
        normal="yvil",
        anglish="yfel"
    )

    kale = Word(
        normal={
            Dialects.S:"cole",
            Dialects.A:"kale"
        },
        etymology={Dialects.ME:"",Dialects.OE:"cawel"}

    )

    lough = Word(
        normal="lough",
        anglish="luge",
        glosses=["loch","lough"]
    )

    hair = Word(
        normal={
            Dialects.S:"hear",
            Dialects.A:"heer"
        },
        etymology={
            Dialects.WS: "hǣr",
            Dialects.A: "hēr"
        }
    )

    Anglo = [
        Word(
            word="Ingle",
            anglish="Ingel",
            lore=["Engle","Ængle","Angle"],
            wordclass=Wordclass.NP,
            glosses="anglo"
        ),
        Word(
            "Inglish",
            anglish="Inglisc",
            wordclass=Wordclass.AJP,
            glosses="anglo"
        )
    ]

    Saxon = [
        Word(
            "Sax",
            wordclass=Wordclass.NP
        ),
        Word(
            "Saxish",
            anglish="Saxisc",
            wordclass=Wordclass.AJP
        )
    ]

    elephant = Word(normal={
        Dialects.WS:"ilp",
        Dialects.AK:"elp"
    })

    birth = Word(
        {
            Dialects.NORSE:"birth",
            Dialects.E:"ybyrd"
        },
        anglish={
            Dialects.NORSE: "birð",
        },
        etymology={
            Dialects.NORSE: "*byrðr",
        }

    )

    devil = Word(
        "devil",
        anglish="defel"
    )

    breakfast = Word(
        "fastbritch",
        anglish="fastbric",
        etymology={Dialects.OE:"fæstenbrice"}
    )

    air = [
        Word("aria", glosses="air"),
        Word({
            Dialects.NORSE:"loft",
            Dialects.E:"lift"
        })
    ]

    cross = [
        Word(
            {
                Dialects.NORSE:"cross",
                Dialects.E: "crouch"
            },
            anglish={
                Dialects.E: "cruce"
            }
        ),
        Word("rood")
    ]

    gear = [
        Word(
            {
                Dialects.NORSE:"gear",
                Dialects.E:"yare",
            },
            anglish={Dialects.E:"geare"},
            etymology={Dialects.E:"gearwe"}

        ),
        Word(
            {
                Dialects.NORSE:"gear",
                Dialects.AK:"yare",
                Dialects.WS:"yir"
            },
            anglish={
                Dialects.AK:"geare",
                Dialects.WS:"gir"
            },
            etymology={
                Dialects.AK:"gearwian",
                Dialects.LWS:"gyrwan",
                Dialects.EWS:"gierwan"

            }

        ),

    ]





