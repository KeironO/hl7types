"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: LRL
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE
from ..datatypes.EI import EI
from ..datatypes.PL import PL
from ..datatypes.XON import XON


class LRL(HL7Model):
    """HL7 v2 LRL segment.

    Attributes
    ----------
    lrl_1 : PL
        LRL.1 (req) - Primary Key Value - LRL (PL)

    lrl_2 : str | None
        LRL.2 (opt) - Segment Action Code (ID)

    lrl_3 : EI | None
        LRL.3 (opt) - Segment Unique Key (EI)

    lrl_4 : CWE
        LRL.4 (req) - Location Relationship ID (CWE)

    lrl_5 : list[XON] | None
        LRL.5 (opt, rep) - Organizational Location Relationship Value (XON)

    lrl_6 : PL | None
        LRL.6 (opt) - Patient Location Relationship Value (PL)
    """

    lrl_1: PL = Field(
        default=...,
        validation_alias=AliasChoices(
            "lrl_1",
            "primary_key_value_lrl",
            "LRL.1",
        ),
        serialization_alias="LRL.1",
        title="Primary Key Value - LRL",
        description="Item #943",
    )

    lrl_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "lrl_2",
            "segment_action_code",
            "LRL.2",
        ),
        serialization_alias="LRL.2",
        title="Segment Action Code",
        description="Item #763 | Table HL70206",
    )

    lrl_3: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "lrl_3",
            "segment_unique_key",
            "LRL.3",
        ),
        serialization_alias="LRL.3",
        title="Segment Unique Key",
        description="Item #764",
    )

    lrl_4: CWE = Field(
        default=...,
        validation_alias=AliasChoices(
            "lrl_4",
            "location_relationship_id",
            "LRL.4",
        ),
        serialization_alias="LRL.4",
        title="Location Relationship ID",
        description="Item #1277 | Table HL70325",
    )

    lrl_5: Optional[List[XON]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "lrl_5",
            "organizational_location_relationship_value",
            "LRL.5",
        ),
        serialization_alias="LRL.5",
        title="Organizational Location Relationship Value",
        description="Item #1301",
    )

    lrl_6: Optional[PL] = Field(
        default=None,
        validation_alias=AliasChoices(
            "lrl_6",
            "patient_location_relationship_value",
            "LRL.6",
        ),
        serialization_alias="LRL.6",
        title="Patient Location Relationship Value",
        description="Item #1292",
    )

    model_config = {"populate_by_name": True}
