from ia.contexte import rechercher_contexte

def repondre_question(question, contexte_cours=None):
    cours_pertinents = rechercher_contexte(question)

    if cours_pertinents:
        chapitres_trouves = ", ".join(c["chapitre"] for c in cours_pertinents)
        extrait = cours_pertinents[0]["contenu"][:200]

        reponse_simulee = (
            f"(Reponse simulee, basee sur tes cours) "
            f"J'ai trouve du contenu pertinent dans : {chapitres_trouves}.\n\n"
            f"Extrait : \"{extrait}...\"\n\n"
            f"Une fois connectee a une vraie IA, je pourrai t'expliquer "
            f"cette notion en detail a partir de ce contenu."
        )
    else:
        reponse_simulee = (
            f"(Reponse simulee) Je n'ai trouve aucun cours correspondant "
            f"a ta question dans le contenu disponible actuellement."
        )

    return reponse_simulee














# def repondre_question(question, context_cours=None):
#     reponse_simulee =(
#     f"(Reponse simule) tu as demande: <<{question}>>."
#     "Une fois connectee a une vrais IA , je pourrai t'explique"
#     "cette notion en dettail, avec des exemple adapltes a ton niveau"
#     )
#     return reponse_simulee