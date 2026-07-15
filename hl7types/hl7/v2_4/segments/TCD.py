"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: TCD
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.SN import SN


class TCD(HL7Model):
    """Test Code Detail (S13.4.10).

    Attributes
    ----------
    tcd_1 : CE
        TCD.1 - Universal Service Identifier (CE) R S13.4.10.1

    tcd_2 : SN | None
        TCD.2 - Auto-Dilution Factor (SN) O S13.4.10.2

    tcd_3 : SN | None
        TCD.3 - Rerun Dilution Factor (SN) O S13.4.10.3

    tcd_4 : SN | None
        TCD.4 - Pre-Dilution Factor (SN) O S13.4.10.4

    tcd_5 : SN | None
        TCD.5 - Endogenous Content of Pre-Dilution Diluent (SN) O S13.4.10.5

    tcd_6 : str | None
        TCD.6 - Automatic Repeat Allowed (ID) O S13.4.10.6 | 0136 - Yes/no indicator

    tcd_7 : str | None
        TCD.7 - Reflex Allowed (ID) O S13.4.10.7 | 0136 - Yes/no indicator

    tcd_8 : CE | None
        TCD.8 - Analyte Repeat Status (CE) O S13.4.10.8 | 0389 - Analyte repeat status
    """

    tcd_1: CE = Field(
        validation_alias=AliasChoices(
            "tcd_1",
            "universal_service_identifier",
            "TCD.1",
        ),
        serialization_alias="TCD.1",
        title="Universal Service Identifier",
        description="R | Item #00238",
    )

    tcd_2: Optional[SN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tcd_2",
            "auto_dilution_factor",
            "TCD.2",
        ),
        serialization_alias="TCD.2",
        title="Auto-Dilution Factor",
        description="O | Item #01420",
    )

    tcd_3: Optional[SN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tcd_3",
            "rerun_dilution_factor",
            "TCD.3",
        ),
        serialization_alias="TCD.3",
        title="Rerun Dilution Factor",
        description="O | Item #01421",
    )

    tcd_4: Optional[SN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tcd_4",
            "pre_dilution_factor",
            "TCD.4",
        ),
        serialization_alias="TCD.4",
        title="Pre-Dilution Factor",
        description="O | Item #01422",
    )

    tcd_5: Optional[SN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tcd_5",
            "endogenous_content_of_pre_dilution_diluent",
            "TCD.5",
        ),
        serialization_alias="TCD.5",
        title="Endogenous Content of Pre-Dilution Diluent",
        description="O | Item #01413",
    )

    tcd_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tcd_6",
            "automatic_repeat_allowed",
            "TCD.6",
        ),
        serialization_alias="TCD.6",
        title="Automatic Repeat Allowed",
        description="O | Item #01416 | Table 0136 - Yes/no indicator | LEN:1",
    )

    tcd_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tcd_7",
            "reflex_allowed",
            "TCD.7",
        ),
        serialization_alias="TCD.7",
        title="Reflex Allowed",
        description="O | Item #01424 | Table 0136 - Yes/no indicator | LEN:1",
    )

    tcd_8: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tcd_8",
            "analyte_repeat_status",
            "TCD.8",
        ),
        serialization_alias="TCD.8",
        title="Analyte Repeat Status",
        description="O | Item #01425 | Table 0389 - Analyte repeat status",
    )

    model_config = {"populate_by_name": True}
