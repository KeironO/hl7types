from __future__ import annotations

from collections.abc import Callable

from hl7types.codecs.encoding import DEFAULT_ENCODING, EncodingChars
from hl7types.codecs.er7.decoder import decode_er7, decode_er7_segment
from hl7types.codecs.er7.encoder import (
    encode_er7,
    encode_er7_segment,
)
from hl7types.codecs.er7.generic import (
    GenericComponent,
    GenericField,
    GenericMessage,
    GenericRepetition,
    GenericSegment,
)
from hl7types.codecs.er7.hybrid import HybridDecodeDiagnostic, HybridMessage, decode_er7_hybrid
from hl7types.codecs.xml.decoder import decode_xml, decode_xml_segment
from hl7types.codecs.xml.encoder import encode_xml
from hl7types.hl7 import HL7Model
from hl7types.hl7._validators import NonStandardDateWarning
from hl7types.registry import HL7Registry
from hl7types.utils.error import err_from_pydantic_error, errs_from_exception

DateParser = Callable[[str], str]

__all__ = [
    "HL7Model",
    "EncodingChars",
    "DEFAULT_ENCODING",
    "encode_er7",
    "encode_er7_segment",
    "decode_er7",
    "decode_er7_segment",
    "decode_er7_hybrid",
    "HybridMessage",
    "HybridDecodeDiagnostic",
    "GenericMessage",
    "GenericSegment",
    "GenericField",
    "GenericRepetition",
    "GenericComponent",
    "encode_xml",
    "decode_xml",
    "decode_xml_segment",
    "HL7Registry",
    "errs_from_exception",
    "err_from_pydantic_error",
    "NonStandardDateWarning",
    "DateParser",
]
