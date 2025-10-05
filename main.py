import discord
from discord.ext import commands
import asyncio
import os
from dotenv import load_dotenv
from flask import Flask
import threading

# -----------------------------
# Charger les variables d'environnement
# -----------------------------
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# -----------------------------
# Configuration du bot
# -----------------------------
CHANNEL_ID = 1201189852889231451  # Salon à surveiller
AUTHOR_ID = 318312854816161792    # Auteur des messages à surveiller

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='?!?!', intents=intents)

# -----------------------------
# Événements du bot
# -----------------------------
@bot.event
async def on_ready():
    print(f"✅ React-o-Message connecté en tant que {bot.user}")

@bot.event
async def on_message(message):
    if message.channel.id == CHANNEL_ID and message.author.id == AUTHOR_ID:
        print("Message vu !")
        reactions = [
            "Monture:1038776048772452482",
            "Mage_Bleu:932505038557941780",
            "Carte:1038776186983161906",
            "Exp:1038799336999489536",
            "Donjon:1038799566977368125",
            "Raid:1038799568613154826",
            ":Beers:370593427580256256",
            "Zonerelique:1076894508664500334",
            "Chasse:1038809363286069318",
            "GoldSaucer:1099788883253788713",
            "Alea:1038799562028093550",
            "Baston:370591248085417984",
            "Event:1147955003005358212"
        ]
        for r in reactions:
            try:
                await message.add_reaction(r)
            except Exception as e:
                print(f"Erreur réaction {r}: {e}")

# -----------------------------
# Flask pour UptimeRobot
# -----------------------------
app = Flask("")

@app.route("/")
def home():
    return "Troisième bot is alive!"

def run_flask():
    app.run(host="0.0.0.0", port=8080)

threading.Thread(target=run_flask).start()

# -----------------------------
# Lancer le bot Discord
# -----------------------------
bot.run(TOKEN)
