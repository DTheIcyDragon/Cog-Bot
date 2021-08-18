import asyncio

import discord
from discord.ext import commands
import settings



class VerifyCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def verify(self, ctx):

        blacklist = [705800487517028493,#regelwerk
                     876917024838807692,#ankündigung
                     876916455915020308,#discord-updates
                     769620365403357254,#log
                     876924752881651843,#mod-talk
                     876917285539971082,#offen-für-alle
                     795043532951650324,#memes
                     851091679917375528,#meme-reife-zitate
                     877562448679411742,#commands
                     876921062602985533,#reports
                     876923450193752104,#mod-abstimmungen
                     876923627080155177,#richterliche-anträge
                     876923883419209738,#brett-der-schande
                     877244424185315389#freestuff
                     ]

        if any(blacklist):
            guild = ctx.guild
            true_member_count = len([m for m in ctx.guild.members if not m.bot])
            em = discord.Embed(title="✔ You got verified.",
                               description=f"You are the {true_member_count} Member.\nEnjoy and stick to the rules :)",
                               color=discord.Color.from_rgb(91, 238, 31))
            await ctx.send(embed = em)
            await asyncio.sleep(0.7)
            verified = guild.get_role(876927534904803398)
            await ctx.author.add_roles(verified, reason=f"Verifizierung von {ctx.author}", atomic=True)
            await ctx.channel.delete(reason="Verifizierung abgeschlossen")
        else:
            em = discord.Embed(title="An Error occurred!",
                               description="You are not allowed to use that command here",
                               color = discord.Color.red())
            await ctx.send(embed=em)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild = member.guild
        category = self.client.get_channel(settings.verify_category)

        verify_overwrite = {
            guild.default_role: discord.PermissionOverwrite(view_channel = False),
            member: discord.PermissionOverwrite(view_channel = True,
                                                send_messages = True)
        }

        channel = await guild.create_text_channel(name=f"Verify {member.display_name}",
                                                  overwrites=verify_overwrite,
                                                  category=category,
                                                  reason="Report Ticket")


        em = discord.Embed(title = f"Verifizierung für {member.display_name}",
                           description=f"Bitte sende in diesen Channel `.verify` wenn du bereit bist die Regeln dieses Discords zu akzeptieren.",
                           color=discord.Color.from_rgb(91, 238, 31))

        await channel.send(embed = em)



def setup(client):
    client.add_cog(VerifyCog(client))