import streamlit as st
from fonction.apropos import compter_utilisateurs, compter_cours, compter_matieres, compter_quiz
from database.operations import enregistrer_message_contact

def afficher_page_apropos():
    st.title("À propos de nous")

    st.markdown("""
    ### À propos du fondateur

    

Je m’appelle Abdouraouf Ahamada Saroumaya, dit Guilbert. Je suis étudiant en Master en Intelligence Artificielle à Midocean University, passionné par les nouvelles technologies, l’intelligence artificielle et l’enseignement.

Mon parcours m’a permis de développer un intérêt particulier pour le domaine de l’IA, tout en conservant une forte passion pour la transmission des connaissances et l’accompagnement des élèves. Mon expérience dans l’enseignement m’a notamment permis de comprendre certaines difficultés rencontrées par les apprenants et l’importance d’un accompagnement pédagogique adapté.

C’est cette double passion — l’intelligence artificielle et l’enseignement — qui m’a donné l’idée de créer ComorIA, une plateforme éducative pensée pour les élèves comoriens.

À travers ComorIA, mon objectif est de mettre les possibilités offertes par l’intelligence artificielle au service de l’éducation aux Comores, en proposant un accompagnement moderne, accessible, interactif et adapté au contexte éducatif comorien.

ComorIA est donc né d’une vision simple : utiliser l’IA pour rendre l’apprentissage plus accessible et contribuer à construire une éducation numérique adaptée aux besoins des élèves comoriens.
  
    
    """)

    st.markdown("""
    ### Notre mission

    Comoria a pour objectif d'**améliorer la manière dont les élèves comoriens appréhendent leurs cours**, en leur donnant accès à un **conseiller IA disponible 24h/24** pour leur expliquer les notions difficiles, répondre à leurs questions et les accompagner à tout moment.

    On veut qu'aucun élève ne reste bloqué sur une question faute d'avoir quelqu'un pour lui expliquer, où qu'il soit et quelle que soit l'heure.
    """)

    st.markdown("### En chiffres")
    col1, col2, col3, col4 = st.columns(4)
