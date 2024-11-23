from modules.dog import Dog

class GoldenRetriever(Dog):
    def __init__(self, name, age, likes_walks=True):
        super().__init__(name, age, likes_walks)
    
    # Overriden method
    def bark(self):
        return "WOOOOOF!"