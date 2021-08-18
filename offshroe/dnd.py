import discord
from discord.ext import commands



class DnDCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def mutebord(self, ctx):
        em = discord.Embed(title="Lord Kerberos Bord", description="Klicke auf die Reaction um zu muten")
        msg = await ctx.channel.send(embed=em)
        await msg.add_reaction("<:DTheDragonFire:868926034509176853>")
        await msg.add_reaction("<:DTheIcyDragon:868926411266719784>")
        await msg.add_reaction("<:DTheJulezDragon:868926034475647026>")
        await msg.add_reaction("<:DTheRainbowDragon:868926034358198283>")
        await msg.add_reaction("<:DTheShadowDragon:868926034463035434>")

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.user_id == 861323291716354058:
            return
        else:
            if payload.emoji == "<:DTheDragonFire:868926034509176853>":
                DTheDragonFire = discord.Guild.get_member(self=payload.guild_id, user_id=622130169657688074)
                DTheDragonFire.edit(mute=True)
            if payload.emoji == "<:DTheIcyDragon:868926411266719784>":
                DTheIcyDragon = discord.Guild.get_member(self=payload.guild_id, user_id=511219492332896266)
                DTheIcyDragon.edit(mute=True)
            if payload.emoji == "<:DTheJulezDragon:868926034475647026>":
                DTheJulezDragon = discord.Guild.get_member(self=payload.guild_id, user_id=336144182915891211)
                DTheJulezDragon.edit(mute=True)
            if payload.emoji == "<:DTheRainbowDragon:868926034358198283>":
                DTheRainbowDragon = discord.Guild.get_member(self=payload.guild_id, user_id=449922603579342858)
                DTheRainbowDragon.edit(mute=True)
            if payload.emoji == "<:DTheShadowDragon:868926034463035434>":
                DTheShadowDragon = discord.Guild.get_member(self=payload.guild_id, user_id=566667355837562881)
                DTheShadowDragon.edit(mute=True)


    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        if payload.user_id == 861323291716354058:
            return
        else:
            if payload.emoji == "<:DTheDragonFire:868926034509176853>":
                DTheDragonFire = discord.Guild.get_member(self=payload.guild_id, user_id=622130169657688074)
                DTheDragonFire.edit(mute=False)
            if payload.emoji == "<:DTheIcyDragon:868926411266719784>":
                DTheIcyDragon = discord.Guild.get_member(self=payload.guild_id, user_id=511219492332896266)
                DTheIcyDragon.edit(mute=False)
            if payload.emoji == "<:DTheJulezDragon:868926034475647026>":
                DTheJulezDragon = discord.Guild.get_member(self=payload.guild_id, user_id=336144182915891211)
                DTheJulezDragon.edit(mute=False)
            if payload.emoji == "<:DTheRainbowDragon:868926034358198283>":
                DTheRainbowDragon = discord.Guild.get_member(self=payload.guild_id, user_id=449922603579342858)
                DTheRainbowDragon.edit(mute=False)
            if payload.emoji == "<:DTheShadowDragon:868926034463035434>":
                DTheShadowDragon = discord.Guild.get_member(self=payload.guild_id, user_id=566667355837562881)
                DTheShadowDragon.edit(mute=False)


def setup(client):
    client.add_cog(DnDCog(client))