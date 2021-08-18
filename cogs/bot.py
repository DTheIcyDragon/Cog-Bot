import discord
from discord.ext import commands
import time


up_scince = time.time()

def sec_to_min(time):
    hours, seconds = divmod(time, 60 * 60)
    minutes, seconds = divmod(seconds, 60)
    return str(hours) + "h " + str(minutes) + "m " + str(int(seconds)) + "s"

class BotCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def uptime(self, ctx):
        import time
        up_now = time.time()
        time = up_now - up_scince
        em = discord.Embed(title="Uptime", description=f'{sec_to_min(time)}',
                           color=discord.colour.Color.from_rgb(104, 189, 191))
        await ctx.send(embed=em)

    @commands.command()
    async def ping(self, ctx):
        latency1 = str(round(self.client.latency, 3))
        latency2 = latency1.split(".")
        em = discord.Embed(title="Pong!",
                           description="❤ " + (latency2[1]) + " ms",
                           color=0x18dc39)                                                      #bot
        await ctx.send(embed=em)


    @commands.command()
    async def source(self, ctx):

        em = discord.Embed(description=f"Source code can be found (here)[https://github.com/DTheIcyDragon/Cog-Bot]")

        await ctx.send(embed=em)



def setup(client):
    client.add_cog(BotCog(client))