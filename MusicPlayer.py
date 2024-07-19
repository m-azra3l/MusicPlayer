# Import the necessary modules from the tkinter library
from pickle import FRAME
from tkinter import Tk, Frame, Button
from tkinter import filedialog, StringVar
from tkinter.ttk import Progressbar
from pygame import mixer
import os
from tkinter import *

# Create a new Tkinter window
root = Tk()
mixer.init()

# Set the window title
root.title("Music Player")

# Create a new frame to hold the buttons and progress bar
frame = Frame(root)

# Create a variable to hold the path of the currently playing song
song_path = StringVar()


# Create a function to select a song to play
def select_song():
  # Use the filedialog module to open a file selection window
  path = filedialog.askdirectory()
  if path:
    os.chdir(path)
    songs = os.listdir(path)

    for song in songs:
        if song.endswith(".mp3"):
            Playlist.insert(END, song)


# Create a function to play the selected song
def play_song():
    Music_Name= Playlist.get(ACTIVE)
    print(Music_Name[0:-4])
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()

# Create a function to pause the currently playing song
def pause_song():
  mixer.music.pause()	
  pass


# Create a function to stop the currently playing song
def stop_song():
  mixer.music.stop()	
  pass


# Create a button to select a song to play
select_button = Button(frame, text="Select Song", command=select_song)

# Create a button to play the selected song
play_button = Button(frame, text="Play", command=play_song)


# Create a button to stop the currently playing song
stop_button = Button(frame, text="Stop", command=stop_song)



Scroll = Scrollbar(frame)
Playlist = Listbox(frame, width=100, font=("Times new roman",10), bg="#333333", fg="grey", selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=Scroll.set)
Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT, fill=Y)
Playlist.pack(side=LEFT, fill=BOTH)

# Pack the buttons and progress bar into the frame
select_button.pack()
play_button.pack()
stop_button.pack()
frame.pack()

# Start the Tkinter main loop
root.mainloop()
