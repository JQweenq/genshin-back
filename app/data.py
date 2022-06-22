from dataclasses import dataclass


@dataclass()
class UserData:
    username: str
    password: str
    email: str
    is_admin: bool


@dataclass()
class CharacterData:
    name: str
    rarity: int
    name_en: str
    full_name: str
    card: str
    weapon: str
    eye: str
    sex: str
    birthday: str
    region: str
    affiliation: str
    portrait: str
    description: str


@dataclass()
class WordData:
    word: str
    translate: str
    subinf: str
    original: str


@dataclass()
class WishData:
    title: str
    version: str
    poster: str
    rate_5: str
    rate_4: str


@dataclass()
class WeaponData:
    title: str
    icon: str
    rarity: int
    damage: int
    dest: str
