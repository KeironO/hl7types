from __future__ import annotations

import sys
from typing import cast

if sys.version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self

from pydantic import BaseModel

from hl7types.codecs.er7.decoder import is_segment_cls, decode_er7, decode_er7_segment
from hl7types.codecs.er7.encoder import (
    DEFAULT_ENCODING,
    EncodingChars,
    is_segment,
    encode_er7,
    encode_er7_segment,
)
from hl7types.codecs.xml.encoder import encode_xml


class HL7Model(BaseModel):
    def model_dump_er7(
        self,
        segment_separator: str = "\r",
        enc: EncodingChars | None = None,
    ) -> str:
        effective_enc = enc if enc is not None else DEFAULT_ENCODING
        if is_segment(self):
            return encode_er7_segment(self, effective_enc)
        return encode_er7(self, segment_separator=segment_separator)

    @classmethod
    def model_validate_er7(
        cls,
        wire: str,
        segment_separator: str = "\r",
        enc: EncodingChars | None = None,
        *,
        strict: bool = False,
    ) -> Self:
        effective_enc = enc if enc is not None else DEFAULT_ENCODING
        if is_segment_cls(cls):
            return cast(Self, decode_er7_segment(wire, cls, effective_enc, strict=strict))
        return cast(Self, decode_er7(wire, msg_cls=cls, segment_separator=segment_separator, strict=strict))

    def model_dump_xml(self, *, pretty: bool = True) -> str:
        return encode_xml(self, pretty=pretty)
