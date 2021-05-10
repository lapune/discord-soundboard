from time import sleep
import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import yaml

data = yaml.load(open('soundboard.yaml'), Loader=yaml.FullLoader)
print(data)

TOKEN = "ODMzOTcxMDc1MjE3MjI3ODM2.YH6GFg.foJS-_u4g0K9o9XqMZZBKNiXLn0"

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print("Il est déjà 9h ?!")

@client.command()
async def refresh(ctx):
    data = yaml.load(open('soundboard.yaml'), Loader=yaml.FullLoader)
    print(data)

@client.command()
async def hello(ctx):
    await ctx.send("Bonjour. C'est moi, Orson Welles. Ceci est ma maison que vous voyez, derrière, là. Pas mal, non ? C'est français.")

@client.command(pass_context = True)
async def join(ctx):
    if (ctx.author.voice):
        await ctx.send("Ok, j'arrive V12.")
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("Va dans un salon vocal, ducon. Signé l'Homme le plus classe du monde")

@client.command(pass_context = True)
async def p(ctx,arg):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio(data[arg])
        player = voice.play(source)
        print("playing "+arg)
        while voice.is_playing():
            sleep(.1)
        await voice.disconnect()
    else:
        await ctx.send("George n'est pas là (à changer)")

@client.command(pass_context = True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.send("Je préfère partir plutôt que d'entendre ça plutôt que d'être sourd.")
        await ctx.guild.voice_client.disconnect()
    else:
        await ctx.send("George n'est pas là (à changer)")

client.run(TOKEN)