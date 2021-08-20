import asyncio
import random

import discord
from discord.ext import commands
import os
from datetime import datetime
import pytz

class ModUtilsCog(commands.Cog):
    def __init__(self, client):
        self.client = client





    @commands.command()
    @commands.has_permissions(administrator=True)
    async def close(self, ctx, *, vorfall:str):
        blacklist = [705800487517028493,#regelwerk
                     876917024838807692,#ankündigung
                     876916455915020308,#discord-updates
                     769620365403357254,#log
                     876924752881651843,#mod-talk
                     876917285539971082,#offen-für-alle
                     795043532951650324,#memes
                     851091679917375528,#meme-reife-zitate
                     877249840805994538,#commands
                     876921062602985533,#reports
                     876923450193752104,#mod-abstimmungen
                     876923627080155177,#richterliche-anträge
                     876923883419209738,#brett-der-schande
                     877244424185315389 #freestuff
                     ]

        if ctx.channel.id in blacklist:
            em = discord.Embed(title="An Error occurred!",
                               description="You are not allowed to use that command here",
                               color = discord.Color.red())
            await ctx.channel.send(embed=em)

        else:
            timezone = pytz.timezone('Europe/Berlin')
            date = datetime.now(tz=timezone)
            os.chdir(r"E:\Logs")

            f = open(f"{vorfall}_{ctx.channel.name}.archiev", "a")
            f.write(f'#{vorfall}\n#{date.strftime("%d-%m-%Y %H:%M")}\n')

            async for word in ctx.channel.history(oldest_first=True):
                if word.author.id == 861323291716354058:
                    pass
                else:
                    f.write(f"{word.author}: '{word.content}'\n")

            await ctx.channel.delete(reason="Ticket closed")
            f.close()
            channel = self.client.get_channel(873536647201964053)
            await channel.send(file=discord.File(rf"E:\Logs\{vorfall}_{ctx.channel.name}.archiev"))


    @close.error
    async def close_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            em = discord.Embed(title="Error", description="Bitte gib an was in diesem Ticket geschehen ist.\n(.close [Vorfall])", color=discord.Color.red())
            await ctx.send(embed=em)


    @commands.command(aliases=["rep", "reporter"])
    async def report(self, ctx, member: discord.Member, *, msg):
        if member.id == 511219492332896266:
            em = discord.Embed(description="**Der Owner ist unantastbar**", color=discord.Color.from_rgb(240, 72, 49))
            await ctx.send(embed=em)

        else:
            em = discord.Embed(title=f"Report from {ctx.author.display_name}",
                               description=f"`{ctx.author.display_name}` reported `{member.display_name}`\nBecause: `{msg}`",
                               color=discord.Color.dark_purple())

            em.add_field(name="Reporting ID", value=ctx.author.id)
            em.add_field(name="Reported ID", value=member.id)

            channel = ctx.guild.get_channel(867378126450327602)
            react = await channel.send(embed=em)

            await react.add_reaction("<:JA:842160937161982002>")
            await react.add_reaction("<:Vielleicht:842160936898527275>")
            await react.add_reaction("<:Nein:842160936869036043>")
            #print(em.to_dict())

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):

        if payload.user_id == 861323291716354058:
            pass
        else:
            if payload.guild_id == 578446945425555464:
                if payload.channel_id == 867378126450327602:
                    if str(payload.emoji) == "<:JA:842160937161982002>":

                        id = payload.message_id
                        channel = self.client.get_channel(867378126450327602)
                        msg = await channel.fetch_message(id)
                        await msg.delete()


                    if str(payload.emoji) == "<:Vielleicht:842160936898527275>":
                        pass

                    if str(payload.emoji) == "<:Nein:842160936869036043>":
                        id = payload.message_id
                        channel = self.client.get_channel(867378126450327602)
                        msg = await channel.fetch_message(id)
                        embed = msg.embeds[0]
                        embeddict = embed.to_dict()
                        #print(embeddict)
                        reported_id = embeddict["fields"][1]['value']




                        guild = self.client.get_guild(payload.guild_id)

                        category = self.client.get_channel(867816787528777738)

                        counter = random.randint(100000000000, 999999999999)
                        channel = await guild.create_text_channel(name=f"Rep #{counter}", overwrites=None, category=category, reason="Report Ticket")

                        em = discord.Embed(title="Erklärung", description=f"Ticket: https://discordapp.com/channels/578446945425555464/867378126450327602/{payload.message_id}")

                        em.add_field(name="Commands", value=".close to close the ticket")

                        await channel.send(embed=em)

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.channel.id == 877249840805994538:
            if msg.author.id == 235088799074484224:
                await asyncio.sleep(600)
                await msg.delete()
            if msg.author.id == 861323291716354058:
                await asyncio.sleep(600)
                await msg.delete()
            else:
                await asyncio.sleep(30)
                await msg.delete()
        else:
            pass


def setup(client):
    client.add_cog(ModUtilsCog(client))
