import streamlit as st
import numpy as np

# Function to simulate the game
def simulate_game(home_mean, home_std, away_mean, away_std, spread_line=4.5, over_under_line=220, simulations=100000):
    home_scores = np.random.normal(home_mean, home_std, simulations)
    away_scores = np.random.normal(away_mean, away_std, simulations)

    home_win = home_scores > away_scores
    spread_cover = (home_scores - away_scores) > spread_line
    total_points = home_scores + away_scores
    over_total = total_points > over_under_line

    ml_prob = round(np.mean(home_win) * 100, 2)
    spread_prob = round(np.mean(spread_cover) * 100, 2)
    over_prob = round(np.mean(over_total) * 100, 2)

    return ml_prob, spread_prob, over_prob

# Streamlit UI
st.title("NBA Game Forecast")
st.write("Predict Moneyline, Spread, and Over/Under probabilities for any NBA game.")

# Teams selection
home_team = st.text_input("Home Team", "Suns")
away_team = st.text_input("Away Team", "Rockets")

# Team stats inputs
home_mean = st.number_input(f"{home_team} Avg Points", min_value=50.0, max_value=150.0, value=113.0)
home_std = st.number_input(f"{home_team} Std Dev", min_value=0.0, max_value=30.0, value=10.0)
away_mean = st.number_input(f"{away_team} Avg Points", min_value=50.0, max_value=150.0, value=110.0)
away_std = st.number_input(f"{away_team} Std Dev", min_value=0.0, max_value=30.0, value=12.0)

spread_line = st.number_input("Spread Line (Home Team)", value=4.5)
over_under_line = st.number_input("Over/Under Line", value=220.0)

if st.button("Forecast Game"):
    ml_prob, spread_prob, over_prob = simulate_game(home_mean, home_std, away_mean, away_std, spread_line, over_under_line)
    
    st.subheader("Forecast Results")
    st.write(f"**Moneyline:** {home_team} win probability = {ml_prob}%")
    st.write(f"**Spread:** {home_team} -{spread_line} cover probability = {spread_prob}%")
    st.write(f"**Over {over_under_line} points probability:** {over_prob}%")
