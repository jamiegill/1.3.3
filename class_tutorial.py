class Bassist(object):
    def __init__(self):
        self.sounds = ["Twang", "Thrumb", "Bling"]

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=" ")
        print()

class Guitarist(object):
    def __init__(self):
        self.sounds = ["Boink", "Bow", "Boom"]

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=" ")
        print()

    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")
