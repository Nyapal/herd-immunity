import pytest

from person import Person
from virus import Virus

def test_person_instance():
    person = Person(420, False, None)
    assert person._id == 420
    assert person.is_vaccinated is False
    assert person.is_alive is True
    assert person.infection is None

def test_did_survive_infection():
    virus = Virus('Ebola', 0.70, 0.25)
    person = Person(420, False, None)
    assert person.is_alive is True
    assert person.is_vaccinated is False
    assert person.infection is virus

    if person.did_survive_infection():
        assert person.infection is None
        assert person.is_vaccinated is True
        assert person.is_alive is True
    else:
        assert person.is_alive is False
