from ex0.factories import AquaFactory, FlameFactory, CreatureFactory
from ex1.factories import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    AggressiveStrategy,
    BattleStrategy,
    DefensiveStrategy,
    InvalidStrategyError,
    NormalStrategy,
)

Opponent = tuple[CreatureFactory, BattleStrategy]

FACTORY_LABELS = {
    FlameFactory: "Flameling",
    AquaFactory: "Aquabub",
    HealingCreatureFactory: "Healing",
    TransformCreatureFactory: "Transform",
}


def opponent_label(factory: CreatureFactory, strategy: BattleStrategy) -> str:
    factory_label = FACTORY_LABELS[type(factory)]
    strategy_label = type(strategy).__name__.replace("Strategy", "")
    return (f"{factory_label}+{strategy_label}")


def battle(opponents: list[Opponent]) -> None:
    """make every opponent fight every other opponent once."""
    fighters = [
        (factory.create_base(), strategy) for factory, strategy in opponents
    ]

    for i in range(len(fighters)):
        for j in range(i + 1, len(fighters)):
            creature_a, strategy_a = fighters[i]
            creature_b, strategy_b = fighters[j]

            print("* Battle *")
            print(creature_a.describe())
            print(" vs.")
            print(creature_b.describe())
            print(" now fight!")

            for line in strategy_a.act(creature_a):
                print(line)
            for line in strategy_b.act(creature_b):
                print(line)
            print()


def run_tournament(label: str, opponents: list[Opponent]) -> None:
    print(f"Tournament {label}")
    summary = ", ".join(
        f"({opponent_label(factory, strategy)})"
        for factory, strategy in opponents
    )
    print(f" [ {summary} ]")
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    print()

    try:
        battle(opponents)
    except InvalidStrategyError as exc:
        print(f"Battle error, aborting tournament: {exc}")
        print()


def main() -> None:
    tournament_0: list[Opponent] = [
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
    ]
    run_tournament("0 (basic)", tournament_0)

    tournament_1: list[Opponent] = [
        (FlameFactory(), AggressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
    ]
    run_tournament("1 (error)", tournament_1)

    tournament_2: list[Opponent] = [
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy()),
    ]
    run_tournament("2 (multiple)", tournament_2)


if __name__ == "__main__":
    main()
