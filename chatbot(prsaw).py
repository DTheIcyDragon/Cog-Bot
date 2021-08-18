import discord
from discord.ext import commands
from prsaw import RandomStuffV2



class HelpCog(commands.Cog):
    def __init__(self, client):
        self.client = client



    @commands.command()
    async def chatinfo(self, ctx):
        em = discord.Embed(description="Dieser Chatbot ist mithilfe der PR-Saw libary geschrieben")
        await ctx.send(embed=em)

    @commands.Cog.listener()
    async def on_message(self, msg):
        rs = RandomStuffV2()
        if self.client.user == msg.author:
            return
        if msg.channel.id == 866622671064268811:
            response = rs.get_ai_response(msg.content)
            await msg.reply(response)
        await self.client.process_commands(msg)

def setup(client):
    client.add_cog(HelpCog(client))