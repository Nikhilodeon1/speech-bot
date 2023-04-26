from pygame import mixer
import time
mixer.init() #Initialzing pyamge mixer

mixer.music.load('thatfile.mp3') #Loading Music File

mixer.music.play() #Playing Music with Pygame

time.sleep(5)


mixer.music.stop()