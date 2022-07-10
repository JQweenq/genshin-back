from dataclasses import dataclass


@dataclass()
class WeaponData:
    title: str = None
    title_en: str = None
    icon: str = None
    rarity: int = None
    damage: int = None
    dest: str = None
