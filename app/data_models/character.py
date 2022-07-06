from dataclasses import dataclass


@dataclass()
class CharacterData:
    name: str = None
    rarity: int = None
    name_en: str = None
    full_name: str = None
    card: str = None
    weapon: str = None
    eye: str = None
    sex: str = None
    birthday: str = None
    region: str = None
    affiliation: str = None
    portrait: str = None
    description: str = None
