# Import required libraries
from meteostat import Point, Daily

# Define a function to fetch climate data for a specific location and time range
def fetch_climate_data(latitude, longitude, start_date, end_date):
    

    # Create a Point for the location
    location = Point(latitude, longitude, 70)

    # Get daily data for the specified time range
    data = Daily(location, start_date, end_date)
    data = data.fetch()

    # Select the required parameters
    data = data[['tavg', 'tmin', 'tmax', 'prcp', 'wspd', 'wdir', 'pres']]

    return data
