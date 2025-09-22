from faker import Faker
import json
import random

fake = Faker()

def generate_ngo():
    return {
        "id": f"NGO-{fake.uuid4().split('-')[0].upper()}",
        "name": fake.company(),
        "location": fake.city(),
        "coordinates": {
            "lat": round(random.uniform(8.0, 37.0), 4),
            "lng": round(random.uniform(68.0, 97.0), 4)
        },
        "resources": {
            "food": random.randint(500, 5000),
            "water": random.randint(500, 5000),
            "medicine": random.randint(100, 1000)
        },
        "contact": {
            "email": fake.email(),
            "phone": fake.phone_number()
        }
    }

ngos = [generate_ngo() for _ in range(10000)]

with open(r'C:/Git projects/Disaster-Relief-Simulation/server/data/ngos.json', 'w') as f:
    json.dump(ngos, f, indent=4)

print("ngos.json file with 10,000 entries has been generated.")
