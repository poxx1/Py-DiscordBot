import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$Holi'):
        await message.channel.send('Quien te conoce papa?')

client.run(os.getenv('ODA5MTA5MTIzNzY4NjQ3NzAx.YCQTlw.Mnkmcufqn9I09_5kyDuiTQcK2Os'))
