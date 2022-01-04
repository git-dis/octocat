from platform import python_version

from disnake import Embed, AppCmdInter
from disnake.ext import commands

from octocat.config import Colour
from octocat.octocat import Octocat

class Status(commands.Cog):
    """The bot's status"""

    def __init__(self, bot: Octocat) -> None:
        self.bot = bot

    @commands.slash_command(description="Retrieve information about Octocat")
    async def status(self, inter: AppCmdInter) -> None:
        resp: Embed = Embed(colour=0xffffff, title="Octocat Status")
        resp.add_field(name="Python version", value=python_version())
        resp.add_field(name="Gateway Latency", value=f"{self.bot.latency * 1000:.2f}ms")
        await inter.response.send_message(
            embed=resp
        )

def setup(bot):
    bot.add_cog(Status(bot))