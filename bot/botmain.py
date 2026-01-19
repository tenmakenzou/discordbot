#the essentials
import discord
import os
import json


from discord.ext import commands, tasks
from discord import app_commands


# other .py
from sitish import *
from library import *

# -------- CONFIG --------
GUILDS_FILE = "guilds.json"


def load_channels():
    try:
        with open(GUILDS_FILE, "r") as f:
            data = json.load(f)
            return data.get("channels", [])
    except FileNotFoundError:
        return []


def save_channels(channels):
    with open(GUILDS_FILE, "w") as f:
        json.dump({"channels": channels}, f, indent=4)

# ------------------------

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="/", intents=intents)
tree = bot.tree


# -------- DAILY TASK --------
@tasks.loop(hours=24)
async def called_once_a_day():
    channel_ids = load_channels()

    embed = discord.Embed(colour=0x000000)
    embed.add_field(name="Today's Schedule", value=run("today"), inline=False)

    for channel_id in channel_ids:
        channel = bot.get_channel(channel_id)
        if channel:
            try:
                await channel.send(embed=embed)
            except Exception as e:
                print(f"Failed to send to {channel_id}: {e}")

@tree.command(name="addchannel", description="Add this channel to daily messages (Admin only)")
async def addchannel(interaction: discord.Interaction):

    if not interaction.user.guild_permissions.administrator:
        await interaction.response.send_message(
            "You don't have permission to do this.",
            ephemeral=True
        )
        return

    channel_id = interaction.channel.id
    channels = load_channels()

    if channel_id in channels:
        await interaction.response.send_message(
            "This channel is already in the list.",
            ephemeral=True
        )
        return

    channels.append(channel_id)
    save_channels(channels)

    await interaction.response.send_message(
        "Channel added successfully.",
        ephemeral=True
    )



@called_once_a_day.before_loop
async def before_called_once_a_day():
    await bot.wait_until_ready()
    print("Daily task is ready")
# ----------------------------


@bot.event
async def on_ready():
    print(f"Bot is running as {bot.user}")

    if not called_once_a_day.is_running():
        called_once_a_day.start()

    await bot.change_presence(activity=discord.Game(name="/help"))

    try:
        synced = await tree.sync()
        print(f"Synced {len(synced)} slash commands.")
    except Exception as e:
        print(f"Failed to sync commands: {e}")



@tree.command(name="departments", description="Show all UNIWA departments")
async def departments(interaction: discord.Interaction):

    embed = discord.Embed(
        title="Τμήματα Πανεπιστημίου Δυτικής Αττικής",
        colour=0x000000
    )

    embed.add_field(
        name="Δημόσια Υγεία",
        value=(
            "[Τμήμα Δημόσιας και Κοινοτικής Υγείας](https://pch.uniwa.gr/)\n"
            "[Τμήμα Πολιτικών Δημόσιας Υγείας](http://php.uniwa.gr)\n"
        ),
        inline=False
    )

    embed.add_field(
        name="Διοικητικές, Οικονομικές & Κοινωνικές Επιστήμες",
        value=(
            "[Τμήμα Αγωγής και Φροντίδας στην Πρώιμη Παιδική Ηλικία](http://ecec.uniwa.gr/)\n"
            "[Τμήμα Αρχειονομίας, Βιβλιοθηκονομίας και Συστημάτων Πληροφόρησης](http://alis.uniwa.gr)\n"
            "[Τμήμα Διοίκησης Επιχειρήσεων](http://www.ba.uniwa.gr/)\n"
            "[Τμήμα Διοίκησης Τουρισμού](http://tourism.uniwa.gr/)\n"
            "[Τμήμα Κοινωνικής Εργασίας](http://sw.uniwa.gr/)\n"
            "[Τμήμα Λογιστικής και Χρηματοοικονομικής](https://accfin.uniwa.gr/)"
        ),
        inline=False
    )

    embed.add_field(
        name="Επιστήμες Τροφίμων",
        value=(
            "[Τμήμα Επιστήμης και Τεχνολογίας Τροφίμων](http://fst.uniwa.gr/)\n"
            "[Τμήμα Επιστημών Οίνου, Αμπέλου και Ποτών](http://wvbs.uniwa.gr/)"
        ),
        inline=False
    )

    embed.add_field(
        name="Επιστήμες Υγείας & Πρόνοιας",
        value=(
            "[Τμήμα Βιοϊατρικών Επιστημών](http://bisc.uniwa.gr/)\n"
            "[Τμήμα Εργοθεραπείας](http://ot.uniwa.gr/)\n"
            "[Τμήμα Μαιευτικής](http://midw.uniwa.gr/)\n"
            "[Τμήμα Νοσηλευτικής](http://nurs.uniwa.gr/)\n"
            "[Τμήμα Φυσικοθεραπείας](http://www.phys.uniwa.gr/)"
        ),
        inline=False
    )

    embed.add_field(
        name="Εφαρμοσμένες Τέχνες & Πολιτισμός",
        value=(
            "[Τμήμα Γραφιστικής και Οπτικής Επικοινωνίας](http://www.gd.uniwa.gr)\n"
            "[Τμήμα Εσωτερικής Αρχιτεκτονικής](http://ia.uniwa.gr)\n"
            "[Τμήμα Συντήρησης Αρχαιοτήτων και Έργων Τέχνης](http://cons.uniwa.gr)\n"
            "[Τμήμα Φωτογραφίας και Οπτικοακουστικών Τεχνών](http://phaa.uniwa.gr)"
        ),
        inline=False
    )

    embed.add_field(
        name="Μηχανικοί & Πολυτεχνική",
        value=(
            "[Τμήμα Μηχανικών Βιοϊατρικής](http://bme.uniwa.gr)\n"
            "[Τμήμα Ηλεκτρολόγων και Ηλεκτρονικών Μηχανικών](http://eee.uniwa.gr)\n"
            "[Τμήμα Μηχανικών Βιομηχανικής Σχεδίασης και Παραγωγής](http://idpe.uniwa.gr)\n"
            "[Τμήμα Μηχανικών Πληροφορικής και Υπολογιστών](http://www.ice.uniwa.gr)\n"
            "[Τμήμα Μηχανικών Τοπογραφίας και Γεωπληροφορικής](http://www.geo.uniwa.gr)\n"
            "[Τμήμα Μηχανολόγων Μηχανικών](http://mech.uniwa.gr)\n"
            "[Τμήμα Ναυπηγών Μηχανικών](http://www.na.uniwa.gr)\n"
            "[Τμήμα Πολιτικών Μηχανικών](http://civ.uniwa.gr)"
        ),
        inline=False
    )

    embed.set_footer(
        text=f"Requested by {interaction.user}",
        icon_url=interaction.user.display_avatar.url
    )

    await interaction.response.send_message(embed=embed)


@tree.command(name="s", description="Get today's or tomorrow's schedule")
@app_commands.describe(arg="Choose 'today' or 'tomorrow'")
async def s(interaction: discord.Interaction, arg: str):

    embed = discord.Embed(colour=0x000000)
    embed.add_field(name=" ", value=run(arg), inline=False)
    embed.set_footer(
        text=f"Requested by {interaction.user}",
        icon_url=interaction.user.display_avatar.url
    )

    await interaction.response.send_message(embed=embed)


@tree.command(name="help", description="Show all commands")
async def help_command(interaction: discord.Interaction):

    embed = discord.Embed(colour=0x000000, title="Bot Commands")
    embed.set_author(name="Creator: tenma_kenzo_ | Hoster: Mr.pancakes")
    embed.set_thumbnail(
        url="https://www.artmajeur.com/medias/standard/t/a/tatjana-siadova/artwork/13448606_2953a.jpg"
    )

    embed.add_field(name="/s today", value="Today's schedule", inline=False)
    embed.add_field(name="/s tomorrow", value="Tomorrow's schedule", inline=False)
    embed.add_field(name="/f", value="Shows if library/restaurant is open", inline=False)
    embed.add_field(name="/services", value="Shows university services", inline=False)
    embed.add_field(name="/departments", value="Shows university's departments sites", inline=False)
    embed.add_field(
        name="Github",
        value="https://github.com/tenmakenzou/discordbot/",
        inline=False
    )

    embed.set_footer(
        text=f"Requested by {interaction.user}",
        icon_url=interaction.user.display_avatar.url
    )

    await interaction.response.send_message(embed=embed)


@tree.command(name="f", description="Check if the library and restaurant are open")
async def f(interaction: discord.Interaction):

    embed = discord.Embed(colour=0x000000)
    embed.add_field(name=" ", value=get_library(), inline=False)
    embed.add_field(name=" ", value=get_restauraunt(), inline=False)
    embed.set_footer(
        text=f"Requested by {interaction.user}",
        icon_url=interaction.user.display_avatar.url
    )

    await interaction.response.send_message(embed=embed)


@tree.command(name="services", description="Show university services")
async def services(interaction: discord.Interaction):

    embed = discord.Embed(colour=0x000000)
    embed.add_field(name="Eclass", value="https://eclass.uniwa.gr/", inline=False)
    embed.add_field(
        name="Services",
        value="https://sso.uniwa.gr/login?service=https%3A%2F%2Fservices.uniwa.gr%2Flogin%2Fcas",
        inline=False
    )

    embed.set_footer(
        text=f"Requested by {interaction.user}",
        icon_url=interaction.user.display_avatar.url
    )

    await interaction.response.send_message(embed=embed)


@tree.command(name="clear", description="Clear messages (Admin only)")
@app_commands.describe(limit="Number of messages to delete")
async def clear(interaction: discord.Interaction, limit: int):

    if not interaction.user.guild_permissions.administrator:
        await interaction.response.send_message(
            "You don't have permission to use this command.",
            ephemeral=True
        )
        return

    await interaction.channel.purge(limit=limit + 1)
    await interaction.response.send_message(
        f"Cleared {limit} messages.",
        ephemeral=True
    )


bot.run(os.getenv("TOKEN"))
