import streamlit as st
from fonction.apropos import compter_utilisateurs, compter_cours, compter_matieres, compter_quiz
from database.operations import enregistrer_message_contact

def afficher_page_apropos():
    st.markdown("""
    <style>
        .carte-apropos {
            background-color: white;
            border-radius: 20px;
            padding: 1.5rem 2rem;
            margin-bottom: 1.5rem;
        }
    </style>
    """, unsafe_allow_html=True)

    st.title("À propos de nous")

    with st.container(border=True):
        st.markdown("### À propos de moi")
        st.markdown("""
        Je m'appelle **Abdouraouf Ahamada**, dit **Guilbert**, étudiant en **Master d'IA et enseignement de mathématiques-physique**.

        C'est cette double formation — entre intelligence artificielle et enseignement des mathématiques et de la physique — qui m'a donné envie de créer Comoria : allier ma passion pour l'IA et mon expérience de l'enseignement pour offrir aux élèves comoriens un accompagnement pédagogique moderne et accessible.
        """)

    with st.container(border=True):
        st.markdown("### Notre mission")
        st.markdown("""
        Comoria a pour objectif d'**améliorer la manière dont les élèves comoriens appréhendent leurs cours**, en leur donnant accès à un **conseiller IA disponible 24h/24** pour leur expliquer les notions difficiles, répondre à leurs questions et les accompagner à tout moment.

        On veut qu'aucun élève ne reste bloqué sur une question faute d'avoir quelqu'un pour lui expliquer, où qu'il soit et quelle que soit l'heure.
        """)

    with st.container(border=True):
        st.markdown("### En chiffres")
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Utilisateurs", compter_utilisateurs())
        col2.metric("Chapitres", compter_cours())
        col3.metric("Matières", compter_matieres())
        col4.metric("Quiz", compter_quiz())

    with st.container(border=True):
        st.markdown("### Nous contacter")
        with st.form("formulaire_contact"):
            nom = st.text_input("Ton nom")
            email = st.text_input("Ton email")
            message = st.text_area("Ton message")
            envoyer = st.form_submit_button("Envoyer", use_container_width=True)

            if envoyer:
                if not nom or not email or not message:
                    st.warning("Remplis tous les champs.")
                else:
                    enregistrer_message_contact(nom, email, message)
                    st.success("Message envoyé ! Merci, on te répondra bientôt.")
