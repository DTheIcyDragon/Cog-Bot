import discord
import json
import os

from discord.ext import commands


async def update_data(users, user):
    if not f"{user.id}" in users:
        users[f"{user.id}"] = {}
        users[f"{user.id}"]["xp"] = 0
        users[f"{user.id}"]["level"] = 1


async def add_experience(users, user, xp):
    users[f"{user.id}"]["xp"] += xp



async def level_up(users, user, msg):
    os.chdir(r"/json-data")
    with open("level.json", "r") as g:
        levels = json.load(g)
    xp = users[f"{user.id}"]["xp"]
    lvl_start = users[f"{user.id}"]["level"]
    lvl_end = int(xp ** (1/4))
    if lvl_start < lvl_end:
        await msg.channel.send(f"{user.mention} reached level {lvl_end}")
        users[f"{user.id}"]["level"] = lvl_end


class Level(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def level(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author

        id = member.id
        os.chdir(r"/json-data")
        with open("level.json", "r") as f:
            users = json.load(f)
        lvl = users[str(id)]["level"]

        em = discord.Embed(description=f"{member} is on Level {lvl}")

        await ctx.send(embed=em, delete_after=20)





    @commands.Cog.listener()
    async def on_member_join(self, member):
        os.chdir(r"/json-data")
        with open('user.json', "r") as f:
            users = json.load(f)
        await update_data(users, member)

        os.chdir(r"/json-data")
        with open("user.json", "w") as f:
            json.dump(users, f, indent=4)


    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.author.bot == False:
            os.chdir(r"/json-data")
            with open("level.json", "r") as f:
                users = json.load(f)

            await update_data(users, msg.author)
            await add_experience(users, msg.author, 5)
            await level_up(users, msg.author, msg)
            os.chdir(r"/json-data")
            with open("level.json", "w") as f:
                json.dump(users, f, indent=4)



def setup(client):
    client.add_cog(Level(client))