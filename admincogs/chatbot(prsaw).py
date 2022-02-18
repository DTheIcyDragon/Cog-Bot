import discord
from discord.ext import commands
import randomstuff



class Chatbot(commands.Cog):
    def __init__(self, client):
        self.client = client



    @commands.command()
    async def chatinfo(self, ctx):
        em = discord.Embed(description="Dieser Chatbot ist mithilfe der PR-Saw libary geschrieben")
        await ctx.send(embed=em)

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.channel.id == 888788300930900018:

            try:

                with randomstuff.Client(api_key='L9NxBSFXUpp5') as chat:
                    response = chat.get_ai_response(msg.content)
                    em = discord.Embed(description=response.message)
                    await msg.channel.send(response.message)

            except:
                pass

def setup(client):
    client.add_cog(Chatbot(client))