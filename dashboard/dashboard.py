import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
aotizhongxin_df = pd.read_csv('https://raw.githubusercontent.com/marceloreis/HTI/refs/heads/master/PRSA_Data_20130301-20170228/PRSA_Data_Aotizhongxin_20130301-20170228.csv')

# Remove data for the year 2017
aotizhongxin_df = aotizhongxin_df[aotizhongxin_df['year'] != 2017]

# Convert 'year', 'month', 'day' into a single datetime column for easier filtering
aotizhongxin_df['date'] = pd.to_datetime(aotizhongxin_df[['year', 'month', 'day']])

# Title of the dashboard
st.title("Aotizhongxin Air Quality and Weather Dashboard")

# Sidebar for selecting date range filter
st.sidebar.header("Filters")
start_date = st.sidebar.date_input("Select Start Date", min_value=aotizhongxin_df['date'].min(), max_value=aotizhongxin_df['date'].max(), value=aotizhongxin_df['date'].min())
end_date = st.sidebar.date_input("Select End Date", min_value=start_date, max_value=aotizhongxin_df['date'].max(), value=aotizhongxin_df['date'].max())

# Filter dataset based on the selected date range
filtered_data = aotizhongxin_df[(aotizhongxin_df['date'] >= pd.to_datetime(start_date)) & (aotizhongxin_df['date'] <= pd.to_datetime(end_date))]

st.write(f"Showing data from {start_date} to {end_date}:")
st.dataframe(filtered_data)

# ----------------------------- 1. Temperature Trend -----------------------------
st.subheader("Daily Average Temperature Trend")
temperature_trend = filtered_data.groupby(['year', 'month', 'day'])['TEMP'].mean().reset_index()
temperature_trend['date'] = pd.to_datetime(temperature_trend[['year', 'month', 'day']])

# Plot temperature trend
plt.figure(figsize=(10, 6))
sns.lineplot(data=temperature_trend, x='date', y='TEMP', hue='year', palette='tab10')
plt.title(f"Average Daily Temperature from {start_date} to {end_date}")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
st.pyplot(plt)

# ----------------------------- 2. Wind Effect on Extreme Temperatures -----------------------------
st.subheader("Wind Effect on Extreme Temperatures (High and Low)")

# Scatter plot of wind speed and direction vs extreme temperatures
plt.figure(figsize=(10, 6))

# Plot wind speed vs max temperature (suhu maksimum)
sns.scatterplot(data=filtered_data, x='WSPM', y='TEMP', hue='WSPM', palette='coolwarm', size='WSPM', sizes=(20, 200))
plt.title(f"Wind Speed vs Temperature from {start_date} to {end_date}")
plt.xlabel("Wind Speed (km/h)")
plt.ylabel("Temperature (°C)")
st.pyplot(plt)

# ----------------------------- 3. Seasonal Patterns of Max and Min Temperatures -----------------------------
st.header("Pola Musiman Suhu Maksimum dan Minimum (2013–2016)")

# Pastikan filter waktu diterapkan ke df
aotizhongxin_df['month_name'] = aotizhongxin_df['month'].map({
    1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun",
    7: "Jul", 8: "Aug", 9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"
})

# Hitung suhu maksimum dan minimum harian
daily_temp = aotizhongxin_df.groupby(['year', 'month', 'day']).agg({
    'TEMP': ['min', 'max']
}).reset_index()
daily_temp.columns = ['year', 'month', 'day', 'min_temp', 'max_temp']
daily_temp['month_name'] = daily_temp['month'].map({
    1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun",
    7: "Jul", 8: "Aug", 9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"
})

# Buat boxplot suhu minimum
st.subheader("Pola Musiman terhadap Suhu Minimum per Bulan")
fig_min, ax_min = plt.subplots(figsize=(10, 5))
sns.boxplot(x='month_name', y='min_temp', data=daily_temp,
            order=["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                   "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], ax=ax_min)
ax_min.set_xlabel("Bulan")
ax_min.set_ylabel("Suhu Minimum (°C)")
ax_min.set_title("Pola Musiman terhadap Suhu Minimum")
st.pyplot(fig_min)

# Buat boxplot suhu maksimum
st.subheader("Pola Musiman terhadap Suhu Maksimum per Bulan")
fig_max, ax_max = plt.subplots(figsize=(10, 5))
sns.boxplot(x='month_name', y='max_temp', data=daily_temp,
            order=["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                   "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], ax=ax_max)
ax_max.set_xlabel("Bulan")
ax_max.set_ylabel("Suhu Maksimum (°C)")
ax_max.set_title("Pola Musiman terhadap Suhu Maksimum")
st.pyplot(fig_max)