import datetime

import discord
from discord.ext import commands

import base_cmds
import events
import mod_cmds
import other_cmds
import voice_cmds

start_time = datetime.datetime.now(datetime.UTC)
token = 'token here'
intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix='x!', intents=intents)

# do things while we are ready
@client.event
async def on_ready():
    client.remove_command('help')

    await client.add_cog(events.Events(client))
    await client.add_cog(base_cmds.BaseCommands(client, start_time))
    await client.add_cog(mod_cmds.ModCommands(client))
    await client.add_cog(other_cmds.OtherCmds(client))
    await client.add_cog(voice_cmds.VoiceCommands(client))

    print('Servers connected to:')

    for guild in client.guilds:
        print(guild.name)

    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f" x!help"))

client.run(token)
