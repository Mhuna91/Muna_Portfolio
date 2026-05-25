import streamlit as st
import os
import time
import requests

# ---------------------------
# PAGE CONFIG (MUST BE FIRST)
# ---------------------------
st.set_page_config(
    page_title="Muna Portfolio",
    layout="wide",
    page_icon="🚀"
)

# ---------------------------
# INTRO LOADER
# ---------------------------
placeholder = st.empty()

with placeholder.container():
    st.markdown("<h1 style='text-align:center;'>🚀 Mavericks</h1>", unsafe_allow_html=True)
    time.sleep(2)

placeholder.empty()

# ---------------------------
# ADMIN LOGIN
# ---------------------------
password = st.text_input("🔐 Enter Admin Password", type="password")

if password != "muna123":
    st.stop()

# ---------------------------
# GOOGLE ANALYTICS
# ---------------------------
st.markdown("""
<script async src="https://www.googletagmanager.com/gtag/js?id=G-1C57N3TE8E"></script>
<script>
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());
gtag('config', 'G-1C57N3TE8E');
</script>
""", unsafe_allow_html=True)

# ---------------------------
# VISITOR COUNTER (REAL)
# ---------------------------
count = requests.get("https://api.countapi.xyz/hit/muna-portfolio/visits").json()["value"]

# ---------------------------
# SIDEBAR NAVIGATION
# ---------------------------
menu = st.sidebar.radio("📌 Navigation", [
    "Home",
    "Projects",
    "Certificates",
    "CV",
    "Contact"
])

# ---------------------------
# DARK MODE
# ---------------------------
mode = st.sidebar.toggle("🌗 Dark Mode", value=True)

if mode:
    text_color = "white"
else:
    text_color = "black"

# ---------------------------
# PREMIUM CSS (GLASS UI)
# ---------------------------
st.markdown(f"""
<style>

body {{
    background: linear-gradient(135deg, #0e1117, #1c1f26);
    color: {text_color};
    font-family: 'Segoe UI', sans-serif;
}}

.card {{
    padding: 25px;
    border-radius: 20px;
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(10px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    margin-bottom: 20px;
    transition: all 0.3s ease;
}}

.card:hover {{
    transform: translateY(-8px) scale(1.02);
}}

.hero-title {{
    font-size: 60px;
    font-weight: 700;
}}

.hero-sub {{
    font-size: 22px;
    opacity: 0.8;
}}

</style>
""", unsafe_allow_html=True)

# ---------------------------
# HOME
# ---------------------------
if menu == "Home":

    col1, col2 = st.columns([1, 3])

    with col1:
        try:
            st.image("assets/profile.jpg", width=220)
        except:
            st.warning("Upload profile.jpg inside assets folder")

    with col2:
        st.markdown(f"""
        <div class="hero-title">🚀 Mavericks</div>
        <div class="hero-sub">AI Engineer • Data Scientist • Recommender Systems</div>
        <br>
        👀 Visitors: <b>{count}</b>
        """, unsafe_allow_html=True)

# ---------------------------
# PROJECTS
# ---------------------------
elif menu == "Projects":

    st.header("📊 Featured Projects")

    projects = [
        ("Restaurant Recommender", "https://mavericks-restaurant-recommender-dnkztuh9nv34lzmgnubg3s.streamlit.app/"),
        ("Petrol Station Dashboard", "https://petrolstationdashboard-hyiqfesovhaugbngntxcba.streamlit.app/"),
        ("Retail Sales App", "https://mhuna91-retail-company-sales-data-app-ooeqle.streamlit.app/"),
        ("Sales Analysis", "https://mhuna91-sales-data-analyses2-app-xsx2ew.streamlit.app/"),
        ("Valuation Dashboard", "https://valuation-sentiment-dashboard-cvmixmvyxgzstgaashdygf.streamlit.app/")
    ]

    cols = st.columns(2)

    for i, (name, link) in enumerate(projects):
        with cols[i % 2]:
            st.markdown(f"""
            <div class="card">
                <h3>{name}</h3>
                <a href="{link}" target="_blank">🚀 Launch Project</a>
            </div>
            """, unsafe_allow_html=True)
# ---------------------------
# Netlify PROJECTS
# ---------------------------

elif menu == "Netlify Projects":

    st.header("🌍 Netlify Projects")
    netlify_links = [
    "https://app.netlify.com/projects/valuer-network/",
    "https://app.netlify.com/projects/land-use-act/",
    "https://app.netlify.com/projects/earnest-cascaron-2f461b/"
    
    ]
    cols = st.columns(2)

    for i, (name, link) in enumerate(projects):
        with cols[i % 2]:
            st.markdown(f"""
            <div class="card">
                <h3>{name}</h3>
                <a href="{link}" target="_blank">🚀 Launch Project</a>
            </div>
            """, unsafe_allow_html=True)

# ---------------------------
# CERTIFICATES
# ---------------------------
elif menu == "Certificates":

    st.header("🏅 Certificates")

    cert_folder = "assets"

    cert_files = [
        f for f in os.listdir(cert_folder)
        if f.lower().endswith(("png", "jpg", "jpeg"))
    ]

    cols = st.columns(3)

    for i, cert in enumerate(cert_files):
        with cols[i % 3]:
            st.image(f"{cert_folder}/{cert}", caption=cert)

# ---------------------------
# CV DOWNLOAD
# ---------------------------
elif menu == "CV":

    st.header("📄 Download CVs")

    try:
        with open("assets/cv1.pdf", "rb") as file:
            st.download_button("📥 Download CV 1", file, "cv1.pdf")

        with open("assets/cv2.pdf", "rb") as file:
            st.download_button("📥 Download CV 2", file, "cv2.pdf")
    except:
        st.warning("Upload CVs into assets folder")

# ---------------------------
# CONTACT
# ---------------------------
elif menu == "Contact":

    st.header("📬 Contact")

    st.markdown("""
    - 📧 iheanachomunachi123@gmail.com  
    - 🌐 linguarai.com  
    - 💼 https://github.com/Mhuna91/
    """)

# ---------------------------
# FLOATING WHATSAPP BUTTON
# ---------------------------
st.markdown("""
<style>
.whatsapp-float {
    position: fixed;
    bottom: 20px;
    right: 20px;
    background-color: #25D366;
    color: white;
    padding: 15px 18px;
    border-radius: 50px;
    text-decoration: none;
    font-size: 18px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    z-index: 1000;
}
</style>

<a href="https://wa.me/2348100622292" target="_blank" class="whatsapp-float">
💬 Hire Me
</a>
""", unsafe_allow_html=True)

# ---------------------------
# FOOTER
# ---------------------------
st.success("🚀 Portfolio Live — Startup Level Achieved!")
