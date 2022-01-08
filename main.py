from discord.ext import commands
import os
from keep_alive import keep_alive

bot = commands.Bot(command_prefix='>')

bot.lava_nodes = [
    {
        'host': 'lava.link',
        'port': 80,
        'rest_uri':  f'http://lava.link:80',
        'identifier': 'MAIN',
        'password': 'anything',
        'region': 'singapore',
            }
]


@bot.event
async def on_ready():
    print('Bot is ready to make you feel alive.')
    bot.load_extension('dismusic')
    bot.load_extension('dch')

my_secret = os.environ['TOKEN']

keep_alive()
bot.run(my_secret)
