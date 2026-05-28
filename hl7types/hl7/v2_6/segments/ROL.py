"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: ROL
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CWE import CWE
from ..datatypes.EI import EI
from ..datatypes.PL import PL
from ..datatypes.XAD import XAD
from ..datatypes.XCN import XCN
from ..datatypes.XTN import XTN


class ROL(BaseModel):
    """HL7 v2 ROL segment."""

    rol_1: EI | None = Field(
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

    rol_3: CWE = Field(
        default=...,
        validation_alias=AliasChoices(
            "rol_3",
            "role_rol",
            "ROL.3",
        ),
        serialization_alias="ROL.3",
        title="Role-ROL",
        description="Item #1197 | Table HL70443",
    )

    rol_4: list[XCN] = Field(
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

    rol_5: str | None = Field(
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

    rol_6: str | None = Field(
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

    rol_7: CWE | None = Field(
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

    rol_8: CWE | None = Field(
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

    rol_9: list[CWE] | None = Field(
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

    rol_10: CWE | None = Field(
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

    rol_11: list[XAD] | None = Field(
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

    rol_12: list[XTN] | None = Field(
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

    rol_13: PL | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "rol_13",
            "person_s_location",
            "ROL.13",
        ),
        serialization_alias="ROL.13",
        title="Person's Location",
        description="Item #2183",
    )

    model_config = {"populate_by_name": True}
