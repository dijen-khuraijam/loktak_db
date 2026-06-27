import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio
from database import database
from datetime import datetime, timezone

async def seed():
    now = datetime.now(timezone.utc)

    print("Seeding database...")

    # Clear old seed data
    await database["users"].delete_many({})
    await database["pollution_reports"].delete_many({})
    await database["homestays"].delete_many({})
    await database["sos_alerts"].delete_many({})
    print("Old data cleared!")

    # Seed users
    await database["users"].insert_many([
        {
            "name": "Tomba Singh",
            "email": "tomba@seed.com",
            "phone": "+919876543210",
            "role": "tourist",
            "password_hash": "hashed_pw_1",
            "location": {"type": "Point", "coordinates": [93.77, 24.53]},
            "is_verified": True,
            "created_at": now
        },
        {
            "name": "Ibemhal Devi",
            "email": "ibemhal@seed.com",
            "phone": "+919876543211",
            "role": "host",
            "password_hash": "hashed_pw_2",
            "location": {"type": "Point", "coordinates": [93.76, 24.54]},
            "whatsapp_number": "+919876543211",
            "is_verified": True,
            "created_at": now
        },
        {
            "name": "Ranjit Meetei",
            "email": "ranjit@seed.com",
            "phone": "+919876543212",
            "role": "cleanup_crew",
            "password_hash": "hashed_pw_3",
            "location": {"type": "Point", "coordinates": [93.78, 24.52]},
            "is_verified": True,
            "created_at": now
        }
    ])

    # Seed pollution reports
    await database["pollution_reports"].insert_many([
        {
            "location": {"type": "Point", "coordinates": [93.77, 24.53]},
            "hazard_type": "plastic",
            "severity": "high",
            "description": "SEED - Plastic dump near phumdis",
            "images": [],
            "status": "pending",
            "created_at": now
        },
        {
            "location": {"type": "Point", "coordinates": [93.78, 24.54]},
            "hazard_type": "oil_spill",
            "severity": "medium",
            "description": "SEED - Oil spill near boat dock",
            "images": [],
            "status": "assigned",
            "created_at": now
        }
    ])

    # Seed homestay
    await database["homestays"].insert_one({
        "title": "SEED - Lakeside Hut near Sendra",
        "description": "Beautiful view of Loktak Lake",
        "location": {"type": "Point", "coordinates": [93.76, 24.54]},
        "address": "Moirang, Manipur",
        "price_per_night": 800,
        "amenities": ["meals", "boat"],
        "whatsapp_link": "https://wa.me/919876543211",
        "is_verified": True,
        "is_available": True,
        "created_at": now
    })

    # Seed SOS alert
    await database["sos_alerts"].insert_one({
        "location": {"type": "Point", "coordinates": [93.79, 24.51]},
        "gps_accuracy": 5.2,
        "message": "SEED - Boat engine failed near Keibul",
        "status": "active",
        "created_at": now
    })

    print("✅ Seed data inserted!")

if __name__ == "__main__":
    asyncio.run(seed())