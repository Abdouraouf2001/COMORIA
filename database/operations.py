from database.connexion import obtenir_connexion
import hashlib
from datetime import datetime


# =========================================================
# MOT DE PASSE
# =========================================================

def hacher_mot_de_passe(mot_de_passe):
    return hashlib.sha256(mot_de_passe.encode()).hexdigest()


# =========================================================
# INSCRIPTION
# =========================================================

def inscrire_utilisateur_db(nom, mot_de_passe, role="eleve"):

    connexion = obtenir_connexion()
    curseur = connexion.cursor()

    curseur.execute(
        "SELECT * FROM utilisateurs WHERE nom = ?",
        (nom,)
    )

    if curseur.fetchone():
        connexion.close()
        return False, "Ce nom d'utilisateur existe deja."

    curseur.execute(
        """
        INSERT INTO utilisateurs
        (nom, mot_de_passe, role)
        VALUES (?, ?, ?)
        """,
        (
            nom,
            hacher_mot_de_passe(mot_de_passe),
            role
        )
    )

    connexion.commit()
    connexion.close()

    return True, "Inscription reussie !"


# =========================================================
# CONNEXION
# =========================================================

def verifier_connexion_db(nom, mot_de_passe):

    connexion = obtenir_connexion()
    curseur = connexion.cursor()

    mot_de_passe_hache = hacher_mot_de_passe(
        mot_de_passe
    )

    curseur.execute(
        """
        SELECT *
        FROM utilisateurs
        WHERE nom = ?
        AND mot_de_passe = ?
        """,
        (
            nom,
            mot_de_passe_hache
        )
    )

    utilisateur = curseur.fetchone()

    connexion.close()

    if utilisateur:
        return True, utilisateur["role"]

    return False, None


# =========================================================
# DÉFINIR ADMINISTRATEUR
# =========================================================

def definir_administrateur(nom):

    connexion = obtenir_connexion()
    curseur = connexion.cursor()

    curseur.execute(
        """
        UPDATE utilisateurs
        SET role = ?
        WHERE nom = ?
        """,
        (
            "admin",
            nom
        )
    )

    connexion.commit()

    modifie = curseur.rowcount > 0

    connexion.close()

    return modifie


# =========================================================
# RÉCUPÉRER TOUS LES UTILISATEURS
# =========================================================

def obtenir_utilisateurs():

    connexion = obtenir_connexion()
    curseur = connexion.cursor()

    curseur.execute(
        """
        SELECT id, nom, role
        FROM utilisateurs
        ORDER BY id DESC
        """
    )

    utilisateurs = curseur.fetchall()

    connexion.close()

    return utilisateurs


# =========================================================
# MODIFIER LE RÔLE
# =========================================================

def modifier_role_utilisateur(
    utilisateur_id,
    nouveau_role
):

    connexion = obtenir_connexion()
    curseur = connexion.cursor()

    curseur.execute(
        """
        UPDATE utilisateurs
        SET role = ?
        WHERE id = ?
        """,
        (
            nouveau_role,
            utilisateur_id
        )
    )

    connexion.commit()

    modifie = curseur.rowcount > 0

    connexion.close()

    return modifie


# =========================================================
# SUPPRIMER UN UTILISATEUR
# =========================================================

def supprimer_utilisateur(utilisateur_id):

    connexion = obtenir_connexion()
    curseur = connexion.cursor()

    curseur.execute(
        """
        DELETE FROM utilisateurs
        WHERE id = ?
        """,
        (utilisateur_id,)
    )

    connexion.commit()

    supprime = curseur.rowcount > 0

    connexion.close()

    return supprime


# =========================================================
# STATISTIQUES UTILISATEURS
# =========================================================

def compter_utilisateurs():

    connexion = obtenir_connexion()
    curseur = connexion.cursor()

    curseur.execute(
        "SELECT COUNT(*) FROM utilisateurs"
    )

    total = curseur.fetchone()[0]

    connexion.close()

    return total


def compter_utilisateurs_par_role(role):

    connexion = obtenir_connexion()
    curseur = connexion.cursor()

    curseur.execute(
        """
        SELECT COUNT(*)
        FROM utilisateurs
        WHERE role = ?
        """,
        (role,)
    )

    total = curseur.fetchone()[0]

    connexion.close()

    return total


def creer_table_messages():

    conn = obtenir_connexion()
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS messages_contact (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            email TEXT NOT NULL,
            message TEXT NOT NULL,
            date_envoi TEXT NOT NULL
        )
        """
    )

    conn.commit()
    conn.close()


def enregistrer_message_contact(
    nom,
    email,
    message
):

    conn = obtenir_connexion()
    cursor = conn.cursor()

    date_envoi = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    cursor.execute(
        """
        INSERT INTO messages_contact
        (nom, email, message, date_envoi)
        VALUES (?, ?, ?, ?)
        """,
        (
            nom,
            email,
            message,
            date_envoi
        )
    )

    conn.commit()
    conn.close()
