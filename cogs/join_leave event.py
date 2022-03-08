import discord
from discord.ext import commands



class jl(commands.Cog):

    def __init__(self, client):
        self.client=client

    
    
#for events
    @commands.Cog.listener()
    async def on_member_join (self,member):
        print(f'{member} Just Hopped into the  server!')
        jlchannel = self.client.get_channel(946781764339265617)
        await jlchannel.send(f'{member} Just Hopped into the  server!')

    @commands.Cog.listener()
    async def on_member_remove (self,member):
        print(f'{member} Just Left the Server')
        jlchannel = self.client.get_channel(946781764339265617)
        await jlchannel.send(f'{member} Just Left the Server')

def setup(client):
    client.add_cog(jl(client))