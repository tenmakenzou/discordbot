import discord
from sitish import *
from discord.ext import commands




intents = discord.Intents.all()
client = commands.Bot(command_prefix = '/',intents=intents)




@client.event
async def on_ready():
    print("bot is ready!")
    
@client.command()
async def hello(ctx):
    await ctx.send("test")
    

@client.command()
async def sitish(ctx):
     
     await ctx.send(get_current_day_and_week())

@client.command()
async def menu(ctx,arg):
     
    
     await ctx.send(get_menu(arg))

@client.command()
async def clear (ctx, limit: int):
        await ctx.channel.purge(limit=limit+1)

client.run('token here')

