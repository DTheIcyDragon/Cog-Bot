import discord
import random
import asyncio
from discord.ext import commands

class Games(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def guess(self, ctx):
        rand1 = random.randint(0, 37)
        rand2 = random.randint(63, 100)
        guess_answer = random.randint(rand1, rand2)
        #    print(guess_answer)
        em = discord.Embed(title="Guess",
                           description="Guess a number between " + str(rand1) + " and " + str(rand2) + ".",
                           color=discord.Color.dark_green())
        await ctx.send(embed=em)

        def is_correct_guess(m):
            return m.author == ctx.author and m.content.isdigit()

        try:
            user_guess = await self.client.wait_for('message', check=is_correct_guess, timeout=10.0)
        except asyncio.TimeoutError:
            em = discord.Embed(title="Timed Out",
                               description=f'Your guess took too long the correct was answer was {guess_answer}',
                               color=discord.Color.dark_green())
            return await ctx.channel.send(embed=em)

        if int(user_guess.content) == guess_answer:
            em = discord.Embed(title="Correct", description="You guessed right.", color=0xff0000)
            await ctx.channel.send(embed=em)

        else:
            em = discord.Embed(title="You were Wrong", description="Correct was "f'{guess_answer}', color=0xe81717)
            await ctx.channel.send(embed=em)

    @commands.command(aliases=["8ball"])
    async def _8ball(self, ctx, *, question):
        ball_choices = [" It is certain.", " It is decidedly so.", " Without a doubt.", " Yes – definitely.",
                        "You may rely on it.",
                        " As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
                        "Reply hazy, try again.",
                        "Ask again later.", "Better not tell you now.", "Cannot predict now.",
                        "Concentrate and ask again.",
                        "Don’t count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.",
                        "Very doubtful."]

        ball_choice = random.choice(ball_choices)
        em = discord.Embed(description=f"**Question:** {question}\n **" + ball_choice + "**", color=discord.Color.dark_green())

        await ctx.send(embed=em)

    @commands.command()
    async def roll(self, ctx, dice_size = 6, trows = 1):
        answer = []
        for i in range(int(trows)):
            choice = random.randint(1,int(dice_size))
            answer.append(choice)

        em = discord.Embed(title=f"{ctx.author.display_name}", description=answer, color=discord.Color.dark_green())
        await ctx.send(embed=em)

def setup(client):
    client.add_cog(Games(client))