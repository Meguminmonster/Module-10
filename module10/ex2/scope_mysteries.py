from typing import Callable, Dict


def mage_counter() -> Callable:
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable:
    total = initial_power

    def accumulator(amount: int):
        nonlocal total
        total += amount
        return total

    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    return lambda item: f"{enchantment_type} {item}"


def memory_vault() -> Dict[str, Callable]:
    storage = {}

    def store(key, value):
        storage[key] = value

    def recall(key):
        return storage.get(key, "Memory not found")

    return {"store": store, "recall": recall}


if __name__ == "__main__":
    print("\nTesting mage counter...")
    counter = mage_counter()
    print("Call 1:", counter())
    print("Call 2:", counter())
    print("Call 3:", counter())

    print("\nTesting enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))

    print("\nTesting spell accumulator...")

    mana_pool = spell_accumulator(100)
    print("Base (100 + 50):", mana_pool(50))
    print("Accumulation (+ 25):", mana_pool(25))

    otro_pool = spell_accumulator(0)
    print("Another base:", otro_pool(10))

    print("\nTesting memory vault...")
    vault = memory_vault()

    vault["store"]("fireball", "A BIIIG fireball.")
    vault["store"]("blink", "Instant tp just like in dragon ball.")

    print("Restoring fireball:", vault["recall"]("fireball"))
    print("Restoring blink:", vault["recall"]("blink"))

    print("False spell:", vault["recall"]("avada_kedavra"))
