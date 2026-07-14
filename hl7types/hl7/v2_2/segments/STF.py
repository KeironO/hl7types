"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: STF
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.AD import AD
from ..datatypes.CE import CE
from ..datatypes.PN import PN
from ..datatypes.TS import TS


class STF(HL7Model):
    """staff identification segment (S9.1.1).

    Attributes
    ----------
    stf_1 : CE
        STF.1 (req) - STF - primary key value (CE) S9.1.1.1

    stf_2 : list[CE] | None
        STF.2 (opt, rep) - Staff ID Code (CE) S9.1.1.2

    stf_3 : PN | None
        STF.3 (opt) - Staff Name (PN) S9.1.1.3

    stf_4 : list[str] | None
        STF.4 (opt, rep) - Staff Type (ID) S9.1.1.4 | 0182 - Staff Type

    stf_5 : str | None
        STF.5 (opt) - Sex (ID) S3.3.2.8 | 0001 - SEX

    stf_6 : TS | None
        STF.6 (opt) - Date of Birth (TS) S3.3.2.7

    stf_7 : str | None
        STF.7 (opt) - Active / inactive (ID) S9.1.1.7 | 0183 - Active/Inactive

    stf_8 : list[CE] | None
        STF.8 (opt, rep) - Department (CE) S9.1.1.8 | 0184 - Department

    stf_9 : list[CE] | None
        STF.9 (opt, rep) - Service (CE) S9.1.1.9

    stf_10 : list[str] | None
        STF.10 (opt, rep) - Phone (TN) S9.1.1.10

    stf_11 : list[AD] | None
        STF.11 (opt, rep) - Office / home address (AD) S9.1.1.11

    stf_12 : list[str] | None
        STF.12 (opt, rep) - Activation Date (CM) S9.1.1.12

    stf_13 : list[str] | None
        STF.13 (opt, rep) - Inactivation Date (CM) S9.1.1.13

    stf_14 : list[CE] | None
        STF.14 (opt, rep) - Backup Person ID (CE) S9.1.1.14

    stf_15 : list[str] | None
        STF.15 (opt, rep) - E-mail Address (ST) S9.1.1.15

    stf_16 : str | None
        STF.16 (opt) - Preferred method of Contact (ID) S9.1.1.16 | 0185 - Preferred Method Of Contrct
    """

    stf_1: CE = Field(
        validation_alias=AliasChoices(
            "stf_1",
            "stf_primary_key_value",
            "STF.1",
        ),
        serialization_alias="STF.1",
        title="STF - primary key value",
        description="Item #671",
    )

    stf_2: Optional[List[CE]] = Field(
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

    stf_3: Optional[PN] = Field(
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

    stf_4: Optional[List[str]] = Field(
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

    stf_5: Optional[str] = Field(
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

    stf_6: Optional[TS] = Field(
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

    stf_7: Optional[str] = Field(
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

    stf_8: Optional[List[CE]] = Field(
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

    stf_9: Optional[List[CE]] = Field(
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

    stf_10: Optional[List[str]] = Field(
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

    stf_11: Optional[List[AD]] = Field(
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

    stf_12: Optional[List[str]] = Field(
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

    stf_13: Optional[List[str]] = Field(
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

    stf_14: Optional[List[CE]] = Field(
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

    stf_15: Optional[List[str]] = Field(
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

    stf_16: Optional[str] = Field(
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
