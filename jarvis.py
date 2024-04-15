import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

contacts = {
    "sajid": "sajeedballur2@gmail.com",
    "shashank": "ysshashank42@gmail.com",
    "Bob": "bob@example.com",
    "murali" : "murulimurthy76@gmail.com"
    # Add more contacts as needed
}

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12): 
        speak("Good Morning ")
    elif hour>=12 and hour<18:
        speak("Good Afternoon ")
    else:
        speak("Good Evening ")

    speak("I am Jarvis Sir. Please Tell me how may i help you!")    

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en')
        print(f"User Said: {query}\n")
    except Exception as e:
        print("Say that again please....")
        return "None"
    return query

def sendEmail(to , content): #iudwdwspwpgmlcfs
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('ballursajeed@gmail.com','iudwdwspwpgmlcfs')
    server.sendmail('ballursajeed@gmail.com',to,content)
    server.close()
 
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

if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia",'')
            results = wikipedia.summary(query,sentences = 2)
            speak("According To wikipedia")
            print(results)
            speak(results)
           
        elif "stop" in query:
            speak("Ok now i am stop assisting")
            break

        elif 'who are you' in query:
            speak('I am JARVIS, a virtual artificial intelligence, and I am here to assist you . I am equipped to handle a wide range of tasks, from managing your schedule to controlling the functions of the computer system')
        
        elif 'what is your name' in query:
            speak('My name is JARVIS, a virtual artificial intelligence, and I am here to assist you . I am equipped to handle a wide range of tasks, from managing your schedule to controlling the functions of the computer system')

        elif 'open youtube' in query:
            speak("opening youtube..")
            webbrowser.open("youtube.com")
            
        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("opening google..")
       
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
        
        elif 'play music' in query:
            music_dir = 'D:\\Non critical\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'time' in query:
            stsTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"The Current time is {stsTime} sir")
        
        elif 'open vs code' in query:
            codePath = "C:\\Users\SHASHANK AMITH\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            speak('opening VS code')

        elif 'email to ' in query:
            try:
                speak("What should i say")
                content = takeCommand()
                to = ''
                contact_name = query.split('email to ')[1]
               # Check if the contact name exists in the contacts dictionary
                if contact_name in contacts:
                  recipient_email = contacts[contact_name]
                  speak(f"Sending email to {contact_name}")
                # Call the sendEmail function with recipient_email as the recipient
                  sendEmail(recipient_email,content)
                else:
                  speak(f"Sorry, {contact_name} is not in your contacts.")
                  sendEmail(to,content)
                speak("Email has been sent")
     
            except Exception as e:
                print(e)
                speak("Sorry boss. I am not able to send the email at the moment")
        else:
            api_key = "AIzaSyB6m5YN2v0BVUqFHiKsmGWJbOOVkPl3PfM"
            result = generate_content(query, api_key)
            if result:
                clean_result = result.replace('*', '')  # Remove asterisks
                print(clean_result)
                speak(clean_result)
            else:
                print("No content generated for the query.")
                speak(" sorry sir,  i did not understand")
                      