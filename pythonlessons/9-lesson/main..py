from mylog import add_to_log
import requests
import telebot

API_URL = "https://api.openweathermap.org/data/2.5/weather"
API_KEY_WEATHER = "58be6e33e2673b0273048234ee64ede7"
API_KEY_BOT = "7706761124:AAETi8CN-uGRMxm5-ST8-WZA6CiF2lBeTKA"

bot = telebot.TeleBot(API_KEY_BOT)

def get_location() ->str :
    """вернет город"""
    return input("какой город?")

def get_weather(location: str) -> float :
    """возвращает погоду"""
    params_openweathermap = {"q": location, "appid": API_KEY_WEATHER}
    response_openweathermap = requests.get(API_URL, params=params_openweathermap, timeout=10)
    my_weather = response_openweathermap.json()
    return my_weather["main"]["temp"]

@bot.message_handler(commands=["start", "hello", "help"])
def main(message):
    if message.text == "/start" :
         bot.send_message(message.chat.id, "hi, " + message.from_user.first_name + message.from_user.last_name)
    if message.text == "/help" :
         bot.send_message(message.chat.id, "введите город")

@bot.message_handler()
def main(message):
    lock = message.text
    add_to_log("User " + message.from_user.first_name + message.from_user.last_name + " asked weather for " + lock)
    try:
        bot.send_message(message.chat.id, str(get_weather(lock) - 273))
    except:
        bot.send_message(message.chat.id, "ты уверен?")
    add_to_log("Weather for " + lock + " is " + str(get_weather(lock) - 273))

bot.polling(non_stop=True)

