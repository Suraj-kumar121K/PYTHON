import datetime
import time
import webbrowser
import pyautogui
import speech_recognition as sr
import pyttsx3

def initialize_engine():
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-50)
    volume = engine.getProperty('volume')
    engine.setProperty('volume', volume+0.25)
    return engine

def speak(text):
    engine = initialize_engine()
    engine.say(text)
    engine.runAndWait()
    
def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        print("Listening.........", end="", flush=True)
        r.pause_threshold=1.0
        r.phrase_threshold=0.3
        r.sample_rate = 48000
        r.dynamic_energy_threshold=True
        r.operation_timeout=5
        r.non_speaking_duration=0.5
        r.dynamic_energy_adjustment=2
        r.energy_threshold=4000
        r.phrase_time_limit = 10
        # print(sr.Microphone.list_microphone_names())
        audio = r.listen(source)
    try:
        print("\r", end="", flush=True)
        print("Recognizing..........", end="", flush=True)
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")
    except Exception as e:
        print("Say that again please")
        return "None"
    return query

def cal_day():
    day = datetime.datetime.today().weekday() + 1
    day_dict={
        1:"Monday",
        2:"Tuesday",
        3:"Wednesday",
        4:"Thursday",
        5:"Friday",
        6:"Saturday",
        7:"Sunday"
    }
    if day in day_dict.keys():
        day_of_week = day_dict[day]
        print(day_of_week)
    return day_of_week

def wishMe():
    hour = int(datetime.datetime.now().hour)
    t = time.strftime("%I:%M:%p")
    day = cal_day()
    
    if(hour>=0) and (hour<=12) and ('AM' in t):
        speak(f"Good morning suraj, it's {day} and the time is {t}")
    elif(hour>=12) and (hour<=16) and ('PM' in t):
        print(f"Good afternoon suraj, it's {day} and the time is {t}")
    else:
        speak(f"Good evening suraj, it's {day} and the time is {t}")  

def social_media(command):
    if 'facebook' in command:
        speak("opening your facebook")
        webbrowser.open("https://www.facebook.com")
    
    elif 'youtube' in command:
        speak("opening your youtube")
        webbrowser.open("https://www.youtube.com")
        
    elif 'instagram' in command:
        speak("opening your instagram")
        webbrowser.open("https://www.instagram.com") 
        
    elif 'whatsapp' in command:
        speak("opening your whatsapp")
        webbrowser.open("https://www.whatsapp.com")  
    else:
        speak("No result found")  

def schedule():
      day = cal_day().lower()
      speak("Boss today's schedule is")
      week={
            "monday": "Boss, from 9:30 am to 7:00 pm you have company. from 7:00 pm to 4:00 am study , 4:00 am to 9:00 am sleep",
            "tuesday": "Boss, from 9:30 am to 7:00 pm you have company. from 7:00 pm to 4:00 am study , 4:00 am to 9:00 am sleep",
            "wednesday": "Boss, from 9:30 am to 7:00 pm you have company. from 7:00 pm to 4:00 am study , 4:00 am to 9:00 am sleep",
            "thursday": "Boss, from 9:30 am to 7:00 pm you have company. from 7:00 pm to 4:00 am study , 4:00 am to 9:00 am sleep",
            "friday": "Boss, from 9:30 am to 7:00 pm you have company. from 7:00 pm to 4:00 am study , 4:00 am to 9:00 am sleep",
            "saturday": "Boss, from 9:30 am to 7:00 pm you have company. from 7:00 pm to 4:00 am study , 4:00 am to 9:00 am sleep",
            "sunday": "Boss, from 9:30 am to 7:00 pm you have company. from 7:00 pm to 4:00 am study , 4:00 am to 9:00 am sleep"
        }
      if day in week.keys():
          speak(week[day])
            
if __name__ == "__main__":
    wishMe()
    while True:
        # query = command().lower()
        query = input("Enter a command-> ")
        if('facebook' in query) or ('youtube' in query) or ('instagram' in query) or ('whatsapp' in query):
            social_media(query)
        elif ("company time table" in query) or ("schedule" in query):
            schedule()
        elif ("volume up" in query) or ("increase volume" in query):
            pyautogui.press("volumeup")
            speak("Volume increased")
        elif ("volume down" in query) or ("decrease volume" in query):
            pyautogui.press("volumedown")
            speak("Volume decreased")
        elif ("volume mute" in query) or ("mute the sound" in query):
            pyautogui.press("Volumemute")
            speak("Volume muted")
        elif
        
# speak("Hello, I'm suraj")
    