import abc

from ex0.creatures import Aquabub, Creature, Flameling, Pyrodon, Torragon


class CreatureFactory(abc.ABC):
    """Abstract factory: creates a base and an evolved Creature."""

    @abc.abstractmethod
    def create_base(self) -> Creature:
        raise NotImplementedError

    @abc.abstractmethod
    def create_evolved(self) -> Creature:
        raise NotImplementedError


class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Flameling()

    def create_evolved(self) -> Creature:
        return Pyrodon()


class AquaFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Aquabub()

    def create_evolved(self) -> Creature:
        return Torragon()
