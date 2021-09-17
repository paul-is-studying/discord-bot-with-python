import discord #import the Discord's module
token = "ODg4MzMzNzQzMTMwMDI2MDA1.YURLRA.YLfPbB0AqExDGmloKqVr6yTzgrM" #Get the bot's token to run it.
client = discord.Client() #setup client

@client.event
async def on_ready():
    print("Ready to launch!")
    print(client.user)
    print("=========================")

@client.event
async def on_message(message):
    if message.content == "Hey": #when the user says "hey"
        await message.channel.send("Wut") #then answer with "Wut"
    
    if message.content == "was": #same as above
        await message.channel.send("sup") 



client.run(token)

