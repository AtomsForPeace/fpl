from dataclasses import dataclass


@dataclass
class Pick:
    player_id: int
    position: int
    multiplier: int
    is_captain: bool
    is_vice_captain: bool
