"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: PEO
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CWE import CWE
from ..datatypes.FT import FT
from ..datatypes.XAD import XAD
from ..datatypes.XPN import XPN
from ..datatypes.XTN import XTN


class PEO(BaseModel):
    """HL7 v2 PEO segment.

    Attributes
    ----------
    peo_1 : list[CWE] | None
        PEO.1 (opt, rep) - Event Identifiers Used (CWE)

    peo_2 : list[CWE] | None
        PEO.2 (opt, rep) - Event Symptom/Diagnosis Code (CWE)

    peo_3 : str
        PEO.3 (req) - Event Onset Date/Time (DTM)

    peo_4 : str | None
        PEO.4 (opt) - Event Exacerbation Date/Time (DTM)

    peo_5 : str | None
        PEO.5 (opt) - Event Improved Date/Time (DTM)

    peo_6 : str | None
        PEO.6 (opt) - Event Ended Data/Time (DTM)

    peo_7 : list[XAD] | None
        PEO.7 (opt, rep) - Event Location Occurred Address (XAD)

    peo_8 : list[str] | None
        PEO.8 (opt, rep) - Event Qualification (ID)

    peo_9 : str | None
        PEO.9 (opt) - Event Serious (ID)

    peo_10 : str | None
        PEO.10 (opt) - Event Expected (ID)

    peo_11 : list[str] | None
        PEO.11 (opt, rep) - Event Outcome (ID)

    peo_12 : str | None
        PEO.12 (opt) - Patient Outcome (ID)

    peo_13 : list[FT] | None
        PEO.13 (opt, rep) - Event Description from Others (FT)

    peo_14 : list[FT] | None
        PEO.14 (opt, rep) - Event Description from Original Reporter (FT)

    peo_15 : list[FT] | None
        PEO.15 (opt, rep) - Event Description from Patient (FT)

    peo_16 : list[FT] | None
        PEO.16 (opt, rep) - Event Description from Practitioner (FT)

    peo_17 : list[FT] | None
        PEO.17 (opt, rep) - Event Description from Autopsy (FT)

    peo_18 : list[CWE] | None
        PEO.18 (opt, rep) - Cause Of Death (CWE)

    peo_19 : list[XPN] | None
        PEO.19 (opt, rep) - Primary Observer Name (XPN)

    peo_20 : list[XAD] | None
        PEO.20 (opt, rep) - Primary Observer Address (XAD)

    peo_21 : list[XTN] | None
        PEO.21 (opt, rep) - Primary Observer Telephone (XTN)

    peo_22 : str | None
        PEO.22 (opt) - Primary Observer's Qualification (ID)

    peo_23 : str | None
        PEO.23 (opt) - Confirmation Provided By (ID)

    peo_24 : str | None
        PEO.24 (opt) - Primary Observer Aware Date/Time (DTM)

    peo_25 : str | None
        PEO.25 (opt) - Primary Observer's identity May Be Divulged (ID)
    """

    peo_1: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "peo_1",
            "event_identifiers_used",
            "PEO.1",
        ),
        serialization_alias="PEO.1",
        title="Event Identifiers Used",
        description="Item #1073 | Table HL79999",
    )

    peo_2: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "peo_2",
            "event_symptom_diagnosis_code",
            "PEO.2",
        ),
        serialization_alias="PEO.2",
        title="Event Symptom/Diagnosis Code",
        description="Item #1074 | Table HL79999",
    )

    peo_3: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "peo_3",
            "event_onset_date_time",
            "PEO.3",
        ),
        serialization_alias="PEO.3",
        title="Event Onset Date/Time",
        description="Item #1075",
    )

    peo_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "peo_4",
            "event_exacerbation_date_time",
            "PEO.4",
        ),
        serialization_alias="PEO.4",
        title="Event Exacerbation Date/Time",
        description="Item #1076",
    )

    peo_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "peo_5",
            "event_improved_date_time",
            "PEO.5",
        ),
        serialization_alias="PEO.5",
        title="Event Improved Date/Time",
        description="Item #1077",
    )

    peo_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "peo_6",
            "event_ended_data_time",
            "PEO.6",
        ),
        serialization_alias="PEO.6",
        title="Event Ended Data/Time",
        description="Item #1078",
    )

    peo_7: Optional[List[XAD]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "peo_7",
            "event_location_occurred_address",
            "PEO.7",
        ),
        serialization_alias="PEO.7",
        title="Event Location Occurred Address",
        description="Item #1079",
    )

    peo_8: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "peo_8",
            "event_qualification",
            "PEO.8",
        ),
        serialization_alias="PEO.8",
        title="Event Qualification",
        description="Item #1080 | Table HL70237",
    )

    peo_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "peo_9",
            "event_serious",
            "PEO.9",
        ),
        serialization_alias="PEO.9",
        title="Event Serious",
        description="Item #1081 | Table HL70238",
    )

    peo_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "peo_10",
            "event_expected",
            "PEO.10",
        ),
        serialization_alias="PEO.10",
        title="Event Expected",
        description="Item #1082 | Table HL70239",
    )

    peo_11: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "peo_11",
            "event_outcome",
            "PEO.11",
        ),
        serialization_alias="PEO.11",
        title="Event Outcome",
        description="Item #1083 | Table HL70240",
    )

    peo_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "peo_12",
            "patient_outcome",
            "PEO.12",
        ),
        serialization_alias="PEO.12",
        title="Patient Outcome",
        description="Item #1084 | Table HL70241",
    )

    peo_13: Optional[List[FT]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "peo_13",
            "event_description_from_others",
            "PEO.13",
        ),
        serialization_alias="PEO.13",
        title="Event Description from Others",
        description="Item #1085",
    )

    peo_14: Optional[List[FT]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "peo_14",
            "event_description_from_original_reporter",
            "PEO.14",
        ),
        serialization_alias="PEO.14",
        title="Event Description from Original Reporter",
        description="Item #1086",
    )

    peo_15: Optional[List[FT]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "peo_15",
            "event_description_from_patient",
            "PEO.15",
        ),
        serialization_alias="PEO.15",
        title="Event Description from Patient",
        description="Item #1087",
    )

    peo_16: Optional[List[FT]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "peo_16",
            "event_description_from_practitioner",
            "PEO.16",
        ),
        serialization_alias="PEO.16",
        title="Event Description from Practitioner",
        description="Item #1088",
    )

    peo_17: Optional[List[FT]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "peo_17",
            "event_description_from_autopsy",
            "PEO.17",
        ),
        serialization_alias="PEO.17",
        title="Event Description from Autopsy",
        description="Item #1089",
    )

    peo_18: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "peo_18",
            "cause_of_death",
            "PEO.18",
        ),
        serialization_alias="PEO.18",
        title="Cause Of Death",
        description="Item #1090 | Table HL79999",
    )

    peo_19: Optional[List[XPN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "peo_19",
            "primary_observer_name",
            "PEO.19",
        ),
        serialization_alias="PEO.19",
        title="Primary Observer Name",
        description="Item #1091",
    )

    peo_20: Optional[List[XAD]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "peo_20",
            "primary_observer_address",
            "PEO.20",
        ),
        serialization_alias="PEO.20",
        title="Primary Observer Address",
        description="Item #1092",
    )

    peo_21: Optional[List[XTN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "peo_21",
            "primary_observer_telephone",
            "PEO.21",
        ),
        serialization_alias="PEO.21",
        title="Primary Observer Telephone",
        description="Item #1093",
    )

    peo_22: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "peo_22",
            "primary_observer_s_qualification",
            "PEO.22",
        ),
        serialization_alias="PEO.22",
        title="Primary Observer's Qualification",
        description="Item #1094 | Table HL70242",
    )

    peo_23: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "peo_23",
            "confirmation_provided_by",
            "PEO.23",
        ),
        serialization_alias="PEO.23",
        title="Confirmation Provided By",
        description="Item #1095 | Table HL70242",
    )

    peo_24: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "peo_24",
            "primary_observer_aware_date_time",
            "PEO.24",
        ),
        serialization_alias="PEO.24",
        title="Primary Observer Aware Date/Time",
        description="Item #1096",
    )

    peo_25: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "peo_25",
            "primary_observer_s_identity_may_be_divulged",
            "PEO.25",
        ),
        serialization_alias="PEO.25",
        title="Primary Observer's identity May Be Divulged",
        description="Item #1097 | Table HL70243",
    )

    model_config = {"populate_by_name": True}
