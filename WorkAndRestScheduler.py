#!/usr/bin/env python
# coding: utf-8


import time

import os

import subprocess as s

import webbrowser

import sys

import subprocess

from gtts import gTTS

import pyttsx3

import pandas as pd

import numpy as np

import pyforest

from pydub import AudioSegment

from pydub.playback import play



# Wait 30 seconds for bootup of system and Python to get ready to run the script
time.sleep(15)



def send_notification_and_sound(primary_text = 'Great' , secondary_text = 'job'):
   
   '''
   
   This function send notification and read notification to user
   
   '''
   
   s.call(['notify-send', primary_text , secondary_text])
   os.system('echo "{}" | festival --tts '.format(primary_text))


def browser_auto_open():
    
    '''
    
    This function open browsers with the URLs I mostly use , thus saving more time for me
    
    '''


    url_list_window1 = ['https://drive.google.com/drive/my-drive' , 
           'https://keep.google.com/u/0/' , 
           'https://asoftmurmur.com/?lang=en']


    url_list_window2 = ['https://wipro.udemy.com/organization/home/' , 
                    'https://www.hackerrank.com/dashboard'
                   ]


    for link in url_list_window1:
        webbrowser.open_new_tab(link)

    webbrowser.open_new('')

    for link in url_list_window2:
        webbrowser.open_new_tab(link)



def launch_jupyter_lab(): 
    
    '''
    
    This function launches jupyter lab
    
    '''
    
    openJupyter = "jupyter-lab"
    subprocess.Popen(openJupyter, shell=True)



def wait_30_minutes():
    
    '''
    
    This function makes the control wait for 30 minutes , 
    I use this in program to schedule a notification every 30 mins
    
    '''
    
    
    time.sleep(1800)



def play_rest_music():
    
    '''
    
    This function plays my rest music in the 20 minutes when I take the rest
    
    '''
    
    music = AudioSegment.from_mp3('/home/deku/Documents/AutomationProjects/WorkAndRestSchedulerProject/mario.mp3')
    play(music)


launch_jupyter_lab()
time.sleep(13)

df = pd.read_csv('/home/deku/Documents/AutomationProjects/WorkAndRestSchedulerProject/quotes.csv')



list_of_motivation_quotes = list(df.Quote)




#launch_jupyter_lab()
#time.sleep(5)



browser_auto_open()



while True:
    
    '''
    
    This while loop implement the core logic of my work pattern , 
    90 minutes work (Notified in the time frame by notifications) 
    and
    20 minutes rest (Program will play my rest music so I will feel refreshed)
    
    '''
    
    send_notification_and_sound(primary_text='Work Time Started' , secondary_text= 'keep going Champ')
    for i in range(3):
        wait_30_minutes()
        send_notification_and_sound(primary_text= np.random.choice(list_of_motivation_quotes) , 
                                   secondary_text= 'Another 30 Minutes successfully invested in great work , Keep it up')
    time.sleep(3)
        
    send_notification_and_sound(primary_text='Enjoy 20 minutes Rest' , secondary_text= 'Enjoyyy')
    
    for i in range(16):
        play_rest_music()
        time.sleep(3)
        
    send_notification_and_sound(primary_text = 'Get ready for hustling' , secondary_text = 'Come on Buddy , You can do it')
    
    time.sleep(10)
    
    music = AudioSegment.from_mp3('wake_up.mp3')
    play(music)
    
    send_notification_and_sound(primary_text= '3 2 1 GO' , secondary_text = 'Welcome Back Champ')

