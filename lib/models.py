from dataclasses import dataclass, field
from enum import Enum
from typing import List, Union

class Participant(Enum):
    HOME: str
    AWAY: str


@dataclass
class Stats:
    goals_attempts: Union[int, None] = None
    shots_on_goal: Union[int, None] = None
    shots_off_goal: Union[int, None] = None
    shots: Union[int, None] = None
    punches: Union[int, None] = None





@dataclass
class Statistics:
    general: Stats = field(default_factory=Stats)
    half_first: Stats = field(default_factory=Stats)
    half_second: Stats = field(default_factory=Stats)
    time_spam_0_15: Stats = field(default_factory=Stats)
    time_spam_15_30: Stats = field(default_factory=Stats)
    time_spam_30_45: Stats = field(default_factory=Stats)
    time_spam_45_60: Stats = field(default_factory=Stats)
    time_spam_60_75: Stats = field(default_factory=Stats)
    time_spam_75_90: Stats = field(default_factory=Stats)


@dataclass
class Incident:
    player: str
    minute: int


@dataclass
class Summary:
    goals: List[Incident] = field(default_factory=list)
    cards_y: List[Incident] = field(default_factory=list)
    cards_r: List[Incident] = field(default_factory=list)


@dataclass
class Match:
    team_home: str
    team_away: str
    date: str = ""
    summary: Summary = field(default_factory=Summary)
    stats: Statistics = field(default_factory=Statistics)
    played: bool = False
