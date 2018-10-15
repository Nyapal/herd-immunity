import random

class Person(object):
    def __init__(self, _id, is_vaccinated, infection=None):
        self._id = _id
        self.is_vaccinated = is_vaccinated
        self.is_alive = True
        self.infection = infection

    def did_survive_infection(self):
        if self.infection != None:
            num = random.uniform(0,1)
            if num < self.infection.mortality_rate:
                self.is_alive = False
                return False
            else:
                self.is_vaccinated = True
                self.infection = None
                self.is_alive = True
                return True
