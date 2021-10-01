import discord
from discord.ext import commands, tasks



class Stat(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def serverstats(self, ctx):
        total_channel = len(ctx.guild.voice_channels) + len(ctx.guild.text_channels) + len(ctx.guild.stage_channels)
        em = discord.Embed(title=f"Stats for {ctx.guild.name}", color = discord.Color.from_rgb(235, 73, 238))
        em.add_field(name=f"Name", value=f"{ctx.guild.name}", inline=True)
        em.add_field(name=f"ID", value=f"{ctx.guild.id}", inline=True)
        em.add_field(name=f"Owner", value=f"{ctx.guild.owner}", inline=True)
        em.add_field(name=f"Members", value=f"{ctx.guild.member_count}", inline=True)
        em.add_field(name=f"Roles", value=f"{len(ctx.guild.roles)}", inline=True)
        em.add_field(name=f"Channel", value=f"{total_channel}", inline=True)
        em.add_field(name=f"Nitro Stufe", value=f"{ctx.guild.premium_tier}", inline=True)
        em.add_field(name=f"Boost", value=f"{ctx.guild.premium_subscription_count}", inline=True)
        await ctx.send(embed=em)





"""Ja if member.bot else Nein"""

def setup(client):
    client.add_cog(Stat(client))