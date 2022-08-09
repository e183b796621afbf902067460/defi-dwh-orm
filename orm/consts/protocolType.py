from enum import Enum


class ProtocolType(Enum):
    LENDING: str = 'LENDING'
    STAKING: str = 'STAKING'
    DEX: str = 'DEX'
