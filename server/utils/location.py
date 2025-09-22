import requests
import json
from typing import Tuple, Optional, List, Dict

class Geocoder:
    def __init__(self, json_file_path: str = "ngos.json"):
        self.nominatim_url = "https://nominatim.openstreetmap.org/search"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        self.json_file_path = json_file_path
        self.ngos_data = self.load_ngos_data()
    
    def load_ngos_data(self) -> List[Dict]:
        """Load NGO data from JSON file"""
        try:
            with open(self.json_file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: JSON file '{self.json_file_path}' not found.")
            return []
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON file: {e}")
            return []
    
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
    
    def find_nearest_ngos(self, target_lat: float, target_lng: float, max_results: int = 5, max_distance: float = 1.0) -> List[Dict]:
        """
        Find NGOs near the given coordinates using Haversine formula
        
        Args:
            target_lat (float): Target latitude
            target_lng (float): Target longitude
            max_results (int): Maximum number of results to return
            max_distance (float): Maximum distance in kilometers
            
        Returns:
            List[Dict]: List of nearby NGOs sorted by distance
        """
        from math import radians, sin, cos, sqrt, atan2
        
        def haversine(lat1, lng1, lat2, lng2):
            """Calculate distance between two points using Haversine formula"""
            R = 6371  # Earth radius in kilometers
            
            lat1_rad = radians(lat1)
            lat2_rad = radians(lat2)
            delta_lat = radians(lat2 - lat1)
            delta_lng = radians(lng2 - lng1)
            
            a = (sin(delta_lat/2) * sin(delta_lat/2) + 
                 cos(lat1_rad) * cos(lat2_rad) * 
                 sin(delta_lng/2) * sin(delta_lng/2))
            c = 2 * atan2(sqrt(a), sqrt(1-a))
            
            return R * c
        
        nearby_ngos = []
        
        for ngo in self.ngos_data:
            ngo_lat = ngo['coordinates']['lat']
            ngo_lng = ngo['coordinates']['lng']
            
            distance = haversine(target_lat, target_lng, ngo_lat, ngo_lng)
            
            if distance <= max_distance:
                ngo_copy = ngo.copy()
                ngo_copy['distance_km'] = round(distance, 2)
                nearby_ngos.append(ngo_copy)
        
        # Sort by distance and return top results
        nearby_ngos.sort(key=lambda x: x['distance_km'])
        return nearby_ngos[:max_results]
    
    def search_ngos_by_name_or_location(self, search_term: str, max_results: int = 5) -> List[Dict]:
        """
        Search NGOs by name or location name
        
        Args:
            search_term (str): Term to search for in NGO names or locations
            max_results (int): Maximum number of results to return
            
        Returns:
            List[Dict]: Matching NGOs
        """
        search_term_lower = search_term.lower()
        matches = []
        
        for ngo in self.ngos_data:
            if (search_term_lower in ngo['name'].lower() or 
                search_term_lower in ngo['location'].lower()):
                matches.append(ngo)
                
                if len(matches) >= max_results:
                    break
        
        return matches

def main():
    geocoder = Geocoder("ngos.json")  # Make sure the path is correct
    
    print("=== NGO Location Search ===")
    print("1. Search by address to find nearby NGOs")
    print("2. Search NGOs by name or location")
    print("Type 'quit' to exit\n")
    
    while True:
        choice = input("Choose search method (1 or 2): ").strip()
        
        if choice.lower() in ['quit', 'exit', 'q']:
            print("Goodbye!")
            break
        
        if choice == '1':
            # Search by address
            address = input("Enter address: ").strip()
            
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
                print("-" * 50)
                
                # Find nearby NGOs
                print("\n🔍 Searching for nearby NGOs...")
                nearby_ngos = geocoder.find_nearest_ngos(lat, lon, max_results=5, max_distance=50.0)
                
                if nearby_ngos:
                    print(f"Found {len(nearby_ngos)} NGO(s) within 50 km:")
                    print("=" * 60)
                    
                    for i, ngo in enumerate(nearby_ngos, 1):
                        print(f"\n{i}. {ngo['name']}")
                        print(f"   Location: {ngo['location']}")
                        print(f"   Distance: {ngo['distance_km']} km")
                        print(f"   Coordinates: ({ngo['coordinates']['lat']}, {ngo['coordinates']['lng']})")
                        print(f"   Resources - Food: {ngo['resources']['food']}, "
                              f"Water: {ngo['resources']['water']}, "
                              f"Medicine: {ngo['resources']['medicine']}")
                        print(f"   Contact: {ngo['contact']['phone']} | {ngo['contact']['email']}")
                        print(f"   ID: {ngo['id']}")
                else:
                    print("❌ No NGOs found within 50 km radius.")
                
            else:
                print("❌ Could not find coordinates for the given address.")
        
        elif choice == '2':
            # Search by NGO name or location
            search_term = input("Enter NGO name or location to search: ").strip()
            
            if not search_term:
                print("Please enter a search term.")
                continue
            
            print(f"Searching for: {search_term}")
            matches = geocoder.search_ngos_by_name_or_location(search_term, max_results=5)
            
            if matches:
                print(f"\nFound {len(matches)} matching NGO(s):")
                print("=" * 60)
                
                for i, ngo in enumerate(matches, 1):
                    print(f"\n{i}. {ngo['name']}")
                    print(f"   Location: {ngo['location']}")
                    print(f"   Coordinates: ({ngo['coordinates']['lat']}, {ngo['coordinates']['lng']})")
                    print(f"   Resources - Food: {ngo['resources']['food']}, "
                          f"Water: {ngo['resources']['water']}, "
                          f"Medicine: {ngo['resources']['medicine']}")
                    print(f"   Contact: {ngo['contact']['phone']} | {ngo['contact']['email']}")
                    print(f"   ID: {ngo['id']}")
            else:
                print("❌ No NGOs found matching your search.")
        
        else:
            print("Invalid choice. Please enter 1 or 2.")
        
        print("\n" + "=" * 60 + "\n")

if __name__ == "__main__":
    main()