import io
import sys
from person import Person

class Logger(object):
    def __init__(self, file_name):
        self.file_name = None

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num):
        pass
    def log_infection_survival(self, person, did_die_from_infection):
        pass
    def log_time_step(self, time_step_number):
        pass
    
