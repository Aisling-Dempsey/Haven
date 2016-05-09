import requests
import json

def current_lat_long():
    """outputs current lat/long estimate as a tuple based upon user ip"""
    r = requests.get("http://freegeoip.net/json/")
    location = r.json()
    return (location['latitude'], location['longitude'])

