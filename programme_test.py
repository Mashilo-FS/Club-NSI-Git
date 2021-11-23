from time import sleep
from backend import *
from frontend import *


def birthday(person: dict):
    if back_makeBirthday(person):
        front_birthday(person)
    

def morning(person: dict, reminder_time: int):
    front_morning(person)
    sleep(reminder_time)

if __name__ == "__main__":
    print("Fichier Principal")
    birthday(me)
    # Le lundi !!!
    morning(me, 3)