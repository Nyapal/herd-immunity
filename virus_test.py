import pytest

from person import Person
from virus import Virus

def test_virus_instance():
    ebola = Virus('Ebola', 0.70, 0.25)
    assert ebola.name == 'Ebola'
    assert ebola.mortality_rate == 0.70
    assert ebola.repro_rate == 0.25
