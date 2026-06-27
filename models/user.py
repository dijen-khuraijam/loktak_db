from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from enum import Enum
from datetime import datetime, timezone

class UserRole(str, Enum):
    tourist      = "tourist"
    host         = "host"
    cleanup_crew = "cleanup_crew"
    admin        = "admin"

class GeoPoint(BaseModel):
    type: str = "Point"
    coordinates: list[float]   # [longitude, latitude]

class UserModel(BaseModel):
    name: str
    email: EmailStr
    phone: str
    role: UserRole
    password_hash: str
    location: Optional[GeoPoint] = None
    whatsapp_number: Optional[str] = None
    is_verified: bool = False
    # This ensures a fresh, clean UTC timestamp is generated for every unique user
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class UserResponse(BaseModel):
    """What the API returns — never expose password_hash"""
    id: str
    name: str
    email: str
    phone: str
    role: UserRole
    is_verified: bool
    created_at: datetime