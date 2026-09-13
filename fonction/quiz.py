
import json

def charger_quiz():
    with open("data/quiz.json", "r", encoding="utf-8") as fichier:
        return json.load(fichier)

def obtenir_questions(quiz, niveau, matiere):
    return [
        q for q in quiz
        if q["niveau"] == niveau
        and q["matiere"] == matiere
    ]

def corriger_reponse(question, reponse_utilisateur):
    return reponse_utilisateur == question["bonne_reponse"]


