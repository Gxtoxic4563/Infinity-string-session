# Copyright (C) 2024 by Badhacker98@Github, < https://github.com/Badhacker98 >.
#
# This file is part of < https://github.com/Badhacker98/StringBot > project,
# and is released under the license agreement specified in:
# < https://github.com/Badhacker98/StringBot/blob/main/LICENSE >
#
# All rights reserved.

import config
import time
import logging
import asyncio
from pyrogram import Client, idle
from pyromod import listen  
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid

# Configure logging
logging.basicConfig(
    level=logging.WARNING,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# Track start time
StartTime = time.time()

# Initialize Pyrogram Client
app = Client(
    "Anonymous",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    in_memory=True,
    plugins=dict(root="StringBot"),
)

async def main():
    print("Starting StringBot...")
    try:
        await app.start()
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("❌ Your API_ID or API_HASH is invalid.")
    except AccessTokenInvalid:
        raise Exception("❌ Your BOT_TOKEN is invalid.")
    
    me = await app.get_me()
    print(f"✅ Bot started as @{me.username}")
    
    await idle()
    await app.stop()
    print("🛑 Stopping StringBot...")

if __name__ == "__main__":
    asyncio.run(main())