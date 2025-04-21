import streamlit as st
from model.bayesian_model import build_model, get_prediction

st.set_page_config(page_title="🎬 Movie Recommender", layout="centered")

st.title("🎬 Movie Recommendation System")
st.markdown("This app uses a **Bayesian Network** to predict if you'll like a movie!")

# --- Build model once ---
infer = build_model()

# --- Input Form ---
with st.form("user_input"):
    st.subheader("🎯 Select Your Info:")
    age = st.selectbox("🧓 Select Age Group", options=["Teen", "Adult", "Senior"])
    gender = st.radio("🧑 Select Gender", options=["Male", "Female"])
    genre = st.selectbox("🎞️ Choose Movie Genre", options=[" -mAction", "Comedy", "Romance", "Horror", "Drama"])
    submit = st.form_submit_button("🔍 Predict")

# --- Process Form ---
if submit:
    # Mapping inputs to the corresponding numeric values in the Bayesian Network
    age_map = {"Teen": 0, "Adult": 1, "Senior": 2}
    gender_map = {"Male": 0, "Female": 1}
    genre_map = {"Action": 0, "Comedy": 1, "Romance": 2, "Horror": 3, "Drama": 4}

    # 🧠 Pass all required arguments in the correct order
    result = get_prediction(
        infer,
        age=age_map[age],
        gender=gender_map[gender],
        genre=genre_map[genre]
    )

    # Extract the probabilities of liking the movie
    liked_prob = result.values[1] * 100  # 1 for "Liked"
    not_liked_prob = result.values[0] * 100  # 0 for "Not Liked"

    # Display results
    st.success(f"👍 Liked Probability: **{liked_prob:.2f}%**")
    st.warning(f"👎 Not Liked Probability: **{not_liked_prob:.2f}%**")

    # Show bar chart
    st.subheader("📊 Prediction Breakdown")
    st.bar_chart({
        "Liked": [liked_prob],
        "Not Liked": [not_liked_prob]
    })
