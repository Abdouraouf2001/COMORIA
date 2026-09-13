from fonction.cours import charger_cours
def rechercher_contexte(question, nombre_resultats=2):
    cours = charger_cours()
    mots_question = question.lower().split()

    resultats_notes = []

    for c in cours:
        texte_cours = (c["chapitre"] + " " + c["contenu"]).lower()
        score = sum(1 for mot in mots_question if mot in texte_cours)

        if score > 0:
            resultats_notes.append((score, c))

    resultats_notes.sort(key=lambda x: x[0], reverse=True)

    return [c for score, c in resultats_notes[:nombre_resultats]]

