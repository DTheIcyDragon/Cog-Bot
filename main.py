import settings
import discord
import json
import os
import time
import asyncio
import secrets
import string

from discord.ext import commands, tasks





"""=Startup="""

up_scince = time.time()

client = commands.Bot(command_prefix="//",
                      intents=discord.Intents.all(),
                      strip_after_prefix=True,
                      case_insensitive  =True)

client.remove_command("help")


@client.event  # nie wieder anfassen
async def on_ready():
    #print("With the Token: " + settings.bot_token)
    print(6 * "\n ")
    print(f"Logged in as {client.user}")
    print("It is on these Servers:")
    async for guild in client.fetch_guilds(limit=150):  # Start Section DO NEVER EVER TOUCH IT
        print(guild.name)
    print(228 * "=")
    print("Developed by DTheIcyDragon#1209 and DTheDragonFire#1648")

    with open("json-data/loads.json", "r") as f:
        loads = json.load(f)

    loads = loads["cogs"]

    for key, value in loads.items():
        if value == "1":
# with help from Ikarus#7098 (544956941643022356) or <@544956941643022356> find him on https://discord.id
            client.load_extension(f"cogs.{key}")
            print(f"loaded {key}")




@tasks.loop(seconds = 60)
async def ch_pr():  # ch_pr = change presence
    await client.wait_until_ready()

    while not client.is_closed():
        # Background Task wechselt den Status immer wieder
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Version 2.0"))

        await asyncio.sleep(20)

        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f" {len(client.guilds)} Server"))

        await asyncio.sleep(20)

        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=" .help"))

        await asyncio.sleep(20)

ch_pr.start()



@client.command()
async def cogs(ctx):

    with open("json-data/loads.json", "r") as f:
        loads = json.load(f)
    
    loads = loads["cogs"]
    
    embed = discord.Embed(title="Cog Board",
                          description="Shows wich Modules are loaded",
                          color=discord.Color.dark_red())

    for key, value in loads.items():

        embed.add_field(name=key.capitalize(), value=f'{"🟢" if value == "1" else "🔴"}')

    await ctx.send(embed = embed)


"""=cogs="""

@client.command()
@commands.has_permissions(administrator=True)
async def load(ctx, extension):

    extension = extension.lower()

    client.load_extension(f"cogs.{extension}")

    em = discord.Embed(title=f"I successfully loaded `{extension}`", color=discord.Color.from_rgb(49, 231, 39))
    await ctx.send(embed=em)

    with open("json-data/loads.json", "r") as f:
        loads = json.load(f)

    loads["cogs"][extension] = "1"

    with open("json-data/loads.json", "w") as f:
        json.dump(loads, f, indent=4)


@client.command()
@commands.has_permissions(administrator=True)
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")

    em = discord.Embed(title=f"I successfully unloaded `{extension}`", color=discord.Color.from_rgb(49, 231, 39))
    await ctx.send(embed=em)

    with open("json-data/loads.json", "r") as f:
        loads = json.load(f)

    loads["cogs"][extension] = "0"

    with open("json-data/loads.json", "w") as f:
        json.dump(loads, f, indent=4)


@load.error
async def load_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):

        em = discord.Embed(title="An Error occurred!",
                           description=f"I don't have enough arguments. Maybe you missed one!",
                           color=discord.colour.Color.red())

        await ctx.send(embed=em)

    elif isinstance(error, commands.MissingPermissions):
        em = discord.Embed(title="An Error occurred!",
                           description="You don't have enough permissions to execute that command!\nYou have to be an Administrator to use that.",
                           color=discord.colour.Color.red())
        await ctx.send(embed=em)

    elif isinstance(error, commands.BadArgument):
        em = discord.Embed(title="An Error occurred!", description="I don't have the right arguments. I don't know what to do with these!",
                       color=discord.colour.Color.red())
        await ctx.send(embed=em)

    elif isinstance(error, commands.ExtensionAlreadyLoaded):
        em = discord.Embed(title="An Error occurred!", description="I don't have to load something that is already there!",
                       color=discord.colour.Color.red())
        await ctx.send(embed=em)

    elif isinstance(error, commands.ExtensionNotFound):
        em = discord.Embed(title="An Error occurred!", description="I can't load something, I don't find!",
                       color=discord.colour.Color.red())
        await ctx.send(embed=em)

    else:
        em = discord.Embed(title="An Error occurred!", description="It us not defined so ",
                       color=discord.colour.Color.red())
        await ctx.send(embed=em)

@unload.error
async def unload_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):

        em = discord.Embed(title="An Error occurred!",
                           description=f"I don't have enough arguments.",
                           color=discord.colour.Color.red())

        await ctx.send(embed=em)

    elif isinstance(error, commands.MissingPermissions):
        em = discord.Embed(title="An Error occurred!",
                           description="You don't have enough permissions to execute that command!\nYou have to be an Administrator to use that.",
                           color=discord.colour.Color.red())
        await ctx.send(embed=em)

    elif isinstance(error, commands.BadArgument):
        em = discord.Embed(title="An Error occurred!", description="I don't have the right arguments. I don't know what to do with these!",
                       color=discord.colour.Color.red())
        await ctx.send(embed=em)

    elif isinstance(error, commands.ExtensionAlreadyLoaded):
        em = discord.Embed(title="An Error occurred!", description="I don't have to unload something that isn't loaded!",
                       color=discord.colour.Color.red())
        await ctx.send(embed=em)

    elif isinstance(error, commands.ExtensionNotFound):
        em = discord.Embed(title="An Error occurred!", description="I can't unload something, I don't find!",
                       color=discord.colour.Color.red())
        await ctx.send(embed=em)

@client.event
async def on_command_error(ctx, error):
    print(error)
    if isinstance(error, commands.CommandNotFound):
        em = discord.Embed(title="An Error occurred!",
                           description="I didn't found that command! Maybe it doesn't exist.",
                           color=discord.colour.Color.red())
        await ctx.send(embed=em)

client.run(settings.bot_token)
