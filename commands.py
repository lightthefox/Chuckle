import discord
import sys
sys.path.insert(1, './commands')
import chuckleTalk as chTalk
import joke 
import Help

chuckleresponses=[]
with open("chuckleResponses.lgdb","r") as f:
	b = f.read().split("\n")
	for i in b:
		chuckleresponses.append(i.split("|"))
#print(chuckleresponses)


async def cmds(message):
	doNothing=False
	if message.content.startswith('chuckleTalk') and message.author.guild_permissions.administrator:
		chTalk.chuckleTalk(message)
	elif message.content.startswith('jokeEmbed'):
		joke.jokeEmbed(message)
	elif message.content.startswith('joke'):
		joke.jokePT(message)
	elif message.content.startswith('what does the joke bot do'):
		Help.help(message)
	else:
		for i in chuckleresponses:
			#await message.channel.send("testing arrView["+i[0]+","+i[1]+"]")
			if i[0] in message.content:
				#insults=False
				await message.channel.send(i[1])
				break
			else:
				doNothing = True
				#await message.channel.send#("[Debug] No response found...")
				#insults=True