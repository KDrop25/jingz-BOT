import discord
from discord.ext import commands

class modcmd(commands.Cog):

    def __init__(self, client):
        self.client=client
    
#for commands
    @commands.command()
    async def kick(self ,ctx, member : discord.Member, *,reason = None):
        await member.kick(reason = reason)
        await ctx.channel.purge(limit=1)
        await ctx.send(f'**"{member}"** has been kicked due to **Reason:** {reason}')

    @commands.command()
    async def ban(self,ctx, member : discord.Member, *,reason = None):
        await member.ban(reason = reason)
        await ctx.channel.purge(limit=1)
        await ctx.send(f'**"{member}"** has been banned due to **Reason:** {reason}')

    @commands.command()
    async def unban(self,ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name , member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user


            if (user.name , user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'UnBanned {user.mention}')
                return

    @commands.command()
    async def clear(self,ctx, amount=0,):
        if amount <= 0:
            await ctx.send('please enter the number of messages to delete after the ".clear" command')
        else:
            await ctx.channel.purge(limit=amount + 1)

def setup(client):
    client.add_cog(modcmd(client))