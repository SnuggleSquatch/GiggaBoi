from asyncio.windows_events import NULL
from operator import truediv
import time
from discord import guild
from discord.player import FFmpegAudio, FFmpegPCMAudio
from discord.voice_client import VoiceClient
import nacl
import json
import os
import youtube_dl
from youtube_dl.YoutubeDL import YoutubeDL
import youtube_dl.downloader
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
        print (message.content.upper())
        if 'POTATO' in message.content.upper():
            await message.channel.send(ReplaceAllOccurences(message.content,'potato','PotAHto'))
        #if 'POTATO' in message.content.upper():
        #   await message.channel.send("PotAHto")
        if "TOMATO" in message.content.upper():
            await message.channel.send("TomAHto")        
        if message.content.upper() == "CONNECTTOME":
            print("connecting to user")
            await connectToUserVoiceChannel(message.author)
        if(message.content.upper() == "DISCONNECTFROMME"):
            print("disconnecting to user")
            await disconnectFromVoiceChannel(message.author)
        if(message.content.upper() == "KILLALLCONNECTIONS"):
            await killConnections()
        if(message.content.upper() == 'PLAYTESTAUDIO'):
            await playTestAudio(message.author)
        if(message.content.upper() == "BITCOIN"):
            await gilfoylesayshi(message.author)   

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
                print("starting test audio...")
                ytdlOptions = {
                    'format':'bestaudio/best',
                    'outtmpl':'C:/Users/Tyson Shepherd/Desktop/GiggaBoi/test.mp3',
                    'postprocessors': [{
                        'key':'FFmpegExtractAudio',
                        'preferredcodec':'mp3',
                        'preferredquality':'0'
                    }]
                }
                #if(os.path.exists('C:/Users/Tyson Shepherd/Desktop/GiggaBoi/test.mp3')):
                #    os.remove('C:/Users/Tyson Shepherd/Desktop/GiggaBoi/test.mp3')
                #else:
                #    print("file doesn't exist")
                #YoutubeDL(ytdlOptions).download(['https://www.youtube.com/watch?v=h2dJ-JUzhVs'])
                audioFile = discord.FFmpegPCMAudio("C:/Users/Tyson Shepherd/Desktop/GiggaBoi/WAP.mp3", executable="C:/Users/Tyson Shepherd/Desktop/GiggaBoi/ffmpeg/bin/ffmpeg.exe")
                voiceClient.play(audioFile)
                print("playing audio")

async def gilfoylesayshi(user:discord.user):
    for VoiceClient in client.voice_clients:
        if VoiceClient.guild == user.guild:
            if user.voice == None or user.VoiceChannel != VoiceClient.channel:
                return
            else:
                ytdlOptions = {
                    'format':'bestaudio/best',
                    'outtmpl':'C:/Users/Tyson Shepherd/Desktop/GiggaBoi/test.mp3',
                    'postprocessors': [{
                        'key':'FFmpegExtractAudio',
                        'preferredcodec':'mp3',
                        'preferredquality':'0'
                    }]
                }
                audioFile = discord.FFmpegPCMAudio("C:/Users/Tyson Shepherd/Desktop/GiggaBoi/gilfoylesayshi.mp3", executable="C:/Users/Tyson Shepherd/Desktop/GiggaBoi/ffmpeg/bin/ffmpeg.exe")                  
                VoiceClient.play(audioFile)
                
def ReplaceAllOccurences(input:str, substringToReplace:str, substringSubstituion:str):
    output = input
    upperCaseInput = input.upper()
    
    i=0
    stepbackAmount = len(substringSubstituion) - len(substringToReplace)
    stepCount = 0
    while i < len(upperCaseInput):
        foundIndex = upperCaseInput.find(substringToReplace.upper(),i)
        if foundIndex != -1:
            upperCaseInput = upperCaseInput.replace(substringToReplace.upper(),substringSubstituion,1)
            i = foundIndex + len(substringToReplace) + stepbackAmount
            output = output[0:foundIndex] + substringSubstituion + output[foundIndex + len(substringToReplace):len(output)]
        else:
            break
    return(output)

client.run(TOKEN)
