from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum
from datetime import datetime, timezone

class HazardType(str, Enum):
    plastic           = "plastic"
    oil_spill         = "oil_spill"
    sewage            = "sewage"
    phumdi_overgrowth = "phumdi_overgrowth" 
    other             = "other"

class Severity(str, Enum):
    low    = "low"
    medium = "medium"
    high   = "high"

class ReportStatus(str, Enum):
    pending  = "pending"
    assigned = "assigned"
    resolved = "resolved"

class GeoPoint(BaseModel):
    type: str = "Point"
    coordinates: list[float]

class PollutionReportModel(BaseModel):
    reported_by: str 
    location: GeoPoint
    hazard_type: HazardType
    severity: Severity
    description: str
    images: List[str] = []
    status: ReportStatus = ReportStatus.pending
    assigned_crew: Optional[str] = None
    
    # Generates a fresh UTC timestamp the exact moment a report is fired
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    resolved_at: Optional[datetime] = None