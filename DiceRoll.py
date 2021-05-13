import discord
import re
from random import randint

# discord token kept in separate file for security purposes
token = open('Tokens.txt').read().rstrip()
client = discord.Client()

@client.event
async def on_message(message):
    # strips spaces and lowercases all text
    text = message.content.lower()
    text = text.replace(' ', '')

    #looks for !roll at start of message
    if text.startswith('!roll'):
        # finds all instances of #d#+/-# ex) 2d10-3
        dice = re.findall('(\d+)?d(\d+)([\+\-]\d+)?', text)
        values = []
        # for every N die (out of potential list of dice rolled at once ex) 1d20, 2d10...), gets its value and adds it to a total for that die
        for die in dice:
            die_total = 0
            for x in range(0, int(die[0])):
                die_total += randint(1, int(die[1]))
            if not die[2] == '':
                values.append(die_total + int(die[2]))
            else:
                values.append(die_total)
        output = ''
        for value in values:
            output = output + '[' + str(value) + '] '
        output.rstrip()
        await message.channel.send(output)

client.run(token)
