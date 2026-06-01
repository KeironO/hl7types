"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: ROL
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator

from ..datatypes.CWE import CWE
from ..datatypes.EI import EI
from ..datatypes.PL import PL
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

    rol_3 : CWE
        ROL.3 (req) - Role-ROL (CWE)

    rol_4 : list[XCN] | None
        ROL.4 (req, rep) - Role Person (XCN) [optional: XCN has no required components]

    rol_5 : str | None
        ROL.5 (opt) - Role Begin Date/Time (DTM)

    rol_6 : str | None
        ROL.6 (opt) - Role End Date/Time (DTM)

    rol_7 : CWE | None
        ROL.7 (opt) - Role Duration (CWE)

    rol_8 : CWE | None
        ROL.8 (opt) - Role Action Reason (CWE)

    rol_9 : list[CWE] | None
        ROL.9 (opt, rep) - Provider Type (CWE)

    rol_10 : CWE | None
        ROL.10 (opt) - Organization Unit Type (CWE)

    rol_11 : list[XAD] | None
        ROL.11 (opt, rep) - Office/Home Address/Birthplace (XAD)

    rol_12 : list[XTN] | None
        ROL.12 (opt, rep) - Phone (XTN)

    rol_13 : PL | None
        ROL.13 (opt) - Person's Location (PL)
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

    rol_5: Optional[str] = Field(
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

    rol_6: Optional[str] = Field(
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

    rol_7: Optional[CWE] = Field(
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

    rol_8: Optional[CWE] = Field(
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

    rol_9: Optional[List[CWE]] = Field(
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

    rol_10: Optional[CWE] = Field(
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

    rol_13: Optional[PL] = Field(
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

    @field_validator("rol_5", "rol_6", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 datetime")
        return v

    model_config = {"populate_by_name": True}
