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
        STF.1 - STF - primary key value (CE) R S9.1.1.1

    stf_2 : list[CE] | None
        STF.2 - Staff ID Code (CE) NA rep S9.1.1.2

    stf_3 : PN | None
        STF.3 - Staff Name (PN) NA S9.1.1.3

    stf_4 : list[str] | None
        STF.4 - Staff Type (ID) NA rep S9.1.1.4 | 0182 - Staff Type

    stf_5 : str | None
        STF.5 - Sex (ID) NA S3.3.2.8 | 0001 - SEX

    stf_6 : TS | None
        STF.6 - Date of Birth (TS) NA S3.3.2.7

    stf_7 : str | None
        STF.7 - Active / inactive (ID) NA S9.1.1.7 | 0183 - Active/Inactive

    stf_8 : list[CE] | None
        STF.8 - Department (CE) NA rep S9.1.1.8 | 0184 - Department

    stf_9 : list[CE] | None
        STF.9 - Service (CE) NA rep S9.1.1.9

    stf_10 : list[str] | None
        STF.10 - Phone (TN) NA rep S9.1.1.10

    stf_11 : list[AD] | None
        STF.11 - Office / home address (AD) NA rep S9.1.1.11

    stf_12 : list[str] | None
        STF.12 - Activation Date (CM) NA rep S9.1.1.12

    stf_13 : list[str] | None
        STF.13 - Inactivation Date (CM) NA rep S9.1.1.13

    stf_14 : list[CE] | None
        STF.14 - Backup Person ID (CE) NA rep S9.1.1.14

    stf_15 : list[str] | None
        STF.15 - E-mail Address (ST) NA rep S9.1.1.15

    stf_16 : str | None
        STF.16 - Preferred method of Contact (ID) NA S9.1.1.16 | 0185 - Preferred Method Of Contrct
    """

    stf_1: CE = Field(
        validation_alias=AliasChoices(
            "stf_1",
            "stf_primary_key_value",
            "STF.1",
        ),
        serialization_alias="STF.1",
        title="STF - primary key value",
        description="R | Item #00671",
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
        description="NA | Item #00672",
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
        description="NA | Item #00673",
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
        description="NA | Item #00674 | Table 0182 - Staff Type | LEN:2",
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
        description="NA | Item #00111 | Table 0001 - SEX | LEN:1",
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
        description="NA | Item #00110",
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
        description="NA | Item #00675 | Table 0183 - Active/Inactive | LEN:1",
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
        description="NA | Item #00676 | Table 0184 - Department",
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
        description="NA | Item #00677",
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
        description="NA | Item #00678 | LEN:40",
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
        description="NA | Item #00679",
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
        description="NA | Item #00680",
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
        description="NA | Item #00681",
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
        description="NA | Item #00682",
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
        description="NA | Item #00683 | LEN:40",
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
        description=(
            "NA | Item #00684 | Table 0185 - Preferred Method Of Contrct | LEN:1"
        ),
    )

    model_config = {"populate_by_name": True}
