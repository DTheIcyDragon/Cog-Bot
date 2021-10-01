import discord
from discord.ext import commands



class Mod(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["clear"])
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, limit: int):
        await ctx.channel.purge(limit=limit)
        em = discord.Embed(description=f"**Cleared by {ctx.author.mention}**", color=0x18dc39)
        await ctx.send(embed=em, delete_after=10)

    @purge.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please specify the amount of messages you want to clear. Usage: //clear <number>')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('You do not have manage_messages permssion')

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason):

        invite = self.client.get_channel(839480594311413761)
        invitelink = await invite.create_invite(max_uses=1, max_age=0)
        try:
            await member.send(
                f"You got kicked from ►𝙏𝙝𝙚𝘿𝙧𝙖𝙜𝙤𝙣𝙨◄ \nBecause: {reason}\n{invitelink}")  # mod
        except:
            ctx.send(f"The direct messages from {member} are closed.")
        await member.kick(reason=reason)
        em = discord.Embed(title="Kick",
                           description=f"Member: {member}\nReason: {reason}\n By {ctx.author.display_name}, {ctx.author.id}",
                           color=discord.colour.Color.red())
        await ctx.send(embed=em)

        log_channel = self.client.get_channel(769620365403357254)
        em = discord.Embed(title = ":exclamation: **KICK** :exclamation:",
                           description=f"<@{ctx.author.id}> kicked {member}\nBecause:{reason}")
        log_channel.send(embed=em)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason):
        await member.ban(reason=reason)
        await ctx.send(f'User {member} has been banned')  # mod
        log_channel = self.client.get_channel(769620365403357254)
        em = discord.Embed(title=":exclamation: **BAN**",
                           description=f"<@{ctx.author.id}> banned {member}\nBecause:{reason}")
        await log_channel.send(embed=em)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):  # mod
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def say(self, ctx, *, message):
        ctx.send(f"{message.content}")


def setup(client):
    client.add_cog(Mod(client))