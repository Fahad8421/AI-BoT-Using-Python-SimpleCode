from sys import path
import pyttsx3
from requests.api import head
import speech_recognition as sr
import datetime
import os
import cv2
import random
import requests 
from requests import get
import wikipedia
import webbrowser
import smtplib
import sys
import time
import datetime
import pyjokes
import pyautogui
import instadownloader
from wikipedia.wikipedia import page
import PyPDF2
from  email.mime.text import MIMEText
from  email.mime.multipart import MIMEMultipart
from  email.mime.base import MIMEBase
from email import encoders
import instaloader
import operator
import random
import pywhatkit
import PyQt5
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtCore import QTimer ,QTime ,QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvisUi import Ui_jarvisUi


engine = pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices',voices[0].id)

#take to Speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
# to convert voice to text


#to wish
def wish():
   hour =int( datetime.datetime.now().hour)

   if hour>= 0 and  hour<= 12:
      speak("good morning")
   elif hour>=12 and hour<=18:
      speak("good afternoon")
   else:
      speak("good eveaning")
   speak("hello Sir . please say  how may i help you..")

#send email
def sendEmail(t0,content):
  server = satplib.SMTP("smtp.gmail.com",587)
  server.ehlo()
  server.starttls()
  server.login('fahadbakshi123@gmail.com','9860056917')
  server.sendemail('fahadbakshi123@gmail.com', to ,content)
  server.close()

#for news update
def news():
   main_url ="http://newsapi.org/v2/top-headlines?sources=techcrunch&apikey=e8b3d2c615a8438da71658285591742c"

   main_page = requests.get(main_url).json()
   #print (main_page)
   articles = main_page["articles"]
   #print(articles)
   head=[]
   day=["first","second","third","foruth","fifth","sixth","seventh","eighth","ninth","tenth"]
   for ar in articles:
      head.append(ar["title"])
   for i in range(len(day)):
      speak(f"today's {day[i]} news is {head[i]} ")


def pdf_reader():
   book = open('DAA.pdf','rb')
   pdfReader = PyPDF2.pdfFileReader(book)   #pip install pyPDF2
   pages = pdfReader.numpages
   speak(f"total number of pages in this bokk{pages}")
   speak("sir please enter the page number i have to read")
   pg = int(input("please enter the page number:"))
   page = pdfReader.getpage(pg)
   text = page.extractText()
   speak(text)

class MainThread(QThread):
   
   def __int__(self):
      super(MainThread,self).__int__()
   
   def run(self):
      self.TaskExecution

   def takecommand(self):
      r=sr.Recognizer()
      with sr.Microphone() as source:
         print("Listening......")
         r.pause_threshold=1
         audio = r.listen(source,timeout=1,phrase_time_limit=5)
      
      try:
         print("Recognizing.....")
         query = r.recognize_google(audio,language ='en-in')
         print(f"user said:{query}")

      except Exception as e:
         speak("say that again please.........")
         return "none"
      return query

   def TaskExecution(self):

      wish()
      #takecommand()
      #speak("this is advance jarvis")

   
      while True:
      #if 1:

         self.query = self.takecommand()
         #logical building for task
         if "open notepad" in self.query:
            npath="C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories"
            os.startfile(npath)
         
         elif "open chorme" in self.query:
            npath="C:\ProgramData\Microsoft\Windows\Start Menu\Programs"
            os.startfile(npath)

         elif "open commad prompt" in self.query:
            os.system("start cmd")

         elif "open camera" in self.query:
            cap=cv2.VideoCapture(0)  # for internal camer 0 for external 1
            while True:
               ret,img = cap.read()
               cv2.imshow('webcam',img)
               k=cv2.waitKey(50)
               if k ==27:
                  break
            cap.release()
            cv2.destroyAllWindows()

         elif "play music" in self.query:
            music_dir ="D:\Quran sharif\Al_Quraan_Ul_Karim_2"
            songs = os.listdir
            # rd = random.choice(songs)   <----- for random song
            for song in songs:
               if songs.endswith('.mp3'): 
                  os.startfile(os.path.join(music_dir,song))

         
         elif "ip address" in self.query:
            ipAdd = requests.get('https://api.ipify.org').text
            print(ipAdd)
            speak("your ip address is 1.187.50.126 ")
            #ip = get('https://api.ipify.org').text
            #speak(f"your ip address is{ip}")

         elif "wikipedia" in self.query:
            speak("searching wikipedia......")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
         # print(results) 

         elif "open youtube" in self.query:
            webbrowser.open("www.youtube.com")

         elif "open facebook" in self.query:
            webbrowser.open("www.facebook.com")

         elif "open stackoverflow" in self.query:
            webbrowser.open("www.stackoverflow.com")

         elif "open instagram" in self.query:
            webbrowser.open("www.instagram.com")
            speak("opeaning instagram..")

         elif "open my Whatsapp " in self.query:
            webbrowser.open("https://web.whatsapp.com//")
            
            

         elif "open my instagram account" in self.query:
            webbrowser.open("https://www.instagram.com/fahadbakshi/")

         elif "open my facebook account" in self.query:
            webbrowser.open("https://www.facebook.com/profile.php?id=100008560592205")

         elif "open Fahim account" in self.query:
            webbrowser.open("https://www.instagram.com/fahimbakshi/")

         elif "open yash account" in self.query:
            webbrowser.open("https://www.instagram.com/fahimbakshi/")

         elif "open imran account" in self.query:
            webbrowser.open("https://www.instagram.com/yash_padwalkar/")

         elif "open Ruksar account" in self.query:
            webbrowser.open("https://www.instagram.com/r_u_k_s_a_r_mujawar/")

         elif "open Gyatari account" in self.query:
            webbrowser.open("https://www.instagram.com/cool__gayu/")

         elif "open google" in self.query:
            speak("sir,what should i serach on google")
            cm = self.takecommand().lower()
            webbrowser.open(f"{cm}")
            
         elif "send message" in self.query:
            pywhatkit.sendwhatmsg('+88304 58846', 'i am fahad', 11,15)
                                 #number ,msg.timing(houres,minutes)


         elif"play song on youtube" in self.query:
            pywhatkit.playonyt("see u again")

         elif "send email" in self.query:
            try:
               speak("what should i say")
               content = self.takecommand().lower()
               to ="imranmurshad16@gmail.com"
               sendEmail(to,content)
               speak("email has been sent to fahad")

            except Exception as e:
               print(e)
               speak("sorry sir i am not able to send email")
      
         elif"no thanks " in self.query:
            speak("thank for using me sir, have a good day.")
            sys.exit()

      #to close any application
         elif "close notepad" in self.query:
            speak("okay sir,closing notepad")
            os.system("taskkill /f/im notepad.exe")

      #to set an alarm
         elif "set alarm" in self.query:
            nn = int(datetime.datetime.now().hour)
            if nn==22:
               music_dir ='E:\\music'
               songs = os.listdir(music_dir)
               os.startfile(os.path.join(music_dir.songs[0]))

      #to fine joke
         elif "joke " in self.query:
            joke = pyjokes.get_joke()
            speak(joke)

         elif "shut down the system" in self.query:
            os.system("shutdown /r /t 5")

         elif "restart the system" in self.query:
            os.system("shutdown /r /t 5")

         elif "sleep the system" in self.query:
            os.system("rundll32.exe powrprof.dil,setsuspendstate 0,1,0")
         
         elif "switch the window " in self.query:
            pyautogui.keydown("alt")
            pyautogui.keydown("tab")
            time.sleep(1)
            pyautogui.keydown("alt")

         elif "tell me a news" in self.query:
            speak("please wait sir, featchin news... ")
            news()


         elif "email to Fahad" in self.query:

            speak("sir what should i  say ")
            self.query= self.takecommand().lower()
            if "send file" in self.query:
               email = "fahadbaksho123@gmail.com"
               password ="9860056917"
               send_to_email ="fahadbakshi03@gmail.com"
               speak("okay..sir what is the subject for email")
               self.query= self.takecommand().lower()
               subject = query
               speak("and sir what is the message of  thsi email ")
               self.query2 = self.takecommand().lower()
               message = self.query2
               speak(" sir , please enter the correct path of file into the shell.")
               file_location = input("please enter the path here = ")

               speak(" please waith sir , i am sending Email.") 

               msg =MIMEMultipart()
               msg['form'] = email
               msg['to'] =send_to_email
               msg['subject'] = subject

               msg.attach(MIMEText(message,'plain'))

               # Setup the attachment
               filename= os.path.basename(file_location)
               attachment =open(file_location,"rb")
               part = MIMEBase('application','octet-stream')
               part.set_playload(attachment.read())
               encoders.encode_base64(part)
               part.add_header('content-Disposition',"attachment ; filename= %s" % filename)

               #Attach the attachment to  the MIMEMultipart object
               msg.attach(part)

               server = smtplib.SMTP('smpt.google.com',587)
               server.starttls()
               server.login(email,password)
               text = msg.as_string()
               server.quit()
               speak("email has been send")

            else:
                  email ="fahadbakshi123@gamil.com" 
                  password="9860056917"
                  send_to_email="fahadbakshi03@gmail.com"
                  message = self.query

                  server =smtplib.SMTP('smtp.gmail.com ',587)
                  server.starttls()
                  server.login(email,password)
                  server.quit()
                  speak("email has been send ")

      

               
         elif "where i am " in self.query or "where we are" in self.query:
            speak("wait sir ,let me chek")
            try:
               ipAdd = requests.get('https://api.ipify.org').text
               print(ipAdd)
               url ='https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
               geo_requests = requests.get(url)
               geo_data = geo_requests.json()
               #print(geo_data)
               city = geo_data['city']
               #state =geo_data['state']
               country = geo_data['country']
               speak(f"sir i am not sure, but i think your are in in {city} city of {country} country  ")
            except Exception as e :
               speak(" sorry sir ,due to network issue i am not able to find where we are.")
               pass 


            # instagarm profile
      
         elif "instagram profile " in self.query or "profile on instagram " in self.query:
            speak("sir please enter the user name correctly.")
            name = input("enter username here:")
            webbrowser.open(f"WWW.instagram.com{name}")
            speak(f"sir here is the profile of the user {name}")
            time.sleep(5)
            speak("sir whould you like to download profile picture of this account.")
            condition = self.takecommand().lower()
            if "yes" in condition:
               mod = instadownloader.Instaloader() #pip install instadownloader
               mod.downloade_profile(name , profile_pic_only=True)
               speak("i am done sir, profile picture is saved in your download folder ")
            else:
               pass


         # to take Screen shot

         elif "take Screenshot" in self.query:
            speak("sir please say me a name for screen shot file.")
            name = self.takecommand().lower()
            speak("please sir hold the screen for some movement i am taking Screenshot")
            time.sleep(3)
            img =pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("i am done sir,  i save Screen shot in your folder")

         #to read Pdf file

         elif "read PDF" in self.query:
            pdf_reader()


      #to hide and un hide file in system
         elif "hide all file " in self.query or "hide this file" in self.query or "visible for everyone" in self.query:
            speak("sir please tell me u want to hide thsi folder or make it visible for everyone")
            condition = self.takecommand().lower()
            if "hide it" in condition:
               os.system("attrib +h /s /d") #os module
               speak("all this file in ths folder are now hidden.")

            elif" make it visible" in condition:
               os.system("attrib -h /s /d")
               speak("sir ,all file in this folder are noe visible to everone")

            elif "leave it"  in condition or "leave for now" in condition:
               speak(" ok sir")
   
startExecution  = MainThread()


class Main(QMainWindow):
   def __init__(self):
      super().__init__()
      self.ui = Ui_jarvisUi()
      self.ui.setupUi(self)
      self.ui.Run.clicked.connect(self.startTask)
      self.ui.pushButton_2.clicked.connect(self.close)
   
   def startTask(self):
      self.ui.movie= QtGui.QMovie("1.jpg")
      self.ui.label.setMovie(self.ui.movie)
      self.ui.movie.start()
      self.ui.movie= QtGui.QMovie("int.gif")
      self.ui.label_2.setMovie(self.ui.movie)
      self.ui.movie.start()
      self.ui.movie= QtGui.QMovie("clock.gif")
      self.ui.label_3.setMovie(self.ui.movie)
      self.ui.movie.start()
      self.ui.movie= QtGui.QMovie("Network.gif")
      self.ui.label_4.setMovie(self.ui.movie)
      self.ui.movie.start()
      self.ui.movie= QtGui.QMovie("story.gif")
      self.ui.label_5.setMovie(self.ui.movie)
      self.ui.movie.start()
      self.ui.movie= QtGui.QMovie("giphy-5.gif")
      self.ui.label_6.setMovie(self.ui.movie)
      self.ui.movie.start()
      self.ui.movie= QtGui.QMovie("cyberpunk-alien.gif")
      self.ui.label_7.setMovie(self.ui.movie)
      self.ui.movie.start()
      self.ui.movie= QtGui.QMovie("face.gif")
      self.ui.label_8.setMovie(self.ui.movie)
      self.ui.movie.start()
      timer = QTimer(self)
      timer.timeout.connect(self.showTime)
      timer.start(1000)
      startExecution.start()

   def showtime(self):
      current_time = QTime.currentTime()
      current_time = QDate.currentDate()
      label_time = current_time.toString('hh:mm:ss')
      #label_date = current_date.toString(Qt.ISODate)
      self.ui.textBrowser.setText(label_time)
      #self.ui.textBrowser_2.setText(label_date)

app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())
         #speak("sir,do you have any other work")