import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import requests
import wikipedia 
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import pyjokes
import pyautogui
import time 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import instaloader
import subprocess
import PyPDF2
from bs4 import BeautifulSoup
import speedtest
from dotenv import load_dotenv

from twitterBot import tweet
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt 
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvisUi import Ui_MainWindow

import tkinter as tk
import cloudinary
import cloudinary.uploader
import cloudinary.api
import json

# Load environment variables from .env file
load_dotenv()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty("rate",195)

contacts = {
    "sajid": "sajeedballur2@gmail.com",
    "shashank": "ysshashank42@gmail.com",
    "Bob": "bob@example.com",
    # Add more contacts as needed
}

phone = {
  "me" : "+919880580629",
  "shashank": "+919008915360",
  "sanju":"+919035329887",
  "abbu": "+919535809127",
}

def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()
    
# Configure your Cloudinary credentials
cloudinary.config(
  cloud_name = os.getenv('CLOUDINARY_CLOUD_NAME'),
  api_key = os.getenv('CLOUDINARY_API_KEY'),
  api_secret = os.getenv('CLOUDINARY_API_SECRET')
)


def wishMe():
    hour = int(datetime.datetime.now().hour)
    stsTime = datetime.datetime.now().strftime('%H:%M:%S')
    if(hour>=0 and hour<12): 
        speak(f"Good Morning, it is {stsTime}")
    elif hour>=12 and hour<18:
        speak(f"Good Afternoon, it is {stsTime} ")
    else:
        speak(f"Good Evening, it is {stsTime}")

    speak("I am Jarvis Sir. Please Tell me how may i help you!")

def sendEmail(to, content): #iudwdwspwpgmlcfs
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('ballursajeed@gmail.com','iudwdwspwpgmlcfs')
    server.sendmail('ballursajeed@gmail.com',to,content)
    server.close()

def news():
    main_url = 'https://newsapi.org/v2/top-headlines?country=in&apiKey=3bf4ef889c8a4724a5168ab5070fb899'
    main_page = requests.get(main_url).json()
    articles = main_page['articles'] 
    head = []
    day = ['first','second','third','fourth','fifth','sixth','seventh','eighth','ninth','tenth']
    for ar in articles:
        head.append(ar['title'])
    for i in range (len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")
      
def generate_content(prompt, api_key):
     url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={api_key}'
     payload = {
        "contents": [{
            "parts": [{
                "text": prompt
            }]
        }]
    }
     headers = {
        'Content-Type': 'application/json'
    }
     try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # Raise an exception for non-200 response codes
        data = response.json()
        if 'candidates' in data and len(data['candidates']) > 0 and 'content' in data['candidates'][0]:
           return data['candidates'][0]['content']['parts'][0]['text']
        else:
            return None
     except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None

def pdf_reader():
    with open("description.pdf", "rb") as file:
        pdfReader = PyPDF2.PdfReader(file)
        pages = len(pdfReader.pages)
        speak(f"Total number of pages in this book is {pages}")
        speak("Sir, please enter the page number that I have to read")
        pg = int(input("Please enter the page number: "))
        page = pdfReader.pages[pg]
        text = page.extract_text()
        speak(text)

def open_notepad():
    try:
        return subprocess.Popen(['notepad.exe'])
    except FileNotFoundError:
        print("Notepad is not installed or not found in the system PATH.")

def write_to_notepad(content):
    
    try:
        notepad_process = open_notepad()
        time.sleep(1)  # Wait for Notepad to open
        pyautogui.write(content, interval=0.05)  # Write content with a slight delay between keystrokes
        speak("Content written to Notepad successfully.")
    except Exception as e:
        print("An error occurred:", e)
        return False

def upload_image_to_cloudinary( file_path):
        try:
            response = cloudinary.uploader.upload(file_path)
            url = response.get('url')
            return url
        except Exception as e:
            print(f"Failed to upload {file_path}: {e}")
            return None

def post_image( image_url):
    access_token = os.getenv('ACCESS_TOKEN')
    ig_user_id = os.getenv('IG_USER_ID')
    post_url = 'https://graph.facebook.com/v20.0/{}/media'.format(ig_user_id)
    payload = {
        'image_url': image_url,
        'caption': 'a test posting',
        'access_token': access_token,
    }

    r = requests.post(post_url, data=payload)
    print(r.text)
    print("Media uploaded successfully!")

    result = json.loads(r.text)
    if 'id' in result:
        creation_id = result['id']
        second_url = 'https://graph.facebook.com/v20.0/{}/media_publish'.format(ig_user_id)
        second_payload = {
            'creation_id': creation_id,
            'access_token': access_token,
        }
        r = requests.post(second_url, data=second_payload)
        print(r.text)
        print("image published to Instagram")
    else:
        print("Image posting is not possible!")

def select_and_post_image(file_path):
        if file_path:
            speak("Uploading the image to Cloudinary.")
            image_url = upload_image_to_cloudinary(file_path)
            if image_url:
                speak("Image uploaded successfully. Posting to Instagram.")
                post_image(image_url)
                speak("Image has been posted to Instagram successfully.")
            else:
                speak("Failed to upload the image to Cloudinary.")
        else:
            speak("No image selected.")

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 

class MainThread(QThread):

    def __init__(self):
        super(MainThread,self).__init__()
    def run(self):
        #self.TaskExecution()
        while True:
            permission = self.takeCommand().lower()
            if "wake up" in permission or "hey jarvis" in permission or "jarvis" in permission:
                self.TaskExecution()
            elif "good bye" in permission or "sleep jarvis" in permission or "shutdown jarvis" in permission:
                sys.exit()
        
    def TaskExecution(self):
        wishMe()
        notepad_process = None  # Initialize variable to hold Notepad process
        while True:
            query = self.takeCommand().lower()
           
            if "open notepad" in query:    
                path = "C:\\Program Files\\WindowsApps\\Microsoft.WindowsNotepad_11.2401.26.0_x64__8wekyb3d8bbwe\\Notepad\\Notepad.exe" 
                os.startfile(path)
            elif "close notepad" in query:     
                speak("Closing notepad")
                os.system("taskkill /f /im notepad.exe")

            elif "open adobe " in query:
                speak("opening Adobe reader")
                path = "C:\\Program Files\\Adobe\Acrobat DC\\Acrobat\\Acrobat.exe"
                os.startfile(path)
            
            elif "close adobe" in query:
                speak("Closing Adobe")
                os.system("taskkill /f /im Acrobat.exe")
            
            elif "open command prompt" in query:
                os.system("start cmd")
            
            elif "close command prompt" in query:
                speak("Closing command prompt")
                os.system("taskkill /f /im cmd.exe")
            
            elif "open camera" in query:
                cad = cv2.VideoCapture(0)
                while True:
                    ret, img = cad.read()
                    cv2.imshow('webcam',img)
                    k = cv2.waitKey(50)
                    if k==27:
                        break
                cad.release()
                cv2.destroyAllWindows()
            
            elif 'play music' in query:
                music_dir = "C:\\Users\\SHASHANK AMITH\\Music"
                song = os.listdir(music_dir)
                rd = random.choice(song)
                for s in song:
                    if s.endswith('.mp3'):
                        os.startfile(os.path.join(music_dir,rd))
            elif "ip address" in query:
                ip = get('https://api.ipify.org').text
                speak(f"Your IP address is {ip}")

            elif "wikipedia" in query:
                speak("Searching wikipedia")
                query = query.replace("wikipedia",'')
                results = wikipedia.summary(query, sentences=2)
                speak("According to wikipedia")
                speak(results)
            
            elif 'open youtube' in query:
                    speak("opening youtube..")
                    webbrowser.open("youtube.com")
                    
            elif 'open google' in query:
                    speak("Sir, what should i search on google")
                    cm = self.takeCommand().lower()
                    webbrowser.open(f"{cm}")
                    speak(f"searching on google about {cm} ..")
            
            elif 'open instagram' in query:
                    webbrowser.open("instagram.com")
                    speak("opening instagram..")

            elif 'open facebook' in query:
                speak("opening facebook..")
                webbrowser.open("facebook.com")
                
            elif 'open twitter' in query:
                    webbrowser.open("twitter.com")
                    speak("opening twitter..")

            elif 'open stack overflow' in query:
                    webbrowser.open("stackoverflow.com")
                    speak("opening stackoverflow dot com..")

            elif "send message to " in query:
                contact_name = query.split('send message to ')[1]
                if contact_name in phone:
                    speak("Sir what should i send")
                    msg = self.takeCommand().lower()
                    recipient_phone = phone[contact_name]
                    now = datetime.datetime.now()
                    # Calculate the time 15 seconds ahead
                    future_time = now + datetime.timedelta(seconds=30)
                    hour = int(future_time.strftime("%H"))
                    minute = int(future_time.strftime('%M'))
                    kit.sendwhatmsg(recipient_phone,msg,hour,minute)
                else:
                    speak(f"Sorry sir , the {contact_name} is not in your contant list")

            elif "play song on youtube" in query:
                kit.playonyt("cheques")
            
            elif "email to" in query:
                try:
                    speak("What should i say")
                    content =self.takeCommand().lower()
                    contact_name = query.split('email to ')[1]
                    # Check if the contact name exists in the contacts dictionary
                    if "send file" in content:
                        if contact_name in contacts:
                            recipient_email = contacts[contact_name]
                            speak(f"Sending email to {contact_name}")
                            # Call the sendEmail function with recipient_email as the recipient
                            to = recipient_email
                            email = 'ballursajeed@gmail.com'
                            password = 'iudwdwspwpgmlcfs'
                            speak("Okay sir, what is the subject for this email")
                            query = self.takeCommand().lower()
                            subject = query
                            speak("And sir, what is the message for this email")
                            query2 = self.takeCommand().lower()
                            message = query2
                            speak('sir please enter the correct path of the file into the shell')
                            file_location = input("Please enter the file path here:")

                            speak("Please wait sir, I am sending email now")

                            msg = MIMEMultipart()
                            msg['From'] = email
                            msg['To'] = to
                            msg['Subject'] = subject

                            msg.attach(MIMEText(message,'plain'))

                            #setUp attachment 
                            filename = os.path.basename(file_location)
                            attachment = open(file_location, 'rb')
                            part = MIMEBase('application','octet-stream')
                            part.set_payload(attachment.read())
                            encoders.encode_base64(part)
                            part.add_header('Content-Disposition','attachment; filename= %s' % filename)

                            msg.attach(part)

                            server = smtplib.SMTP('smtp.gmail.com', 587)
                            server.starttls()
                            server.login(email,password)
                            text = msg.as_string()
                            server.sendmail(email,to,text)
                            server.quit()
                            speak(f"Email has been sent to {contact_name}")

                        else:
                            speak(f"Sorry, {contact_name} is not in your contacts.")
                            break
                            
                    else:
                        if contact_name in contacts:
                            recipient_email = contacts[contact_name]
                            speak(f"Sending email to {contact_name}")
                        # Call the sendEmail function with recipient_email as the recipient
                            to = recipient_email
                            sendEmail(to,content)
                        else:
                            speak(f"Sorry, {contact_name} is not in your contacts.")
                        speak(f"Email has been sent to {contact_name}")     
                    
                except Exception as e:
                    print(e)
                    speak("Sorry boss. I am not able to send the email at the moment")
            
            elif "set alarm" in query:
                speak("Sir Please tell me the time to set alarm. for example , set alarm to 5:30 AM")
                tt = self.takeCommand().lower()
                print(tt)
                tt = tt.replace("set alarm to ","")
                tt = tt.replace(".","")
                tt = tt.upper()
                print(tt)
                import MyAlarm
                MyAlarm.alarm(tt)

            elif "tell me a joke" in query:
                joke = pyjokes.get_joke()
                speak(joke)
            
            elif "shutdown the system" in query:
                speak("System is shutdowning")
                os.system('shutdown -s')
                
            elif "restart the system" in query:
                speak("Restarting the system")
                os.system("shutdown /r /t 5")
            
            elif 'time' in query:
                    stsTime = datetime.datetime.now().strftime('%H:%M:%S')
                    speak(f"The Current time is {stsTime} sir")
                
            elif "sleep the system" in query:
                os.system("rund1132.exe pwerprof.dll, SetSuspendState 0,1,0")
                
            elif "switch the window" in query:
                speak("switching the window.....")
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")

            elif "latest news" in query:
                speak("Please wait sir, fetching the latest news")
                news()    
            
            elif "can you tweet" in query:
                speak("Sir, What should i tweet")
                cmd = self.takeCommand().lower()
                tweet(cmd)
            
            elif "tell me my location" in query or "where i am" in query or "where we are" in query:
                speak("Wait sir, let me check")
                try:
                    ip = requests.get("https://api.ipify.org").text
                    print(ip)
                    url = 'https://get.geojs.io/v1/ip/geo/'+ip+'.json'
                    geo_request = requests.get(url)
                    geo_data = geo_request.json()
                    print(geo_data)
                    city = geo_data['city']
                    state = geo_data['region']
                    country = geo_data['country']
                    speak(f"Sir i am not sure, but i think we are in {city} city of country {country}")
                except Exception as e:
                    speak("Sorry sir, Due to some netwoork issue i am not able to find where we are")

            elif "instagram profile" in query or "profile on instagram" in query:
                speak("Sir please enter the user name correctly")
                name = input("Enter the username")
                webbrowser.open(f"www.instagram.com/{name}")
                speak(f"Sir here is the profile of the user {name}")
                time.sleep(2)
                speak("Sir would you like to download profile picture of this account, say yes or no")
                condition = self.takeCommand().lower()
                print(condition)
                print(condition=='none')
                if "yes" in condition:
                        mod = instaloader.Instaloader()
                        mod.download_profile(name,profile_pic_only=True)
                        speak("I am done sir, profile picture is saved in our main folder. now i am ready to next command")
                elif "no" in condition:
                        speak("ok sir")
                while condition=='none':
                    speak("Say that again please")
                    condition = self.takeCommand().lower()
                    if "yes" in condition:
                        mod = instaloader.Instaloader()
                        mod.download_profile(name,profile_pic_only=True)
                        speak("I am done sir, profile picture is saved in our main folder. now i am ready to next command")
                    
            elif "take screenshot" in query or "take a screenshot" in query:
                speak("Sir, Please tell me the name for this screen shot file")
                name = self.takeCommand().lower()
                speak("Please sir hold screen for few seconds, i am taking a screen shot")
                time.sleep(2)
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                speak("i am done sir, the screen shot is saved in our main folder")
                
            elif "read pdf" in query:
                pdf_reader()       
            
            elif "how much battery i left" in query or "how much power we have" in query or "battery" in query:
                import psutil
                bettery = psutil.sensors_battery()
                percentage = bettery.percent
                speak(f"Sir our system have {percentage} percent bettery")
                if percentage >= 75:
                    speak("Sir we have enough power to continue our work")
                elif percentage>=40 and percentage <= 75:
                    speak("Sir we can connect our system to charging point to charge our battery")
                elif percentage >= 15 and percentage <= 30:
                    speak("we don't have enough power to work, please connect to charging")
                elif percentage <= 15:
                    speak("We have very low, please connect to charging the system will shutdown very soon")
            
            elif "internet speed" in query:
                speak("Please wait sir, i am checkimng internet speed")
                def convert_to_mbps(speed_bps):
                  return speed_bps / 1_000_000
                st = speedtest.Speedtest()
                dl_bps = st.download()
                up_bps = st.upload()
                dl_mbps = convert_to_mbps(dl_bps)
                up_mbps = convert_to_mbps(up_bps)
                
                dl_mbps_rounded = round(dl_mbps, 2)
                up_mbps_rounded = round(up_mbps, 2)
                
                speak(f"Sir we have {dl_mbps_rounded} MB per second downloading speed and {up_mbps_rounded} MB per second uploading speed")
                    
            elif "hide all files" in query or "hide this folder" in query or "visible for everyone" in query:
                speak("sir please tell me you want to hide this folder or make it visible for everyone")
                condition = self.takeCommand().lower()
                if "hide" in condition:
                    os.system("attrib +h /s /d")
                    speak("Sir, all the files in this folder are now hidden.")
                elif "visible" in condition:
                    os.system("attrib -h /s /d")
                    speak("sir, all the files in this folder are now visible to everyone.")
                elif "leave it" in condition or "leave for now" in condition:
                    speak("Ok sir")
 
            elif "open mobile camera" in query:
                import urllib.request
                import cv2
                import numpy as np
                import time
                URL = "http://100.102.167.171:8080/shot.jpg"
                while True:
                    img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()),dtype=np.uint8)
                    img = cv2.imdecode(img_arr,-1)
                    cv2.imshow("IPWebcam",img)
                    q = cv2.waitKey(1)
                    if q == ord("q"):
                        break;
                
                cv2.destroyAllWindows()
 
            elif "can you calculate" in query or "calculate" in query:
                if notepad_process:
                  notepad_process.kill()
                speak("Say what you want to calculate")
                question = self.takeCommand().lower()
                api_key = "AIzaSyB6m5YN2v0BVUqFHiKsmGWJbOOVkPl3PfM"
                result = generate_content(question, api_key)
                print(result)
                write_to_notepad(result)
            
            elif "temperature" in query:
                if "temperature in" in query:
                    search = query.split('temperature in ')[1]
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div",class_="BNeawe").text
                    speak(f"current temperature in {search} is {temp}")
                else:
                    search = "temperature in davanagere"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div",class_="BNeawe").text
                    speak(f"current {search} is {temp}")
            elif "volume up" in query:
                pyautogui.press("volumeup")
            
            elif "volume down" in query:
                pyautogui.press("volumedown")
            
            elif "volume mute" in query:
                pyautogui.press("volumemute")
            
            elif "how to" in query:
               from pywikihow import search_wikihow
               how  = query
               max_result = 1
               how_to = search_wikihow(how,max_result)
               assert len(how_to) == 1
               how_to[0].print()
               speak(how_to[0].summary)

            elif "shutdown jarvis" in query or "stop jarvis" in query:
                speak("thanks for using me sir, have a good day")
                if notepad_process:
                  notepad_process.kill()  # Close Notepad if it's open
                break
          
            elif "write" in query or "prove" in query:
                if notepad_process:
                  notepad_process.kill()
                api_key = "AIzaSyB6m5YN2v0BVUqFHiKsmGWJbOOVkPl3PfM"
                result = generate_content(query, api_key)
                speak("Ok sir here is the content for your query")
                (write_to_notepad(result))
                print(result)
                  
            elif "post on instagram" in query:
               speak("please select the image sir")
               imga_path = self.select_image()
               select_and_post_image(imga_path)
               
            else:
             api_key = "AIzaSyB6m5YN2v0BVUqFHiKsmGWJbOOVkPl3PfM"
             result = generate_content(query, api_key)
             if result:
                clean_result = result.replace('*', '')  # Remove asterisks
                print(clean_result)
                speak(clean_result)
             
            speak("sir, do you have any other work")

    def takeCommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening.......")
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing.....")
            query = r.recognize_google(audio, language='en-in')
            print(f"User Said: {query}\n")
        except Exception as e:
            print("Say that again please....")
            return "None"
        return query
    def select_image(self):
        # Function to open a file dialog and select an image
        file_path, _ = QFileDialog.getOpenFileName(None, "Select Image", "", "Image Files (*.png *.jpg *.jpeg *.gif *.bmp);;All Files (*)")
        return file_path

startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)
        self.main_thread = MainThread()
     
    def startTask(self):
        self.ui.movie = QtGui.QMovie("7LP8.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("install.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()
    
    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        lable_date = current_date.toString(Qt.ISODate)
        self.ui.label_4.setText(label_time)
        self.ui.label_3.setText(lable_date)

app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())