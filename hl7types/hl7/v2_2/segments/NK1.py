"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: NK1
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.AD import AD
from ..datatypes.CE import CE
from ..datatypes.PN import PN

_RE_SI = re.compile(r'\d*')
_RE_DT = re.compile(r'(\d{4}([01]\d(\d{2})?)?)?')


class NK1(HL7Model):
    """NEXT OF KIN (S3.3.5).

    Attributes
    ----------
    nk1_1 : str
        NK1.1 - Set ID - Next of Kin (SI) R S3.3.5.1

    nk1_2 : PN | None
        NK1.2 - Name (PN) NA S3.3.5.2

    nk1_3 : CE | None
        NK1.3 - Relationship (CE) NA S3.3.5.3 | 0063 - RELATIONSHIP

    nk1_4 : AD | None
        NK1.4 - Address (AD) NA S3.3.5.4

    nk1_5 : list[str] | None
        NK1.5 - Phone Number (TN) NA rep S3.3.5.5

    nk1_6 : str | None
        NK1.6 - Business Phone Number (TN) NA S3.3.5.6

    nk1_7 : CE | None
        NK1.7 - Contact Role (CE) NA S3.3.5.7 | 0131 - CONTRACT ROLE

    nk1_8 : str | None
        NK1.8 - Start Date (DT) NA S3.3.5.8

    nk1_9 : str | None
        NK1.9 - End Date (DT) NA S3.3.5.9

    nk1_10 : str | None
        NK1.10 - Next of Kin (ST) NA S3.3.5.10

    nk1_11 : str | None
        NK1.11 - Next of kin job code / class (CM) NA S3.3.5.11

    nk1_12 : str | None
        NK1.12 - Next of Kin Employee Number (ST) NA S3.3.5.12

    nk1_13 : str | None
        NK1.13 - Organization Name (ST) NA S3.3.5.13
    """

    nk1_1: str = Field(
        validation_alias=AliasChoices(
            "nk1_1",
            "set_id_next_of_kin",
            "NK1.1",
        ),
        serialization_alias="NK1.1",
        title="Set ID - Next of Kin",
        description="R | Item #00190 | LEN:4",
    )

    nk1_2: Optional[PN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_2",
            "name",
            "NK1.2",
        ),
        serialization_alias="NK1.2",
        title="Name",
        description="NA | Item #00191",
    )

    nk1_3: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_3",
            "relationship",
            "NK1.3",
        ),
        serialization_alias="NK1.3",
        title="Relationship",
        description="NA | Item #00192 | Table 0063 - RELATIONSHIP",
    )

    nk1_4: Optional[AD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_4",
            "address",
            "NK1.4",
        ),
        serialization_alias="NK1.4",
        title="Address",
        description="NA | Item #00193",
    )

    nk1_5: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_5",
            "phone_number",
            "NK1.5",
        ),
        serialization_alias="NK1.5",
        title="Phone Number",
        description="NA | Item #00194 | LEN:40",
    )

    nk1_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_6",
            "business_phone_number",
            "NK1.6",
        ),
        serialization_alias="NK1.6",
        title="Business Phone Number",
        description="NA | Item #00195 | LEN:40",
    )

    nk1_7: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_7",
            "contact_role",
            "NK1.7",
        ),
        serialization_alias="NK1.7",
        title="Contact Role",
        description="NA | Item #00196 | Table 0131 - CONTRACT ROLE",
    )

    nk1_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_8",
            "start_date",
            "NK1.8",
        ),
        serialization_alias="NK1.8",
        title="Start Date",
        description="NA | Item #00197 | LEN:8",
    )

    nk1_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_9",
            "end_date",
            "NK1.9",
        ),
        serialization_alias="NK1.9",
        title="End Date",
        description="NA | Item #00198 | LEN:8",
    )

    nk1_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_10",
            "next_of_kin",
            "NK1.10",
        ),
        serialization_alias="NK1.10",
        title="Next of Kin",
        description="NA | Item #00199 | LEN:60",
    )

    nk1_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_11",
            "next_of_kin_job_code_class",
            "NK1.11",
        ),
        serialization_alias="NK1.11",
        title="Next of kin job code / class",
        description="NA | Item #00200",
    )

    nk1_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_12",
            "next_of_kin_employee_number",
            "NK1.12",
        ),
        serialization_alias="NK1.12",
        title="Next of Kin Employee Number",
        description="NA | Item #00201 | LEN:20",
    )

    nk1_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_13",
            "organization_name",
            "NK1.13",
        ),
        serialization_alias="NK1.13",
        title="Organization Name",
        description="NA | Item #00202 | LEN:60",
    )

    @field_validator("nk1_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        if not _RE_SI.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("nk1_8", "nk1_9", mode='before')
    @classmethod
    def _validate_dt(cls, v: str) -> str:
        if not _RE_DT.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    model_config = ConfigDict(populate_by_name=True)
