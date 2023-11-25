import os
from typing import Tuple

from dotenv import load_dotenv
import googlemaps

load_dotenv()

KEY = os.getenv("GOOGLE_API_KEY")


def get_geocode_location(address: str) -> Tuple[float, float]:
    gmaps = googlemaps.Client(key=KEY)
    # Geocoding an address
    geocode_result = gmaps.geocode(address)

    lat = geocode_result[0]["geometry"]["location"]["lat"]
    lng = geocode_result[0]["geometry"]["location"]["lng"]

    return lat, lng


if __name__ == "__main__":
    address = "21286 Mission BLVD, Hayward CA 94541"
    print(get_geocode_location(address))
