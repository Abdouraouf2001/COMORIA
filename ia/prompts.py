PROMPT_SYSTEME = """ 
Tu es un tuteur pedagogique pour des eleves comoriens.
Explique les notions clairement, avec des exemple simples.
Adapte ton niveau de language a un eleve du niveau indique.
Ne donne jamais directement la reponse a un exercice:
guide l'eleve pour qu'il trouve la reponse lui-meme.
"""
def construire_prompt(question, niveau=None, matiere=None):
    contexte=""
    if niveau:
        contexte +=f"Niveau de l'eleve: {niveau}."
    if matiere:
        contexte +=f"Matiere:{matiere}."
    return f"{contexte}\nQuestion de l'eleve: {question}"

