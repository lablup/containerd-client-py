"""Dynamic protoc module; attributes are Any (see scripts/regen.py)."""

from typing import Any

def __getattr__(name: str) -> Any: ...
