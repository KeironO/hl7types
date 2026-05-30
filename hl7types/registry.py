from __future__ import annotations

from pydantic import BaseModel

_PROTECTED_SEGMENTS = {"MSH", "FHS", "BHS"}


class HL7Registry:
    def __init__(self) -> None:
        self._segments: dict[str, type[BaseModel]] = {}
        self._messages: dict[tuple[str, str], type[BaseModel]] = {}

    def register_segment(self, name: str, cls: type[BaseModel]) -> None:
        if name in _PROTECTED_SEGMENTS:
            raise ValueError(f"{name!r} is a delimiter-definition segment and cannot be overridden")
        self._segments[name] = cls

    def get_segment(self, name: str) -> type[BaseModel] | None:
        return self._segments.get(name)

    def register_message(self, version: str, name: str, cls: type[BaseModel]) -> None:
        self._messages[(version, name)] = cls

    def get_message(self, version: str, name: str) -> type[BaseModel] | None:
        return self._messages.get((version, name))


_default_registry = HL7Registry()


def register_segment(name: str, cls: type[BaseModel]) -> None:
    _default_registry.register_segment(name, cls)


def register_message(version: str, name: str, cls: type[BaseModel]) -> None:
    _default_registry.register_message(version, name, cls)
