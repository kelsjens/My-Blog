import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ————— Load & Preprocess —————
@st.cache_data
def load_data():
    df = pd.read_csv("flights_data.csv", parse_dates=["scheduledTime", "actualTime"])
    df["delay"] = (df["actualTime"] - df["scheduledTime"]).dt.total_seconds() / 60
    df["Day"] = df["scheduledTime"].dt.day_name()
    df["Delayed_Over_25"] = df["delay"] > 25
    return df

df = load_data()
sns.set_style("whitegrid")
# ————— App Header —————


# ————— Sidebar Navigation —————
st.sidebar.title("SLC Flight Delays (May 2024)")
page = st.sidebar.selectbox(
    "Choose a View",
    ["Average Delay by Airline", "Delay % by Airline & Day", "Departure Time vs. Delay", "Delay by Hour"]
)

# ————— View 1 —————
if page == "Average Delay by Airline":
    st.header("Average Delay by Airline")
    avg_delays = df.groupby('airline')['delay'].mean().sort_values(ascending=False)

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=avg_delays.index, y=avg_delays.values, ax=ax)
    ax.set_ylabel("Average Delay (minutes)")
    ax.set_xlabel("Airline")
    plt.xticks(rotation=45)
    st.pyplot(fig)

# ————— View 2 —————
elif page == "Delay % by Airline & Day":
    st.header("Delay % >25 min by Airline & Day")
    all_airlines = sorted(df['airline'].unique())
    all_days = sorted(df['Day'].unique())

    sel_airlines = st.sidebar.multiselect("Select Airlines", all_airlines, default=all_airlines)
    sel_days = st.sidebar.multiselect("Select Days", all_days, default=all_days)

    filtered = df[df['airline'].isin(sel_airlines) & df['Day'].isin(sel_days)]
    pct = (
        filtered.groupby(['airline', 'Day'])['Delayed_Over_25']
        .mean().mul(100).reset_index()
    )

    fig2, ax2 = plt.subplots(figsize=(10, 6))
    sns.barplot(data=pct, x='airline', y='Delayed_Over_25', hue='Day', ax=ax2)
    ax2.set_ylabel("Delay % (>25 min)")
    ax2.set_xlabel("Airline")
    plt.xticks(rotation=45)
    ax2.legend(title="Day of Week", bbox_to_anchor=(1.05, 1), loc="upper left")
    st.pyplot(fig2)

# ————— View 3 —————
elif page == "Departure Time vs. Delay":
    st.header("Departure Time vs. Delay")

    airline = st.sidebar.selectbox("Choose Airline", sorted(df['airline'].unique()))
    day = st.sidebar.selectbox("Choose Day of Week", sorted(df['Day'].unique()))

    scatter_df = df[(df['airline'] == airline) & (df['Day'] == day)].copy()
    scatter_df['sched_hour'] = (
        scatter_df['scheduledTime'].dt.hour +
        scatter_df['scheduledTime'].dt.minute / 60
    )

    fig3, ax3 = plt.subplots(figsize=(10, 6))
    ax3.scatter(scatter_df['sched_hour'], scatter_df['delay'], alpha=0.6)
    ax3.set_xlabel("Scheduled Hour")
    ax3.set_ylabel("Delay (minutes)")
    ax3.set_title(f"{airline} on {day}")
    st.pyplot(fig3)

elif page == "Delay by Hour":
    st.header("Average Delay by Hour")

    all_airlines = sorted(df['airline'].unique())
    airline = st.sidebar.selectbox("Choose Airline", all_airlines)

    df['Hour'] = df['scheduledTime'].dt.hour  # Add hour column if not already present
    sub = df[df["airline"] == airline]
    hourly = sub.groupby("Hour")["delay"].mean().reset_index()

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(data=hourly, x="Hour", y="delay", marker="o", ax=ax)
    ax.set_ylabel("Average Delay (minutes)")
    ax.set_xlabel("Scheduled Hour of Day")
    ax.set_xticks(range(0, 24))
    st.pyplot(fig)
