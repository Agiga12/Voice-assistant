import requests
import json
import speech_recognition
import pyttsx3
import subprocess
import webbrowser
import googlesearch
import os
import datetime
from bs4 import BeautifulSoup
import requests
from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models.gigachat import GigaChat

# Авторизация в сервисе GigaChat
chat = GigaChat(credentials='MzcyYmJhMTYtYTkwMS00M2FkLWEyN2EtYzNmMjhlMzlkMDhlOjBjNTdiODgxLWQyNTYtNDc0Ni05NzAwLTAzNWI3MDA3MTNkYg==', verify_ssl_certs=False)





sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5

def listen_command():

    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
        return query
    except speech_recognition.UnknownValueError:
        return 'Не понятно:('

def chatt():
    messages = [
        SystemMessage(
        content=" "
    )]
    voice = pyttsx3.init()
    voice.say('Здравствуйте, как ваше настроение?')
    voice.runAndWait()
    while True:

        # Получение голосовой команды пользователя
        user_input = listen_command()
        messages.append(HumanMessage(content=user_input))

        # Отправка запроса на анализ сервису GigaChat
        response = chat(messages)

        # Обработка ответа
        messages.append(response)
        response_text = response.content

        # Вывод ответа на экран
        print("Bot:", response_text)

        # Произношение ответа голосом (если используется TTS)
        engine = pyttsx3.init()
        engine.say(response_text)
        engine.runAndWait()
        if user_input=="выключись":
            break
def weather(city):
    voice = pyttsx3.init()
    voice.say('Назовите город')
    voice.runAndWait()

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
    }



    res = requests.get(
        f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',
        headers=headers
    )

    soup = BeautifulSoup(res.text, 'html.parser')

    precipitation = soup.select('#wob_dc')[0].getText().strip()
    weatherr = soup.select('#wob_tm')[0].getText().strip()



    print(f'''Информация об осадках: {precipitation}
    Температура воздуха: {weatherr}°C''')


def time():
    now = datetime.datetime.now()
    voice = pyttsx3.init()
    voice.say('Сейчас %d часов %d минут' % (now.hour, now.minute))
    print(now.hour, now.minute)
    voice.runAndWait()


def openurl():
    voice = pyttsx3.init()
    voice.say('Что бы вы хотели найти?')
    voice.runAndWait()
    try:
        from googlesearch import search
    except ImportError:
        print("Не получилось найти:(")


    query = listen_command()

    for j in search(query, tld="co.in", num=1, stop=1, pause=1):
        print(j)

        url = j
        chrome_path = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        webbrowser.register("chrome", None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get("chrome").open_new(url)
def music():
    voice = pyttsx3.init()
    voice.say('Приятного прослушивания!')
    voice.runAndWait()
    url = "https://music.yandex.ru/home"
    chrome_path = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    webbrowser.register("chrome", None, webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get("chrome").open_new(url)
def openSteam():
    voice = pyttsx3.init()
    voice.say('Открываю')
    voice.runAndWait()
    subprocess.Popen("C:\Program Files (x86)\Steam\Steam.exe")

def opendoc():
    voice = pyttsx3.init()
    voice.say('Произнесите фамилию человека, чьи документы вы хотели бы открыть')
    voice.runAndWait()

    query = listen_command()
    if query:
        file_path = f"L:\\doc\\{query}.txt"
        if os.path.exists(file_path):
            subprocess.Popen(['notepad.exe', file_path])
        else:
            voice.say('Документ не найден.')
            voice.runAndWait()
    else:
        voice.say('Не удалось распознать фамилию.')
        voice.runAndWait()
def openBrowser():
    voice = pyttsx3.init()
    voice.say('Выполняю')
    voice.runAndWait()
    subprocess.Popen("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
def greeting():
    voice = pyttsx3.init()
    text = 'Добрый день!'
    voice.say(text)
    voice.runAndWait()

def create_task():
    voice = pyttsx3.init()
    voice.say('Что добавить в список дел?')
    voice.runAndWait()

    query = listen_command()

    with open('task_list.txt', 'a') as file:
        file.write(f'{query}; ')


    voice.say (f'Задача {query} добавлена в список!')
    voice.runAndWait()

def main():
#    bot_active = False  # Инициализация переменной для отслеживания состояния бота

#   def activate_bot():
#        nonlocal bot_active
#        bot_active = True
#        print("Бот активирован.")
#
#    def deactivate_bot():
#        nonlocal bot_active
#        bot_active = False
#        print("Бот выключен.")


    query = listen_command()
    while query != 'стоп':
        if query == 'давай пообщаемся':
            chatt()
        elif query == 'привет друг'or query == 'приветствую' or query == 'привет' or query == 'здравствуй' or query == 'хай':
            print(greeting())

        elif query == 'добавить задачу' or query == 'список дел':
            print(create_task())
        elif query == 'играть' or query == 'открой стим':
            print(openSteam())
        elif query == 'открой браузер' or query == 'гугл' or query == 'открой гугл':
            print(openBrowser())
        elif query == 'музыка' or query == 'яндекс музыка':
            print(music())
        elif query == 'искать':
            print(openurl())
        elif query == 'время':
            print(time())
        elif query == 'погода':
            city = listen_command()
            print(weather(city))
            # Call the getWeather function with the city name to update the frontend
            requests.get(f'http://127.0.0.1:5000/weather?city={city}')
        elif query == 'открыть документ':
            print(opendoc())
        else:
            print('Не понятно :( ')
        query = listen_command()

if __name__ == '__main__':
    main()


