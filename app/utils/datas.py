from dataclasses import dataclass
from typing import List
from app.data_models.user import UserData
from app.data_models.character import CharacterData
from app.data_models.word import WordData
from app.data_models.weapon import WeaponData
from app.data_models.wish import WishData
from app.data_models.meta import MetaData


@dataclass
class GET:
    attr: str = None
    id: int = None
    start: int = None
    end: int = None
    _lists: List[str] = None
    _lists_is_empty: bool = True


@dataclass
class POST(UserData, CharacterData, WordData, WeaponData, WishData, MetaData):
    attr: str = None
    _lists: List[str] = None
    _lists_is_empty: bool = True


@dataclass
class DELETE:
    id: int = None
    attr: str = None
    _lists: List[str] = None
    _lists_is_empty: bool = True


@dataclass
class PATCH:
    id: int = None
    attr: str = None
    value: str = None
    _lists: List[str] = None
    _lists_is_empty: bool = True
