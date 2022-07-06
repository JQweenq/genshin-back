from dataclasses import dataclass


@dataclass()
class UserData:
    username: str = None
    password: str = None
    email: str = None
    is_admin: bool = False
