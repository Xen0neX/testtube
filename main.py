# This is a test Discord Bot.
# This is not for commercial use.
# Use this bot/code at your own risk
import os
import discord
from dotenv import load_dotenv

def main():
    # get values from the .evn file
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    SUPER = os.getenv('SUPER_ID')

    client = discord.Client()

    # Ready up the bot
    @client.event
    async def on_ready():
        print(f'{client.user.name}, Hello, hello friend!')

    # Start listing to commands
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith('!hello'):
            if message.author.id == int(SUPER):
                await message.channel.send('All hail!')
            else:
                await message.channel.send('Hi!')
        elif message.content.startswith('!weather'):
            print(message.content[9:])
            await message.channel.send('This feature is under development')

    client.run(TOKEN)


# Run main only if this is run as a program and not if this file is called
if __name__ == '__main__':
    main()
