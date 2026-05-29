from __future__ import annotations

# Patches BaseModel.__init_subclass__ so every class defined under hl7types.hl7.*
# gets model_dump_er7() and model_validate_er7() injected at class-definition time.
# Scoped to hl7types.hl7.* to avoid polluting unrelated BaseModel subclasses.
# hl7types must be imported before any hl7types.hl7.* imports for the hook to fire.
from typing import Any

from pydantic import BaseModel

from hl7types.codecs.er7.decoder import _is_segment_cls, decode_er7, decode_er7_segment
from hl7types.codecs.er7.encoder import (
    DEFAULT_ENCODING,
    EncodingChars,
    _is_segment,
    encode_er7,
    encode_er7_segment,
)
from hl7types.codecs.xml.encoder import encode_xml


def _dump_er7(
    self: BaseModel,
    segment_separator: str = "\r",
    enc: EncodingChars | None = None,
) -> str:
    effective_enc = enc if enc is not None else DEFAULT_ENCODING
    if _is_segment(self):
        return encode_er7_segment(self, effective_enc)
    return encode_er7(self, segment_separator=segment_separator)


def _validate_er7(
    cls: type[BaseModel],
    wire: str,
    segment_separator: str = "\r",
    enc: EncodingChars | None = None,
    *,
    strict: bool = False,
) -> BaseModel:
    effective_enc = enc if enc is not None else DEFAULT_ENCODING
    if _is_segment_cls(cls):
        return decode_er7_segment(wire, cls, effective_enc, strict=strict)
    return decode_er7(wire, msg_cls=cls, segment_separator=segment_separator, strict=strict)


def _dump_xml(
    self: BaseModel,
    *,
    pretty: bool = True,
) -> str:
    return encode_xml(self, pretty=pretty)


def _inject(cls: type) -> None:
    cls.model_dump_er7 = _dump_er7
    cls.model_validate_er7 = classmethod(_validate_er7)
    cls.model_dump_xml = _dump_xml


_original_init_subclass = BaseModel.__init_subclass__


@classmethod  # type: ignore[misc]
def _patched_init_subclass(cls, **kwargs: Any) -> None:
    _original_init_subclass(**kwargs)
    if cls.__module__.startswith("hl7types.hl7."):
        _inject(cls)


BaseModel.__init_subclass__ = _patched_init_subclass  # type: ignore[method-assign]


__all__ = [
    "EncodingChars",
    "DEFAULT_ENCODING",
    "encode_er7",
    "encode_er7_segment",
    "decode_er7",
    "decode_er7_segment",
    "encode_xml",
]
