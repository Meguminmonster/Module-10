from functools import lru_cache, partial, reduce, singledispatch
from operator import add, mul
from typing import Callable, Dict, List


def spell_reducer(spells: List[int], operation: str) -> int:
    ops = {"add": add, "multiply": mul, "max": max, "min": min}
    return reduce(ops[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> Dict[str, Callable]:
    return {
        "fire_enchant": partial(base_enchantment, 50, "fire"),
        "ice_enchant": partial(base_enchantment, 50, "ice"),
        "lightning_enchant": partial(base_enchantment, 50, "lightning"),
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable:
    @singledispatch
    def cast(arg):
        return "Unknown spell type"

    @cast.register
    def _(arg: int):
        return f"Damage spell hits for {arg} power"

    @cast.register
    def _(arg: str):
        return f"Enchantment applied: {arg}"

    @cast.register
    def _(arg: list):
        return [cast(a) for a in arg]

    return cast


if __name__ == "__main__":
    print("\nTesting spell reducer...")
    print("Sum:", spell_reducer([10, 20, 30, 40], "add"))
    print("Product:", spell_reducer([10, 20, 30, 40], "multiply"))
    print("Max:", spell_reducer([10, 20, 30, 40], "max"))
    print("Min:", spell_reducer([10, 20, 30, 40], "min"))

    print("\nTesting memoized fibonacci...")
    print("Fib(10):", memoized_fibonacci(10))
    print("Fib(15):", memoized_fibonacci(15))

    print("\nTesting partial enchanter...")

    def base_enchant(power: int, element: str, item: str):
        return f"Enchanting {item} with {element} (Power: {power})"

    enchanters = partial_enchanter(base_enchant)
    print(enchanters["fire_enchant"]("Sword"))
    print(enchanters["ice_enchant"]("Shield"))
    print(enchanters["lightning_enchant"]("Staff"))

    print("\nTesting spell dispatcher...")
    cast = spell_dispatcher()

    print("Int cast:", cast(100))
    print("Str cast:", cast("Invisibility"))
    print("List cast:", cast([50, "Poison", 20]))
    print("Unknown cast:", cast(12.5))
