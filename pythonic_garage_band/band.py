
class Band:
    #instances = []
    def __init__(self,name,members):
        self.name = name
        self.members = members

    #def __str__(self):
    #def __repr__(self):

    def play_solos(self):
        pass
class  Musician:
    def __init__(self, name, type, instrument):
        self.name = name
        self.type = type
        self.instrument = instrument

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    #def __repr__(self):

    def get_instrument(self):
        return f"{self.instrument}"

    def play_solo(self):
        #needs to return a string
        pass
class Guitarist(Musician):
    def __init__(self, name):
        super().__init__(name, 'Guitarist', 'guitar')

    def __repr__(self):
        # return a string with how to reproduce the object
        return f'Guitarist instance. Name = {self.name}'

class Bassist(Musician):
    def __init__(self, name):
        super().__init__(name, 'Bassist', 'bass')

    def __repr__(self):
        # return a string with how to reproduce the object
        return f'Bassist instance. Name = {self.name}'

class Drummer(Musician):
    def __init__(self, name):
        super().__init__(name, 'Drummer', 'drums')

    def __repr__(self):
        # return a string with how to reproduce the object
        return f'Drummer instance. Name = {self.name}'