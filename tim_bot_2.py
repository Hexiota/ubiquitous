import discord
import random
import asyncio
import os
from discord import FFmpegPCMAudio
from discord.ext import commands
from discord.utils import get
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')


bot = commands.Bot(command_prefix='PEEPEE POOPOO ')


@bot.event
async def on_ready():
    print('Bot is ready.')


@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
    else:
        await ctx.send("I am not in a voice channel.")


@bot.command()
async def join(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()


@bot.event
async def on_message(message):
    if 'frog' in message.content.lower():
        await message.channel.send(f"<@{277318719066210304}>")
        await message.add_reaction('\U0001F438')

    if message.author.id == 96375227365232640 and 'husband' in message.content.lower():
        await message.add_reaction('\U0001F621')
        await message.channel.send(f'''Actually, he did. He bought this for me on our ten-year anniversary. Not only is he my lover, he's my best friend and my soulmate. I'm not ashamed of who I love, nor should I be. For someone with strange abilities due to, I assume, accidental exposure to radioactive spider-blood, you're not very tolerant of those different to yourself. You're on the wrong side of history, Spider-Man.''')

    if 'corn' and 'dog' in message.content:
        await message.add_reaction('\U0001F33D')
        await message.add_reaction('\U0001F415')

    if 'daniel' in message.content:
        await message.add_reaction('\U0001F528')
        await message.channel.send(f'''[Intro]
Na na-na-nah
Na-na,na nana nana
Na na na na nah, nah

[Verse 1]
White bed now red, that Minecraft dye
Sleeping, you're right outside my house
Creepers, outside and they'll explode
Think you're invisible
Arrows on both my knees from you
Don't say cuss words like 'frick'
I mine what I want when I'm wanting to
My sword has sharpness II

[Chorus]
So you're a griefer
Like to steal my ores guy
Like to grief my house guy
Chest is always missing ores
I'm that bad player
Make Minecrafter sad type
Make your Alex play MC
Might just take your E-chest
I'm a griefer
(You're banned!)
[Post-Chorus]
I'm a griefer

[Verse 2]
I like it when you play Minecraft
Even if you know that you don't follow rules
I'll let you play Minecraft
I'll be your player too
My Alex likes to mine diamonds with me
But she won't mine this iron
If she looks inside of my chest she'll think
That I'm a noob

[Chorus]
So you're a griefer
Like to steal my ores guy
Like to grief my house guy
Chest is always missing ores
I'm that bad player
Make Minecrafter sad type
Make your Alex play MC
Might just take your E-chest
I'm a griefer
(You're banned!)

[Post-Chorus]
I'm a griefer
(You're banned!)
[Outro]
I'm only good at griefing Steves!
Griefing''')

    if 'bee' in message.content.lower():
        await message.add_reaction('\U0001F41D')

    if 'based' in message.content.lower():
        await message.add_reaction('\U0001F621')
        await message.channel.send(f"Based? Based on what? In your dick? Please shut the fuck up and use words properly you fuckin troglodyte, "
                                   f"do you think God gave us a freedom of speech just to spew random words that have no meaning that doesn't even correllate to the topic of the conversation? "
                                   f"Like please you always complain about why no one talks to you or no one expresses their opinions on you because you're always spewing random shit like poggers based cringe and when you try to explain what it is and you just say that it's funny like what? "
                                   f"What the fuck is funny about that do you think you'll just become a stand-up comedian that will get a standing ovation just because you said \"cum\" in the stage? HELL NO YOU FUCKIN IDIOT, so please shut the fuck up and use words properly you dumb bitch")

    await bot.process_commands(message)


@bot.command()
async def beemovie(ctx):
    await ctx.channel.purge(limit=1)
    with open('bee_movie.txt') as file_object:
        for line in file_object.readlines():
            print(line)
            await ctx.send(line)
            await asyncio.sleep(3.5)
            await ctx.channel.purge(limit=1)


@bot.command()
async def monkas(ctx):
    jerma_monkas = ['monkas_1.wav',
                    'monkas_2.wav',
                    'monkas_3.wav',
                    'monkas_4.wav',
                    'monkas_5.wav',
                    'monkas_6.wav',
                    'monkas_7.wav',
                    'monkas_8.wav',
                    'monkas_10.wav',
                    'monkas_11.wav',
                    'monkas_12.wav',
                    'monkas_13.wav',
                    'monkas_14.wav',
                    'monkas_15.wav',
                    'monkas_16.wav',
                    'monkas_17.wav',
                    'monkas_18.wav',
                    'monkas_19.wav',
                    'monkas_20.wav',
                    'monkas_21.wav']
    if ctx.author.voice:
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio(random.choice(jerma_monkas))
        player = voice.play(source)
        await asyncio.sleep(4)
        await ctx.voice_client.disconnect()
    else:
        await ctx.send("I am not in a voice channel!")


@bot.event
async def on_voice_state_update(member, before, after):
    bald = 'bald.wav'
    if not before.channel and after.channel and member.id == 199027714525626368:

        channel = after.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio(bald)
        player = voice.play(source)
        await asyncio.sleep(7.5)
        await voice.disconnect()


@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')


@bot.command(aliases=['8ball', 'eightball'])
async def _8ball(ctx, *, question):
    responses = ["It is certain.",
                 "It is decidedly so.",
                 "Without a doubt.",
                 "Yes - definitely.",
                 "You may rely on it.",
                 "As I see it, yes.",
                 "Most likely.",
                 "Outlook good.",
                 "Yes.",
                 "Signs point to yes.",
                 "Reply hazy, try again.",
                 "Ask again later.",
                 "Better not tell you now.",
                 "Cannot predict now.",
                 "Concentrate and ask again.",
                 "Don't count on it.",
                 "My reply is no.",
                 "My sources say no.",
                 "Outlook not so good.",
                 "Very doubtful."]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


@bot.command()
async def becca(ctx):
    becca_messages = ['ginklopincan, portokolipsis', 'A mystery']
    await ctx.send(f'{random.choice(becca_messages)}')


@bot.command()
async def brady(ctx):
    await ctx.send(f'Fuck you, Brady')


@bot.command()
async def cody(ctx):
    await ctx.send(f"' Bald")


@bot.command()
async def sus(ctx):
    await ctx.send(f"https://static.wikia.nocookie.net/jerma-lore/images/e/e3/JermaSus.jpg/revision/latest?cb=20201206225609")


@bot.command()
async def smallsus(ctx):
    await ctx.send(f"https://ih1.redbubble.net/image.2801557322.6474/flat,128x128,075,t-pad,128x128,f8f8f8.jpg")


@bot.command(aliases=['rockesmeller', 'fartmouth'])
async def DaylightisfadingawaynightsilhouettesintheskyLEDlightsareflashingontowersItsManhattansmagicaltimeBallerinasdancingtheSwanLakeOnarivermadeofdiamondsandpearlsEverythingsalittlebitweirdnowBecausetonightitisshowtimeInthemiddleofthestreetlifeAllwecelebratearegoodtimesBecausetonightitisshowtimeComeandwalkwithme1273downtheRockefellerstreetLifeismarchinondoyoufeelthat1273downtheRockefellerstreetEverythingismorethansurrealAlrightalrightalrightLetsgoletsgoOldschoolHollywoodstarsPartycinderellasarehereTheymovelikecomputergameheroesBecausetheyknowitisshowtimeInthemiddleofthestreetlifeAlltheycelebratearegoodtimesBecausetonightitisshowtimeSoletskeepmovinon1273downtheRockefellerstreetLifeismarchinondoyoufeelthat1273downtheRockefellerstreetEverythingismorethansurrealSoletskeepmovinonKeepmovinkeepmovinkeepmovinkeepmovinIfyouwanttoknowwhatRockefellergrooveisKeepmovinkeepmovinkeepmovinkeepmovinTimeisrighttocelebrategoodtimesKeepmovinkeepmovinkeepmovinkeepmovinIfyouwanttoknowwhatRockefellergrooveisKeepmovinkeepmovinkeepmovinkeepmovinTimeisrighttocelebratethegoodtimes1273downtheRockefellerstreetLifeismarchinondoyoufeelthat1273downtheRockefellerstreetEverythingismorethansurrealSoletskeepmovinonKeepmovinkeepmovinkeepmovinkeepmovinIfyouwanttoknowwhatRockefellergrooveisKeepmovinkeepmovinkeepmovinkeepmovinTimeisrighttocelebratethegoodtimesWeresinging1273downtheRockefellerstreetLifeismarchinondoyoufeelthatWeresinging1273downtheRockefellerstreetEverythingismorethansurreal(ctx):
    rockefeller = 'rockefeller.wav'
    if ctx.author.voice:
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio(rockefeller)
        player = voice.play(source)


@bot.command()
async def rockespeeder(ctx):
    song = 'rockespeeder.wav'
    if ctx.author.voice:
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio(song)
        player = voice.play(source)


bot.run(TOKEN)

