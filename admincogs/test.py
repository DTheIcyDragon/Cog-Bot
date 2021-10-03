import discord
from discord.ext import commands



class TestCog(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):

        if after.channel.id == 876924799564279820:
            guild = member.guild
            category = self.client.get_channel(705789538005418044)

            verify_overwrite = {
                guild.default_role: discord.PermissionOverwrite(view_channel=False),
                member: discord.PermissionOverwrite(view_channel=True,
                                                    send_messages=True)
            }

            channel = await guild.create_voice_channel(name=f"Test",
                                                      overwrites=verify_overwrite,
                                                      category=category,
                                                      reason="Report Ticket")

            await member.move_to(channel = channel, reason = "Join to Create")

            blacklist = [878401060069339207,
                         878401877715329064,
                         876924799564279820,
                         876917960265048095,
                         876917443627483186,
                         876917487357267969,
                         876917569620168704,
                         876917598363738122,
                         876918694939344896,
                         876919378476691467,
                         878374791348895824,
                         878374688311611432,
                         876924305479450674,
                         876924191595704352
                         ]



            if before.channel.id not in blacklist:
                if len(before.members) == 0:
                    await before.delete()




def setup(client):
    client.add_cog(TestCog(client))