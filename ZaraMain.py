from fileinput import close
import PyPDF2
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import pyjokes 
import ctypes
import pyautogui 
import time
import requests
import instaloader # type: ignore
from PyPDF2 import PdfReader # type: ignore
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from ZaraUi import Ui_ZaraUi
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QThread

engine=pyttsx3.init('sapi5')
voices=engine.getProperty("voices")
engine.setProperty('voice',voices[1].id)

#text to speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# def takeCommand():
#     r=sr.Recognizer()
#     with sr.Microphone() as source:
#         print("listening...")
#         r.pause_threshold=1
#         audio=r.listen(source,timeout=1,phrase_time_limit=5)
#     try:
#         print("Recognizing...")
#         query=r.recognize_google(audio,language="en-in")
#         print(f"user said:{query}")
#     except Exception as e:
#            speak("say that again please...") 
#            return "none"
#     return query

def wishMe():
     hour = int(datetime.datetime.now().hour)
     tm = time.strftime("%H hour %M minutes %p")
     if hour>=0 and hour<=12:
          speak(f"good morning, it's{tm}")
     elif hour>12 and hour<18:
          speak(f"good afternoon, it's{tm}")
     else:
         
         speak(f"good evening, it's{tm}") 
     speak("i am Zara... please tell me how may i help you") 

def location():
     speak("wait ,let me check")
     try:
             ipAdd=requests.get("https://api.ipify.org").text
             print(ipAdd)
             url='https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
             geo_requests=requests.get(url)
             geo_data=geo_requests.json()
             city=geo_data['city']
             country=geo_data['country']
             print(f'i am not sure,but i think we are in {city} city of  {country} country')
             speak(f'i am not sure,but i think we are in {city} city of  {country} country')
     except Exception as e:
             print(e)
             speak("sorry mam,due to technical issue i am not able to find where we are")               

def close(app):
    os.system(f'taskkill /f /im {app}')

def op():
     speak("opening mam")

def pdf_reader():
    with open(r"C:\Users\wajih\Desktop\Angular.pdf", 'rb') as file:
      reader = PdfReader(file)
      pgs=len(reader.pages)
      print(f"Pages: {pgs}")
      speak(f"{pgs} pages have in this book mam")
      speak("which page do you want me to read,please eneter the page number")
      pg=int(input("enter page number:"))
      page=reader.pages[pg]
      text=page.extract_text()
      print(text)
      speak(text)

class MainThread(QThread):
     def __init__(self):
          super(MainThread,self).__init__()
     def run(self):
          self.TaskExecution()
     
     def takeCommand(self):
          r=sr.Recognizer()
          with sr.Microphone() as source:
               print("listening...")
               r.pause_threshold=1
               audio=r.listen(source,timeout=3,phrase_time_limit=5)
          try:
               print("Recognizing...")
               query=r.recognize_google(audio,language="en-in")
               print(f"user said:{query}")
          except Exception as e:
                    speak("say that again please...") 
                    return "none"
          return query
    
     def TaskExecution(self):
      wishMe() 
      while True:
         
         self.query=self.takeCommand().lower()

         if "hello" in self.query:
              speak("hello mam")  
          
         elif "how are you" in self.query:
              speak("i am good mam ,thank you for asking ,what about you")
          
         elif "i am doing great" in self.query:
              speak("that's great to hear")
              speak("please tell me how may i help you")
              
         
         elif "open notepad" in self.query:
              op()
              npath="C:\\Windows\\notepad.exe"
              os.startfile(npath)
         
         elif "close notepad" in  self.query:
              close("notepad.exe")

         elif "open command prompt" in  self.query:
              op()
              os.system("start cmd")
          
         elif "close command prompt" in self.query:
              close("cmd.exe")

         elif "open camera" in  self.query:
              op()
              os.system("start microsoft.windows.camera:")
              speak("Camera opened successfully!")
         
         elif "close camera" in  self.query:
              os.system("taskkill /f /im WindowsCamera.exe")
              speak("Camera closed successfully!")
         
         elif "play music" in  self.query: 
              music_dir="C:\\Users\\wajih\\Desktop\\music_dir" 
              songs=os.listdir(music_dir)
              rd=random.choice(songs)
              for song in songs:
                   if song.endswith('.mp3'):
                     os.startfile(os.path.join(music_dir,song))
         
         elif "ip address" in  self.query:
              ip=get('https://api.ipify.org').text
              print(ip)
              speak(f"your ip address is {ip}")

         elif "wikipedia" in self.query:
              speak("searching in wikipedia...")
              query=query.replace("wikipedia","")
              results=wikipedia.summary(query,sentences=1)
              speak("according to wikipedia")
              print(results)
              speak(results)

         elif "open youtube" in  self.query:
              op()
              webbrowser.open("www.youtube.com")

         elif "open stack overflow" in  self.query:
              op()
              webbrowser.open("www.stackoverflow.com")

         elif "open google" in  self.query:
              op()
              speak("what should i search on google?")
              cm=self.takeCommand().lower()
              webbrowser.open(f"{cm}")

         elif "send message" in  self.query:
              speak("sending mam,please gimme a second")
              kit.sendwhatmsg("+918978935262","ok",11,13)
              speak("msg sent successfully")

         elif "play song on youtube" in  self.query:
              kit.playonyt("see you again")

         elif "set alarm" in  self.query:
             tt=int(datetime.datetime.now().hour)
             if tt==19:
                 speak(f"speak wake up the time is {tt}")
                 music_dir="C:\\Users\\wajih\\Desktop\\music_dir" 
                 songs=os.listdir(music_dir)
                 os.startfile(os.path.join(music_dir,songs[0]))
         
         elif "tell me a joke" in  self.query:
             joke=pyjokes.get_joke()
             print(f'joke:{joke}')
             speak(joke)

         elif "shut down the system" in  self.query:
             os.system("shutdown /s /t 5")

         elif "restart the system" in  self.query:
             os.system("shutdown /r /t 5")
             
         elif "sleep the system" in  self.query:
            ctypes.windll.PowrProf.SetSuspendState(0, 1, 0)
          
         elif "switch the window" in  self.query:
             pyautogui.keyDown("alt")
             pyautogui.press("tab")
             time.sleep(3)
             pyautogui.keyUp("alt")
         
         elif "love you" in  self.query:
             speak("sorry mam i am unable to recieve your love")
             speak("As per my knowledge you have a boyfriend named jaan please express your love to him")
         
         elif "where am i" in  self.query or "where we are" in  self.query or "find location" in  self.query:
              location()
         
         elif "insta profile" in  self.query or "download insta profile" in  self.query:
              speak("sir please enter the username correctly")
              name=input("enter username here: ")
              webbrowser.open(f"www.instagram.com/{name}")
              speak(f"mam here is the profile of the user {name}")
              time.sleep(5)
              speak("sir would you like to download profile picture")
              condition=self.takeCommand().lower()
              if "yes" in condition or "proceed" in condition:
                   mod=instaloader.Instaloader()
                   mod.download_profile(name,profile_pic_only=True)
                   speak("profile photo has been downloaded,please check in the folder")  
              else:
                   pass
         
         elif "take screenshot" in  self.query:
                mysc=pyautogui.screenshot()
                mysc.save(r'D:\\screenshot.png')
                speak("screenshot taken and saved in d drive")

         elif "open c drive" in  self.query:
              op()
              os.startfile("C:\\")
          
         elif "open d drive" in  self.query:
              op()
              os.startfile("D:\\")

         elif "open e drive" in  self.query:
              op()
              os.startfile("E:\\")

         elif "open f drive" in  self.query:
              op()
              os.startfile("E:\\")
         
         elif "are you there" in  self.query:
              speak("yes mam....")
         
         elif "thank you" in  self.query:
              speak("it's my pleasure mam")

         elif "close" in  self.query:
              speak("do you have any otherworks mam")
              
         elif "no thanks" in  self.query:
          speak(" ok i am quitting mam,have a good day!")
          break
          
         elif "read pdf" in  self.query:
              pdf_reader()
        
         elif 'timer' in self.query or 'stopwatch' in self.query:
                speak("For how many minutes?")
                timing = self.takecommand()
                timing =timing.replace('minutes', '')
                timing = timing.replace('minute', '')
                timing = timing.replace('for', '')
                timing = float(timing)
                timing = timing * 60
                speak(f'I will remind you in {timing} seconds')
                time.sleep(timing)
                speak('Your time has been finished sir') 

startExecution=MainThread()
class Main(QMainWindow):
     def __init__(self):
          super().__init__()
          self.ui=Ui_ZaraUi()
          self.ui.setupUi(self)
          self.ui.pushButton.clicked.connect(self.startTask)
          self.ui.pushButton_2.clicked.connect(self.close)
     
     def startTask(self):
          self.ui.movie=QtGui.QMovie("../../Downloads/background_img.jpg")
          self.ui.label.setMovie(self.ui.movie)
          self.ui.movie.start()
          self.ui.movie=QtGui.QMovie("../../Downloads/top_loading.gif")
          self.ui.label_2.setMovie(self.ui.movie)
          self.ui.movie.start()
          timer=QTimer(self)
          timer.timeout.connect(self.showTime)
          timer.start(1000)
          startExecution.start()

     def showTime(self):
       current_time=QTime.currentTime()
       current_date=QDate.currentDate()
       label_time=current_time.toString("hh:mm:ss")
       label_date=current_date.toString(Qt.ISODate)
       self.ui.textBrowser.setText(label_date)
       self.ui.textBrowser_2.setText(label_time)

    
app=QApplication(sys.argv) # type: ignore
Zaara=Main()
Zaara.show()
exit(app.exec_())

           
                
              
              


     