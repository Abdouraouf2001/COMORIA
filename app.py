
from interface.apropos import afficher_page_apropos
from database.operations import creer_table_messages
import streamlit as st
from database.models import creer_tables
from config.colors import primaryColor,textColor , secondaryTextColor
from interface.connexion import afficher_page_connexion
from interface.accueil import afficher_accueil
from interface.cours import afficher_page_cours
from interface.programme import afficher_page_programme
from interface.quiz import afficher_page_quiz
from interface.assistant_ia import afficher_page_assistant


creer_tables()
creer_table_messages()


st.set_page_config(
    page_title="ComorIA",
    page_icon="🇰🇲",
    layout="wide",
    initial_sidebar_state="collapsed"
)


st.markdown(
    """
<link rel="manifest" href="./static/manifest.json">
<meta name="theme-color" content="#0D6EFD">
<link rel="apple-touch-icon" href="./static/icon-192.png">
""",
    unsafe_allow_html=True
)


if "connecte" not in st.session_state:
    st.session_state.connecte = False


if not st.session_state.connecte:

    afficher_page_connexion()

else:

    st.markdown(
        f"""
<style>
.stApp {{
background-color: {primaryColor};
}}
.block-container {{
max-width: 1100px;
padding-top: 1rem;
padding-left: 1rem;
padding-right: 1rem;
}}
.comoria-header {{
background-color: white;
border-radius: 16px;
padding: 14px 18px;
margin-bottom: 18px;
box-shadow: 0 2px 10px rgba(0,0,0,0.06);
display: flex;
align-items: center;
justify-content: space-between;
gap: 10px;
}}
.comoria-logo {{
color: {primaryColor};
font-size: 21px;
font-weight: 700;
}}
.comoria-user {{
text-align: right;
font-size: 14px;
color: #333;
}}
.comoria-role {{
color: {secondaryTextColor};
font-size: 12px;
}}
.stButton button {{
border-radius: 10px !important;
min-height: 42px !important;
font-weight: 600 !important;
}}
.stTextInput input,
.stTextArea textarea,
.stSelectbox div {{
border-radius: 10px !important;
}}
@media (max-width: 768px) {{
.block-container {{
padding-top: 0.5rem;
padding-left: 0.7rem;
padding-right: 0.7rem;
}}
.comoria-header {{
padding: 12px;
border-radius: 12px;
}}
.comoria-logo {{
font-size: 18px;
}}
.comoria-user {{
font-size: 12px;
}}
.comoria-role {{
font-size: 10px;
}}
h1 {{
font-size: 1.6rem !important;
}}
h2 {{
font-size: 1.35rem !important;
}}
h3 {{
font-size: 1.15rem !important;
}}
.stButton button {{
min-height: 45px !important;
}}
}}
@media (max-width: 400px) {{
.comoria-header {{
flex-direction: column;
align-items: flex-start;
}}
.comoria-user {{
text-align: left;
}}
}}
</style>
""",
        unsafe_allow_html=True
    )


    st.markdown(
        f"""
<div class="comoria-header">
<div class="comoria-logo">🇰🇲 ComorIA</div>
<div class="comoria-user">
👤 {st.session_state.nom_utilisateur}
<br>
<span class="comoria-role">{st.session_state.role}</span>
</div>
</div>
""",
        unsafe_allow_html=True
    )


    st.sidebar.title("🇰🇲 ComorIA")

    st.sidebar.caption(
        "Plateforme éducative intelligente"
    )

    st.sidebar.markdown("---")


    page = st.sidebar.radio(
        "📚 Navigation",
        [
            "Accueil",
            "Cours",
            "Programme officiel",
            "Quiz",
            "Assistant IA",
            "A propos"
        ]
    )


    st.sidebar.markdown("---")


    if st.sidebar.button(
        "🚪 Se déconnecter",
        use_container_width=True
    ):

        st.session_state.connecte = False

        st.rerun()


    if "page_forcee" in st.session_state:

        page = st.session_state.page_forcee

        del st.session_state.page_forcee


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


    elif page == "A propos":

        afficher_page_apropos()
