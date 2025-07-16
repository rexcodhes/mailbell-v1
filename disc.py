from dotenv import load_dotenv
import os
import discord
from discord.ext import commands
import logging
import summary
import requests

def run_discord():
    load_dotenv()
    token = os.getenv("DISCORD_TOKEN")
    url = os.getenv("base_url")

    handler = logging.FileHandler(
        filename="discord.log",
        encoding="utf-8",
        mode="w"
    )

    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True

    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        print("Bot is ready")

    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return
        await bot.process_commands(message)

    @bot.command()
    async def meow(ctx):
        await ctx.send(f"Meow {ctx.author.mention}!")

    @bot.command()
    async def connectgmail(ctx):
        await ctx.send(f"Meow {ctx.author.mention}!")

    @bot.command()
    async def email(ctx):
        response = requests.get(f"{url}/mail")
        data = response.json()

        await ctx.author.send(data)

    bot.run(token, log_handler=handler, log_level=logging.DEBUG)

if __name__ == "__main__":
    run_discord()