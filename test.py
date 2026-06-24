import asyncio
from database import ping_server

async def test():
    print("Testing connection...")
    await ping_server()

if __name__ == "__main__":
    asyncio.run(test())