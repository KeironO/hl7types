"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: SID
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE


class SID(HL7Model):
    """Substance Identifier (S13.4.11).

    Attributes
    ----------
    sid_1 : CWE | None
        SID.1 - Application/Method Identifier (CWE) C S13.4.11.1 | 9999 - no table for CE

    sid_2 : str | None
        SID.2 - Substance Lot Number (ST) C S13.4.11.2

    sid_3 : str | None
        SID.3 - Substance Container Identifier (ST) C S13.4.11.3

    sid_4 : CWE | None
        SID.4 - Substance Manufacturer Identifier (CWE) C S13.4.11.4 | 0385 - Manufacturer Identifier
    """

    sid_1: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sid_1",
            "application_method_identifier",
            "SID.1",
        ),
        serialization_alias="SID.1",
        title="Application/Method Identifier",
        description="C | Item #01426 | Table 9999 - no table for CE",
    )

    sid_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sid_2",
            "substance_lot_number",
            "SID.2",
        ),
        serialization_alias="SID.2",
        title="Substance Lot Number",
        description="C | Item #01129",
    )

    sid_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sid_3",
            "substance_container_identifier",
            "SID.3",
        ),
        serialization_alias="SID.3",
        title="Substance Container Identifier",
        description="C | Item #01428",
    )

    sid_4: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sid_4",
            "substance_manufacturer_identifier",
            "SID.4",
        ),
        serialization_alias="SID.4",
        title="Substance Manufacturer Identifier",
        description="C | Item #01429 | Table 0385 - Manufacturer Identifier",
    )

    model_config = {"populate_by_name": True}
