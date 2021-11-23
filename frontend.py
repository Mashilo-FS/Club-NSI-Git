def front_birthday(person: dict):
    name = person["name"]
    print(f"Bon anniversaire { name } !")
    age = person["age"]
    print(f"Tu as maintenant { age } ans !")

def front_morning(person: dict):
    name = person["name"]
    print(f"{ name }, debout ! C'est pas comme ça que tu deviendra le roi des pirates")
    
def front_morning_reminder():
    print("LEVE-TOI J'AI DIT !")