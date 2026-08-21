from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any

from hl7types.codecs.encoding import (
    DEFAULT_ENCODING,
    DELIM_DEF,
    EncodingChars,
    encoding_from_segment,
    split_segments,
)


@dataclass(frozen=True, slots=True)
class GenericComponent:
    """A component from an untyped ER7 field repetition."""

    subcomponents: tuple[str, ...]

    def to_dict(self) -> dict[str, Any]:
        return {"subcomponents": list(self.subcomponents)}

    def model_dump(self, mode: str = "json") -> dict[str, Any]:  # noqa: ARG002
        return self.to_dict()


@dataclass(frozen=True, slots=True)
class GenericRepetition:
    """A repetition from an untyped ER7 field."""

    components: tuple[GenericComponent, ...]

    def to_dict(self) -> dict[str, Any]:
        return {"components": [c.to_dict() for c in self.components]}

    def model_dump(self, mode: str = "json") -> dict[str, Any]:  # noqa: ARG002
        return self.to_dict()


@dataclass(frozen=True, slots=True)
class GenericField:
    """An untyped ER7 field, including all repetitions and components."""

    value: str
    repetitions: tuple[GenericRepetition, ...]

    def to_dict(self) -> dict[str, Any]:
        return {
            "value": self.value,
            "repetitions": [r.to_dict() for r in self.repetitions],
        }

    def model_dump(self, mode: str = "json") -> dict[str, Any]:  # noqa: ARG002
        return self.to_dict()


@dataclass(frozen=True, slots=True)
class GenericSegment:
    """An untyped ER7 segment retained exactly as received."""

    raw: str
    name: str
    fields: tuple[GenericField, ...]

    def get_field(self, position: int) -> GenericField | None:
        """Return field at 1-based HL7 position, or None if out of range."""
        if 1 <= position <= len(self.fields):
            return self.fields[position - 1]
        return None

    def __getattr__(self, name: str) -> GenericField:
        # Only handle {segment}_{position} lookups; everything else is a real error.
        if name.startswith("_"):
            raise AttributeError(f"{type(self).__name__!s} has no attribute {name!r}")
        # Guard against recursion during unpickling / slots init
        try:
            seg_name: str = object.__getattribute__(self, "name")
            fields: tuple[GenericField, ...] = object.__getattribute__(self, "fields")
        except AttributeError:
            raise AttributeError(f"{type(self).__name__!s} has no attribute {name!r}") from None
        prefix = f"{seg_name.lower()}_"
        if name.startswith(prefix) and name[len(prefix) :].isdigit():
            position = int(name[len(prefix) :])
            if 1 <= position <= len(fields):
                return fields[position - 1]
        raise AttributeError(f"{type(self).__name__!s} has no attribute {name!r}")

    def to_dict(self) -> dict[str, Any]:
        base: dict[str, Any] = {"raw": self.raw, "name": self.name}
        for idx, field in enumerate(self.fields, start=1):
            base[f"{self.name.lower()}_{idx}"] = field.to_dict()
        return base

    def model_dump(self, mode: str = "json") -> dict[str, Any]:  # noqa: ARG002
        return self.to_dict()


@dataclass(frozen=True, slots=True)
class GenericMessage:
    """A lossless, untyped ER7 message representation."""

    raw: str
    segment_separator: str
    encoding: EncodingChars
    segments: tuple[GenericSegment, ...]

    def get_segment(self, name: str) -> GenericSegment | tuple[GenericSegment, ...] | None:
        matches = tuple(s for s in self.segments if s.name == name)
        if len(matches) == 1:
            return matches[0]
        if matches:
            return matches
        return None

    def __getitem__(self, name: str) -> GenericSegment | tuple[GenericSegment, ...]:
        result = self.get_segment(name)
        if result is None:
            raise KeyError(name)
        return result

    def __getattr__(self, name: str) -> GenericSegment | tuple[GenericSegment, ...]:
        if name.startswith("_"):
            raise AttributeError(f"{type(self).__name__!s} has no attribute {name!r}")
        # Don't intercept dataclass internals
        if name in ("raw", "segment_separator", "encoding", "segments"):
            raise AttributeError(f"{type(self).__name__!s} has no attribute {name!r}")
        try:
            segments: tuple[GenericSegment, ...] = object.__getattribute__(self, "segments")
        except AttributeError:
            raise AttributeError(f"{type(self).__name__!s} has no attribute {name!r}") from None
        matches = tuple(s for s in segments if s.name == name)
        if len(matches) == 1:
            return matches[0]
        if matches:
            return matches
        raise AttributeError(f"{type(self).__name__!s} has no attribute {name!r}")

    def model_dump_er7(self) -> str:
        """Return the exact ER7 wire string supplied to the generic decoder."""
        return self.raw

    def to_dict(self) -> dict[str, Any]:
        result: dict[str, Any] = {
            "segment_separator": self.segment_separator,
            "encoding": {
                "field": self.encoding.field,
                "component": self.encoding.component,
                "repetition": self.encoding.repetition,
                "escape": self.encoding.escape,
                "subcomponent": self.encoding.subcomponent,
                "truncation": self.encoding.truncation,
            },
        }
        for seg_name in dict.fromkeys(s.name for s in self.segments):
            matches = [s.to_dict() for s in self.segments if s.name == seg_name]
            result[seg_name] = matches[0] if len(matches) == 1 else matches
        return result

    def model_dump(self, mode: str = "json") -> dict[str, Any]:  # noqa: ARG002
        return self.to_dict()

    def model_dump_json(self, **kwargs: Any) -> str:
        return json.dumps(self.to_dict(), **kwargs)


def _parse_field(raw: str, encoding: EncodingChars) -> GenericField:
    repetitions = tuple(
        GenericRepetition(
            components=tuple(
                GenericComponent(
                    subcomponents=tuple(component.split(encoding.subcomponent)),
                )
                for component in repetition.split(encoding.component)
            ),
        )
        for repetition in raw.split(encoding.repetition)
    )
    return GenericField(value=raw, repetitions=repetitions)


def _parse_scalar_field(value: str) -> GenericField:
    return GenericField(
        value=value,
        repetitions=(
            GenericRepetition(
                components=(GenericComponent(subcomponents=(value,)),),
            ),
        ),
    )


def _segment_fields(segment: str, encoding: EncodingChars) -> tuple[GenericField, ...]:
    parts = segment.split(encoding.field)
    if segment[:3] in DELIM_DEF and len(segment) > 3:
        fields = [encoding.field, *parts[1:]]
        return tuple(_parse_scalar_field(field) for field in fields[:2]) + tuple(
            _parse_field(field, encoding) for field in fields[2:]
        )
    return tuple(_parse_field(field, encoding) for field in parts[1:])


def decode_er7_generic(
    wire: str,
    segment_separator: str = "\r",
) -> GenericMessage:
    """Parse ER7 without resolving generated models or validating HL7 content.

    The returned object retains the complete original wire string and every
    segment in arrival order, including unknown and ``Z`` segments. Parsed
    fields preserve empty values, repetitions, components, and subcomponents.
    Escape sequences are retained verbatim rather than interpreted.
    """
    segment_strings = split_segments(wire, segment_separator)
    encoding = next(
        (
            detected
            for segment in segment_strings
            if (detected := encoding_from_segment(segment, strict=False)) is not None
        ),
        DEFAULT_ENCODING,
    )

    segments = tuple(
        GenericSegment(
            raw=segment,
            name=segment.split(encoding.field, 1)[0],
            fields=_segment_fields(segment, encoding),
        )
        for segment in segment_strings
    )
    return GenericMessage(
        raw=wire,
        segment_separator=segment_separator,
        encoding=encoding,
        segments=segments,
    )
