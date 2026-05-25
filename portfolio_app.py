import streamlit as st

st.set_page_config(page_title="Mavericks Portfolio", layout="wide")

# HERO
st.title("🚀 Muna Portfolio")
st.subheader("AI Engineer | Data Scientist | Recommender Systems")

st.markdown("🌐 **My Platform:** [linguarai.com](https://linguarai.com)")

st.divider()

# PROJECTS
st.header("Featured Projects")

projects = {
    "Restaurant Recommender": "https://mavericks-restaurant-recommender-dnkztuh9nv34lzmgnubg3s.streamlit.app/",
    "Petrol Station Dashboard": "https://petrolstationdashboard-hyiqfesovhaugbngntxcba.streamlit.app/",
    "Retail Sales App": "https://mhuna91-retail-company-sales-data-app-ooeqle.streamlit.app/",
    "Sales Analysis": "https://mhuna91-sales-data-analyses2-app-xsx2ew.streamlit.app/",
    "Valuation Dashboard": "https://valuation-sentiment-dashboard-cvmixmvyxgzstgaashdygf.streamlit.app/"
}

cols = st.columns(2)
for i, (name, link) in enumerate(projects.items()):
    with cols[i % 2]:
        st.markdown(f"### {name}")
        st.markdown(f"[🚀 Open App]({link})")

st.divider()

# API
st.header("⚙️ API Endpoint")
st.markdown("[🔗 Open API](https://restaurant-recommender-5d4o.onrender.com)")
st.markdown("[📄 API Docs](https://restaurant-recommender-5d4o.onrender.com/docs)")

st.divider()

# GITHUB
st.header("💻 GitHub")
st.markdown("[🔗 Visit My GitHub](https://github.com/Mhuna91/)")

st.divider()

# NETLIFY
st.header("🌍 Netlify Projects")
st.markdown("""
- https://app.netlify.com/projects/valuer-network/
- https://app.netlify.com/projects/land-use-act/
- https://app.netlify.com/projects/earnest-cascaron-2f461b/
""")

st.divider()

# CV DOWNLOAD (BETTER THAN UPLOAD)
st.header("📄 CV Download")

st.markdown("👉 Upload your CV files into the **assets/** folder in GitHub")

try:
    with open("assets/cv1.pdf", "rb") as file:
        st.download_button("Download CV 1", file, "cv1.pdf")

    with open("assets/cv2.pdf", "rb") as file:
        st.download_button("Download CV 2", file, "cv2.pdf")
except:
    st.info("Upload CV files into assets folder to enable download")

st.divider()

# CERTIFICATES
st.header("🏅 Certificates")

st.markdown("👉 Add certificate images or PDFs in **assets/** folder")

st.write("Certificates will appear here once uploaded.")

st.divider()

# CONTACT
st.header("📬 Contact")

st.markdown("""
- Email: iheanachomunachi123@gmial.com  
- GitHub: https://github.com/Mhuna91/  
- Website: linguarai.com  
""")

st.success("✅ Portfolio Live & Ready!")
