from models.homestay import HomestayModel

print("--- TESTING HOMESTAY MODEL ---")

try:
    homestay = HomestayModel(
        host_id="host_999",
        title="Floating Phumdi Retreat",
        description="Experience authentic life on the lake with this traditional floating homestay.",
        location={"type": "Point", "coordinates": [93.79, 24.55]},
        address="Near Sendra Island, Bishnupur District",
        price_per_night=1500.00,
        amenities=["Local Breakfast included", "Guided Boat Ride", "Solar power"],
        whatsapp_link="https://wa.me/919876543210"
    )
    print("✅ Success: Valid homestay listing created!")
    print(f"   Homestay: {homestay.title}")
    print(f"   Timestamp generated: {homestay.created_at}")
except Exception as e:
    print(f"❌ Failure on valid data: {e}")