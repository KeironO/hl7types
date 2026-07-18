"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: PID
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, ValidationInfo, field_validator
from hl7types.hl7 import HL7Model
from hl7types.hl7._validators import _apply_dt_fallback

from ..datatypes.CWE import CWE
from ..datatypes.CX import CX
from ..datatypes.HD import HD
from ..datatypes.XAD import XAD
from ..datatypes.XPN import XPN
from ..datatypes.XTN import XTN

_RE_SI = re.compile(r'\d*')
_RE_DTM = re.compile(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?')
_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class PID(HL7Model):
    """Patient Identification (S3.4.2).

    Attributes
    ----------
    pid_1 : str | None
        PID.1 - Set ID - PID (SI) O S2.B.8.3.1

    pid_3 : list[CX]
        PID.3 - Patient Identifier List (CX) R rep S17.7.4.33

    pid_5 : list[XPN]
        PID.5 - Patient Name (XPN) R rep S2.B.8.3.5 | 0200 - Name Type

    pid_6 : list[XPN] | None
        PID.6 - Mother's Maiden Name (XPN) O rep S2.B.8.3.6

    pid_7 : str | None
        PID.7 - Date/Time of Birth (DTM) O S15.4.8.6

    pid_8 : CWE | None
        PID.8 - Administrative Sex (CWE) O S15.4.8.5 | 0001 - Administrative Sex

    pid_10 : list[CWE] | None
        PID.10 - Race (CWE) O rep S15.4.8.27 | 0005 - Race

    pid_11 : list[XAD] | None
        PID.11 - Patient Address (XAD) O rep S2.B.8.3.11

    pid_13 : list[XTN] | None
        PID.13 - Phone Number - Home (XTN) O rep S2.B.8.3.13

    pid_14 : list[XTN] | None
        PID.14 - Phone Number - Business (XTN) O rep S2.B.8.3.14

    pid_15 : CWE | None
        PID.15 - Primary Language (CWE) O S2.B.8.3.15 | 0296 - Primary Language

    pid_16 : CWE | None
        PID.16 - Marital Status (CWE) O S15.4.8.17 | 0002 - Marital Status

    pid_17 : CWE | None
        PID.17 - Religion (CWE) O S15.4.8.40 | 0006 - Religion

    pid_18 : CX | None
        PID.18 - Patient Account Number (CX) O S2.B.8.3.18

    pid_21 : list[CX] | None
        PID.21 - Mother's Identifier (CX) O rep S2.B.8.3.21

    pid_22 : list[CWE] | None
        PID.22 - Ethnic Group (CWE) O rep S15.4.8.28 | 0189 - Ethnic Group

    pid_23 : str | None
        PID.23 - Birth Place (ST) O S2.B.8.3.23

    pid_24 : str | None
        PID.24 - Multiple Birth Indicator (ID) O S2.B.8.3.24 | 0136 - Yes/no Indicator

    pid_25 : str | None
        PID.25 - Birth Order (NM) O S2.B.8.3.25

    pid_26 : list[CWE] | None
        PID.26 - Citizenship (CWE) O rep S15.4.8.30 | 0171 - Citizenship

    pid_27 : CWE | None
        PID.27 - Veterans Military Status (CWE) O S2.B.8.3.27 | 0172 - Veterans Military Status

    pid_29 : str | None
        PID.29 - Patient Death Date and Time (DTM) O S2.B.8.3.29

    pid_30 : str | None
        PID.30 - Patient Death Indicator (ID) O S2.B.8.3.30 | 0136 - Yes/no Indicator

    pid_31 : str | None
        PID.31 - Identity Unknown Indicator (ID) O S2.B.8.3.31 | 0136 - Yes/no Indicator

    pid_32 : list[CWE] | None
        PID.32 - Identity Reliability Code (CWE) O rep S2.B.8.3.32 | 0445 - Identity Reliability Code

    pid_33 : str | None
        PID.33 - Last Update Date/Time (DTM) O S2.B.8.3.33

    pid_34 : HD | None
        PID.34 - Last Update Facility (HD) O S2.B.8.3.34

    pid_35 : CWE | None
        PID.35 - Taxonomic Classification Code (CWE) O S3.4.2.35

    pid_36 : CWE | None
        PID.36 - Breed Code (CWE) O S2.B.8.3.36 | 0447 - Breed Code

    pid_37 : str | None
        PID.37 - Strain (ST) O S2.B.8.3.37

    pid_38 : list[CWE] | None
        PID.38 - Production Class Code (CWE) O rep S2.B.8.3.38 | 0429 - Production Class Code

    pid_39 : list[CWE] | None
        PID.39 - Tribal Citizenship (CWE) O rep S2.B.8.3.39 | 0171 - Citizenship

    pid_40 : list[XTN] | None
        PID.40 - Patient Telecommunication Information (XTN) O rep S2.B.8.3.40
    """

    pid_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_1",
            "set_id_pid",
            "PID.1",
        ),
        serialization_alias="PID.1",
        title="Set ID - PID",
        description="O | Item #00104 | LEN:4",
    )

    pid_3: List[CX] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "pid_3",
            "patient_identifier_list",
            "PID.3",
        ),
        serialization_alias="PID.3",
        title="Patient Identifier List",
        description="R | Item #00106",
    )

    pid_5: List[XPN] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "pid_5",
            "patient_name",
            "PID.5",
        ),
        serialization_alias="PID.5",
        title="Patient Name",
        description="R | Item #00108 | Table 0200 - Name Type",
    )

    pid_6: Optional[List[XPN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_6",
            "mother_s_maiden_name",
            "PID.6",
        ),
        serialization_alias="PID.6",
        title="Mother's Maiden Name",
        description="O | Item #00109",
    )

    pid_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_7",
            "date_time_of_birth",
            "PID.7",
        ),
        serialization_alias="PID.7",
        title="Date/Time of Birth",
        description="O | Item #00110",
    )

    pid_8: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_8",
            "administrative_sex",
            "PID.8",
        ),
        serialization_alias="PID.8",
        title="Administrative Sex",
        description="O | Item #00111 | Table 0001 - Administrative Sex",
    )

    pid_10: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_10",
            "race",
            "PID.10",
        ),
        serialization_alias="PID.10",
        title="Race",
        description="O | Item #00113 | Table 0005 - Race",
    )

    pid_11: Optional[List[XAD]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_11",
            "patient_address",
            "PID.11",
        ),
        serialization_alias="PID.11",
        title="Patient Address",
        description="O | Item #00114",
    )

    pid_13: Optional[List[XTN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_13",
            "phone_number_home",
            "PID.13",
        ),
        serialization_alias="PID.13",
        title="Phone Number - Home",
        description="O | Item #00116",
    )

    pid_14: Optional[List[XTN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_14",
            "phone_number_business",
            "PID.14",
        ),
        serialization_alias="PID.14",
        title="Phone Number - Business",
        description="O | Item #00117",
    )

    pid_15: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_15",
            "primary_language",
            "PID.15",
        ),
        serialization_alias="PID.15",
        title="Primary Language",
        description="O | Item #00118 | Table 0296 - Primary Language",
    )

    pid_16: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_16",
            "marital_status",
            "PID.16",
        ),
        serialization_alias="PID.16",
        title="Marital Status",
        description="O | Item #00119 | Table 0002 - Marital Status",
    )

    pid_17: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_17",
            "religion",
            "PID.17",
        ),
        serialization_alias="PID.17",
        title="Religion",
        description="O | Item #00120 | Table 0006 - Religion",
    )

    pid_18: Optional[CX] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_18",
            "patient_account_number",
            "PID.18",
        ),
        serialization_alias="PID.18",
        title="Patient Account Number",
        description="O | Item #00121",
    )

    pid_21: Optional[List[CX]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_21",
            "mother_s_identifier",
            "PID.21",
        ),
        serialization_alias="PID.21",
        title="Mother's Identifier",
        description="O | Item #00124",
    )

    pid_22: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_22",
            "ethnic_group",
            "PID.22",
        ),
        serialization_alias="PID.22",
        title="Ethnic Group",
        description="O | Item #00125 | Table 0189 - Ethnic Group",
    )

    pid_23: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_23",
            "birth_place",
            "PID.23",
        ),
        serialization_alias="PID.23",
        title="Birth Place",
        description="O | Item #00126",
    )

    pid_24: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_24",
            "multiple_birth_indicator",
            "PID.24",
        ),
        serialization_alias="PID.24",
        title="Multiple Birth Indicator",
        description="O | Item #00127 | Table 0136 - Yes/no Indicator | LEN:1",
    )

    pid_25: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_25",
            "birth_order",
            "PID.25",
        ),
        serialization_alias="PID.25",
        title="Birth Order",
        description="O | Item #00128",
    )

    pid_26: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_26",
            "citizenship",
            "PID.26",
        ),
        serialization_alias="PID.26",
        title="Citizenship",
        description="O | Item #00129 | Table 0171 - Citizenship",
    )

    pid_27: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_27",
            "veterans_military_status",
            "PID.27",
        ),
        serialization_alias="PID.27",
        title="Veterans Military Status",
        description="O | Item #00130 | Table 0172 - Veterans Military Status",
    )

    pid_29: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_29",
            "patient_death_date_and_time",
            "PID.29",
        ),
        serialization_alias="PID.29",
        title="Patient Death Date and Time",
        description="O | Item #00740",
    )

    pid_30: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_30",
            "patient_death_indicator",
            "PID.30",
        ),
        serialization_alias="PID.30",
        title="Patient Death Indicator",
        description="O | Item #00741 | Table 0136 - Yes/no Indicator | LEN:1",
    )

    pid_31: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_31",
            "identity_unknown_indicator",
            "PID.31",
        ),
        serialization_alias="PID.31",
        title="Identity Unknown Indicator",
        description="O | Item #01535 | Table 0136 - Yes/no Indicator | LEN:1",
    )

    pid_32: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_32",
            "identity_reliability_code",
            "PID.32",
        ),
        serialization_alias="PID.32",
        title="Identity Reliability Code",
        description="O | Item #01536 | Table 0445 - Identity Reliability Code",
    )

    pid_33: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_33",
            "last_update_date_time",
            "PID.33",
        ),
        serialization_alias="PID.33",
        title="Last Update Date/Time",
        description="O | Item #01537",
    )

    pid_34: Optional[HD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_34",
            "last_update_facility",
            "PID.34",
        ),
        serialization_alias="PID.34",
        title="Last Update Facility",
        description="O | Item #01538",
    )

    pid_35: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_35",
            "taxonomic_classification_code",
            "PID.35",
        ),
        serialization_alias="PID.35",
        title="Taxonomic Classification Code",
        description="O | Item #01539",
    )

    pid_36: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_36",
            "breed_code",
            "PID.36",
        ),
        serialization_alias="PID.36",
        title="Breed Code",
        description="O | Item #01540 | Table 0447 - Breed Code",
    )

    pid_37: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_37",
            "strain",
            "PID.37",
        ),
        serialization_alias="PID.37",
        title="Strain",
        description="O | Item #01541",
    )

    pid_38: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_38",
            "production_class_code",
            "PID.38",
        ),
        serialization_alias="PID.38",
        title="Production Class Code",
        description="O | Item #01542 | Table 0429 - Production Class Code",
    )

    pid_39: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_39",
            "tribal_citizenship",
            "PID.39",
        ),
        serialization_alias="PID.39",
        title="Tribal Citizenship",
        description="O | Item #01840 | Table 0171 - Citizenship",
    )

    pid_40: Optional[List[XTN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_40",
            "patient_telecommunication_information",
            "PID.40",
        ),
        serialization_alias="PID.40",
        title="Patient Telecommunication Information",
        description="O | Item #02289",
    )

    @field_validator("pid_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        if not _RE_SI.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("pid_7", "pid_29", "pid_33", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        if _RE_DTM.fullmatch(v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    @field_validator("pid_25", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
