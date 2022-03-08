import discord
from discord.ext import commands
from discord.ext import tasks

class example(commands.Cog):

    def __init__(self, client):
        self.client=client
    
#for events
    @commands.Cog.listener()
    async def b(self):
        print('Servers are Back Online')
#for commands
    @commands.command(aliases = ['c'])
    async def a(self ,ctx):
        await ctx.send(f'Ping: {round(self.client.latency* 1000)}ms')

#tasks
    @tasks.loop(seconds=10)
    async def a(self,ctx):
        await ctx.send('task example')

def setup(client):
    client.add_cog(example(client))