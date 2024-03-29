import discord
import random
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import requests
import os

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *, question):
    responses = ['It is certain.',
                'It is decidely so.',
                'Without a doubt.',
                'Yes - definitely',
                'You may rely on it',
                'As I see it, yes',
                'Most likely',
                'Outlook good',
                'Yes.',
                'Signs point to yes.',
                'Reply hazy, try again.',
                'Ask again later.',
                'Better not tell you now.',
                'Cannot predict now.',
                'Concentrate and ask again.',
                "Don't count on it.",
                'My reply is no.',
                'My sources say no.',
                'Outlook not too good',
                'Very doubtful']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

client.run(str(os.environ.get('NTk2MzUzNjQxMzgwNTc3Mjgw.XR6tZw.iOTb45jxsWKiuG1VxVWhXQSucOE')))
