import abc
from typing import Optional


class HealCapability(abc.ABC):
    """Abstract capability can heal. Does not inherit from Creature."""
    @abc.abstractmethod
    def heal(self, target: Optional[str] = None) -> str:
        raise NotImplementedError


class TransformCapability(abc.ABC):
    """ Abstract capability: can transform and revert.

    Holds persistent state ('_transformed') that impacts how a
    Creature using this capabiity attacks.
    """
    def __init__(self) -> None:
        self._transformed = False

    @abc.abstractmethod
    def transform(self) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    def revert(self) -> str:
        raise NotImplementedError
