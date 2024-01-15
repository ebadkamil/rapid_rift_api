from enum import Enum


class DbTypes(Enum):
    ORACLE = "oracle"
    SQLITE = "sqlite"
    UNKNOWN = "unknown"  # for unittest puproses
