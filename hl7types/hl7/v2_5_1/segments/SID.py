"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: SID
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE


class SID(HL7Model):
    """Substance Identifier (S13.4.11).

    Attributes
    ----------
    sid_1 : CE | None
        SID.1 - Application / Method Identifier (CE) C S13.4.11.1

    sid_2 : str | None
        SID.2 - Substance Lot Number (ST) C S13.4.11.2

    sid_3 : str | None
        SID.3 - Substance Container Identifier (ST) C S13.4.11.3

    sid_4 : CE | None
        SID.4 - Substance Manufacturer Identifier (CE) C S13.4.11.4 | 0385 - Manufacturer identifier
    """

    sid_1: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sid_1",
            "application_method_identifier",
            "SID.1",
        ),
        serialization_alias="SID.1",
        title="Application / Method Identifier",
        description="C | Item #01426",
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
        description="C | Item #01129 | LEN:20",
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
        description="C | Item #01428 | LEN:200",
    )

    sid_4: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sid_4",
            "substance_manufacturer_identifier",
            "SID.4",
        ),
        serialization_alias="SID.4",
        title="Substance Manufacturer Identifier",
        description="C | Item #01429 | Table 0385 - Manufacturer identifier",
    )

    model_config = {"populate_by_name": True}
