import streamlit as st

# Custom CSS for animations, styling, and overlays
st.markdown("""
<style>
    /* Global styling */
    body { font-family: 'sans-serif'; color: #FAFAFA;}
    .stApp { background-color: #00172B; }
    /* Fade-in animation */
    @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
    .fade-in { animation: fadeIn 2s; }
    /* Button styling with hover animation */
    .stButton > button { background-color: #E694FF; color: #00172B; border: none; padding: 10px 20px; border-radius: 5px; transition: transform 0.3s; }
    .stButton > button:hover { transform: scale(1.05); }
    /* Overlay for header */
    .header-overlay { position: relative; text-align: center; color: white; }
    .header-overlay img { width: 100%; height: auto; opacity: 0.6; }
    .header-text { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 590px;}
    /* Footer */
    .footer { text-align: center; padding: 10px; background-color: #0083B8; color: #FAFAFA; }
</style>
""", unsafe_allow_html=True)

# Header with overlay image (lazy loading via Streamlit caching)
st.markdown('<div class="header-overlay fade-in">', unsafe_allow_html=True)
st.image("images/RMS_Titanic_3.jpg", use_container_width=True)
st.markdown('<div class="header-text"><h1>Titanic Survival Predictor 🚢</h1><h1></h1></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Sidebar navigation (Streamlit auto-generates from pages/)
st.sidebar.title("Navigation 🧭")
st.sidebar.markdown("Explore the project:")

# Content
st.write("### Welcome to My Titanic Project! 🎉")
st.write("This interactive web app showcases machine learning on the Titanic dataset. Built with Streamlit, it features exploratory data analysis, model training, and survival predictions in a sleek, dark-themed interface.")
st.write("Navigate using the sidebar to explore visualizations, train models, or predict survival.")

# Footer
st.markdown('<div class="footer">© 2025 Muzamal Asghar | Hex Softwares Internship Project</div>', unsafe_allow_html=True)