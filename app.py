import streamlit as st

st.set_page_config(page_title="Foci AI Tippek", layout="wide")

st.title("⚽ Foci AI WebApp")
st.write("Ez az alkalmazás élő futball statisztikák alapján ad fogadási ajánlásokat.")

st.header("🔮 Tipp: Over/Under 2.5 gól")
goals = st.slider("Jelenlegi gólok száma", 0, 10, 2)
dangerous_attacks = st.number_input("Veszélyes támadások száma", min_value=0)
shots_on_target = st.number_input("Kaput eltaláló lövések", min_value=0)

if st.button("Tipp generálása"):
    score = goals + 0.1 * dangerous_attacks + 0.3 * shots_on_target
    if score > 3.5:
        st.success("Ajánlott tipp: ✅ Over 2.5")
    else:
        st.warning("Ajánlott tipp: ❌ Under 2.5")
add app.py
