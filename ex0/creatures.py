import abc


class Creature(abc.ABC):
    """"Abstract base for all creatures."""

    def __init__(self, name: str, creature_type: str) -> None:
        self._name = name
        self._type = creature_type

    @property
    def name(self) -> str:
        return self._name

    @property
    def type(self) -> str:
        return self._type

    @abc.abstractmethod
    def attack(self) -> str:
        raise NotImplementedError

    def describe(self) -> str:
        return (f"{self._name} is a {self._type} type Creature")

    class Flameling(Creature):
        def __init__(self) -> None:
            super().__init__("Flameling", "Fire")

        def attack(self) -> str:
            return (f"{self._name} uses Ember!")


    class Pyrodon(Creature):
        def __init__