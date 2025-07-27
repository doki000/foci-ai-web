import streamlit as st
import requests

def get_openligadb_data():
    """Példa: Élő meccs statisztikáinak lekérése a Bundesliga 1-ből"""
    url = "https://www.openligadb.de/api/getmatchdata/bl1"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data:
            last_match = data[0]  # utolsó meccs
            team1 = last_match['team1']['teamName']
            team2 = last_match['team2']['teamName']
            goals1 = last_match['matchResults'][0]['pointsTeam1']
            goals2 = last_match['matchResults'][0]['pointsTeam2']
            return f"{team1} {goals1} - {goals2} {team2}"
        else:
            return "Nincs elérhető meccsadat."
    else:
        return "Hiba az API hívás során."

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
if st.button("Frissítés API-ból"):
    eredmeny = get_openligadb_data()
    st.info(f"Utolsó Bundesliga 1 meccs eredménye: {eredmeny}")
