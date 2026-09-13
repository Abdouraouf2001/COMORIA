import json
import hashlib

def charger_utilisateurs():
    with open("data/user.json", "r", encoding="utf-8") as fichier:
        return json.load(fichier)

def sauvegarder_utilisateurs(utilisateurs):
    with open("data/user.json", "w", encoding="utf-8") as fichier:
        json.dump(utilisateurs, fichier, indent=4, ensure_ascii=False)

def hacher_mot_de_passe(mot_de_passe):
    return hashlib.sha256(mot_de_passe.encode()).hexdigest()

def inscrire_utilisateur(nom, mot_de_passe, role="eleve"):
    utilisateurs = charger_utilisateurs()

    for u in utilisateurs:
        if u["nom"] == nom:
            return False, "Ce nom d'utilisateur existe deja."

    nouvel_utilisateur = {
        "nom": nom,
        "mot_de_passe": hacher_mot_de_passe(mot_de_passe),
        "role": role
    }
    utilisateurs.append(nouvel_utilisateur)
    sauvegarder_utilisateurs(utilisateurs)
    return True, "Inscription reussie !"

def verifier_connexion(nom, mot_de_passe):
    utilisateurs = charger_utilisateurs()
    mot_de_passe_hache = hacher_mot_de_passe(mot_de_passe)
    for u in utilisateurs:
        if u["nom"] == nom and u["mot_de_passe"] == mot_de_passe_hache:
            return True, u["role"]

    return False, None
