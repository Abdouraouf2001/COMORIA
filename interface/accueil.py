import streamlit as st


def afficher_accueil():
    """Affiche la page d'accueil de Comoros AI Tuto."""
    st.title("Comoros AI Tuto")
    st.subheader("🎓 Votre tuteur numérique pour apprendre autrement")
    st.write(
        """
        Bienvenue sur **Comoros AI Tuto**,une plateforme éducative
        destinée à accompagner les élèves dans leur apprentissage.

        📚 Accédez aux cours et aux leçons  
        📝 Testez vos connaissances avec les quiz  
        🔎 Recherchez rapidement un cours  
        🤖 Posez vos questions à l'assistant IA
        """
    )
    st.divider()
    st.subheader("🚀 Que souhaitez-vous faire ?")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("📚 Cours")
        st.write("Consultez les cours disponibles.")
    with col2:
        st.markdown("📝 Quiz")
        st.write("Testez vos connaissances.")
    with col3:
        st.markdown("🤖 Assistant IA")
        st.write("Posez vos questions à l'IA.")
    st.divider()
    st.info(
        "💡 Choisissez une rubrique dans le menu pour commencer votre apprentissage."
    )
