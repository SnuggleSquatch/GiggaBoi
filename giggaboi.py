from asyncio.windows_events import NULL
from operator import truediv
import time
from discord import guild
from discord.voice_client import VoiceClient
import nacl
import json
import os
import discord
from discord import channel
from discord.channel import VoiceChannel
from discord.message import Message

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
configFile = open(os.path.join(__location__, 'config.json'))
jsonConfig = json.loads(configFile.read())
TOKEN = jsonConfig['TOKEN']

client = discord.Client()
@client.event
async def on_ready():
        print('Logged in as ' + str(client.user))

@client.event
async def on_message(message:discord.Message):
    print('Message from:' + str(message.author) + " content:" + str(message.content) + " channelId:" + str(message.channel.id))
    if message.author == client.user:
        return
    else:
        if message.content.upper() == 'POTATO':
            await message.channel.send('PotAHto')
        if message.content.upper() == 'TOMATO':
            await message.channel.send('TomAHto')        
        if message.content.upper() == 'CONNECTOME':
            await connectToUserVoiceChannel(message.author)
        if(message.content.upper() == 'DISCONNECTFROMME'):
            await disconnectFromVoiceChannel(message.author)
        if(message.content.upper() == 'KILLALLCONNECTIONS'):
            await killConnections()
        if(message.content.upper == 'PLAYTESTAUDIO'):
            await playTestAudio(message.author)
            str.

async def connectToUserVoiceChannel(user:discord.user):
    for voiceClient in client.voice_clients:
        if voiceClient.guild == user.guild:
            if user.voice == None or user.voice.channel == voiceClient.channel:
                print("Not a valid user or already connected to channel")
                return
    if(user.voice == None):
        return
    targetChannel = user.voice.channel
    await targetChannel.connect()

async def disconnectFromVoiceChannel(user:discord.user):
    for voiceClient in client.voice_clients:
            if voiceClient.guild == user.guild:
                if user.voice == None or user.voice.channel != voiceClient.channel:
                    print('Not a valid user or the user is not connected to the same channel as the bot.')
                    return
                else:
                    await voiceClient.disconnect()

async def killConnections():
    print("Killing All Connections!")
    for voiceClient in client.voice_clients:
        print("Killed Connection")
        await voiceClient.disconnect()

async def playTestAudio(user:discord.user):
    for voiceClient in client.voice_clients:
        if voiceClient.guild == user.guild:
            if user.voice == None or user.voice.channel != voiceClient.channel:
                return
            else:
                print("starting to play audio!")
                voiceClient.play('C:/Users/Tyson Shepherd/Music/test.mp3')



client.run(TOKEN)
