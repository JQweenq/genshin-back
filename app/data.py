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
    word: str = None
    translate: str = None
    subinf: str = None
    original: str = None


# TODO add fields
@dataclass()
class WishData:
    title: str = None
    version: str = None
    poster: str = None
    rate_5: str = None
    rate_4: str = None


@dataclass()
class WeaponData:
    title: str = None
    icon: str = None
    rarity: int = None
    damage: int = None
    dest: str = None
