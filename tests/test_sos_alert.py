from models.sos_alert import SOSAlertModel, SOSStatus

print("--- TESTING SOS ALERT MODEL ---")

try:
    alert = SOSAlertModel(
        user_id="tourist_001",
        location={"type": "Point", "coordinates": [93.82, 24.57]},
        gps_accuracy=15.5,
        message="Emergency: Stranded near Phumdi cluster."
    )
    print("✅ Success: SOS Alert created!")
    print(f"   Status: {alert.status}")
    print(f"   Created at: {alert.created_at}")
except Exception as e:
    print(f"❌ Failure: {e}")