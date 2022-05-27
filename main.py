from webbrowser import get
import aiohttp
import discord
import asyncio
from discord.ext import commands
import random
import requests
import youtube_dl
import logging
import datetime
import os 


bot = discord.Bot(debug_guilds=[931093864503201813], command_prefix="!")
discord.Intents.all()
@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")
owner_id = 405356071989936129

@bot.slash_command(name = "hello", description = "Say hello to the bot")
async def hello(ctx):
    await ctx.respond("Hey!")

@bot.slash_command(name = "ban", description = "Ban a user from the server")
async def ban(ctx, member: discord.Member, *, reason = None):
    if ctx.author.guild_permissions.ban_members:
        await member.ban(reason = reason)
        await ctx.respond(f"{member} has been banned", ephemeral=True)
    else:
        await ctx.respond("You do not have the permissions to ban members", ephemeral=True)

@bot.slash_command(name = "kick", description = "Kick a user from the server")
async def kick(ctx, member: discord.Member, *, reason = None):
    if ctx.author.guild_permissions.kick_members:
        await member.kick(reason = reason)
        await ctx.respond(f"{member} has been kicked", ephemeral=True)
    else:
        await ctx.respond("You do not have the permissions to kick members", ephemeral=True)
#discord user info command
@bot.slash_command(name = "userinfo", description = "Gets info about a user")
async def userinfo(ctx, member: discord.Member):
    embed = discord.Embed(title = f"{member}'s info", description = f"{member.mention}", color = 0x00ff00)
    embed.add_field(name = "ID", value = member.id)
    embed.add_field(name = "Nickname", value = member.nick)
    embed.add_field(name = "Joined at", value = member.joined_at)
    embed.add_field(name = "Created at", value = member.created_at)
    embed.add_field(name = "Top role" , value = member.top_role)
    embed.add_field(name = "Bot?", value = member.bot)
    embed.add_field(name = "Last online", value = member.last.seen)
    embed.add_field(name = "Does user have nitro" , value = member.premium_since)
    embed.set_thumbnail(url = member.avatar.url)
    await ctx.respond(embed = embed)
@bot.slash_command(name = "avatar", description = "Gets the avatar of a user")
async def avatar(ctx, member: discord.Member):
    embed = discord.Embed(title = f"{member}'s avatar", description = f"{member.mention}", color = 0x00ff00)
    embed.set_image(url = member.avatar.url)
    await ctx.respond(embed = embed)
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
    await ctx.send(embed = embed)
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
    await ctx.respond(f"**Pong** :ping_pong:{round(bot.latency * 1000)}ms")
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
        await ctx.respond(f"{channel} has been slowed to {amount} seconds")
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
        await ctx.respond(f"{member} has been rickrolled")
    else:
        await ctx.respond("You do not have the permissions to use this command")
#8ball
@bot.slash_command(name = "magicball", description = "Ask the bot a question")
async def eightball(ctx, *, question):
        responses = ["It is certain", "It is decidedly so", "Without a doubt", "Yes, definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]
        await ctx.respond(f"Question: {question}\nAnswer: {random.choice(responses)}")
#ping member
@bot.slash_command(name = "pingmember", description = "Ping a member")
async def pingmember(ctx, member: discord.Member):
    if ctx.author.guild_permissions.manage_messages:
        await ctx.respond(f"{member} has been pinged")
    else:
        await ctx.respond("You do not have the permissions to use this command")
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
#unlock channel with permission and channel id
@bot.slash_command(name = "unlock", description = "Unlock a channel")
async def unlock(ctx, channel_id):
    if ctx.author.guild_permissions.manage_channels:
        channel = bot.get_channel(int(channel_id))
        await channel.edit(reason = "Unlocked by bot", locked = False)
        await ctx.respond(f"{channel} has been unlocked")
    else:
        await ctx.respond("You do not have the permissions to use this command")
#lockdown a server with admin permissions and remove a permissions to type messeges in all channels
@bot.slash_command(name = "lockdown", description = "Lockdown a server")
async def lockdown(ctx):
    if ctx.author.guild_permissions.administrator:
        for channel in ctx.guild.channels:
            await channel.edit(reason = "Locked by bot", locked = True)
        await ctx.respond("Server has been locked")
    else:
        await ctx.respond("You do not have the permissions to use this command")
#create channel which is ticket
@bot.slash_command(name = "ticket", description = "Create a ticket channel")
async def ticket(ctx):
    if ctx.author.guild_permissions.manage_channels:
        await ctx.guild.create_text_channel("ticket", reason = "Created by bot")
        await ctx.respond("Ticket channel has been created")
    else:
        await ctx.respond("You do not have the permissions to use this command")
#dm a user a patreon link
@bot.slash_command(name = "patreon", description = "Send a patreon link to a user")
async def patreon(ctx, member: discord.Member):
    if ctx.author.guild_permissions.manage_messages:
        await member.send("Become a patreon today <https://bit.ly/38d0U9v>")
        await ctx.respond(f"{member} has been sent a patreon link")
    else:
        await ctx.respond("You do not have the permissions to use this command")
#send rickroll in channel with id of channel
@bot.slash_command(name = "rickrollchannel", description = "Rickroll a user in a channel", reason = "Rickroll by bot")
async def rickrollchannel(ctx, channel_id):
    if ctx.author.guild_permissions.manage_messages:
        channel = bot.get_channel(int(channel_id))
        await channel.send("https://cdn.discordapp.com/avatars/702473604616421476/a_35cef7f419d30f3434d2dbb4f7fad4a7.gif?size=1024")
        await ctx.respond(f"{channel} has been rickrolled", ephemeral=True)
    else:
        await ctx.respond("You do not have the permissions to use this command")
#math command
@bot.slash_command(name = "math", description = "Do math")
async def math(ctx, *, equation):
    if ctx.author.guild_permissions.manage_messages:
        await ctx.respond(f"{eval(equation)}", ephemeral=True)
    else:
        await ctx.respond("You do not have the permissions to use this command")
#iphone gif
@bot.slash_command(name = "iphone", description = "Send an iphone gif")
async def iphone(ctx):
    if ctx.author.guild_permissions.manage_messages:
        await ctx.respond("https://tenor.com/view/apple-apple-iphone12-iphone12pro-gif-18835952", ephemeral=True)
    else:
        await ctx.respond("You do not have the permissions to use this command")
#send random tenor gif via api
@bot.slash_command(name = "tenor", description = "Send a random gif from tenor")
async def tenor(ctx):
    if ctx.author.guild_permissions.manage_messages:
        r = requests.get("https://api.tenor.com/v1/random?key=LIVDSRZULELA&q=gif&limit=1")
        data = r.json()
        await ctx.respond(f"{data['results'][0]['url']}")
    else:
        await ctx.respond("You do not have the permissions to use this command")
#disable command wihout cogs
@bot.slash_command(name = "disable", description = "Disable a command")
async def disable(ctx, command):
    if ctx.author.guild_permissions.manage_messages:
        bot.remove_command(command)
        await ctx.respond(f"{command} has been disabled")
    else:
        await ctx.respond("You do not have the permissions to use this command")

bot.run("token") # runthe bot with the token
