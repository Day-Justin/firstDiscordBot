# Example bot following minimalbot documentation on Discord.py

import discord
#imports the discord library from discord.py

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
#Client is the connection to Discord, and we use it as a declorator of events

#the library is asynchronous, so events are handled in a 'callback' manner
#A callback is a function that is called in response to an event

@client.event
async def on_ready():
	print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
	if message.author == client.user:
		return
#on_message reacts to every message, so the bot needs to ignore messages from its self
	
	if message.content.startswith('$hello'):
		await message.channel.send("Hello!')
#

client.run('token here')
