# app.py

# Import Streamlit and other necessary modules
import streamlit as st
from api.meteostat_api import fetch_climate_data
from frontend.layout import create_header, create_date_slider, create_sidebar
from frontend.charts import create_temperature_chart, create_precipitation_chart, create_windspeed_chart, create_pressure_chart, create_winddirection_chart


# Initialize the Streamlit app
from datetime import datetime

def main():
    create_header()
    selected_date_range = create_date_slider()
    create_sidebar()

    # Convert selected dates to datetime format for the API call
    start_date = datetime.combine(selected_date_range[0], datetime.min.time())

    end_date = datetime.combine(selected_date_range[1], datetime.min.time())

    # Fetch climate data using the Meteostat API
    climate_data = fetch_climate_data(6.5244, 3.3792, start_date, end_date)  # Example coordinates for Lagos, Nigeria

    # Display the climate data
    st.write(climate_data)

    # Create a temperature chart
    temperature_chart = create_temperature_chart(climate_data)

    # Display the chart
    st.plotly_chart(temperature_chart)

    # Create a precipitation chart
    precipitation_chart = create_precipitation_chart(climate_data)

    # Display the chart
    st.plotly_chart(precipitation_chart)

    # Create a windspeed chart
    windspeed_chart = create_windspeed_chart(climate_data)

    # Display the chart
    st.plotly_chart(windspeed_chart)

    # Create a pressure chart
    pressure_chart = create_pressure_chart(climate_data)

    # Display the chart
    st.plotly_chart(pressure_chart)

    # Create a winddirection chart
    winddirection_chart = create_winddirection_chart(climate_data)

    # Display the chart
    st.plotly_chart(winddirection_chart)

    




if __name__ == '__main__':
    main()
