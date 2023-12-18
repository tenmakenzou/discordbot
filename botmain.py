import discord
from sitish import *
from discord.ext import commands




intents = discord.Intents.all()
client = commands.Bot(command_prefix = '/',intents=intents)



##
@client.event
async def on_ready():
    print("Bot is running!")

"""
@client.command()
async def hello(ctx):
    await ctx.send("test")
"""

@client.command()
async def sitish(ctx,arg):
     
        await ctx.send(get_current_day_and_week(arg))
     

@client.command()
async def helpsitish(ctx):

#https://www.youtube.com/watch?v=wILcnFaO2lk&ab_channel=RichardSchwabe
    embed = discord.Embed(
      colour=discord.Colour.random(),       
     title="Bot Commands")  
    embed.set_author(name="Creator : tenma_kenzo_ + BladeZ (ez)",url = "https://ih0.redbubble.net/image.4837681105.5862/raf,360x360,075,t,fafafa:ca443f4786.jpg")
    embed.set_thumbnail(url="https://ih0.redbubble.net/image.4837681105.5862/raf,360x360,075,t,fafafa:ca443f4786.jpg")
    embed.add_field(name="clear [num]" , value="")
    embed.add_field(name="sitish tommorow" , value ="")
    embed.add_field(name="sitish today",value ="")
    embed.add_field(name="sitish weekly" , value ="")
    embed.add_field(name="sitish schedule" , value = "")
    embed.add_field(name="sitish [Day of current week]",value = "['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']")
    await ctx.send(embed=embed)
"""
@client.command()
async def clear (ctx, limit: int):
        await ctx.channel.purge(limit=limit+1)

Will be brought back once permissions for moderators are included"""



client.run('MTE4MDE3OTIxNTExOTgxODc3Mw.Gdej6D.qj7Zr9gYXTTH3WGxje3vjtRnKDFpbMb13Sl82w')