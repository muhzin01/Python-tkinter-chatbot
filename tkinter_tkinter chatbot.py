import datetime as dt
from datetime import datetime
import os
import subprocess
import webbrowser
from tkinter import *
import platform
import pyttsx3
import requests
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim
from nltk.decorators import getinfo
from tqdm import tk

root = Tk()
root.title("Chatbot")

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

dctn = {
    "music": "C:\Program Files (x86)\Steam\Steam.exe",
    "steam": "C:\Program Files (x86)\Steam\Steam.exe",
    "firefox": "C:\Program Files\Mozilla Firefox\ firefox.exe",
    "videos": "C:\Program Files (x86)\Steam\Steam.exe",
    "visual studio": "C:\Program Files (x86)\Steam\Steam.exe",

}
t = ""
e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
list1 = ["open facebook", "open youtube", "open instagram", "what is the date today", "-----can open some apps-----",
         "yes", "current location", "kochi", "current system information", "current time"]

txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
txt.grid(row=1, column=0, columnspan=2)
user = e.get().lower()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


def location1():
    s = "Bot :-"
    geolocator = Nominatim(user_agent="geoapiExercises")
    s = "Bot :-"
    place = "kochi"
    place_res = place
    location = geolocator.geocode(place)
    res = location
    ew = str(res)
    er = str(place_res)
    txt.insert(END, "\n" + s + ew)

    # object of tkinter


# and background set for light grey


# variable Classes in tkinter


# creating label for each information
# name using widget Label

def weather():
    geolocator = Nominatim(user_agent="geoapiExercises")
    Latitude = "25.594095"
    Longitude = "85.137566"
    location = geolocator.reverse(Latitude + "," + Longitude)
    address = location.raw['address']
    # city = geolocator.get('city', '')
    s = "Bot :-"
    e = user
    city = "kochi"
    city = city + " weather"
    res = requests.get(
        f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',
        headers=headers)
    txt.insert(END, "\n" + s + "searching...")
    soup = BeautifulSoup(res.text, 'html.parser')
    location = soup.select('#wob_loc')[0].getText().strip()
    time = soup.select('#wob_dts')[0].getText().strip()
    info = soup.select('#wob_dc')[0].getText().strip()
    weather = soup.select('#wob_tm')[0].getText().strip()
    list2 = [location, time, info, weather]
    for i in list2:
        txt.insert(END, "\n" + "-" + i)


def Call():
    global e, user, t
    s = "bot:-"
    txt.insert(END, "\n" + str(user))
    if t == list1[7]:
        location1()
    else:
        txt.insert(END, "\n" + s + "ok daaaaa")


def open_app():
    global user, list1, dctn
    for i in dctn:
        if (user == i):
            os.startfile(dctn[i])
            os.system(dctn[i])
            subprocess.Popen([dctn[i]])
            subprocess.call(dctn[i])


def Time_date():
    s = "Bot :-"
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    txt.insert(END, "\n" + s + "The time is = " + current_time)


def sys_info():
    my_system = platform.uname()

    txt.insert(END, "\n" + f"System: {my_system.system}")
    txt.insert(END, "\n" + f"Node Name: {my_system.node}")
    txt.insert(END, "\n" + f"Release: {my_system.release}")
    txt.insert(END, "\n" + f"Version: {my_system.version}")
    txt.insert(END, "\n" + f"Machine: {my_system.machine}")
    txt.insert(END, "\n" + f"Processor: {my_system.processor}")


def social_media():
    global user, list1
    if user == list1[0]:
        webbrowser.open('https://www.facebook.com/')
    elif (user == list1[1]):
        webbrowser.open('https://www.youtube.com/')
    elif (user == list1[2]):
        webbrowser.open("https://www.instagram.com/")


sm = list1[0] + "\n" + list1[1] + "\n" + list1[2] + "\n" + list1[3] + "\n" + list1[4]
date = dt.datetime.now()


# Send function
def send():
    global list1, user, sm, date, dctn, t, e
    send = "You :- " + e.get()
    txt.insert(END, "\n" + send)
    s = "Bot :-"
    user = e.get().lower()

    if user == "hello":
        txt.insert(END, "\n" + s + "Hi there, how can I help?" + "\n" + sm),
        pyttsx3.speak("Hi there, how can I help?")
        for i in dctn:
            txt.insert(END, "\n" + "open" + i)
        txt.insert(END, "\n" + s + "would you like know more information" + "\n" + "yes or no")
    elif user == "how are you":
        txt.insert(END, "\n" + s + "fine! and you"),
        pyttsx3.speak("fine! and you")
    elif (user == "Goodbye" or user == "See you later" or user == "see yaa" or user == "goodbye"):
        txt.insert(END, "\n" + s + "Have a nice day!")
        pyttsx3.speak("Have a nice day!")
    elif user == "Tell me a joke" or user == "Tell me something funny" or user == "crack a funny line":
        txt.insert(END, "\n" + s + "What did the buffalo say when his son left for college? Bison.! ")
        pyttsx3.speak("What did the buffalo say when his son left for college? Bison.!")

    elif user == "what are you doing":
        txt.insert(END, "\n" + s + "iam here to assisting you")
        pyttsx3.speak("iam here to assisting you")
    elif user == "Thanks" or user == "Thank you" or user == "now its my time" or user == "iam fine":
        txt.insert(END, "\n" + s + "My pleasure !")
        pyttsx3.speak("My pleasure !")

    elif user == "hi" or user == "hii" or user == "hiiii" or user == "hey":
        txt.insert(END, "\n" + s + "Hi there, what can I do for you?" + "\n" + sm)
        pyttsx3.speak("Hi there, what can I help for you?")
        for i in dctn:
            txt.insert(END, "\n" + "open" + i)
        txt.insert(END, "\n" + s + "would you like know more information...?" + "\n" + "yes or no")
    elif user == "yes":
        txt.insert(END, "\n" + "-current location" + "\n" + "-what is the weather today" + "\n" + "-" + list1[
            8] + "\n" + "-" +
                   list1[9]),
    elif user == "current location":
        location1()
    elif user == "what is the weather today":
        weather()
    elif user == list1[8]:
        sys_info()
    elif user == list1[9]:
        Time_date()
    elif user == list1[0] or user == list1[1] or user == list1[2]:
        txt.insert(END, "\n" + s + "...opening....")
        pyttsx3.speak("...opening....")
        social_media()
    elif (user == dctn["music"] or dctn["steam"] or dctn["firefox"] or dctn["videos"] or dctn["visual studio"]):
        open_app()
    elif (user == list1[3]):
        txt.insert(END, "\n" + s + "Today date is.." + f"{date:%A, %B %d, %Y}")
        pyttsx3.speak("Today date is.." + f"{date:%A, %B %d, %Y}")

    elif user == "hi" or user == "hii" or user == "hiiii" or user == "hey":
        txt.insert(END, "\n" + s + "Hi there, what can I do for you?" + "\n" + sm)
        pyttsx3.speak("Hi there, what can I help for you?")
    else:
        txt.insert(END, "\n" + s + "Sorry! I dind't got you")
        pyttsx3.speak("Sorry! I dind't got you")

    e.delete(0, END)


lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome", font=FONT_BOLD, pady=10, width=20, height=1).grid(
    row=0)

'''txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60 )
txt.grid(row=1, column=0, columnspan=2)'''

scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)

e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
e.grid(row=2, column=0)

send = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY,
              command=send).grid(row=2, column=1)

root.mainloop()


