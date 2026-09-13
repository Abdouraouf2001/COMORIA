# import json
# from pathlib import Path

# BASE_DIR = Path(__file__).resolve().parent.parent
# DATA_DIR = BASE_DIR / "data"


# def charger_json(nom_fichier):
#     """
#     Charge un fichier JSON situé dans le dossier data.
#     """

#     chemin = DATA_DIR / nom_fichier

#     if not chemin.exists():
#         print(f"Fichier introuvable : {chemin}")
#         return []

#     try:
#         with open(chemin, "r", encoding="utf-8") as fichier:
#             donnees = json.load(fichier)

#         if isinstance(donnees, list):
#             return donnees

#         print(f"Le fichier {nom_fichier} ne contient pas une liste.")
#         return []

#     except json.JSONDecodeError as erreur:
#         print(f"Erreur JSON dans {nom_fichier} : {erreur}")
#         return []

#     except Exception as erreur:
#         print(f"Erreur lors du chargement de {nom_fichier} : {erreur}")
#         return []


# def charger_mathematiques_4eme():
#     """
#     Charge les cours de mathématiques de 4ème.
#     """

#     return charger_json("cours_maths_svt_4eme.json")

# def obtenir_matieres(cours):
#     """
#     Retourne les matières disponibles.
#     """

#     matieres = set()

#     for cours_item in cours:
#         matiere = cours_item.get("matiere")

#         if matiere:
#             matieres.add(matiere)

#     return sorted(matieres)

# def obtenir_niveaux(cours):
#     """
#     Retourne les niveaux disponibles.
#     """

#     niveaux = set()

#     for cours_item in cours:
#         niveau = cours_item.get("niveau")

#         if niveau:
#             niveaux.add(niveau)

#     return sorted(niveaux)

# def obtenir_categories(cours):
#     """
#     Retourne les catégories disponibles.
#     """

#     categories = set()

#     for cours_item in cours:
#         categorie = cours_item.get("categorie")

#         if categorie:
#             categories.add(categorie)

#     return sorted(categories)

# def obtenir_chapitres(cours):
#     """
#     Retourne les chapitres disponibles.
#     """

#     chapitres = []

#     for cours_item in cours:
#         chapitre = cours_item.get("chapitre")

#         if chapitre:
#             chapitres.append(chapitre)

#     return chapitres

# def filtrer_cours(cours, niveau=None, matiere=None, categorie=None):
#     """
#     Filtre les cours selon le niveau, la matière et la catégorie.
#     """

#     resultats = []

#     for cours_item in cours:

#         if niveau and cours_item.get("niveau") != niveau:
#             continue

#         if matiere and cours_item.get("matiere") != matiere:
#             continue

#         if categorie and cours_item.get("categorie") != categorie:
#             continue

#         resultats.append(cours_item)

#     return resultats


# def rechercher_chapitre(cours, nom_chapitre):
#     """
#     Recherche un chapitre précis.
#     """

#     for cours_item in cours:

#         chapitre = cours_item.get("chapitre", "")

#         if chapitre.lower() == nom_chapitre.lower():
#             return cours_item

#     return None
