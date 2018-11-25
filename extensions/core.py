import discord
from discord.ext import commands


class Core:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def invite(self, ctx):
        await ctx.send(f'<{self.bot.invite_url}>')

    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, name: str):
        """ Reloads an extension in the bot """
        m = await ctx.send(f'Reloading {name}')
        try:
            self.bot.unload_extension(f'extensions.{name}')
            self.bot.load_extension(f'extensions.{name}')
            await m.edit(content='Extension reloaded.')
        except (ImportError, SyntaxError, discord.ClientException) as e:
            stack_line = str(e).split('\n')[-1]
            await m.edit(content=f'Error while reloading {name}\n`{stack_line}`')
	
	async def load(self, ctx, name: str):
		""" Loads an extension in the bot. """
		m = await ctx.send(f'Loading {name}')
		try:
			self.bot.load_extension(f'extensions.{name}')
			await m.edit(content='Extension loaded.')
        except (ImportError, SyntaxError, discord.ClientException) as e:
            stack_line = str(e).split('\n')[-1]
            await m.edit(content=f'Error while loading {name}\n`{stack_line}`')

	async def unload(self, ctx, name: str):
		""" Loads an extension in the bot. """
		m = await ctx.send(f'Unloading {name}')
		try:
			self.bot.unload_extension(f'extensions.{name}')
			await m.edit(content='Extension unloaded.')
        except (ImportError, SyntaxError, discord.ClientException) as e:
            stack_line = str(e).split('\n')[-1]
            await m.edit(content=f'Error while unloading {name}\n`{stack_line}`')


def setup(bot):
    bot.add_cog(Core(bot))
