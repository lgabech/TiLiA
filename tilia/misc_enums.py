from enum import Enum


class StartOrEnd(Enum):
    START = "start"
    END = "end"


class SingleOrMultiple(Enum):
    SINGLE = "single"
    MULTIPLE = "multiple"


class IncreaseOrDecrease(Enum):
    INCREASE = 1
    DECREASE = -1


class InOrOut(Enum):
    IN = 1
    OUT = -1
