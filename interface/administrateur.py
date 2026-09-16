import streamlit as st

from database.operations import (
    obtenir_utilisateurs,
    modifier_role_utilisateur,
    supprimer_utilisateur,
    compter_utilisateurs,
    compter_utilisateurs_par_role
)


def afficher_page_administrateur():

    st.title("🛡️ Administration ComorIA")

    st.caption(
        "Centre de gestion de la plateforme éducative"
    )

    st.divider()

    # =====================================================
    # NAVIGATION ADMINISTRATION
    # =====================================================

    section = st.radio(
        "📚 Gestion de la plateforme",
        [
            "📊 Tableau de bord",
            "👥 Utilisateurs",
            "📚 Contenus pédagogiques",
            "💬 Communauté",
            "🔬 Recherche scientifique",
            "📩 Messages",
            "⚙️ Paramètres"
        ],
        horizontal=True
    )

    st.divider()

    # =====================================================
    # TABLEAU DE BORD
    # =====================================================

    if section == "📊 Tableau de bord":

        st.subheader("📊 Tableau de bord")

        total = compter_utilisateurs()
        eleves = compter_utilisateurs_par_role("eleve")
        professeurs = compter_utilisateurs_par_role("professeur")
        administrateurs = compter_utilisateurs_par_role("admin")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "👥 Utilisateurs",
                total
            )

        with col2:
            st.metric(
                "👨‍🎓 Élèves",
                eleves
            )

        with col3:
            st.metric(
                "👨‍🏫 Professeurs",
                professeurs
            )

        with col4:
            st.metric(
                "🛡️ Administrateurs",
                administrateurs
            )

        st.divider()

        st.subheader("📈 État de la plateforme")

        col1, col2 = st.columns(2)

        with col1:

            with st.container(border=True):

                st.markdown("### 👥 Utilisateurs")

                st.write(
                    f"**{total}** utilisateur(s) "
                    "enregistré(s)."
                )

                st.write(
                    f"👨‍🎓 Élèves : **{eleves}**"
                )

                st.write(
                    f"👨‍🏫 Professeurs : **{professeurs}**"
                )

                st.write(
                    f"🛡️ Administrateurs : "
                    f"**{administrateurs}**"
                )

        with col2:

            with st.container(border=True):

                st.markdown("### 🏫 ComorIA")

                st.write(
                    "Plateforme éducative intelligente "
                    "destinée aux apprenants et enseignants."
                )

                st.write(
                    "🇰🇲 L'IA au service de "
                    "l'éducation aux Comores."
                )

    # =====================================================
    # UTILISATEURS
    # =====================================================

    elif section == "👥 Utilisateurs":

        st.subheader("👥 Gestion des utilisateurs")

        utilisateurs = obtenir_utilisateurs()

        if not utilisateurs:

            st.info(
                "Aucun utilisateur enregistré."
            )

        else:

            for utilisateur in utilisateurs:

                utilisateur_id = utilisateur["id"]
                nom = utilisateur["nom"]
                role = utilisateur["role"]

                with st.container(border=True):

                    col1, col2, col3 = st.columns(
                        [2, 2, 1]
                    )

                    with col1:

                        st.markdown(
                            f"### 👤 {nom}"
                        )

                    with col2:

                        nouveau_role = st.selectbox(
                            "Rôle",
                            [
                                "eleve",
                                "professeur",
                                "admin"
                            ],
                            index=[
                                "eleve",
                                "professeur",
                                "admin"
                            ].index(role)
                            if role in [
                                "eleve",
                                "professeur",
                                "admin"
                            ]
                            else 0,
                            key=f"role_{utilisateur_id}"
                        )

                    with col3:

                        if st.button(
                            "💾 Enregistrer",
                            key=f"modifier_{utilisateur_id}",
                            use_container_width=True
                        ):

                            modifier_role_utilisateur(
                                utilisateur_id,
                                nouveau_role
                            )

                            st.success(
                                "Rôle modifié."
                            )

                            st.rerun()

                    st.caption(
                        f"Rôle actuel : {role}"
                    )

                    if st.button(
                        "🗑️ Supprimer cet utilisateur",
                        key=f"supprimer_{utilisateur_id}"
                    ):

                        supprimer_utilisateur(
                            utilisateur_id
                        )

                        st.success(
                            "Utilisateur supprimé."
                        )

                        st.rerun()

    # =====================================================
    # CONTENUS
    # =====================================================

    elif section == "📚 Contenus pédagogiques":

        st.subheader(
            "📚 Gestion des contenus pédagogiques"
        )

        col1, col2 = st.columns(2)

        with col1:

            with st.container(border=True):

                st.markdown("### 📖 Cours")

                st.write(
                    "Gérer les cours disponibles "
                    "sur ComorIA."
                )

                st.button(
                    "📚 Gérer les cours",
                    use_container_width=True,
                    key="admin_cours"
                )

        with col2:

            with st.container(border=True):

                st.markdown("### 📝 Quiz")

                st.write(
                    "Gérer les quiz et évaluations."
                )

                st.button(
                    "📝 Gérer les quiz",
                    use_container_width=True,
                    key="admin_quiz"
                )

        col1, col2 = st.columns(2)

        with col1:

            with st.container(border=True):

                st.markdown("### 📑 Leçons")

                st.write(
                    "Gérer les leçons pédagogiques."
                )

                st.button(
                    "📑 Gérer les leçons",
                    use_container_width=True,
                    key="admin_lecons"
                )

        with col2:

            with st.container(border=True):

                st.markdown("### 🇰🇲 Programmes officiels")

                st.write(
                    "Gérer les programmes scolaires "
                    "officiels des Comores."
                )

                st.button(
                    "📚 Gérer les programmes",
                    use_container_width=True,
                    key="admin_programmes"
                )

    # =====================================================
    # COMMUNAUTÉ
    # =====================================================

    elif section == "💬 Communauté":

        st.subheader(
            "💬 Gestion de la communauté"
        )

        st.info(
            "Cette section permettra à l'administrateur "
            "de modérer les publications et discussions."
        )

        st.button(
            "🛡️ Ouvrir la modération",
            use_container_width=True,
            key="admin_communaute"
        )

    # =====================================================
    # RECHERCHE SCIENTIFIQUE
    # =====================================================

    elif section == "🔬 Recherche scientifique":

        st.subheader(
            "🔬 Recherche scientifique"
        )

        col1, col2 = st.columns(2)

        with col1:

            with st.container(border=True):

                st.markdown("### 📚 Ressources")

                st.write(
                    "Gérer les ressources scientifiques."
                )

                st.button(
                    "📚 Gérer les ressources",
                    use_container_width=True,
                    key="admin_ressources"
                )

        with col2:

            with st.container(border=True):

                st.markdown("### 🧪 Publications")

                st.write(
                    "Gérer les publications "
                    "scientifiques."
                )

                st.button(
                    "🧪 Gérer les publications",
                    use_container_width=True,
                    key="admin_publications"
                )

    # =====================================================
    # MESSAGES
    # =====================================================

    elif section == "📩 Messages":

        st.subheader(
            "📩 Messages de contact"
        )

        st.info(
            "Les messages envoyés depuis la plateforme "
            "seront affichés ici."
        )

    # =====================================================
    # PARAMÈTRES
    # =====================================================

    elif section == "⚙️ Paramètres":

        st.subheader(
            "⚙️ Paramètres de ComorIA"
        )

        st.write(
            "Configuration générale de la plateforme."
        )

        st.checkbox(
            "Activer les inscriptions",
            value=True
        )

        st.checkbox(
            "Activer la communauté",
            value=True
        )

        st.checkbox(
            "Activer l'assistant IA",
            value=True
        )

        st.info(
            "Les paramètres seront connectés "
            "à la base de données dans une prochaine étape."
        )
