import abc
from typing import List

from ex0.creatures import Creature
from ex1.capabilities import HealCapability, TransformCapability


class InvalidStrategyError(Exception):
    """raised when BattleStrategy is aplied to an unfit Creature."""

    def __init__(self, creature_name: str, strategy_label: str) -> None:
        self.creature_name = creature_name
        self.strategy_label = strategy_label
        message = (
            f"Invalid Creature '{creature_name}'"
            f"for this {strategy_label} strategy"
        )
        super().__init__(message)


class BattleStrategy(abc.ABC):
    """Abstract strategy: a sequence of moves a Creature performs"""

    @abc.abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        raise NotImplementedError

    @abc.abstractmethod
    def act(self, creature: Creature) -> List[str]:
        raise NotImplementedError


class NormalStrategy(BattleStrategy):
    """Suitable for any Creature: Just attack"""
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> List[str]:
        if not self.is_valid(creature):
            raise InvalidStrategyError(creature.name, "normal")
        return [creature.attack()]


class AggressiveStrategy(BattleStrategy):
    """suitable for Creatures with TransformCapability:
    transform, attack, revert."""
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> List[str]:
        if not isinstance(creature, TransformCapability):
            raise InvalidStrategyError(creature.name, "aggressive")
        return [
            creature.transform(),
            creature.attack(),
            creature.revert(),
        ]


class DefensiveStrategy(BattleStrategy):
    """Suitable for Creatures with HealCapability: attack, then heal."""
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> List[str]:
        if not isinstance(creature, HealCapability):
            raise InvalidStrategyError(creature.name, "defensive")
        return [
            creature.attack(),
            creature.heal(),
        ]
