from __future__ import annotations

import warnings
from collections.abc import Callable
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, PrivateAttr, ValidationError, model_serializer

from hl7types.codecs.er7.decoder import decode_er7_from_segments
from hl7types.encoding import (
    DEFAULT_ENCODING,
    DELIM_DEF,
    EncodingChars,
    encoding_from_segment,
    split_segments,
)
from hl7types.registry import HL7Registry


class GenericModel(BaseModel):
    model_config = ConfigDict(frozen=True)


class GenericComponent(GenericModel):
    """A component from an untyped ER7 field repetition."""

    subcomponents: tuple[str, ...]


class GenericRepetition(GenericModel):
    """A repetition from an untyped ER7 field."""

    components: tuple[GenericComponent, ...]


class GenericField(GenericModel):
    """An untyped ER7 field, including all repetitions and components."""

    value: str
    repetitions: tuple[GenericRepetition, ...]


class GenericSegment(GenericModel):
    """An untyped ER7 segment retained exactly as received."""

    raw: str
    name: str
    fields: tuple[GenericField, ...]

    def __getattr__(self, name: str) -> GenericField:
        prefix = f"{self.name.lower()}_"
        if name.startswith(prefix) and name[len(prefix) :].isdigit():
            position = int(name[len(prefix) :])
            if position > 0 and position <= len(self.fields):
                return self.fields[position - 1]
        raise AttributeError(f"{type(self).__name__!s} has no attribute {name!r}")

    @model_serializer
    def _serialize(self) -> dict[str, Any]:
        return {
            "raw": self.raw,
            "name": self.name,
            **{
                f"{self.name.lower()}_{position}": field.model_dump(mode="json")
                for position, field in enumerate(self.fields, start=1)
            },
        }


class GenericMessage(GenericModel):
    """A lossless, untyped ER7 message representation."""

    _raw: str = PrivateAttr()
    segment_separator: str
    encoding: EncodingChars
    segments: tuple[GenericSegment, ...]

    def __getattr__(self, name: str) -> GenericSegment | tuple[GenericSegment, ...]:
        try:
            return super().__getattr__(name)  # type: ignore[has-type]
        except AttributeError:
            pass
        matches = tuple(segment for segment in self.segments if segment.name == name)
        if len(matches) == 1:
            return matches[0]
        if matches:
            return matches
        raise AttributeError(f"{type(self).__name__!s} has no attribute {name!r}")

    def model_dump_er7(self) -> str:
        """Return the exact ER7 wire string supplied to the generic decoder."""
        return self._raw

    @model_serializer
    def _serialize(self) -> dict[str, Any]:
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
        for name in dict.fromkeys(segment.name for segment in self.segments):
            matches = tuple(segment for segment in self.segments if segment.name == name)
            serialized = [segment.model_dump(mode="json") for segment in matches]
            result[name] = serialized[0] if len(serialized) == 1 else serialized
        return result


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


def _decode_er7_generic(
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
    message = GenericMessage(
        segment_separator=segment_separator,
        encoding=encoding,
        segments=segments,
    )
    message._raw = wire  # type: ignore[private-usage]
    return message


class HybridDecodeDiagnostic(BaseModel):
    """A warning or error raised while building a typed message view."""

    model_config = ConfigDict(frozen=True)

    level: Literal["warning", "error"]
    message: str


class HybridMessage(BaseModel):
    """A lossless generic message with an optional typed message view."""

    model_config = ConfigDict(frozen=True)

    generic: GenericMessage
    typed: BaseModel | None
    diagnostics: tuple[HybridDecodeDiagnostic, ...]

    def model_dump_er7(self) -> str:
        """Return the original ER7 wire string from the generic view."""
        return self.generic.model_dump_er7()


def decode_er7_hybrid(
    wire: str,
    msg_cls: type[BaseModel] | None = None,
    segment_separator: str = "\r",
    *,
    registry: HL7Registry | None = None,
    dt_parser: Callable[[str], str] | None = None,
    dtm_parser: Callable[[str], str] | None = None,
) -> HybridMessage:
    """Decode ER7 losslessly and attempt to build a best-effort typed view.

    The generic view always retains every received segment. The typed view uses
    lenient structural decoding, so unknown segments and missing required
    fields become diagnostics rather than preventing access to known content.
    Field-format validation errors and unknown message structures leave
    ``typed`` as ``None`` while preserving the generic view.

    The wire is split into segments exactly once, by the generic parse. The
    typed view is then built from those same segment strings rather than
    re-splitting the wire, so encoding detection and structural decoding share
    a single segmentation pass.
    """
    generic = _decode_er7_generic(wire, segment_separator)
    seg_strings = [segment.raw for segment in generic.segments]
    typed: BaseModel | None = None
    error: ValueError | ValidationError | None = None

    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        try:
            typed = decode_er7_from_segments(
                seg_strings,
                msg_cls,
                strict=False,
                registry=registry,
                dt_parser=dt_parser,
                dtm_parser=dtm_parser,
            )
        except (ValueError, ValidationError) as exc:
            error = exc

    diagnostics = tuple(
        HybridDecodeDiagnostic(level="warning", message=str(warning.message)) for warning in caught
    )
    if error is not None:
        diagnostics += (HybridDecodeDiagnostic(level="error", message=str(error)),)

    return HybridMessage(generic=generic, typed=typed, diagnostics=diagnostics)
