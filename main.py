# This is a sample Python script.
import os
import discord
from dotenv import load_dotenv

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')

    client = discord.Client()

    client.run(TOKEN)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()