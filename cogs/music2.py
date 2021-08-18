import discord
from discord.ext import commands
import DiscordUtils


class Music2Cog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def playlist(self, ctx):
        await ctx.send(".play https://www.youtube.com/watch?v=DynTwKGcEHM&ab_channel=Pillow")


def setup(client):
    client.add_cog(Music2Cog(client))