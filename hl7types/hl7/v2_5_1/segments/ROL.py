"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: ROL
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.EI import EI
from ..datatypes.TS import TS
from ..datatypes.XAD import XAD
from ..datatypes.XCN import XCN
from ..datatypes.XTN import XTN


class ROL(HL7Model):
    """Role (S15.4.7).

    Attributes
    ----------
    rol_1 : EI | None
        ROL.1 - Role Instance ID (EI) C S15.4.7.1

    rol_2 : str
        ROL.2 - Action Code (ID) R S12.4.1.1 | 0287 - Problem/goal action code

    rol_3 : CE
        ROL.3 - Role-ROL (CE) R S15.4.7.3 | 0443 - Provider role

    rol_4 : list[XCN]
        ROL.4 - Role Person (XCN) R rep S15.4.7.4

    rol_5 : TS | None
        ROL.5 - Role Begin Date/Time (TS) O S15.4.7.5

    rol_6 : TS | None
        ROL.6 - Role End Date/Time (TS) O S15.4.7.6

    rol_7 : CE | None
        ROL.7 - Role Duration (CE) O S15.4.7.7

    rol_8 : CE | None
        ROL.8 - Role Action Reason (CE) O S15.4.7.8

    rol_9 : list[CE] | None
        ROL.9 - Provider Type (CE) O rep S15.4.7.9

    rol_10 : CE | None
        ROL.10 - Organization Unit Type (CE) O S15.4.7.10 | 0406 - Organization unit type

    rol_11 : list[XAD] | None
        ROL.11 - Office/Home Address/Birthplace (XAD) O rep S15.4.7.11

    rol_12 : list[XTN] | None
        ROL.12 - Phone (XTN) O rep S15.4.7.12
    """

    rol_1: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rol_1",
            "role_instance_id",
            "ROL.1",
        ),
        serialization_alias="ROL.1",
        title="Role Instance ID",
        description="C | Item #01206",
    )

    rol_2: str = Field(
        validation_alias=AliasChoices(
            "rol_2",
            "action_code",
            "ROL.2",
        ),
        serialization_alias="ROL.2",
        title="Action Code",
        description=(
            "R | Item #00816 | Table 0287 - Problem/goal action code | LEN:2"
        ),
    )

    rol_3: CE = Field(
        validation_alias=AliasChoices(
            "rol_3",
            "role_rol",
            "ROL.3",
        ),
        serialization_alias="ROL.3",
        title="Role-ROL",
        description="R | Item #01197 | Table 0443 - Provider role",
    )

    rol_4: List[XCN] = Field(
        min_length=1,
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
            "role_action_reason",
            "ROL.8",
        ),
        serialization_alias="ROL.8",
        title="Role Action Reason",
        description="O | Item #01205",
    )

    rol_9: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rol_9",
            "provider_type",
            "ROL.9",
        ),
        serialization_alias="ROL.9",
        title="Provider Type",
        description="O | Item #01510",
    )

    rol_10: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rol_10",
            "organization_unit_type",
            "ROL.10",
        ),
        serialization_alias="ROL.10",
        title="Organization Unit Type",
        description="O | Item #01461 | Table 0406 - Organization unit type",
    )

    rol_11: Optional[List[XAD]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rol_11",
            "office_home_address_birthplace",
            "ROL.11",
        ),
        serialization_alias="ROL.11",
        title="Office/Home Address/Birthplace",
        description="O | Item #00679",
    )

    rol_12: Optional[List[XTN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rol_12",
            "phone",
            "ROL.12",
        ),
        serialization_alias="ROL.12",
        title="Phone",
        description="O | Item #00678",
    )

    model_config = {"populate_by_name": True}
