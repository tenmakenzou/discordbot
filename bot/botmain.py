import discord
import os

from discord.ext import commands
from discord import app_commands
from sitish import *
from library import *

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="/", intents=intents)
tree = bot.tree   


@bot.event
async def on_ready():
    print(f"Bot is running as {bot.user}")
    await bot.change_presence(activity=discord.Game(name="/help"))
    try:
        synced = await tree.sync()
        print(f"Synced {len(synced)} slash commands.")
    except Exception as e:
        print(f"Failed to sync commands: {e}")


@tree.command(name="s", description="Get today's or tomorrow's schedule")
@app_commands.describe(arg="Choose 'today' or 'tomorrow'")
async def s(interaction: discord.Interaction, arg: str):
    
    embed = discord.Embed(colour=0x000000, title="")
    embed.set_author(name="", url="")
    embed.add_field(name=" ", value=run(arg), inline=False)
    embed.set_footer(text=f"Requested by {interaction.user}", icon_url=interaction.user.display_avatar.url)

    await interaction.response.send_message(embed=embed)


@tree.command(name="help", description="Show all commands")
async def help_command(interaction: discord.Interaction):
    
    embed = discord.Embed(colour=0x000000, title="Bot Commands")
    embed.set_author(name="Creator: tenma_kenzo_ Hoster : Mr.pancakes", url="")
    embed.set_thumbnail(url="https://www.artmajeur.com/medias/standard/t/a/tatjana-siadova/artwork/13448606_2953a.jpg")
    embed.add_field(name="/s today", value="Today's schedule", inline=False)
    embed.add_field(name="/s tomorrow", value="Tomorrow's schedule", inline=False)
    embed.add_field(name="/f", value="Shows if library/restaurant is open", inline=False)
    embed.add_field(name="/services", value="Shows university services", inline=False)
    embed.add_field(name="Github", value="https://github.com/tenmakenzou/discordbot/", inline=False)
    embed.set_footer(text=f"Requested by {interaction.user}", icon_url=interaction.user.display_avatar.url)

    await interaction.response.send_message(embed=embed)


@tree.command(name="f", description="Check if the library and restaurant are open")
async def b(interaction: discord.Interaction):
    embed = discord.Embed(colour=0x000000, title="")
    embed.set_author(name="", url="")
    embed.add_field(name=" ", value=get_library(), inline=False)
    embed.add_field(name=" ", value=get_restauraunt(), inline=False)
    embed.set_footer(text=f"Requested by {interaction.user}", icon_url=interaction.user.display_avatar.url)

    await interaction.response.send_message(embed=embed)


@tree.command(name="services", description="Show university services")
async def services(interaction: discord.Interaction):
    embed = discord.Embed(colour=0x000000, title="")
    embed.set_author(name="", url="")
    embed.add_field(name="Eclass", value="https://eclass.uniwa.gr/", inline=False)
    embed.add_field(name="Services", value="https://sso.uniwa.gr/login?service=https%3A%2F%2Fservices.uniwa.gr%2Flogin%2Fcas", inline=False)
    embed.set_footer(text=f"Requested by {interaction.user}", icon_url=interaction.user.display_avatar.url)

    await interaction.response.send_message(embed=embed)


@tree.command(name="clear", description="Clear messages (Admin only)")
@app_commands.describe(limit="Number of messages to delete")
async def clear(interaction: discord.Interaction, limit: int):
    if not interaction.user.guild_permissions.administrator:
        await interaction.response.send_message("You don't have permission to use this command.", ephemeral=True)
        return

    await interaction.channel.purge(limit=limit + 1)
    await interaction.response.send_message(f"Cleared {limit} messages.", ephemeral=True)



token = os.getenv('TOKEN')
print(token)
bot.run(token)
