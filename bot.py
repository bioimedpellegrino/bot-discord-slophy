# bot.py
import os
from sys import intern

import discord
from discord.ext import commands

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
MIN_MEMBER_INVITES = 20
ROLE_NAME = "WhiteList Member"

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
    print(message.channel.id)
    if message.content.startswith('!invites') and str(message.channel.id).strip() == '925018144072949760': #id ranks and leaderbord
        role = discord.utils.get(message.author.guild.roles, name=ROLE_NAME)
        totalInvites = 0
        for i in await message.guild.invites():
            if i.inviter == message.author:
                totalInvites += i.uses
        if totalInvites < MIN_MEMBER_INVITES:
            await message.channel.send(f"You've invited {totalInvites} member{'' if totalInvites == 1 else 's'} to the server! Invite {MIN_MEMBER_INVITES} to get access to the whitelist!")
        else:
            for member_role in message.author.roles:
                if member_role == role:
                    await message.channel.send(f"You've invited {totalInvites} member{'' if totalInvites == 1 else 's'} to the server!")
                    return
            member = message.author
            await member.add_roles(role)
            await message.channel.send(f"Congratulations! You've invited {totalInvites} member{'' if totalInvites == 1 else 's'} to the server! Now you have been added to the whitelist channel :)")
    elif message.content.startswith('!gabino') and str(message.channel.id).strip() == '922952926798962688': #id moderators-only
        await message.channel.send("CAZZO MI FA MALEEEE IL CAZZOOOOOOOOOOO!")
    elif message.content.startswith('!ivan') and str(message.channel.id).strip() == '922952926798962688': #id moderators-only
        await message.channel.send("Ivan ha il penone grande quanto la tour Eiffel! Parola di Francesco Amadori")
    elif message.content.startswith('!foodemperor') and str(message.channel.id).strip() == '922952926798962688': #id moderators-only
        await message.channel.send("Sono food emperor. Hai trovato il migliore easter egg. Cazzoooo mi fa male il cazzo, guardati questo cazzo di video. https://www.youtube.com/watch?v=OjVUdJD-WRQ")
    elif message.content.startswith('!lucamorocutti') and str(message.channel.id).strip() == '922952926798962688': #id moderators-only
        await message.channel.send("Luca scopa come un dannato! Te lo dico io che sono un bot (quindi mi faccio le bottane)")

client.run(TOKEN)
