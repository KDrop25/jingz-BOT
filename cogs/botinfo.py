import discord
from discord.ext import commands,tasks
from itertools import cycle

status = cycle(["to Ppl's Problems",'the executed Commands','Music',"Hydra's MOM",'bitches','errors aint my Job'])

class BotInfo(commands.Cog):

    def __init__(self, client):
        self.client=client
    
#for events
    @commands.Cog.listener()
    async def on_ready(self):
        BotInfo.change_status.start(self)
        await self.client.change_presence(status = discord.Status.idle,activity = discord.Activity(type=discord.ActivityType.listening, name=".Hello"))
        print('Servers are Back Online')
        
#for commands
    @commands.command(aliases = ['latency'])
    async def ping(self ,ctx):
        await ctx.send(f'Ping: {round(self.client.latency* 1000)}ms')

    @commands.command()
    async def about(self ,ctx):
        await ctx.send("**About:** this bot is made by **KDrop**")

#tasks
    @tasks.loop(seconds=10)
    async def change_status(self):
        await self.client.change_presence(activity = discord.Activity(type=discord.ActivityType.listening, name=(next(status))))

def setup(client):
    client.add_cog(BotInfo(client))











