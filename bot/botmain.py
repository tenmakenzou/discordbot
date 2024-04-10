import discord


from sitish import *
from library import *

from discord.ext import commands 
from discord.ext.commands import has_permissions, CheckFailure





intents = discord.Intents.all()
client = commands.Bot(command_prefix = '/',intents=intents)
client.remove_command("help")




@client.event
async def on_ready():
    print("Bot is running!")
    print("Week has been reset!")
    await client.change_presence(activity=discord.Game(name="/help"))
        

    


@client.command()
async def poll(ctx,*,arg):

    message = await ctx.send(arg)
    emoji1 = '\N{THUMBS UP SIGN}'
    emoji2 = '\N{THUMBS DOWN SIGN}'
    await message.add_reaction(emoji1)
    await message.add_reaction(emoji2)


    
@client.command()
@commands.cooldown(1, 5, type=commands.BucketType.user) # 5 second cooldown

async def s(ctx,arg):

        
        if arg == "weekly":
             await ctx.send(file = discord.File(get_current_day_and_week(arg)))

        elif arg == "weeks":
             await ctx.send(file = discord.File("week1.jpg")) 
             await ctx.send(file = discord.File("week2.jpg"))
             await ctx.send(file = discord.File("week3.jpg"))
             await ctx.send(file = discord.File('week4.jpg'))                     
        else:

            embed = discord.Embed(colour=000000,title="")  
            embed.set_author(name="" , url = "")
            embed.add_field(name=" ", value=(get_current_day_and_week(arg)),inline=False)
            embed.set_footer(text=f"Requested by {ctx.author}",icon_url=ctx.author.avatar)
            
            await ctx.send(embed=embed)
         



@client.command()
async def help(ctx):


    embed = discord.Embed(colour=000000,title="Bot Commands")  
    
    embed.set_author(name="Creator : tenma_kenzo_ + BladeZ (ez)" , url = "")

    embed.set_thumbnail(url="https://www.artmajeur.com/medias/standard/t/a/tatjana-siadova/artwork/13448606_2953a.jpg")
    embed.add_field(name="/s today",value ="Today's schedule",inline=False)
    embed.add_field(name="/s tomorrow" , value ="Tomorrow's schedule",inline=False)
    embed.add_field(name="/s weekly" , value ="Weeekly  schedule",inline=False)
    embed.add_field(name="/s weeks" , value ="Shows all weeks",inline=False)
    embed.add_field(name="/s open , schedule , when" , value = "Shows if restaurant is open",inline=False)
    embed.add_field(name="/s [Day of current week]",value = "['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']",inline=False)
    embed.add_field(name="/poll" , value = "simple yes/no poll",inline=False)
    embed.add_field(name="/b" , value ="Shows if library is open",inline=False)
    embed.add_field(name="/services" , value ="Shows services of uni",inline=False)
    embed.set_footer(text=f"Requested by {ctx.author}",icon_url=ctx.author.avatar)
    
    await ctx.send(embed=embed)


@client.command()
async def b(ctx):
            embed = discord.Embed(colour=000000,title="")  
            embed.set_author(name="" , url = "")
            embed.add_field(name=" ", value=(get_library()),inline=False)
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






f = open("token.txt","r")
token = f.readline()
f.close()
client.run(str(token))
