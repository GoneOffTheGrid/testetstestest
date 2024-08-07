import discord
import random
import asyncio
import requests
from discord.ext import commands

intents = discord.Intents.default()
intents.typing = True
intents.presences = True
intents.messages = True
intents.reactions = True

client = commands.Bot(command_prefix='-', self_bot=True, intents=intents)

reacting = False           ## DONT CHANGE ANY OF THIS
custom_emoji = None        ## DONT CHANGE ANY OF THIS
afk_message = ""           ## DONT CHANGE ANY OF THIS
afk_active = False         ## DONT CHANGE ANY OF THIS
bigtext_enabled = False    ## DONT CHANGE ANY OF THIS
generate_names = False     ## DONT CHANGE ANY OF THIS
link_enabled = False       ## DONT CHANGE ANY OF THIS
continuous_send = False    ## DONT CHANGE ANY OF THIS
ratelimited = False        ## DONT CHANGE ANY OF THIS
speed = 0.2                ## DONT CHANGE ANY OF THIS
server_link = ""           ## DONT CHANGE ANY OF THIS
counter_running = False    ## DONT CHANGE ANY OF THIS
counter_message = ""       ## DONT CHANGE ANY OF THIS
autorespond_settings = {}  ## DONT CHANGE ANY OF THIS
mocking_enabled = False    ## DONT CHANGE ANY OF THIS
mock_target = None         ## DONT CHANGE ANY OF THIS
mock_text = ""             ## DONT CHANGE ANY OF THIS
continue_handler = True    ## DONT CHANGE ANY OF THIS
is_rated = False           ## DONT CHANGE ANY OF THIS
target_user_id = None      ## DONT CHANGE ANY OF THIS
mock_text = None           ## DONT CHANGE ANY OF THIS
mimic_enabled = False      ## DONT CHANGE ANY OF THIS
mimic_target = None        ## DONT CHANGE ANY OF THIS
spam_message = None        ## DONT CHANGE ANY OF THIS
spam_channel = None        ## DONT CHANGE ANY OF THIS

words_file_path = 'words.txt' ## ig u can change it to smth else but then youd have to fw the code aswell js leave it as ts pls
spamming = False
outlast_enabled = False
count2 = 0

@client.event
async def on_ready():
    print(f'selfbot connected to {client.user.name}')

async def handle_rate_limit(channel):
    global is_rated

@client.event
async def on_message(message):
    global reacting, custom_emoji, afk_message, afk_active, bigtext_enabled, generate_names, link_enabled, server_link, counter_running, counter_message, spamming, generate_names, mocking_enabled, mock_target, mock_text, continue_handler, is_rated, target_user_id, mock_text, mimic_enabled, mimic_target, spam_message, spam_channel, outlast_enabled

    if message.content == '.cmds' and message.author == client.user:
        misc_list = [
            'command : the command symbol is -, add - before any commands e.g -info',
            'info : Nigger selfbot info',
            'stop : stop a client info',
            'cat : cat.',
            'anime : kawaii',
            'animeN : not so kawaii...',
            'ip @user : totally real discord id to ip 100% works btw',
            'react enable : auto reaction',
            'emoji <any emoji> : custom emoji you want the auto reaction set on',
            'react disable : stops auto reaction',
            'stream <text> : streams whatever the text is',
            'av @user : gets someone\'s profile picture',
            'afk <afk text>: sends an autoresponse message when pinged or replied to (only works in dms or groupchats), just say -afk to turn off',
            'purge <number> : purges a specific number of messages',
            'bigtext : auto big text',
            'link <https:// >: auto link text , link must start with https:// , can be any link',
            'counter <counter text> : counter, can be used as afk check',
        ]
        chatpacking_list = [
            'gc <name> : changes the group chat name',
            'chp <@user> : autopress with a counter, needs a words.txt of sentences or words which will be sent - dm for my config',
            'ar <@user> : autoresponder, can be ANY text.',
            'mock <@user> <mock_text> : mocks someone',
            'mimic <@user> : mimics someone',
            'spam : basic spam',
            'outlast : outlast text with delay + counter',
        ]
        response = '```ini\n[- Nigger bot misc commands :]\n{}```'.format('\n'.join(misc_list))
        await message.channel.send(response)

        response = '```ini\n[- Nigger bot chatpack commands :]\n{}```'.format('\n'.join(chatpacking_list))
        await message.channel.send(response)
        return

    if message.content == '-info' and message.author == client.user:
        bot_info = ('Nigger bot information: This bot is specifically made for chatpacking and general stuff like rpc and auto react. ')
        response = '```' + bot_info + '```'
        await message.channel.send(response)
        return

    if message.content == '-stop' and message.author == client.user:
        stop_info = ('To stop a specific command, just type the command followed by "stop". For example "counterstop" ')



        response = '```' + stop_info + '```'
        await message.channel.send(response)
        return

##---------------------------------------------------------------------misc-----------------------------------------------------------------------------------

## -purge

    if message.content.startswith('-purge') and message.author == client.user:
        args = message.content.split()
        if len(args) == 2:
            try:
                limit = int(args[1]) + 1
                if isinstance(message.channel, discord.TextChannel) or isinstance(message.channel, discord.GroupChannel):
                    if isinstance(message.channel, discord.TextChannel):
                        deleted = await message.channel.purge(limit=limit, check=lambda msg: msg.author == client.user)
                        await message.channel.send(f"Deleted {len(deleted)} messages.", delete_after=5)
                    else:  # For group channels
                        async for msg in message.channel.history(limit=limit):
                            if msg.author == client.user:
                                await msg.delete()
                        await message.channel.send(f"Deleted **{limit - 1}** messages.", delete_after=2)
                elif isinstance(message.channel, discord.DMChannel):
                    async for msg in message.channel.history(limit=limit):
                        if msg.author == client.user:
                            await msg.delete()
                    await message.channel.send(f"Deleted **{limit - 1}** messages.", delete_after=2)
            except ValueError:
                await message.channel.send("Please provide a valid number of messages to delete.")
        return


## -cat

    if message.content == '-cat' and message.author == client.user:
         response = requests.get('https://api.thecatapi.com/v1/images/search')
         data = response.json()
         cat_image_url = data[0]['url']
         await message.channel.send(cat_image_url)
         return
    
## -anime

    if message.content == '-anime' and message.author == client.user:
         response2 = requests.get('https://api.waifu.pics/sfw/waifu')
         data = response2.json()
         waifu_image_url = data['url']
         await message.channel.send(waifu_image_url)
         return
    
## -animeN

    if message.content == '-animeN' and message.author == client.user:
         response3 = requests.get('https://api.waifu.pics/nsfw/waifu')
         data = response3.json()
         anime_image_url = data['url']
         await message.channel.send(anime_image_url)
         return

## -react enable , -emoji , -react disable

    if message.author == client.user:
        parts = message.content.split()
        if len(parts) >= 2 and parts[0] == '-react':
            if parts[1].lower() == 'enable':
                reacting = True
                await message.channel.send("Reactions are now **enabled**")
                await message.delete()
            elif parts[1].lower() == 'disable':
                reacting = False
                await message.add_reaction('✅')
                await message.delete()
            else:
                await message.channel.send("Invalid command. For auto reaction, use `-react enable` or `-react disable`.")
                await message.add_reaction('❌')
        elif len(parts) >= 2 and parts[0] == '-emoji':
            custom_emoji = parts[1]
            await message.channel.send(f"**Auto-react emoji set to:** {custom_emoji}")
            await message.delete()

    if reacting and message.author == client.user:
        if custom_emoji is not None:
            await message.add_reaction(custom_emoji)
        else:
            await message.add_reaction('👍')

## -stream

    if message.content.lower() == '-streamstop':
        if message.author == client.user:
            await client.change_presence(activity=None)
            await message.channel.send("Streaming status has been stopped.")
            await message.delete()

    elif message.content.startswith('-stream'):
        if message.author == client.user:
            new_status = message.content[8:].strip()
            if new_status:
                await client.change_presence(activity=discord.Streaming(name=new_status, url='https://www.twitch.tv/owobotplays'))  # add any yt or twitch link
                await message.channel.send(f"Streaming status changed to: **{new_status}**")
                await message.delete()
            else:
                await message.channel.send("Please provide a status message.")
                await message.delete()
                return


## -av

    if message.content.startswith('-av'):
        if message.author == client.user:
            if message.mentions:
                user = message.mentions[0]
                avatar_url = user.avatar_url
                await message.channel.send(avatar_url)
                await message.delete()
            else:
                await message.channel.send("Please mention a user.")
                await message.delete()

## -afk , -afkstop

    if message.content.startswith('-afk') and message.author == client.user:
        afk_command = message.content.split(' ', 1)
        if len(afk_command) > 1:
            afk_message = afk_command[1]
            afk_active = True
            await message.delete()
            confirmation_msg = await message.channel.send(f'**AFK message set to: {afk_message}**')
            await asyncio.sleep(1)
            await confirmation_msg.delete()
            return

    if afk_active:
        if client.user.mentioned_in(message) or (message.reference and message.reference.cached_message and message.reference.cached_message.author == client.user):
            if isinstance(message.channel, discord.DMChannel) or isinstance(message.channel, discord.GroupChannel):
                await message.reply(afk_message)

    if message.content.strip() == '-afkstop' and message.author == client.user:
        afk_active = False
        await message.delete()
        confirmation_msg = await message.channel.send("AFK message deactivated")
        await asyncio.sleep(1)
        await confirmation_msg.delete()

## -bigtext, -bigtextstop

    if message.content == '-bigtext' and message.author == client.user:
        bigtext_enabled = True
        await message.delete()
        confirmation_msg = await message.channel.send("bigtext is on")
        await asyncio.sleep(1)
        await confirmation_msg.delete()
        return

    if message.content == '-bigtextstop' and message.author == client.user:
        bigtext_enabled = False
        await message.delete()
        confirmation_msg = await message.channel.send("**bigtext is off**")
        await asyncio.sleep(1)
        await confirmation_msg.delete()
        return

    if bigtext_enabled:
        await message.edit(content=f"# {message.content}")

## -link , -linkstop

    if link_enabled:
        await message.edit(content=f"[{message.content}]({server_link})")

    if message.content.startswith('-link') and message.author == client.user:
        link_enabled = True
        server_link = message.content.split('-link ')[-1]
        confirmation_msg = await message.channel.send("**link text is on**")
        await asyncio.sleep(1)
        await confirmation_msg.delete()
        await message.delete()
        return

    if message.content.startswith('-linkstop') and message.author == client.user:
        link_enabled = False
        await message.delete()

## -counter , -counterstop

    if message.content.startswith('-counter') and not counter_running and message.author == client.user:
        counter_running = True
        counter_message = message.content[len('-counter '):].strip()

        for i in range(999999999999999):
            if not counter_running:
                break
            await asyncio.sleep(0.8)
            await message.channel.send(f"{counter_message} {i}")
        
        if counter_running:
            confirmation_msg = await message.channel.send("**counter is off**")
            await asyncio.sleep(1)
            await confirmation_msg.delete()
            counter_running = False
        return
    
    if message.content.startswith('-counterstop') and counter_running and message.author == client.user:
        counter_running = False
        confirmation_msg = await message.channel.send("**counter is off**")
        await asyncio.sleep(1)
        await confirmation_msg.delete()
        return

##---------------------------------------------------------------------chatpack-----------------------------------------------------------------------------------

## -gc , -gcstop

    if message.content.startswith('-gc') and message.author.name == "illegibly" and not generate_names:
        generate_names = True
        counter = 1
        while generate_names:
            new_name = f"{message.content[4:]} {counter}"
            try:
                await message.channel.edit(name=new_name)
                counter += 1
                await asyncio.sleep(1.42)
                if counter % 100 == 0:
                    await asyncio.sleep(1.5)
                if counter % 200 == 0:
                    await asyncio.sleep(1.6)
            except discord.HTTPException as e:
                if e.status == 429: 
                    retry_after = e.retry_after
                    print(f"Rate limit hit. Retrying after {retry_after} seconds.")
                    await asyncio.sleep(retry_after)

    if message.author.name == "illegibly" and message.content.lower() == "-gcstop":
        generate_names = False
        return
    
## -chp , -chpstop

    if message.author == client.user and message.content.lower() == "-chpstop":
        confirmation_msg = await message.channel.send("**auto press stopped**")
        await asyncio.sleep(1.5)
        await confirmation_msg.delete()
        spamming = False
        return

    if message.content.startswith('-chp') and message.author == client.user:
        if not message.mentions:
            await message.channel.send("Please mention a user to ping.")
            return
        
        target_user_id = message.mentions[0].id
        count = 0
        spamming = True
        
        with open(words_file_path, 'r') as words_file:
            words = words_file.read().splitlines()

        while spamming:
            random_word = random.choice(words)
            try:
                count += 1
                await message.channel.send(content=f"<@{target_user_id}> {random_word} ``{count}``")
            except discord.errors.HTTPException as e:
                print(f"Rate limited: {e}")
                if e.status == 429:
                    retry_after = e.response.headers.get('Retry-After')
                    await handle_rate_limit(message.channel)
            await asyncio.sleep(0.04) 

## -ar , -arstop

    if message.content.startswith('-ar ') and message.author == client.user:
        try:
            parts = message.content.split(' ', 2)
            user_mention = parts[1]
            response_text = parts[2]

            user_id = int(user_mention[3:-1]) if user_mention.startswith('<@!') else int(user_mention[2:-1])

            autorespond_settings[user_id] = response_text
            await message.channel.send(f'auto response set to {user_mention}')
        
        except Exception as e:
            await message.channel.send('Invalid command usage. Correct format: -ar @user [the text wanted to autorespond with]')

    elif message.content.startswith('-arstop') and message.author == client.user:
        try:
            parts = message.content.split(' ', 1)
            user_mention = parts[1]
            user_id = int(user_mention[3:-1]) if user_mention.startswith('<@!') else int(user_mention[2:-1])

            if user_id in autorespond_settings:
                del autorespond_settings[user_id]
                await message.channel.send(f'auto response stopped for {user_mention}')
            else:
                await message.channel.send(f'there is no auto response set for {user_mention}')
        
        except Exception as e:
            await message.channel.send('Invalid command, correct format: -arstop @user')

    if message.author.id in autorespond_settings:
        await message.channel.send(autorespond_settings[message.author.id])
        return

## -mock , -mockstop

    if message.author == client.user and message.content.lower() == "-mockstop":
        target_user_id = None
        mock_text = ""
        mocking_enabled = False
        confirmation_msg = await message.channel.send('Mocking stopped')
        await asyncio.sleep(1)
        await confirmation_msg.delete()

    if message.content.startswith('-mock') and message.author == client.user:
        mocking_enabled = True
        command = message.content.split(' ')
        if len(command) >= 4:
            if command[1].startswith('<@') and command[1].endswith('>'):
                target_user_id = command[1][2:-1]
                mock_text = ' '.join(command[2:])
                confirmation_msg = await message.channel.send(f'mock set to **{target_user_id}**')
                await asyncio.sleep(1)
                await confirmation_msg.delete()
        elif message.content.lower() != "-mockstop" and message.author == client.user:  
            confirmation_msg2 = await message.channel.send('Wrong command use. Correct format: -mock @user [mock text]')
            await asyncio.sleep(1)
            await confirmation_msg2.delete()
            return

    if mocking_enabled and target_user_id and message.author.id == int(target_user_id) and not is_rated:
        try:
            await message.channel.send(content=f'"{message.content}" {mock_text}')
        except discord.errors.HTTPException as e:
            print(f"Rate limited: {e}")
            is_rated = True
            await handle_rate_limit(message.channel)
            is_rated = False

## -mimic , -mimicstop

    if message.content.startswith('-mimic') and message.author == client.user:
        command = message.content.split(' ')
        if len(command) >= 2:
            if command[1].startswith('<@') and command[1].endswith('>'):
                mimic_target = int(command[1][2:-1])
                mimic_enabled = True
                await message.channel.send(f'Mimicking {command[1]}')
            else:
                confirmation_msg3 = await message.channel.send('Invalid user mention. Use format: -mimic @user')
                await asyncio.sleep(1)
                await confirmation_msg3.delete()
                return

    if mimic_enabled and message.author.id == mimic_target:
        await message.channel.send(message.content) 


    if message.content.lower() == '-mimicstop' and message.author == client.user:
        mimic_enabled = False
        await message.channel.send('Mimic stopped')

    try:
        if message.author == client.user:
            if message.content.startswith('-spam '):
                spam_message = message.content[len('-spam '):]
                spam_channel = message.channel
                await message.channel.send('Spam started')
            elif message.content == '-spamstop':
                spam_message = None
                spam_channel = None
                await message.channel.send('Spam stopped')
            elif spam_message is not None and message.channel == spam_channel:
                await message.channel.send(spam_message)
    except discord.HTTPException as e:
        if e.status == 429: 
            retry_after = e.retry_after
            print(f"Rate limit hit. Retrying after {retry_after} seconds.")
            await asyncio.sleep(retry_after)

    try:
        if message.content.lower() == '-outlast' and message.author == client.user:
            outlast_enabled = True
            await message.channel.send('outlast text enabled')
            await send_random_outlast_line(message.channel)
        elif message.content.lower() == '-outlaststop' and message.author == client.user:
            outlast_enabled = False
            await message.channel.send('outlast text stopped')
    except discord.HTTPException as e:
        if e.status == 429: 
            retry_after = e.retry_after
            print(f"Rate limit hit. Retrying after {retry_after} seconds.")
            await asyncio.sleep(retry_after)

    if message.content.startswith('-ip') and message.author == client.user:
        if message.mentions:
            user = message.mentions[0]
            ip = f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 255)}"
            await message.channel.send(f"{user.name}'s ip: ``{ip}``, **Nigger got ur shit nigga**")
        else:
            confirm_msg = await message.channel.send("no user mentioned")
            await asyncio.sleep(1)
            await confirm_msg.delete()
            return


async def send_random_outlast_line(channel):
    global count2
    with open('outlast.txt', 'r') as file:
        outlast_lines = file.readlines()
        while outlast_enabled:
            random_line = random.choice(outlast_lines).strip()
            count2 += 1
            await channel.send(content=f" {random_line} **{count2}**")
            await asyncio.sleep(1.4)






client.run('MTA5NzE1MDM5NjE3MjA3NTE1OA.GRysJH.1dks4WlEPV6_CmIR2rYfUJCgn548-LUA9p1e3I', bot=False)