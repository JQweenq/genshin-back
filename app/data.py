from dataclasses import dataclass


@dataclass()
class UserData:
    username: str
    password: str
    email: str
    is_admin: bool


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
