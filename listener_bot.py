# Python program to work as per audio command

# it is a jarvis kind of bot which listen to your command and works on specific commands doesnt work with everything you say
# but this definitely give it a shot kind of project

#used selenium driver for web scrapping

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import speech_recognition as sr
import pyttsx3
import time
import os

# Initialize the recognizer
r = sr.Recognizer()

# Function to convert text to
# speech
def SpeakText(command):
	
	# Initialize the engine
	engine = pyttsx3.init()
	engine.say(command)
	engine.runAndWait()
	
	
# Loop infinitely for user to
# speak
options=Options()
options.binary_location="C:\Program Files\Google\Chrome\Application\chrome.exe"

browser = webdriver.Chrome(chrome_options=options,executable_path="C:\\Users\\choud\\chromedriver.exe")
while(1):	
	
	# Exception handling to handle
	# exceptions at the runtime
	try:
		# use the microphone as source for input.
		with sr.Microphone() as source2:
			# wait for a second to let the recognizer
			# adjust the energy threshold based on
			# the surrounding noise level
			r.adjust_for_ambient_noise(source2, duration=0.2)
			SpeakText("Say now")	
			#listens for the user's input
			audio2 = r.listen(source2)
			
			# Using ggogle to recognize audio
			MyText = r.recognize_google(audio2,language="en-In")
			MyText = MyText.lower()

			print("Did you say "+MyText)
			SpeakText(MyText)	
		if MyText=="open instagram":
			browser = webdriver.Chrome()
			browser.get("https://www.instagram.com/")
			time.sleep(2)
			# creating a sleep timer to allow initializing the browser
			username = browser.find_element_by_name("username")
			#("_2hvTZ pexuQ zyHYP")
			username.send_keys("choudhary_manu_prakash")
			password = browser.find_element_by_name("password") #enter your password here
			password.send_keys("")
			browser.find_element_by_xpath("//button[@class='sqdOP  L3NKy   y3zKF     ']").click()
			time.sleep(6)
			browser.find_element_by_xpath("//button[@class='sqdOP yWX7d    y3zKF     ']").click()
			#its class is 				   //buton[@class='sqdOP yWX7d    y3zKF     ']

		elif MyText=="open youtube":
			browser.execute_script('''window.open("https://www.youtube.com/","_blank");''')
		elif MyText=="open spotify":
			os.system("C:/Users/choud/AppData/Roaming/Spotify/Spotify.exe")
		elif MyText=="play songs":
			browser.execute_script('''window.open("https://www.youtube.com/watch?v=wyQg8bBIwLE&list=RDMMwyQg8bBIwLE&start_radio=1","_blank");''')
		elif MyText=="open chrome":
			os.system("C:/Users/Public/Desktop/GoogleChrome.lnk")
		elif MyText=="stop":
			break
		time.sleep(4)
	except sr.RequestError as e:
		print("Could not request results; {0}".format(e))
		
	except sr.UnknownValueError:
		print("unknown error occured")
	
