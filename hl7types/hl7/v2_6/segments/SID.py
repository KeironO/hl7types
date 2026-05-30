"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: SID
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE


class SID(HL7Model):
    """HL7 v2 SID segment.

    Attributes
    ----------
    sid_1 : CWE | None
        SID.1 (opt) - Application/Method Identifier (CWE)

    sid_2 : str | None
        SID.2 (opt) - Substance Lot Number (ST)

    sid_3 : str | None
        SID.3 (opt) - Substance Container Identifier (ST)

    sid_4 : CWE | None
        SID.4 (opt) - Substance Manufacturer Identifier (CWE)
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
        description="Item #1426 | Table HL79999",
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
        description="Item #1129",
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
        description="Item #1428",
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
        description="Item #1429 | Table HL70385",
    )

    model_config = {"populate_by_name": True}
