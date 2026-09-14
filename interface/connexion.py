import streamlit as st
from database.operations import inscrire_utilisateur_db, verifier_connexion_db
from config.colors import primaryColor, backgroundColor, secondaryTextColor

def afficher_page_connexion():
    st.markdown("""
    <style>
        .stApp {
            background-color: #E8F0EA;
        }
        div[data-testid="stVerticalBlockBorderWrapper"] {
            background-color: white;
            border-radius: 20px;
            padding: 1rem;
        }
    </style>
    """, unsafe_allow_html=True)

    col_gauche, col_centre, col_droite = st.columns([1, 2, 1])

    with col_centre:
        with st.container(border=True):
            st.markdown(f"""
            <div style="text-align:center; padding: 1rem 0 0.5rem 0;">
                <h2 style="color:{primaryColor}; margin:0;">Salama ! Bonjour !</h2>
                <p style="color:{secondaryTextColor}; font-size:14px; margin-top:6px;">
                    Connecte-toi pour retrouver tes cours et tes progres.
                </p>
            </div>
            """, unsafe_allow_html=True)

            onglet_connexion, onglet_inscription = st.tabs(["Se connecter", "S'inscrire"])

            with onglet_connexion:
                nom = st.text_input("Nom d'utilisateur", key="nom_connexion", placeholder="Ton prenom ou pseudo")
                mot_de_passe = st.text_input("Mot de passe", type="password", key="mdp_connexion")

                if st.button("Commencer", use_container_width=True, key="btn_connexion"):
                    if not nom or not mot_de_passe:
                        st.warning("Remplis tous les champs.")
                    else:
                        succes, role = verifier_connexion_db(nom, mot_de_passe)
                        if succes:
                            st.session_state.connecte = True
                            st.session_state.nom_utilisateur = nom
                            st.session_state.role = role
                            st.success(f"Bienvenue, {nom} !")
                            st.rerun()
                        else:
                            st.error("Nom d'utilisateur ou mot de passe incorrect.")

            with onglet_inscription:
                nouveau_nom = st.text_input("Choisis un nom d'utilisateur", key="nom_inscription")
                nouveau_mdp = st.text_input("Choisis un mot de passe", type="password", key="mdp_inscription")
                role = st.selectbox("Tu es :", ["eleve", "professeur"])

                if st.button("Commencer", use_container_width=True, key="btn_inscription"):
                    if not nouveau_nom or not nouveau_mdp:
                        st.warning("Remplis tous les champs.")
                    else:
                        succes, message = inscrire_utilisateur_db(nouveau_nom, nouveau_mdp, role)
                        if succes:
                            st.success(message)
                        else:
                            st.error(message)
