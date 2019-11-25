from flask import Flask
from threading import Thread
import discord
from discord.ext import commands
from discord import Game
import random
import os
import json

app = Flask('')

@app.route('/')
def home():
    return "bot active"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():  
    t = Thread(target=run)
    t.start()

description = ''
bot = commands.Bot(command_prefix='/', description=description)
token = "NjQ3ODM3NjA1NTU1MjA4MjEy.Xdlf0g.jACo1KaHnW5A9Hf3Hc-3VuNxNgg"
client = discord.Client()

@bot.event
async def on_ready():
  print('Logged in as')
  print(bot.user.name)
  print(bot.user.id)
  guildno = len(bot.guilds)
  print ("Guilds = "+str(guildno))
  print('------')
  status = ["Roleplaying with reaper"]
  await bot.change_presence(activity=discord.Game(name=status[0]))
  
@bot.command(pass_context=True)
async def roll(ctx):
  '''use to roll dice\nUsage - /roll [number of sides] [number of dice]'''
  guild = ctx.message.guild
  channel = ctx.message.channel
  caller = ctx.message.author.id
  content = ctx.message.content
  content = content.split(" ")
  sides = content[1]
  num = content [2]
  i = 0
  if sides == 1:
    await ctx.send("you need to have a dice with more than 1 side, you can't have a 2d dice")
  else:
    if int(sides) < 1000 and int(num) <1000:
      for x in range(0,int(num)):
        i = int(i)+random.randint(1,int(sides))
      await ctx.send("<@{}> you rolled a {}!".format(caller,i))
    else:
      await ctx.send("<@{}> those numbers are too big!".format(caller))
  

@bot.command(pass_context=True)
async def setdoc(ctx):
  '''Use to create a document - ADMIN ONLY'''
  guild = ctx.message.guild
  channel = ctx.message.channel
  caller = ctx.message.author
  content = ctx.message.content
  content = content.split(" ")
  filename = content[1]
  contain = content[2:]
  if discord.utils.get(ctx.message.guild.roles, name = "Admin")in caller.roles or caller.id == 472444723509067776:
    f = open("docs/{}.txt".format(filename.lower()),"w+")
    text = ""
    for x in contain:
      text = text +" "+ x
    f.write(text)
    f.close()
    await ctx.send("Done!")
  else:
    pass
    
@bot.command(pass_context=True)
async def readdoc(ctx):
  '''Reads a document use /viewdocs to know all the documents there are'''
  guild = ctx.message.guild
  channel = ctx.message.channel
  caller = ctx.message.author.id
  content = ctx.message.content
  content = content.split(" ")
  filename = content[1]
  try:
    f = open("docs/{}.txt".format(filename.lower()),"r")
    await ctx.send(f.read())
    f.close()
  except:
    await ctx.send("oops, i couldn't read that file, its likely it doesn't exist.")

@bot.command(pass_context=True)
async def deletedoc(ctx):
  '''Deletes a document - ADMIN ONLY'''
  guild = ctx.message.guild
  channel = ctx.message.channel
  caller = ctx.message.author
  content = ctx.message.content
  content = content.split(" ")
  filename = content[1]
  if discord.utils.get(ctx.message.guild.roles, name = "Admin")in caller.roles or caller.id == 472444723509067776:
    try:
      os.remove("docs/{}.txt".format(filename.lower()))
      await ctx.send("Done!")
    except:
      await ctx.send("oops, i couldn't delete that file, its likely it doesn't exist.")
  else:
    await ctx.send("oops, you don't seem to have permission to do that.")

@bot.command(pass_context=True)
async def viewdocs(ctx):
  '''Used to view all possible documents\nUsage - /viewdocs'''
  guild = ctx.message.guild
  channel = ctx.message.channel
  caller = ctx.message.author
  content = ctx.message.content
  y = os.listdir("docs")
  z = ""
  for x in y:
    z = z+x[:len(x)-4]+"\n"
  await ctx.send(z)
  
@bot.command(pass_context=True)
async def setname(ctx):
  '''use to set your player name\nUsage - /setname name'''
  guild = ctx.message.guild
  channel = ctx.message.channel
  caller = ctx.message.author.id
  content = ctx.message.content
  content = content[9:]
  try:
    f = open("players/{}.json".format(caller,"r"))
    playerinfo =  json.loads(f.read())
    playerinfo["name"] = content
    f.close()
    f = open("players/{}.json".format(caller),"w")
    json.dump(playerinfo,f)
    f.close()
    await ctx.send("Done!")
  except:
    await ctx.send("oops, it looks like you don't have a profile yet use /setup to create one then come and set your values")

@bot.command(pass_context=True)
async def setbio(ctx):
  '''use to set your player bio\nUsage - /setbio bio'''
  guild = ctx.message.guild
  channel = ctx.message.channel
  caller = ctx.message.author.id
  content = ctx.message.content
  content = content[7:]
  try:
    f = open("players/{}.json".format(caller,"r"))
    playerinfo =  json.loads(f.read())
    playerinfo["bio"] = content
    f.close()
    f = open("players/{}.json".format(caller),"w")
    json.dump(playerinfo,f)
    f.close()
    await ctx.send("Done!")
  except:
    await ctx.send("oops, it looks like you don't have a profile yet use /setup to create one then come and set your values")

@bot.command(pass_context=True)
async def setage(ctx):
  '''use to set your player age\nUsage - /setage age'''
  guild = ctx.message.guild
  channel = ctx.message.channel
  caller = ctx.message.author.id
  content = ctx.message.content
  content = content[7:]
  try:
    f = open("players/{}.json".format(caller,"r"))
    playerinfo =  json.loads(f.read())
    playerinfo["age"] = content
    f.close()
    f = open("players/{}.json".format(caller),"w")
    json.dump(playerinfo,f)
    f.close()
    await ctx.send("Done!")
  except:
    await ctx.send("oops, it looks like you don't have a profile yet use /setup to create one then come and set your values")

@bot.command(pass_context=True)
async def setsexuality(ctx):
  '''use to set your player sexuality\nUsage - /setsexuality sexuality'''
  guild = ctx.message.guild
  channel = ctx.message.channel
  caller = ctx.message.author.id
  content = ctx.message.content
  content = content[13:]
  try:
    f = open("players/{}.json".format(caller,"r"))
    playerinfo =  json.loads(f.read())
    playerinfo["sexuality"] = content
    f.close()
    f = open("players/{}.json".format(caller),"w")
    json.dump(playerinfo,f)
    f.close()
    await ctx.send("Done!")
  except:
    await ctx.send("oops, it looks like you don't have a profile yet use /setup to create one then come and set your values")

@bot.command(pass_context=True)
async def setappearance(ctx):
  '''use to set your player appearance\nUsage - /setappearance appearance'''
  guild = ctx.message.guild
  channel = ctx.message.channel
  caller = ctx.message.author.id
  content = ctx.message.content
  content = content[14:]
  try:
    f = open("players/{}.json".format(caller,"r"))
    playerinfo =  json.loads(f.read())
    playerinfo["appearance"] = content
    f.close()
    f = open("players/{}.json".format(caller),"w")
    json.dump(playerinfo,f)
    f.close()
    await ctx.send("Done!")
  except:
    await ctx.send("oops, it looks like you don't have a profile yet use /setup to create one then come and set your values")

@bot.command(pass_context=True)
async def setgender(ctx):
  '''use to set your player gender\nUsage - /setgender gender'''
  guild = ctx.message.guild
  channel = ctx.message.channel
  caller = ctx.message.author.id
  content = ctx.message.content
  content = content[10:]
  try:
    f = open("players/{}.json".format(caller,"r"))
    playerinfo =  json.loads(f.read())
    playerinfo["gender"] = content
    f.close()
    f = open("players/{}.json".format(caller),"w")
    json.dump(playerinfo,f)
    f.close()
    await ctx.send("Done!")
  except:
    await ctx.send("oops, it looks like you don't have a profile yet use /setup to create one then come and set your values")

@bot.command(pass_context=True)
async def setclass(ctx):
  '''ADMIN ONLY\nUsage - /setclass userid class'''
  guild = ctx.message.guild
  channel = ctx.message.channel
  caller = ctx.message.author
  content = ctx.message.content
  content = content.split(" ")
  if discord.utils.get(ctx.message.guild.roles, name = "Admin")in caller.roles or caller.id == 472444723509067776:
    y = ""
    i = 2
    for x in range(2,len(content)):
      y = y +" "+content[i]
      i = i+1
    try:
      f = open("players/{}.json".format(content[1]),"r")
      playerinfo =  json.loads(f.read())
      playerinfo["class"] = y
      f.close()
      f = open("players/{}.json".format(content[1]),"w")
      json.dump(playerinfo,f)
      f.close()
      await ctx.send("Done!")
    except:
      await ctx.send("oops, it looks like you don't have a profile yet use /setup to create one then come and set your values")

@bot.command(pass_context=True)
async def setrace(ctx):
  '''ADMIN ONLY\nUsage - /setrace userid race'''
  guild = ctx.message.guild
  channel = ctx.message.channel
  caller = ctx.message.author
  content = ctx.message.content
  content = content.split(" ")
  if discord.utils.get(ctx.message.guild.roles, name = "Admin")in caller.roles or caller.id == 472444723509067776:
    y = ""
    i = 2
    for x in range(2,len(content)):
      y = y +" "+content[i]
      i = i+1
    try:
      f = open("players/{}.json".format(content[1]),"r")
      playerinfo =  json.loads(f.read())
      playerinfo["race"] = y
      f.close()
      f = open("players/{}.json".format(content[1]),"w")
      json.dump(playerinfo,f)
      f.close()
      await ctx.send("Done!")
    except:
      await ctx.send("no profile found")


@bot.command(pass_context=True)
async def setitems(ctx):
  '''ADMIN ONLY\nUsage - /setclass userid items\nWARNING - will overwrite current items'''
  guild = ctx.message.guild
  channel = ctx.message.channel
  caller = ctx.message.author
  content = ctx.message.content
  content = content.split(" ")
  if discord.utils.get(ctx.message.guild.roles, name = "Admin")in caller.roles or caller.id == 472444723509067776:
    y = ""
    i = 2
    for x in range(2,len(content)):
      y = y +" "+content[i]
      i = i+1
    try:
      f = open("players/{}.json".format(content[1]),"r")
      playerinfo =  json.loads(f.read())
      playerinfo["items"] = y
      f.close()
      f = open("players/{}.json".format(content[1]),"w")
      json.dump(playerinfo,f)
      f.close()
      await ctx.send("Done!")
      
    except:
      await ctx.send("no profile found")

@bot.command(pass_context=True)
async def setcompanions(ctx):
  '''ADMIN ONLY\nUsage - /setcompanions userid companions\nWARNING - will overwrite current companions'''
  guild = ctx.message.guild
  channel = ctx.message.channel
  caller = ctx.message.author
  content = ctx.message.content
  content = content.split(" ")
  if discord.utils.get(ctx.message.guild.roles, name = "Admin")in caller.roles or caller.id == 472444723509067776:
    y = ""
    i = 2
    for x in range(2,len(content)):
      y = y +" "+content[i]
      i = i+1
    try:
      f = open("players/{}.json".format(content[1]),"r")
      playerinfo =  json.loads(f.read())
      playerinfo["companions"] = y
      f.close()
      f = open("players/{}.json".format(content[1]),"w")
      json.dump(playerinfo,f)
      f.close()
      await ctx.send("Done!")
    except:
      await ctx.send("no profile found")

@bot.command(pass_context=True)
async def setskills(ctx):
  '''ADMIN ONLY\nUsage - /setskills userid skills\nWARNING - will overwrite current skills'''
  guild = ctx.message.guild
  channel = ctx.message.channel
  caller = ctx.message.author
  content = ctx.message.content
  content = content.split(" ")
  if discord.utils.get(ctx.message.guild.roles, name = "Admin")in caller.roles or caller.id == 472444723509067776:
    y = ""
    i = 2
    for x in range(2,len(content)):
      y = y +" "+content[i]
      i = i+1
    #try:
    f = open("players/{}.json".format(content[1]),"r")
    playerinfo =  json.loads(f.read())
    playerinfo["skills"] = y
    f.close()
    f = open("players/{}.json".format(content[1]),"w")
    json.dump(playerinfo,f)
    f.close()
    await ctx.send("Done!")
    #except:
      #await ctx.send("no profile found")

@bot.command(pass_context=True)
async def delacc(ctx):
  '''ADMIN ONLY\nUsage - /delacc userid \nWARNING - IRREVERSIBLE!!!'''
  guild = ctx.message.guild
  channel = ctx.message.channel
  caller = ctx.message.author
  content = ctx.message.content
  content = content.split(" ")
  if discord.utils.get(ctx.message.guild.roles, name = "Admin")in caller.roles or caller.id == 472444723509067776:
    try:
      os.remove("players/{}.json".format(content[1]))
      await ctx.send("Done!")
    except:
      await ctx.send("no profile found")

@bot.command(pass_context=True)
async def profile(ctx):
  '''view your profile'''
  caller = ctx.message.author
  content = ctx.message.content.split(" ")
  content = content[1]
  #try:  
  f = open("players/{}.json".format(content.strip("<@").strip(">")),"r")
  jc = f.read()
  playerinfo =  json.loads(jc)
  print(playerinfo)
  f.close()
  e = discord.Embed(title="<@{}>'s profile".format(content.strip("<@").strip(">")),colour=0xffffff)
  e.add_field(name = "name:",value=playerinfo["name"]+".",inline=False)
  e.add_field(name = "race:",value=playerinfo["race"]+".",inline=False)
  e.add_field(name = "class:",value=playerinfo["class"]+".",inline=False)
  e.add_field(name = "gender:",value=playerinfo["gender"]+".",inline=False)
  e.add_field(name = "age:",value=playerinfo["age"]+".",inline=False)
  e.add_field(name = "sexuality:",value=playerinfo["sexuality"]+".",inline=False)
  e.add_field(name = "appearance:",value=playerinfo["appearance"]+".",inline=False)
  e.add_field(name = "bio:",value=playerinfo["bio"]+".",inline=False)
  e.add_field(name = "skills:",value=playerinfo["skills"]+".",inline=False)
  e.add_field(name = "items:",value=playerinfo["items"]+".",inline=False)
  e.add_field(name = "stats:",value=playerinfo["stats"]+".",inline=False)
  e.add_field(name = "companions:",value=playerinfo["companions"]+".",inline=False)
  await ctx.send(embed=e)
  
  
  #except:
  #  await ctx.send("no profile found")

@bot.command(pass_context=True)
async def setup(ctx):
  '''Use this to set up your profile for the first time'''
  guild = ctx.message.guild
  channel = ctx.message.channel
  caller = ctx.message.author.id
  content = ctx.message.content
  try:
    f=open("players/{}.json".format(caller),"r")
    f.close()
    await ctx.send("It looks like you already have an account")
  except:
    playerinfo = {
      "name" : "",
      "race" : "",
      "class": "",
      "gender" : "",
      "age" : "",
      "sexuality" : "",
      "appearance" : "",
      "bio" : "",
      "skills" : "",
      "items" : "",
      "stats":"",
      "companions": ""
    }
    f = open("players/{}.json".format(caller),"w+")
    json.dump(playerinfo, f)
    f.close()
    await ctx.send("Done!")

@bot.command(pass_context=True)
async def setstats(ctx):
  '''ADMIN ONLY\nUsage - /setstats userid stats\nWARNING - will overwrite current skills'''
  guild = ctx.message.guild
  channel = ctx.message.channel
  caller = ctx.message.author
  content = ctx.message.content
  content = content.split(" ")
  if discord.utils.get(ctx.message.guild.roles, name = "Admin")in caller.roles or caller.id == 472444723509067776:
    y = ""
    i = 2
    for x in range(2,len(content)):
      y = y +" "+content[i]
      i = i+1
    try:
      f = open("players/{}.json".format(content[1]),"r")
      playerinfo =  json.loads(f.read())
      playerinfo["stats"] = y
      f.close()
      f = open("players/{}.json".format(content[1]),"w")
      json.dump(playerinfo,f)
      f.close()
      await ctx.send("Done!")
    except:
      await ctx.send("no profile found")


keep_alive()
bot.run(token)
