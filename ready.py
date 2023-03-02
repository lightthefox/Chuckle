import discord
restartMsgChannel=1079858413841940480

restartMsg=""
with open("RestartMsg.txt","r") as f:
	restartMsg=f.read()

async def ready(client):
	print(f'Logged in as {client.user}')
	chn = client.get_channel(restartMsgChannel)
	await chn.send("Bot Restarted "+restartMsg)
	#while True:
# Setting `Listening ` status
	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="what does the joke bot do"))