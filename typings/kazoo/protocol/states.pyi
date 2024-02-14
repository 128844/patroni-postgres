from typing import Any, NamedTuple
class KazooState:
    SUSPENDED: str
    CONNECTED: str
    LOST: str
class KeeperState:
    AUTH_FAILED: str
    CONNECTED: str
    CONNECTED_RO: str
    CONNECTING: str
    CLOSED: str
    EXPIRED_SESSION: str
class WatchedEvent(NamedTuple):
    type: str
    state: str
    path: str
class ZnodeStat(NamedTuple):

    czxid: int
    mzxid: int
    ctime: float
    mtime: float
    version: int
    cversion: int
    aversion: int
    ephemeralOwner: Any
    dataLength: int
    numChildren: int
    pzxid: int
