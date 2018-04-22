import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='$')


class Pokemon:
    """Weaknesses & More"""

    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command=True, pass_context=True)
    async def gen_1(self,ctx,pokemon):
        
        if ctx.invoked_subcommand is None:
            await self.bot.say("""**__Error__**: You have either selected to incorrect Pokemon name or you used a capital letter. Please Try Again""")

    @gen_1.command(pass_context=True)
    async def bulbasaur(self,ctx):
        
        author = "Bulbasaur"
        description = ("#001")
        field_name = "Weakness"
        field_contents = "<:firetype:437249724538683393> <:icetype:437249726035787786> <:flyingtype:437249725658431490> <:psychictype:437249726908203028>"
        footer_text = "Created by ༒TᴀͪsͤʜᴋᴇᴛᴄʜͬᴜͤᴍͣL ™༒"

        embed = discord.Embed(colour=0x0FF00, description=description)  # Can use discord.Colour()
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/434542722121203712/437347577415860224/bulbasaur.gif")
        embed.title = "Pokedex Entry"
        embed.set_author(name="Bulbasaur", icon_url="https://cdn.discordapp.com/attachments/434779639320281111/437247916030164992/silenttrainers.png")
        embed.add_field(name="Types", value="<:grasstype:437249725796712468> <:poisontype:437249726790893578>")
        embed.add_field(name="Weakness", value="<:firetype:437249724538683393> <:icetype:437249726035787786> <:flyingtype:437249725658431490> <:psychictype:437249726908203028>")  # Can add multiple fields.
        embed.add_field(name="HP", value="45")
        embed.add_field(name="Attack", value="49")
        embed.add_field(name="Defense", value="49")
        embed.add_field(name="Sp. Attack", value="65")
        embed.add_field(name="Sp. Defense", value="65")
        embed.add_field(name="Speed", value="45")
        embed.add_field(name="Evolutions", value="#002 Ivysaur | #003 Venusaur")
        embed.set_footer(text=footer_text)

        await self.bot.say(embed=embed)
		

    @gen_1.command()
    async def ivysaur(self):
        
        author = "Ivysaur"
        description = ("#002")
        field_name = "Weakness"
        field_contents = "<:firetype:437249724538683393> <:icetype:437249726035787786> <:flyingtype:437249725658431490> <:psychictype:437249726908203028>"
        footer_text = "Created by ༒TᴀͪsͤʜᴋᴇᴛᴄʜͬᴜͤᴍͣL ™༒"

        embed = discord.Embed(colour=0x0FF00, description=description)  # Can use discord.Colour()
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/338042911528583170/437357991814234122/ivysaur.gif")
        embed.title = "Pokedex Entry"
        embed.set_author(name="Ivysaur", icon_url="https://cdn.discordapp.com/attachments/434779639320281111/437247916030164992/silenttrainers.png")
        embed.add_field(name="Types", value="<:grasstype:437249725796712468> <:poisontype:437249726790893578>")
        embed.add_field(name="Weakness", value="<:firetype:437249724538683393> <:icetype:437249726035787786> <:flyingtype:437249725658431490> <:psychictype:437249726908203028>")  # Can add multiple fields.
        embed.add_field(name="HP", value="60")
        embed.add_field(name="Attack", value="62")
        embed.add_field(name="Defense", value="63")
        embed.add_field(name="Sp. Attack", value="80")
        embed.add_field(name="Sp. Defense", value="80")
        embed.add_field(name="Speed", value="60")
        embed.add_field(name="Evolutions", value="#001 Bulbasaur | #003 Venusaur")
        embed.set_footer(text=footer_text)

        await self.bot.say(embed=embed)
		

    @gen_1.command()
    async def venusaur(self):
        
        author = "Venusaur"
        description = ("#003")
        field_name = "Weakness"
        field_contents = "<:firetype:437249724538683393> <:icetype:437249726035787786> <:flyingtype:437249725658431490> <:psychictype:437249726908203028>"
        footer_text = "Created by ༒TᴀͪsͤʜᴋᴇᴛᴄʜͬᴜͤᴍͣL ™༒"

        embed = discord.Embed(colour=0x0FF00, description=description)  # Can use discord.Colour()
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/338042911528583170/437358055743815680/venusaur.gif")
        embed.title = "Pokedex Entry"
        embed.set_author(name="Venusaur", icon_url="https://cdn.discordapp.com/attachments/434779639320281111/437247916030164992/silenttrainers.png")
        embed.add_field(name="Types", value="<:grasstype:437249725796712468> <:poisontype:437249726790893578>")
        embed.add_field(name="Weakness", value="<:firetype:437249724538683393> <:icetype:437249726035787786> <:flyingtype:437249725658431490> <:psychictype:437249726908203028>")  # Can add multiple fields.
        embed.add_field(name="HP", value="80")
        embed.add_field(name="Attack", value="82")
        embed.add_field(name="Defense", value="83")
        embed.add_field(name="Sp. Attack", value="100")
        embed.add_field(name="Sp. Defense", value="100")
        embed.add_field(name="Speed", value="80")
        embed.add_field(name="Evolutions", value="#001 Bulbasaur | #002 Ivysaur")
        embed.set_footer(text=footer_text)

        await self.bot.say(embed=embed)
		

def setup(bot):
    bot.add_cog(Pokemon(bot))

