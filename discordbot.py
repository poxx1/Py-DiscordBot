import discord
import os

client = discord.Client()

@client.event
async def on_ready():
   #print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
  if message.content.startswith('Hol'):
        await message.channel.send('Tomatela flaco!')

    if message.content.startswith('75'):
        await message.channel.send('Me importa un carajo, tomatela te dije')

    if message.content.startswith('ja'):
        await message.channel.send('Quien te conoce papa?')
        
    if message.content.startswith('xd'):
        await message.channel.send('Atiendo boludos')

    if message.content.startswith('xD'):
        await message.channel.send('Sos un boludo y no tenes huevos')

client.run(os.getenv('token'))
