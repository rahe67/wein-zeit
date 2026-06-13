import streamlit as st

# 1. Seiteneinstellungen festlegen
st.set_page_config(
    page_title="Wein-Zeit",
    page_icon="🍷",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Weinrotes Design UND Ausblenden der weißen Leiste erzwingen
# Das sorgt dafür, dass die App IMMER dunkelrot bleibt – egal ob Embed-Modus oder nicht!
custom_style = """
    <style>
    /* Hintergrundfarbe auf das tiefe Weinrot/Dunkel setzen */
    .stApp {
        background-color: #1a0508 !important;
        color: #ffffff !important;
    }
    
    /* Komplettes Ausblenden der störenden Streamlit-Elemente */
    [data-testid="stStatusWidget"] {visibility: hidden !important; display: none !important;}
    footer {visibility: hidden !important; display: none !important;}
    .stAppDeployButton {visibility: hidden !important; display: none !important;}
    #MainMenu {visibility: hidden !important; display: none !important;}
    header {visibility: hidden !important; display: none !important;}
    stDecoration {visibility: hidden !important; display: none !important;}
    
    /* Die weiße Leiste am unteren Bildschirmrand im Embed-Modus eliminieren */
    [data-testid="stEmbedFooter"] {display: none !important; visibility: hidden !important;}
    footer, .st-emotion-cache-z5fcl4, .stEmbedFooter {display: none !important; visibility: hidden !important;}
    
    /* Sicherstellen, dass Texte in Eingabefeldern lesbar bleiben */
    .stSelectbox, .stRadio, p, h1, h2, h3 {
        color: #ffffff !important;
    }
    </style>
"""
st.markdown(custom_style, unsafe_allow_html=True)

# Premium placeholder wine menu data
WINE_DATA = {
    "Weißwein": [
        {
            "name": "Sommerwind Riesling",
            "profile": "Trocken & Spritzig",
            "vibe": "Erfrischung pur",
            "description": "Ein spritziger, mineralischer Riesling mit lebendiger Säure und Aromen von grünem Apfel, Limette und weißem Pfirsich. Perfekt für laue Sommerabende.",
            "price_glass": "6.50 €",
            "price_bottle": "24.00 €"
        },
        {
            "name": "Sonnenaufgang Grauburgunder",
            "profile": "Fruchtig & Harmonisch",
            "vibe": "Gemütliches Beisammensein",
            "description": "Weich, ausgewogen und voller Fruchtaromen von reifer Birne, Honigmelone und gelbem Apfel. Der ideale Begleiter für gesellige, entspannte Runden.",
            "price_glass": "7.00 €",
            "price_bottle": "26.00 €"
        },
        {
            "name": "Abendlicht Chardonnay",
            "profile": "Kräftig & Vollmundig",
            "vibe": "Tiefgründige Gespräche",
            "description": "Ein im Holzfass gereifter, komplexer Chardonnay mit cremiger Textur, feinen Vanille- und Röstaromen sowie einer dezenten Butternote. Tiefgründig und ausdrucksstark.",
            "price_glass": "8.50 €",
            "price_bottle": "32.00 €"
        }
    ],
    "Rosé": [
        {
            "name": "Rosentraum Spätburgunder Rosé",
            "profile": "Trocken & Spritzig",
            "vibe": "Erfrischung pur",
            "description": "Elegant, trocken und spritzig. Frische Aromen von Himbeeren, Walderdbeeren und eine feine Kräuternote sorgen für pure, anspruchsvolle Erfrischung.",
            "price_glass": "6.80 €",
            "price_bottle": "25.00 €"
        },
        {
            "name": "Dämmerung Grenache Rosé",
            "profile": "Fruchtig & Harmonisch",
            "vibe": "Gemütliches Beisammensein",
            "description": "Harmonisch balanciert mit zarten floralen Noten, reifer Beerenfrucht und einer milden, schmeichelnden Säure. Perfekt für entspannte Stunden.",
            "price_glass": "7.20 €",
            "price_bottle": "27.00 €"
        },
        {
            "name": "Kupferglanz Syrah Rosé",
            "profile": "Kräftig & Vollmundig",
            "vibe": "Tiefgründige Gespräche",
            "description": "Ein kräftiger, würziger Rosé mit Noten von reifen Kirschen, Kräutern der Provence und komplexem Nachhall. Ideal für tiefgründige Gespräche.",
            "price_glass": "8.00 €",
            "price_bottle": "30.00 €"
        }
    ],
    "Rotwein": [
        {
            "name": "Samt & Seide Pinot Noir",
            "profile": "Trocken & Spritzig",
            "vibe": "Erfrischung pur",
            "description": "Ein samtiger, eleganter Pinot Noir. Kann leicht gekühlt getrunken werden. Belebende Aromen von frischer Sauerkirsche und roten Johannisbeeren.",
            "price_glass": "7.50 €",
            "price_bottle": "28.00 €"
        },
        {
            "name": "Abendrot Merlot",
            "profile": "Fruchtig & Harmonisch",
            "vibe": "Gemütliches Beisammensein",
            "description": "Sehr weich, samtig und verführungsvoll fruchtig. Aromen von dunklen Pflaumen, Brombeeren und ein Hauch von feiner Zartbitterschokolade.",
            "price_glass": "7.80 €",
            "price_bottle": "29.00 €"
        },
        {
            "name": "Kaminfeuer Cabernet Sauvignon",
            "profile": "Kräftig & Vollmundig",
            "vibe": "Tiefgründige Gespräche",
            "description": "Ein wuchtiger, komplexer Rotwein mit reifen Tanninen, viel Körper und tiefen Aromen von Cassis, Zedernholz, Pfeffer und dunklem Kakao.",
            "price_glass": "9.50 €",
            "price_bottle": "36.00 €"
        }
    ]
}

# Premium Custom CSS Injection for Mobile-First Burgundy Theme
custom_css = """
<style>
/* Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&family=Inter:wght@300;400;500;600;700&display=swap');

/* Main app background and typography */
.stApp {
    background: linear-gradient(180deg, #120106 0%, #1d030a 40%, #0e0104 100%) !important;
    color: #f5ecef !important;
    font-family: 'Inter', sans-serif !important;
}

/* Responsive mobile-first container */
@media (min-width: 576px) {
    .block-container {
        max-width: 480px !important;
        padding: 3rem 2rem !important;
        margin: 2rem auto !important;
        background-color: rgba(29, 3, 10, 0.85) !important;
        border: 1px solid rgba(229, 169, 60, 0.25) !important;
        border-radius: 32px !important;
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.8) !important;
        backdrop-filter: blur(15px) !important;
    }
}

/* Hide standard Streamlit header, footer, etc. */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.stDeployButton {display:none;}

/* Header styles */
.app-header {
    text-align: center;
    margin-bottom: 24px;
}
.logo {
    font-size: 3rem;
    margin-bottom: 8px;
    display: inline-block;
    animation: sway 3s ease-in-out infinite alternate;
}
@keyframes sway {
    0% { transform: rotate(-6deg); }
    100% { transform: rotate(6deg); }
}
.brand-title {
    font-family: 'Playfair Display', serif;
    font-size: 2.3rem;
    font-weight: 800;
    color: #E5A93C;
    margin: 0;
    letter-spacing: 1px;
    text-shadow: 0 2px 4px rgba(0,0,0,0.5);
}
.brand-subtitle {
    font-family: 'Inter', sans-serif;
    font-size: 0.95rem;
    color: #dcd0d4;
    margin-top: 6px;
    margin-bottom: 0;
    font-weight: 300;
    letter-spacing: 0.5px;
}

/* Custom styled tabs */
div[data-baseweb="tab-list"] {
    background-color: rgba(255, 255, 255, 0.02) !important;
    border-radius: 12px !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    padding: 4px !important;
    margin-bottom: 2rem !important;
    display: flex !important;
    justify-content: space-around !important;
}

div[data-baseweb="tab-list"] button {
    background-color: transparent !important;
    color: #dcd0d4 !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 10px 16px !important;
    font-family: 'Inter', sans-serif !important;
    font-weight: 500 !important;
    font-size: 0.95rem !important;
    transition: all 0.3s ease !important;
    flex-grow: 1 !important;
    text-align: center !important;
}

div[data-baseweb="tab-list"] button[aria-selected="true"] {
    background-color: #5C061E !important;
    color: #E5A93C !important;
    box-shadow: 0 4px 12px rgba(92, 6, 30, 0.5) !important;
    border: 1px solid rgba(229, 169, 60, 0.3) !important;
}

/* Radio button text formatting */
div[data-testid="stMarkdownContainer"] p {
    font-size: 1rem !important;
    color: #f5ecef !important;
}

/* Style radio title labels */
div[data-testid="stRadio"] > label {
    font-family: 'Inter', sans-serif !important;
    font-weight: 600 !important;
    color: #E5A93C !important;
    font-size: 1.05rem !important;
    margin-bottom: 10px !important;
    border-left: 3px solid #5C061E !important;
    padding-left: 8px !important;
}

div[data-testid="stRadio"] div[role="radiogroup"] {
    display: flex !important;
    flex-direction: column !important;
    gap: 8px !important;
}

div[data-testid="stRadio"] div[role="radiogroup"] label {
    background-color: rgba(255, 255, 255, 0.02) !important;
    border: 1px solid rgba(255, 255, 255, 0.06) !important;
    border-radius: 12px !important;
    padding: 12px 16px !important;
    color: #f5ecef !important;
    cursor: pointer !important;
    transition: all 0.2s ease !important;
}

div[data-testid="stRadio"] div[role="radiogroup"] label:hover {
    background-color: rgba(92, 6, 30, 0.2) !important;
    border-color: rgba(229, 169, 60, 0.3) !important;
}

/* Selected option indicators styling */
div[role="radiogroup"] label span[data-baseweb="radio"] {
    border-color: rgba(255, 255, 255, 0.3) !important;
    background-color: transparent !important;
}

div[role="radiogroup"] label span[data-baseweb="radio"] > div {
    background-color: #E5A93C !important;
}

/* Streamlit button styling */
.stButton button {
    width: 100% !important;
    background: linear-gradient(135deg, #5C061E 0%, #3D0414 100%) !important;
    color: #E5A93C !important;
    border: 1px solid #E5A93C !important;
    border-radius: 12px !important;
    padding: 12px 24px !important;
    font-family: 'Inter', sans-serif !important;
    font-weight: 600 !important;
    font-size: 1.05rem !important;
    letter-spacing: 0.5px !important;
    box-shadow: 0 4px 15px rgba(92, 6, 30, 0.4) !important;
    transition: all 0.3s ease !important;
    margin-top: 10px;
}

.stButton button:hover {
    background: linear-gradient(135deg, #7C0A29 0%, #5C061E 100%) !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 6px 20px rgba(229, 169, 60, 0.2) !important;
    color: #ffffff !important;
}

/* Wine Menu Card styling */
.wine-card {
    background: linear-gradient(135deg, rgba(61, 4, 20, 0.4) 0%, rgba(37, 5, 16, 0.6) 100%);
    border: 1px solid rgba(229, 169, 60, 0.15);
    border-radius: 16px;
    padding: 18px;
    margin-bottom: 16px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.25);
    transition: all 0.3s ease;
}
.wine-card:hover {
    transform: translateY(-2px);
    border-color: rgba(229, 169, 60, 0.45);
    box-shadow: 0 6px 20px rgba(229, 169, 60, 0.15);
}
.wine-card-header {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-bottom: 8px;
    gap: 12px;
}
.wine-name {
    font-family: 'Playfair Display', serif;
    font-size: 1.25rem;
    font-weight: 700;
    color: #E5A93C;
}
.wine-price {
    font-family: 'Inter', sans-serif;
    font-size: 0.95rem;
    font-weight: 600;
    color: #ffffff;
    white-space: nowrap;
}
.wine-description {
    font-family: 'Inter', sans-serif;
    font-size: 0.9rem;
    color: #dcd0d4;
    line-height: 1.45;
    margin-bottom: 12px;
    font-style: italic;
}
.wine-tags {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
}
.wine-tag {
    font-family: 'Inter', sans-serif;
    font-size: 0.75rem;
    font-weight: 600;
    color: #E5A93C;
    background-color: rgba(92, 6, 30, 0.3);
    border: 1px solid rgba(229, 169, 60, 0.25);
    padding: 4px 10px;
    border-radius: 20px;
}

/* Quiz match result card */
.result-card-container {
    background: linear-gradient(135deg, rgba(92, 6, 30, 0.6) 0%, rgba(61, 4, 20, 0.8) 100%);
    border: 2px solid #E5A93C;
    border-radius: 24px;
    padding: 26px;
    margin-top: 10px;
    margin-bottom: 24px;
    box-shadow: 0 12px 30px rgba(229, 169, 60, 0.25);
    animation: fadeIn 0.6s cubic-bezier(0.16, 1, 0.3, 1);
    text-align: center;
}
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(15px); }
    to { opacity: 1; transform: translateY(0); }
}
.result-label {
    font-family: 'Inter', sans-serif;
    font-size: 0.85rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    color: #E5A93C;
    margin-bottom: 10px;
}
.result-wine-name {
    font-family: 'Playfair Display', serif;
    font-size: 1.9rem;
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 12px;
    text-shadow: 0 2px 4px rgba(0,0,0,0.6);
}
.result-wine-description {
    font-family: 'Inter', sans-serif;
    font-size: 0.95rem;
    color: #f5ecef;
    line-height: 1.5;
    margin-bottom: 18px;
    font-style: italic;
}
.result-details {
    border-top: 1px solid rgba(255, 255, 255, 0.12);
    border-bottom: 1px solid rgba(255, 255, 255, 0.12);
    padding: 14px 0;
    margin-bottom: 18px;
}
.result-price {
    font-family: 'Inter', sans-serif;
    font-size: 1.05rem;
    color: #ffffff;
    display: flex;
    justify-content: center;
    gap: 20px;
}
.result-price strong {
    color: #E5A93C;
}
.result-tags {
    display: flex;
    justify-content: center;
    gap: 8px;
    flex-wrap: wrap;
}

/* Category header */
.category-header {
    font-family: 'Playfair Display', serif;
    font-size: 1.5rem;
    font-weight: 700;
    color: #E5A93C;
    margin-top: 24px;
    margin-bottom: 14px;
    border-bottom: 1px solid rgba(229, 169, 60, 0.2);
    padding-bottom: 6px;
    text-align: left;
}
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# Application Header
st.markdown(
    """
    <div class="app-header">
        <div class="logo">🍷</div>
        <h1 class="brand-title">Wein-Zeit</h1>
        <p class="brand-subtitle">Dein interaktiver Event-Weinbegleiter</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Initialize Session State for Quiz Results
if "quiz_match" not in st.session_state:
    st.session_state.quiz_match = None

# Recommendation Scoring Function
def get_recommendation(wine_type, profile, vibe):
    candidates = WINE_DATA.get(wine_type, [])
    best_candidate = None
    max_score = -1
    
    for wine in candidates:
        score = 0
        if wine["profile"] == profile:
            score += 2
        if wine["vibe"] == vibe:
            score += 1
            
        if score > max_score:
            max_score = score
            best_candidate = wine
            
    return best_candidate

# Setup Main Navigation Tabs
tab1, tab2 = st.tabs(["Geschmacks-Finder", "Digitale Weinkarte"])

# AREA 1: Geschmacks-Finder (Interactive Quiz)
with tab1:
    if st.session_state.quiz_match is None:
        st.markdown("<h3 style='margin-top:0;'>Finde deinen perfekten Wein</h3>", unsafe_allow_html=True)
        
        # Question 1
        q_type = st.radio(
            "1. Was trinkst du am liebsten?",
            options=["Weißwein", "Rosé", "Rotwein"],
            key="quiz_type"
        )
        
        st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
        
        # Question 2
        q_profile = st.radio(
            "2. Wie soll dein Wein schmecken?",
            options=["Trocken & Spritzig", "Fruchtig & Harmonisch", "Kräftig & Vollmundig"],
            key="quiz_profile"
        )
        
        st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
        
        # Question 3
        q_vibe = st.radio(
            "3. Was ist dein Vibe im Moment?",
            options=["Erfrischung pur", "Gemütliches Beisammensein", "Tiefgründige Gespräche"],
            key="quiz_vibe"
        )
        
        st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)
        
        if st.button("Wein finden"):
            match = get_recommendation(q_type, q_profile, q_vibe)
            st.session_state.quiz_match = match
            st.rerun()
            
    else:
        match = st.session_state.quiz_match
        
        st.markdown(
            f"""
            <div class="result-card-container">
                <div class="result-label">Dein Perfect Match 🍷</div>
                <div class="result-wine-name">{match['name']}</div>
                <div class="result-wine-description">"{match['description']}"</div>
                <div class="result-details">
                    <div class="result-price">
                        <span>Glas (0.1l): <strong>{match['price_glass']}</strong></span>
                        <span>Flasche (0.75l): <strong>{match['price_bottle']}</strong></span>
                    </div>
                </div>
                <div class="result-tags">
                    <span class="wine-tag">{match['profile']}</span>
                    <span class="wine-tag">{match['vibe']}</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        if st.button("Erneut suchen"):
            st.session_state.quiz_match = None
            st.rerun()

# AREA 2: Digitale Weinkarte (Digital Menu)
with tab2:
    st.markdown("<h3 style='margin-top:0;'>Unsere Weinkarte</h3>", unsafe_allow_html=True)
    
    for category, wines in WINE_DATA.items():
        icon = "🥂" if "Weiß" in category else "🌸" if "Rosé" in category else "🍷"
        st.markdown(f"<div class='category-header'>{icon} {category}</div>", unsafe_allow_html=True)
        
        for wine in wines:
            st.markdown(
                f"""
                <div class="wine-card">
                    <div class="wine-card-header">
                        <span class="wine-name">{wine['name']}</span>
                        <span class="wine-price">{wine['price_glass']} / {wine['price_bottle']}</span>
                    </div>
                    <div class="wine-description">{wine['description']}</div>
                    <div class="wine-tags">
                        <span class="wine-tag">{wine['profile']}</span>
                        <span class="wine-tag">{wine['vibe']}</span>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
# Ultimativer Block zum Ausblenden aller Leisten, Kronen und Menüs
hide_everything_style = """
    <style>
    [data-testid="stStatusWidget"] {visibility: hidden !important; display: none !important;}
    footer {visibility: hidden !important; display: none !important;}
    .stAppDeployButton {visibility: hidden !important; display: none !important;}
    #MainMenu {visibility: hidden !important; display: none !important;}
    header {visibility: hidden !important; display: none !important;}
    stDecoration {visibility: hidden !important; display: none !important;}
    [data-testid="stSidebarCollapseButton"] {visibility: hidden !important;}
    </style>
"""
st.markdown(hide_everything_style, unsafe_allow_html=True)