import discord
from discord.ext import commands



class FunCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_role(862396474481967154)
    async def punish(self, ctx, member: discord.Member, *, reason="for no reason!"):
        em = discord.Embed(description=f"{ctx.author.display_name} punished {member.display_name} {reason}")
        await ctx.send(embed=em)

    @commands.command()
    @commands.has_role(862396474481967154)
    async def slap(self,ctx, member: discord.Member, *, reason="for no reason!"):
        em = discord.Embed(description=f"{ctx.author.display_name} slapped {member.display_name} {reason}")
        await ctx.send(embed=em)

    @commands.command()
    @commands.has_role(862396474481967154)
    async def kill(self,ctx, member: discord.Member, *, reason="for no reason!"):
        em = discord.Embed(title=f"{ctx.author.display_name} killed {member.display_name} {reason}")
        await ctx.send(embed=em)

    @commands.command()
    @commands.has_role(862396474481967154)
    async def bonk(self,ctx, member: discord.Member):
        em = discord.Embed(title=f"{ctx.author.display_name} send {member.display_name} to horny jail")
        await ctx.send(embed=em)



def setup(client):
    client.add_cog(FunCog(client))