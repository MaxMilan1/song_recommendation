import streamlit as st
from clustering import *


def main():
    st.title("Create Your Playlist")

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

    weather_code_to_num = {desc: code for code, desc in weather_codes.items()}
    weather_code = weather_code_to_num[weather_code]

    # Select length of playlist
    lengths = [1,2,4,6,8]
    playlist_length = st.selectbox("Select playlist length in (hours):", lengths)



    st.subheader("Generated Playlist")
    playlist = get_playlist(activity, weather_code, playlist_length)
    st.dataframe(playlist)

if __name__ == "__main__":
    main()
