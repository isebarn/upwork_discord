import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.content.startswith('clear'):
    channel = client.get_channel(int(os.environ.get('CHANNEL')))
    history = await channel.history(limit=200).flatten()
    counter = 0
    for message in history:
      counter += 1
      print("Deleted: {}/{}".format(counter, len(history)))

      try:
        await message.delete()
      except Exception as e:
        print('Cannot')


client.run(os.environ.get('PASSKEY'))

if __name__ == "__main__":
  print(os.environ.get('PASSKEY'))
  print(os.environ.get('CHANNEL'))