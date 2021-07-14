# RannLabs2
In this project we are going to learn how to download youtube videos manually and automatically. For downloading the video automatically we are going to give a post request to the API which will help us to download the video without entering any youtube link.


At first we will look how to download a youtube video manually. We will be needing a few libraries, first one is pytube which will help us to download youtube videos and the second one is tkinter it will help us to make a GUI in which we will provide the youtube video link and the path. You can see the code named as rannlabs2.py. You can aslo check the output of this code(output.png).


After downloading a video manually, now it's time to download it automatically, but before that we have to give a post request to the API in order to get the youtube video name and the youtube video link in order to download it and for that we need to import request library. The code for the post request is given in main.py. In the output we are going to get the name and link of the youtube video. In output2.png you can see the outcome.


After the post request we have to download the video automatically without providing the video link everytime. We need to import tkinter.ttk as ttk and pafy. tkinter.tkk will be used to show a progressbar on the GUI and pafy will help us to get the size of the video. The output is given in output3(a) and output3(b) where you can see the size of the video and the GUI for automatically downloading the video respectively
