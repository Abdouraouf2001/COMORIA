from database.connexion import obtenir_connexion
import hashlib

def hacher_mot_de_passe(mot_de_passe):
    return hashlib.sha256(mot_de_passe.encode()).hexdigest()

def inscrire_utilisateur_db(nom, mot_de_passe, role="eleve"):
    connexion = obtenir_connexion()
    curseur = connexion.cursor()

    curseur.execute("SELECT * FROM utilisateurs WHERE nom = ?", (nom,))
    if curseur.fetchone():
        connexion.close()
        return False, "Ce nom d'utilisateur existe deja."

    curseur.execute(
        "INSERT INTO utilisateurs (nom, mot_de_passe, role) VALUES (?, ?, ?)",
        (nom, hacher_mot_de_passe(mot_de_passe), role)
    )
    connexion.commit()
    connexion.close()
    return True, "Inscription reussie !"

def verifier_connexion_db(nom, mot_de_passe):
    connexion = obtenir_connexion()
    curseur = connexion.cursor()

    mot_de_passe_hache = hacher_mot_de_passe(mot_de_passe)
    curseur.execute(
        "SELECT * FROM utilisateurs WHERE nom = ? AND mot_de_passe = ?",
        (nom, mot_de_passe_hache)
    )
    utilisateur = curseur.fetchone()
    connexion.close()

    if utilisateur:
        return True, utilisateur["role"]
    return False, None
