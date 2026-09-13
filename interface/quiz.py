
import streamlit as st
from fonction.quiz import charger_quiz, obtenir_questions, corriger_reponse
from fonction.cours import obtenir_niveaux, obtenir_matieres, charger_cours

def afficher_page_quiz():
    st.title("Quiz")

    cours = charger_cours()
    quiz = charger_quiz()

    niveau = st.selectbox("Ton niveau :", obtenir_niveaux(cours))
    matiere = st.selectbox("Matiere :", obtenir_matieres(cours, niveau))

    questions = obtenir_questions(quiz, niveau, matiere)

    if not questions:
        st.warning("Pas de quiz disponible pour ce choix.")
        return

    if "index_question" not in st.session_state:
        st.session_state.index_question = 0
        st.session_state.score = 0

    if st.session_state.index_question < len(questions):
        question = questions[st.session_state.index_question]
        st.subheader(question["question"])
        reponse = st.radio("Choisis :", question["choix"])

        if st.button("Valider"):
            if corriger_reponse(question, reponse):
                st.success("Bonne reponse !")
                st.session_state.score += 1
            else:
                st.error(f"Faux, la bonne reponse etait : {question['bonne_reponse']}")
            st.session_state.index_question += 1
    else:
        st.write(f"Quiz termine ! Score : {st.session_state.score}/{len(questions)}")
        if st.button("Recommencer"):
            st.session_state.index_question = 0
            st.session_state.score = 0

