from dataclasses import dataclass


@dataclass()
class WishData:
    title: str = None
    title_en: str = None
    version: str = None
    poster: str = None
