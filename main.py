from webbrowser import get
import aiohttp
import pycord
import discord
import asyncio
from discord.ext import commands
import random
import requests
from keep_alive import keep_alive
import logging
import datetime
import os 


bot = discord.Bot(debug_guilds=[931093864503201813, 952860765352755261], command_prefix="!")
discord.Intents.all()
@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")
    await bot.change_presence(activity=discord.Game('SBI'))
owner_id = 405356071989936129

@bot.slash_command(name = "hello", description = "Say hello to the bot")
async def hello(ctx):
    await ctx.respond("Hey!")

@bot.slash_command(name = "ban", description = "Ban a user from the server")
async def ban(ctx, member: discord.Member, *, reason = None):
    if ctx.author.guild_permissions.ban_members:
        await member.ban(reason = reason)
        await ctx.respond(f"{member} has been banned ✔️", ephemeral=True)
    else:
        await ctx.respond("You do not have the permissions to ban members", ephemeral=True)

@bot.slash_command(name = "kick", description = "Kick a user from the server")
async def kick(ctx, member: discord.Member, *, reason = None):
    if ctx.author.guild_permissions.kick_members:
        await member.kick(reason = reason)
        await ctx.respond(f"{member} has been kicked", ephemeral=True)
    else:
        await ctx.respond("You do not have the permissions to kick members", ephemeral=True)
@bot.slash_command(name = "avatar", description = "Gets the avatar of a user")
async def avatar(ctx, member: discord.Member):
    embed = discord.Embed(title = f"{member}'s avatar", description = f"{member.mention}", color = 0x00ff00)
    embed.set_image(url = member.avatar.url)
    await ctx.respond(embed = embed, ephemeral=True)
#help command slash commands
@bot.slash_command(name = "help", description = "Gets info about the bot")
async def help(ctx):
    embed = discord.Embed(title = "Help", description = "Here are the commands", color = 0x00ff00)
    embed.add_field(name = "/hello", value = "Says hello to the bot")
    embed.add_field(name = "/ban", value = "Ban a user from the server")
    embed.add_field(name = "/kick", value = "Kick a user from the server")
    embed.add_field(name = "/userinfo", value = "Gets info about a user")
    embed.add_field(name = "/avatar", value = "Gets the avatar of a user")
    embed.add_field(name = "/help", value = "Gets info about the bot")
    await ctx.respond(embed = embed, ephemeral=True)
#dm member admin perms
@bot.slash_command(name = "dm", description = "Dm a member")
async def dm(ctx, member: discord.Member, *, message):
    if ctx.author.guild_permissions.administrator:
        await member.send(message)
        await ctx.respond(f"{member} has been dmed", ephemeral=True)
    else:
        await ctx.respond("You do not have the permissions to use this command", ephemeral=True)
#send msg in a channel with and channel id
@bot.slash_command(name = "send", description = "Send a message in a channel")
async def send(ctx, channel_id, *, message):
    if ctx.author.guild_permissions.manage_messages:
        channel = bot.get_channel(int(channel_id))
        await channel.send(message)
        await ctx.respond(f"Message sent in {channel}", ephemeral=True)
    else:
        await ctx.respond("You do not have the permissions to use this command", ephemeral=True)
#purge 
@bot.slash_command(name = "purge", description = "Purge a number of messages")
async def purge(ctx, amount: int):
    if ctx.author.guild_permissions.manage_messages:
        await ctx.channel.purge(limit = amount)
        await ctx.respond(f"{amount} messages have been purged", ephemeral=True)
    else:
        await ctx.respond("You do not have the permissions to use this command", ephemeral=True)
#ping 
@bot.slash_command(name = "ping", description = "Ping the bot")
async def ping(ctx):
    await ctx.respond(f"**Pong** :ping_pong:{round(bot.latency * 1000)}ms", ephemeral=True)
#add role
@bot.slash_command(name = "addrole", description = "Add a role to a user")
async def addrole(ctx, member: discord.Member, role: discord.Role):
    if ctx.author.guild_permissions.manage_messages:
        await member.add_roles(role)
        await ctx.respond(f"{member} has been given the {role} role", ephemeral=True)
    else:
        await ctx.respond("You do not have the permissions to use this command")
#slowmode command with permissions accepts an channel id
@bot.slash_command(name = "slowmode", description = "Slowmode a channel")
async def slowmode(ctx, channel_id, amount: int):
    if ctx.author.guild_permissions.manage_messages:
        channel = bot.get_channel(int(channel_id))
        await channel.edit(slowmode_delay = amount)
        await ctx.respond(f"{channel} has been slowed to {amount} seconds :white_check_mark:", ephemeral=True)
    else:
        await ctx.respond("You do not have the permissions to use this command")
#rename channel with permission
@bot.slash_command(name = "rename", description = "Rename a channel")
async def rename(ctx, channel_id, *, name):
    if ctx.author.guild_permissions.manage_channels:
        channel = bot.get_channel(int(channel_id))
        await channel.edit(name = name)
        await ctx.respond(f"{channel} has been renamed to {name}", ephemeral=True)
    else:
        await ctx.respond("You do not have the permissions to use this command")
#lbs to kgs
@bot.slash_command(name = "lbs", description = "Convert lbs to kgs")
async def lbs(ctx, lbs: float):
        kgs = lbs * 0.45359237
        await ctx.respond(f"{lbs} lbs is {kgs} kgs", ephemeral=True)
#rickroll command
@bot.slash_command(name = "rickroll", description = "Rickroll a user")
async def rickroll(ctx, member: discord.Member):
    if ctx.author.guild_permissions.manage_messages:
        await member.send("https://tenor.com/view/rickroll-roll-rick-never-gonna-give-you-up-never-gonna-gif-22954713")
        await ctx.respond(f"{member} has been rickrolled", ephemeral=True)
    else:
        await ctx.respond("You do not have the permissions to use this command")
#8ball
@bot.slash_command(name = "magicball", description = "Ask the bot a question")
async def eightball(ctx, *, question):
        responses = ["It is certain", "It is decidedly so", "Without a doubt", "Yes, definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]
        await ctx.respond(f"Question: {question}\nAnswer: {random.choice(responses)}")
#nick member
@bot.slash_command(name = "nick", description = "Nick a member")
async def nick(ctx, member: discord.Member, *, name):
    if ctx.author.guild_permissions.manage_nicknames:
        await member.edit(nick = name)
        await ctx.respond(f"{member} has been renamed to {name}", ephemeral=True)
    else:
        await ctx.respond("You do not have the permissions to use this command")
#remove send message from channel
@bot.slash_command(name = "remove", description = "Remove a message from a channel")
async def remove(ctx, channel_id, message_id):
    if ctx.author.guild_permissions.manage_messages:
        channel = bot.get_channel(int(channel_id))
        message = await channel.fetch_message(int(message_id))
        await message.delete()
        await ctx.respond(f"{message} has been removed", ephemeral=True)
    else:
        await ctx.respond("You do not have the permissions to use this command")
#send rickroll in channel with id of channel
@bot.slash_command(name = "rickrollchannel", description = "Rickroll a user in a channel", reason = "Rickroll by bot")
async def rickrollchannel(ctx, channel_id):
    if ctx.author.guild_permissions.manage_messages:
        channel = bot.get_channel(int(channel_id))
        await channel.send("https://tenor.com/view/rickroll-roll-rick-never-gonna-give-you-up-never-gonna-gif-22954713")
        await ctx.respond(f"{channel} has been rickrolled <a:CatDance:976551837224300614>", ephemeral=True)
    else:
        await ctx.respond("You do not have the permissions to use this command")
#math command
@bot.command(name = "math", description = "Do math")
async def math(ctx, *, equation):
        await ctx.respond(f"{eval(equation)}", ephemeral=True)
#iphone gif
@bot.slash_command(name = "iphone", description = "Send an iphone gif")
async def iphone(ctx):
        await ctx.respond("https://tenor.com/view/apple-apple-iphone12-iphone12pro-gif-18835952", ephemeral=True)
#send random tenor gif via api
@bot.slash_command(name = "tenor", description = "Send a random gif from tenor")
async def tenor(ctx):
        r = requests.get("https://api.tenor.com/v1/random?key=LIVDSRZULELA&q=gif&limit=1")
        data = r.json()
        await ctx.respond(f"{data['results'][0]['url']}", ephemeral=True)
@bot.slash_command(name = "github", description = "Send a link to the bot's github")
async def github(ctx):
        await ctx.respond("Github link https://github.com/M4axim/taipixel", ephemeral=True)
#rickroll command
@bot.slash_command(name = "worshipsky", description = "Worship sky")
async def worshipsky(ctx, member: discord.Member):
    if ctx.author.guild_permissions.manage_messages:
        await member.send("https://cdn.discordapp.com/avatars/702473604616421476/a_35cef7f419d30f3434d2dbb4f7fad4a7.gif?size=512 Worship sky <:salute:980553271351603260>")
        await ctx.respond(f"{member} has been worshipied <:salute:980553271351603260>", ephemeral=True)
    else:
        await ctx.respond("You do not have the permissions to use this command")
keep_alive()
token = os.environ['token']
bot.run(token)
