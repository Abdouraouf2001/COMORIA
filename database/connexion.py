import sqlite3

def obtenir_connexion():
    connexion =sqlite3.connect("data/comoria")
    connexion.row_factory = sqlite3.Row
    return connexion