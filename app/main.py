import streamlit as st

# Main entry point (this can be empty or configured for your app)
def main():

    st.title("XYLOS - Music Recommendation Demo")

    st.header("How It Works")
    st.write("""
        The platform allows users to:
        - Select an activity (e.g., Run, Hike, Yoga)
        - Choose the current weather conditions (e.g., Clear Sky, Rainy)
        - Get personalized music recommendations based on these choices.

        The system uses data analysis and clustering algorithms to predict the most suitable songs 
        for a given combination of activity and weather condition.
    """)


if __name__ == "__main__":
    main()