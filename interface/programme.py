import streamlit as st
from programmes.gestionnaire import ( obtenir_matieres, obtenir_niveaux, obtenir_programme)



def afficher_page_programme():

    st.title("📚 Programmes scolaires officiels")

    st.info(
        "Programmes scolaires du secondaire "
        "de l'Union des Comores."
    )
    cycle = st.selectbox(
        "🎓 Choisissez le cycle :",
        ["college", "lycee"],
        format_func=lambda x: x.capitalize()
    )
    niveaux = obtenir_niveaux(cycle)
    niveaux = st.selectbox(
        "📖 Choisissez votre niveau :",
        niveaux
    )
    matieres = obtenir_matieres(cycle, niveaux)
    matieres = st.selectbox(
        "📚 Choisissez la matière :",
        matieres
    )
    programme = obtenir_programme(
        matieres,
        niveaux,
        cycle
    )

    st.divider()

    st.header(
        f"📘 {matieres} — {niveaux}"
    )

    if programme:

        # Cas général : dictionnaire
        if isinstance(programme, dict):

            for categorie, contenu in programme.items():

                titre = (
                    str(categorie)
                    .replace("_", " ")
                    .title()
                )

                with st.expander(
                    f"📖 {titre}",
                    expanded=False
                ):

                    if isinstance(contenu, list):

                        for element in contenu:
                            st.write(f"• {element}")

                    elif isinstance(contenu, dict):

                        for cle, valeur in contenu.items():

                            sous_titre = (
                                str(cle)
                                .replace("_", " ")
                                .title()
                            )

                            st.markdown(
                                f"### {sous_titre}"
                            )

                            if isinstance(valeur, list):

                                for element in valeur:
                                    st.write(
                                        f"• {element}"
                                    )

                            else:
                                st.write(valeur)

                    else:
                        st.write(contenu)

        else:
            st.write(programme)

    else:

        st.warning(
            f"📋 Le programme officiel de "
            f"**{matieres}** pour **{niveaux}** "
            "sera ajouté prochainement."
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




