import streamlit as st
from database.models import creer_tables
from config.couleurs import COULEUR_PRINCIPALE, COULEUR_FOND, COULEUR_TEXTE_SECONDAIRE
from interface.connexion import afficher_page_connexion
from interface.accueil import afficher_accueil
from interface.cours import afficher_page_cours
from interface.programme import afficher_page_programme
from interface.quiz import afficher_page_quiz
from interface.assistant_ia import afficher_page_assistant
creer_tables()

st.set_page_config(
    page_title="Comoros AI Tuto",
    page_icon="📚",
    layout="wide"
)

if "connecte" not in st.session_state:
    st.session_state.connecte = False

if not st.session_state.connecte:
    afficher_page_connexion()
else:
    st.markdown(f"""
    <style>
        .stApp {{
            background-color: {COULEUR_FOND};
        }}
        .en-tete-app {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1rem 1.5rem;
            background: white;
            border-radius: 12px;
            margin-bottom: 1.5rem;
            border-bottom: 3px solid {COULEUR_PRINCIPALE};
        }}
        .stButton > button {{
            background-color: {COULEUR_PRINCIPALE};
            color: white;
            border-radius: 6px;
            border: none;
        }}
    </style>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="en-tete-app">
        <div>
            <span style="font-size:20px; font-weight:600; color:{COULEUR_PRINCIPALE};">📚 Comoros AI Tuto</span>
        </div>
        <div style="text-align:right;">
            <span style="font-size:14px; color:#333;">{st.session_state.nom_utilisateur}</span>
            <span style="font-size:12px; color:{COULEUR_TEXTE_SECONDAIRE};"> — {st.session_state.role}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.sidebar.title("Menu")

    if st.sidebar.button("Se deconnecter"):
        st.session_state.connecte = False
        st.rerun()

    st.sidebar.markdown("---")

    if "page_forcee" in st.session_state:
        page = st.session_state.page_forcee
        del st.session_state.page_forcee
    else:
        page = st.sidebar.radio("Navigation", ["Accueil", "Cours", "Programme officiel", "Quiz", "Assistant IA"])

    col_gauche, col_centre, col_droite = st.columns([1, 6, 1])
    with col_centre:
        if page == "Accueil":
            afficher_accueil()
        elif page == "Cours":
            afficher_page_cours()
        elif page == "Programme officiel":
            afficher_page_programme()
        elif page == "Quiz":
            afficher_page_quiz()
        elif page == "Assistant IA":
            afficher_page_assistant()





# import streamlit as st
# from interface.accueil import afficher_accueil
# from interface.connexion import afficher_page_connexion
# from interface.cours import afficher_page_cours
# from interface.quiz import afficher_page_quiz
# from interface.assistant_ia import afficher_page_assistant
# from interface.programme import afficher_page_programme
# from database.models import creer_tables
# creer_tables()


# st.set_page_config(
#     page_title="Comoros AI Tuto",
#     page_icon="📚",
#     layout="wide"
# )

# st.markdown("""
# <style>
#     .stApp {
#         font-family: 'Segoe UI', sans-serif;
#     }
#     h1 {
#         color: #00843D;
#         border-bottom: 3px solid #FFC72C;
#         padding-bottom: 8px;
#     }
#     h2, h3 {
#         color: #00843D;
#     }
#     [data-testid="stSidebar"] {
#         background-color: #F5F7F5;
#         border-right: 2px solid #00843D;
#     }
#     .stButton > button {
#         background-color: #00843D;
#         color: white;
#         border-radius: 6px;
#         border: none;
#     }
#     .stButton > button:hover {
#         background-color: #006B31;
#     }
# </style>
# """, unsafe_allow_html=True)
# if "connecte" not in st.session_state:
#     st.session_state.connecte = False
# if not st.session_state.connecte:
#     afficher_page_connexion()
# else:
#     st.sidebar.title("Menu")
#     st.sidebar.write(f"Connecte en tant que : **{st.session_state.nom_utilisateur}**")
#     st.sidebar.write(f"Role : {st.session_state.role}")

#     if st.sidebar.button("Se deconnecter"):
#        st.session_state.connecte = False
#        st.rerun()

#        st.sidebar.markdown("----")

#        st.sidebar.title("Menu")
#     page=st.sidebar.radio("Navigation", ["Accueil","Cours","Programme officiel","Quiz","Assistant IA"])
#     if page=="Accueil":
#         afficher_accueil()
#     elif page == "Cours":
#         afficher_page_cours()
#     elif page =="Programme officiel":
#         afficher_page_programme()
#     elif page == "Quiz": 
#         afficher_page_quiz()
#     elif page == "Assistant IA":
#         afficher_page_assistant()

