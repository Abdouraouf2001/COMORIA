import streamlit as st
from ia.assistant import repondre_question

def afficher_page_assistant():
    st.title("Assistant IA")
    st.info("Version de test : les reponses sont simulees pour l'instant.")

    if "historique_chat" not in st.session_state:
        st.session_state.historique_chat = []

    for message in st.session_state.historique_chat:
        with st.chat_message(message["role"]):
            st.write(message["contenu"])

    question = st.chat_input("Pose ta question ici...")

    if question:
        st.session_state.historique_chat.append(
            {"role": "user", "contenu": question}
        )
        with st.chat_message("user"):
            st.write(question)

        reponse = repondre_question(question)
        st.session_state.historique_chat.append(
            {"role": "assistant", "contenu": reponse}
        )
        with st.chat_message("assistant"):
            st.write(reponse)



    st.markdown("""
        <div class="footer-apropos">
              <strong>ComorIA</strong> — L'IA au service de l'éducation aux Comores
            <br>
            Une initiative portée par Abdouraouf Ahamada Saroumaya (Guilbert)
                <br>
                   2026 ComorIA . Tous droits reserves
        </div
        """, unsafe_allow_html=True)