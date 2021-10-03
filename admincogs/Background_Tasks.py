import random
import discord
from discord.ext import commands, tasks

role_names = []

def role_rename(role_name):
    role_before = str(role_name)
    role_after = str(random.choice(role_names))
    if role_before != role_after:
        return role_after
    else:
        role_rename(role_name=role_before)

class Tasks(commands.Cog):
    def __init__(self, client):
        self.client = client




@tasks.loop(minutes=1)
async def role_renamer(self):
    await self.client.wait_until_ready()
    while not self.client.is_closed():
        guild = self.client.get_guild(578446945425555464)
        role = guild.get_role(878748713491771423)
        await role.edit(name=role_rename(role_name=str(role.name)))


def setup(client):
    client.add_cog(Tasks(client))