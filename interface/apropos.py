import streamlit as st


def afficher_page_apropos():
    # ==============================
    # STYLE DE LA PAGE
    # ==============================
    st.markdown("""
    <style>
    .apropos-header {
        padding: 30px;
        border-radius: 20px;
        background: linear-gradient(135deg, #00843D, #006B32);
        color: white;
        margin-bottom: 30px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.10);
    }

    .apropos-header h1 {
        font-size: 38px;
        margin-bottom: 8px;
    }

    .apropos-header p {
        font-size: 18px;
        margin: 0;
        opacity: 0.95;
    }

    .section-title {
        font-size: 27px;
        font-weight: 700;
        margin-top: 25px;
        margin-bottom: 15px;
    }

    .founder-card {
        background: white;
        padding: 28px;
        border-radius: 18px;
        border: 1px solid #E5E7EB;
        box-shadow: 0 5px 18px rgba(0,0,0,0.06);
        line-height: 1.8;
        margin-bottom: 25px;
    }

    .mission-card {
        background: #F5F7F7;
        padding: 28px;
        border-radius: 18px;
        border-left: 6px solid #00843D;
        box-shadow: 0 5px 18px rgba(0,0,0,0.05);
        line-height: 1.8;
        margin-bottom: 30px;
    }

    .stat-card {
        background: white;
        padding: 22px 15px;
        border-radius: 16px;
        text-align: center;
        border: 1px solid #E5E7EB;
        box-shadow: 0 5px 15px rgba(0,0,0,0.06);
        min-height: 135px;
    }

    .stat-icon {
        font-size: 30px;
        margin-bottom: 5px;
    }

    .stat-number {
        font-size: 30px;
        font-weight: 800;
        color: #00843D;
    }

    .stat-label {
        font-size: 14px;
        color: #6B7280;
    }

    .vision-card {
        background: linear-gradient(135deg, #FFF8D8, #FFFDF2);
        padding: 28px;
        border-radius: 18px;
        border: 1px solid #F1D76A;
        margin-top: 30px;
        line-height: 1.8;
    }

    .values-card {
        background: white;
        padding: 24px;
        border-radius: 16px;
        border: 1px solid #E5E7EB;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05);
        min-height: 180px;
    }

    .values-card h4 {
        color: #00843D;
        margin-bottom: 10px;
    }

    .footer-apropos {
        text-align: center;
        padding: 30px 10px 10px 10px;
        color: #6B7280;
        font-size: 14px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="apropos-header">
        <h1>🇰🇲 À propos de ComorIA</h1>
        <p>
            L'intelligence artificielle au service de l'éducation comorienne.
        </p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown(
        '<div class="section-title">👨‍💻 À propos du fondateur</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="founder-card">

    <h3>Abdouraouf Ahamada Saroumaya, dit Guilbert</h3>

    <p>
    Je suis étudiant en <strong>Master en Intelligence Artificielle
    à Midocean University</strong>, passionné par les nouvelles
    technologies, l'intelligence artificielle et l'enseignement.
    </p>

    <p>
    Mon parcours m'a permis de développer un intérêt particulier pour
    le domaine de l'IA, tout en conservant une forte passion pour
    <strong>la transmission des connaissances et l'accompagnement des élèves</strong>.
    Mon expérience dans l'enseignement m'a notamment permis de comprendre
    certaines difficultés rencontrées par les apprenants et l'importance
    d'un accompagnement pédagogique adapté.
    </p>

    <p>
    C'est cette double passion — <strong>l'intelligence artificielle
    et l'enseignement</strong> — qui m'a donné l'idée de créer
    <strong>ComorIA</strong>, une plateforme éducative pensée pour
    les élèves comoriens.
    </p>

    <p>
    À travers ComorIA, mon objectif est de mettre les possibilités
    offertes par l'intelligence artificielle au service de
    <strong>l'éducation aux Comores</strong>, en proposant un
    accompagnement moderne, accessible, interactif et adapté au
    contexte éducatif comorien.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">🎯 Notre mission</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="mission-card">

    <p>
    ComorIA a pour objectif d'<strong>améliorer la manière dont les
    élèves comoriens appréhendent leurs cours</strong>, en leur donnant
    accès à un <strong>conseiller IA disponible 24h/24</strong> pour
    expliquer les notions difficiles, répondre à leurs questions et
    les accompagner dans leur apprentissage.
    </p>

    <p>
    Notre ambition est simple :
    <strong>qu'aucun élève ne reste bloqué sur une question faute
    d'avoir quelqu'un pour lui expliquer</strong>, où qu'il soit et
    quelle que soit l'heure.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">📊 ComorIA en quelques chiffres</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-icon">📚</div>
            <div class="stat-number">7+</div>
            <div class="stat-label">Matières scolaires</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-icon">🎓</div>
            <div class="stat-number">7+</div>
            <div class="stat-label">Niveaux scolaires</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-icon">🤖</div>
            <div class="stat-number">24/7</div>
            <div class="stat-label">Assistance IA</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-icon">🇰🇲</div>
            <div class="stat-number">100%</div>
            <div class="stat-label">Pensé pour les Comores</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">💡 Nos valeurs</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="values-card">
            <h4>🎓 Éducation</h4>
            <p>
            Mettre la technologie au service de l'apprentissage
            et de la réussite scolaire.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="values-card">
            <h4>🤖 Innovation</h4>
            <p>
            Exploiter l'intelligence artificielle pour créer
            de nouvelles expériences d'apprentissage.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="values-card">
            <h4>🇰🇲 Accessibilité</h4>
            <p>
            Concevoir une solution adaptée aux réalités et
            aux besoins des élèves comoriens.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">🚀 Notre vision</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="vision-card">

    <h3>Construire l'avenir de l'éducation aux Comores</h3>

    <p>
    Nous croyons que l'intelligence artificielle peut devenir un
    véritable outil d'accompagnement pédagogique lorsqu'elle est
    conçue pour répondre aux réalités locales.
    </p>

    <p>
    Avec ComorIA, nous voulons contribuer progressivement à une
    <strong>éducation numérique plus accessible, plus interactive
    et plus personnalisée</strong> pour les élèves comoriens.
    </p>

    <p>
    <strong>Notre ambition : apprendre autrement, grâce à la technologie,
    tout en restant proche des besoins de nos élèves.</strong>
    </p>

    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="footer-apropos">
          <strong>ComorIA</strong> — L'IA au service de l'éducation aux Comores
        <br>
        Une initiative portée par Abdouraouf Ahamada Saroumaya (Guilbert)
            <br>
               2026 ComorIA . Tous droits reserves
    </div
    """, unsafe_allow_html=True)



