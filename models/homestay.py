from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime, timezone

class GeoPoint(BaseModel):
    type: str = "Point"
    coordinates: list[float]

class HomestayModel(BaseModel):
    host_id: str
    title: str
    description: str
    location: GeoPoint
    address: str
    price_per_night: float
    images: List[str] = []
    amenities: List[str] = []
    whatsapp_link: str
    is_verified: bool = False
    is_available: bool = True
    
    # Generates a fresh UTC timestamp the moment a host lists their property
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))