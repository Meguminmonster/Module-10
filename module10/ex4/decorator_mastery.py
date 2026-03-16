import random
import time
from functools import wraps
from typing import Callable


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Spell completed in {round(end - start, 3)} seconds")
        return result

    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            power = kwargs.get("power") or (args[1] if len(args) > 1 else None)

            if power is None or power < min_power:
                return f"Insufficient power (Required: {min_power})"
            return func(*args, **kwargs)

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt < max_attempts:
                        print(f"FAIL {e}. Retrying ({attempt}/{max_attempts})")
                    else:
                        return f"Casting failed after {max_attempts} attempts."

        return wrapper

    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name)

    @power_validator(10)
    def cast_spell(self, power: int, spell_name: str) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    guild = MageGuild()

    print("\nTesting Power Validator...")
    print(guild.cast_spell(power=5, spell_name="Spark"))
    print(guild.cast_spell(20, "Inferno"))

    print("\nTesting Retry Spell...")

    @retry_spell(max_attempts=3)
    def unstable_portal():
        if random.random() < 0.7:
            raise Exception("Mana turbulence detected!!")
        return "OMG YOU DID IT DUDE, Portal Opened!"

    print("Result:", unstable_portal())

    print("\nTesting mage name validation...")
    names = ["Gandalf", "Al", "Merlin 123", "Saruman the White"]
    for name in names:
        valid = guild.validate_mage_name(name)
        status = "Valid name:" if valid else "Invalid name:"
        print(f"{status} {name}")

  @spell_timer
        def fireball():
            time.sleep(0.1)
            return "Fireball cast!"

        print("Result:", fireball())

