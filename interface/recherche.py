import json
import unicodedata
from pathlib import Path

import streamlit as st


BASE_DIR = Path(__file__).resolve().parent.parent
COURS_FILE = BASE_DIR / "data" / "cours.json"


def charger_cours():
    try:
        with open(COURS_FILE, "r", encoding="utf-8") as fichier:
            donnees = json.load(fichier)

        return donnees if isinstance(donnees, list) else []

    except FileNotFoundError:
        st.error("❌ Le fichier data/cours.json est introuvable.")
        return []

    except json.JSONDecodeError:
        st.error("❌ Le fichier cours.json contient une erreur JSON.")
        return []

    except Exception as erreur:
        st.error(f"❌ Erreur : {erreur}")
        return []


def texte_normalise(texte):

    if texte is None:
        return ""

    if isinstance(texte, list):
        texte = " ".join(str(x) for x in texte)

    elif isinstance(texte, dict):
        texte = " ".join(str(x) for x in texte.values())

    else:
        texte = str(texte)

    texte = texte.lower()

    texte = unicodedata.normalize("NFD", texte)

    texte = "".join(
        caractere
        for caractere in texte
        if unicodedata.category(caractere) != "Mn"
    )

    return texte


def rechercher_cours(
    cours,
    recherche="",
    niveau="Tous",
    matiere="Toutes"
):

    recherche = texte_normalise(recherche).strip()
    niveau = texte_normalise(niveau).strip()
    matiere = texte_normalise(matiere).strip()

    resultats = []

    for cours_item in cours:

        niveau_cours = texte_normalise(
            cours_item.get("niveau", "")
        )

        matiere_cours = texte_normalise(
            cours_item.get("matiere", "")
        )

        chapitre_cours = texte_normalise(
            cours_item.get("chapitre", "")
        )

        contenu_cours = texte_normalise(
            cours_item.get("contenu", "")
        )

        texte_complet = " ".join([
            niveau_cours,
            matiere_cours,
            chapitre_cours,
            contenu_cours
        ])

        if niveau != "tous" and niveau_cours != niveau:
            continue

        if matiere != "toutes" and matiere_cours != matiere:
            continue

        if recherche and recherche not in texte_complet:
            continue

        resultats.append(cours_item)

    return resultats


def afficher_page_recherche():

    st.title("🔎 Recherche")

    st.write(
        "Trouvez rapidement un cours, un chapitre, "
        "une matière ou un contenu dans ComorIA."
    )

    st.divider()

    cours = charger_cours()

    if not cours:
        st.warning("⚠️ Aucun cours disponible.")
        return

    recherche = st.text_input(
        "🔎 Que recherchez-vous ?",
        placeholder="Exemple : mathematiques, triangle, pythagore..."
    )

    niveaux = sorted({
        str(c.get("niveau", "")).strip()
        for c in cours
        if c.get("niveau")
    })

    matieres = sorted({
        str(c.get("matiere", "")).strip()
        for c in cours
        if c.get("matiere")
    })

    col1, col2 = st.columns(2)

    with col1:

        niveau = st.selectbox(
            "🎓 Niveau",
            ["Tous"] + niveaux
        )

    with col2:

        matiere = st.selectbox(
            "📚 Matière",
            ["Toutes"] + matieres
        )

    rechercher = st.button(
        "🔎 Rechercher",
        use_container_width=True
    )

    st.divider()

    if rechercher:

        resultats = rechercher_cours(
            cours,
            recherche,
            niveau,
            matiere
        )

        if resultats:

            st.success(
                f"✅ {len(resultats)} résultat(s) trouvé(s)"
            )

            for index, cours_item in enumerate(resultats):

                niveau_cours = cours_item.get(
                    "niveau",
                    "Niveau non précisé"
                )

                matiere_cours = cours_item.get(
                    "matiere",
                    "Matière non précisée"
                )

                chapitre_cours = cours_item.get(
                    "chapitre",
                    "Chapitre sans titre"
                )

                contenu = cours_item.get(
                    "contenu",
                    ""
                )

                if isinstance(contenu, (dict, list)):
                    contenu = texte_normalise(contenu)

                contenu = " ".join(
                    str(contenu).split()
                )

                if len(contenu) > 300:
                    contenu = contenu[:300] + "..."

                with st.container(border=True):

                    st.subheader(
                        f"📖 {chapitre_cours}"
                    )

                    st.caption(
                        f"🎓 {niveau_cours}  •  "
                        f"📚 {matiere_cours}"
                    )

                    st.write(contenu)

                    if st.button(
                        "📖 Ouvrir le cours",
                        key=f"ouvrir_cours_{index}"
                    ):

                        # Enregistrer le cours sélectionné
                        st.session_state[
                            "cours_selectionne"
                        ] = cours_item

                        # Demander à l'application
                        # d'afficher la page Cours
                        st.session_state[
                            "page_forcee"
                        ] = "Cours"

                        # Recharger l'application
                        st.rerun()

        else:

            st.warning(
                "🔍 Aucun résultat trouvé."
            )

            st.info(
                "Essayez un autre mot-clé ou "
                "modifiez les filtres."
            )

    else:

        st.info(
            "💡 Entrez un mot-clé puis cliquez sur "
            "« Rechercher »."
        )
