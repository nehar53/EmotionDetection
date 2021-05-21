
from tkinter import *
import os
import sys
import vlc
from pathlib import Path
import random


Instance = vlc.Instance()

player = Instance.media_player_new()




class MusicPlayer(object):

  def __init__(self,root,emotionStr):
    self.root = root

    self.root.title("Music Player")

    self.root.geometry("1000x200+200+200")

    self.track = StringVar()

    self.status = StringVar()

    trackframe = LabelFrame(self.root,text="Song Track",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=GROOVE)
    trackframe.place(x=0,y=0,width=620,height=100)

    songtrack = Label(trackframe,textvariable=self.track,width=20,font=("times new roman",24,"bold"),bg="grey",fg="gold").grid(row=0,column=0,padx=10,pady=5)

    trackstatus = Label(trackframe,textvariable=self.status,font=("times new roman",18,"bold"),bg="grey",fg="gold").grid(row=0,column=1,padx=5,pady=5)

    buttonframe = LabelFrame(self.root,text="Control Panel",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=GROOVE)
    buttonframe.place(x=0,y=100,width=620,height=100)

    playbtn = Button(buttonframe,text="PLAY",command=self.playsong,width=6,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold").grid(row=0,column=0,padx=10,pady=5)

    playbtn = Button(buttonframe,text="PAUSE",command=self.pausesong,width=8,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold").grid(row=0,column=1,padx=10,pady=5)

    playbtn = Button(buttonframe,text="SHUFFLE",command=self.shufflesong,width=10,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold").grid(row=0,column=2,padx=10,pady=5)

    playbtn = Button(buttonframe,text="STOP",command=self.stopsong,width=6,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold").grid(row=0,column=3,padx=10,pady=5)
    playbtn = Button(buttonframe,text="NEXT",command=self.nextsong,width=6,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold").grid(row=0,column=4,padx=10,pady=5)

    songsframe = LabelFrame(self.root,text="Song Playlist",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=GROOVE)
    songsframe.place(x=600,y=0,width=400,height=200)

    scrol_y = Scrollbar(songsframe,orient=VERTICAL)

    self.playlist = Listbox(songsframe,yscrollcommand=scrol_y.set,selectbackground="gold",selectmode=SINGLE,font=("times new roman",12,"bold"),bg="silver",fg="navyblue",bd=5,relief=GROOVE)

    scrol_y.pack(side=RIGHT,fill=Y)
    scrol_y.config(command=self.playlist.yview)
    self.playlist.pack(fill=BOTH)

    os.chdir(str(Path(__file__).parent.absolute())+"\songs\\"+emotionStr+"\\")

    songtracks = os.listdir()
    self.songtracks = songtracks

    for track in songtracks:
      self.playlist.insert(END,track)
    if(player.is_playing() == 0):
      ranSong = random.choice(self.songtracks)
      self.pos = self.songtracks.index(ranSong)
      self.track.set(ranSong)
      self.status.set("-Playing "+emotionStr)
      Media = Instance.media_new(ranSong)
      player.set_media(Media)
      player.play()

  def playsong(self):

    self.track.set(self.playlist.get(ACTIVE))

    self.status.set("-Playing")

    Media = Instance.media_new(self.playlist.get(ACTIVE))
    player.set_media(Media)
    player.play()

  def stopsong(self):

    self.status.set("-Stopped")

    player.stop()
    self.root.destroy()
    os.chdir(str(Path(__file__).parent.absolute()))
    os.system("python emotions.py")


  def pausesong(self):

    self.status.set("-Paused")

    player.pause()


  def nextsong(self):
    i=0
    while i< len(self.songtracks):
      if i == self.pos:
        i = i+1
        if i >= len(self.songtracks):
          i= 0
        nsong = self.songtracks[i]
        self.pos = i
      i = i + 1
    player.stop()
    self.track.set(nsong)

    Media = Instance.media_new(nsong)
    player.set_media(Media)
    player.play()


  def shufflesong(self):
    self.status.set("-Shuffle Play")
    song2 =random.choice(self.songtracks)
    self.pos = self.songtracks.index(song2)
    player.stop()
    self.track.set(song2)

    Media = Instance.media_new(song2)
    player.set_media(Media)
    player.play()
      




