"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: ROL
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.EI import EI
from ..datatypes.TS import TS
from ..datatypes.XCN import XCN


class ROL(HL7Model):
    """HL7 v2 ROL segment.

    Attributes
    ----------
    rol_1 : EI
        ROL.1 (req) - Role Instance ID (EI)

    rol_2 : str
        ROL.2 (req) - Action Code (ID)

    rol_3 : CE | None
        ROL.3 (opt) - Role (CE)

    rol_4 : XCN
        ROL.4 (req) - Role Person (XCN)

    rol_5 : TS | None
        ROL.5 (opt) - Role Begin Date/Time (TS)

    rol_6 : TS | None
        ROL.6 (opt) - Role End Date/Time (TS)

    rol_7 : CE | None
        ROL.7 (opt) - Role Duration (CE)

    rol_8 : CE | None
        ROL.8 (opt) - Role Action (Assumption) Reason (CE)
    """

    rol_1: EI = Field(
        default=...,
        validation_alias=AliasChoices(
            "rol_1",
            "role_instance_id",
            "ROL.1",
        ),
        serialization_alias="ROL.1",
        title="Role Instance ID",
        description="Item #1206",
    )

    rol_2: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "rol_2",
            "action_code",
            "ROL.2",
        ),
        serialization_alias="ROL.2",
        title="Action Code",
        description="Item #816 | Table HL70287",
    )

    rol_3: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rol_3",
            "role",
            "ROL.3",
        ),
        serialization_alias="ROL.3",
        title="Role",
        description="Item #1197",
    )

    rol_4: XCN = Field(
        default=...,
        validation_alias=AliasChoices(
            "rol_4",
            "role_person",
            "ROL.4",
        ),
        serialization_alias="ROL.4",
        title="Role Person",
        description="Item #1198",
    )

    rol_5: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rol_5",
            "role_begin_date_time",
            "ROL.5",
        ),
        serialization_alias="ROL.5",
        title="Role Begin Date/Time",
        description="Item #1199",
    )

    rol_6: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rol_6",
            "role_end_date_time",
            "ROL.6",
        ),
        serialization_alias="ROL.6",
        title="Role End Date/Time",
        description="Item #1200",
    )

    rol_7: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rol_7",
            "role_duration",
            "ROL.7",
        ),
        serialization_alias="ROL.7",
        title="Role Duration",
        description="Item #1201",
    )

    rol_8: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rol_8",
            "role_action_assumption_reason",
            "ROL.8",
        ),
        serialization_alias="ROL.8",
        title="Role Action (Assumption) Reason",
        description="Item #1205",
    )

    model_config = {"populate_by_name": True}
