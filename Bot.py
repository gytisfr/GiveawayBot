#GiveawayBot by ~ Gytis5089

import discord.utils
import discord
import asyncio
import random
import os
from discord_buttons import DiscordButton, Button, ButtonStyle, InteractionType
from discord.ext import commands
from discord.utils import get
from discord.ext import menus

client = commands.Bot(command_prefix = 'give ', intents=discord.Intents.all())
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name=f"give help"))
    print('GiveawayBot now online.')
    print(f'We are running with {round(client.latency * 100)}ms ping.')

@client.command()
async def create(ctx, emoji, channel : discord.TextChannel, *, message):
    embed = discord.Embed(
        title="Giveaway",
        colour=0x7289DA,
        description=f"{message}\n\nSent by: {ctx.author.mention}"
    )
    givemessage = await channel.send(embed=embed)
    await givemessage.add_reaction(emoji)

@client.command()
async def end(ctx, *, message : discord.Message):
    users = await message.reactions[0].users().flatten()
    users = [member for member in users if member.id != client.user.id]
    winner = random.choice(users)
    embed = discord.Embed(
        title="Giveaway",
        colour=0x7289DA,
        description=f"Rolling...\n\nThe winner is; {str(winner)}"
    )
    await ctx.send(embed=embed)

@client.command()
async def help(ctx):
    embed = discord.Embed(
        title="Help",
        colour=0x7289DA,
        description="__**Creating:**__\ngive create `emoji` `channel` `message`\n\n__**Ending:**__\ngive end `message`\nFor the message, you use the message **ID**"
    )
    await ctx.send(embed=embed)

client.run('ODY4MTU4MTM3MzU2NjQ4NDU4.YPrlRQ.4VRU6MkK3ifcijJY0mrcsg40h8Y')