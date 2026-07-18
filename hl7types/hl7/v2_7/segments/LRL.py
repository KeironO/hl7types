"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: LRL
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE
from ..datatypes.EI import EI
from ..datatypes.PL import PL
from ..datatypes.XON import XON


class LRL(HL7Model):
    """Location Relationship (S8.9.4).

    Attributes
    ----------
    lrl_1 : PL
        LRL.1 - Primary Key Value - LRL (PL) R S8.9.4.1

    lrl_2 : str | None
        LRL.2 - Segment Action Code (ID) O S10.6.3.2 | 0206 - Segment action code

    lrl_3 : EI | None
        LRL.3 - Segment Unique Key (EI) O S8.9.3.3

    lrl_4 : CWE
        LRL.4 - Location Relationship ID (CWE) R S8.9.4.4 | 0325 - Location Relationship ID

    lrl_5 : list[XON] | None
        LRL.5 - Organizational Location Relationship Value (XON) C rep S8.9.4.5

    lrl_6 : PL | None
        LRL.6 - Patient Location Relationship Value (PL) C S8.9.4.6
    """

    lrl_1: PL = Field(
        validation_alias=AliasChoices(
            "lrl_1",
            "primary_key_value_lrl",
            "LRL.1",
        ),
        serialization_alias="LRL.1",
        title="Primary Key Value - LRL",
        description="R | Item #00943",
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
        description=(
            "O | Item #00763 | Table 0206 - Segment action code | LEN:1"
        ),
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
        description="O | Item #00764",
    )

    lrl_4: CWE = Field(
        validation_alias=AliasChoices(
            "lrl_4",
            "location_relationship_id",
            "LRL.4",
        ),
        serialization_alias="LRL.4",
        title="Location Relationship ID",
        description="R | Item #01277 | Table 0325 - Location Relationship ID",
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
        description="C | Item #01301",
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
        description="C | Item #01292",
    )

    model_config = ConfigDict(populate_by_name=True)
