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
    """Role (S12.3.3).

    Attributes
    ----------
    rol_1 : EI
        ROL.1 - Role Instance ID (EI) R S12.3.3.1

    rol_2 : str
        ROL.2 - Action Code (ID) R S12.3.1 | 0287 - Action Code

    rol_3 : CE | None
        ROL.3 - Role (CE) O S12.3.3.3

    rol_4 : XCN
        ROL.4 - Role Person (XCN) R S12.3.3.4

    rol_5 : TS | None
        ROL.5 - Role Begin Date/Time (TS) O S12.3.3.5

    rol_6 : TS | None
        ROL.6 - Role End Date/Time (TS) O S12.3.3.6

    rol_7 : CE | None
        ROL.7 - Role Duration (CE) O S12.3.3.7

    rol_8 : CE | None
        ROL.8 - Role Action (Assumption) Reason (CE) O S12.3.3.8
    """

    rol_1: EI = Field(
        validation_alias=AliasChoices(
            "rol_1",
            "role_instance_id",
            "ROL.1",
        ),
        serialization_alias="ROL.1",
        title="Role Instance ID",
        description="R | Item #01206",
    )

    rol_2: str = Field(
        validation_alias=AliasChoices(
            "rol_2",
            "action_code",
            "ROL.2",
        ),
        serialization_alias="ROL.2",
        title="Action Code",
        description="R | Item #00816 | Table 0287 - Action Code | LEN:2",
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
        description="O | Item #01197",
    )

    rol_4: XCN = Field(
        validation_alias=AliasChoices(
            "rol_4",
            "role_person",
            "ROL.4",
        ),
        serialization_alias="ROL.4",
        title="Role Person",
        description="R | Item #01198",
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
        description="O | Item #01199",
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
        description="O | Item #01200",
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
        description="O | Item #01201",
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
        description="O | Item #01205",
    )

    model_config = {"populate_by_name": True}
