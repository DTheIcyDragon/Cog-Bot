import discord
from discord.ext import commands, tasks

#Defenitionen


class REPLACE_ME(commands.Cog):
    def __init__(self, client):
        self.client = client



#CODE



def setup(client):
    client.add_cog(REPLACE_ME(client))