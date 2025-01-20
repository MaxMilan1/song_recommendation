import streamlit as st
from clustering import *

def main():
    # Set page title
    st.title("Activity and Weather Selection")

    # Define the list of activities
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

    # Display the selected activity and weather
    st.subheader("Your Selection")
    st.write(f"**Activity:** {activity}")
    st.write(f"**Weather Condition:** {weather_code}")

    st.subheader("Recommended playlist")

    # Define the recommended playlist for each activity and weather condition
    data = (activity, weather_code)

    

if __name__ == "__main__":
    main()