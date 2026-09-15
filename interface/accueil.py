import streamlit as st
from config.colors import primaryColor, textColor, secondaryColor


def afficher_accueil():

    st.markdown(
        f"""
<style>
.hero {{
background: linear-gradient(135deg, {primaryColor}, {textColor});
padding: 28px 20px;
border-radius: 20px;
color: white;
text-align: center;
margin-bottom: 20px;
}}
.hero h1 {{
font-size: 32px;
margin-bottom: 8px;
}}
.hero p {{
font-size: 16px;
margin: 0;
}}
.welcome {{
background-color: white;
padding: 20px;
border-radius: 16px;
margin-bottom: 20px;
box-shadow: 0 2px 10px rgba(0,0,0,0.06);
}}
.feature-card {{
background-color: white;
padding: 20px;
border-radius: 16px;
min-height: 150px;
margin-bottom: 15px;
box-shadow: 0 2px 10px rgba(0,0,0,0.06);
text-align: center;
}}
.feature-icon {{
font-size: 32px;
margin-bottom: 8px;
}}
.feature-title {{
font-size: 18px;
font-weight: 700;
margin-bottom: 8px;
color: {primaryColor};
}}
.feature-text {{
font-size: 14px;
color: #666;
}}
.info-box {{
background-color: #EAF3DE;
padding: 16px;
border-radius: 14px;
text-align: center;
margin-top: 10px;
color: {secondaryColor};
}}
@media (max-width: 768px) {{
.hero {{
padding: 24px 15px;
border-radius: 16px;
}}
.hero h1 {{
font-size: 25px;
}}
.hero p {{
font-size: 14px;
}}
.welcome {{
padding: 16px;
border-radius: 14px;
}}
.feature-card {{
padding: 18px;
min-height: 130px;
}}
.feature-icon {{
font-size: 28px;
}}
.feature-title {{
font-size: 17px;
}}
.feature-text {{
font-size: 13px;
}}
}}
</style>
""",
        unsafe_allow_html=True
    )

    nom = st.session_state.get("nom_utilisateur", "Élève")

    st.markdown(
        f"""
<div class="hero">
<h1>🇰🇲 ComorIA</h1>
<p>Votre plateforme éducative intelligente</p>
</div>
""",
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
<div class="welcome">
<h3>👋 Bienvenue, {nom} !</h3>
<p>Apprenez, entraînez-vous et progressez avec ComorIA.</p>
</div>
""",
        unsafe_allow_html=True
    )

    st.subheader("🚀 Que souhaitez-vous faire ?")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
<div class="feature-card">
<div class="feature-icon">📚</div>
<div class="feature-title">Cours</div>
<div class="feature-text">Consultez vos cours et développez vos connaissances.</div>
</div>
""",
            unsafe_allow_html=True
        )
        if st.button("📚 Ouvrir les cours", use_container_width=True):
            st.session_state.page_forcee = "Cours"
            st.rerun()

    with col2:
        st.markdown(
            """
<div class="feature-card">
<div class="feature-icon">📝</div>
<div class="feature-title">Quiz</div>
<div class="feature-text">Testez vos connaissances et mesurez vos progrès.</div>
</div>
""",
            unsafe_allow_html=True
        )
        if st.button("📝 Faire un quiz", use_container_width=True):
            st.session_state.page_forcee = "Quiz"
            st.rerun()

    col3, col4 = st.columns(2)

    with col3:
        st.markdown(
            """
<div class="feature-card">
<div class="feature-icon">📖</div>
<div class="feature-title">Programmes officiels</div>
<div class="feature-text">Consultez les programmes scolaires officiels.</div>
</div>
""",
            unsafe_allow_html=True
        )
        if st.button("📖 Voir les programmes", use_container_width=True):
            st.session_state.page_forcee = "Programme officiel"
            st.rerun()

    with col4:
        st.markdown(
            """
<div class="feature-card">
<div class="feature-icon">🤖</div>
<div class="feature-title">Assistant IA</div>
<div class="feature-text">Posez vos questions et obtenez de l'aide.</div>
</div>
""",
            unsafe_allow_html=True
        )
        if st.button("🤖 Ouvrir l'assistant", use_container_width=True):
            st.session_state.page_forcee = "Assistant IA"
            st.rerun()

    st.markdown(
        """
<div class="info-box">
💡 <strong>Conseil :</strong> choisissez une rubrique ci-dessus pour commencer votre apprentissage.
</div>
""",
        unsafe_allow_html=True
    )
     
          







# import streamlit as st


# def afficher_accueil():

#     st.markdown(
#         """
#         <style>

#         .hero {
#             background: linear-gradient(
#                 135deg,
#                 #00843D,
#                 #00A651
#             );
#             padding: 28px 20px;
#             border-radius: 20px;
#             color: white;
#             text-align: center;
#             margin-bottom: 20px;
#         }

#         .hero h1 {
#             font-size: 32px;
#             margin-bottom: 8px;
#         }

#         .hero p {
#             font-size: 16px;
#             margin: 0;
#         }

#         .welcome {
#             background-color: white;
#             padding: 20px;
#             border-radius: 16px;
#             margin-bottom: 20px;
#             box-shadow: 0 2px 10px rgba(0,0,0,0.06);
#         }

#         .feature-card {
#             background-color: white;
#             padding: 20px;
#             border-radius: 16px;
#             min-height: 150px;
#             margin-bottom: 15px;
#             box-shadow: 0 2px 10px rgba(0,0,0,0.06);
#             text-align: center;
#         }

#         .feature-icon {
#             font-size: 32px;
#             margin-bottom: 8px;
#         }

#         .feature-title {
#             font-size: 18px;
#             font-weight: 700;
#             margin-bottom: 8px;
#         }

#         .feature-text {
#             font-size: 14px;
#             color: #666;
#         }

#         .info-box {
#             background-color: #F0F5F3;
#             padding: 16px;
#             border-radius: 14px;
#             text-align: center;
#             margin-top: 10px;
#         }

#         @media (max-width: 768px) {

#             .hero {
#                 padding: 24px 15px;
#                 border-radius: 16px;
#             }

#             .hero h1 {
#                 font-size: 25px;
#             }

#             .hero p {
#                 font-size: 14px;
#             }

#             .welcome {
#                 padding: 16px;
#                 border-radius: 14px;
#             }

#             .feature-card {
#                 padding: 18px;
#                 min-height: 130px;
#             }

#             .feature-icon {
#                 font-size: 28px;
#             }

#             .feature-title {
#                 font-size: 17px;
#             }

#             .feature-text {
#                 font-size: 13px;
#             }
#         }

#         </style>
#         """,
#         unsafe_allow_html=True
#     )

#     nom = st.session_state.get(
#         "nom_utilisateur",
#         "Élève"
#     )

#     st.markdown(
#         f"""
#         <div class="hero">

#             <h1>🇰🇲 ComorIA</h1>

#             <p>
#                 Votre plateforme éducative intelligente
#             </p>

#         </div>
#         """,
#         unsafe_allow_html=True
#     )

#     st.markdown(
#         f"""
#         <div class="welcome">

#             <h3>👋 Bienvenue, {nom} !</h3>

#             <p>
#                 Apprenez, entraînez-vous et progressez
#                 avec ComorIA.
#             </p>

#         </div>
#         """,
#         unsafe_allow_html=True
#     )

#     st.subheader("🚀 Que souhaitez-vous faire ?")

#     col1, col2 = st.columns(2)

#     with col1:

#         st.markdown(
#             """
#             <div class="feature-card">

#                 <div class="feature-icon">
#                     📚
#                 </div>

#                 <div class="feature-title">
#                     Cours
#                 </div>

#                 <div class="feature-text">
#                     Consultez vos cours et
#                     développez vos connaissances.
#                 </div>

#             </div>
#             """,
#             unsafe_allow_html=True
#         )

#         if st.button(
#             "📚 Ouvrir les cours",
#             use_container_width=True
#         ):
#             st.session_state.page_forcee = "Cours"
#             st.rerun()

#     with col2:

#         st.markdown(
#             """
#             <div class="feature-card">

#                 <div class="feature-icon">
#                     📝
#                 </div>

#                 <div class="feature-title">
#                     Quiz
#                 </div>

#                 <div class="feature-text">
#                     Testez vos connaissances
#                     et mesurez vos progrès.
#                 </div>

#             </div>
#             """,
#             unsafe_allow_html=True
#         )

#         if st.button(
#             "📝 Faire un quiz",
#             use_container_width=True
#         ):
#             st.session_state.page_forcee = "Quiz"
#             st.rerun()

#     col3, col4 = st.columns(2)

#     with col3:

#         st.markdown(
#             """
#             <div class="feature-card">

#                 <div class="feature-icon">
#                     📖
#                 </div>

#                 <div class="feature-title">
#                     Programmes officiels
#                 </div>

#                 <div class="feature-text">
#                     Consultez les programmes
#                     scolaires officiels.
#                 </div>

#             </div>
#             """,
#             unsafe_allow_html=True
#         )

#         if st.button(
#             "📖 Voir les programmes",
#             use_container_width=True
#         ):
#             st.session_state.page_forcee = "Programme officiel"
#             st.rerun()

#     with col4:

#         st.markdown(
#             """
#             <div class="feature-card">

#                 <div class="feature-icon">
#                     🤖
#                 </div>

#                 <div class="feature-title">
#                     Assistant IA
#                 </div>

#                 <div class="feature-text">
#                     Posez vos questions et
#                     obtenez de l'aide.
#                 </div>

#             </div>
#             """,
#             unsafe_allow_html=True
#         )

#         if st.button(
#             "🤖 Ouvrir l'assistant",
#             use_container_width=True
#         ):
#             st.session_state.page_forcee = "Assistant IA"
#             st.rerun()

#     st.markdown(
#         """
#         <div class="info-box">

#             💡 <strong>Conseil :</strong>
#             choisissez une rubrique ci-dessus
#             pour commencer votre apprentissage.

#         </div>
#         """,
#         unsafe_allow_html=True
#     )





# # import streamlit as st


# # def afficher_accueil():
# #     """Affiche la page d'accueil de Comoros AI Tuto."""
# #     st.title("Comoros AI Tuto")
# #     st.subheader("🎓 Votre tuteur numérique pour apprendre autrement")
# #     st.write(
# #         """
# #         Bienvenue sur **Comoros AI Tuto**,une plateforme éducative
# #         destinée à accompagner les élèves dans leur apprentissage.

# #         📚 Accédez aux cours et aux leçons  
# #         📝 Testez vos connaissances avec les quiz  
# #         🔎 Recherchez rapidement un cours  
# #         🤖 Posez vos questions à l'assistant IA
# #         """
# #     )
# #     st.divider()
# #     st.subheader("🚀 Que souhaitez-vous faire ?")
# #     col1, col2, col3 = st.columns(3)
# #     with col1:
# #         st.markdown("📚 Cours")
# #         st.write("Consultez les cours disponibles.")
# #     with col2:
# #         st.markdown("📝 Quiz")
# #         st.write("Testez vos connaissances.")
# #     with col3:
# #         st.markdown("🤖 Assistant IA")
# #         st.write("Posez vos questions à l'IA.")
# #     st.divider()
# #     st.info(
# #         "💡 Choisissez une rubrique dans le menu pour commencer votre apprentissage."
# #     )
