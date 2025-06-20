import discord
import os

from library import *
from sitish import *
from discord.ext import commands 
from discord.ext.commands import has_permissions, CheckFailure





intents = discord.Intents.all()
client = commands.Bot(command_prefix = '/',intents=intents)
client.remove_command("help")




@client.event
async def on_ready():
    print("Bot is running!")
    await client.change_presence(activity=discord.Game(name="/help"))
        

    


    
@client.command()
@commands.cooldown(1, 5, type=commands.BucketType.user) # 5 second cooldown

async def s(ctx,arg):
            embed = discord.Embed(colour=000000,title="")  
            embed.set_author(name="" , url = "")
            embed.add_field(name=" ", value=(run(arg)),inline=False)
            embed.set_footer(text=f"Requested by {ctx.author}",icon_url=ctx.author.avatar)
            
            await ctx.send(embed=embed)
         



@client.command()
async def help(ctx):


    embed = discord.Embed(colour=000000,title="Bot Commands")  
    
    embed.set_author(name="Creator : tenma_kenzo_ + mr.pancakes" , url = "")

    embed.set_thumbnail(url="https://www.artmajeur.com/medias/standard/t/a/tatjana-siadova/artwork/13448606_2953a.jpg")
    embed.add_field(name="/s today",value ="Today's schedule",inline=False)
    embed.add_field(name="/s tomorrow",value ="Today's schedule",inline=False)
    embed.add_field(name="/b" , value ="Shows if library/restauraunt is open",inline=False)
    embed.add_field(name="/services" , value ="Shows services of uni",inline=False)
    embed.add_field(name="Github" , value ="https://github.com/tenmakenzou/discordbot/",inline=False)
    embed.set_footer(text=f"Requested by {ctx.author}",icon_url=ctx.author.avatar)

    
    await ctx.send(embed=embed)


@client.command()
async def b(ctx):
            embed = discord.Embed(colour=000000,title="")  
            embed.set_author(name="" , url = "")
            embed.add_field(name=" ", value=(get_library()),inline=False)
            embed.add_field(name=" ", value=(get_restauraunt()),inline=False)
            embed.set_footer(text=f"Requested by {ctx.author}",icon_url=ctx.author.avatar)
            
            await ctx.send(embed=embed)
         


@client.command()
async def services(ctx):
            embed = discord.Embed(colour=000000,title="")  
            embed.set_author(name="" , url = "")
            embed.add_field(name="Eclass", value="https://eclass.uniwa.gr/",inline=False)
            embed.add_field(name="Services", value="https://sso.uniwa.gr/login?service=https%3A%2F%2Fservices.uniwa.gr%2Flogin%2Fcas",inline=False)
            embed.set_footer(text=f"Requested by {ctx.author}",icon_url=ctx.author.avatar)
            
            await ctx.send(embed=embed)

@client.command(pass_context=True)
@has_permissions(administrator=True) #clear messages
async def clear (ctx, limit: int):
        await ctx.channel.purge(limit=limit+1)


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command does not exist use [/help]")



token = os.getenv('TOKEN')
print(token)
client.run(token)
