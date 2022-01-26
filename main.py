# This is a sample Python script.
import os
import discord
from dotenv import load_dotenv


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    SUPER = os.getenv('SUPER_ID')

    client = discord.Client()

    @client.event
    async def on_ready():
        print(f'{client.user.name}, Hello, hello friend!')

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
            await message.channel.send('This feature is under development')

    client.run(TOKEN)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
