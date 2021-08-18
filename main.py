import settings
import discord
import json
import os
import time
import asyncio
import DiscordUtils

from discord.ext import commands

def get_prefix(client, message):
    os.chdir(r"C:\Users\DTheIcyDragon\PycharmProjects\CogBotPycharmdebug")
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

"""=Startup="""

up_scince = time.time()

client = commands.Bot(command_prefix=get_prefix,
                      intents=discord.Intents.all(),
                      strip_after_prefix=True,
                      case_insensitive  =True)

client.remove_command("help")
music = DiscordUtils.Music()

@client.event  # nie wieder anfassen
async def on_ready():
    print("With the Token: " + settings.bot_token)
    print(6 * "\n ")
    print("Logged in as {0.user}".format(client))
    print("It is on these Servers:")
    async for guild in client.fetch_guilds(limit=150):  # Start Section DO NEVER EVER TOUCH IT
        print(guild.name)
    print(228 * "=")
    print("Developed by DTheIcyDragon#1209 and DTheDragonFire#1648")


async def ch_pr():  # ch_pr = change presence
    await client.wait_until_ready()

    while not client.is_closed():
        # Background Task wechselt den Status immer wieder
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Version ALPHA"))

        await asyncio.sleep(20)

        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f" {len(client.guilds)} Server"))

        await asyncio.sleep(20)

        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=" .help"))

        await asyncio.sleep(20)



client.loop.create_task(ch_pr())

"""=Prefixes="""
@client.event
async def on_guild_join(guild):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = "//"

    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=4)


@client.event
async def on_guild_remove(guild):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

"""-Prefixes-"""


@client.event
async def on_command_error(ctx, error):
    print(error)
    if isinstance(error, commands.CommandNotFound):
        em = discord.Embed(title="An Error occurred!",
                           description="I didn't found that command! Maybe it doesn't exist.",
                           color=discord.colour.Color.red())
        await ctx.send(embed=em)

kontrolle = []
extensions = []

"""=Cogs="""

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f'cogs.{filename[:-3]}')  #"//load cog on start//"
        print(f"Loaded {filename}")

@client.command()
@commands.has_permissions(administrator=True)
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")
    em = discord.Embed(title=f"I successfully loaded `{extension}`", color=discord.Color.from_rgb(49, 231, 39))
    await ctx.send(embed=em)
    extensions.append(str(extension[:-3]))
    extensions.sort()


@load.error
async def load_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):

        em = discord.Embed(title="An Error occurred!",
                           description=f"I don't have enough arguments. Maybe you missed one!\nAvailible are:\n\n {'All Cogs are loaded' if extensions == kontrolle else ''.join(extensions)}",
                           color=discord.colour.Color.red())

        await ctx.send(embed=em)

    if isinstance(error, commands.MissingPermissions):
        em = discord.Embed(title="An Error occurred!",
                           description="You don't have enough permissions to execute that command!\nYou have to be an Administrator to use that.",
                           color=discord.colour.Color.red())
        await ctx.send(embed=em)

"""    if isinstance(error, commands.BadArgument):
        em = discord.Embed(title="An Error occurred!", description="I don't have the right arguments. I don't know what to do with these!",
                       color=discord.colour.Color.red())
        await ctx.send(embed=em)

    if isinstance(error, commands.ExtensionAlreadyLoaded):
        em = discord.Embed(title="An Error occurred!", description="I don't have to load something that is already there!",
                       color=discord.colour.Color.red())
        await ctx.send(embed=em)

    if isinstance(error, commands.ExtensionNotFound):
        em = discord.Embed(title="An Error occurred!", description="I can't load something, I don't find!",
                       color=discord.colour.Color.red())
        await ctx.send(embed=em)"""


@client.command()
@commands.has_permissions(manage_guild=True)
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")

    em = discord.Embed(title=f"I successfully unloaded `{extension}`", color=discord.Color.from_rgb(49, 231, 39))
    await ctx.send(embed=em)
    extensions.remove(str(extension))

"""@unload.error
async def unload_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        em = discord.Embed(title="An Error occurred!", description="You don't have enough permissions to execute that command")
        ctx.send(embed=em)"""

#unhandeled exception counts

@client.event
async def on_message(msg):

    try:
        if ":" == msg.content[0] and ":" == msg.content[-1]:
            emoji_name = msg.content[1:-1]
            for emoji in msg.guild.emojis:
            # don't respond to ourselves
                if msg.author == client.user:
                    return
                elif emoji_name == emoji.name:
                    await msg.channel.send(str(f"{msg.author}: {emoji}"))
                    await msg.delete()
                    break
    except IndexError:
        pass


    await client.process_commands(msg)


#**-Music Player-**

@client.command()
async def join(ctx):
    await ctx.author.voice.channel.connect()  # Joins author's voice channel

@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

@client.command()
async def play(ctx, *, url):
    try:
        await ctx.author.voice.channel.connect()
    except:
        pass

    player = music.get_player(guild_id=ctx.guild.id)
    if not player:
        player = music.create_player(ctx, ffmpeg_error_betterfix=True)
    if not ctx.voice_client.is_playing():
        await player.queue(url, search=True)
        song = await player.play()
        em = discord.Embed(description=f"Playing {song.name}", color=discord.colour.Color.dark_orange())
        await ctx.send(embed=em)
    else:
        song = await player.queue(url, search=True)
        em = discord.Embed(description=f"Queued {song.name}", color=discord.colour.Color.dark_orange())
        await ctx.send(embed=em)

@client.command()
async def pause(ctx):

    player = music.get_player(guild_id=ctx.guild.id)
    song = await player.pause()
    em = discord.Embed(description=f"Paused `{song.name}`")
    await ctx.send(embed=em)

@client.command()
async def resume(ctx):

    player = music.get_player(guild_id=ctx.guild.id)
    song = await player.resume()
    em = discord.Embed(description=f"Resumed `{song.name}`", color=discord.colour.Color.dark_orange())
    await ctx.send(embed=em)

@client.command()
async def stop(ctx):

    player = music.get_player(guild_id=ctx.guild.id)
    await player.stop()
    em = discord.Embed(description="Stopped")
    await ctx.send(embed = em)

@client.command()
async def loop(ctx):

    player = music.get_player(guild_id=ctx.guild.id)
    song = await player.toggle_song_loop()
    if song.is_looping:
        em = discord.Embed(description=f"Enabled loop for {song.name}", color=discord.colour.Color.dark_orange())
        await ctx.send(embed=em)
    else:
        em = discord.Embed(description=f"Disabled loop for {song.name}", color=discord.colour.Color.dark_orange())
        await ctx.send(embed=em)

@client.command()
async def queue(ctx):

    player = music.get_player(guild_id=ctx.guild.id)
    em = discord.Embed(description=f"`{' '.join([song.name for song in player.current_queue()])}`\n", color=discord.colour.Color.dark_orange())
    await ctx.send(embed=em)

@client.command()
async def np(ctx):

    player = music.get_player(guild_id=ctx.guild.id)
    song = player.now_playing()
    em = discord.Embed(description=f"Now plays `{song.name}`", color=discord.colour.Color.dark_orange())
    await ctx.send(embed=em)

@client.command()
async def skip(ctx):

    player = music.get_player(guild_id=ctx.guild.id)
    data = await player.skip(force=True)
    if len(data) >= 2:
        em = discord.Embed(description=f"Skipped from `{data[0].name}` to `{data[1].name}`", color=discord.colour.Color.dark_orange())
        await ctx.send(embed=em)
    else:
        em = discord.Embed(description=f"Skipped {data[0].name}", color=discord.colour.Color.dark_orange())
        await ctx.send(embed=em)

@client.command()
async def volume(ctx, vol):

    player = music.get_player(guild_id=ctx.guild.id)
    song, volume = await player.change_volume(float(vol) / 100)  # volume should be a float between 0 to 1
    em = discord.Embed(description=f"Changed volume to `{volume * 100}`%", color=discord.colour.Color.dark_orange())
    await ctx.send(embed = em)

@client.command()
async def remove(ctx, index):

    player = music.get_player(guild_id=ctx.guild.id)
    song = await player.remove_from_queue(int(index))
    em = discord.Embed(description=f"Removed `{song.name}` from queue", color=discord.colour.Color.dark_orange())
    await ctx.send(embed=em)

client.run(settings.bot_token)