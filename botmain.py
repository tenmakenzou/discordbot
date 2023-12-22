import discord
from sitish import *
from discord.ext import commands 
from discord.ext.commands import has_permissions, CheckFailure




intents = discord.Intents.all()
client = commands.Bot(command_prefix = '/',intents=intents)



@commands.cooldown(rate=1, per=5, type=commands.BucketType.user) # 5 second cooldown



@client.event
async def on_ready():
    print("Bot is running!")
    changeweek("reset")
    print("Week has been reset!")
    
    
@client.command()
async def hello(ctx):
    await ctx.send("test")


@client.command()
async def s(ctx,arg):
     
        await ctx.send(get_current_day_and_week(arg))
     

@client.command()
async def helpsitish(ctx):


    embed = discord.Embed(
      colour=discord.Colour.random(),       
     title="Bot Commands")  
    embed.set_author(name="Creator : tenma_kenzo_ + BladeZ (ez)",url = "https://ih0.redbubble.net/image.4837681105.5862/raf,360x360,075,t,fafafa:ca443f4786.jpg")
    embed.set_thumbnail(url="https://ih0.redbubble.net/image.4837681105.5862/raf,360x360,075,t,fafafa:ca443f4786.jpg")
    embed.add_field(name="clear [num]" , value="")
    embed.add_field(name="s tommorow" , value ="")
    embed.add_field(name="s today",value ="")
    embed.add_field(name="s weekly" , value ="")
    embed.add_field(name="s schedule" , value = "")
    embed.add_field(name="s [Day of current week]",value = "['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']")
    await ctx.send(embed=embed)




@client.command(pass_context=True)
@has_permissions(administrator=True)
async def changesitish(ctx , arg):
        await ctx.send(changeweek(arg))
        await ctx.send("week changed!")
    


@client.command(pass_context=True)
@has_permissions(administrator=True) #clear messages
async def clear (ctx, limit: int):
        await ctx.channel.purge(limit=limit+1)




client.run('MTE4MDE3OTIxNTExOTgxODc3Mw.Gdej6D.qj7Zr9gYXTTH3WGxje3vjtRnKDFpbMb13Sl82w')
