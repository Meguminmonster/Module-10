from typing import Dict, List


def artifact_sorter(artifacts: List[Dict]) -> List[Dict]:
    return sorted(artifacts, key=lambda a: a["power"], reverse=True)


def power_filter(mages: List[Dict], min_power: int) -> List[Dict]:
    return list(filter(lambda m: m["power"] >= min_power, mages))


def spell_transformer(spells: List[str]) -> List[str]:
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: List[Dict]) -> Dict:
    max_power = max(mages, key=lambda m: m["power"])["power"]
    min_power = min(mages, key=lambda m: m["power"])["power"]
    avg_power = round(sum(map(lambda m: m["power"], mages)) / len(mages), 2)

    return {"max": max_power, "min": min_power, "avg": avg_power}


if __name__ == "__main__":
    print("\nTesting artifact sorter...")
    artifacts = [
        {"name": "Fire Staff", "power": 92, "type": "staff"},
        {"name": "Crystal Orb", "power": 85, "type": "orb"},
    ]
    sorted_artifacts = artifact_sorter(artifacts)
    print(
        f"{sorted_artifacts[0]['name']} "
        f"({sorted_artifacts[0]['power']} power) comes before "
        f"{sorted_artifacts[1]['name']} "
        f"({sorted_artifacts[1]['power']} power)"
    )

    print("\nTesting spell transformer...")
    spells = ["fireball", "heal", "shield"]
    print(" ".join(spell_transformer(spells)))

    print("\nTesting power filter...")
    mages = [
        {"name": "Jordan", "power": 98},
        {"name": "Kai", "power": 62},
        {"name": "Alex", "power": 93},
        {"name": "Luna", "power": 87},
        {"name": "Sage", "power": 53},
    ]
    filter = power_filter(mages, 80)
    print(f"{filter}")

    print("\nTesting mage stats...")
    stats = mage_stats(mages)
    print(f"{stats}")
