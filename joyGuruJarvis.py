from tkinter import *
import pygame 
import speech_recognition as  sr 
import pyttsx3
import pygame
import wikipedia
import webbrowser
import smtplib
import random
import os, sys, subprocess, datetime
import  time 
from PIL import  ImageTk, Image
import requests
import json
import cv2
import pyzbar.pyzbar as pyz 

from pytube import *
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *

#Music Loader....

pygame.mixer.init()
pygame.mixer.music.load('JARVIS.mp3')
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(1)


time.sleep(23)


#Making  Engine Property.....

engine=pyttsx3.init()
voices=engine.getProperty('voices')

#Speak Function...

def speak(audio):
	engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0')
	engine.say(audio)
	engine.runAndWait()



def myCommand():
	r=sr.Recognizer()
	with sr.Microphone() as source:
		audio=r.listen(source)
	try:
		query1=r.recognize_google(audio,  language='en-in')

	except sr.UnknownValueError:
		speak("Try Again, Please")
		pass
	return  query1




def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!, Master')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon! Master')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening! Master')


# class Widget:
#     def __init__(self):
#        root = Tk()
#        root.title('JARVIS Developed By Chando Dhar')
#        root.config(background='Red')
#        root.geometry('700x600')
#        root.resizable(0, 0)
#        # root.iconbitmap(r'C:\\Users\\QC\\Downloads\\Untitled-1.ico')
#        # img = ImageTk.PhotoImage(Image.open(r'test01.png'))
#        # panel = Label(root, image = img)
#        # panel.pack(side = "bottom", fill = "both", expand = "no")
#        self.compText = StringVar()
#        self.userText = StringVar()

#        self.userText.set('Click \'Start Listening\' to Give commands')

#        userFrame = LabelFrame(root, text="USER", font=('Black ops one', 10, 'bold'))
#        userFrame.pack(fill="both", expand="yes")
         
#        left2 = Message(userFrame, textvariable=self.userText, bg='dodgerBlue', fg='white')
#        left2.config(font=("Comic Sans MS", 10, 'bold'))
#        left2.pack(fill='both', expand='yes')

#        compFrame = LabelFrame(root, text="JARVIS", font=('Black ops one', 10, 'bold'))
#        compFrame.pack(fill="both", expand="yes")
         
#        left1 = Message(compFrame, textvariable=self.compText, bg='Red',fg='white')
#        left1.config(font=("Comic Sans MS", 10, 'bold'))
#        left1.pack(fill='both', expand='yes')
       
#        btn = Button(root, text='Start Listening!', font=('Black ops one', 25, 'bold'), bg='deepSkyBlue', fg='white').pack(fill='x', expand='no')
#        btn2 = Button(root, text='Close!', font=('Black Ops One', 25, 'bold'), bg='deepSkyBlue', fg='white', command=root.destroy).pack(fill='x', expand='no')

       
#        speak('Hello, I am JARVIS! What should I do for You?')
#        self.compText.set('Hello, I am JARVIS! What should I do for You?')

#        # root.bind("<Return>", self.clicked) # handle the enter key event of your keyboard
#        root.mainloop()


class Widget():
	def __init__(self):
		root=Tk()
		root.title("J.A.R.V.I.S")
		root.config(background='#F0F0F0')
		root.iconbitmap("fridayicon.ico")
		root.geometry("700x650")
		root.resizable(0,0)
		icon01=PhotoImage(file="fridayicon.png")
		icon02=PhotoImage(file="speak.png")


		def getTime():
			timeString=time.strftime("%I: %M: %S : %p")
			clock.config(text=timeString)
			clock.after(200,getTime)

		label=Label(root,text="'J.A.R.V.I.S' DEVELOPED BY MISHU DHAR",bg='deepSkyBlue',fg='#391C11',font=('Agency FB', 30, 'bold')).pack(fill='both',expand='no')

		label02=Label(root,image=icon01).pack(fill='both',expand='no')

		clock=Label(root,background="#F0F0F0",font=('FFF Tusj', 25,'bold'),fg='deepSkyBlue')
		clock.pack()

		btn=Button(root,image=icon02,command=self.clickedbtn).pack(side='bottom',fill='both',expand='no')



		
		speak("Hello Master , Iam JARVIS")
		speak("What Should I Do For You.....")


		getTime()
		root.mainloop()

	def clickedbtn(self):
		global query
		query1=myCommand()
		query1=query1.lower()

		google_searches_dict = {'what': 'what', 'why': 'why', 'who': 'who', 'which': 'which','how':'how'}

		def is_valid_search(phrase):
			if(google_searches_dict.get(phrase.split(' ')[0])==phrase.split(' ')[0]):
				return True

		if 'open youtube' in query1:
			speak("Ok Master")
			webbrowser.open("www.youtube.com")
		elif 'password' in query1:
			speak("Ok Master")
			speak("Here is Your Saved Connected Wifi Password")
			Collect_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
			Collect_profiles = [i.split(":")[1][1:-1] for i in Collect_data if "All User Profile" in i]
			for i in Collect_profiles:
				results=subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
				results=[b.split(":")[1][1:-1] for b in results if "Key Content" in b]
				try:
					print("Wifi name: {:<20}|  Password: {:<}".format(i, results[0]))
				except:
					print("Wifi name: {:<20}|  Password:  {:<}".format(i, ""))
		elif 'say' in query1:
			speak("Hello Viewer, Iam JARVIS, Please Make Sure to Subscribe this Channel, And Must Hit The Bell ICON,  Stay Safe Viewer")
		elif 'play music' in query1:
			os.startfile('E:\\Audio Song\\The Software Engineer Song(MP3_160K).mp3')
			speak("Here is Your Music, ENJOY!")
		elif 'location' in query1:
			res = requests.get('https://ipinfo.io/')
			data = res.json()

			city = data['city']

			location = data['loc'].split(',')
			latitude = location[0]
			longitude = location[1]
			address=data['country']

			print("Latitude value :", latitude)
			speak("Latitude value is {}".format(latitude))
			print("Longitude value: ", longitude)
			speak("Longitude value is {}".format(longitude))
			print("Captial City : ", city)
			speak("Captial City Name is {}".format(city))
			print("Country :",address)
			speak("Country name is {}".format(address))
		elif is_valid_search(query1):
			speak("In Opening Searching Google..")
			taburl="http://google.com/?#q="
			question=query1
			webbrowser.open(taburl+question)
		elif 'download' in query1:
			speak("Paste Your Youtube Video Link: ")
			url=input("Paste Your Youtube Video Link: ")
			url=str(url)
			path_to_save=askdirectory()
			if path_to_save is None:
				return
			obj=Youtube(url)
			strm=obj.streams.first()
			strm.download(path_to_save)
			print("Done...")
			showinfo("Download Finished","Download SuccessFull")
			speak("Download Finished","Download SuccessFull")
		elif 'scanner' in query1:
			speak("In Opening Web Camera...")
			video=cv2.VideoCapture(0)
			while True:
				ret,frame=video.read()
				decodeObj=pyz.decode(frame)
				for obj in decodeObj:
					print(obj.data)
				cv2.imshow("Frame",frame)
				k=cv2.waitKey(1)
				if k==ord('q'):
					break
			video.release()
			cv2.destroyAllWindows()
		elif 'face' in query1:
			speak("In Opening Web Camera...")
			faceDected=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
			video=cv2.VideoCapture(0)
			while True:
				ret,frame=video.read()
				faces=faceDected.detectMultiScale(frame, 1.3,5)
				for x,y,w,h in faces:
					cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
				cv2.imshow("Frame", frame)
				k=cv2.waitKey(1)
				if k==ord('q'):
					break
			video.release()
			cv2.destroyAllWindows()




if __name__ == '__main__':
    greetMe()
    widget = Widget() 
    speak("Bye Sir, Stay Safe")       