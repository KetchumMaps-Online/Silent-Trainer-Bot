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
        """Bulbasaur Weakness & More"""
        author = "Bulbasaur"
        description = ("<:grasstype:437249725796712468> <:poisontype:437249726790893578>")
        field_name = "Weakness"
        field_contents = "<:firetype:437249724538683393> <:icetype:437249726035787786> <:flyingtype:437249725658431490> <:psychictype:437249726908203028>"
        footer_text = "Created by ༒TᴀͪsͤʜᴋᴇᴛᴄʜͬᴜͤᴍͣL ™༒"

        embed = discord.Embed(colour=0xFF0000, description=description)  # Can use discord.Colour()
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/434542722121203712/437347577415860224/bulbasaur.gif")
        embed.title = "Types"
        embed.set_author(name="Bulbasaur", icon_url="https://cdn.discordapp.com/attachments/434779639320281111/437247916030164992/silenttrainers.png")
        embed.add_field(name="Weakness", value="<:firetype:437249724538683393> <:icetype:437249726035787786> <:flyingtype:437249725658431490> <:psychictype:437249726908203028>")  # Can add multiple fields.
        embed.set_footer(text=footer_text)

        await self.bot.say(embed=embed)
		

    @gen_1.command()
    async def ivysaur(self):
        """Ivysaur Weakness & More"""
        author = "Ivysaur"
        description = ("<:grasstype:437249725796712468> <:poisontype:437249726790893578>")
        field_name = "Weakness"
        field_contents = "<:firetype:437249724538683393> <:icetype:437249726035787786> <:flyingtype:437249725658431490> <:psychictype:437249726908203028>"
        footer_text = "More Coming Soon"

        embed = discord.Embed(colour=0xFF0000, description=description)  # Can use discord.Colour()
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/338042911528583170/437357991814234122/ivysaur.gif")
        embed.title = "Types"
        embed.set_author(name="Ivysaur", icon_url="https://cdn.discordapp.com/attachments/434779639320281111/437247916030164992/silenttrainers.png")
        embed.add_field(name="Weakness", value="<:firetype:437249724538683393> <:icetype:437249726035787786> <:flyingtype:437249725658431490> <:psychictype:437249726908203028>")  # Can add multiple fields.
        embed.set_footer(text=footer_text)

        await self.bot.say(embed=embed)
		

    @gen_1.command()
    async def venusaur(self):
        """Venusaur Weakness & More"""
        author = "Venusaur"
        description = ("<:grasstype:437249725796712468> <:poisontype:437249726790893578>")
        field_name = "Weakness"
        field_contents = "<:firetype:437249724538683393> <:icetype:437249726035787786> <:flyingtype:437249725658431490> <:psychictype:437249726908203028>"
        footer_text = "More Coming Soon"

        embed = discord.Embed(colour=0xFF0000, description=description)  # Can use discord.Colour()
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/338042911528583170/437358055743815680/venusaur.gif")
        embed.title = "Types"
        embed.set_author(name="Venusaur", icon_url="https://cdn.discordapp.com/attachments/434779639320281111/437247916030164992/silenttrainers.png")
        embed.add_field(name="Weakness", value="<:firetype:437249724538683393> <:icetype:437249726035787786> <:flyingtype:437249725658431490> <:psychictype:437249726908203028>")  # Can add multiple fields.
        embed.set_footer(text=footer_text)

        await self.bot.say(embed=embed)
		

    @gen_1.command()
    async def charmander(self):
        """Charmander Weakness & More"""
        author = "Charmander"
        description = ("<:firetype:437249724538683393>")
        field_name = "Weakness"
        field_contents = "<:watertype:437249726476189698> <:ground:437249726400823316> <:rocktype:437249726698618880>"
        footer_text = "More Coming Soon"

        embed = discord.Embed(colour=0xFF0000, description=description)  # Can use discord.Colour()
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/338042911528583170/437358967853678592/charmander.gif")
        embed.title = "Types"
        embed.set_author(name="Charmander", icon_url="https://cdn.discordapp.com/attachments/434779639320281111/437247916030164992/silenttrainers.png")
        embed.add_field(name="Weakness", value="<:watertype:437249726476189698> <:ground:437249726400823316> <:rocktype:437249726698618880>")  # Can add multiple fields.
        embed.set_footer(text=footer_text)

        await self.bot.say(embed=embed)
		

    @gen_1.command()
    async def charmeleon(self):
        """Charmeleon Weakness & More"""
        author = "Charmeleon"
        description = ("<:firetype:437249724538683393>")
        field_name = "Weakness"
        field_contents = "<:watertype:437249726476189698> <:ground:437249726400823316> <:rocktype:437249726698618880>"
        footer_text = "More Coming Soon"

        embed = discord.Embed(colour=0xFF0000, description=description)  # Can use discord.Colour()
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/338042911528583170/437359639315742740/charmeleon.gif")
        embed.title = "Types"
        embed.set_author(name="Charmeleon", icon_url="https://cdn.discordapp.com/attachments/434779639320281111/437247916030164992/silenttrainers.png")
        embed.add_field(name="Weakness", value="<:watertype:437249726476189698> <:ground:437249726400823316> <:rocktype:437249726698618880>")  # Can add multiple fields.
        embed.set_footer(text=footer_text)

        await self.bot.say(embed=embed)
		

    @gen_1.command()
    async def charizard(self):
        """Charizard Weakness & More"""
        author = "Charizard"
        description = ("<:firetype:437249724538683393> <:flyingtype:437249725658431490>")
        field_name = "Weakness"
        field_contents = "<:watertype:437249726476189698> <:rocktype:437249726698618880> <:electrictype:437249725264166912>"
        footer_text = "More Coming Soon"

        embed = discord.Embed(colour=0xFF0000, description=description)  # Can use discord.Colour()
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/435121510449938444/437364888562696203/charizard.gif")
        embed.title = "Types"
        embed.set_author(name="Charizard", icon_url="https://cdn.discordapp.com/attachments/434779639320281111/437247916030164992/silenttrainers.png")
        embed.add_field(name="Weakness", value="<:watertype:437249726476189698> <:rocktype:437249726698618880> <:electrictype:437249725264166912>")  # Can add multiple fields.
        embed.set_footer(text=footer_text)

        await self.bot.say(embed=embed)
		

    @gen_1.command()
    async def squirtle(self):
        """Squirtle Weakness & More"""
        author = "Squirtle"
        description = ("<:watertype:437249726476189698>")
        field_name = "Weakness"
        field_contents = "<:grasstype:437249725796712468> <:electrictype:437249725264166912>"
        footer_text = "More Coming Soon"

        embed = discord.Embed(colour=0xFF0000, description=description)  # Can use discord.Colour()
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/435121510449938444/437369728688848896/squirtle.png")
        embed.title = "Types"
        embed.set_author(name="Squirtle", icon_url="https://cdn.discordapp.com/attachments/434779639320281111/437247916030164992/silenttrainers.png")
        embed.add_field(name="Weakness", value="<:grasstype:437249725796712468> <:electrictype:437249725264166912>")  # Can add multiple fields.
        embed.set_footer(text=footer_text)

        await self.bot.say(embed=embed)
		

    @gen_1.command()
    async def wartortle(self):
        """Wartortle Weakness & More"""
        author = "Wartortle"
        description = ("<:watertype:437249726476189698>")
        field_name = "Weakness"
        field_contents = "<:grasstype:437249725796712468> <:electrictype:437249725264166912>"
        footer_text = "More Coming Soon"

        embed = discord.Embed(colour=0xFF0000, description=description)  # Can use discord.Colour()
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/435121510449938444/437367249427365889/wartortle.gif")
        embed.title = "Types"
        embed.set_author(name="Wartortle", icon_url="https://cdn.discordapp.com/attachments/434779639320281111/437247916030164992/silenttrainers.png")
        embed.add_field(name="Weakness", value="<:grasstype:437249725796712468> <:electrictype:437249725264166912>")  # Can add multiple fields.
        embed.set_footer(text=footer_text)

        await self.bot.say(embed=embed)
		

    @gen_1.command()
    async def blastoise(self):
        """Blastoise Weakness & More"""
        author = "Blastoise"
        description = ("<:watertype:437249726476189698>")
        field_name = "Weakness"
        field_contents = "<:grasstype:437249725796712468> <:electrictype:437249725264166912>"
        footer_text = "More Coming Soon"

        embed = discord.Embed(colour=0xFF0000, description=description)  # Can use discord.Colour()
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/435121510449938444/437371179683020811/blastoise.gif")
        embed.title = "Types"
        embed.set_author(name=" Blastoise", icon_url="https://cdn.discordapp.com/attachments/434779639320281111/437247916030164992/silenttrainers.png")
        embed.add_field(name="Weakness", value="<:grasstype:437249725796712468> <:electrictype:437249725264166912>")  # Can add multiple fields.
        embed.set_footer(text=footer_text)

        await self.bot.say(embed=embed)
		

    @gen_1.command()
    async def caterpie(self):
        """Caterpie Weakness & More"""
        author = "Caterpie"
        description = ("<:bugtype:437249719497129996>")
        field_name = "Weakness"
        field_contents = "<:firetype:437249724538683393> <:rocktype:437249726698618880> <:flyingtype:437249725658431490>"
        footer_text = "More Coming Soon"

        embed = discord.Embed(colour=0xFF0000, description=description)  # Can use discord.Colour()
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/435121510449938444/437371773613375529/caterpie.gif")
        embed.title = "Types"
        embed.set_author(name="Caterpie", icon_url="https://cdn.discordapp.com/attachments/434779639320281111/437247916030164992/silenttrainers.png")
        embed.add_field(name="Weakness", value="<:firetype:437249724538683393> <:rocktype:437249726698618880> <:flyingtype:437249725658431490>")  # Can add multiple fields.
        embed.set_footer(text=footer_text)

        await self.bot.say(embed=embed)
		

    @gen_1.command()
    async def metapod(self):
        """Metapod Weakness & More"""
        author = "Metapod"
        description = ("<:bugtype:437249719497129996>")
        field_name = "Weakness"
        field_contents = "<:firetype:437249724538683393> <:rocktype:437249726698618880> <:flyingtype:437249725658431490>"
        footer_text = "More Coming Soon"

        embed = discord.Embed(colour=0xFF0000, description=description)  # Can use discord.Colour()
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/435121510449938444/437373874162892800/metapod.gif")
        embed.title = "Types"
        embed.set_author(name="Metapod", icon_url="https://cdn.discordapp.com/attachments/434779639320281111/437247916030164992/silenttrainers.png")
        embed.add_field(name="Weakness", value="<:firetype:437249724538683393> <:rocktype:437249726698618880> <:flyingtype:437249725658431490>")  # Can add multiple fields.
        embed.set_footer(text=footer_text)

        await self.bot.say(embed=embed)
		

    @gen_1.command()
    async def butterfree(self):
        """Butterfree Weakness & More"""
        author = "Butterfree"
        description = ("<:bugtype:437249719497129996> <:flyingtype:437249725658431490>")
        field_name = "Weakness"
        field_contents = "<:firetype:437249724538683393> <:icetype:437249726035787786> <:flyingtype:437249725658431490> <:psychictype:437249726908203028>"
        footer_text = "More Coming Soon"

        embed = discord.Embed(colour=0xFF0000, description=description)  # Can use discord.Colour()
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/435121510449938444/437374761396600832/butterfree.gif")
        embed.title = "Types"
        embed.set_author(name="Butterfree", icon_url="https://cdn.discordapp.com/attachments/434779639320281111/437247916030164992/silenttrainers.png")
        embed.add_field(name="Weakness", value="<:firetype:437249724538683393> <:rocktype:437249726698618880> <:icetype:437249726035787786> <:flyingtype:437249725658431490> <:electrictype:437249725264166912>")  # Can add multiple fields.
        embed.set_footer(text=footer_text)

        await self.bot.say(embed=embed)
		

    @gen_1.command()
    async def weedle(self):
        """Weedle Weakness & More"""
        author = "Weedle"
        description = ("<:bugtype:437249719497129996> <:poisontype:437249726790893578>")
        field_name = "Weakness"
        field_contents = "<:firetype:437249724538683393> <:rocktype:437249726698618880> <:icetype:437249726035787786> <:flyingtype:437249725658431490> <:psychictype:437249726908203028>"
        footer_text = "More Coming Soon"

        embed = discord.Embed(colour=0xFF0000, description=description)  # Can use discord.Colour()
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/435121510449938444/437376279109435423/weedle.gif")
        embed.title = "Types"
        embed.set_author(name="Weedle", icon_url="https://cdn.discordapp.com/attachments/434779639320281111/437247916030164992/silenttrainers.png")
        embed.add_field(name="Weakness", value="<:firetype:437249724538683393> <:rocktype:437249726698618880> <:icetype:437249726035787786> <:flyingtype:437249725658431490> <:psychictype:437249726908203028>")  # Can add multiple fields.
        embed.set_footer(text=footer_text)

        await self.bot.say(embed=embed)
		

    @gen_1.command()
    async def kakuna(self):
        """Kakuna Weakness & More"""
        author = "Kakuna"
        description = ("<:bugtype:437249719497129996> <:poisontype:437249726790893578>")
        field_name = "Weakness"
        field_contents = "<:firetype:437249724538683393> <:rocktype:437249726698618880> <:icetype:437249726035787786> <:flyingtype:437249725658431490> <:psychictype:437249726908203028>"
        footer_text = "More Coming Soon"

        embed = discord.Embed(colour=0xFF0000, description=description)  # Can use discord.Colour()
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/435121510449938444/437376973644234752/kakuna.gif")
        embed.title = "Types"
        embed.set_author(name="Kakuna", icon_url="https://cdn.discordapp.com/attachments/434779639320281111/437247916030164992/silenttrainers.png")
        embed.add_field(name="Weakness", value="<:firetype:437249724538683393> <:rocktype:437249726698618880> <:icetype:437249726035787786> <:flyingtype:437249725658431490> <:psychictype:437249726908203028>")  # Can add multiple fields.
        embed.set_footer(text=footer_text)

        await self.bot.say(embed=embed)
		

    @gen_1.command()
    async def beedrill(self):
        """Beedrill Weakness & More"""
        author = "Beedrill"
        description = ("<:bugtype:437249719497129996> <:poisontype:437249726790893578>")
        field_name = "Weakness"
        field_contents = "<:firetype:437249724538683393> <:rocktype:437249726698618880> <:icetype:437249726035787786> <:flyingtype:437249725658431490> <:psychictype:437249726908203028>"
        footer_text = "More Coming Soon"

        embed = discord.Embed(colour=0xFF0000, description=description)  # Can use discord.Colour()
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/435121510449938444/437377844134281230/beedrill.gif")
        embed.title = "Types"
        embed.set_author(name="Beedrill", icon_url="https://cdn.discordapp.com/attachments/434779639320281111/437247916030164992/silenttrainers.png")
        embed.add_field(name="Weakness", value="<:firetype:437249724538683393> <:rocktype:437249726698618880> <:icetype:437249726035787786> <:flyingtype:437249725658431490> <:psychictype:437249726908203028>")  # Can add multiple fields.
        embed.set_footer(text=footer_text)

        await self.bot.say(embed=embed)
		

    @gen_1.command()
    async def pidgey(self):
        """Pidgey Weakness & More"""
        author = "Pidgey"
        description = ("<:normaltype:437249726660739084> <:flyingtype:437249725658431490>")
        field_name = "Weakness"
        field_contents = "<:icetype:437249726035787786> <:rocktype:437249726698618880> <:electrictype:437249725264166912>"
        footer_text = "More Coming Soon"

        embed = discord.Embed(colour=0xFF0000, description=description)  # Can use discord.Colour()
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/437380847629369354/437380993155072000/pidgey.gif")
        embed.title = "Types"
        embed.set_author(name="Pidgey", icon_url="https://cdn.discordapp.com/attachments/434779639320281111/437247916030164992/silenttrainers.png")
        embed.add_field(name="Weakness", value="<:icetype:437249726035787786> <:rocktype:437249726698618880> <:electrictype:437249725264166912>")  # Can add multiple fields.
        embed.set_footer(text=footer_text)

        await self.bot.say(embed=embed)
		

    @gen_1.command()
    async def pidgeotto(self):
        """Pidgeotto Weakness & More"""
        author = "Pidgeotto"
        description = ("<:normaltype:437249726660739084> <:flyingtype:437249725658431490>")
        field_name = "Weakness"
        field_contents = "<:icetype:437249726035787786> <:rocktype:437249726698618880> <:electrictype:437249725264166912>"
        footer_text = "More Coming Soon"

        embed = discord.Embed(colour=0xFF0000, description=description)  # Can use discord.Colour()
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/437380847629369354/437380990638489600/pidgeotto.gif")
        embed.title = "Types"
        embed.set_author(name="Pidgeotto", icon_url="https://cdn.discordapp.com/attachments/434779639320281111/437247916030164992/silenttrainers.png")
        embed.add_field(name="Weakness", value="<:icetype:437249726035787786> <:rocktype:437249726698618880> <:electrictype:437249725264166912>")  # Can add multiple fields.
        embed.set_footer(text=footer_text)

        await self.bot.say(embed=embed)
		

    @gen_1.command()
    async def pidgeot(self):
        """Pidgeot Weakness & More"""
        author = "Pidgeot"
        description = ("<:normaltype:437249726660739084> <:flyingtype:437249725658431490>")
        field_name = "Weakness"
        field_contents = "<:icetype:437249726035787786> <:rocktype:437249726698618880> <:electrictype:437249725264166912>"
        footer_text = "More Coming Soon"

        embed = discord.Embed(colour=0xFF0000, description=description)  # Can use discord.Colour()
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/437380847629369354/437380988515909643/pidgeot.gif")
        embed.title = "Types"
        embed.set_author(name="Pidgeot", icon_url="https://cdn.discordapp.com/attachments/434779639320281111/437247916030164992/silenttrainers.png")
        embed.add_field(name="Weakness", value="<:icetype:437249726035787786> <:rocktype:437249726698618880> <:electrictype:437249725264166912>")  # Can add multiple fields.
        embed.set_footer(text=footer_text)

        await self.bot.say(embed=embed)
		

    @gen_1.command()
    async def rattata(self):
        """Rattata Weakness & More"""
        author = "Rattata"
        description = ("<:normaltype:437249726660739084>")
        field_name = "Weakness"
        field_name = "Evolutions"
        field_contents = "<:fightingtype:437249726069473290>"
        footer_text = "More Coming Soon"

        embed = discord.Embed(colour=0xFF0000, description=description)  # Can use discord.Colour()
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/437380847629369354/437380999572357130/rattata.gif")
        embed.title = "Types"
        embed.set_author(name="Rattata", icon_url="https://cdn.discordapp.com/attachments/434779639320281111/437247916030164992/silenttrainers.png")
        embed.add_field(name="Weakness", value="<:fightingtype:437249726069473290>")  # Can add multiple fields.
        embed.add_field(name="Evolutions", value="Raticate")
        embed.set_footer(text=footer_text)

        await self.bot.say(embed=embed)
		

    @gen_1.command()
    async def raticate(self):
        """Raticate Weakness & More"""
        author = "Raticate"
        description = ("<:normaltype:437249726660739084>")
        field_name = "Weakness"
        field_contents = "<:fightingtype:437249726069473290>"
        footer_text = "More Coming Soon"

        embed = discord.Embed(colour=0xFF0000, description=description)  # Can use discord.Colour()
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/437380847629369354/437380997105844245/raticate.gif")
        embed.title = "Types"
        embed.set_author(name="Raticate", icon_url="https://cdn.discordapp.com/attachments/434779639320281111/437247916030164992/silenttrainers.png")
        embed.add_field(name="Weakness", value="<:fightingtype:437249726069473290>")  # Can add multiple fields.
        embed.set_footer(text=footer_text)

        await self.bot.say(embed=embed)
		

    @gen_1.command()
    async def spearow(self):
        """Spearow Weakness & More"""
        author = "Spearow"
        description = ("<:normaltype:437249726660739084> <:flyingtype:437249725658431490>")
        field_name = "Weakness"
        field_contents = "<:rocktype:437249726698618880> <:icetype:437249726035787786> <:electrictype:437249725264166912>"
        footer_text = "More Coming Soon"

        embed = discord.Embed(colour=0xFF0000, description=description)  # Can use discord.Colour()
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/437380847629369354/437398640156475392/spearow.gif")
        embed.title = "Types"
        embed.set_author(name="Spearow", icon_url="https://cdn.discordapp.com/attachments/434779639320281111/437247916030164992/silenttrainers.png")
        embed.add_field(name="Weakness", value="<:rocktype:437249726698618880> <:icetype:437249726035787786> <:electrictype:437249725264166912>")  # Can add multiple fields.
        embed.set_footer(text=footer_text)

        await self.bot.say(embed=embed)
		

    @gen_1.command()
    async def fearow(self):
        """Fearow Weakness & More"""
        author = "Fearow"
        description = ("<:normaltype:437249726660739084> <:flyingtype:437249725658431490>")
        field_name = "Weakness"
        field_contents = "<:rocktype:437249726698618880> <:icetype:437249726035787786> <:electrictype:437249725264166912>"
        footer_text = "More Coming Soon"

        embed = discord.Embed(colour=0xFF0000, description=description)  # Can use discord.Colour()
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/437380847629369354/437398649111314443/fearow.gif")
        embed.title = "Types"
        embed.set_author(name="Fearow", icon_url="https://cdn.discordapp.com/attachments/434779639320281111/437247916030164992/silenttrainers.png")
        embed.add_field(name="Weakness", value="<:rocktype:437249726698618880> <:icetype:437249726035787786> <:electrictype:437249725264166912>")  # Can add multiple fields.
        embed.set_footer(text=footer_text)

        await self.bot.say(embed=embed)
		

    @gen_1.command()
    async def ekans(self):
        """Ekans Weakness & More"""
        author = "Ekans"
        description = ("<:poisontype:437249726790893578>")
        field_name = "Weakness"
        field_contents = "<:ground:437249726400823316> <:psychictype:437249726908203028>"
        footer_text = "More Coming Soon"

        embed = discord.Embed(colour=0xFF0000, description=description)  # Can use discord.Colour()
        embed.set_image(url="https://cdn.discordapp.com/attachments/437380847629369354/437398644283670539/ekans.gif")
        embed.title = "Types"
        embed.set_author(name="Ekans", icon_url="https://cdn.discordapp.com/attachments/434779639320281111/437247916030164992/silenttrainers.png")
        embed.add_field(name="Weakness", value="<:ground:437249726400823316> <:psychictype:437249726908203028>")  # Can add multiple fields.
        embed.set_footer(text=footer_text)

        await self.bot.say(embed=embed)
		

    @gen_1.command()
    async def arbok(self):
        """Arbok Weakness & More"""
        author = "Arbok"
        description = ("<:poisontype:437249726790893578>")
        field_name = "Weakness"
        field_contents = "<:ground:437249726400823316> <:psychictype:437249726908203028>"
        footer_text = "More Coming Soon"

        embed = discord.Embed(colour=0xFF0000, description=description)  # Can use discord.Colour()
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/437380847629369354/437398642832441366/arbok.gif")
        embed.title = "Types"
        embed.set_author(name="Arbok", icon_url="https://cdn.discordapp.com/attachments/434779639320281111/437247916030164992/silenttrainers.png")
        embed.add_field(name="Weakness", value="<:ground:437249726400823316> <:psychictype:437249726908203028>")  # Can add multiple fields.
        embed.set_footer(text=footer_text)

        await self.bot.say(embed=embed)

    
def setup(bot):
    bot.add_cog(Weakness(bot))
