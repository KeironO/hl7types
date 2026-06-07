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
    """HL7 v2 ROL segment.

    Attributes
    ----------
    rol_1 : EI | None
        ROL.1 (opt) - Role Instance ID (EI)

    rol_2 : str
        ROL.2 (req) - Action Code (ID)

    rol_3 : CE
        ROL.3 (req) - Role-ROL (CE)

    rol_4 : list[XCN] | None
        ROL.4 (req, rep) - Role Person (XCN) [optional: XCN has no required components]

    rol_5 : TS | None
        ROL.5 (opt) - Role Begin Date/Time (TS)

    rol_6 : TS | None
        ROL.6 (opt) - Role End Date/Time (TS)

    rol_7 : CE | None
        ROL.7 (opt) - Role Duration (CE)

    rol_8 : CE | None
        ROL.8 (opt) - Role Action Reason (CE)

    rol_9 : list[CE] | None
        ROL.9 (opt, rep) - Provider Type (CE)

    rol_10 : CE | None
        ROL.10 (opt) - Organization Unit Type (CE)

    rol_11 : list[XAD] | None
        ROL.11 (opt, rep) - Office/Home Address/Birthplace (XAD)

    rol_12 : list[XTN] | None
        ROL.12 (opt, rep) - Phone (XTN)
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
        description="Item #1206",
    )

    rol_2: str = Field(
        validation_alias=AliasChoices(
            "rol_2",
            "action_code",
            "ROL.2",
        ),
        serialization_alias="ROL.2",
        title="Action Code",
        description="Item #816 | Table HL70287",
    )

    rol_3: CE = Field(
        validation_alias=AliasChoices(
            "rol_3",
            "role_rol",
            "ROL.3",
        ),
        serialization_alias="ROL.3",
        title="Role-ROL",
        description="Item #1197 | Table HL70443",
    )

    rol_4: Optional[List[XCN]] = Field(
        default=None,
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
            "role_action_reason",
            "ROL.8",
        ),
        serialization_alias="ROL.8",
        title="Role Action Reason",
        description="Item #1205",
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
        description="Item #1510",
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
        description="Item #1461 | Table HL70406",
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
        description="Item #679",
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
        description="Item #678",
    )

    model_config = {"populate_by_name": True}
