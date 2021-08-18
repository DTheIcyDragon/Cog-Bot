import discord
from discord.ext import commands



class HelpCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        em = discord.Embed(title=f"Hilfe für {ctx.author.display_name}",
                           description="Für nähere Hilfe gib\n**//help** *<Command to help>* ein.\n",
                           color=discord.Color.dark_gold())

        em.add_field(name="`Administration`", value="Purge, Say, Kick, Ban, Unban", inline=False)
        em.add_field(name="`Bot`", value="Ping, Source, Uptime", inline=False)

        await ctx.send(embed=em)


def setup(client):
    client.add_cog(HelpCog(client))