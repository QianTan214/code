import random

target = "I love cs50"


class Phrase:
    def __init__(self):
        self.characters = []
        for i in range (len(target)):
            """ random printable characters in ASCII code,
                chr convert int to char"""
            character = chr(random.choice(range(32, 127)))
            self.characters.append(character)


    def getContents(self):
        """join a list of char into a string"""
        return "".join(self.characters)


    def getFitness(self):
        """this function doesn't return anything"""
        """set a new property in other functions other than in __init__ function"""
        self.fitness = 0 
        for i in range(len(self.characters)):
            if self.characters[i] == target[i]:
                self.fitness += 1
        

    def crossover(self, partner):
        child = Phrase()
        for i in range (len(self.characters)):
            if random.random() < 0.5: # random.random () returns a real value 0 - 1
                child.characters[i] == self.characters[i]
            else:
                child.characters[i] == partner.characters[i]
        
        return child


    def mutate(self):
        for i in range (len(self.characters)):
            if random.random() < 0.01: # mutation rate
                self.characters[i] == chr(random.choice(range(32, 127)))
