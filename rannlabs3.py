import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog
import requests
import pafy


from pytube.cli import on_progress
# Creating object of tk class
root = tk.Tk()
# Setting the title, background color
# and size of the tkinter window and
# disabling the resizing property
root.geometry("810x220")
root.resizable(True, True)
root.title("YouTube_Video_Downloader")
root.config(background="#000000")
# Creating the tkinter Variables
link = StringVar()
video_link = StringVar()
download_Path = StringVar()
# api-endpoint
URL = "http://smartgsc.rannlabprojects.com/api/CMS/SearchAdvertisement"
# defining a params dict for the parameters to be sent to the API
PARAMS = {
    "Gender": "All",
    "MacAddress": "b8:27:eb:45:c7:21",
    "Location": "",
    "Business": "",
    "Age": ""
}
# sending get request and saving the response as response object
r = requests.post(url=URL, params=PARAMS)
# extracting data in json format
# data = r.json()
data_test = {"ID": 101, "VideoUrl": "https://www.youtube.com/watch?v=KHMTn9Az92w"}
video_name = str(data_test["ID"])
video_link = str(data_test["VideoUrl"])
print("The api video name is: %s" % video_name, "The video link is: %s" % video_link)
# Defining Widgets() function
# to create necessary tkinter widgets
def Widgets():
    body_label = Label(root,
                       text="{Manually} : Please enter a video_link if you wanna download a YouTube video",
                       bg="#FFFFFF")
    body_label.grid(row=1,
                    column=1,
                    pady=5,
                    padx=5)
    body_label = Label(root,
                       text="{Automatically} : Or just ignore this step to download a youtube video using api requests",
                       bg="#FFFFFF")
    body_label.grid(row=2,
                    column=1,
                    pady=5,
                    padx=5)
    link_label = Label(root,
                       text="YouTube link  :",
                       bg="#FFFFFF")
    link_label.grid(row=3,
                    column=0,
                    pady=5,
                    padx=5)
    root.linkText = Entry(root,
                          width=60,
                          textvariable=link)
    root.linkText.grid(row=3,
                       column=1,
                       pady=5,
                       padx=5,
                       )
    destination_label = Label(root,
                              text="Destination    :",
                              bg="#FFFFFF")
    destination_label.grid(row=4,
                           column=0,
                           pady=5,
                           padx=5)
    root.destinationText = Entry(root,
                                 width=60,
                                 textvariable=download_Path)
    root.destinationText.grid(row=4,
                              column=1,
                              pady=5,
                              padx=5)
    browse_B = Button(root,
                      text="Browse",
                      command=Browse,
                      width=10,
                      bg="#05E8E0")
    browse_B.grid(row=4,
                  column=2,
                  pady=1,
                  padx=1)
    progressbar = ttk.Progressbar(root, orient="horizontal", length=300, mode='determinate',maximum=100,value=1)
    progressbar.grid(row=6,
                    column=1,
                    pady=6,
                    padx=6)
    Download_B = Button(root,
                        text="Download",
                        command=Download,
                        width=20,
                        bg="#05E8E0")
    Download_B.grid(row=5,
                    column=1,
                    pady=3,
                    padx=3)
# Defining Browse() to select a
# destination folder to save the video
def Browse():
    # Presenting user with a pop-up for
    # directory selection. initialdir
    # argument is optional Retrieving the
    # user-input destination directory and
    # storing it in downloadDirectory
    download_Directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH")
    # Displaying the directory in the directory
    # textbox
    download_Path.set(download_Directory)
def progress_function(self, size, stream, chunk, file_handle=None, bytes_remaining=None):
    p = 0
    while p < 100:
        progressbar['value'] = p
        progressbar.start(p)
        root.update_idletasks()
        p = percent(bytes_remaining, size)
    progressbar.finish()
def percent(self, tem, total):
        perc = ((1-(float(tem) / float(total))) * float(100))
        return perc

video=pafy.new(video_link)

video = pafy.new(video_link)

# getting all the available streams
streams = video.allstreams

# selecting one stream
stream = streams[4]

# getting file size of stream
value = stream.get_filesize()

# printing the value
print("File Size in bytes: " + str(value))

# Defining Download() to download the video
def Download():
    # check if link.get()#"" if true then update youtube_link and video_name
    # note that when video_name==None by dnefault the video will take the title name from youtube
  if (str(link.get()) != ""):
        youtube_link = str(link.get())
        youtube_video_name = None
# if link.get()=="" then just download the video_link from dictionary data_test, the video will be named video_name
  else:
        youtube_link = video_link
        youtube_video_name = video_name
# Download the youtube video haping video_link
  if (youtube_link != ""):
        # select the optimal location for
        # saving file's
        download_Folder = download_Path.get()
        # Creating object of YouTube()
        getVideo = YouTube(youtube_link,on_progress_callback=progress_function)
        # Getting all the available streams of the
        # youtube video and selecting the first
        # from the
        videoStream = getVideo.streams.first()
        # Downloading the video to destination
        # directory
        videoStream.download(output_path=download_Folder, filename=youtube_video_name)
        # Displaying the message
        messagebox.showinfo("SUCCESSFULLY",
                            "DOWNLOADED AND SAVED IN\n"
                            + download_Folder)
# if there is no video_link then we show error message and we stop the function by doing return
  else:
        messagebox.showinfo("ERROR", "ENTER url ")
# Calling the Widgets() function
Widgets()
# Defining infinite loop to run
# application
root.mainloop()