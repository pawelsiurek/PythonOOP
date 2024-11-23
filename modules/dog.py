# Parents class to GoldenRetriever and Chihuahua classes
class Dog:
    def __init__(self, name, age, likes_walks=True):
        self.name =        name
        self.age =         age
        self.likes_walks = likes_walks
    
    def bark(self):
        return "Woof!"