import asyncio

import discord
from discord.ext import commands, tasks

#Defenitionen


class Temporary(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def testing(self, ctx):
        f = await ctx.author.profile()
        if f.premium:
            print("True")
        else:
            print("False")

    @commands.command()
    async def split(self, ctx):
        channel = self.client.get_channel(798302722431909892)
        counter = 0
        with open(r"C:\Users\DTheIcyDragon\PycharmProjects\CogBotPycharmdebug\admincogs\useless\codes.txt") as codes:

            for f in codes:
                counter += 1
                await channel.send(f"Nr.{counter}: {f}")
                await asyncio.sleep(0.5)
        await ctx.send("Done :)")



def setup(client):
    client.add_cog(Temporary(client))