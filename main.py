import discord,requests,json,os,re,time,sys
from flask import Flask
from threading import Thread
from io import StringIO
from KeepAlive import home,run
from ready import ready
from commands import cmds

def keep_alive():
    t = Thread(target=run)
    t.start()
keep_alive()

version = "0.1.0-DEV"

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
	await ready(client)

@client.event
async def on_message(message):
	await cmds(message)
	
#client.run(os.environ["token"])
client.run("MTA3ODc1OTY1MjcxMzU4MjY5Mg.G6L6pt.6UtbgR4C7NPFqZtVk3A3Lbp9KeMa_fwx5zg3CU")