import time  # to simulate a real time data, time loop
import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import streamlit as st  # 🎈 data web app development
from PIL import Image

st.set_page_config(
    page_title="Real-Time Data Science Dashboard",
    page_icon="✅",
    layout="wide",
)
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
# read csv from a github repo
dataset_url = "https://raw.githubusercontent.com/Lexie88rus/bank-marketing-analysis/master/bank.csv"

# read csv from a URL
@st.cache_data
def get_data() -> pd.DataFrame:
    return pd.read_csv(dataset_url)

df = get_data()

# dashboard title
st.title("Real-Time / Live Data Science Dashboard")

# top-level filters
job_filter = st.selectbox("Select the Job", pd.unique(df["job"]))

# creating a single-element container
placeholder = st.empty()

# dataframe filter
df = df[df["job"] == job_filter]

# near real-time / live feed simulation
for seconds in range(200):

    df["age_new"] = df["age"] * np.random.choice(range(1, 5))
    df["balance_new"] = df["balance"] * np.random.choice(range(1, 5))

    # creating KPIs
    avg_age = np.mean(df["age_new"])

    count_married = int(
        df[(df["marital"] == "married")]["marital"].count()
        + np.random.choice(range(1, 30))
    )

    balance = np.mean(df["balance_new"])

    with placeholder.container():

        # create three columns
        kpi1, kpi2, kpi3, kpi4, kpi5 = st.columns([1,1,1,1,1])

        # fill in those three columns with respective metrics or KPIs
        kpi1.image(Image.open('LogoFiles/intek.png'))
        
        kpi2.metric(
            label="A/C Balance",
            value=round(avg_age),
        )

        kpi3.metric(
            label="A/C Balance",
            value=round(avg_age),
        )
        
        kpi4.metric(
            label="A/C Balance",
            value=int(count_married),
        )
        
        kpi5.metric(
            label="A/C Balance",
            value=f"$ {round(balance,2)} ",
        )

        # create two columns for charts
        fig_col1, fig_col2 = st.columns(2)
        with fig_col1:
            st.markdown("### First Chart")
            fig = px.density_heatmap(
                data_frame=df, y="age_new", x="marital"
            )
            st.write(fig)
            
        with fig_col2:
            st.markdown("### Second Chart")
            fig2 = px.histogram(data_frame=df, x="age_new")
            st.write(fig2)

        st.markdown("### Detailed Data View")
        st.dataframe(df)
        time.sleep(1)

