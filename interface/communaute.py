

import streamlit as st
from database.operations import (
    creer_publication_db,
    obtenir_publications_db,
    utilisateur_a_like_db,
    basculer_like_db,
    supprimer_publication_db,
)


def afficher_page_communaute():

    st.markdown("""
    <style>
        .communaute-header {
            padding: 25px;
            border-radius: 18px;
            background: linear-gradient(135deg, #00843D, #006B32);
            color: white;
            margin-bottom: 25px;
        }
        .communaute-header h1 { margin: 0; font-size: 32px; }
        .communaute-header p { margin-top: 8px; font-size: 16px; opacity: 0.95; }
        .publication {
            padding: 20px;
            border-radius: 15px;
            background: #FFFFFF;
            border: 1px solid #E5E7EB;
            margin-bottom: 15px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        }
        .publication-auteur { font-weight: 700; color: #00843D; font-size: 16px; }
        .publication-date { color: #6B7280; font-size: 12px; }
        .publication-categorie {
            display: inline-block;
            padding: 4px 10px;
            border-radius: 20px;
            background: #F5F7F7;
            color: #00843D;
            font-size: 12px;
            font-weight: 600;
            margin-top: 8px;
        }
        .publication-contenu { margin-top: 15px; font-size: 15px; line-height: 1.6; color: #1F2937; }
        .info-box {
            padding: 18px;
            border-radius: 15px;
            background: #F5F7F7;
            border-left: 5px solid #FFC72C;
            margin-bottom: 20px;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="communaute-header">
        <h1>🌍 Communaute ComorIA</h1>
        <p>Un espace pour apprendre, echanger et partager entre eleves et enseignants.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
        <strong>💡 Bienvenue dans la communaute !</strong><br>
        Pose tes questions, partage tes connaissances et echange avec
        les autres membres de ComorIA dans le respect et la bienveillance.
    </div>
    """, unsafe_allow_html=True)

    utilisateur = st.session_state.get("nom_utilisateur", "Utilisateur")
    role = st.session_state.get("role", "eleve")

    noms_roles = {
        "eleve": "👨‍🎓 Eleve",
        "professeur": "👨‍🏫 Professeur",
        "admin": "🛡️ Administrateur"
    }
    role_affiche = noms_roles.get(role, "👤 Utilisateur")

    publications_toutes = obtenir_publications_db()

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("📝 Publications", len(publications_toutes))
    with col2:
        st.metric("👥 Membres", "—")
    with col3:
        st.metric("💬 Discussions", len(publications_toutes))

    st.markdown("---")

    st.subheader("✍️ Creer une publication")

    with st.form("formulaire_publication", clear_on_submit=True):

        st.caption(f"Publication en tant que : **{utilisateur} — {role_affiche}**")

        categorie = st.selectbox(
            "Categorie",
            ["📚 Etudes", "❓ Question", "💡 Astuce", "🧠 Revision",
             "🎓 Enseignement", "📢 Annonce", "💬 Discussion"]
        )

        contenu = st.text_area(
            "Votre publication",
            placeholder="Ecrivez votre question, votre idee ou partagez une connaissance...",
            height=130
        )

        publier = st.form_submit_button("🚀 Publier", use_container_width=True)

        if publier:
            if not contenu.strip():
                st.warning("⚠️ Veuillez ecrire quelque chose avant de publier.")
            else:
                creer_publication_db(utilisateur, role_affiche, categorie, contenu.strip())
                st.success("✅ Publication creee avec succes !")
                st.rerun()

    st.markdown("---")

    st.subheader("🔎 Publications")

    col1, col2 = st.columns([2, 1])
    with col1:
        recherche = st.text_input("Rechercher", placeholder="🔍 Rechercher une publication...")
    with col2:
        filtre = st.selectbox(
            "Categorie",
            ["Toutes", "📚 Etudes", "❓ Question", "💡 Astuce", "🧠 Revision",
             "🎓 Enseignement", "📢 Annonce", "💬 Discussion"]
        )

    publications_filtrees = obtenir_publications_db(recherche=recherche, categorie=filtre)

    if not publications_filtrees:
        st.info("🔍 Aucune publication ne correspond a votre recherche.")
    else:
        for publication in publications_filtrees:

            publication_id = publication["id"]

            st.markdown(f"""
                <div class="publication">
                    <div class="publication-auteur">👤 {publication['auteur']}</div>
                    <div class="publication-date">{publication['role']} • {publication['date']}</div>
                    <div class="publication-categorie">{publication['categorie']}</div>
                    <div class="publication-contenu">{publication['contenu']}</div>
                </div>
            """, unsafe_allow_html=True)

            col1, col2, col3 = st.columns([1, 1, 4])

            with col1:
                deja_like = utilisateur_a_like_db(publication_id, utilisateur)
                bouton = "❤️ Aime" if deja_like else "🤍 J'aime"

                if st.button(bouton, key=f"like_{publication_id}"):
                    basculer_like_db(publication_id, utilisateur)
                    st.rerun()

            with col2:
                st.write(f"❤️ {publication['likes']}")

            with col3:
                if publication["auteur"] == utilisateur:
                    if st.button("🗑️ Supprimer", key=f"supprimer_{publication_id}"):
                        supprimer_publication_db(publication_id, utilisateur)
                        st.success("Publication supprimee.")
                        st.rerun()

            st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("---")

    with st.expander("📜 Regles de la communaute"):
        st.markdown("""
        ### 🤝 Respect
        Respectez les autres membres de la communaute.

        ### 📚 Education
        Les publications doivent rester principalement liees a l'education, aux etudes ou a la vie scolaire.

        ### 🚫 Pas de contenu offensant
        Les insultes, discriminations, menaces et contenus inappropries ne sont pas autorises.

        ### 💡 Partage
        N'hesitez pas a partager vos connaissances, vos methodes de travail et vos conseils.

        ### 🛡️ Moderation
        Les administrateurs pourront moderer les publications et supprimer les contenus qui ne respectent pas les regles.
        """)
