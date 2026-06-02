from __future__ import annotations

import sys
from typing import cast

if sys.version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self

from pydantic import BaseModel, ConfigDict

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
    """Base class for all HL7 v2 models.

    All generated message, segment, group, and datatype classes inherit from
    ``HL7Model``. It extends Pydantic's ``BaseModel`` with ER7 and XML
    serialisation methods and enables both positional field names and
    human-readable aliases on input.

    Parameters
    ----------
    **data : Any
        Field values accepted by name, human-readable alias, or HL7 dot
        notation (e.g. ``MSH.3``). All three forms are equivalent.

    Attributes
    ----------
    model_config : ConfigDict
        Pydantic configuration. ``populate_by_name=True`` allows field
        population using the Python attribute name in addition to any alias.
        ``validate_by_alias=True`` ensures alias-keyed input is validated.

    Examples
    --------
    >>> from hl7types.hl7.v2_5_1.datatypes import HD
    >>> HD(hd_1="WPAS").hd_1
    'WPAS'
    >>> HD(hierarchic_designator_namespace_id="WPAS").hd_1
    'WPAS'
    >>> HD(**{"HD.1": "WPAS"}).hd_1
    'WPAS'
    """

    model_config = ConfigDict(populate_by_name=True, validate_by_alias=True)

    def model_dump_er7(
        self,
        segment_separator: str = "\r",
        enc: EncodingChars | None = None,
    ) -> str:
        """Encode the model to an ER7 (pipe-delimited) wire string.

        For segment models, returns a single segment string with no trailing
        separator. For message and group models, returns all segments joined
        by ``segment_separator``.

        Parameters
        ----------
        segment_separator : str, optional
            Character used to join segments. The HL7 v2 specification mandates
            a carriage return (``\\r``, ASCII 0x0D). Defaults to ``"\\r"``.
        enc : EncodingChars, optional
            Delimiter characters to use for encoding. Defaults to the standard
            HL7 encoding characters (``|``, ``^``, ``~``, ``\\``, ``&``).

        Returns
        -------
        str
            ER7-encoded wire string.

        Examples
        --------
        >>> from hl7types.hl7.v2_5_1.segments import MSA
        >>> MSA(msa_1="AA", msa_2="MSG001").model_dump_er7()
        'MSA|AA|MSG001'
        """
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
        """Decode an ER7 wire string into a typed model instance.

        For segment classes, ``wire`` should be a single segment string. For
        message and group classes, ``wire`` should be a complete multi-segment
        message. Use the top-level :func:`hl7types.decode_er7` helper instead
        when the message type should be resolved automatically from MSH.

        Parameters
        ----------
        wire : str
            ER7-encoded wire string to decode.
        segment_separator : str, optional
            Character used to split segments. Defaults to ``"\\r"``.
        enc : EncodingChars, optional
            Delimiter characters to use for decoding. When ``None``, the
            decoder reads the encoding characters from MSH in the wire string.
        strict : bool, optional
            If ``True``, raises ``pydantic.ValidationError`` when required
            fields or segments are absent. If ``False``, missing required
            fields are filled with empty placeholder values and a
            ``UserWarning`` is emitted. Defaults to ``False``.

        Returns
        -------
        Self
            A fully validated instance of the calling class.

        Raises
        ------
        pydantic.ValidationError
            If ``strict=True`` and required fields are missing, or if any
            field value fails format validation.
        ValueError
            If the wire string is empty or the message type cannot be resolved.

        Examples
        --------
        >>> from hl7types.hl7.v2_5_1.segments import MSA
        >>> seg = MSA.model_validate_er7("MSA|AA|MSG001")
        >>> seg.msa_1
        'AA'
        """
        effective_enc = enc if enc is not None else DEFAULT_ENCODING
        if is_segment_cls(cls):
            return cast(Self, decode_er7_segment(wire, cls, effective_enc, strict=strict))
        return cast(Self, decode_er7(wire, msg_cls=cls, segment_separator=segment_separator, strict=strict))

    def model_dump_xml(self, *, pretty: bool = True) -> str:
        """Encode the model to an HL7 v2 XML wire string.

        Parameters
        ----------
        pretty : bool, optional
            If ``True``, the output is indented for readability.
            If ``False``, the output is compact with no extra whitespace.
            Defaults to ``True``.

        Returns
        -------
        str
            HL7 v2 XML-encoded string with an XML declaration and the
            ``urn:hl7-org:v2xml`` namespace.

        Examples
        --------
        >>> from hl7types.hl7.v2_5_1.segments import MSA
        >>> print(MSA(msa_1="AA", msa_2="MSG001").model_dump_xml())
        <?xml version='1.0' encoding='UTF-8'?>
        <MSA xmlns="urn:hl7-org:v2xml">
            <MSA.1>AA</MSA.1>
            <MSA.2>MSG001</MSA.2>
        </MSA>
        """
        return encode_xml(self, pretty=pretty)
