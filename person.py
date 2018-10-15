class Person(object):
    def __init__(self, _id, is_vaccinated, infected=None):
        self._id = _id
        self.is_vaccinated = is_vaccinated
        self.is_alive = True
        self.infected = infected

    def did_survive_infection(self):
        if self.infected != None:
            num = random.uniform(0,1)
            if num < self.infected.mortality_rate:
                self.is_alive = False
                return False
            else:
                self.is_vaccinated = True
                self.infected = None
                self.is_alive = True
                return True
