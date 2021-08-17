import  os, requests
from dotenv import load_dotenv, find_dotenv
import discord.ext
from discord.ext import commands
from cat import getcat
from num2words import num2words

load_dotenv(find_dotenv())

client = discord.Client()
client = commands.Bot(command_prefix='Give ')  # starting the


@client.event
async def on_ready():
	print("bot online")  # will print "bot online" in the console when the bot is online


@client.command()
async def ping(ctx):
	await ctx.send("PONG!")
	print("Sent a pong")


@client.command()
async def echo(ctx, *args):
	print(args)
	output = ''
	for word in args:
		output += word
		output += ' '
	await ctx.send(output)
	print("Sent an echo")


@client.command()
async def cat(ctx, *args):
	if not args:
		print("Sent a cat!")
		await ctx.channel.send(f'{ctx.author.mention}, Here is your cat!')
		await ctx.send(getcat())

	else:
		print(f"Sent {num2words(int(args[0]))} cats!")
		await ctx.channel.send(f'{ctx.author.mention}, Here is your {num2words(int(args[0]))} cats!')
		await ctx.send(getcat(int(args[0])))


@client.command()
async def fact(ctx):
	await ctx.send(requests.get("https://catfact.ninja/fact").json()['fact'])
	print("Sent a catfact")


client.run(os.getenv("TOKEN"))
