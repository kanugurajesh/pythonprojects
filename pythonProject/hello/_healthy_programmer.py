# hello this is a code we are going to program
input()
import datetime
from time import time

def datetimes():
    return datetime.datetime.now()

from pygame import mixer
def musicplayer(music,stopper):
    mixer.init()
    mixer.music.load(music)
    mixer.music.play()
    while True:
        input_of_user = input("sir please enter the input: ")
        if input_of_user == "q":
            print("program is quitted")
            break
        elif input_of_user == "r":
            print("program is resumed")
            mixer.music.play()
        elif input_of_user == "p":
            print("program is paused")
            mixer.music.pause()
        elif input_of_user == stopper:
            break
    exporter(input_of_user,f"{datetimes()}\n")

def exporter(msg,time):
    with open("module_of_time","a") as s:
        s.write(f"the message is {msg} and time is {time}")

if __name__ == "__main__":
    water_interval = 10
    eyes_excercise = 20
    physical_excercise = 30
    current_water = time()
    current_eyes_excercise = time()
    current_physical_excercise = time()

while True:
    if time() - current_water >water_interval:
        musicplayer("water.mp3.mp3","drank")
        current_water = time()
        print("you drank water")
    elif time() - current_eyes_excercise > eyes_excercise:
        musicplayer("eyeblink.mp3.mp3","eyesdon")
        print("you have done eyes excercise")
        current_eyes_excercise = time()
    elif time() - current_physical_excercise > physical_excercise:
        musicplayer("excercise.mp3.mp3","physical excercise done")
        current_physical_excercise = time()
        print("you have done physical excercises")

# if you have logic programming can be done