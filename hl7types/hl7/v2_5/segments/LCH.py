"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: LCH
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.EI import EI
from ..datatypes.PL import PL


class LCH(HL7Model):
    """Location Characteristic (S8.9.3).

    Attributes
    ----------
    lch_1 : PL
        LCH.1 - Primary Key Value - LCH (PL) R S8.9.3.1

    lch_2 : str | None
        LCH.2 - Segment Action Code (ID) O S8.9.3.2 | 0206 - Segment action code

    lch_3 : EI | None
        LCH.3 - Segment Unique Key (EI) O S8.9.3.3

    lch_4 : CE
        LCH.4 - Location Characteristic ID (CE) R S8.9.3.4 | 0324 - Location characteristic ID

    lch_5 : CE
        LCH.5 - Location Characteristic Value-LCH (CE) R S8.9.3.5
    """

    lch_1: PL = Field(
        validation_alias=AliasChoices(
            "lch_1",
            "primary_key_value_lch",
            "LCH.1",
        ),
        serialization_alias="LCH.1",
        title="Primary Key Value - LCH",
        description="R | Item #01305",
    )

    lch_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "lch_2",
            "segment_action_code",
            "LCH.2",
        ),
        serialization_alias="LCH.2",
        title="Segment Action Code",
        description=(
            "O | Item #00763 | Table 0206 - Segment action code | LEN:3"
        ),
    )

    lch_3: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "lch_3",
            "segment_unique_key",
            "LCH.3",
        ),
        serialization_alias="LCH.3",
        title="Segment Unique Key",
        description="O | Item #00764",
    )

    lch_4: CE = Field(
        validation_alias=AliasChoices(
            "lch_4",
            "location_characteristic_id",
            "LCH.4",
        ),
        serialization_alias="LCH.4",
        title="Location Characteristic ID",
        description="R | Item #01295 | Table 0324 - Location characteristic ID",
    )

    lch_5: CE = Field(
        validation_alias=AliasChoices(
            "lch_5",
            "location_characteristic_value_lch",
            "LCH.5",
        ),
        serialization_alias="LCH.5",
        title="Location Characteristic Value-LCH",
        description="R | Item #01294",
    )

    model_config = ConfigDict(populate_by_name=True)
