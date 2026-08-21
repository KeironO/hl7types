from __future__ import annotations

import warnings
from collections.abc import Callable
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, ValidationError, field_serializer

from hl7types.codecs.er7.decoder import decode_er7_from_segments

# Re-export generic types so existing imports keep working.
from hl7types.codecs.er7.generic import (
    GenericComponent,
    GenericField,
    GenericMessage,
    GenericRepetition,
    GenericSegment,
    decode_er7_generic,
)
from hl7types.registry import HL7Registry

__all__ = [
    "GenericComponent",
    "GenericField",
    "GenericMessage",
    "GenericRepetition",
    "GenericSegment",
    "HybridDecodeDiagnostic",
    "HybridMessage",
    "decode_er7_hybrid",
]


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

    @field_serializer("generic")
    def _serialize_generic(self, generic: GenericMessage) -> dict[str, Any]:
        return generic.to_dict()

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
    generic = decode_er7_generic(wire, segment_separator)
    seg_strings = [segment.raw for segment in generic.segments]
    typed: BaseModel | None = None
    error: ValueError | ValidationError | None = None
    collected: list[str] = []

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
                _diagnostics=collected,
            )
        except (ValueError, ValidationError) as exc:
            error = exc

    diagnostics = tuple(HybridDecodeDiagnostic(level="warning", message=msg) for msg in collected)
    diagnostics += tuple(
        HybridDecodeDiagnostic(level="warning", message=str(warning.message)) for warning in caught
    )
    if error is not None:
        diagnostics += (HybridDecodeDiagnostic(level="error", message=str(error)),)

    return HybridMessage(generic=generic, typed=typed, diagnostics=diagnostics)
