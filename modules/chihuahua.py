from modules.dog import Dog

class Chihuahua(Dog):
    def __init__(self, name, age, likes_walks=True):
        super().__init__(name, age, likes_walks)
    
    # Overridem method
    def bark(self):
        return "arf arf!!"