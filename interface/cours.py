
import streamlit as st
from fonction.cours import charger_cours, obtenir_niveaux, obtenir_matieres, obtenir_cours
from config.colors import primaryColor, secondaryColor, secondaryTextColor


def afficher_page_cours():

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
<p class="cours-titre">📚 Choisis ton cours</p>
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
        niveau = st.selectbox("🎓 Ton niveau :", niveaux)

    matieres = obtenir_matieres(cours, niveau)

    if not matieres:
        st.warning("Aucune matière disponible pour ce niveau.")
        return

    with st.container(border=True):
        matiere = st.selectbox("📖 Matière :", matieres)

    resultats = obtenir_cours(cours, niveau, matiere)

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

    for c in resultats:
        chapitre = c.get("chapitre", "Chapitre sans titre")
        with st.expander(f"📘 {chapitre}"):
            st.write(c.get("contenu", ""))

            if "exercices" in c and c["exercices"]:
                st.markdown("### 📝 Exercices")
                for ex in c["exercices"]:
                    st.write(f"- {ex.get('question', 'Question non disponible')}")



# import streamlit as st
# from fonction.cours import  charger_cours, obtenir_niveaux, obtenir_matieres, obtenir_cours 

# def afficher_page_cours():

#     st.title("📚 Choisis ton cours")
#     cours = charger_cours()

#     if not cours:
#         st.warning("Aucun cours disponible.")
#         return
#     niveaux = obtenir_niveaux(cours)
#     if not niveaux:
#         st.warning("Aucun niveau disponible.")
#         return
#     niveau = st.selectbox(
#         "🎓 Ton niveau :",
#         niveaux
#     )
#     matieres = obtenir_matieres(cours, niveau)
#     if not matieres:
#         st.warning("Aucune matière disponible pour ce niveau.")
#         return
#     matiere = st.selectbox(
#         "📖 Matière :",
#         matieres
#     )

#     resultats = obtenir_cours(
#         cours,
#         niveau,
#         matiere
#     )

#     if not resultats:
#         st.info("Aucun cours trouvé pour cette sélection.")
#         return

#     # Afficher les cours
#     for c in resultats:

#         chapitre = c.get("chapitre", "Chapitre sans titre")

#         with st.expander(f"📘 {chapitre}"):

#             st.write(c.get("contenu", ""))

#             if "exercices" in c and c["exercices"]:

#                 st.markdown("### 📝 Exercices")

#                 for ex in c["exercices"]:
#                     st.write(
#                         f"- {ex.get('question', 'Question non disponible')}"
#                     )




# # import streamlit as st
# # from fonction.cours import charger_cours, obtenir_niveaux, obtenir_matieres, obtenir_cours

# # def afficher_page_cours():
# #     st.title("Choisis ton cours")

# #     cours = charger_cours()
# #     niveau = st.selectbox("ton niveau:", obtenir_niveaux(cours))
# #     matiers= st.selectbox("Matiere:",obtenir_matieres(cours , niveau))

# #     resultats = obtenir_cours(cours,niveau,matiers)
# #     for c in resultats:
# #         with st.expander(f"{c['chapitre']}"):
# #             st.write(c["contenu"])

# #             if "exercices" in c :
# #                st.markdown("***Exercices : ***")
# #                for ex in c["exercices"]:
# #                    st.write(f"-{ex['question']}")

