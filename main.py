import os

import disnake
from disnake.ext import commands
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.environ.get("TOKEN")
GUILD_ID = int(os.environ.get("GUILD_ID"))


bot = commands.Bot(command_prefix="!", intents=disnake.Intents.all())
bot.remove_command("help")


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    print(f"Bot ID: {bot.user.id}")
    print(f"Guild ID: {GUILD_ID}")
    print(f"Total Guilds: {len(bot.guilds)}")

@bot.event
async def on_disconnect():
    print("Bot disconnected from Discord")

@bot.event
async def on_resumed():
    print("Bot resumed from Discord")


if __name__ == "__main__":
    if TOKEN is None or TOKEN == "":
        raise ValueError("TOKEN is not set in .env file")

    if GUILD_ID is None or GUILD_ID == "":
        raise ValueError("GUILD_ID is not set in .env file")

    bot.run(TOKEN)
