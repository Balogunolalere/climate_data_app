import matplotlib.pyplot as plt
import plotly.express as px


def create_temperature_chart(climate_data):
    """
    Create a temperature chart using the climate data.

    Parameters:
    climate_data (DataFrame): The climate data to use for the chart.

    Returns:
    Plotly chart: A temperature chart.
    """
    # Create a line chart
    temperature_chart = px.line(
        climate_data,
        x=climate_data.index,
        y='tavg',
        title='Temperature'
    )

    # Customize the chart layout
    temperature_chart.update_layout(
        xaxis_title='Date',
        yaxis_title='Temperature (°C)',
        showlegend=False
    )

    return temperature_chart

#Precipitation
def create_precipitation_chart(climate_data):
    """
    Create a precipitation chart using the climate data.

    Parameters:
    climate_data (DataFrame): The climate data to use for the chart.

    Returns:
    Plotly chart: A precipitation chart.
    """
    # Create a line chart
    precipitation_chart = px.line(
        climate_data,
        x=climate_data.index,
        y='prcp',
        title='Precipitation'
    )

    # Customize the chart layout
    precipitation_chart.update_layout(
        xaxis_title='Date',
        yaxis_title='Precipitation (mm)',
        showlegend=False
    )

    return precipitation_chart

#Wind Speed
def create_windspeed_chart(climate_data):
    """
    Create a windspeed chart using the climate data.

    Parameters:
    climate_data (DataFrame): The climate data to use for the chart.

    Returns:
    Plotly chart: A windspeed chart.
    """
    # Create a line chart
    windspeed_chart = px.line(
        climate_data,
        x=climate_data.index,
        y='wspd',
        title='Windspeed'
    )

    # Customize the chart layout
    windspeed_chart.update_layout(
        xaxis_title='Date',
        yaxis_title='Windspeed (m/s)',
        showlegend=False
    )

    return windspeed_chart

#Wind Direction
def create_winddirection_chart(climate_data):
    """
    Create a winddirection chart using the climate data.

    Parameters:
    climate_data (DataFrame): The climate data to use for the chart.

    Returns:
    Plotly chart: A winddirection chart.
    """
    # Create a line chart
    winddirection_chart = px.line(
        climate_data,
        x=climate_data.index,
        y='wdir',
        title='Winddirection'
    )

    # Customize the chart layout
    winddirection_chart.update_layout(
        xaxis_title='Date',
        yaxis_title='Winddirection (°)',
        showlegend=False
    )

    return winddirection_chart

#Pressure
def create_pressure_chart(climate_data):
    """
    Create a pressure chart using the climate data.

    Parameters:
    climate_data (DataFrame): The climate data to use for the chart.

    Returns:
    Plotly chart: A pressure chart.
    """
    # Create a line chart
    pressure_chart = px.line(
        climate_data,
        x=climate_data.index,
        y='pres',
        title='Pressure'
    )

    # Customize the chart layout
    pressure_chart.update_layout(
        xaxis_title='Date',
        yaxis_title='Pressure (hPa)',
        showlegend=False
    )

    return pressure_chart

