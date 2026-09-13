import json
import unicodedata
from pathlib import Path
MATIERES_COLLEGE = [
    "mathematiques",
    "francais",
    "anglais",
    "arabe",
    "histoire-geographie",
    "SVT",
    "Physique-Chimie"
]


MATIERES_LYCEE = [
    "mathematiques",
    "francais",
    "Anglais",
    "Arabe",
    "histoire-geographie",
    "SVT",
    "Physique-Chimie",
    "Philosophie"
]


NIVEAUX_COLLEGE = [
    "6e",
    "5e",
    "4e",
    "3e"
]

NIVEAUX_LYCEE = [
    "Seconde",
    "Premiere",
    "Terminale"
]
SERIES_LYCEE = {
    "Seconde":[
        "A",
        "C",
        "G"
    ],
    "Premiere":[
        "A",
        "C",
        "D",
        "G"
    ],
    "Terminale":[
        "A1",
        "A4",
        "C",
        "D",
        "G"
    ]
}
try:
    from programmes.mathematiques.programme_mathematiques import  PROGRAMME_MATHEMATIQUES 
except ImportError:
    PROGRAMME_MATHEMATIQUES = {
        "colege": {},
        "lycee": {}
    }

try:
    from programmes.francais.programme_francais import PROGRAMME_FRANCAIS 
except ImportError:
    PROGRAMME_FRANCAIS = {
        "colege": {},
        "lycee": {}
    }

try:
    from programmes.svt.programme_svt import ( PROGRAMME_SVT )
except ImportError:
    PROGRAMME_SVT = {
        "colege": {},
        "lycee": {}
    }

try:
    from programmes.histoire_geographie.programme_histoire_geographie import ( PROGRAMME_HISTOIRE_GEOGRAPHIE )
except ImportError:
    PROGRAMME_HISTOIRE_GEOGRAPHIE = {
        "colege": {},
        "lycee": {}
    }

def obtenir_matieres(cycle, niveaux):
    if cycle=="college":
        return MATIERES_COLLEGE.copy()
    if cycle=="lycee":
        return MATIERES_LYCEE.copy()
    return []
def obtenir_niveaux(cycle):
    if cycle =="college":
        return NIVEAUX_COLLEGE.copy()
    if cycle=="lycee":
        return NIVEAUX_LYCEE.copy()
    return[]
PROGRAMME_PAR_MATIERE ={
    "mathematiques":PROGRAMME_MATHEMATIQUES,
    "francais": PROGRAMME_FRANCAIS,
    "SVT":PROGRAMME_SVT,
    "histoire_geographie":PROGRAMME_HISTOIRE_GEOGRAPHIE
}

def obtenir_programme(matieres , niveaux, cycle):
    cle_cycle="college" if cycle=="college" else "lycee"

    Programme_matiere =PROGRAMME_PAR_MATIERE.get(matieres)
    if not Programme_matiere:
        return None

    return Programme_matiere.get(cle_cycle, {}).get(niveaux)
    