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