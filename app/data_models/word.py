from dataclasses import dataclass


@dataclass()
class WordData:
    word: str = None
    translate: str = None
    subinf: str = None
    original: str = None
