import random, sys
random.seed(42)

from person import Person
from logger import Logger
from virus import Virus

class Simulation(object)
    def __init__(self, population_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num, initial_infected=1):
        self.population_size = population_size
        self.vacc_percentage = vacc_percentage
        self.virus_name = virus_name
        self.mortality_rate = mortality_rate
        self.basic_repro_num = basic_repro_num
        self.population = []
        self.total_infected = 0
        self.current_infected = 0
        self.next_person_id = 0
        self.virus = virus
        self.file_name = "{}_simulation_pop_{}_vp_{}_infected_{}.txt".format(
            virus_name, population_size, vacc_percentage, initial_infected)
        self.logger = Logger(self.file_name)
        self.newly_infected = []
        self.population = self._create_population(initial_infected)

    def _create_population(self, initial_infected):
        population = []
        infected_count = 0
        while len(population) != self.population_size:
            if infected_count != initial_infected:
                infected_person = Person(self.next_person_id, is_vaccinated=False, infection=self.virus)
                self.population.append(infected_person)
                infected_count += 1
                self.next_person_id += 1
            else:
                rand_num = random.uniform(0,1)
                if rand_num < self.vacc_percentage:
                    vacc_person = Person(self.next_person_id, is_vaccinated=True, infection=None)
                    population.append(vacc_person)
                    self.next_person_id += 1
                else:
                    nonvacc_person = Person(self.next_person_id, is_vaccinated=False, infection=None)
                    population.append(nonvacc_person)
                    self.next_person_id += 1

    def _simulation_should_continue(self):
        num_dead = 0
        num_infected = 0


        for person in self.population:
            if person.infection == True:
                num_infected += 1

        for person in self.population:
            if person.is_alive == False:
                num_dead += 1


        if num_dead == len(self.population) or infected_count == 0:
            return False
        else:
            return True


    def run(self):
        time_step_counter = 0
        should_continue = self._simulation_should_continue()
        while should_continue:
            self.time_step()
            log_time_step(time_step_counter)
            time_step_counter += 1
            should_continue = self._simulation_should_continue()

    def time_step(self):


    def interaction(self, person, random_person):


    def _infect_newly_infected(self):


if __name__ == "__main__":
    params = sys.argv[1:]
    pop_size = int(params[0])
    vacc_percentage = float(params[1])
    virus_name = str(params[2])
    mortality_rate = float(params[3])
    basic_repro_num = float(params[4])
    if len(params) == 6:
        initial_infected = int(params[5])
    else:
        initial_infected = 1
    simulation = Simulation(pop_size, vacc_percentage, virus_name, mortality_rate,
                            basic_repro_num, initial_infected)
    simulation.run()
