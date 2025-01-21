import streamlit as st
import pandas as pd
from clustering import *
import plotly.express as px
 
def main():
    st.title("Visualization Clusters")
    data = pd.read_csv("app/cluster_data.csv")
    st.dataframe(data)

    #cluster the data based on the column "Cluster" and the count of them
    # Create the bar chart using Plotly
    # fig = px.bar(data_frame=data, x=data["Cluster"].value_counts().index, y=data["Cluster"].value_counts().values, 
    #             labels={'x': 'Cluster', 'y': 'Count'},
    #             title='Cluster Distribution')

    # # Customize the layout for better aesthetics
    # fig.update_layout(
    #     plot_bgcolor='rgba(0,0,0,0)',  # Transparent background
    #     xaxis_title='Cluster',
    #     yaxis_title='Count',
    #     template='plotly_dark',  # Dark theme
    #     xaxis=dict(tickmode='linear', tickangle=45),  # Improve readability of x-axis labels
    #     yaxis=dict(tickformat='d')  # Format y-axis as integer
    # )

    # # Display the figure
    # st.plotly_chart(fig)

    # # Get the clusters
    activities = [
        "Run",
        "Rowing",
        "Hike",
        "Workout",
        "Walk",
        "Snowboard",
        "Ride",
        "WaterSport",
        "AlpineSki",
        "StandUpPaddling",
        "Kitesurf",
        "InlineSkate",
        "Yoga",
        "Kayaking",
        "Velomobile",
    ]

    # Define weather codes and their descriptions
    weather_codes = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Depositing rime fog",
        51: "Drizzle: Light",
        53: "Drizzle: Moderate",
        55: "Drizzle: Dense intensity",
        56: "Drizzle: Light freezing",
        57: "Drizzle: Dense intensity freezing",
        61: "Rain: Slight",
        63: "Rain: Moderate",
        65: "Rain: Heavy intensity",
        66: "Rain: Slightly freezing",
        67: "Rain: Heavy intensity freezing",
        71: "Snow fall: Slight",
        73: "Snow fall: Moderate",
        75: "Snow fall: Heavy intensity",
        77: "Snow grains",
        80: "Rain showers: Slight",
        81: "Rain showers: Moderate",
        82: "Rain showers: Heavy intensity",
        85: "Snow showers: Slight",
        86: "Snow showers: Heavy",
        95: "Thunderstorm: Slight or moderate",
        96: "Thunderstorm: Heavy hail",
        99: "Thunderstorm: Slight hail",

    }

    # Create a dropdown for selecting the activity type
    activity = st.selectbox("Select an activity type:", activities)

    # Create a dropdown for selecting the weather code
    weather_code = st.selectbox(
        "Select a weather condition:", 
        [f"{desc}" for code, desc in weather_codes.items()]
    )

    weather_code_to_num = {desc: code for code, desc in weather_codes.items()}
    weather_code = weather_code_to_num[weather_code]

    #Show the process of the clustering steps.
    encoded_activity, data, predicted_cluster, songs = recommendation_split(activity, weather_code)

    st.write("The data that will be used to predict the cluster: (encoded activity + Weather_Code)",data)

    st.write("The predicted cluster: ", predicted_cluster)

    st.write("All the songs in the predicted cluster: ")
    st.dataframe(songs)

 
if __name__ == "__main__":
    main()