import discord #import the Discord's module
client = discord.Client() #setup client

f = open("token.txt", 'r')
token = f.read()
f.close()


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

    if message.content.startswith('!embed'):
        embedVar = discord.Embed(title="A Wild EMBED has appeared.", description="Simple description", color=0x7289da)
        embedVar.add_field(name="Field1", value="hi", inline=False)
        embedVar.add_field(name="Field2", value="hi2", inline=False)
        await message.channel.send(embed=embedVar)

    if message.content == "!anotherembed":
        embed = discord.Embed(
            title = "A Wild EMBED has appeared.",
            description = "Another Simple Description",
            color = 0x7289da
        )

        embed.set_footer(text="Simple Footer.")
        embed.set_image(url="https://cdn.discordapp.com/avatars/627292715956043785/f72916a9f5c728c0f69cba48a6a63488.webp?size=1024")
        embed.set_thumbnail(url="https://cdn.discordapp.com/icons/645137556777992203/81dad01e48347b548e6f4530c1a0c3ef.webp?size=1024")
        embed.set_author(name="Author Name", icon_url="https://cdn.discordapp.com/avatars/627292715956043785/f72916a9f5c728c0f69cba48a6a63488.webp?size=1024")
        embed.add_field(name="Field Name", value="Field Value", inline=False)
        embed.add_field(name="Inline Field_1", value="A simple field value for inline embed", inline=True)
        embed.add_field(name="Inline Field_2", value="Another simple field value for another inline embed", inline=True)

        await message.channel.send(embed=embed)

client.run(token)

