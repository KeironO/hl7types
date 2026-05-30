"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: AL1
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE


class AL1(HL7Model):
    """HL7 v2 AL1 segment.

    Attributes
    ----------
    al1_1 : str
        AL1.1 (req) - Set ID - AL1 (SI)

    al1_2 : str | None
        AL1.2 (opt) - Allergy Type (IS)

    al1_3 : CE
        AL1.3 (req) - Allergy Code/Mnemonic/Description (CE)

    al1_4 : str | None
        AL1.4 (opt) - Allergy Severity (IS)

    al1_5 : list[str] | None
        AL1.5 (opt, rep) - Allergy Reaction (ST)

    al1_6 : str | None
        AL1.6 (opt) - Identification Date (DT)
    """

    al1_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "al1_1",
            "set_id_al1",
            "AL1.1",
        ),
        serialization_alias="AL1.1",
        title="Set ID - AL1",
        description="Item #203",
    )

    al1_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "al1_2",
            "allergy_type",
            "AL1.2",
        ),
        serialization_alias="AL1.2",
        title="Allergy Type",
        description="Item #204 | Table HL70127",
    )

    al1_3: CE = Field(
        default=...,
        validation_alias=AliasChoices(
            "al1_3",
            "allergy_code_mnemonic_description",
            "AL1.3",
        ),
        serialization_alias="AL1.3",
        title="Allergy Code/Mnemonic/Description",
        description="Item #205",
    )

    al1_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "al1_4",
            "allergy_severity",
            "AL1.4",
        ),
        serialization_alias="AL1.4",
        title="Allergy Severity",
        description="Item #206 | Table HL70128",
    )

    al1_5: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "al1_5",
            "allergy_reaction",
            "AL1.5",
        ),
        serialization_alias="AL1.5",
        title="Allergy Reaction",
        description="Item #207",
    )

    al1_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "al1_6",
            "identification_date",
            "AL1.6",
        ),
        serialization_alias="AL1.6",
        title="Identification Date",
        description="Item #208",
    )

    model_config = {"populate_by_name": True}
