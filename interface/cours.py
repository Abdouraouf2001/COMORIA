
import streamlit as st
from fonction.cours import  charger_cours, obtenir_niveaux, obtenir_matieres, obtenir_cours 

def afficher_page_cours():

    st.title("📚 Choisis ton cours")
    cours = charger_cours()

    if not cours:
        st.warning("Aucun cours disponible.")
        return
    niveaux = obtenir_niveaux(cours)
    if not niveaux:
        st.warning("Aucun niveau disponible.")
        return
    niveau = st.selectbox(
        "🎓 Ton niveau :",
        niveaux
    )
    matieres = obtenir_matieres(cours, niveau)
    if not matieres:
        st.warning("Aucune matière disponible pour ce niveau.")
        return
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
        st.info("Aucun cours trouvé pour cette sélection.")
        return

    # Afficher les cours
    for c in resultats:

        chapitre = c.get("chapitre", "Chapitre sans titre")

        with st.expander(f"📘 {chapitre}"):

            st.write(c.get("contenu", ""))

            if "exercices" in c and c["exercices"]:

                st.markdown("### 📝 Exercices")

                for ex in c["exercices"]:
                    st.write(
                        f"- {ex.get('question', 'Question non disponible')}"
                    )




# import streamlit as st
# from fonction.cours import charger_cours, obtenir_niveaux, obtenir_matieres, obtenir_cours

# def afficher_page_cours():
#     st.title("Choisis ton cours")

#     cours = charger_cours()
#     niveau = st.selectbox("ton niveau:", obtenir_niveaux(cours))
#     matiers= st.selectbox("Matiere:",obtenir_matieres(cours , niveau))

#     resultats = obtenir_cours(cours,niveau,matiers)
#     for c in resultats:
#         with st.expander(f"{c['chapitre']}"):
#             st.write(c["contenu"])

#             if "exercices" in c :
#                st.markdown("***Exercices : ***")
#                for ex in c["exercices"]:
#                    st.write(f"-{ex['question']}")

