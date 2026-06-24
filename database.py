import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

# 1. Load the secret variables from your local .env file
load_dotenv()

# 2. Grab the connection string
MONGO_DETAILS = os.getenv("MONGO_URI")

# 3. Initialize the asynchronous MongoDB client
client = AsyncIOMotorClient(MONGO_DETAILS)

# 4. Connect to your specific database
database = client.loktak_db

# 5. Reference the collections you created in mongosh
user_collection = database.get_collection("users")
report_collection = database.get_collection("pollution_reports")
homestay_collection = database.get_collection("homestays")
sos_collection = database.get_collection("sos_alerts")

# 6. Helper function your teammate can run to verify the connection
async def ping_server():
    try:
        await client.admin.command('ping')
        print("Successfully connected to Loktak MongoDB!")
    except Exception as e:
        print(f"Database connection failed: {e}")