import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="✈️ Flight Price Dashboard", layout="wide")
st.title("✈️ Flight Price Dashboard")

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("airline_flights_csv.csv")
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("🔍 Filter Options")

# Airline multiselect
airline_filter = st.sidebar.multiselect(
    "Select Airline",
    options=df["airline"].unique(),
    default=df["airline"].unique()
)

# Class multiselect
class_filter = st.sidebar.multiselect(
    "Select Class",
    options=df["class"].unique(),
    default=df["class"].unique()
)

# Source dropdown (single select)
source_filter = st.sidebar.selectbox(
    "Source City",
    options=["All"] + sorted(df["source_city"].unique().tolist())
)

# Destination dropdown (single select)
destination_filter = st.sidebar.selectbox(
    "Destination City",
    options=["All"] + sorted(df["destination_city"].unique().tolist())
)

# Apply filters
filtered_df = df[(df["airline"].isin(airline_filter)) & (df["class"].isin(class_filter))]

if source_filter != "All":
    filtered_df = filtered_df[filtered_df["source_city"] == source_filter]

if destination_filter != "All":
    filtered_df = filtered_df[filtered_df["destination_city"] == destination_filter]

# Page navigation
page = st.sidebar.radio(
    "📌 Navigate to:",
    ["Overview", "Price Analysis", "Airline Comparison", "Stops & Duration Analysis"]
)

# Page 1: Overview
if page == "Overview":
    st.header("📊 Flight Data Overview")

    st.subheader("Filtered Data Summary")
    st.write(f"Number of flights: {filtered_df.shape[0]}")

    if st.checkbox("Show Raw Data"):
        st.dataframe(filtered_df.head())

    st.subheader("💰 Price Distribution")
    fig, ax = plt.subplots()
    sns.histplot(filtered_df["price"], kde=True, ax=ax)
    st.pyplot(fig)

# Page 2: Price Analysis
elif page == "Price Analysis":
    st.header("💰 Price Analysis")

    st.subheader("Days Left vs Price")
    fig3, ax3 = plt.subplots()
    sns.scatterplot(x="days_left", y="price", data=filtered_df, alpha=0.6, ax=ax3)
    st.pyplot(fig3)

# Page 3: Airline Comparison
elif page == "Airline Comparison":
    st.header("🛫 Airline Comparison")

    st.subheader("Price by Airline")
    fig2, ax2 = plt.subplots(figsize=(12, 6))
    sns.boxplot(x="airline", y="price", data=filtered_df, ax=ax2)
    plt.xticks(rotation=90)
    st.pyplot(fig2)

# Page 4: Stops & Duration Analysis
elif page == "Stops & Duration Analysis":
    st.header("⏱️ Stops & Duration Analysis")

    if "stops" in filtered_df.columns:
        st.subheader("Price vs Number of Stops")
        fig4, ax4 = plt.subplots()
        sns.boxplot(x="stops", y="price", data=filtered_df, ax=ax4)
        st.pyplot(fig4)

    if "duration" in filtered_df.columns:
        st.subheader("Duration vs Price")
        fig5, ax5 = plt.subplots()
        sns.scatterplot(x="duration", y="price", data=filtered_df, alpha=0.6, ax=ax5)
        st.pyplot(fig5)
