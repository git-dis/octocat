from discord.ext.commands import Cog, Bot, Context, command
from discord import Embed, Guild, Invite, Member
from datetime import datetime

class Ping(Cog):
    """
    Provides information about bot latency.
    """

    def __init__(self, bot: Bot) -> None:
        self.bot: Bot = bot
        return

    @command(description='Returns bot latency')
    async def ping(self, ctx: Context) -> None:
        """
        Returns two types of latency:
        1. The processing time it takes for the bot to register a command
        2. The Discord API Latency. Measures the time between a `HEARTBEAT` and a `HEARTBEAT_ACK`
        """
        current_time: datetime = datetime.utcnow()
        message_creation: datetime = ctx.message.created_at
        command_time: float = (current_time - message_creation).total_seconds() * 1000
        command_time: str = f'{command_time:.3f} ms'

        # Discord returns latency in seconds not milliseconds
        api_ping: str = f'{self.bot.latency * 1000:.3f} ms'

        embed: Embed = Embed(
            title='Pong!',
            colour=0x00d166
        )

        embed.timestamp = current_time

        user: Member = ctx.author
        user_info: str = f"{user.display_name}#{user.discriminator}"
        embed.set_footer(text=f"Requested by {user_info}")

        for description, latency in zip(['Command Processing Time', 'Discord API Latency'], [command_time, api_ping]):
            embed.add_field(
                name=description,
                value=latency,
                inline=False
            )

        await ctx.send(embed=embed)
        return

def setup(bot: Bot):
    bot.add_cog(Ping(bot))
