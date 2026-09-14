import streamlit as st
from fonction.apropos import compter_utilisateurs, compter_cours, compter_matieres, compter_quiz
from database.operations import enregistrer_message_contact

def afficher_page_apropos():
    st.title("À propos de nous")

    st.markdown("""
    ### À propos de moi

    Je m'appelle **Abdouraouf Ahamada**, dit **Guilbert**, chercheur en 'IA et enseignement de mathématiques-physique**.

    C'est cette double formation — entre intelligence artificielle et enseignement des mathématiques et de la physique — qui m'a donné envie de créer Comoria : allier ma passion pour l'IA et mon expérience de l'enseignement pour offrir aux élèves comoriens un accompagnement pédagogique moderne et accessible.
    """)

    st.markdown("""
    ### Notre mission

    Comoria a pour objectif d'**améliorer la manière dont les élèves comoriens appréhendent leurs cours**, en leur donnant accès à un **conseiller IA disponible 24h/24** pour leur expliquer les notions difficiles, répondre à leurs questions et les accompagner à tout moment.

    On veut qu'aucun élève ne reste bloqué sur une question faute d'avoir quelqu'un pour lui expliquer, où qu'il soit et quelle que soit l'heure.
    """)

    st.markdown("Nam karibou ! ")
    col1, col2, col3, col4 = st.columns(4)
