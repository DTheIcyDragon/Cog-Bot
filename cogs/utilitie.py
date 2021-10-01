import asyncio
import secrets
import string
import time

import discord
from discord.ext import commands


class Utilitie(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["pwd"])
    async def password(self, ctx):
        (secrets.choice("ab"))
        (secrets.token_bytes())
        (secrets.token_urlsafe())
        chars = string.digits + string.ascii_letters
        (len(chars))
        gen_password = (''.join(secrets.choice(chars) for _ in range(40)))

        em = discord.Embed(
            description=gen_password + "\n [You can check it strength here](http://rumkin.com/tools/password/passchk.php)\n"
                                       "[Or here](https://checkdeinpasswort.de/)\n Non of these Websites are affiliated with me in any way",
            color=discord.colour.Color.greyple())
        await ctx.author.send(embed=em)

    @commands.command(aliases=["vorschlag", "suggest"])
    async def suggestion(self, ctx, *, message):
        em = discord.Embed(title=f"Vorschlag von {ctx.author}\n{ctx.author.id} ", description=message,  # utilities
                           color=discord.Color.dark_purple())
        channel = await self.client.get_channel(769611628718456912)
        await channel.send(embed=em)

    @commands.command(aliases=["countdown"])
    async def timer(self, ctx, time: int):  # lerning case

        await asyncio.sleep(time)

        em = discord.Embed(title=ctx.author.display_name, description="Your timer is up",
                           color=discord.Colour.teal())  # utilities
        await ctx.send(ctx.author.mention, delete_after=0.1)
        await ctx.send(embed=em)

    @commands.command()
    @commands.has_role(862396474481967154)
    async def zitat(self, ctx, member, date, *, message):

        date = date.replace("_", " ")

        em = discord.Embed(title=f"-{str(member)}", description=f"***\"{str(message)}\"***  {str(date)}",
                           color=discord.Color.dark_purple())
        em.set_footer(text=f"{ctx.author.display_name} • {ctx.author.id}")
        channel = self.client.get_channel(851091679917375528)
        await channel.send(embed=em)

    @commands.command(aliases=["uinfo"])
    async def userinfo(self,ctx , member : discord.Member):

        joined_at = member.joined_at
        joined_at.timestamp()
        joined_at = (time.mktime(joined_at.timetuple()))

        created_at = member.created_at
        created_at.timestamp()
        created_at = (time.mktime(created_at.timetuple()))

        em = discord.Embed(title=f"Userinfo für {member.display_name}", color=discord.Color.from_rgb(235, 73, 238))
        em.add_field(name=f"Name", value=f"{member.name}", inline=False)
        em.add_field(name=f"ID", value=f"{member.id}", inline=False)
        em.add_field(name=f"Erstellungsdatum", value=f"<t:{int(created_at)}:F>", inline=False)
        em.add_field(name="Beigetreten", value=f"<t:{int(joined_at)}:F>")
        em.add_field(name=f"Bot", value=f"{'Ja' if member.bot else 'Nein'}", inline=False)
        em.set_thumbnail(url=member.avatar_url_as(size=4096))
        await ctx.send(embed=em)

    @commands.Cog.listener()
    async def on_member_join(self, member):

        created_at = member.created_at
        created_at.timestamp()
        created_at = (time.mktime(created_at.timetuple()))

        em = discord.Embed(title="Member joined", color=discord.Color.from_rgb(83, 22, 159))
        em.add_field(name=f"Name", value=f"{member.name}", inline=False)
        em.add_field(name=f"ID", value=f"{member.id}", inline=False)
        em.add_field(name=f"Erstellungs Datum", value=f"<t:{int(created_at)}:F>", inline=False)
        em.add_field(name=f"Bot", value=f"{'Ja' if member.bot else 'Nein'}", inline=False)

        em.set_thumbnail(url=member.avatar_url_as(size=4096))

        true_member_count = len([m for m in ctx.guild.members if not m.bot])
        channel = ctx.guild.get_channel(878401877715329064)
        await channel.edit(name = f"😃 User: {true_member_count}")

        bot_count = len([m for m in ctx.guild.members if m.bot])
        channel = ctx.guild.get_channel(878401060069339207)
        await channel.edit(name = f"🤖 Bots: {bot_count}")

        channel = self.client.get_channel(769620365403357254)
        await channel.send(embed=em)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        em = discord.Embed(title="Member left", color=discord.Color.from_rgb(83, 22, 159))
        em.add_field(name="Member", value=f"{member.name}", inline=False)
        em.add_field(name="ID", value=f"{member.id}", inline=False)
        em.add_field(name="Ging", value=f"<t:{int(time.time())}:F>", inline=False)
        em.set_thumbnail(url=member.avatar_url_as(size=4096))

        true_member_count = len([m for m in ctx.guild.members if not m.bot])
        channel = ctx.guild.get_channel(878401877715329064)
        await channel.edit(name = f"😃 User: {true_member_count}")

        bot_count = len([m for m in ctx.guild.members if m.bot])
        channel = ctx.guild.get_channel(878401060069339207)
        await channel.edit(name = f"🤖 Bots: {bot_count}")

        channel = self.client.get_channel(769620365403357254)
        await channel.send(embed=em)

def setup(client):
    client.add_cog(Utilitie(client))
