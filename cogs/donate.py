import discord
from discord.ext import commands

class Donation:
    """Donations"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=False)
    async def donate(self):
        """Donations"""
        await self.bot.say("**__PayPal__**\nhttp://www.paypal.me/ketchumamps\nDonate to help keep things going")

def setup(bot):
    bot.add_cog(Donation(bot))
