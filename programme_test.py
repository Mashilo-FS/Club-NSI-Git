from time import sleep

me = {
    "name": "Lucas",
    "age": 16,
    "class": "Terminale"
}

def birthday(person: dict):
    name = person["name"]
    print(f"Bon anniversaire { name } !")
    person["age"] += 1
    age = person["age"]
    print(f"Tu as maintenant { age } ans !")

def morning(person: dict, reminder_time: int):
    name = person["name"]
    print(f"{ name }, debout ! C'est pas comme ça que tu deviendra le roi des pirates")
    sleep(reminder_time)
    print("LEVE-TOI J'AI DIT !")

if __name__ == "__main__":
    print("Fichier Principal")
    birthday(me)