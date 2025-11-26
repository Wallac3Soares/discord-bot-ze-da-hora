import discord
from discord.ext import commands, tasks
import datetime
import pytz
import os

TOKEN = os.environ.get("DISCORD_TOKEN")

if TOKEN is None:
    print("❌ ERRO: A variável DISCORD_TOKEN não foi definida no Render!")
    exit()

CANAL_ID = 1266482204981067810
TZ = pytz.timezone("America/Sao_Paulo")

HORA_BOM_DIA = 7
HORA_BOA_NOITE = 22

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@tasks.loop(time=datetime.time(hour=HORA_BOM_DIA, minute=0, tzinfo=TZ))
async def bom_dia_task():
    canal = bot.get_channel(CANAL_ID)
    if canal:
        await canal.send("**Bom dia a todos!** 🌅")

@tasks.loop(time=datetime.time(hour=HORA_BOA_NOITE, minute=0, tzinfo=TZ))
async def boa_noite_task():
    canal = bot.get_channel(CANAL_ID)
    if canal:
        await canal.send("**Boa noite!** 🌙")

@bot.event
async def on_ready():
    print(f"Bot {bot.user} conectado com sucesso!")
    if not bom_dia_task.is_running():
        bom_dia_task.start()
    if not boa_noite_task.is_running():
        boa_noite_task.start()

@bot.command()
async def teste(ctx):
    await ctx.send("O Zé da Hora está **online e rodando pelo Render**! 🚀")

bot.run(TOKEN)
