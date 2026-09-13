import json

def charger_cours():
    with open("data/cours.json", "r" , encoding="utf-8") as fichier:
        return json.load(fichier)

def obtenir_niveaux(cours):
    niveaux = sorted(set({c["niveau"] for c in cours}))
    return niveaux

def obtenir_matieres(cours, niveau):
    matiere = sorted(set(cours_item["matiere"] for cours_item in cours))
    return matiere

def obtenir_cours(cours, niveau,matiere):
    return[
        cours_item
        for cours_item in cours
        if cours_item["niveau"]==niveau 
        and cours_item["matiere"]==matiere
    ]






# def charger_cours():
#     """Charge les cours depuis le fichier JSON."""

#     chemin = os.path.join(
#         os.path.dirname(os.path.dirname(__file__)),
#         "data",
#         "cours.json"
#     )

#     with open(chemin, "r", encoding="utf-8") as fichier:
#         return json.load(fichier)


# def obtenir_niveaux(cours):
#     """Retourne la liste des niveaux disponibles."""

#     niveaux = sorted(
#         set(c["niveau"] for c in cours)
#     )

#     return niveaux


# def obtenir_matieres(cours, niveau):
#     """Retourne les matières disponibles pour un niveau."""

#     matieres = sorted(set(cours_item["matiere"] for cours_item in cours if cours_item["niveau"] == niveau))

#     return matieres


# def obtenir_cours(cours, niveau, matiere):
#     """Retourne les cours correspondant au niveau et à la matière."""

#     return [
#         cours_item
#         for cours_item in cours
#         if cours_item["niveau"] == niveau
#         and cours_item["matiere"] == matiere
#     ]







# import json

# def charger_cours():
#     with open("data/cours.json", "r" , encoding="utf-8") as fichier:
#         return json.load(fichier)

# def obtenir_niveaux(cours):
#     niveaux = sorted(set({c["niveau"] for c in cours}))
#     return niveaux

# def obtenir_matieres(cours, niveau):
#     matiere = sorted(set(cours_item["matiere"] for cours_item in cours))
#     return matiere


# def obtenir_cours(cours, niveau, matiere):
#     return[
#         cours_item
#         for cours_item in cours
#         if cours_item["niveau"]==niveau 
#         and cours_item["matiere"]==matiere
#     ]