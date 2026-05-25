import streamlit as st
import os

# ---------------------------
# PAGE CONFIG
# ---------------------------
st.set_page_config(
    page_title="Muna Portfolio",
    layout="wide",
    page_icon="🚀"
)

# ---------------------------
# DARK / LIGHT MODE TOGGLE
# ---------------------------
mode = st.toggle("🌗 Dark Mode", value=True)

if mode:
    bg_color = "#0e1117"
    text_color = "white"
    card_bg = "#1c1f26"
else:
    bg_color = "#ffffff"
    text_color = "#000000"
    card_bg = "#f5f5f5"

# ---------------------------
# CUSTOM CSS (ANIMATIONS)
# ---------------------------
st.markdown(f"""
<style>
body {{
    background-color: {bg_color};
    color: {text_color};
}}
.card {{
    padding: 20px;
    border-radius: 15px;
    background: {card_bg};
    box-shadow: 0px 4px 20px rgba(0,0,0,0.2);
    margin-bottom: 20px;
    transition: transform 0.3s ease;
}}
.card:hover {{
    transform: scale(1.03);
}}
.center {{
    text-align: center;
}}
</style>
""", unsafe_allow_html=True)

# ---------------------------
# ANALYTICS (SIMPLE COUNTER)
# ---------------------------
counter_file = "counter.txt"

if not os.path.exists(counter_file):
    with open(counter_file, "w") as f:
        f.write("0")

with open(counter_file, "r") as f:
    count = int(f.read())

count += 1

with open(counter_file, "w") as f:
    f.write(str(count))

# ---------------------------
# HERO SECTION
# ---------------------------
col1, col2 = st.columns([1, 3])

with col1:
    try:
        st.image("assets/profile.jpg", width=200)
    except:
        st.warning("Add profile.jpg to assets folder")

with col2:
    st.title("🚀 Mavericks Portfolio")
    st.subheader("AI Engineer | Data Scientist | Recommender Systems")
    st.markdown("🌐 [linguarai.com](https://linguarai.com)")
    st.write(f"👀 Visitors: {count}")

st.divider()

# ---------------------------
# PROJECTS
# ---------------------------
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
        <a href="{link}" target="_blank">🚀 Open App</a>
        </div>
        """, unsafe_allow_html=True)

st.divider()

# ---------------------------
# API SECTION
# ---------------------------
st.header("⚙️ API Endpoint")

st.markdown(f"""
<div class="card">
<a href="https://restaurant-recommender-5d4o.onrender.com" target="_blank">🔗 Open API</a><br>
<a href="https://restaurant-recommender-5d4o.onrender.com/docs" target="_blank">📄 API Docs</a>
</div>
""", unsafe_allow_html=True)

st.divider()

# ---------------------------
# GITHUB
# ---------------------------
st.header("💻 GitHub")

st.markdown("""
<div class="card">
<a href="https://github.com/Mhuna91/" target="_blank">🔗 Visit GitHub</a>
</div>
""", unsafe_allow_html=True)

st.divider()

# NETLIFY PROJECTS
st.header("🌍 Netlify Projects")

netlify_links = [
    "https://app.netlify.com/projects/valuer-network/",
    "https://app.netlify.com/projects/land-use-act/",
    "https://app.netlify.com/projects/earnest-cascaron-2f461b/"
]

for link in netlify_links:
    st.markdown(f"- 🔗 {link}")

st.divider()

# ---------------------------
# CERTIFICATE GALLERY
# ---------------------------
st.header("🏅 Certificates Gallery")

cert_folder = "assets"

cert_files = [
    f for f in os.listdir(cert_folder)
    if f.lower().endswith(("png", "jpg", "jpeg"))
]

cols = st.columns(3)

for i, cert in enumerate(cert_files):
    with cols[i % 3]:
        st.image(f"{cert_folder}/{cert}", caption=cert)

st.divider()

# ---------------------------
# CV DOWNLOAD SECTION
# ---------------------------
st.header("📄 Download CVs")

try:
    with open("assets/cv1.pdf", "rb") as file:
        st.download_button("📥 Download CV 1", file, "cv1.pdf")

    with open("assets/cv2.pdf", "rb") as file:
        st.download_button("📥 Download CV 2", file, "cv2.pdf")
except:
    st.warning("Upload CVs into assets folder")

st.divider()

# ---------------------------
# CONTACT
# ---------------------------
st.header("📬 Contact")

st.markdown("""
- 📧 iheanachomunachi123@gmail.com  
- 🌐 linguarai.com  
- 💼 https://github.com/Mhuna91/
""")

st.success("🚀 Portfolio Live & Premium Ready!")



