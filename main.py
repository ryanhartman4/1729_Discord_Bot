# Importing libraries
import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive

# Establishing client
client = discord.Client()

# Sad words list 
sad_words = ['sad','depressed','ugh',':(','unhappy','miserable','depressing']

# starter encouragements
starter_encouragments = ['you are great','stay happy','you are wonderful']

# Turn bot off and on 
if 'responding' not in db.keys():
    db['responding'] = True


# Get quote helper function 
def get_quote():
    response = requests.get('https://zenquotes.io/api/random')

    json_data = json.loads(response.text)

    quote = json_data[0]['q'] + ' - ' + json_data[0]['a']

    return(quote)

# Updating list of encouragements
def update_encouragements(new_message):
    if 'encouragements' in db.keys():
        encouragements = db['encouragements']
        encouragements.append(new_message)
        db['encouragements'] = encouragements
    else:
        db['encouragements'] = [new_message]

def delete_encouragement(index):
    encouragements = db['encouragements']
    if len(encouragements) > index:
        del encouragements[index]
        db['encouragements'] = encouragements

# defining 'ready' message
@client.event 
async def on_ready(): 
    print('We have logged in as {0.user}'.format(client))

# Message get quote function   
@client.event
async def on_message(message): 
    if message.author == client.user:
        return
    
    msg = message.content

    if message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)
    
    if db['responding']:
        options = starter_encouragments
        if 'encouragements' in db.keys():
            for i in range(len(options)):
                db['encouragements'].append(options[i])
            options = db['encouragements']

        if any(word in msg for word in sad_words):
            await message.channel.send(random.choice(options))

    if msg.startswith('$new'):
        encouraging_message = msg.split("$new ",1)[1]
        update_encouragements(encouraging_message)
        await message.channel.send('Your encouraging message has been added')
    
    if msg.startswith('$del'):
        encouragements = []
        if "encouragements" in db.keys():
            index = int(msg.split('$del',1)[1])
            delete_encouragement(index)
            encouragements = db['encouragements']
            await message.channel.send(encouragements)
        else: 
            await message.channel.send('There is nothing to delete!')

    if msg.startswith('$list'):
        encouragements = []
        if 'encouragements' in db.keys():
            encouragements = db['encouragements']
            await message.channel.send(encouragements)
        else: 
            await message.channel.send('The list is empty!')
    
    if msg.startswith('$responding'):
        command = msg.split('$responding ',1)[1]

        if command.lower() == 'true' or command.lower() == 'on':
            db['responding'] = True
            await message.channel.send('The bot will now respond to sad words!')
        elif command.lower() == 'false' or command.lower == 'off':
            db['responding'] = False
            await message.channel.send('Responding turned off!')
        else: 
            await message.channel.send('Invalid command! Options: true, false')
        
# Running bot
keep_alive()
TOKEN = os.environ['token']
client.run(TOKEN)