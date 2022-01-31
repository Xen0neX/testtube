# This is a test Discord Bot.
# This is not for commercial use.
# Use this bot/code at your own risk
import os
import discord
from dotenv import load_dotenv
import requests
import pandas as pd


# def get_weather(city_name):
#     base_weather_url = "https://api.openweathermap.org/data/2.5/weather?q="
#     load_dotenv()
#     weather_api = os.getenv('OPEN_WEATHER')
#     weather_url = base_weather_url+city_name+"&apiid="+weather_api
#     weather_response = requests.get(weather_url)
#     json_weather_data = weather_response.json()
#     print(json_weather_data)

def get_film(film_name):
    base_film_url = "http://www.omdbapi.com/?apikey="
    film_title = film_name.replace(" ", "_")
    load_dotenv()
    film_token = os.getenv('OMDB_TOKEN')
    film_url = base_film_url + film_token + "&t=" + film_title

    film_data = requests.get(film_url)
    film_data_json = film_data.json()
    film_database = pd.DataFrame(film_data_json)
    print(film_database)
    for key, value in film_data_json.items():
        print(key + ':', value)


def help_message():
    general_help = "The Bot currently supports the following commands:\n" \
                   "**!help :** Displays this help page\n" \
                   "**!hello :** Responds with a pleasant greeting\n" \
                   "**!film<space><name of film>:** Provides information about the film\n" \
                   "**!weather :** returns information about the current weather"
    return general_help


def main():
    # get values from the .evn file
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    SUPER = os.getenv('SUPER_ID')

    client = discord.Client()

    # get_film("The Dark Knight")

    # Ready up the bot
    @client.event
    async def on_ready():
        print(f'{client.user.name}, Hello, hello friend!')

    # Start listening for commands
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith('!hello'):
            if message.author.id == int(SUPER):
                await message.channel.send('All hail!')
            else:
                await message.channel.send('Hi!')

        if message.content.startswith('!help'):
            if len(message.content) < 6:
                send_help = help_message()
                await message.channel.send(send_help)
            else:
                await message.channel.send("More helps pages are being writen")

        if message.content.startswith('!film'):
            print(message.content[6:])
            await message.channel.send('This feature is under development')

        if message.content.startswith('!weather'):
            print(message.content[9:])
            await message.channel.send('This feature is under development')

    client.run(TOKEN)


# Run main only if this is run as a program and not if this file is called
if __name__ == '__main__':
    main()
