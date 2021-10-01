import discord
from discord.ext import commands



class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        em = discord.Embed(title = f"Help for {ctx.author.display_name}",
                           color = discord.Color.magenta())
        em.add_field(name="Modules", value="Bot\nFun\nGames\nHelp\nLevel\nModeration\nModutils\nStats\nUtilitie\nVerification")

        await ctx.send(embed=em)


    @help.command()
    async def Bot(self, ctx):
        em = discord.Embed(title = "Help to the Bot Module",
                           description = "Syntax: `Command` [Required Argument] <Optional Argument>",
                           color = discord.Color.magenta())
        em.add_field(name="Uptime", value="Syntax: None", inline=False)
        em.add_field(name="Ping", value="Syntax: None", inline=False)
        em.add_field(name="Source", value="Syntax: None", inline=False)

        await ctx.send(embed=em)

    @help.command()
    async def Fun(self, ctx):
        em = discord.Embed(title = "Help to the Bot Module",
                           description = "Syntax: `Command` [Required Argument] <Optional Argument>",
                           color = discord.Color.magenta())
        em.add_field(name="Punish", value="Syntax: [User]", inline=False)
        em.add_field(name="Slap", value="Syntax: [User]", inline=False)
        em.add_field(name="Kill", value="Syntax: [User]", inline=False)
        em.add_field(name="Bonk", value="Syntax: [User]", inline=False)

        await ctx.send(embed=em)

    @help.command()
    async def Games(self, ctx):
        em = discord.Embed(title = "Help to the Bot Module",
                           description = "Syntax: `Command` [Required Argument] <Optional Argument>",
                           color = discord.Color.magenta())
        em.add_field(name="Guess", value="Syntax: [User]", inline=False)
        em.add_field(name="8Ball", value="Syntax: [Question]", inline=False)
        em.add_field(name="Roll", value="Syntax: [User]", inline=False)

        await ctx.send(embed=em)

    @help.command()
    async def Level(self, ctx):
        em = discord.Embed(title = "Help to the Bot Module",
                           description = "Syntax: `Command` [Required Argument] <Optional Argument>",
                           color = discord.Color.magenta())
        em.add_field(name="Level", value="Syntax: <User>", inline=False)

        await ctx.send(embed=em)

    @help.command()
    async def Moderation(self, ctx):
        em = discord.Embed(title = "Help to the Bot Module",
                           description = "Syntax: `Command` [Required Argument] <Optional Argument>",
                           color = discord.Color.magenta())
        em.add_field(name="Purge, Clear", value="Syntax: [User]", inline=False)
        em.add_field(name="Slap", value="Syntax: [User]", inline=False)
        em.add_field(name="Kill", value="Syntax: [User]", inline=False)
        em.add_field(name="Bonk", value="Syntax: [User]")

        await ctx.send(embed=em)

    @help.command()
    async def ModUtils(self, ctx):
        em = discord.Embed(title = "Help to the Bot Module",
                           description = "Syntax: `Command` [Required Argument] <Optional Argument>",
                           color = discord.Color.magenta())
        em.add_field(name="Report", value="Syntax: [User] [Reason]", inline=False)
        em.add_field(name="Close", value="Syntax: [Incident]", inline=False)

        await ctx.send(embed=em)

    @help.command()
    async def Stats(self, ctx):
        em = discord.Embed(title = "Help to the Bot Module",
                           description = "Syntax: `Command` [Required Argument] <Optional Argument>",
                           color = discord.Color.magenta())
        em.add_field(name="Password", value="Syntax:", inline=False)
        em.add_field(name="Suggestion", value="Syntax: [Suggestion]", inline=False)
        em.add_field(name="Timer", value="Syntax: [Seconds]", inline=False)
        em.add_field(name="Userinfo", value="Syntax: [User]", inline=False)

        await ctx.send(embed=em)

    @help.command()
    async def Music(self, ctx):
        em = discord.Embed(title = "Help to the Bot Module",
                           description = "Syntax: `Command` [Required Argument] <Optional Argument>",
                           color = discord.Color.magenta())

        em.add_field(name="Join", value="Syntax: ", inline=False)
        em.add_field(name="Leave", value="Syntax: ", inline=False)
        em.add_field(name="Play", value="Syntax: <Song to Play> if no song is provided a paused song will be played", inline=False)
        em.add_field(name="Pause", value="Syntax: ", inline=False)
        em.add_field(name="Stop", value="Syntax: ", inline=False)
        em.add_field(name="Skip", value="Syntax: ", inline=False)
        em.add_field(name="Previous", value="Syntax: ", inline=False)
        em.add_field(name="Shuffle", value="Syntax: ", inline=False)
        em.add_field(name="Repeat", value="Syntax: [none, one, all]", inline=False)
        em.add_field(name="Queue", value="Syntax: ", inline=False)
        em.add_field(name="Volume", value="Syntax: [Integer from 1 to 150]", inline=False)
        em.add_field(name="Lyrics", value="Syntax: ", inline=False)
        em.add_field(name="Np", value="Syntax: ", inline=False)
        em.add_field(name="SkipTo", value="Syntax: [Index]", inline=False)
        em.add_field(name="Restart", value="Syntax: ", inline=False)
        await ctx.send(embed=em)

def setup(client):
    client.add_cog(Help(client))