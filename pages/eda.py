import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data with caching for lazy loading
@st.cache_data
def load_data():
    return pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

df = load_data()

st.title("Exploratory Data Analysis 📊")
st.write("Visualize and analyze the Titanic dataset.")

# Data overview
st.subheader("Dataset Preview")
st.dataframe(df.head(), use_container_width=True)

# Visualizations (cached for performance)
@st.cache_data
def plot_survival_count():
    fig, ax = plt.subplots()
    sns.countplot(x='Survived', data=df, palette='viridis', ax=ax)
    ax.set_title("Survival Count")
    return fig

@st.cache_data
def plot_age_distribution():
    fig, ax = plt.subplots()
    sns.histplot(df['Age'].dropna(), kde=True, color='#E694FF', ax=ax)
    ax.set_title("Age Distribution")
    return fig

st.subheader("Survival Count")
st.pyplot(plot_survival_count(), use_container_width=True)

st.subheader("Age Distribution")
st.pyplot(plot_age_distribution(), use_container_width=True)

st.write("**Insights**: More passengers did not survive (0) than survived (1). Age distribution is right-skewed, with most passengers being young adults.")