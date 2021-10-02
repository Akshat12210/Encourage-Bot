import discord
import os
import requests#to get data from api (https)
import json #store data in json file to use easily


client=discord.Client()


def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data=json.loads(response.text)
  quote=json_data[0]['q']+ " -    "+json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  # don't respond to ourselves
  if message.author == client.user:
    return
  if message.content.startswith('$inspire'):
    quote=get_quote()
    await message.channel.send(quote)

client.run(os.getenv('TOKEN'))