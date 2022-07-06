from dataclasses import dataclass


@dataclass()
class WeaponData:
    title: str = None
    icon: str = None
    rarity: int = None
    damage: int = None
    dest: str = None
