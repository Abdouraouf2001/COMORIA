from interface.apropos import afficher_page_apropos
from database.operations import creer_table_messages
import streamlit as st
from database.models import creer_tables
from config.colors import primaryColor, backgroundColor, secondaryTextColor
from interface.connexion import afficher_page_connexion
from interface.accueil import afficher_accueil
from interface.cours import afficher_page_cours
from interface.programme import afficher_page_programme
from interface.quiz import afficher_page_quiz
from interface.assistant_ia import afficher_page_assistant

creer_tables()
creer_table_messages()


st.set_page_config(
    page_title="Comoros AI Tuto",
    page_icon="📚",
    layout="centered",
    initial_sidebar_state="collapsed"
)

if "connecte" not in st.session_state:
    st.session_state.connecte = False

if not st.session_state.connecte:
    afficher_page_connexion()
else:
    st.markdown(f"""
    <style>
    .stApp {{
        background-color: {backgroundColor};
    }}
    .login-card {{
        background-color: white;
        border-radius: 20px;
        padding: 40px 30px;
        max-width: 380px;
        margin: 60px auto;
        text-align: center;
        box-shadow: 0 2px 12px rgba(0,0,0,0.08);
    }}
    .login-card h1 {{
        color: {primaryColor};
        font-size: 24px;
        margin-bottom: 8px;
    }}
    .login-card p {{
        color: #555;
        font-size: 14px;
        margin-bottom: 20px;
    }}
    .stTextInput input {{
        border-radius: 10px !important;
        padding: 12px !important;
        background-color: #F0F5F3 !important;
    }}
    .stButton button {{
        background-color: {primaryColor} !important;
        color: white !important;
        border-radius: 10px !important;
        padding: 12px !important;
        font-weight: bold !important;
        width: 100%;
    }}
    @media (max-width: 600px) {{
        .login-card {{
            margin: 30px 16px;
            padding: 30px 20px;
        }}
    }}
    </style>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="en-tete-app">
        <div>
            <span style="font-size:20px; font-weight:600; color:{primaryColor};">📚 Comoros AI Tuto</span>
        </div>
        <div style="text-align:right;">
            <span style="font-size:14px; color:#333;">{st.session_state.nom_utilisateur}</span>
            <span style="font-size:12px; color:{secondaryTextColor};"> — {st.session_state.role}</span>
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
        page = st.sidebar.radio("Navigation", ["Accueil", "Cours", "Programme officiel", "Quiz", "Assistant IA", "A propos"])

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
        elif page=="A propos":
            afficher_page_apropos()
 