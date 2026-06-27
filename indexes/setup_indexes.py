import asyncio
from database import database

async def create_indexes():
    print("Creating indexes...")

    # ── Geospatial indexes ─────────────────────────────
    await database["pollution_reports"].create_index(
        [("location", "2dsphere")],
        name="location_2dsphere"
    )
    await database["homestays"].create_index(
        [("location", "2dsphere")],
        name="location_2dsphere"
    )
    await database["sos_alerts"].create_index(
        [("location", "2dsphere")],
        name="location_2dsphere"
    )
    await database["users"].create_index(
        [("location", "2dsphere")],
        name="location_2dsphere"
    )

    # ── Users indexes ──────────────────────────────────
    await database["users"].create_index(
        [("email", 1)],
        unique=True,
        name="email_unique"
    )
    await database["users"].create_index(
        [("phone", 1)],
        unique=True,
        name="phone_unique"
    )
    await database["users"].create_index(
        [("role", 1)],
        name="role_index"
    )

    # ── Pollution reports indexes ──────────────────────
    await database["pollution_reports"].create_index(
        [("status", 1)],
        name="status_index"
    )
    await database["pollution_reports"].create_index(
        [("created_at", -1)],
        name="created_at_desc"
    )

    # ── Homestays indexes ──────────────────────────────
    await database["homestays"].create_index(
        [("is_available", 1), ("is_verified", 1)],
        name="available_verified"
    )

    # ── SOS indexes ────────────────────────────────────
    await database["sos_alerts"].create_index(
        [("status", 1), ("created_at", -1)],
        name="status_created"
    )

    # ── Refresh tokens ─────────────────────────────────
    await database["refresh_tokens"].create_index(
        [("token", 1)],
        unique=True,
        name="token_unique"
    )
    await database["refresh_tokens"].create_index(
        [("user_id", 1)],
        name="user_id_index"
    )
    await database["refresh_tokens"].create_index(
        [("created_at", 1)],
        expireAfterSeconds=604800,   # auto-delete after 7 days
        name="ttl_index"
    )

    print("✅ All indexes created successfully!")

if __name__ == "__main__":
    asyncio.run(create_indexes())