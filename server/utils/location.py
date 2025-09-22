import requests
import json
from typing import Tuple, Optional

class Geocoder:
    def __init__(self):
        self.nominatim_url = "https://nominatim.openstreetmap.org/search"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
    
    def geocode_address(self, address: str) -> Optional[Tuple[float, float, dict]]:
        """
        Convert address to latitude and longitude using OpenStreetMap Nominatim
        
        Args:
            address (str): The address to geocode
            
        Returns:
            Tuple[float, float, dict] or None: (latitude, longitude, full_data) or None if not found
        """
        params = {
            'q': address,
            'format': 'json',
            'limit': 1
        }
        
        try:
            response = requests.get(self.nominatim_url, params=params, headers=self.headers, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            if not data:
                print(f"No results found for address: {address}")
                return None
            
            location = data[0]
            lat = float(location['lat'])
            lon = float(location['lon'])
            
            return lat, lon, location
            
        except requests.exceptions.RequestException as e:
            print(f"Error making API request: {e}")
            return None
        except (KeyError, IndexError, ValueError) as e:
            print(f"Error parsing response: {e}")
            return None

def main():
    geocoder = Geocoder()
    
    print("=== Address to Coordinates Converter ===")
    print("Enter an address to get its latitude and longitude")
    print("Type 'quit' to exit\n")
    
    while True:
        address = input("Enter address: ").strip()
        
        if address.lower() in ['quit', 'exit', 'q']:
            print("Goodbye!")
            break
            
        if not address:
            print("Please enter a valid address.")
            continue
        
        print(f"Searching for: {address}")
        
        result = geocoder.geocode_address(address)
        
        if result:
            lat, lon, full_data = result
            print(f"\n📍 Location Found:")
            print(f"Latitude: {lat}")
            print(f"Longitude: {lon}")
            print(f"Display Name: {full_data.get('display_name', 'N/A')}")
            print(f"Type: {full_data.get('type', 'N/A')}")
            print(f"Importance: {full_data.get('importance', 'N/A')}")
            print("-" * 50)
        else:
            print("❌ Could not find coordinates for the given address.\n")

if __name__ == "__main__":
    main()