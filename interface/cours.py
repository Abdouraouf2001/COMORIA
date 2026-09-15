import streamlit as st

from fonction.cours import (
    charger_cours,
    obtenir_niveaux,
    obtenir_matieres,
    obtenir_cours
)

from config.colors import (
    primaryColor,
    secondaryColor,
    secondaryTextColor
)


def afficher_cours_selectionne(cours_selectionne):

    st.markdown(
        f"""
        <style>
        .cours-carte {{
            background-color: white;
            border-radius: 16px;
            padding: 1rem 1.25rem;
            margin-bottom: 14px;
            border: 0.5px solid #E0E6EC;
        }}

        .cours-titre {{
            color: {primaryColor};
            font-size: 22px;
            font-weight: 700;
            margin: 0 0 4px;
        }}

        .cours-info {{
            background-color: #EAF3DE;
            border-radius: 12px;
            padding: 12px 14px;
            color: {secondaryColor};
            font-size: 13px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    niveau = cours_selectionne.get(
        "niveau",
        "Niveau non précisé"
    )

    matiere = cours_selectionne.get(
        "matiere",
        "Matière non précisée"
    )

    chapitre = cours_selectionne.get(
        "chapitre",
        "Chapitre sans titre"
    )

    contenu = cours_selectionne.get(
        "contenu",
        "Aucun contenu disponible."
    )

    st.markdown(
        f"""
        <div class="cours-carte">
            <p class="cours-titre">
                📖 {chapitre}
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.info(
        f"🎓 Niveau : {niveau}  •  📚 Matière : {matiere}"
    )

    st.markdown("### 📖 Contenu du cours")

    if isinstance(contenu, list):
        for element in contenu:
            st.write(element)

    elif isinstance(contenu, dict):
        for cle, valeur in contenu.items():
            st.markdown(f"**{cle}**")
            st.write(valeur)

    else:
        st.write(contenu)

    exercices = cours_selectionne.get(
        "exercices",
        []
    )

    if exercices:

        st.markdown("### 📝 Exercices")

        for index, exercice in enumerate(
            exercices,
            start=1
        ):

            if isinstance(exercice, dict):

                question = exercice.get(
                    "question",
                    "Question non disponible"
                )

                st.write(
                    f"**{index}.** {question}"
                )

            else:

                st.write(
                    f"**{index}.** {exercice}"
                )

    st.divider()

    if st.button(
        "⬅️ Retour à la liste des cours",
        use_container_width=True
    ):

        del st.session_state["cours_selectionne"]

        st.rerun()


def afficher_page_cours():

    if "cours_selectionne" in st.session_state:

        afficher_cours_selectionne(
            st.session_state["cours_selectionne"]
        )

        return

    st.markdown(
        f"""
        <style>

        .cours-carte {{
            background-color: white;
            border-radius: 16px;
            padding: 1rem 1.25rem;
            margin-bottom: 14px;
            border: 0.5px solid #E0E6EC;
        }}

        .cours-titre {{
            color: {primaryColor};
            font-size: 22px;
            font-weight: 700;
            margin: 0 0 4px;
        }}

        .cours-info {{
            background-color: #EAF3DE;
            border-radius: 12px;
            padding: 12px 14px;
            color: {secondaryColor};
            font-size: 13px;
        }}

        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="cours-carte">
            <p class="cours-titre">
                📚 Choisis ton cours
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    cours = charger_cours()

    if not cours:
        st.warning("Aucun cours disponible.")
        return

    niveaux = obtenir_niveaux(cours)

    if not niveaux:
        st.warning("Aucun niveau disponible.")
        return

    with st.container(border=True):
        niveau = st.selectbox(
            "🎓 Ton niveau :",
            niveaux
        )

    matieres = obtenir_matieres(
        cours,
        niveau
    )

    if not matieres:
        st.warning(
            "Aucune matière disponible pour ce niveau."
        )
        return

    with st.container(border=True):
        matiere = st.selectbox(
            "📖 Matière :",
            matieres
        )

    resultats = obtenir_cours(
        cours,
        niveau,
        matiere
    )

    if not resultats:

        st.markdown(
            """
            <div class="cours-info">
                Aucun cours trouvé pour cette sélection.
            </div>
            """,
            unsafe_allow_html=True
        )

        return

    for index, c in enumerate(resultats):

        chapitre = c.get(
            "chapitre",
            "Chapitre sans titre"
        )

        with st.expander(
            f"📘 {chapitre}"
        ):

            contenu = c.get(
                "contenu",
                ""
            )

            if isinstance(contenu, list):

                for element in contenu:
                    st.write(element)

            elif isinstance(contenu, dict):

                for cle, valeur in contenu.items():

                    st.markdown(
                        f"**{cle}**"
                    )

                    st.write(valeur)

            else:

                st.write(contenu)

            exercices = c.get(
                "exercices",
                []
            )

            if exercices:

                st.markdown(
                    "### 📝 Exercices"
                )

                for exercice in exercices:

                    if isinstance(exercice, dict):

                        st.write(
                            f"- {exercice.get(
                                'question',
                                'Question non disponible'
                            )}"
                        )

                    else:

                        st.write(
                            f"- {exercice}"
                        )

    st.markdown("""
        <div class="footer-apropos">
              <strong>ComorIA</strong> — L'IA au service de l'éducation aux Comores
            <br>
            Une initiative portée par Abdouraouf Ahamada Saroumaya (Guilbert)
                <br>
                   2026 ComorIA . Tous droits reserves
        </div
        """, unsafe_allow_html=True)