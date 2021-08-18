import discord
from discord.ext import commands



class StatCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def statupdate(self,ctx):

        true_member_count = len([m for m in ctx.guild.members if not m.bot])
        channel = ctx.guild.get_channel(872475756540866620)
        await channel.edit(name = f"User: {true_member_count}")

        bot_count = len([m for m in ctx.guild.members if m.bot])
        channel = ctx.guild.get_channel(873532019894804490)
        await channel.edit(name = f"Bots: {bot_count}")

        print(true_member_count, bot_count)





"""Ja if member.bot else Nein"""

def setup(client):
    client.add_cog(StatCog(client))