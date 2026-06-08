
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Netflix Recommendation System",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 Netflix Recommendation System")
st.markdown("Hybrid Recommendation Engine using ItemCF + SVD")

# Metrics
col1, col2, col3, col4 = st.columns(4)

col1.metric("ItemCF RMSE", "1.0062")
col2.metric("SVD RMSE", "0.9403")
col3.metric("Hybrid RMSE", "0.9385")
col4.metric("MAP@10", "0.7350")

st.divider()

st.header("Dataset Overview")

dataset = pd.DataFrame({
    "Metric": ["Ratings", "Users", "Movies", "Sparsity"],
    "Value": ["5,000,000", "404,478", "996", "98.76%"]
})

st.dataframe(dataset)

st.divider()

st.header("Model Comparison")

comparison = pd.DataFrame({
    "Model": ["ItemCF", "SVD", "Hybrid"],
    "RMSE": [1.0062, 0.9403, 0.9385],
    "MAP@10": [0.0, 0.7347, 0.7350]
})

st.dataframe(comparison)

st.bar_chart(
    comparison.set_index("Model")[["RMSE"]]
)

st.divider()

st.header("Top Recommendations")

recommendations = pd.DataFrame({
    "Movie": [
        "ABC Primetime: Mel Gibson's The Passion of the Christ",
        "Dil Chahta Hai",
        "Lord of the Rings: Return of the King",
        "Monarch of the Glen: Series 2",
        "Homicide: Life on the Street: Season 7"
    ],
    "Hybrid Score": [
        4.05,
        3.95,
        3.88,
        3.84,
        3.84
    ]
})

st.dataframe(recommendations)

st.bar_chart(
    recommendations.set_index("Movie")
)

st.divider()

st.header("Explainable Recommendation")

movie = st.selectbox(
    "Select Movie",
    recommendations["Movie"]
)

st.success(
    f"""
Recommended Movie: {movie}

Reason:
• Similar users rated it highly
• Strong SVD latent preference match
• High Hybrid recommendation score
"""
)
