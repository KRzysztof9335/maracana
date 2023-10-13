from dataclasses import dataclass, field
from enum import Enum
from typing import List, Dict, Union

import hashlib
import logging
import time

class Participant(Enum):
    HOME = "home"
    AWAY = "away"


class PredictionEvents(Enum):
    "Events that may occur"
    CARD_RED = "card_red"

# GOAL_0_15: str
# GOAL_75_90: str
# GOALS_TOTAL_LT_3_5: str
# GOALS_TOTAL_LT_4_5: str
# GOALS_TOTAL_LT_5_5: str
# GOALS_TOTAL_GT_0_5: str
# GOALS_TOTAL_GT_1_5: str
# CARDS_YELLOW_TOTAL = "cards_yellow_total"
# CARDS_YELLOW_HALF_FIRST ="cards_yellow_half_first"
# CARDS_YELLOW_HALF_SECOND: str

@dataclass
class Prediction:
    name: PredictionEvents
    probability: float  # in percentage
    course: float = 1.1
    expected: bool = True
    real: Union[None, bool] = None
    guessed: Union[None, bool] = None
    id: str = field(init=False)

    def __post_init__(self):
        to_hash = str(time.time_ns())
        self.id = hashlib.sha256(to_hash.encode('utf-8')).hexdigest()[0:20]

        if self.probability > 100 or self.probability < 0:
            raise ValueError(f"Provided wrong probability {self.probability}")

    def update_prediction(self, value: bool) -> None:
        self.real = value
        if self.real == self.expected:
            self.guessed = True
        else:
            self.guessed = False

# @dataclass
# class Stats:
#     goals_attempts: Union[int, None] = None
#     shots_on_goal: Union[int, None] = None
#     shots_off_goal: Union[int, None] = None
#     shots: Union[int, None] = None
#     punches: Union[int, None] = None


# @dataclass
# class Statistics:
#     general: Stats = field(default_factory=Stats)
#     half_first: Stats = field(default_factory=Stats)
#     half_second: Stats = field(default_factory=Stats)
#     time_spam_0_15: Stats = field(default_factory=Stats)
#     time_spam_15_30: Stats = field(default_factory=Stats)
#     time_spam_30_45: Stats = field(default_factory=Stats)
#     time_spam_45_60: Stats = field(default_factory=Stats)
#     time_spam_60_75: Stats = field(default_factory=Stats)
#     time_spam_75_90: Stats = field(default_factory=Stats)




@dataclass
class Incident:
    player: str
    minute: int


@dataclass
class Summary:
    goals: List[Incident] = field(default_factory=list)
    cards_y: List[Incident] = field(default_factory=list)
    cards_r: List[Incident] = field(default_factory=list)

    def is_empty(self):
        return not any([self.goals, self.cards_r, self.cards_y])

@dataclass
class Match:
    id: str = field(init=False)
    date: str
    country: str
    league: str
    team_home: str
    team_away: str
    summary: Summary = field(default_factory=Summary)
    predictions: Dict[str, Prediction] = field(default_factory=dict)
    played: bool = False

    def __post_init__(self):
        to_hash = self.date + self.country + self.league + self.team_home + self.team_away
        self.id = hashlib.sha256(to_hash.encode('utf-8')).hexdigest()[0:20]

    def repr_short(self) -> str:
        return f"{self.date} - {self.team_home} - {self.team_away}"

    def add_prediction(self, prediction: Prediction):
        "Add prediction"
        self.predictions[prediction.id] = prediction

    def update_prediction(self, id: str, value: bool):
        if id not in self.predictions.keys():
            logging.warning(f"For match {self.repr_short()}: no prediction with id {id}")
            return
        self.predictions[id].update_prediction(value)
