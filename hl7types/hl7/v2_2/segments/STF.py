"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: STF
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.AD import AD
from ..datatypes.CE import CE
from ..datatypes.PN import PN
from ..datatypes.TS import TS


class STF(BaseModel):
    """HL7 v2 STF segment."""

    stf_1: CE = Field(
        default=...,
        validation_alias=AliasChoices(
            "stf_1",
            "stf_primary_key_value",
            "STF.1",
        ),
        serialization_alias="STF.1",
        title="STF - primary key value",
        description="Item #671",
    )

    stf_2: list[CE] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_2",
            "staff_id_code",
            "STF.2",
        ),
        serialization_alias="STF.2",
        title="Staff ID Code",
        description="Item #672",
    )

    stf_3: PN | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_3",
            "staff_name",
            "STF.3",
        ),
        serialization_alias="STF.3",
        title="Staff Name",
        description="Item #673",
    )

    stf_4: list[str] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_4",
            "staff_type",
            "STF.4",
        ),
        serialization_alias="STF.4",
        title="Staff Type",
        description="Item #674 | Table HL70182",
    )

    stf_5: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_5",
            "sex",
            "STF.5",
        ),
        serialization_alias="STF.5",
        title="Sex",
        description="Item #111 | Table HL70001",
    )

    stf_6: TS | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_6",
            "date_of_birth",
            "STF.6",
        ),
        serialization_alias="STF.6",
        title="Date of Birth",
        description="Item #110",
    )

    stf_7: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_7",
            "active_inactive",
            "STF.7",
        ),
        serialization_alias="STF.7",
        title="Active / inactive",
        description="Item #675 | Table HL70183",
    )

    stf_8: list[CE] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_8",
            "department",
            "STF.8",
        ),
        serialization_alias="STF.8",
        title="Department",
        description="Item #676 | Table HL70184",
    )

    stf_9: list[CE] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_9",
            "service",
            "STF.9",
        ),
        serialization_alias="STF.9",
        title="Service",
        description="Item #677",
    )

    stf_10: list[str] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_10",
            "phone",
            "STF.10",
        ),
        serialization_alias="STF.10",
        title="Phone",
        description="Item #678",
    )

    stf_11: list[AD] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_11",
            "office_home_address",
            "STF.11",
        ),
        serialization_alias="STF.11",
        title="Office / home address",
        description="Item #679",
    )

    stf_12: list[str] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_12",
            "activation_date",
            "STF.12",
        ),
        serialization_alias="STF.12",
        title="Activation Date",
        description="Item #680",
    )

    stf_13: list[str] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_13",
            "inactivation_date",
            "STF.13",
        ),
        serialization_alias="STF.13",
        title="Inactivation Date",
        description="Item #681",
    )

    stf_14: list[CE] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_14",
            "backup_person_id",
            "STF.14",
        ),
        serialization_alias="STF.14",
        title="Backup Person ID",
        description="Item #682",
    )

    stf_15: list[str] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_15",
            "e_mail_address",
            "STF.15",
        ),
        serialization_alias="STF.15",
        title="E-mail Address",
        description="Item #683",
    )

    stf_16: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_16",
            "preferred_method_of_contact",
            "STF.16",
        ),
        serialization_alias="STF.16",
        title="Preferred method of Contact",
        description="Item #684 | Table HL70185",
    )

    model_config = {"populate_by_name": True}
