
import discord
from discord.ext import commands
import random
import os

#from keep_alive import keep_alive

intents = discord.Intents().all()




client = commands.Bot(command_prefix = '.',intents = intents)



@client.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.CommandNotFound):
        await ctx.send('Error:No Such Command Available!')





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




 





for filename in os.listdir('D:\Work\Coding\Python\Python Projects\Discord BOT Projects\Discord Bot(python) (jingz BOT)\jingz-BOT\cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
    

    


#keep_alive()
client.run(os.getenv("TOKEN"))
