from discord.ext import commands
import discord
import requests

class FunStuff(commands.Cog):
    def __init__(self, bot, dirname):
        self.bot = bot
        self._last_member = None
        self.dirname = dirname
        
    @commands.command()
    async def inspirobot(self, ctx):
        payload = {"generate": "true"}
        r = requests.get("http://inspirobot.me/api", params=payload)
        embed = discord.Embed(title="A motivating quote from InspiroBot")
        embed.color = 0x33cc33
        embed.set_image(url=r.text)
        await ctx.trigger_typing()
        await ctx.send(embed=embed)
