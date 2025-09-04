from enum import Enum

class InstitutionType(Enum):
    SCHOOL = 1
    SCHOOL_AND_COLLEGE = 2
    COLLEGE = 3
    MADRASHA=4
    QUAOMI_MADRASHA = 5
    TECHNICAL_AND_VOCATIONAL = 6

class HigestLevelType(Enum):
    JUNIOR_SECONDARY = 1
    SECONDARY = 2
    HIGHER_SECONDARY = 3
    DIPLOMA = 16
    HONOURS = 4
    MASTERS = 5
    DAKHIL = 6
    ALIM = 7
    FAZIL = 8
    KAMIL = 9
    HIFZUL_QURAN = 10
    AL_MARHALATUL_MUTASSITAH= 12
    AL_MARHALATUL_SANABIATUL_ULAIYA = 13
    MARHALATUL_FAZILAT = 14
    MARHALATUL_TAKMIL = 15

class StudentType(Enum):
    BOY= 1
    GIRL = 2
    CO_EDUCATION = 3

class ApprovalStatus(Enum):
    BUILD = 1
    TEACHING  = 2
    ALL = 3
    NOTHING = 4