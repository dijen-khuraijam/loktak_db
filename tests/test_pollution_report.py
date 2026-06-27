from models.pollution_report import PollutionReportModel, HazardType, Severity

print("--- TESTING POLLUTION REPORT MODEL ---")

# 1. Test a Valid Report
try:
    valid_report = PollutionReportModel(
        reported_by="user_12345",
        location={"type": "Point", "coordinates": [93.8123, 24.5511]}, 
        hazard_type=HazardType.plastic,
        severity=Severity.high,
        description="Massive plastic accumulation blocking the waterway.",
        images=["url_to_image_1.jpg"]
    )
    print("✅ Success: Valid report created!")
    print(f"   Status defaulted to: {valid_report.status}")
    print(f"   Timestamp generated: {valid_report.created_at}")
except Exception as e:
    print(f"❌ Failure on valid data: {e}")

print("\n--- TEST INVALID DATA CATCHING ---")

# 2. Test Invalid Data (This should intentionally fail!)
try:
    invalid_report = PollutionReportModel(
        reported_by="user_12345",
        location={"type": "Point", "coordinates": ["not", "numbers"]}, # Bad coordinates
        hazard_type="not_a_real_hazard", # Not in Enum
        severity="extreme",              # Not in Enum
        description="This should fail"
    )
except Exception as e:
    print("✅ Success: Pydantic caught the bad data successfully!")
    print(e)