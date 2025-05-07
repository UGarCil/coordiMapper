'''
Coordinate_handler module to receive user input and produce a set of coordinates.
'''

import requests

# FD. get_coordinates()
def get_coordinates(location, wait=0.0):
    '''
    Get the coordinates of a given location using OpenStreetMap Nominatim API.
    wait is the time to wait between requests to avoid hitting the API too hard.
    '''
    url = 'https://nominatim.openstreetmap.org/search'
    params = {
        'q': location,
        'format': 'json',
        'limit': 1
    }
    headers = {
        'User-Agent': 'geo-coord-script'
    }
    
    if wait > 0:
        import time
        time.sleep(wait)
        
    response = requests.get(url, params=params, headers=headers)
    data = response.json()
    
    if data:
        lat = float(data[0]['lat'])
        lon = float(data[0]['lon'])
        return lat, lon
    else:
        return None, None

# How ot use:
if __name__ == "__main__":
    locations = ['St. Joan of Arc Catholic Academy - School']
    results = {loc: get_coordinates(loc) for loc in locations}
    print(results)
