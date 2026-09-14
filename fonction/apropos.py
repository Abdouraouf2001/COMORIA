
import json
from database.connexion import obtenir_connexion

def compter_utilisateurs():
    conn = obtenir_connexion()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM utilisateurs")
    nombre = cursor.fetchone()[0]
    conn.close()
    return nombre

def compter_cours():
    with open("data/cours.json", "r", encoding="utf-8") as f:
        cours = json.load(f)
    return len(cours)

def compter_matieres():
    with open("data/cours.json", "r", encoding="utf-8") as f:
        cours = json.load(f)
    matieres = set(chapitre["matiere"] for chapitre in cours)
    return len(matieres)

def compter_quiz():
    with open("data/quiz.json", "r", encoding="utf-8") as f:
        quiz = json.load(f)
    return len(quiz)
