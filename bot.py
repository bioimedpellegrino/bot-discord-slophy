# bot.py
import os
from sys import intern

import discord
from discord.ext import commands

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
MIN_MEMBER_INVITES = 1
ROLE_NAME = "penonelungo"

intents = discord.Intents.all()
client = discord.Client(intents=intents)

bot = bot = commands.Bot(command_prefix="/")

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    for i in await member.guild.invites():
        print("ok")
        if i.inviter == member:
            print("ok")
    
@client.event
async def on_message(message):
    if message.content.startswith('!invites'):
        role = discord.utils.get(message.author.guild.roles, name=ROLE_NAME)
        totalInvites = 0
        for i in await message.guild.invites():
            if i.inviter == message.author:
                totalInvites += i.uses
        if totalInvites < MIN_MEMBER_INVITES:
            await message.channel.send(f"You've invited {totalInvites} member{'' if totalInvites == 1 else 's'} to the server!. Invite {MIN_MEMBER_INVITES} to get access to the whitelist!")
        else:
            for member_role in message.author.roles:
                if member_role == role:
                    return
            member = message.author
            await member.add_roles(role)
            await message.channel.send(f"Congratulations! You've invited {totalInvites} member{'' if totalInvites == 1 else 's'} to the server! Now you have been added to the whitelist channel :)")

client.run(TOKEN)
