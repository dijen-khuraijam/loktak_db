from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum
from datetime import datetime, timezone

class SOSStatus(str, Enum):
    active     = "active"
    dispatched = "dispatched"
    resolved   = "resolved"

class GeoPoint(BaseModel):
    type: str = "Point"
    coordinates: list[float]

class SOSAlertModel(BaseModel):
    user_id: str
    location: GeoPoint
    gps_accuracy: Optional[float] = None
    message: str
    status: SOSStatus = SOSStatus.active
    dispatched_to: Optional[str] = None
    
    # Generates a fresh UTC timestamp for each specific alert
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))