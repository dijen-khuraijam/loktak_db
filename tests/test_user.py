from models.user import UserModel, UserRole

print("--- RUNNING PYDANTIC SCHEMA TESTS ---")

# 1. Test standard successful user creation
try:
    valid_user = UserModel(
        name="Dijen Khuraijam",
        email="dijen@example.com",
        phone="+919876543210",
        role=UserRole.admin,
        password_hash="supersecretencryptedstring",
        location={"type": "Point", "coordinates": [93.8, 24.6]} # Loktak area roughly
    )
    print("✅ Success: Valid user created perfectly!")
    print(f"   Timestamp generated: {valid_user.created_at}")
except Exception as e:
    print(f"❌ Failure: Valid data broke: {e}")

print("\n--- TEST INVALID DATA CATCHING ---")

# 2. Test what happens if someone provides a bad email address format or fake role
try:
    invalid_user = UserModel(
        name="Bad Email Test",
        email="not-an-email-address", # Should fail validation
        phone="12345",
        role="not_a_real_role",       # Should fail enum check
        password_hash="12345"
    )
except Exception as e:
    print("✅ Success: Pydantic caught the bad data successfully!")
    print(e)