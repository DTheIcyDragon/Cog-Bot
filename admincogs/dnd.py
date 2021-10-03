import discord
from discord.ext import commands



class DnD(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def panel(self,ctx):

        em = discord.Embed(title=f"Mute Panel",
                           color=discord.Color.from_rgb(178, 54, 95))

        react = await ctx.send(embed=em)

        await react.add_reaction("<:DTheShadowDragon:868926034463035434>")
        await react.add_reaction("<:DTheRainbowDragon:868926034358198283>")
        await react.add_reaction("<:DTheJulezDragon:868926034475647026>")
        await react.add_reaction("<:DTheIcyDragon:868926411266719784>")
        await react.add_reaction("<:DTheDragonFire:868926034509176853>")
        await react.add_reaction("<:BTheBeginning:868926034102345829>")
        print(em.to_dict())

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):

        guild = self.client.get_guild(id=578446945425555464)

        Anton = guild.get_member(user_id=566667355837562881)
        Paul = guild.get_member(user_id=511219492332896266)
        Ben = guild.get_member(user_id=449922603579342858)
        Julez = guild.get_member(user_id=336144182915891211)
        Nick = guild.get_member(user_id=622130169657688074)
        Hendrik = guild.get_member(user_id=305029907333775363)

        if payload.user_id == 881597080223772763:
            pass
        else:
            if payload.guild_id == 578446945425555464:
                if payload.channel_id == 840919920966500402:

                    if str(payload.emoji) == "<:DTheShadowDragon:868926034463035434>":
                        await Anton.edit(mute=True)

                    if str(payload.emoji) == "<:DTheRainbowDragon:868926034358198283>":
                        await Ben.edit(mute=True)

                    if str(payload.emoji) == "<:DTheJulezDragon:868926034475647026>":
                        await Julez.edit(mute=True)

                    if str(payload.emoji) == "<:DTheIcyDragon:868926411266719784>":
                        await Paul.edit(mute=True)

                    if str(payload.emoji) == "<:DTheDragonFire:868926034509176853>":
                        await Nick.edit(mute=True)

                    if str(payload.emoji) == "<:BTheBeginning:868926034102345829>":
                        await Hendrik.edit(mute=True)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self,payload):

        guild = self.client.get_guild(id=578446945425555464)

        Anton = guild.get_member(user_id=566667355837562881)
        Paul = guild.get_member(user_id=511219492332896266)
        Ben = guild.get_member(user_id=449922603579342858)
        Julez = guild.get_member(user_id=336144182915891211)
        Nick = guild.get_member(user_id=622130169657688074)
        Hendrik = guild.get_member(user_id=305029907333775363)

        if payload.user_id == 868939322345267300:
            pass
        else:
            if payload.guild_id == 578446945425555464:
                if payload.channel_id == 840919920966500402:

                    if str(payload.emoji) == "<:DTheShadowDragon:868926034463035434>":
                        await Anton.edit(mute=False)

                    if str(payload.emoji) == "<:DTheRainbowDragon:868926034358198283>":
                        await Ben.edit(mute=False)

                    if str(payload.emoji) == "<:DTheJulezDragon:868926034475647026>":
                        await Julez.edit(mute=False)

                    if str(payload.emoji) == "<:DTheIcyDragon:868926411266719784>":
                        await Paul.edit(mute=False)

                    if str(payload.emoji) == "<:DTheDragonFire:868926034509176853>":
                        await Nick.edit(mute=False)

                    if str(payload.emoji) == "<:BTheBeginning:868926034102345829>":
                        await Hendrik.edit(mute=False)


def setup(client):
    client.add_cog(DnD(client))