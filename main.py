import discord
from discord.ext import commands
import random
import os
#from keep_alive import keep_alive

intents = discord.Intents().all()




client = commands.Bot(command_prefix = '.',intents = intents)

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send ('loading Cogs')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send ('Unloading Cogs')

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send ('Reloading Cogs')




 





for filename in os.listdir('cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
    

    


#keep_alive()
client.run('OTUwNjc1NzE1NzMxMzg2Mzg4.YicXwQ.wiXiD2UexsUkOXaW6JLLdPpCo8o')
