import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set(style='dark')

def load_data():
    hour_df = pd.read_csv('clean_hour.csv')
    day_df = pd.read_csv('clean_day.csv')

    hour_df["date"] = pd.to_datetime(hour_df["date"])
    day_df["date"] = pd.to_datetime(day_df["date"])

    return hour_df, day_df

hour_df, day_df = load_data()


# Sidebar Filters
st.sidebar.header("Filter Data")

min_date =day_df["date"].min()
max_date =day_df["date"].max()

start_date, end_date = st.sidebar.date_input(
    label="Rentang Waktu",
    min_value=min_date,
    max_value=max_date,
    value=[min_date, max_date]
)

filtered_day_df = day_df[(day_df["date"] >= pd.to_datetime(start_date)) & 
                         (day_df["date"] <= pd.to_datetime(end_date))]

# Dashboard Title
st.title("🚲 Bike Sharing Dashboard")
st.markdown("---")

# Total Orders & Revenue
col1, col2 = st.columns(2)
with col1:
    st.metric("Total Peminjaman Sepeda", int(filtered_day_df["total_count"].sum()))
with col2:
    st.metric("Total Registered Users", int(filtered_day_df["registered"].sum()))

st.markdown("---")

# Jumlah Peminjaman Per Jam
st.subheader("Jumlah Peminjaman Per Jam")
hour_df.groupby("hours")["total_count"].sum()

fig, ax = plt.subplots(figsize=(10, 5))
hour_df.groupby("hours")["total_count"].sum().plot(kind="bar", color="skyblue", edgecolor="black")
ax.set_xlabel("Jam")
ax.set_ylabel("Total Peminjaman")
ax.set_title("Peminjaman Bike Per Jam")
ax.set_xticks(range(0, 24))
ax.set_xticklabels(range(0, 24))
st.pyplot(fig)

st.markdown("---")

# Perbandingan Jumlah Peminjaman Bike per Bulan
st.subheader("Perbandingan Jumlah Peminjaman Bike per Bulan")

day_df["date"] = pd.to_datetime(day_df["date"])

fig, ax = plt.subplots(figsize=(12, 6))
day_df.resample("M", on="date")[["registered", "casual"]].sum().rename_axis("Bulan").plot(
    kind="bar", ax=ax
)
ax.set_xlabel("Bulan")
ax.set_ylabel("Jumlah Peminjaman")
ax.set_title("Perbandingan Jumlah Peminjaman Bike per Bulan")
ax.legend(["Registered", "Casual"])
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
ax.grid(axis="y")
st.pyplot(fig)

st.markdown("---")

# Analisis RFM
st.subheader("Analisis RFM (Recency, Frequency, Monetary)")
current_date = day_df["date"].max()

rfm_df = day_df.groupby("registered").agg({
    "date": lambda x: (current_date - x.max()).days, 
    "instant": "count",
    "total_count": "sum"
}).rename(columns={"instant": "TransactionCount"}).reset_index()

rfm_df.columns = ["registered", "Recency", "Frequency", "Monetary"]

rfm_df.columns = ["User ID", "Recency", "Frequency", "Monetary"]


fig, ax = plt.subplots(1, 3, figsize=(20, 5))

sns.barplot(y="Recency", x="User ID", data=rfm_df.nsmallest(5, "Recency"), ax=ax[0], palette="Blues_r")
ax[0].set_title("Recency (days)")

sns.barplot(y="Frequency", x="User ID", data=rfm_df.nlargest(5, "Frequency"), ax=ax[1], palette="Greens_r")
ax[1].set_title("Frequency")

sns.barplot(y="Monetary", x="User ID", data=rfm_df.nlargest(5, "Monetary"), ax=ax[2], palette="Reds_r")
ax[2].set_title("Monetary")

st.pyplot(fig)

st.markdown("---")

# Clustering Peminjaman Bike Berdasarkan Waktu
st.subheader("Persentase Peminjaman Bike Berdasarkan Kategori Waktu")

def categorize_time(hour):
    if 6 <= hour < 12:
        return "Pagi"
    elif 12 <= hour < 18:
        return "Siang"
    elif 18 <= hour < 24:
        return "Malam"
    else:
        return "Dini Hari"

hour_df["time_category"] = hour_df["hours"].apply(categorize_time)
time_category_totals = hour_df.groupby("time_category", as_index=False)["total_count"].sum()

if not time_category_totals.empty:
    fig, ax = plt.subplots(figsize=(8, 8))
    colors = ["#ff9999", "#66b3ff", "#99ff99", "#ffcc99"]
    
    plt.pie(time_category_totals["total_count"], labels=time_category_totals["time_category"], 
            autopct="%1.1f%%", colors=colors, startangle=140, wedgeprops={"edgecolor": "black"})
    
    plt.title("Persentase Peminjaman Bike Berdasarkan Kategori Waktu")
    st.pyplot(fig)
else:
    st.warning("Tidak ada data untuk ditampilkan dalam pie chart.")

st.markdown("---")
st.write("Dashboard ini dibuat menggunakan Streamlit untuk menganalisis data peminjaman bike.")
