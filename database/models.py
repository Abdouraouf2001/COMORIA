from database.connexion import obtenir_connexion

def creer_tables():
    connexion = obtenir_connexion()
    curseur = connexion.cursor()

    curseur.execute("""
        CREATE TABLE IF NOT EXISTS utilisateurs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT UNIQUE NOT NULL,
            mot_de_passe TEXT NOT NULL,
            role TEXT NOT NULL
        )
    """)
    curseur.execute(""" 
        CREATE TABLE IF NOT EXISTS publications ( 
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            auteur TEXT NOT NULL, 
            role TEXT NOT NULL, 
            categorie TEXT NOT NULL, 
            contenu TEXT NOT NULL, 
            date TEXT NOT NULL 
        ) 
    """) 
 
    curseur.execute(""" 
        CREATE TABLE IF NOT EXISTS publication_likes ( 
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            publication_id INTEGER NOT NULL, 
            utilisateur TEXT NOT NULL, 
            UNIQUE(publication_id, utilisateur) 
        ) 
    """) 

    connexion.commit()
    connexion.close()
