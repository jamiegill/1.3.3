class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=" ")
        print()

class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self):
        #Call the __init__ method of the parent class
        super().__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self):
        #Call the __init__ method of the parent class
        super().__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")

class Drummer(Musician):
    def __init__(self):
        super().__init__(["Snare", "Tom", "Kick", "Tat"])

    def count(self):
        for i in range(1, 5):
            print(i)
    
    def spontaneous_combust(self):
        print("Spontaneous combustion!!!")

class Band(object):
    def __init__(self):
        drummer = Drummer()
        drummer.count()
        guitarist = Guitarist()
        guitarist.solo(6)
        bassist = Bassist()
        bassist.solo(6)
        drummer.solo(6)
    def hire_fire(self):
        prompt = input("would you like to hire or fire? ")
        if "hire" in prompt:
            prompt = input("Who would you like to hire? ")
            print("{} hired".format(prompt))
        if "fire" in prompt:
            prompt = input("Who would you like to fire? ")
            print("{} fired".format(prompt))

