from abc import ABC, abstractmethod
import typing


class Creature(ABC):
    def __init__(self, name: str, type: str) -> None:
        self.name = name
        self.type = type

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> None:
        return (f"{self.name}is a {self.type} type crea")
    