from typing import Callable, List


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(*args, **kwargs):
        return spell1(*args, **kwargs), spell2(*args, **kwargs)

    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(*args, **kwargs):
        return base_spell(*args, **kwargs) * multiplier

    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def caster(*args, **kwargs):
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        else:
            return "Spell fizzled"

    return caster


def spell_sequence(spells: List[Callable]) -> Callable:
    def sequence(*args, **kwargs):
        return [spell(*args, **kwargs) for spell in spells]

    return sequence


if __name__ == "__main__":
    print("\nTesting spell combiner...")

    def fireball(target):
        return f"Fireball burns {target}"

    def heal(target):
        return f"All {target} injuries dissapear"

    combined = spell_combiner(fireball, heal)
    print("Combined spell result:", ", ".join(combined("Dragon")))

    print("\nTesting power amplifier...")

    def base(x):
        return x

    mega = power_amplifier(base, 3)
    print("Original:", base(10), "Amplified:", mega(10))

    print("\nTesting conditional caster...")

    def coin_rain(x):
        return f"Coins starts to rain {x}"

    def condition(bool):
        return True

    caster = conditional_caster(condition, coin_rain)
    print(caster(""))

    print("\nTesting spell sequence...")

    def revive(target):
        return f"{target} returns from death"

    def ice(target):
        return f"{target} gets headshoted with an ice bullet"

    my_spells = [fireball, ice, revive, heal]

    sequence = spell_sequence(my_spells)
    results = sequence("Goblin")
    print("Sequence:", results)
