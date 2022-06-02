import requests
import json
import random
import nextcord
import asyncio
import os
from urllib import parse, request
from nextcord.ext import commands
from nextcord.utils import get
from nextcord import Color
from asyncio import sleep as s

bot = commands.Bot(command_prefix="!", help_command=None)

# loading the breathing and prompts files
gifs = json.load(open("gifs.json"))
prompts = json.load(open("journal.json"))


# hello
@bot.command(name="hi", aliases=["hello", "hey"])
async def SendMessage(ctx):
    await ctx.send('type !help for a list of my commands')

# help command


@bot.command()
async def help(ctx):
    colourz = nextcord.Colour.from_rgb(199, 237, 228)
    helper = nextcord.Embed(
        title="hello there! i'm stevan, a mental health bot", description="", type="rich", color=colourz)
    helper.add_field(
        name='`!bob`', value='get a bob ross quote', inline=True)
    helper.add_field(
        name='`!bored`', value='get an activity to do', inline=True)
    helper.add_field(
        name='`!breathe`', value='get a breathing exercise', inline=True)
    helper.add_field(
        name='`!remind`', value='remind a user [!remind @username time units (choose from s, m, h, d) message]', inline=False)
    helper.add_field(
        name='`!remindme`', value='remind yourself [!remindme time units (choose from s, m, h, d) message]', inline=False)
    helper.add_field(
        name='`!remindall`', value='remind everyone [!remindall time units (choose from s, m, h, d) message]', inline=False)
    helper.add_field(
        name='`!art`', value='get an art journal prompt', inline=True)
    helper.add_field(
        name='`!write`', value='get a journal prompt', inline=True)
    await ctx.send(embed=helper)
# get random activity


@bot.command()
async def bored(ctx):
    r = requests.get('http://www.boredapi.com/api/activity/').json()
    task = r['activity']
    await ctx.send(task)

# get bob ross quote


@bot.command()
async def bob(ctx):
    g = requests.get('https://api.bobross.dev/api').json()
    quote = g['response'][0]['quote']
    await ctx.send(quote)

# breathing exercises


@bot.command()
async def breathe(ctx):
    breather = random.choice(gifs["breathe"])
    await ctx.send(f"you're going to be alright, friend. just follow along \n {breather}")

# journal prompts


@ bot.command(name="journal", aliases=["write", "art"])
async def Journal(ctx):
    prompt = random.choice(prompts[ctx.invoked_with])
    await ctx.send(f"here's a journal prompt: {prompt}")


# reminders


@ bot.command()
async def remindme(ctx, time: str, *, msg):
    delayz = float(time[:-1])
    units = time[-1]

    if (units == 's'):
        await s(delayz)
    elif (units == 'm'):
        await s(60*delayz)
    elif (units == 'h'):
        await s(3600*delayz)
    elif (units == 'd'):
        await s(86400*delayz)

    await ctx.send(f'hey {ctx.author.mention}, reminding you: {msg}')


@ bot.command()
async def remindall(ctx, time: str, *, msg):
    delayz = float(time[:-1])
    units = time[-1]

    if (units == 's'):
        await s(delayz)
    elif (units == 'm'):
        await s(60*delayz)
    elif (units == 'h'):
        await s(3600*delayz)
    elif (units == 'd'):
        await s(86400*delayz)

    await ctx.send(f'hey @everyone, reminding you: {msg}')


@ bot.command()
async def remind(ctx, user: nextcord.Member, time: str, *, msg):
    delayz = float(time[:-1])
    units = time[-1]

    if (units == 's'):
        await s(delayz)
    elif (units == 'm'):
        await s(60*delayz)
    elif (units == 'h'):
        await s(3600*delayz)
    elif (units == 'd'):
        await s(86400*delayz)

    await ctx.send(f'hey {user.mention}, reminding you: {msg}')


@ bot.event
async def on_ready():
    print('running')

if __name__ == '__main__':
    bot.run(os.environ["DISC_TOKEN"])
